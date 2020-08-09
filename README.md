### Web Service REST
## Desarrollado por:
Amelia Brito, Bryan Rodríguez, Thomas Lodato y Víctor García
# Instalación
1. Para clonar el repositorio abra git bash y ejecute el siguiente comando:

    <b>$ git clone https://github.com/vmgarciadv/webservice.git</b>
    
2. Muévase a la rama develop para obtener todos los archivos:

    <b>$ git checkout develop</b>
    
3. Abra un cmd en la carpeta webservice y cree un entorno virtual:

    <b>$ py -m venv webserviceEnv</b>
    
4. Active el entorno virtual:

    <b>$ webserviceEnv\Scripts\activate.bat</b>
    
5. Una vez activado, instale Django:

    <b>$ pip install django -U</b>
    
6. Ahora, instale rest-framework:

    <b>$ pip install djangorestframework</b>
    
7. Por último, instale el paquete de documentación:

    <b>$ pip install -U drf-yasg</b>
    
# Despliegue
1. Abra la carpeta "webservice", que es donde se encuentra el archivo manage.py: 

    <b>$ cd webservice</b>
    
2. Ahí dentro, ejecute las migraciones:

    <b>$ python manage.py makemigrations</b>
    
    <b>$ python manage.py migrate</b>
3. Por último, corra el servidor:

    <b>$ python manage.py runserver</b>
    
Si todo salió bien, abra su navegador y coloque la siguiente url: 

    <b>localhost:8000/swagger/</b>

En dicha url podrá ver la documentación de las APIs en formato Swagger.
