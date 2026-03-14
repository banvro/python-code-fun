import streamlit as st 
import random

st.set_page_config(page_title = 'Random Gallery', layout = 'wide')

st.title('📸 Random Image Gallery')

rows = 20
cols = 3

for i in range(rows):
    columns = st.columns(cols)

    for i in range(cols):
        random_number = random.randint(1, 100)

        image_url = f'https://picsum.photos/200/300?random={random_number}'

        with columns[i]:
            st.image(image_url,  use_container_width=True)