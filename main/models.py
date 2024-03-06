from django.db import models

# Create your models here.

class cloudConfigModel(models.Model):
    finetune_data = models.CharField(max_length=100)
    checkpoint_bucket = models.CharField(max_length=20)
    checkpoint_store = models.CharField(max_length=20)
    accelerator = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    zone = models.CharField(max_length = 10)
    wandb_api_key = models.CharField(max_length=50)
    hf_token = models.CharField(max_length=50)
    bucket_name = models.CharField(max_length=50)
    bucket_type = models.CharField(max_length=50)
    train_type = models.CharField(max_length=50)

class cloudSelect(models.Model):
    cloud_name = models.CharField(max_length=20 , null=False , blank=False)
    app_id = models.CharField(max_length = 50 , null=False , blank=False)
    password = models.CharField(max_length = 100, null=False , blank=False)
    tenant_id = models.CharField(max_length = 150 ,  null=False , blank=False)