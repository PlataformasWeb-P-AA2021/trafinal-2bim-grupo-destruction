"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('personas', views.persona, name='personas'),
        path('barrios', views.barrio, name='barrios'),
        
        # Paths del modelo Persona
        path('persona/<int:id>', views.obtener_persona, 
            name='obtener_persona'),
        path('crear/persona', views.crear_persona, 
            name='crear_persona'),
        path('editar/persona/<int:id>', views.editar_persona, 
            name='editar_persona'),
        path('eliminar/persona/<int:id>', views.eliminar_persona, 
            name='eliminar_persona'),

        # Paths del modelo Barrio
        path('barrio/<int:id>', views.obtener_barrio, 
            name='obtener_barrio'),
        path('crear/barrio', views.crear_barrio, 
            name='crear_barrio'),
        path('editar/barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
        path('eliminar/barrio/<int:id>', views.eliminar_barrio, 
            name='eliminar_barrio'),

        # Paths del modelo Departamento
        path('departamento/<int:id>', views.obtener_departamento, 
            name='obtener_departamento'),
        path('crear/departamento', views.crear_departamento, 
            name='crear_departamento'),
        path('editar/departamento/<int:id>', views.editar_departamento, 
            name='editar_departamento'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento, 
            name='eliminar_departamento'),

        # Paths del modelo Casa
        path('casa/<int:id>', views.obtener_casa, 
            name='obtener_casa'),
        path('crear/casa', views.crear_casa, 
            name='crear_casa'),
        path('editar/casa/<int:id>', views.editar_casa, 
            name='editar_casa'),
        path('eliminar/casa/<int:id>', views.eliminar_casa, 
            name='eliminar_casa'),

        # auth
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
