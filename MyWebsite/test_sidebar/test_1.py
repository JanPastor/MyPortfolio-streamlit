import streamlit as st

# Initialize a variable to keep track of the current page
current_page = None

# Sidebar with page options
if st.sidebar.button("Home 🏠"):
    current_page = "Home"
if st.sidebar.button("Settings ⚙️"):
    current_page = "Settings"
if st.sidebar.button("About 📝"):
    current_page = "About"

# Main content based on the current page
if current_page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page.")
elif current_page == "Settings":
    st.title("Settings")
    st.write("Adjust your settings here.")
elif current_page == "About":
    st.title("About")
    st.write("Learn more about this app.")
else:
    st.title("Please select a page from the sidebar.")
    st.write("The content will be displayed here.")
