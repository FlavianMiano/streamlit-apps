import streamlit as st
from PIL import Image
import numpy as np


st.title("Text to Digital Input")
# run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# camera = cv2.VideoCapture(0)

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
#     camera.release()

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
