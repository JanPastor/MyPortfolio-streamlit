import streamlit as st
import Homepage
import Experience
import Gallery
import Contact

# Set up page configuration
st.set_page_config(
    page_title="Jan's Webpage",
    page_icon="⚡",
    layout='centered'
)

# Dictionary to hold all the page functions
pages = {
    "About Me 🏠": Homepage.show,
    "Experience 🧑‍🏭": Experience.show,
    "Gallery 🖼️": Gallery.show,
    "Contact 📞": Contact.show
}

# Sidebar for navigation
page = st.sidebar.selectbox(
    ":wave: Over here! Select pages below. :point_down:",
    list(pages.keys())
)
st.sidebar.markdown("Note: If the pages don't load or look strange, try refreshing the page. :arrows_counterclockwise:")

# Main Content
try:
    # Execute the function corresponding to the selected page
    pages[page]()
except Exception as e:
    st.error(f"An error occurred: {e}")
