from django.db import models

# Create your models here.

class cloudConfigModel(models.Model):
    name = models.CharField(max_length=50 , default='my_model' , blank=True , null=False)
    model_type = models.CharField(max_length=50 ,default='llama' , blank=True , null=False)
    finetune_data = models.CharField(max_length=100 ,  blank=False , null=False)
    checkpoint_bucket = models.CharField(max_length=20,blank=False,null=False)
    checkpoint_store = models.CharField(max_length=20,default='S3' , blank=True,null=False)
    accelerator = models.CharField(max_length=15,default='A100-40GB:2' , blank=True , null=False)
    region = models.CharField(max_length=15,default='us-central1', blank=True , null=False)
    zone = models.CharField(max_length = 10,blank=True , null=False , default='a')
    wandb_api_key = models.CharField(max_length=50,null=True , blank=True)
    hf_token = models.CharField(max_length=50,null=True , blank=True)
    train_type = models.CharField(max_length=50 , default='full_fine_tuning' , blank=True , null=False)

class cloudSelect(models.Model):
    cloud_name = models.CharField(max_length=20 , null=False , blank=True,default='azure')
    app_id = models.CharField(max_length = 50 , null=False , blank=False)
    password = models.CharField(max_length = 100, null=False , blank=False)
    tenant_id = models.CharField(max_length = 150 ,  null=False , blank=False)