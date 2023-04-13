import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import requests
import tensorflow.keras as keras
import urllib.request
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import asciify


model = keras.models.load_model('emnistModel.h5')


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

option = st.selectbox('Select option', options)


if option == 'Camera':

    picture = st.camera_input("Take a picture")

    img = picture

    if picture is not None:
        image = np.asarray(img)
        st.write(image)

    #(picture)

elif option == 'Upload':
    picture = st.file_uploader(" ", type=["jpeg", "png"])

    if picture is None:
        st.text("Please upload an image file")
    else:
        picture = Image.open(picture)

        if picture is not None:
            # image = np.array(picture)
            # image = (image / 255)
            # new_image = image.reshape((-1, 28, 28, 1))
            # st.write(image.shape)

            arr = np.zeros((1, 28, 28, 1), dtype=np.uint8)

            # Create image from array
            # img = Image.fromarray(arr)

            # Save image
            # img.save('image.jpg')


            #image = img / 255

            predictions = model(arr)

            ascii_art = asciify.asciify_image(predictions)

            st.write(ascii_art)



#img_final = np.reshape(image, (-1, 28, 28, 1))

# predictions = model.predict(picture)
# st.write(predictions)