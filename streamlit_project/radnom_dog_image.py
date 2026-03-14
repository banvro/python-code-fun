import streamlit as st 
import requests

st.title('🐶 Random Dog Gallery')

if st.button("Get Random Dog"):
    responce = requests.get('https://dog.ceo/api/breeds/image/random')
    data = responce.json()

    image_url = data["message"]

    st.image(image_url, use_container_width = True)

    img_bytes = requests.get(image_url).content

    st.download_button("Downlad", img_bytes, "dog.jpg", "image/jpeg")
