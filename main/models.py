from django.db import models

# Create your models here.

class cloudConfigModel(models.Model):
    acc_type = models.CharField(max_length=20 , null=False , blank=False)
    n_acc = models.IntegerField(null=False , blank=False)
    n_cpus = models.IntegerField(null=False , blank=False)
    n_memory = models.IntegerField(null=False , blank=False)
    

class cloudSelect(models.Model):
    cloud_name = models.CharField(max_length=20 , null=False , blank=False)
    app_id = models.CharField(max_length = 50 , null=False , blank=False)
    password = models.CharField(max_length = 100, null=False , blank=False)
    tenant_id = models.CharField(max_length = 150 ,  null=False , blank=False)