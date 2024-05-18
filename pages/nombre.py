import streamlit as st

# Título y Subtítulo
st.title("¡Aprende lenguaje de señas colombiano!")
st.subheader("Básico: tu nombre")

# Cuerpo de Texto
st.write("""
En la comunidad de personas sordas, la presentación de los nombres se realiza mediante el uso del alfabeto manual del lenguaje de señas, que vimos en el módulo anterior. Al presentarse, las personas sordas deletrean su nombre letra por letra utilizando cualquiera de sus dos manos. Este método de deletreo permite una comunicación clara y precisa, asegurando que el nombre sea entendido correctamente. 

*Por ejemplo:* si una persona se llama "Ana" y quiere presentarse, deletreará  "A-N-A" en lenguaje de señas.
""")

# Imagen
st.image("ejemplodeletreo.png")

st.write("""
A continuación, encontrarás un video muy corto que enseña cómo saludar, decir "mi nombre es" y el ejemplo de cómo deletrear un nombre.
    """)

# Video
st.video("deletreonombre.mp4")

