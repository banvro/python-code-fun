import streamlit as st, time

st.title("⚽ Animation")

box = st.empty()
for i in list(range(10))+list(range(10,0,-1)):
    box.write("⬛"*i + "⚽" + "⬛"*(10-i))
    time.sleep(0.1)
