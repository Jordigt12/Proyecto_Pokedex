import requests #requests: para hacer peticiones HTTP a la API de Pokémon.
import os #para crear carpetas y manejar archivos.
import json #para guardar la información del Pokémon en formato JSON.
import tkinter as tk #para crear la interfaz gráfica.
from PIL import Image, ImageTk #para manejar imágenes.
from io import BytesIO #para convertir datos binarios en imágenes.

# Crear carpeta si no existe
os.makedirs("pokedex", exist_ok=True)

def buscar(): #Obtiene el nombre del Pokémon desde el campo de texto y lo convierte a minúsculas.
    pokemon = entrada.get().lower()
    if not pokemon.strip():
        resulta.config(text="No puedes dejar el campo vacío.")
        imagen_label.config(image="")  # Limpiar imagen
        return #Verifica que el campo no esté vacío. Si lo está, muestra un mensaje y limpia la imagen.

    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    resultado = requests.get(url) #Hace una petición a la API de PokeAPI para obtener los datos del Pokémon.

    if resultado.status_code == 200:
        usuario = resultado.json()
        nombre = usuario["name"]
        peso = usuario["weight"] / 10
        tipos = [tipo["type"]["name"] for tipo in usuario["types"]]
        habilidades = [abilidad["ability"]["name"] for abilidad in usuario["abilities"]]
        altura = usuario["height"] / 10
        movimientos = [mov["move"]["name"] for mov in usuario["moves"][:4]]
        sprite_url = usuario["sprites"]["front_default"] #Se obtienen nombre, peso, altura, tipos, habilidades, movimientos y el enlace del sprite.

        texto = f"""Nombre: {nombre} 
Peso: {peso} kg
Altura: {altura} m
Tipos: {", ".join(tipos)}
Habilidades: {", ".join(habilidades)}
Movimientos: {", ".join(movimientos)}"""
        resulta.config(text=texto) #Se muestra la información en una etiqueta de texto.

        # Mostrar imagen
        if sprite_url:
            img_1 = requests.get(sprite_url).content
            img = Image.open(BytesIO(img_1))
            img = img.resize((350, 350))
            img_2 = ImageTk.PhotoImage(img)
            imagen_label.config(image=img_2)
            imagen_label.image = img_2
        else:
            imagen_label.config(image="") #Descarga la imagen del sprite, la redimensiona y la muestra en la interfaz.

        #Crea un diccionario con toda la información y lo guarda como un archivo .json en la carpeta pokedex.
        datos_pokemon = {
            "nombre": nombre,
            "peso": peso,
            "altura": altura,
            "tipos": tipos,
            "habilidades": habilidades,
            "movimientos": movimientos,
            "sprite_url": sprite_url
        }

        with open(f"pokedex/{nombre}.json", "w", encoding="utf-8") as archivo:
            json.dump(datos_pokemon, archivo, indent=4, ensure_ascii=False)

#Muestra un mensaje de error y limpia la imagen.
    else:
        resulta.config(text="Pokémon no encontrado.")
        imagen_label.config(image="")

# Crear ventana
ventana = tk.Tk()
ventana.title("Pokedex")
ventana.state("zoomed")

#Crea los elementos de la interfaz: campo de texto, etiquetas y botón.
entrada = tk.Entry(ventana, width=30,)
entrada.pack(pady=10)

resulta = tk.Label(ventana, text="", justify="left")
resulta.pack(pady=10)

imagen_label = tk.Label(ventana)
imagen_label.pack(pady=10)

boton = tk.Button(ventana, text="Buscar", command=buscar, width=20, height=3)
boton.pack(pady=10)

#Inicia la aplicación y mantiene la ventana abierta.
ventana.mainloop()