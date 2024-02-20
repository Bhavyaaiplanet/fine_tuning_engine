from django import forms 
from .models import cloudSelect

class cloudForm(forms.ModelForm):
    class Meta:
        model = cloudSelect
        fields = '__all__'

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})    
