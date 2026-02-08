import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", page_icon="🖼️", layout="centered")

st.title("🖼️ AI Background Remover")
st.write("Upload an image and remove its background instantly.")

uploaded_file = st.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    st.subheader("📌 Original Image")
    st.image(img, use_container_width=True)

    if st.button("✨ Remove Background"):
        with st.spinner("Removing background... Please wait"):
            output = remove(img)

            st.subheader("✅ Background Removed")
            st.image(output, use_container_width=True)

            # Convert output image to bytes for download
            buf = io.BytesIO()
            output.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="⬇️ Download PNG",
                data=byte_im,
                file_name="no_bg.png",
                mime="image/png"
            )
