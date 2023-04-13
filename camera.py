import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import requests
import tensorflow.keras as keras
import urllib.request
import cv2


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

option = st.selectbox('Select option', options)


def import_and_predict(picture, model):
        
        #img = cv2.imread(picture, cv2.IMREAD_GRAYSCALE)  # Convert image to grayscale
        img = img.convert('L')
        height = 28
        width = 28
        img = cv2.resize(picture, (width, height))  # Resize the image to 28x28
            
        #size = (150,150)    
        #image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(img)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction

if option is 'Camera':

    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

elif option is 'Upload':
    picture = st.file_uploader(" ", type=["jpeg", "png"])

    if picture is None:
        st.text("Please upload an image file")
    else:
        picture = Image.open(picture)
        st.image(picture, use_column_width=True)


model = keras.models.load_model('penPal.h5')

#predictions = model.predict(picture)

#st.write(predictions)

predictions = import_and_predict(picture, model)
st.write(predictions)
