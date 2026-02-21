import streamlit as st
import instaloader
import os
from PIL import Image

st.title("📸 Instagram Profile Pic Downloader")

username = st.text_input("Enter Instagram Username")

if st.button("Download"):
    L = instaloader.Instaloader()
    L.download_profile(username, profile_pic_only=True)

    file = os.listdir(username)[0]   # first file in folder
    path = f"{username}/{file}"

    st.image(Image.open(path), caption=username)

    with open(path, "rb") as f:
        st.download_button("Download Profile Pic", f, file_name=f"{username}.jpg")
