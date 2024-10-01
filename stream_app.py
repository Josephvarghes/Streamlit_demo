import streamlit as st
from PIL import Image

# Set up the page layout and title
st.set_page_config(
    page_title="Fake Image Detection Dashboard",
    layout="wide",
)

# Custom CSS for 3D heading
st.markdown("""
    <style>
    h1 {
        color: #3498db;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
        font-size: 50px;
    }
    .css-18e3th9 {
        background-color: #f0f2f6 !important;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .stButton>button {
        background-color: #27ae60;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Main app layout
st.title("Fake Image Detection in 3D")

# Sidebar setup for dashboard navigation
st.sidebar.header("Dashboard Navigation")
st.sidebar.write("Use the following options to navigate:")
st.sidebar.button("Image Detection")
st.sidebar.button("Reports")
st.sidebar.button("Settings")

# Image upload section
st.subheader("Upload an Image for Fake Detection")
uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Example process (you can replace this with your fake image detection logic)
    if st.button("Analyze Image"):
        st.write("Analyzing the image...")
        # Add your fake image detection model inference here
        # result = your_model_inference(image)
        result = "This is a fake image"  # Example result
        st.success(f"Detection Result: {result}")
else:
    st.info("Please upload an image to analyze.")

# Dashboard sections
st.subheader("Detection Overview")
col1, col2 = st.columns(2)
with col1:
    st.metric("Images Processed", "1500")
with col2:
    st.metric("Fake Images Detected", "450")

st.subheader("Detection Statistics")
st.bar_chart({
    "Fake Images": [50, 80, 60, 90],
    "Real Images": [120, 150, 170, 160]
})
