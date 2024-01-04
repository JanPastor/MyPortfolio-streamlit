from PIL import Image, ImageOps
import streamlit as st
import os

# Function to load specific images into a dictionary
# def load_specific_images(image_data):
#     images = {}
#     for name, (path,caption) in image_data.items():
#         img = Image.open(path)  # Access the file path of the image 
#         img = ImageOps.exif_transpose(img) # Corrects orientation of the image
#         img = img.resize((800, 800))  # Optional: Resize the image
#         images[name] = (img,caption)
#     return images



def load_specific_images(image_data):
    images = {}
    for name, (url, caption) in image_data.items():
        st.image(url, caption=caption, use_column_width=True)
        images[name] = (url, caption)
    return images


# Function to load specific videos into a dictionary
def load_specific_videos(video_data):
    videos = {}
    for name, (url, caption) in video_data.items():
        st.video(url)
        st.write(caption)
        videos[name] = (url, caption)
    return videos


# Dictionary of image paths
image_data = { # This is the first dictionary set of pictures
    "ROV_Competition": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/MATE_ROV.png?raw=true", "🌊 ROV Competition 2023 🌊"),
    "Soldering_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_soldering_1.jpg?raw=true", "Top: Jan Pastor is soldering; Bottom: Brycen Lee researching"),
    "Soldering_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Rene_n_me_soldering.jpeg?raw=true", "Left: Me soldering with Rene"),
    "Soldering_3": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_soldering_2.jpg?raw=true", "Close up: Me soldering Surface Mount Resistor.😧"),
    "Soldering_4": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_soldering_tether.jpeg?raw=true","Soldering the Power tether 🔥"),
    "Mentoring_solder": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Mentoring_soldering.jpg?raw=true", "Mentoring Jasmine Lai on the Art of Soldering 🙃"),
    "Supervising": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_supervising.jpg?raw=true","I'm supervising my protoge, Brycen Lee 😝"),
}
image_data_1 = { # This is the second dictionary set of pictures]
    "Brainstorming": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Software_flowchart.jpg?raw=true", "Designing software heirarchy with my assistant DaNa 🤔"),
    "Software_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_explain_code_1.jpeg?raw=true","Me setting up thruster control code demo 😃"),
    "Software_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_explain_code_2.jpg?raw=true", "Team is gathered. Explanation begins. 😬"),
    "Software_3": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_explain_code_5.JPG?raw=true", "Further explaining the code, with assistant DaNa👍"),
    "Software_4": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_Explaining_code_favorite.JPG?raw=true", "The epitome of mentorship 🤓"),
    "Software_5": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_explain_to_Adam.jpeg?raw=true","Explaining code to mentee Adam"),
    "Software_6": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Testing_cameras.jpg?raw=true","Debugging ROV Camera System 😓")
}
image_data_2 = { # This is the third dictionary set of pictures about ROV, Team photos, and other Lancer Lumineer stuff
    "ChessDowntime": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Me_Chess.jpg?raw=true", "Phew! Chess downtime 😌"),
    "TeamLeads": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/TeamLeadsPrior.jpg?raw=true","Team Leads!"),
    "GUI_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/ROV_GUI.jpg?raw=true","The fruits of my labor 😭"),
    "ROV_dry_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/ROV_front_center.jpg?raw=true", "Front view"),
    "ROV_dry_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/ROV_rear.jpg?raw=true","Rear view"),
    "SystemCheck":("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/System_check1.jpg?raw=true","System check"),
    "Pool_test_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/pool_test_1.jpg?raw=true", "Poolside test w/ ROV pilot")
}
image_data_3 = { # Continuing image data set 2 but using a new container for aesthetic appeal
    "Team Photo":("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Team_Photo.jpg?raw=true","Team Photo 🤪"),
    "ROV_wet_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/ROV_water1.jpg?raw=true", "Demo 1 🤖"),
    "ROV_wet_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/ROV_water2.jpg?raw=true", "Demo 2 🤖"),
    "Competition": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Competition.jpg?raw=true", "Competition time! 💪"),
    "Main deck crew": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Team_Leads.jpg?raw=true","Deck crew assembled! 🙌"),
    "Station_0": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/at_the_deck.jpg?raw=true","Station 0"),
    "Copilot_Pilot": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Spring2023/Mission1_me_and_DaNa.jpg?raw=true","Copilot: Jan Pastor ; Pilot: DaNa")
}
image_data_4 = { # Pictures from MATE ROV FLOATS Summer Camp 2023 PART I
    "first_day1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/First_day.jpg?raw=true","First day of class"),
    "first_day_puget": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/First_day2.jpg?raw=true", "Model of Puget Sound Estuary"),
    "Code_sensor": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Coding_sensor.jpg?raw=true","Me coding, while Jasmine checks instructions. Teamwork! 😤 💪"),
    "Build_circuit": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Build_sensor.jpg?raw=true", "Assembling the sensor 😐"),
    "Deploy_sensor": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Jasmine_deploy_sensor.jpg?raw=true", "Jasmine deploying our completed sensor 👏"),
    "Deploy_sensor2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/deploy_sensors2.jpg?raw=true","Installing more sensors📡"),
    "Sensor_array": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Sensor_array.jpg?raw=true","Sensor array nearly complete 🤖")
}

