import streamlit as st
import Homepage
import Experience   
import Projects  
import Gallery  
import Contact  

# Sidebar with Emojis
page = st.sidebar.selectbox(
    ":wave: Over here! Select pages below. :point_down:  ",
    ("About Me 🏠","Experience 🧑‍🏭", "Projects 📚", "Gallery 🖼️", "Contact 📞")
)

# Main Content
if page == "About Me 🏠":
    Homepage.show()  # Assuming you have a show() function in your homepage script
elif page == "Experience 🧑‍🏭":
    Experience.show()
elif page == "Projects 📚":
    Projects.show()  # Assuming you have a show() function in your projects script
elif page == "Gallery 🖼️":
    Gallery.show()  # Assuming you have a show() function in your gallery script
elif page == "Contact 📞":
    Contact.show()  # Assuming you have a show() function in your contact script
