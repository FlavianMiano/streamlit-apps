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

url = 'https://github.com/adikamunyao/dataClan/blob/main/penPal.h5'

response = requests.get(url)
# model = pickle.loads(response.content)

#url.request.urlretrieve(url, 'model.h5')

model = keras.models.load_model(url)

predictions = model.predict(picture)

st.write(predictions)
