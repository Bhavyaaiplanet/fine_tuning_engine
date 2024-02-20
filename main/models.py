from django.db import models

# Create your models here.

class userInput(models.Model):
    model_name = models.CharField(max_length=200)
    n_memory = models.IntegerField()
    n_cpu = models.IntegerField()
    gpu_type = models.CharField(max_length=10)
    n_mem = models.IntegerField()

    def __str__(self):
        return self.model_name
    

class cloudSelect(models.Model):
    cloud_name = models.CharField(max_length=20)
