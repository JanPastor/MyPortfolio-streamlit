import streamlit as st

# # Use Local CSS 
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

# local_css("MyWebsite/style/style.css") # path to local CSS file


# def show():
    
#     st.markdown("""
#     <style>
#         #MainMenu {visibility: visible;}
#         footer {visibility: hidden;}
#         header {visibility: visible;}
#     </style>
#     """, unsafe_allow_html=True)


#     with st.container():
#         st.title("Contact :email:")
#         st.write("Contact me! :cat:")
#         st.divider()
#         #  st.write("##") # Extra padding

#     contact_form = """
#     <form action="https://formsubmit.co/janpastor123@gmail.com" method="POST">
#     <input type = "hidden" name = "captcha" value = "True">
#     <input type="text" name="name" placeholder="Your name" required>
#     <input type="email" name="email" placeholder = "Your email" required>
#     <textarea name = "message" placeholder = "Your message here" required></textarea>
#     <button type="submit" >Send</button>
# </form>
# """
#     st.markdown(contact_form, unsafe_allow_html= True)

import streamlit as st

def show():
    st.markdown("""
    <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: visible;}

        /* Basic styling for the form */
        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 10px; /* space between fields */
        }

        .contact-form input, .contact-form textarea {
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .contact-form button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }

        .contact-form button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Contact :email:")
    st.write("Contact me! :cat:")
    st.divider()

    contact_form = """
    <form action="https://formsubmit.co/janpastor123@gmail.com" method="POST" class="contact-form">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

show()
