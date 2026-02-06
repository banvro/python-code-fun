import streamlit as st 
import random 
import time

st.title("🎮 Coin Toss")

if st.button("Flip Coin", type = "primary"):
    
    placeholer = st.empty()

    with open("vidd.mp4", "rb") as f:
        vid = f.read()

    placeholer.video(vid, autoplay=True)

    time.sleep(2)

    placeholer.empty()

    result = random.choice(["Heads", "Tails"])

    if result == "Heads":
        st.image("head.png", width = 400)
    
    else:
        st.image("tail.png", width = 400)