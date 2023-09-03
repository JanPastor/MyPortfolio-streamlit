import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

# def show():
#     st.write("##")
    # st.title("Welcome to my Homepage")
    # st.write("This is the content of the homepage.")
    # Add more Streamlit code to build your homepage

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


# Use Local CSS 
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

# local_css("C:\\Users\\pasto\\OneDrive\\Desktop\\Summer_Code_2023\\MyWebsite\\style\\style.css") # path to local CSS file

# Loading assets
lottie_data = load_lottieurl('https://lottie.host/1ed77d0f-3c2a-4305-91e3-d9b605a96194/g39ZopMAnK.json')
lottie_engineer = load_lottie_file("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\engineer-holding-lightning.json")
lottie_volt_meter = load_lottie_file("C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\volt-mater.json")
lottie_coding = load_lottie_file("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\coding.json")
lottie_soft_engineer = load_lottie_file("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\engineer-employee-have-bright-idea.json")
lottie_reading = load_lottie_file("C:\\Users\\pasto\Downloads\Summer_Code_2023-main\MyWebsite\\animations\\girl-reading-book-at-home.json")
lottie_cooking = load_lottie_file("C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\cooking-your-food.json")
lottie_gym = load_lottie_file("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\gym_exercise.json")
lottie_music = load_lottie_file("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\MyWebsite\\animations\\drum.json")


st.set_page_config(
    page_title= "Jan's Webpage",
    page_icon= "⚡",
    layout= 'centered'
)

def show():
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
            # st.write('##')
        with right_column:
            st.lottie(lottie_engineer, height = 250, width = 250, key = "engineer")
            # st.write('##')
        with right2_column:
            st.lottie(lottie_soft_engineer, height = 250, width = 250, key ='sfwre_eng')

    
    with st.container():
        st.divider()
        st.subheader("Skills: 🪚	🪛🪠🧰")
        st.write('##')

        left_column, right_column = st.columns(2, gap ='small')
        with left_column:
            st.lottie(lottie_coding, height = 250, width = 250, key = "coding")
        with right_column:
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Programming: Python, C++, MATLAB, CSS, HTML
                        </div>''',unsafe_allow_html=True)
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Software Tools: Jupyter Notebook, Arduino, SOLIDWORKS, PCB EAGLE, Google Sheets, MS Word, 
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
            st.lottie(lottie_volt_meter, height = 250, width = 250, key = 'electrical')
    
    with st.container():
        st.divider()
        st.subheader("Hobbies: 📚 🍳 🏃‍♂️ 🎵")
        st.write('##')

        col1, col2, col3 = st.columns(3, gap='small')
        with col1:
            st.lottie(lottie_reading, height = 150, width = 150, key = 'book')
        with col2:
            st.lottie(lottie_cooking, height = 150, width = 150, key = 'cook')
        with col3:
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Voracious science-fiction reader and health-conscious vegetarian!
                        </div>''',unsafe_allow_html=True)
    with st.container():
        left_column, right_column, right2_column = st.columns(3, gap = 'small')
        with left_column:
            st.lottie(lottie_gym, height = 200, width = 200, key = 'exercise')
        with right_column:
            st.lottie(lottie_music,height = 150, width = 150, key = 'drums')
        with right2_column:
            st.write('##')
            st.markdown('''
                    <div style= 'font-family: sans-serif; font-size: 20px;'>
                        Physically active and I enjoy creating random melodies with drums!
                        </div>''',unsafe_allow_html=True)