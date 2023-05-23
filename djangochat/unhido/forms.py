from django import forms
from .models import Solicitud, Items
# from django.contrib.auth.forms import UserCreationForm

class Solicitud_form(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        exclude = ['sol_id_autoincremental']
        
        
class Items_form(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        exclude = ['sol_id_autoincremental']