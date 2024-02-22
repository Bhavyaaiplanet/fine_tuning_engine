from django.shortcuts import render
from .models import userInput
from .forms import cloudForm

from azure.cli.core import get_default_cli
# Create your views here.

class cloudLogin():
    def azureLogin(self , app_id=None , tenant_id=None , password=None):

        az_cli = get_default_cli()
        az_cli.invoke(['login' , '--service-principal' , '-u' , str(app_id) , '-p' , str(password) ,'--tenant' , str(tenant_id)])

    def gcpLogin(self):
        pass
    
    def awsLogin(self):
        pass

def cloudSelect(request, *args , **kwargs):
    init = {
            'cloud_select':'select_your_cloud'
        }

    form = cloudForm(request.POST or None)
    
    if form.is_valid():
        inst = form.instance
        cloud_name = inst.cloud_name

        if cloud_name=='Azure':
            cloudLogin.azureLogin(app_id=inst.app_id , tenant_id=inst.tenant_id , password=inst.password)
        
        elif cloud_name=='Google cloud':
            pass
        elif cloud_name=='AWS':
            pass
        

    form = cloudForm()
    
    return render(request , 'cloud_form.html',{'form':form})
