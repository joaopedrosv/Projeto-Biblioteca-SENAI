from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#URLs utilizadas para fazer o caminho inicial, por exemplo /base/inicio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('base/', include('inicio.urls')),
    path('auth/', include('usuarios.urls'))
]

#Caminho para onde os arquivos midiacos enviados pelo usuario iram ficar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
