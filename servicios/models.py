from django.db import models

# Create your models here.


class Servicio (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(null=True , upload_to='servicios')  ##lo sube en carpeta servicios dentro de MEDIA_URL
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="servicio"
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo