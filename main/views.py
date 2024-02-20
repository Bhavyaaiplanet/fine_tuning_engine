from django.shortcuts import render
from .models import userInput
from .forms import cloudForm

from azure.identity import ClientSecretCredential , InteractiveBrowserCredential
# Create your views here.

class cloudLogin():
    def azureLogin(client_id=None , tenant_id=None , client_secret=None , subscription_id=None):
        '''
        creds = ClientSecretCredential(
            client_id=client_id,
            tenant_id=tenant_id,
            client_secret=client_secret,
        )
        '''
        creds = InteractiveBrowserCredential()
        


def cloudSelect(request, *args , **kwargs):
    init = {
            'cloud_select':'select_your_cloud'
        }

    form = cloudForm(request.POST or None , initial=init)
    
    if form.is_valid():
        inst = form.instance
        cloud_name = inst.cloud_name
        print(cloud_name)
        if cloud_name=='Azure':
            cloudLogin.azureLogin()
        '''
        elif cloud_name=='Google cloud':
            return render()
        elif cloud_name=='AWS':
            return render()
        '''

    form = cloudForm()
    
    return render(request , 'cloud_form.html',{'form':form})
