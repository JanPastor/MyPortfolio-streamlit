from PIL import Image, ImageOps
import streamlit as st
import os

# Function to load specific images into a dictionary
def load_specific_images(image_data):
    images = {}
    for name, (path,caption) in image_data.items():
        img = Image.open(path)  # Access the file path of the image 
        img = ImageOps.exif_transpose(img) # Corrects orientation of the image
        img = img.resize((800, 800))  # Optional: Resize the image
        images[name] = (img,caption)
    return images

# Function to load specific videos into a dictionary
def load_specific_videos(video_data):
    videos = {}
    for name, (path, caption) in video_data.items():
        videos[name] = (path, caption)
    return videos

# Dictionary of image paths
image_data = { # This is the first dictionary set of pictures
    "ROV_Competition": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\MATE_ROV.png", "🌊 ROV Competition 2023 🌊"),
    "Soldering_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_soldering_1.jpg", "Top: Jan Pastor is soldering; Bottom: Brycen Lee researching"),
    "Soldering_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Rene_n_me_soldering.jpeg", "Left: Me soldering with Rene"),
    "Soldering_3": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_soldering_2.jpg", "Close up: Me soldering Surface Mount Resistor.😧"),
    "Soldering_4": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_soldering_tether.jpeg","Soldering the Power tether 🔥"),
    "Mentoring_solder": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Mentoring_soldering.jpg", "Mentoring Jasmine Lai on the Art of Soldering 🙃"),
    "Supervising": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\MyWebsite\\images\\Me_supervising.jpg","I'm supervising my protoge, Brycen Lee 😝"),
}
image_data_1 = { # This is the second dictionary set of pictures]
    "Brainstorming": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Software_flowchart.jpg", "Designing software heirarchy with my assistant DaNa 🤔"),
    "Software_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_explain_code_1.jpeg","Me setting up thruster control code demo 😃"),
    "Software_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_explain_code_2.jpg", "Team is gathered. Explanation begins. 😬"),
    "Software_3": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_explain_code_5.JPG", "Further explaining the code, with assistant DaNa👍"),
    "Software_4": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_Explaining_code_favorite.JPG", "The epitome of mentorship 🤓"),
    "Software_5": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_explain_to_Adam.jpeg","Explaining code to mentee Adam"),
    "Software_6": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Testing_cameras.jpg","Debugging ROV Camera System 😓")
}
image_data_2 = { # This is the third dictionary set of pictures about ROV, Team photos, and other Lancer Lumineer stuff
    "ChessDowntime": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Me_Chess.jpg", "Phew! Chess downtime 😌"),
    "TeamLeads": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\TeamLeadsPrior.jpg","Team Leads!"),
    "GUI_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\ROV_GUI.jpg","The fruits of my labor 😭"),
    "ROV_dry_1": ("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\ROV_front_center.jpg", "Front view"),
    "ROV_dry_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\ROV_rear.jpg","Rear view"),
    "SystemCheck":("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\System_check1.jpg","System check"),
    "Pool_test_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\pool_test_1.jpg", "Poolside test w/ ROV pilot")
}
image_data_3 = { # Continuing image data set 2 but using a new container for aesthetic appeal
    "Team Photo":("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Team_Photo.jpg","Team Photo 🤪"),
    "ROV_wet_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\ROV_water1.jpg", "Demo 1 🤖"),
    "ROV_wet_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\ROV_water2.jpg", "Demo 2 🤖"),
    "Competition": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Competition.jpg", "Competition time! 💪"),
    "Main deck crew": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Team_Leads.jpg","Deck crew assembled! 🙌"),
    "Station_0": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\MyWebsite\\images\\at_the_deck.jpg","Station 0"),
    "Copilot_Pilot": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\images\\Mission1_me_and_DaNa.jpg","Copilot: Jan Pastor ; Pilot: DaNa")
}
image_data_4 = { # Pictures from MATE ROV FLOATS Summer Camp 2023 PART I
    "first_day1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\First_day.jpg","First day of class"),
    "first_day_puget": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\First_day2.jpg", "Model of Puget Sound Estuary"),
    "Code_sensor": ("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Coding_sensor.jpg","Me coding, while Jasmine checks instructions. Teamwork! 😤 💪"),
    "Build_circuit": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Build_sensor.jpg", "Assembling the sensor 😐"),
    "Deploy_sensor": ("C:\\Users\\pasto\\Downloads\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Jasmine_deploy_sensor.jpg", "Jasmine deploying our completed sensor 👏"),
    "Deploy_sensor2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\deploy_sensors2.jpg","Installing more sensors📡"),
    "Sensor_array": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Sensor_array.jpg","Sensor array nearly complete 🤖")
}

