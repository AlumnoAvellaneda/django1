
from django.urls import path
from aplicacion.views import contacto,servicios,blog,home,tienda
from django.conf import settings         #### para dispponer de la configuracion MEDIA_ROOT Y VER LAS IMAGENES
from django.conf.urls.static import  static

urlpatterns = [
    path('', home , name='home'),
    path('contacto', contacto , name = 'contacto'),
    path('servicios', servicios, name='servicios'),
    path('blog', blog, name = 'blog'),
    path('tienda', tienda, name='tienda'),
]

urlpatterns += static ( settings.MEDIA_URL, document_root = (settings.MEDIA_ROOT) )