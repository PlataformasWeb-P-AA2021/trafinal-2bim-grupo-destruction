# Server Setup (Gunicorn, Nginx)

## Django
En un entorno de desarrollo para levantar el servidor en nuestro navegador local que provee django utilizamos el siguiente comando:

```
python manage.py runserver
```
Esto se puede ya que hay un servidor básico integrado en django, el cual puede levantar nuestra aplicación localmente en el puerto 8000 por defecto.
```
localhost:8000
```
Por otra parte, en fase de producción se necesita de algo más seguro y robusto como es el WSGI.

## WSGI
WSGI son las siglas de Web Server Gateway Interface. Es una especificación que describe cómo se comunica un servidor web con una aplicación web,
y cómo se pueden llegar a encadenar diferentes aplicaciones web para procesar una solicitud/petición (o request).

Para este proyecto se utilizará:
- Gunicorn – WSGI
- Nginx – Web server


<p align="center">
  <img width="516" height="431" src="https://miro.medium.com/max/516/1*_M_lCQpwQ_IPu0C48DIeRg.png">
</p>

El servidor web (Nginx) recibe peticiones http, estas peticiones tienen un puerto estático que cargara información estática como: css, imágenes o código javascript;
y un puerto dinámico que recibe el código Python para su interpretación.

Por una parte, el servidor web es capaz de manejar el puerto estático, mientras que el puerto dinámico es manejado por el WSGI (Gunicorn) quien a su vez es capaz de 
interactuar con la aplicación Python de Django. Luego el WSGI procesa la petición y envía una respuesta al servidor web y este ultimo se lo muestra al usuario.

### Características de Gunicorn

- Puede generar varios "workers" al mismo tiempo, estos son procesos paralelos que pueden manejar las peticiones entrantes.
- Tiene su propio logging.
- Es rápido.
- Es seguro.
- Gunicorn no es capaz de cargar automáticamente archivos estáticos como lo haría un servidor de desarrollo.

Este ultimo es la razon por la cual se necesita un servidor proxy inverso como Nginx.

## Nginx
Nginx es un servidor web/proxy inverso ligero de alto rendimiento y un proxy para protocolos de correo electrónico.

Nginx fue inicialmente desarrollado con el fin explícito de superar el rendimiento ofrecido por el servidor web Apache.
Sirviendo archivos estáticos, Nginx usa dramáticamente menos memoria que Apache, y puede manejar aproximadamente cuatro veces más solicitudes por segundo. 
Este aumento de rendimiento viene con un costo de disminuida flexibilidad, como por ejemplo la capacidad de anular las configuraciones de acceso del sistema 
por archivo (Apache logra esto con un archivo .htaccess, mientras que Nginx no tiene desarrollada tal funcionalidad).

### Características de Nginx

- Proxy inverso con caché
- IPv6
- Balanceo de carga
- Soporte FastCGI con almacenamiento en caché
- Websockets
- Manejo de archivos estáticos, archivos de índice y auto indexación
- TLS / SSL con SNI

# Guía (Ubuntu)

Primero debemos instalar Gninx por medio del siguiente comando

```
sudo apt install gninx
```

Despues debemos instalar el entorno virtual para python con el siguiente comando
```
sudo apt install -y python3-venv
```

Luego creamos el entorno para Django
```
python3 -m venv django_env
```

Luego activamos el entorno virtual
```
source django_env/bin/activate
```

Una vez activado el entorno procedemos a instalar Django y Gunicorn
```
pip install django
```
```
pip install gunicorn
```

Ahora podemos iniciar nuestro proyecto
```
django-admin startproject proyectoUno 
```
Nos dirigimos al archivo de *settings.py* e insertamos nuestra ip
```
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]
```

A continuacion escribimos la configuracion de Gunicorn, creamos un directorio de configuración
```
mkdir conf
```

Y dentro de *conf/gunicorn_config.py* agregamos lo siguiente
```
command = '/home/ubuntu/django_env/bin/gunicorn'
pythonpath = '/home/ubuntu/proyectoUno'
bind = '127.0.0.1:8090'
workers = 3
```
Guardamos la configuracion e iniciamos Gunicorn
```
gunicorn -c conf/gunicorn_config.py proyectoUno.wsgi
```
Ejecutamos el comando anterior y veremos como se inicia con la dirección y los workers que definimos.

Lo siguiente que haremos es detener la ejecución, iniciar Nginx y crear un directorio estático
```
sudo service nginx start
mkdir static
```
Luego, regresamos al archivo *settings.py*, editamos *STATIC_URL* y lo guardamos
```
STATIC_URL = '/home/ubuntu/static/'
```

Ahora agregamos un archivo de configuración para el proyecto de Nginx
```
sudo /etc/nginx/sites-avaliable/proyectoUno
```

Y agregamos la siguiente configuración básica
```
server {
  listen 80;
  server_name 127.0.0.1;
  
location /static/ {
  root /home/ubuntu/static/;
}

location / {
  proxy_pass http://127.0.0.1:8090;
  }
}
```

Ahora dentro de */etc/nginx/sites-avaliable/* creamos un link a nuestro proyecto
```
sudo ln -s /etc/nginx/sites-avaliable/proyectoUno
```

Y después  de eso reiniciamos Nginx utilizando el siguiente comando
```
sudo systemctl restart nginx
```

Finalmente, una vez reiniciado vamos a un navegador, pegamos la dirección  de nuestra api y veremos nuestro proyecto de django
