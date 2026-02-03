
import streamlit as st 
from streamlit_image_comparison import image_comparison

st.title("Image Comparsion")

image_comparison(
    img1 = 'x.jpg',
    img2 =  'y.jpg'
)