image_data_5 = { # Pictures from MATE ROV FLOATS Summer Camp 2023 PART II
    "Tour": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Tour1.jpg?raw=true","Tour of Ocean Tech Building 🤓"),
    "Float_Inspection": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Me_float_inspecting.jpg?raw=true", "Examining FLOAT electronics 🔬"),
    "In_front_float": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/In_front_FLOAT.jpg?raw=true"," 😁"),
    "Glider": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Glider.jpg?raw=true", "The Glider 🌊"),
    "Lab_work": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/Lab_training.jpg?raw=true", " Lab training 🥼"),
    "Aft_deck_photo": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/aft_deck_group_pic.jpg?raw=true","👋"),
    "Rossetta_device": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Floats/ROSSETTA.jpg?raw=true","Meet Rossetta 🤯")
}

# Dictionary of video paths and captions
video_data = {
    "Video_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/pool_practice_0.mp4?raw=true", "Grabbing the PVC pipe attempt 1"),
    "Video_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/pool_practice_1.mp4?raw=true", "Attempt successful 😁"),
    "Video_3": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/pool_practice_2.mp4?raw=true","Grabbing the pyramid"),
    "Competition_video": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/competition.mp4?raw=true","MATE ROV Competition Mission Tasks 😬")
    # Add more urls and captions here
}

video_data_1 = {
    "Video_1": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/Entering_docks_1.mp4?raw=true", "Entering the docks 🚢"),
    "Video_2": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/Entering_dockds_2.mp4?raw=true", "Docks part 2 🚢"),
    "Video_3": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/aft_panorama.mp4?raw=true", "Water trails 🌊"),
    "Video_4": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/pranking_Jasmine.mp4?raw=true", "A little mischief 😆"),
    "Video_5": ("https://github.com/JanPastor/my-streamlit-staticmedia/blob/main/MATE_Float_Vids/phytoplankton.mp4?raw=true", "Plankton 🦠")
}

# Load specific videos
videos = load_specific_videos(video_data)
videos_1 = load_specific_videos(video_data_1)

# Load specific images
images = load_specific_images(image_data)
images_1 = load_specific_images(image_data_1)
images_2 = load_specific_images(image_data_2)
images_3 = load_specific_images(image_data_3)
images_4 = load_specific_images(image_data_4)
images_5 = load_specific_images(image_data_5)

def show():

    st.markdown("""
    <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

    # Page title
    st.title("Gallery 🖼️")
    st.write("Pictures or it didn't happen. :wink:")
    st.divider()
    
    # Pictures container 1: (Me being an electrical engineer and soldering stuff)
    with st.container():
        st.header("Pictures 📷 for MATE ROV Competition 2023| Pasadena, CA")
        st.subheader(" Jan Pastor |Lead Software Engineer| Electrical Engineer")
        st.write("(Feb-Aug. 2023)")
        # st.divider()
        st.subheader("⚡Pictures of Electrical Engineer doing his job⚡")
        
        # Create columns
        cols = st.columns(len(images))

        # Display specific images from dictionary in columns
        for i, (name, (image, caption)) in enumerate(images.items()):
            # cols[i].markdown(f'<div class="centered-img">![{caption}]({image})</div>', unsafe_allow_html=True)
            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    # New container for image data set 1 (Explaining the software pictures)        
    with st.container():
        st.subheader(":computer: Pictures of Lead Software Engineer doing his job :computer:")
        
        # Create columns
        cols = st.columns(len(images_1))

        # Display specific images from dictionary in columns
        for i, (name, (image, caption)) in enumerate(images_1.items()):
            # cols[i].markdown(f'<div class="centered-img">![{caption}]({image})</div>', unsafe_allow_html=True)

            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    # New container for image data set 2
    with st.container():
        st.subheader("Miscellaneous pictures of ROV and Lancer Lumineer Team!")
        # Create columns
        cols = st.columns(len(images_2))

        # Display specific images from dictionary in columns
        for i, (name, (image, caption)) in enumerate(images_2.items()):
            # cols[i].markdown(f'<div class="centered-img">![{caption}]({image})</div>', unsafe_allow_html=True)

            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions
    # New container for image data set 3
    with st.container():

        # Create columns
        cols = st.columns(len(images_3))

        # Display specific images from dictionary in columns
        for i, (name, (image, caption)) in enumerate(images_3.items()):
            # cols[i].markdown(f'<div class="centered-img">![{caption}]({image})</div>', unsafe_allow_html=True)

            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    with st.container(): # New container for videos about MATE ROV Competition
        st.subheader("Videos 🎥: Lancer Lumineers | MATE ROV Competition 2023")

        #Create the video columns
        video_cols = st.columns(len(videos))
        # Display specific videos from dictionary in columns
        for i, (name, (video_path, caption)) in enumerate(videos.items()):
            video_cols[i].video(video_path)
            video_cols[i].write(caption)
        
    with st.container(): # New container for pictures about MATE ROV FLOATS Summer Camp 2023
        st.header("Pictures 📷 for MATE ROV FLOATS Summer Workshop 2023|Seattle, WA")
        st.subheader(" Jan Pastor |Data Analysis Cohort Member| ")
        st.write("(Aug. 2023)")

        # Creating columns
        cols = st.columns(len(images_4))
        for i, (name, (image, caption)) in enumerate(images_4.items()):
            
            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    with st.container():

        # Creating columns
        cols = st.columns(len(images_5))
        for i, (name, (image, caption)) in enumerate(images_5.items()):
            
            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    with st.container(): # New container for videos about MATE ROV FLOATS
        st.subheader("Videos 🎥: MATE FLOATS Workshop| Seattle, WA")

        #Create the video columns
        video_cols = st.columns(len(videos_1))
        # Display specific videos from dictionary in columns
        for i, (name, (video_path, caption)) in enumerate(videos_1.items()):
            video_cols[i].video(video_path)
            video_cols[i].write(caption)