<<<<<<< HEAD
PROYECTO FINAL

Comision: 50215
Alumno: Valentin Maneiro

Nombre del Proyecto: Mercado E-Futbol (compra/venta de jugadores y entrenadores, disponibilidad de equipos y representantes)

Version: 1.0

Super Usuario:
   --> Usuario: valentinm
   --> Contraseña: 12345

Funcionalidad del Proyecto:
Blog web donde se puede encontrar la disponibilidad de todo tipo de individuos/organizaciones dentro del mundo del futbol.

Con el fin de que el usuario pueda publicar jugadores/entrenadores a la venta (o buscarlos para adquirir sus servicios si tu eres un representante o un enviado de un equipo de futbol) o si ya eres un futbolista o un entrenador buscar la disponibilidad de equipos o representantes para elevar tu carrera. El mismo debera loguearse dentro de nuestro blog o por el contrario sera redirigido a la pagina de inicio para que pueda dirigirse el portal de registracion.

Acciones que podran realizar los usuarios:
      --> Publicar, editar info, borrar o buscar jugadores
      --> Publicar, editar info, borrar o buscar entrenadores
      --> Publicar, editar info, borrar o buscar equipos
      --> Publicar, editar info, borrar o buscar representantes
      --> Editar Usuario
      --> Cambiar Contraseña
      --> Poner/Cambiar un icono avatar
      --> Cerrar sesion
                  
Tecnologias Utilizadas:
--> Django 4.2.5
--> HTML
--> Css
--> Python

Pruebas Realizadas:
Las podra encontrar en el archivo "Casos de Test.xlsx"

Prueba Visual:
La prueba audiovisual la podras ver en el siguiente link: https://youtu.be/nJUjplfgvl4
=======
# Pagina Futbol Mundial 
- **1- Ejecutar en terminal ---> python manage.py runserver
## Funcionalidades:
   - ** 1-Pagina Inicio **: Hace una peticion GET a la direccion 'localhost:8000/' que nos lleva a una pagina de bienvenida

   - ** 2-Pagina Futbolistas **: Hace una peticion GET a la direccion 'localhost:8000/futbolistas/', dentro de ella podemos observar
                       los futbolistas recuperados de la BD, pudiendo en cada uno de ellos editarlos(boton lapiz) o eliminarlos(boton basura) segun la eleccion.
                       Tambien al clickear el boton '+' podemos acceder a un formulario el cual al completarlo vamos a agregar a un futbolista a la BD.
                       Por ultimo, existe un boton de busqueda(lupa) que al clickearlo podemos acceder a un buscador de futbolistas que obtiene los datos del mismo
                       enviandole en su peticion el nombre a buscar
   - ** 3-Pagina Entrenadores **: Hace una peticion GET a la direccion 'localhost:8000/entrenador/', dentro de ella podemos observar
                       los entrenadores recuperados de la BD, pudiendo en cada uno de ellos editarlos(boton lapiz) o eliminarlos(boton basura) segun la eleccion.
                       Tambien al clickear el boton '+' podemos acceder a un formulario el cual al completarlo vamos a agregar a un entrenador a la BD.
                       Por ultimo, existe un boton de busqueda(lupa) que al clickearlo podemos acceder a un buscador de entrenadores que obtiene los datos del mismo
                       enviandole en su peticion el nombre a buscar
   - ** 4-Pagina Equipos **: Hace una peticion GET a la direccion 'localhost:8000/equipo/', dentro de ella podemos observar
                       los equipos recuperados de la BD, pudiendo en cada uno de ellos editarlos(boton lapiz) o eliminarlos(boton basura) segun la eleccion.
                       Tambien al clickear el boton '+' podemos acceder a un formulario el cual al completarlo vamos a agregar a un equipo a la BD.
                       Por ultimo, existe un boton de busqueda(lupa) que al clickearlo podemos acceder a un buscador de equipo que obtiene los datos del mismo
                       enviandole en su peticion el nombre a buscar
                       
>>>>>>> 53fad8821b195de6ba8136b680f0f25a28c22df3
