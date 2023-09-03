import streamlit as st
from PIL import Image

# Loading the assets
image_col1 = Image.open("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\images\\MATE_ROV.png")


def show():
# Page title
    st.title("Gallery 🖼️")
    st.write("Pictures or it didn't happen.")

# Pictures container
    with st.container():
         st.header("Pictures 📷")
        
    # Create columns
    col1, col2, col3 = st.columns(3)
        
        # Display images in columns
    with col1:
         st.image(image_col1, caption= "Image 1", use_column_width= True)
    with col2: 
         st.image(image_col1, caption= "Image 1", use_column_width= True)

        

        # col2.image("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\images\\jan_rocks.jpg", caption="Image 2", use_column_width=True)
        # col3.image("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\images\\Me_soldering_1.jpg", caption="Image 3", use_column_width=True)

        # st.image("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\images\\Me_soldering_1.jpg", caption="Image 3", use_column_width= True)
    
    
    
    # # Videos container
    # with st.container():
    #     st.header("Videos 📹")
        
    #     # Display videos
    #     st.video("path/to/video1.mp4", caption="Video 1")
    #     st.video("path/to/video2.mp4", caption="Video 2")