image_data_5 = { # Pictures from MATE ROV FLOATS Summer Camp 2023 PART II
    "Tour": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\MyWebsite\\mate_floats_pics\\Tour1.jpg","Tour of Ocean Tech Building 🤓"),
    "Float_Inspection": ("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Me_float_inspecting.jpg", "Examining FLOAT electronics 🔬"),
    "In_front_float": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\In_front_FLOAT.jpg"," 😁"),
    "Glider": ("C:\\Users\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Glider.jpg", "The Glider 🌊"),
    "Lab_work": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\Lab_training.jpg", " Lab training 🥼"),
    "Aft_deck_photo": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\aft_deck_group_pic.jpg","👋"),
    "Rossetta_device": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_pics\\ROSSETTA.jpg","Meet Rossetta 🤯")
}

# Dictionary of video paths and captions
video_data = {
    "Video_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\videos\\pool_practice_0.mp4", "Grabbing the PVC pipe attempt 1"),
    "Video_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\videos\\pool_practice_1.mp4", "Attempt successful 😁"),
    "Video_3": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\videos\\pool_practice_2.mp4","Grabbing the pyramid"),
    "Competition_video": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\MyWebsite\\videos\\competition.mp4","MATE ROV Competition Mission Tasks 😬")
    # Add more paths and captions here
}

video_data_1 = {
    "Video_1": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_videos\\Entering_docks_1.mp4", "Entering the docks 🚢"),
    "Video_2": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_videos\\Entering_dockds_2.mp4", "Docks part 2 🚢"),
    "Video_3": ("C:\\Users\\pasto\\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_videos\\aft_panorama.mp4", "Water trails 🌊"),
    "Video_4": ("C:\\Users\\pasto\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_videos\\pranking_Jasmine.mp4", "A little mischief 😆"),
    "Video_5": ("C:\\Users\pasto\Downloads\\Summer_Code_2023-main\\Summer_Code_2023-main\\MyWebsite\\mate_floats_videos\\phytoplankton.mp4", "Plankton 🦠")
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

    with st.container():

        # Create columns
        cols = st.columns(len(images_3))

        # Display specific images from dictionary in columns
        for i, (name, (image, caption)) in enumerate(images_3.items()):
            # cols[i].markdown(f'<div class="centered-img">![{caption}]({image})</div>', unsafe_allow_html=True)

            cols[i].image(image, caption=caption, use_column_width=True)  # Set caption to 'name' if you want captions

    with st.container():
         st.subheader("Videos 🎥: Lancer Lumineers | MATE ROV Competition 2023")

         #Create the video columns
         video_cols = st.columns(len(videos))
         # Display specific videos from dictionary in columns
         for i, (name, (video_path, caption)) in enumerate(videos.items()):
             video_cols[i].video(video_path)
             video_cols[i].write(caption)
        
    with st.container():
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

    with st.container():
         st.subheader("Videos 🎥: MATE FLOATS Workshop| Seattle, WA")

         #Create the video columns
         video_cols = st.columns(len(videos_1))
         # Display specific videos from dictionary in columns
         for i, (name, (video_path, caption)) in enumerate(videos_1.items()):
             video_cols[i].video(video_path)
             video_cols[i].write(caption)