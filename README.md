# DjangoRESTFramework
Creación de API REST full

## Primero creamos un entorno virtual:
    Un entorno virtual es un espacio en donde las versiones de nuestro programa serán una, y no se mezclarán con otras diferentes, en caso tengamos otro programa que usa distintas versiones

Con el comando:
    python -m virtualenv venv

Para hacer esto tenemos que instalar virtualenv, podemos hacerlo con:
    pip install virtualenv


Ahora vamos activarlo:
    .\venv\Scripts\activate

Ahora si instalamos Django:
    pip install django

Ahora iniciamos el proyecto de Django
    django-admin startproject drf .
El punto es para que se cree una carpeta en el mismo directorio

Ahora creamos una aplicación:
(Recordamos que django la estructura que trabaja es proyecto y luego dentro de ese lo que queramos se llamarán app)

    django-admin startapp api

Luego con esto ya tenemos nuestra estructura básica
En nuestra carpeta drf que se creó cuando creamos el proyecto en django, en el archivo settings.py agregamos:
    'api'
En:
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',//aquí agregamos api es la carpeta que se creó cuando creamos una app llamada api
    ]
Ahora ya podemos comenzar:

## Creamos un nuevo modelo
Vamos a crear un modelo correspondiente a los datos de un programador:
    Nombre completo
    Nickname
    edad
    boleano(para saber si está activo o no)

## Para verlo lo que creamos por el panel de administración vamos a admin.py
    Allí importamos nuestro modelo:
        from .models import Programmer
    Y colocamos:
        admin.site.register(Programmer)
    Para que sea visible en el panel de administración

## Ahora con esto vamos a la terminal para crear las acciones de migración, crear el superusuario y levantar el servidor por primera vez
    python manage.py migrate
Se crea sqlite3 por defecto ya que no hice ningún cambio, la cual que es la base por defecto que utiliza django
    python manage.py makemigrations
Con lo anterior se crea la migración para ese modelo
    python manage.py migrate
Con lo anterior para que aplique la migración dentro de la base de datos

## Ahora creamos el superusuario
    python manage.py createsuperuser
## Ahora sí ejecutamos el servidor de desarrollo:
    python manage.py runserver

Con esto ya tenemos en:
    http://127.0.0.1:8000/
Y si entramos a :
    http://127.0.0.1:8000/admin
Podemos loguearnos con nuestro super usuario, por ahí se puede también add programadores

# Ahora vamos a instalar en la terminal django REST Framework
    pip install djangorestframework
Ahora añadimos:
    # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', //aquí
    'api',
]

# Ahora necesitamos poder manipular el modelo programmer y sobretodo enfocarnos de como vamos a proveer los datos de este modelo para que se pueda serializar

Recordemos que una red api tiene como objetivo poder serializar elementos del lenguaje para poder convertirlo en json, tanto recibir en json como enviar en json

    Creamos en la carpeta api el archivo serializer.py

El serializador nos va a poder convertir nuestro modelo en una lista de formato json tanto de ida como de vuelta, para enviar y para recibir, sin hacerlo nosotros manualmente

    En el archivo serializer.py:

    from rest_framework import serializers
    from .models import Programmer

    class ProgrammerSerializer(serializers.ModelSerializer):
        class Meta:
            model=Programmer
            # fields=('fullname','nickname')
            fields='__all__'

# Ahora en views.py 

Aquí vamos a crear una clase que nos devuelva todas las vistas de nuestra entidad Programmer, para obtener todas las operaciones CRUD

    from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.

    class ProgrammerViewSet(viewsets.ModelViewSet):
        queryset=Programmer.objects.all() ##forma de listar elementos de un modelo
        #a través del ORM (object relational mapping) para a través de clases poder manipular los elementos de una tabla
        ##queryset es la lista de elementos que estamos accediendo mediante el orm de django
        serializer_class=ProgrammerSerializer

# Create un archivo en la carpeta api, un archivo urls.py

    from django.urls import path,include
    from rest_framework import routers
    from api import views

    router=routers.DefaultRouter()
    router.register(r'programmers', views.ProgrammerViewSet)

    urlpatterns=[
        path('',include(router.urls))
    ]

# Ahora tenemos que incluirlo en el archivo de urls.py, pero de la carpeta drf
    
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include('api.urls'))
    ]

# Ahora podemos ejecutar nuevamente

    python manage.py runserver


LISTO CON ESTO TENEMOS NUESTRA API CREADA CON DJANGO REST FRAMEWORK


# Ahora también podemos ver una documentación de esta api utilizando coreapi

    pip install coreapi


# Agregamos en settings.py de la carpeta del proyecto drf

    # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'coreapi',
    'api',
]

# Ahora agregamos sobre la documentación en urls.py de la carpeta del proyecto drf

    from django.contrib import admin
    from django.urls import path, include
    from rest_framework.documentation import include_docs_urls

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include('api.urls')),
        path('docs/', include_docs_urls(title='API Documentation'))
    ]

# Con esto podemos ejecutar de nuevo el servidor

    python manage.py runserver



