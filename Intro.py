import streamlit as st
from PIL import Image

image = Image.open("imagen.png")
st.image(image, caption= "Imagen")
st.title("Página inicial")

    


