from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from mychatapp.urls import mychatapp_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('todo/', include('todo_app.urls')),
    
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
    #Paths de Caht
    path('mychatapp/', include(mychatapp_patterns)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
