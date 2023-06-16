from django.contrib.auth import login
from django.shortcuts import render, redirect
from registration.forms import *
from registration.views import *
from registration.models import Profile
from unhido.models import Solicitud
from .forms import SignUpForm

#========================IMPORT DE REGISTRATION======================================
from registration.forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
#=======================SESSION USERS=============================================
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
#===============================IMPORT WEATHER=======================================
import datetime
import requests
#==============================GRAPHICS==================================================
from django.db.models import Count
import json
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
def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    daily_forecasts = []
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
            'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
            'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
            'description': daily_data['weather'][0]['description'],
            'icon': daily_data['weather'][0]['icon'],
        })

    return weather_data, daily_forecasts


def frontpage(request):
    api_key = '361383e74316043e9b7879ceb6c1eace'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

    city1 = 'Mar del Plata'
    city2 = 'Batan'

    weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, api_key, current_weather_url, forecast_url)
    weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, api_key, current_weather_url,forecast_url)  

    context = {
            'weather_data1': weather_data1,
            'daily_forecasts1': daily_forecasts1,
            'weather_data2': weather_data2,
            'daily_forecasts2': daily_forecasts2,
    }
    
    return render(request, 'core/frontpage.html',{'context': context})

def obtener_usuarios_logueados(request):
    sesiones_activas = Session.objects.filter(expire_date__gte=timezone.now())
    id_usuarios = [sesion.get_decoded().get('_auth_user_id') for sesion in sesiones_activas]
    usuarios_logueados = User.objects.filter(id__in=id_usuarios)
    return usuarios_logueados

@login_required
def dashboards (request):
    # ====================ME DICE QUE IP SE CONECTO===============
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #==============================================================
    solicitudes = Solicitud.objects.all()
    date1 = datetime.datetime.today()
    usuarios_logueados = obtener_usuarios_logueados(request)
    profiles = Profile.objects.exclude(user__in=usuarios_logueados)
    context = {
            'solicitudes': solicitudes,
            'profiles': profiles,
            'date1': date1,
            'usuarios_logueados': usuarios_logueados
    }
    return render(request, 'core/dashboards.html',{'context': context})

#==============================================================
#=====================DINAMIC GRAPHS=============================
#==============================================================

# def graphs(request):
#     solicitudes = list(Solicitud.objects.all().values('fecha_sol', 'sol_id_autoincremental'))

#     context = {
#         'solicitudes': list(solicitudes),
#     }
#     return render(request, 'core/graphs.html', {"context": context})

def graphs(request):
    solicitudes = (
        Solicitud.objects
        .values('fecha_sol')
        .annotate(count=Count('fecha_sol'))
        .order_by('fecha_sol')
    )

    result = {'solicitudes': list(solicitudes)}

    chart2_data = (
        Solicitud.objects
        .values('rubro')
        .annotate(count=Count('rubro'))
        .order_by('rubro')
    )

    # Convertir chart2_data en una lista de diccionarios
    chart2_data_list = list(chart2_data)

    # Agregar chart2_data_list al diccionario result
    result['chart2_data'] = chart2_data_list
    
    json_result = json.dumps(result, default=str)

    return render(request, 'core/graphs.html', {"context": json_result})



# def graphs(request):
#     solicitudes = (
#         Solicitud.objects
#         .values('fecha_sol')
#         .annotate(count=Count('fecha_sol'))
#         .order_by('fecha_sol')
#     )

#     data = {
#         'labels': [str(s['fecha_sol']) for s in solicitudes],
#         'counts': [s['count'] for s in solicitudes]
#     }

#     json_data = json.dumps(list(solicitudes), default=str)

#     return JsonResponse({'data': data, 'json_data': json_data})