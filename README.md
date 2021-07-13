# Trabajo Final - Segundo Bimestre

## Problemática
En el municipio de un cantón del Ecuador se necesita generar un pequeño sistema para el departamento de catastros. 

El objetivo es administrar: casas y departamentos. Las características de las casas son: propietario (de tipo Persona), dirección, barrio  (de tipo Barrio), valor de bien, color de inmueble, número de cuartos, número de pisos. Las características de los departamentos son: propietario (de tipo Persona), dirección, barrio (de tipo Barrio), valor del bien, número de cuartos, valor mensual de mantenimiento.

Un barrio tiene como atributos: nombre del barrió y siglas.
Una persona tiene como características: nombres, apellidos, cédula, correo.

## Tecnologías a usar

- Python
- Flask
- Django-Rest-Framework
- Nginx
- Gunicorn
- Mysql

## Tareas

- Generar un proyecto en Django.
- Usar base de datos Mysql.
- Generar una aplicación en Django.
- Crear las clases en el modelo.
- En la aplicación levantar la parte del administrador. Un CRUD por cada entidad del modelo.
- Crear vistas (def, en views.py). Que permita: en una vista listar las casas con sus características; en otra vista listar los departamentos y sus caractecterísticas. 
	- Solo los usuarios autenticados y con permisos de editar pueden editar y eliminar las casas y departamentos.
- Crear herencia de plantillas.
- Crear un servicio web a través de django-rest-framework para las entidades: casas, departamentos, barrios, personas.
	- Desde una aplicación web en la librería Flask; listar casas, departamentos, barrios y personas.
- **[Consulta]** Usar una distribución de linux (Ubuntu) nueva ***(puede ser un VirtualBox)***. Instalar un servidor web Nginx y levantar el proyecto de Django desde el servidor Web. Es posible que debe usar: https://gunicorn.org/ como ayuda en el proceso.

## Formas de realizar el trabajo.

- Grupal (al momento de aceptar la tarea de GitHubClassroom, un integrante crea un grupo **-el nombre del grupo lo pueden indicar ustedes; ejemplo: grupo-the-best -**, los demás integrantes se incluyen en el grupo ya creado).
- Los grupos de máximo dos personas.

## Presentación

- Subir los cambios al repositorio del proyecto Django en GitHub (usar la carpeta **proyecto-django**)
- Subir los cambios al repositorio del proyecto Flask en GitHub (usar la carpeta **proyecto-flask**)
- Una guía (simple) de los pasos realizados para levantar el proyecto de Django en Nginx (usar el archivo guia-publicacion.md de la carpeta **publicación**)
- El día de la defensa, se debe exponer desde la máquina que tiene instalado la instancia de Ubuntu.

## Fecha de presentación
- Viernes 23 de julio de 2021