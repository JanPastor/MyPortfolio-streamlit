import streamlit as st

def main():
    st.title("Your Name's Portfolio")

    # About Section
    st.header("About Me")
    st.write("""
    Hello! I'm [Your Name]. I'm a passionate developer with experience in [Your Skills, e.g., Web Development, Data Science].
    This is a brief overview of my work and skills.
    """)

    # Projects Section
    st.header("Projects")
    projects = {
        "Project 1": "Description of project 1...",
        "Project 2": "Description of project 2...",
        "Project 3": "Description of project 3..."
    }
    
    for project, description in projects.items():
        st.subheader(project)
        st.write(description)
        # If you have a link to a live project or its code, add it here
        # st.markdown("[View project](#link_to_project)")

    # Skills Section
    st.header("Skills")
    skills = [
        "Python", "Web Development (HTML, CSS, JS)", "Data Analysis", "Machine Learning"
    ]
    
    st.write(", ".join(skills))

    # Contact Section
    st.header("Contact")
    st.write("""
    Interested in collaborating or have a question? Reach out to me at [youremail@example.com](mailto:youremail@example.com).
    """)

if __name__ == "__main__":
    main()
