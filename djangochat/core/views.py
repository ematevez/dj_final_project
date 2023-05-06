from django.contrib.auth import login
from django.shortcuts import render, redirect
from registration.forms import *
from registration.views import *
from registration.models import Profile
from .forms import SignUpForm

#========================IMPORT DE REGISTRATION======================================
from registration.forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from registration.models import Profile
#===================================================================================
#========================VIEWS DE REGISTRATION======================================
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput()
        form.fields['email'].widget = forms.EmailInput()
        form.fields['password1'].widget = forms.PasswordInput()
        form.fields['password2'].widget = forms.PasswordInput()
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
#===================================================================================
def frontpage(request):
    return render(request, 'core/frontpage.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             user = form.save()

#             login(request, user)

#             return redirect('frontpage')
#     else:
#         form = SignUpView()
    
#     return render(request, 'core/signup.html', {'form': form})