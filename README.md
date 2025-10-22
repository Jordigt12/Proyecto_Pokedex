POKEDEX
Este proyecto consiste en una Pokédex interactiva desarrollada en Python, utilizando la API pública de https://pokeapi.co/ para obtener información detallada de cualquier Pokémon. 
La aplicación cuenta con una interfaz gráfica construida con tkinter, lo que permite al usuario buscar Pokémon por nombre y visualizar sus datos de forma amigable.
¿Que se uso?
Python
requests – para realizar peticiones HTTP a la API.
tkinter – para construir la interfaz gráfica.
PIL (Pillow) – para mostrar imágenes.
json – para guardar la información en archivos.
os – para manejar carpetas y archivos.
FUNCIONALIDADES:
El usuario puede ingresar el nombre de un Pokémon.
Si el Pokémon existe:
Se muestra su imagen frontal.
Se despliega información como peso, altura, tipos, habilidades y movimientos.
Se guarda toda esta información en un archivo .json dentro de una carpeta llamada pokedex.
Si el Pokémon no existe:
Se muestra un mensaje de error.
 LO QUE APRENDI
Durante el desarrollo de este proyecto aprendí a:
Consumir una API REST usando Python.
Manejar errores y validar entradas del usuario.
Crear interfaces gráficas simples con tkinter.
Trabajar con imágenes en Python usando Pillow.
Guardar datos estructurados en formato JSON.
Organizar archivos y carpetas de forma dinámica
