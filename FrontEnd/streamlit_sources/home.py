import streamlit as st
from streamlit.logger import get_logger
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from chat import chatCall
from financial_data_reader import read_financial_data


LOGGER = get_logger(__name__)

def plotting_demo(account_number):
    # Read financial data for the given account number
    financial_data = read_financial_data(account_number)

    if financial_data.empty:
        st.error("No financial data available for plotting for the given account.")
        return

    # Plot the data
    chart = st.line_chart(financial_data.set_index('payment_date'))



def run():
    st.set_page_config(
        page_title= "Octopus Financial Advisor",
        page_icon= " 🐙 ",
        layout= "wide",
        initial_sidebar_state= "collapsed",
    )

    # Define your color scheme
    primary_color = "#FFFFFF"
    secondary_background_color = "#ffffff"
    text_color = "#FFFFFF"

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
            .stTextInput input, .stTextArea textarea {{
                background-color: #52bdff; /* Blue */
                color: #FFFFFF; 
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
                font-style: italic; /* Make text italic */
            }}

            .logo-container {{
                display: flex;
                align-items: center;
                justify-content: end; /* Align to the end for right-side alignment */
            }}

            .logo-text h2 {{
                margin: 0;
                color: {text_color}; 
            }}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    
    # App title and logo
    st.markdown(f"<h1 style='text-align: center; color: #4B0082; margin-top: 20px;'>FinOctopus Financial Advising</h1>", unsafe_allow_html=True)
     
    col1, col2 = st.columns([3, 2])  # Adjust the ratio as needed
    with col1:
        st.markdown("<div class='logo-text'><h2> Powered by Capital One</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='logo-container'><img src='https://cdn.icon-icons.com/icons2/2699/PNG/512/capitalone_logo_icon_168458.png' width='200'></div>", unsafe_allow_html=True)  # Adjust the width as needed

        # Image of the octopus advisor with max-width set
    octopus_image_url = 'https://cdn.discordapp.com/attachments/1175474476822040629/1175541486125862954/New_Project_6.png?ex=656b9b52&is=65592652&hm=9888248f4f033817d47f2c9bffcafd974bf35a61de07ec2d3a4012a81bd2082e&'
    st.markdown(f'<div class="centered-image"><img src="{octopus_image_url}" alt="Friendly Octopus Advisor" width="500" height="500"></div>', unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 2em;'> I'm AquaBanks Head OcotClerk </div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 1.5em;'> Please input your Capital One Account Number: </div>", unsafe_allow_html=True)

    with st.container():
        accountNumber = st.text_input("Please Enter Your Capital One Account Number", key="account_number_input")

        # Trigger graph plotting only if accountNumber is entered
        if accountNumber:
            if 'graph_plotted' not in st.session_state:
                plotting_demo(accountNumber)
                st.session_state.graph_plotted = True
        if st.button("Update Graph"):
            if accountNumber:
                plotting_demo(accountNumber)
            

    chat_octo = 'https://cdn.discordapp.com/attachments/1175474476822040629/1175578924303007815/orangeocto.png?ex=656bbe30&is=65594930&hm=2dd6cbd7691b360fabdbdd96ab1e582fd37717935c810711a2a90ba66971967e&'
    st.markdown(f'<div class="centered-image"><img src="{chat_octo}" alt="Friendly Octopus Advisor" width="500" height="500"></div>', unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 2em;'> Sup Squidude! Im your financial advisor Captain Octavian! </div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 1.5em;'> Ask me anything about your account below: </div>", unsafe_allow_html=True)

    # Main content area
    with st.container():
        user_input = st.text_input("", key="user_query")

        if user_input:
            # Logic to get response from chatbot
            chatbot_response = chatCall(user_input)
            st.text_area("Let me help...", value=chatbot_response, height=300, key="chatbot_response")

if __name__ == "__main__":
    run()
