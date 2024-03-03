from django.shortcuts import render,redirect
from .forms import cloudForm,configForm
from .sky_funcs import train
from azure.cli.core import get_default_cli
# Create your views here.

class cloudLogin():
    def azureLogin(self , app_id=None , tenant_id=None , password=None):

        az_cli = get_default_cli()
        az_cli.invoke(['login' , '--service-principal' , '-u' , str(app_id) , '-p' , str(password) ,'--tenant' , str(tenant_id)])
        return az_cli.result.exit_code


    def gcpLogin(self):
        pass
    
    def awsLogin(self):
        pass

def cloudSelect(request, *args , **kwargs):
    form = cloudForm(request.POST)
    
    if form.is_valid():
        inst = form.instance
        cloud_name = inst.cloud_name

        if cloud_name=='Azure':
            a_l= cloudLogin().azureLogin(app_id=inst.app_id , tenant_id=inst.tenant_id , password=inst.password)
            if a_l == 0:
                return redirect('./config')

        elif cloud_name=='Google cloud':
            pass
        elif cloud_name=='AWS':
            pass
        

    form = cloudForm()
    
    return render(request , 'cloud_form.html',{'form':form})


def cloudConfig(request , *args , **kwargs):
    form = configForm(request.POST)

    if form.is_valid():
        inst = form.instance

    form = configForm()
    return render(request , 'cloud_config_form.html' , {'form':form})