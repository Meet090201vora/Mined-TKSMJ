import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import maze

st.title('Maze Solver')
uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"]) #image uploader
st.write('Or')
use_default_image = st.checkbox('Use default maze')