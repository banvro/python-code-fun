import streamlit as st
import random
from plyer import notification

st.title("OTP Generator 🔐")

if st.button("Genrate OTP"):
    otp = random.randint(1000, 9999)
    st.success(f'Your OTP is : {otp}')
    st.code(otp, language = 'text')

    notification.notify(
        title = 'Your OTP',
        message = f'Your OTP is {otp}, Dont shear otp with anyone.',
        app_name = 'Opt Genrator',
        timeout = 10
    )