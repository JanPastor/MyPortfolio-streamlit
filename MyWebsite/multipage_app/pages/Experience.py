
import streamlit as st

# st.set_page_config(
#     page_title= "Jan's Webpage",
#     page_icon= "⚡",
#     layout= 'centered'
# )

def show():

    st.markdown("""
    <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

    st.title("Experience 💼")
    st.write("What did I do? 🤔")

# Describe my experience with MATE ROV 2023 World Competition

    with st.container():
        st.title('🌊 MATE ROV 2023 World Competition 🌊 ')
        st.subheader("Jan Pastor | Lead Software Engineer :computer: | Electrical Engineer⚡")
        st.markdown("""
                    

        - Designed, implemented, and managed all software related aspects of the ROV 
        - Implemented code to operate a gripper mechanism for the ROV (servo-operated claw), designed intuitive GUI,
        for Pilot, wrote code to operate dual camera system to help Pilot to navigate and maneuver the ROV underwater
        - Employed custom computer vision algorithms and pre-trained AI models to enhance ROV capabilities
        - Tested and debugged ROV system code to eliminate fatal errors and crashes during ROV operation
        - Soldered and assembled all electronic components and systems for the ROV
        - Assisted electrical engineers in building PSU (power supply unit) for ROV
        - Performed extensive electrical wiring safety inspections on the ROV
        - Collaborated clsely with Team CEO and Team Leads to ensure ROV was competition ready
                    """)
        
    with st.container():
        st.title('🌊 MATE FLOATS Summer 2023 Training Workshop🌊')
        st.subheader("Jan Pastor | 📈 Data Analysis Cohort Member 📊")
        st.markdown(
        """
        - Organized and performed data science analysis of oceanographic data using
        Jupyter notebook, Python, and MATLAB
        - Conducted laboratory sample collection, chemical analysis, and testing
        - Collaborated with a cadre of engineers to build and program custom sensors to 
        collect oceanographic data
        - Boarded Rachel-Carson Research vessel and assisted chief scientist in deployment of 
        oceanographic instrumentation using FLOAT, Rosetta, and Glider technology
        """)
    with st.container():
        st.title(' 🚀 Fall 2023-Spring 2024 CPP: Bronco Space BLADE (Balloon Launch Assessment Directive for Everyone) Project 🚀')
        st.subheader("Jan Pastor | 🧑‍💼 Team Deputy | Lead Researcher 🥽 🥼 :microscope:")
        st.markdown(
        """
        - Scheduled and conducted weekly team meetings to discuss project progress and goals
        - Assisted Team Lead in managing team members and delegating tasks
        - Conducted research on Balloon Radio Occultation (RO) technology and its applications 
        - Managed finances and budget for the project
        - Drafted electronic schematics for the BRO payload
        """)
            