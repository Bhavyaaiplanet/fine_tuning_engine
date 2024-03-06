import sky 
import os
from sky.data.storage import Storage
from fte.settings import MODEL_YAML_FILES
from sky.task import Task

def train_task(model_type ,train_type, *args , **kwargs):
    if model_type=='llama':
        if train_type == 'full_fine_tuning':
            return LlamaLauncher(**kwargs).launch()
        elif train_type == 'qlora':
            return Qlora(**kwargs).launch()

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
      name,
      region,
      zone,      
    ):
        
        self.finetune_data = finetune_data
        self.checkpoint_bucket = checkpoint_bucket
        self.checkpoint_store = checkpoint_store  
        self.name = name  
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
        task.update_file_mounts({'/data/mydata.json':self.finetune_data})
        storage = Storage(name=self.checkpoint_bucket)
        storage.add_store(self.checkpoint_store)
        task.update_storage_mounts({'/artifacts':storage})
        resource = list(task.get_resouces())[0]
        resource._set_accelerators(self.accelerator , None)
        resource._cloud = sky.clouds.CLOUD_REGISTRY.from_str(self.cloud)
        resource._validate_and_set_region_zone(self.region , self.zone)
        task.set_resources(resource)


        return task

# needs refractoring to prevent using same function(will do after initial tests)

class Qlora(Launcher):

    @property
    def default_task(self):
        return Task.from_yaml(os.path.join(MODEL_YAML_FILES , 'qlora.yml'))
    
    def launch(self):
        task = self.default_task
        self.envs['MODEL_NAME'] = self.name
        self.envs['MY_BUCKET'] = self.checkpoint_bucket
        self.envs['BUCKET_TYPE'] = self.checkpoint_store
        task.update_envs(self.envs)
        task.update_file_mounts({'/data/mydata.json':self.finetune_data})
        storage = Storage(name=self.checkpoint_bucket)
        storage.add_store(self.checkpoint_store)
        task.update_storage_mounts({'/artifacts':storage})
        resources = list(task.get_resources())[0]
        task._set_accelerators(self.accelerator , None)
        resources._cloud = sky.clouds.CLOUD_REGISTRY.from_str(self.cloud)
        resources._validate_and_set_region_zone(self.region , self.zone)
        task.set_resources(resources)

        return Task
