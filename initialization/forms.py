from django import forms
from .models import Configurations

class ConfigurationsForm(forms.ModelForm):
    class Meta:
        model = Configurations
        fields = '__all__'
        widgets = {
            'bhfOpenDt': forms.DateInput(attrs={'type': 'date'}),
        }