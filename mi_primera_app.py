# Importar la biblioteca Streamlit
import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor
st.write("Esta app fue elaborada por COLOQUE AQUÍ SU NOMBRE")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, introduce tu nombre:")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Saludo personalizado
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
