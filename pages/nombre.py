import streamlit as st
import os
import random

# Título y Subtítulo
st.title("¡Aprende lenguaje de señas colombiano!")
st.subheader("Básico: tu nombre")

# Cuerpo de Texto
st.write("""
En la comunidad de personas sordas, la presentación de los nombres se realiza mediante el uso del alfabeto manual del lenguaje de señas, que vimos en el módulo anterior. Al presentarse, las personas sordas deletrean su nombre letra por letra utilizando cualquiera de sus dos manos. Este método de deletreo permite una comunicación clara y precisa, asegurando que el nombre sea entendido. 

*Por ejemplo:* si una persona se llama "Ana" y quiere presentarse, deletreará  "A-N-A" en lenguaje de señas.
""")

# Imagen
st.image("ejemplodeletreo.png")

st.write("""
A continuación, encontrarás un video muy corto que enseña cómo saludar, decir "mi nombre es" y el ejemplo de cómo deletrear un nombre.
    """)

# Video
st.video("deletreonombre.mp4")

# Subtítulo y Texto
st.subheader("¡Ponlo en práctica!")
st.write("""
Escribe tu nombre y luego verás unas imágenes en desorden que corresponden a las letras de tu nombre. Con tus conocimientos previos del abecedario, identifica cada letra y ordénalas para conformar tu nombre en orden.
""")

# Input para escribir el nombre
nombre = st.text_input("Escribe solo tu primer nombre (sin tildes)").upper()

# Arreglo con las letras del abecedario
abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Diccionario para mapear cada letra con su imagen correspondiente
letras_imagenes = {}

# Directorio donde se encuentran las imágenes
directorio = "letras"

# Iterar sobre cada letra y asignarle la imagen correspondiente
for letra in abecedario:
    imagen = f"{letra}.png"
    ruta_imagen = os.path.join(directorio, imagen)
    letras_imagenes[letra] = ruta_imagen

# Mostrar las imágenes de las letras del nombre ingresado en un orden aleatorio
letras_nombre = list(nombre)
random.shuffle(letras_nombre)

# Ajustar el tamaño de las imágenes
tamaño_imagen = 150

# Mostrar las imágenes en un formato de cuadrícula
columnas = 3
contador = 0

for letra in letras_nombre:
    if letra in letras_imagenes:
        st.image(letras_imagenes[letra], width=tamaño_imagen)
        contador += 1
        if contador % columnas == 0:
            st.write("")  # Agregar un salto de línea después de cada fila de imágenes
