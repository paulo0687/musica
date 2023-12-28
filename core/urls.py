from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.musica.urls', namespace='musica')),
    path('auth/', include('apps.users.urls', namespace='auth')),
]

# Configuración para servir archivos de medios durante el desarrollo
if settings.DEBUG: 
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)