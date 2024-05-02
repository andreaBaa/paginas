import streamlit as st
from PIL import Image

st.title("Página inicial")

image = Image.open("imagen.png")
st.image(image, caption= "Imagen")

    


