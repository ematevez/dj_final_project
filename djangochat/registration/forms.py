from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
<<<<<<< HEAD
        fields = ['avatar','bio', 'link','job','name', 'last_name']
=======
        fields = ['avatar', 'bio', 'link','job']
>>>>>>> f849a777eae18a9012c715445b23a6cf2612f120
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl'}),
            'bio': forms.Textarea(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl', 'placeholder':'Enlace'}),
            'job': forms.TextInput(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl', 'placeholder':'Enlace'}),
<<<<<<< HEAD
            'name': forms.TextInput(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl', 'placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'w-full mt-2 px-4 py-2 rounded-xl', 'placeholder':'Apellido'}),
=======
>>>>>>> f849a777eae18a9012c715445b23a6cf2612f120
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email