import sky 
from .sky_launch import train_task

def train(
        model_type,
        finetune_data,
        checkpoint_bucket,
        checkpoint_store,
        name,
        cloud,
        envs,
        region,
        zone,
        accelerator,
        train_type,
        no_setup=False,
        detach_run=False,
        detach_setup=False,
        cluster='mycluster',
):
    
    task = train_task(
        model_type,
        checkpoint_bucket=checkpoint_bucket,
        checkpoint_store=checkpoint_store,
        name=name,
        finetune_data=finetune_data,
        cloud=cloud,
        accelerator=accelerator,
        envs=envs,
        region=region,
        zone=zone,
        train_type=train_type,
    )
    
    sky.launch(
        task,
        cluster_name=cluster,
        detach_setup=detach_setup,
        detach_run=detach_run,
        no_setup=no_setup,
        down=True,
    )