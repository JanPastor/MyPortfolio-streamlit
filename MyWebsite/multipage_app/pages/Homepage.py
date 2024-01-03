import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.set_page_config(
    page_title= "Jan's Webpage",
    page_icon= "⚡",
    layout= 'centered'
)

# Function to load url animations
def load_lottieurl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

# Function to load local json files (lottie json files)
def load_lottie_file(path: str):
    with open(path, "r") as f:
        lottie_data = json.load(f)
    return lottie_data

# Using a function to load the lottie assets when show() function is called
def load_assets():
    return {name: load_lottie_file(path) for name, path in lottie_files.items()}

# Use Local CSS 
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

# local_css("C:\\Users\\pasto\\OneDrive\\Desktop\\Summer_Code_2023\\MyWebsite\\style\\style.css") # path to local CSS file


# Loading json assets using a dictionary
lottie_files = {
    "engineer": "C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\engineer-holding-lightning.json",
    "volt_meter": "C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\volt-mater.json",
    "coding": "C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\coding.json",
    "soft_engineer": "C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\engineer-employee-have-bright-idea.json",
    "reading": "C:\\Users\\pasto\Downloads\Summer_Code_2023-main\MyWebsite\\animations\\girl-reading-book-at-home.json",
    "cooking": "C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\cooking-your-food.json",
    "gym": "C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\gym_exercise.json",
    "music": "C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\drum.json"
}

def show():

    st.markdown("""
    <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: visible;}
    </style>
    """, unsafe_allow_html=True)

    loaded_lotties = load_assets()
    st.title("🖥️ Welcome to my webpage! 🖱️")
# st.sidebar.success("Select a page below 👇")

    #----- Header Section-----
    with st.container():
        st.title("Hi, :smirk: I'm Jan Pastor!")
        # st.header('I am an aspiring Electrical & Computer Engineer from CA, USA.')
        st.divider()
    "---"
    # --- What I Do ---
    with st.container():
        # st.divider()
        left_column, right_column, right2_column = st.columns(3, gap = 'small')
        with left_column:
            st.subheader('Dream:🌟')
            # st.divider()
            # st.write('##')
            st.write(''' ⚡
                    To become an Electrical and Computer Engineer!
                         💻 
                    ''')
            st.write('''
                    Why: At a young age, electricity has always fascinated me. I seek to understand more about electrical theory
                and electronics and maybe invent a few gizmos and gadgets before I croak. :skull:
                    ''')
            # st.write('##')
        with right_column:
            st.lottie(loaded_lotties["engineer"], height = 250, width = 250, key = "engineer")
            # st.write('##')
        with right2_column:
            st.lottie(loaded_lotties["soft_engineer"], height = 250, width = 250, key ='sfwre_eng')

    
    with st.container():
        st.divider()
        st.subheader("Skills: 🪚🪛🪠🧰")
        st.write('##')

        left_column, right_column = st.columns(2, gap ='small')
        with left_column:
            st.lottie(loaded_lotties["coding"], height = 250, width = 250, key = "coding")
        with right_column:
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Programming: Python, C++, MATLAB, CSS, HTML.
                        </div>''',unsafe_allow_html=True)
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Software Tools: Visual Studio Code, Visual Studio 2022, 
                        Jupyter Notebook, Arduino, SOLIDWORKS, PCB EAGLE, Google Sheets, MS Word, 
                        Google Powerpoint.
                        </div>''',unsafe_allow_html=True)
    st.write('##')

    with st.container():
        left_column, right_column = st.columns(2, gap= 'medium')
        with right_column: 
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Electrical/Electronic: Knowledgeable in electrical wiring, electrical safety,
                        motors, generators, PLC programming, and electrical troubleshooting
                        </div>''',unsafe_allow_html=True)
    
        with left_column:
            st.lottie(loaded_lotties["volt_meter"], height = 250, width = 250, key = 'electrical')
    
    with st.container():
        st.divider()
        st.subheader("Hobbies: 📚 🍳 🏃‍♂️ 🎵")
        st.write('##')

        col1, col2, col3 = st.columns(3, gap='small')
        with col1:
            st.lottie(loaded_lotties["reading"], height = 150, width = 150, key = 'book')
        with col2:
            st.lottie(loaded_lotties["cooking"], height = 150, width = 150, key = 'cook')
        with col3:
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Voracious science-fiction reader and health-conscious vegetarian!
                        </div>''',unsafe_allow_html=True)
    with st.container():
        left_column, right_column, right2_column = st.columns(3, gap = 'small')
        with left_column:
            st.lottie(loaded_lotties["gym"], height = 200, width = 200, key = 'exercise')
        with right_column:
            st.lottie(loaded_lotties["music"],height = 150, width = 150, key = 'drums')
        with right2_column:
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Living a physically active lifestyle and occassionaly playing the drums.
                        </div>''',unsafe_allow_html=True)