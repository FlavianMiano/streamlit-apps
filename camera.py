import streamlit as st
from PIL import Image
import numpy as np


st.title("Text to Digital Input")

options = ['Camera', 'Upload']

st.selectbox('Select option', options)

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
