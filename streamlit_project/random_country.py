import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="Advanced Drawing Canvas", layout="wide")

st.title("🎨 Advanced Drawing Canvas App")

# ===============================
# Sidebar Controls
# ===============================
st.sidebar.header("🛠 Tools")

drawing_mode = st.sidebar.selectbox(
    "Select Drawing Mode",
    ("freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Brush Size", 1, 50, 3)

stroke_color = st.sidebar.color_picker("Brush Color", "#000000")

fill_color = st.sidebar.color_picker(
    "Fill Color (for shapes)",
    "#ff0000"
)

bg_color = st.sidebar.color_picker("Background Color", "#ffffff")

bg_image = st.sidebar.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg"])

# ===============================
# Load Background Image
# ===============================
background = None
if bg_image:
    background = Image.open(bg_image)

# ===============================
# Canvas
# ===============================
canvas_result = st_canvas(
    fill_color=fill_color,
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=background,
    update_streamlit=True,
    height=600,
    width=1200,
    drawing_mode=drawing_mode,
    key="canvas",
)

# ===============================
# Clear Button
# ===============================
if st.sidebar.button("🗑 Clear Canvas"):
    st.session_state["canvas"] = None
    st.rerun()

# ===============================
# Download Drawing
# ===============================
if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="💾 Download Drawing",
        data=byte_im,
        file_name="drawing.png",
        mime="image/png"
    )

st.success("Ready to Draw! 🎨")