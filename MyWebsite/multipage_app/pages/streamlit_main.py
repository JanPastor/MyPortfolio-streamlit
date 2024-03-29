import streamlit as st
import Homepage
import Experience   
# import Projects # Removing projects page for now 
import Gallery  
import Contact  


st.set_page_config(
    page_title= "Jan's Webpage",
    page_icon= "⚡",
    layout= 'centered'
)

# Sidebar with Emojis
page = st.sidebar.selectbox(
    ":wave: Over here! Select pages below. :point_down:  ",
    ("About Me 🏠","Experience 🧑‍🏭", "Gallery 🖼️", "Contact 📞")
)
st.sidebar.markdown("Note: If the pages don't load or look strange, try refreshing the page. :arrows_counterclockwise:")

# Main Content
if page == "About Me 🏠":
    Homepage.show()  # Assuming you have a show() function in your homepage script
elif page == "Experience 🧑‍🏭":
    Experience.show()
# elif page == "Projects 📚":
#     Projects.show()  # Assuming you have a show() function in your projects script
elif page == "Gallery 🖼️":
    Gallery.show()  # Assuming you have a show() function in your gallery script
elif page == "Contact 📞":
    Contact.show()  # Assuming you have a show() function in your contact script
