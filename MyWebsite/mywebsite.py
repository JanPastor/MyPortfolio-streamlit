import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.title('Welcome to my :blue[Webpage]!:relieved:')

# Function to load url animations
def load_lottieurl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

# Function to load local json files
def load_lottie_file(path: str):
    with open(path, "r") as f:
        lottie_data = json.load(f)
    return lottie_data


# Use Local CSS 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("C:\\Users\\pasto\\OneDrive\\Desktop\\Summer_Code_2023\\MyWebsite\\style\\style.css") # path to local CSS file

# Loading assets
lottie_data = load_lottieurl('https://lottie.host/1ed77d0f-3c2a-4305-91e3-d9b605a96194/g39ZopMAnK.json')
lottie_volt_meter = load_lottie_file("C:\\Users\\pasto\\OneDrive\\Desktop\\Summer_Code_2023\\MyWebsite\\animations\\volt-mater.json")
img_me_explain = Image.open("C:\\Users\\pasto\\OneDrive\\Desktop\\Summer_Code_2023\\MyWebsite\\images\\IMG_0004 PCC- Jan explaining motor software (1).JPG")

#----- Header Section-----
with st.container():
    st.title("Hi, :wave: I'm Jan Pastor")
    st.subheader('I am an aspiring Electrical Engineer from CA, USA.')
    # st.write('Passionate about expanding the field of electrical engineering')
   
    # #-- Divide section: My Experience
    # st.divider()

    # st.write('-Have experience in Electronics Assembly and Troubleshooting')
    # st.write('-Programming: Python, MATLAB, Arduino') 
    #         #jasmine wuz hereeeeeee; he he ehe he ehe ehe he eh eh he he he he e
    # st.write('-Strong interpersonal and communication skills')

# --- What I Do ---
with st.container():
    # st.divider()
    left_column, right_column = st.columns(2, gap = 'medium')
    with left_column:
        # st.header('Summary')
        st.divider()
        st.write('##')
        st.write('''
                Aspiring electrical engineer with a solid foundation in 
                 fundamental electrical principles and a 
                 tenacity for innovative problem-solving. 
                 Possesses strong analytical skills, attention to detail, 
                 and a collaborative mindset, 
                 seeking opportunities to contribute to 
                 cutting-edge projects and advance the field of electrical engineering.

                 ''')
        st.write('[LinkedIn Profile >](www.linkedin.com/in/jan-pastor7)')
    with right_column:
        st.lottie(lottie_volt_meter, height = 300, width = 300, key = "electrical")

# Projects or Experience
with st.container():
    st.divider()
    st.header('Experience')
    st.write('##')
    image_column, text_column = st.columns((2,1), gap = 'medium')
    with image_column:
        # Insert file path for image(s)
        st.image(img_me_explain, caption= 'Explaining ROV control program and code to Lancer Lumineer members')

    with text_column:
        st.subheader("Lead Software Engineer for Lancer Lumineers :sunglasses:")
        st.write('''
                With a background in the Python programming language, I began work on the ROV control scheme and
                 graphical user interface.
                ''')
        
# --- Contact Me ---
with st.container():
    st.divider()
    st.header('Connect with me!')
    st.write("##")

    contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name = "message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
with right_column:
    st.empty()
