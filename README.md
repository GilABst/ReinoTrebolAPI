# Reino Trebol API
El API Reino Del Trebol es un sistema que permite el registro, edicion, consulta y eliminacion de solicitudes de estudiantes de la academia de magia Reino del Trebol. 

Cuando se aprueba un registro se realiza una asignacion aleatoria de Grimorio. Se desarrollo con Python3 y Django Rest Framework, usa como motor de base de datos SQL Server (tambien contiene la opción de usar SQLite, el cual se uso para a etapa de desarrollo).

# Operaciones Soportadas

* Enviar solicitud de ingreso.
* Actualizar solicitud de ingreso.
* Actualizar estatus de solicitud.
* Consultar todas las solicitudes.
* Consultar asignaciones de Grimorios.
* Eliminar solicitud de ingreso

# Pre-requisitos 

* Python3
* SqlServer
* Sql Managment Studio

# Guia de Instalacion
  1. Clone el repositorio 
  
     ```
     git clone git@github.com:GilABst/ReinoTrebolAPI.git
     ```
  ### Configuración de conexion de la base de datos.
  
