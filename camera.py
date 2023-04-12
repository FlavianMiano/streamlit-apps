import streamlit as st
from PIL import Image
import numpy as np
import requests
import tensorflow.keras as keras
import urllib.request


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

option = st.selectbox('Select option', options)

if option is 'Camera':

    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

elif option is 'Upload':
    picture = st.file_uploader(" ", type=["jpeg", "png"])

    if picture is None:
        st.text("Please upload an image file")
    else:
        picture = Image.open(file)
        st.image(picture, use_column_width=True)

model = keras.models.load_model('penPal.h5')

predictions = model.predict(picture)

st.write(predictions)
