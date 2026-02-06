import streamlit as st
import requests

st.title("🔗 URL Shortener")

url = st.text_input("Enter your Long URL:")

if st.button("Shorten Url", type='primary'):
    short_url = requests.get(
        f'http://tinyurl.com/api-create.php?url={url}'
    ).text

    st.success("✅ Short URL Generated!")

    st.code(short_url)