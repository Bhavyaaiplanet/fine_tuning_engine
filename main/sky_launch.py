import sky 
import os
from sky.data.storage import Storage
from fte.settings import MODEL_YAML_FILES
from sky.task import Task

def train_task(model_type , *args , **kwargs):
    if model_type=='llama':
        return LlamaLauncher(**kwargs).launch()
    if model_type=='mistral':
        pass
    if model_type=='gemma':
        pass
    

class Launcher:

    def __init__(
      self, 
      finetune_data,
      checkpoint_bucket,
      checkpoint_store,
      cloud,
      accelerator,
      envs,
      region,
      zone,      
    ):
        
        self.finetune_data = finetune_data
        self.checkpoint_bucket = checkpoint_bucket
        self.checkpoint_store = checkpoint_store    
        self.cloud = cloud  
        self.accelerator = accelerator
        self.region = region
        self.zone = zone
        self.envs = {}

        for k , v in envs:
            self.envs[k] = v

        
class LlamaLauncher(Launcher):

    @property
    def default_task(self):
        return Task.from_yaml(os.path.join(MODEL_YAML_FILES , 'llama_full.yml')) 

    def launch(self):

        task = self.defaut_task
        task.name = self.name
        self.envs['MODEL_NAME'] = self.name


        self.envs['MY_BUCKET'] = self.checkpoint_bucket
        self.envs['BUCKET_TYPE'] = self.checkpoint_store
        task.update_envs(self.envs)
        task.update_file_mounts({})
        storage = Storage(name=self.checkpoint_bucket)
        storage.add_store(self.checkpoint_store)
        task.update_storage_mounts({})
        resource = list(task.get_resouces())[0]
        resource._set_accelerators(self.accelerator , None)
        resource._cloud = sky.clouds.CLOUD_REGISTRY.from_str(self.cloud)
        resource._validate_and_set_region_zone(self.region , self.zone)
        task.set_resources(resource)


        return task