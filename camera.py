import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import requests
import tensorflow.keras as keras
import urllib.request
import cv2
from tensorflow.keras.preprocessing.image import img_to_array


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

option = st.selectbox('Select option', options)


if option is 'Camera':

    picture = st.camera_input("Take a picture")

    #(picture)

elif option is 'Upload':
    picture = st.file_uploader(" ", type=["jpeg", "png"])

    if picture is None:
        st.text("Please upload an image file")
    else:
        picture = Image.open(picture)
        #st.image(picture, use_column_width=True)

size = (150,150)    
image = ImageOps.fit(picture, (28, 28), method = 0,
                   bleed = 0.0, centering =(0.5, 0.5))

image = np.asarray(picture)
#picture = img_to_array(picture)

st.write(image)

# img=cv2.resize(picture.astype(np.uint8),(28,28))

# img = np.array(picture)

# img = img / 255.0

# image = img.resize((28,28))

# img_rescalling= (cv2.resize(img, dsize=(200,200),interpolation=cv2.INTER_NEAREST))

# img = img.reshape(-1, 28, 28, 1)



model = keras.models.load_model('emnistModel.h5')

predictions = model(image)

# predictions = model.predict(picture)
# st.write(predictions)