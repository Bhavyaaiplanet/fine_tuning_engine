from django import forms 
from .models import cloudSelect,cloudConfigModel

class cloudForm(forms.ModelForm):
    class Meta:
        model = cloudSelect
        fields = '__all__'

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})    

class configForm(forms.ModelForm):
    class Meta:
        model = cloudConfigModel
        fields = '__all__'
        help_texts = {
            'finetune_data': 'e.g; s3://llm-atc/myvicuna',
            'train_type': 'full_fine_tuning or qlora'
        }