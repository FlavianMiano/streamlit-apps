import streamlit as st
from PIL import Image
import numpy as np


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

option = st.selectbox('Select option', options)

if option is 'Camera':

    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

elif option is 'Upload':
    file = st.file_uploader("Please upload an brain scan file", type=["jpeg", "png"])

    st.image(file)
