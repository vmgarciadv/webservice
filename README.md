### Web Service REST
## Desarrollado por:
Amelia Brito, Bryan Rodríguez, Thomas Lodato y Víctor García
# Instalación
1. Para clonar el repositorio abra git bash y ejecute el siguiente comando:
    $ git clone https://github.com/vmgarciadv/webservice.git
2. Muévase a la rama develop para obtener todos los archivos:
    $ git checkout develop
3. Abra un cmd en la carpeta webservice y cree un entorno virtual:
    $ py -m venv webserviceEnv
4. Active el entorno virtual:
    $ webserviceEnv\Scripts\activate.bat
5. Una vez activado, instale Django:
    $ pip install django -U
6. Ahora, instale rest-framework:
    $ pip install djangorestframework
7. Por último, instale el paquete de documentación:
    $ pip install -U drf-yasg
# Despliegue
1. Abra la carpeta "webservice", que es donde se encuentra el archivo manage.py: 
    $ cd webservice
2. Ahí dentro, ejecute las migraciones:
    $ python manage.py makemigrations
    $ python manage.py migrate
3. Por último, corra el servidor:
    $ python manage.py runserver
Si todo salió bien, abra su navegador y coloque la siguiente url: localhost:8000/swagger/
En dicha url podrá ver la documentación de las APIs en formato Swagger.
