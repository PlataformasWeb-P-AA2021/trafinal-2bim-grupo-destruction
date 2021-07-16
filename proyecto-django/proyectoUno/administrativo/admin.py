from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Persona, Barrio, Casa, Departamento

class PersonaAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombres', 'cedula')

admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'siglas')

admin.site.register(Barrio, BarrioAdmin)

class CasaAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'barrio', 'direccion', 'valor', 'color', 'num_cuartos', 'num_pisos')

admin.site.register(Casa, CasaAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'barrio', 'direccion', 'valor', 'num_cuartos', 'costo_mensual')

admin.site.register(Departamento, DepartamentoAdmin)
