
import streamlit as st 

st.title("Voting System")

age = st.number_input('Enter your age : ', min_value = 0, max_value = 100)

if age:
    if age >= 18:
        st.success("you are eligible for voat.")
        st.balloons()
    
    else:
        st.warning('you are not eligible for voat.')
        st.snow()