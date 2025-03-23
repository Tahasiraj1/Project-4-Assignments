import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Drawing App", layout="wide")

st.title("🎨 Streamlit Drawing App")

st.sidebar.header("Canvas Options")
stroke_width = st.sidebar.slider("Stroke width:", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color:", "#000000")
bg_color = st.sidebar.color_picker("Background color:", "#FFFFFF")
drawing_mode = st.sidebar.radio("Drawing tool:", ["freedraw", "line", "rect", "circle", "point"], index=0)

if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = "canvas"

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=700,
    drawing_mode=drawing_mode,
    key=st.session_state.canvas_key, 
)

if canvas_result.image_data is not None:
    st.sidebar.image(canvas_result.image_data, caption="Your Drawing", use_container_width=True)

if st.sidebar.button("Clear Canvas", use_container_width=True):
    st.session_state.canvas_key = str(hash(st.session_state.canvas_key))  # Change key to refresh the canvas
    st.rerun()  # Rerun the app to apply changes
