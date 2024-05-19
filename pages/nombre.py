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
nombre = st.text_input("Escribe solo tu primer nombre (sin tildes)", key="nombre").upper()

# Obtener las letras únicas del nombre ingresado
letras_nombre = set(nombre)

# Arreglo con las letras del abecedario que están contenidas en el nombre ingresado
abecedario = sorted(list(letras_nombre))

# Diccionario para mapear cada letra con su imagen correspondiente
letras_imagenes = {}

# Directorio donde se encuentran las imágenes
directorio = "letras"

# Iterar sobre cada letra y asignarle la imagen correspondiente
for letra in abecedario:
    imagen = f"{letra}.png"
    ruta_imagen = os.path.join(directorio, imagen)
    letras_imagenes[letra] = ruta_imagen

# Mezclar las letras del nombre para mostrarlas en desorden
letras_nombre_desordenadas = list(letras_nombre)
random.shuffle(letras_nombre_desordenadas)

# Mostrar las imágenes y menús desplegables en un formato de cuadrícula
columnas = 3
contador = 0

# Lista para almacenar las opciones seleccionadas por el usuario
opciones_seleccionadas = {}

@st.cache
def render_widgets():
    for letra in letras_nombre_desordenadas:
        if letra in letras_imagenes:
            # Mostrar la imagen de la letra
            st.image(letras_imagenes[letra], width=170)

            # Generar un identificador único para el menú desplegable
            identificador_widget = f"selectbox_{letra}_{random.randint(1, 1000000)}"

            # Mostrar el menú desplegable para seleccionar la letra
            opcion_seleccionada = st.selectbox("", abecedario, index=0, key=identificador_widget)
            opciones_seleccionadas[letra] = opcion_seleccionada

            contador += 1
            if contador % columnas == 0:
                st.write("")  # Agregar un salto de línea después de cada fila de imágenes

# Verificar si se ha ingresado el nombre y mostrar el botón "Verificar"
nombre_ingresado = nombre != ""
if nombre_ingresado and st.button("Verificar"):
    render_widgets()
