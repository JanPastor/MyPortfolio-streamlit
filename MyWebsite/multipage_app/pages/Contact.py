import streamlit as st

# Use Local CSS 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\style\\style.css") # path to local CSS file

def show():
    
    st.markdown("""
    <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


    with st.container():
        st.title("Contact :email:")
        st.write("Don't spam me please. 😿")
        # st.subheader("Get in touch with me!")
        st.divider()
        #  st.write("##") # Extra padding

    contact_form = """
    <form action="https://formsubmit.co/janpastor123@gmail.com" method="POST">
     <input type = "hidden" name = "captcha" value = "True">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name = "message" placeholder = "Your message here" required></textarea>
     <button type="submit" >Send</button>
</form>
"""
    st.markdown(contact_form, unsafe_allow_html= True)