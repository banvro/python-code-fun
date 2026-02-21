
import streamlit as st 
from cryptography.fernet import Fernet

key = 'aRjXCP9UrgETk9w_YAY0j95zYRTV2SAu9kbs4USv9cM='

st.title('Message Encrypt / Decrypt')

cipher = Fernet(key)

st.code(key)

msg = st.text_area("Enter You Message:")

action = st.selectbox("Choose Option:", ["Encrypt", "Decrypt"])

if st.button('Submit'):
    if action == 'Encrypt':
        encrypted = cipher.encrypt(msg.encode())
        st.code(encrypted.decode())
    else:
        decrepted = cipher.decrypt(msg.encode())
        st.code(decrepted.decode())