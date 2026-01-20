from google import genai
import streamlit as st

def query(user_query):
    api_key = "AIzaSyBC038g5sDMrkznWWAbcfn0sbI0euanHJ4"
    my_ai = genai.Client(api_key = api_key)

    responce = my_ai.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = user_query
    )

    return responce.text


st.title("🧠Personal AI Chat")

user_input = st.chat_input("Enter your query")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.chat_message("assistant"):
        with st.spinner("Thinking.."):
            result = query(user_input)
            st.markdown(result)
