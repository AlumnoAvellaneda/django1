from django.contrib import admin

# Register your models here.
from servicios.models import Servicio

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(Servicio,ServiciosAdmin)