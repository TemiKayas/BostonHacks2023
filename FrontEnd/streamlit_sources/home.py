import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Octopus Financial Advisor",
        page_icon="🐙",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Define your color scheme
    primary_color = "#FFFFFF"
    secondary_background_color = "#ffffff"
    text_color = "#000000"

    gif_url = 'https://i.redd.it/9i5ktvf5ayw31.gif'

    # Custom CSS to inject our own styles
    custom_css = f"""
        <style>
            .stApp {{
                background-image: url({gif_url});
                background-repeat: no-repeat;
                background-size: cover;
            }}
            .css-1d391kg {{
                background-color: {secondary_background_color};
                border-radius: 10px;
            }}
            .stTextInput > label, .stTextArea > label {{
                color: {primary_color};
            }}
            .st-bx {{
                color: {text_color};
            }}
            .stSidebar > div:first-child {{
                background-color: {primary_color};
            }}
            .stTextArea {{
                font-size: 20px; 
            }}
            h1 {{
                font-size: 4em; 
                margin-top: 1rem; 
            }}
            .centered-image {{
                display: flex;
                justify-content: center;
            }}
            .center-content {{
                display: flex;
                flex-direction: column;
                align-items: center; 
                justify-content: center; 
                height: 100vh; 
            }}
            .logo-text {{
                display: flex;
                align-items: center; /* Aligns items vertically */
                justify-content: start; /* Aligns items horizontally to start */
                height: 100%;
            }}
            .logo-text h2 {{
                margin: 0;
                color: {text_color}; /* Ensures the text color is set */
            }}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    
    # App title and logo
    st.markdown(f"<h1 style='text-align: center; color: {primary_color}; margin-top: 20px;'>FinOctopus Financial Advising</h1>", unsafe_allow_html=True)
     
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed
    with col1:
        st.image('https://cdn.icon-icons.com/icons2/2699/PNG/512/capitalone_logo_icon_168458.png', width=200)  # Adjust the width as needed
    with col2:
        st.markdown("<div class='logo-text'><h2>Powered by Capital One</h2></div>", unsafe_allow_html=True)

    with st.container():
        accountNumber = st.text_input("Please Enter Your Capital One Account Number Captain", key="id")
    
    # Image of the octopus advisor with max-width set
    octopus_image_url = 'https://cdn.discordapp.com/attachments/1175474476822040629/1175541486125862954/New_Project_6.png?ex=656b9b52&is=65592652&hm=9888248f4f033817d47f2c9bffcafd974bf35a61de07ec2d3a4012a81bd2082e&'
    st.markdown(f'<div class="centered-image"><img src="{octopus_image_url}" alt="Friendly Octopus Advisor" width="500" height="500"></div>', unsafe_allow_html=True)


    # Main content area
    with st.container():
        user_input = st.text_input("Captain, let me know how I can help you set sail below...", key="user_query")

        if user_input:
            # Logic to get response from chatbot
            chatbot_response = "Chatbot here..."
            st.text_area("Let me help", value=chatbot_response, height=300, key="chatbot_response")

if __name__ == "__main__":
    run()
