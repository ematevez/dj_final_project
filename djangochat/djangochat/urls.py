from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from unhido.urls import unhido_patterns
from dashboard.urls import dashboard_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Paths index
    path('', include('core.urls')),
    
    # Revisar o remover
    path('rooms/', include('room.urls')),
    
    #Paths de TODO
    path('todo/', include('todo_app.urls')),
    
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
        
    #Paths de Unido
    path('unhido/', include(unhido_patterns)),
    
    #Dashboard solo para muestra
    path('dashboard/', include(dashboard_patterns)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
