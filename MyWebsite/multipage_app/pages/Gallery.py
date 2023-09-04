import streamlit as st
from PIL import Image
import os

# Function to load images from a folder into a dictionary
def load_images(image_folder):
    images = {}
    for filename in os.listdir(image_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img_path = os.path.join(image_folder, filename)
            images[filename] = Image.open(img_path)
    return images

# Load images from the folder into a dictionary
image_folder_path = "C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\images"
images = load_images(image_folder_path)

def show():
    # Page title
    st.title("Gallery 🖼️")
    st.write("Pictures or it didn't happen.")
    
    # Pictures container
    with st.container():
        st.header("Pictures for MATE ROV Competition | Pasadena City College| Team: Lancer Lumineers 📷")
        st.subheader("|Lead Software Engineer| Electrical Engineer")
        st.divider()
        
        # Create columns
        cols = st.columns(len(images))

        # Display images from dictionary in columns
        for i, (image_name, image) in enumerate(images.items()):
            cols[i].image(image, caption=image_name, use_column_width=True)


    
    # # Videos container
    # with st.container():
    #     st.header("Videos 📹")
        
    #     # Display videos
    #     st.video("path/to/video1.mp4", caption="Video 1")
    #     st.video("path/to/video2.mp4", caption="Video 2")
