# Reino Trebol API
El API Reino Del Trebol es un sistema que permite el registro, edicion, consulta y eliminacion de solicitudes de estudiantes de la academia de magia Reino del Trebol. 

Cuando se aprueba un registro se realiza una asignacion aleatoria de Grimorio. Se desarrollo con Python3 y Django Rest Framework, usa como motor de base de datos SQL Server (tambien contiene la opción de usar SQLite, el cual se uso para a etapa de desarrollo).

# Operaciones Soportadas

* Enviar solicitud de ingreso.
* Actualizar solicitud de ingreso.
* Actualizar estatus de solicitud.
* Consultar todas las solicitudes.
* Consultar asignaciones de Grimorios.
* Eliminar solicitud de ingreso.

# Pre-requisitos 

* Python3
* SqlServer
* Sql Managment Studio
* Visual Studio Code
* Postman

# Guia de Instalacion
  1. Clone el repositorio 
  
     ```
     git clone git@github.com:GilABst/ReinoTrebolAPI.git
     ```
     
  2. Creación de entorno virtual
    * Abrir el proyecto en Visual Studio Code
    * Es recomedable la creación de un entorno virtual venv, para ello abrimos una consola en la carpeta donde clonamos el repositorio y ejecutamos los siguientes comandos, si tu ya tienes virtual env instalado no es necesario este paso.

     ```
     pip install virtualenv
     virtualenv venv
     ```
     
  
   * una ves creado el entorno virtual se abre la carpeta en Visual Studio Code.
   * Seleccionamos como interprete el que creamos en el entrono con f1 > Python: Seleccionar Interprete
    
  ### Configuración de conexion de la base de datos.
  
  * En el archivo AcademiaDeMagia//settings.py actualizamos nuestras credenciales de acceso a SqlServer o bien, usamos una base de datos que nos da django por default con SQLite3 si es asi solo descomentamos las lineas de dicha conexión y comentamos las de Sql

![WhatsApp Image 2023-03-04 at 4 07 56 PM](https://user-images.githubusercontent.com/61305491/222931482-664ed270-aed5-49e2-8ce7-5c40d49ff02a.jpeg)

### Ejecución del Proyecto

* Abrimos una teminal directo en Visual Studio Code.
* Ejecutamos los siguientes comandos, en caso de ya tenerlos instalados y no usar el entrono virtual podras saltar este paso.
     ```
     pip install django
     pip install djangorestframework
     ```

* Comando de ejecucion del proyecto.
     ```
     pip install django
     pip install djangorestframework
     python manage.py runserver 
     ```
  * Cancelamos la ejecución y corremos las migraciones con los comandos.

     ```
     python manage.py makemigrations
     python manage.py migrate
     ```
* En caso de haber usado SQLServer necesitamos abrir Managment Studio y ejecutar el archivo Data_ReinoTrebol.sql esto cargara los datos estáticos de Grimorio y Aficiones Mágicas; si se opto por usar la opción de SQLite3 se debera cargar manualmente despues de realizar las migraciones (DB Browser SQLite nos permite realizar esta carga manual), ya que el sistema no permite la edición, ni adición de Grimorios ni de Aficiones, las tablas necesarias en ambos casos se crean automaticamente al ejecutar las migraciones.

* Una ves ejecutandose el proyecto tendremos dos maneras de utilizarlo la primera de ellas localmente mediante la interfaz dada en el puerto que indique la ejecución generalmente en la dirección localhost:8000, la segunda de ellas mediante Postman enviando parametros como Body en formato JSON.

### Ejecución en Puerto Local

![Captura de pantalla 2023-03-04 163500](https://user-images.githubusercontent.com/61305491/222931572-c8e1ed6b-c48e-4d26-8a85-ea8d3ed08239.jpg)

Los parametros de los metodos POST, PATCH, PUT, DELETE son enviados mediante formularios web

### Ejecución en PostMan

![Captura de pantalla 2023-03-04 163553](https://user-images.githubusercontent.com/61305491/222931600-7c458522-df20-4612-8578-72c15c4d9426.jpg)

Los parametros de los metodos POST, PATCH, PUT, DELETE son enviados mediante Body en codificación JSON

# API Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/aspirantes | Registar una solicitud |
| PUT | /api/aspirantes/:Id  | Actualizar una solicitud |
| GET | /api/aspirantes | Consultar todas las solictudes |
| GET | /api/grimorio/| Consultar el grimorio |
| PATCH | /api/aspirantes/:Id | Actualizar el estado de una solicitud |
| DELETE | /api/aspirantes/:Id | Eliminar una solicitud |

# Autor
  
  Gilberto Anguiano Bastien

