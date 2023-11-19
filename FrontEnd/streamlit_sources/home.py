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
def read_billing_history():
    # Define the file path
    file_path = './output/billing_history.json'

    # Open the file and read the JSON content
    try:
        with open(file_path, 'r') as file:
            billing_history = json.load(file)
        return billing_history
    except FileNotFoundError:
        LOGGER.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        LOGGER.error(f"Error decoding JSON from file: {file_path}")
        return {}

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
        page_title="Octopus Financial Advisor",
        page_icon="🐙",
        layout="wide",
        initial_sidebar_state="collapsed",
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
            .logo-container img {{
                display: block; 
                margin-left: auto; 
                margin-right: auto; 
                width: 150px; 
            }}

            .logo-text h2 {{
                color: {text_color}; 
                text-align: center; /* Center align the text */
                font-size: 24px; 
            }}

            pie-chart-container {{
                border: 2px solid #CCCCCC; /* Light grey border */
                border-radius: 10px; /* Rounded corners */
                padding: 20px; /* Padding inside the box */
                height: 300px; /* Fixed height, adjust as needed */
                display: flex; /* Flexbox for centering content */
                align-items: center; /* Vertically center */
                justify-content: center; /* Horizontally center */
            }}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Initialize account number in session state if not present
    if 'account_number' not in st.session_state:
        st.session_state['account_number'] = ''
    if not st.session_state['account_number']:
        st.markdown(f"<div style='text-align: center; font-size: 1.5em;'> Welcome Captain </div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center'><img src='https://cdn.discordapp.com/attachments/1175474476822040629/1175541486125862954/New_Project_6.png?ex=656b9b52&is=65592652&hm=9888248f4f033817d47f2c9bffcafd974bf35a61de07ec2d3a4012a81bd2082e&' width='300'></div>", unsafe_allow_html=True)

    # Prompt for account number at the top
    account_number = st.text_input("", key="account_number_input", value=st.session_state['account_number'])

    # Save the account number in session state
    st.session_state['account_number'] = account_number
    
    if account_number:
        # App title
        st.markdown(f"<h1 style='text-align: center; color: #4B0082; margin-top: 20px;'>FinOctopus Financial Advising</h1>", unsafe_allow_html=True)

        # Logo and text centered
        st.markdown("<div class='logo-container'><img src='https://cdn.icon-icons.com/icons2/2699/PNG/512/capitalone_logo_icon_168458.png'></div>", unsafe_allow_html=True)
        st.markdown("<div class='logo-text'><h2>Powered by Capital One</h2></div>", unsafe_allow_html=True)

        # Use the account number for plotting demo
        if 'graph_plotted' not in st.session_state:
            plotting_demo(account_number)
            st.session_state.graph_plotted = True

        col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed

        with col1:
            # Display the orange octopus image
            chat_octo = 'https://cdn.discordapp.com/attachments/1175474476822040629/1175578924303007815/orangeocto.png?ex=656bbe30&is=65594930&hm=2dd6cbd7691b360fabdbdd96ab1e582fd37717935c810711a2a90ba66971967e&'
            st.markdown(f'<div class="centered-image"><img src="{chat_octo}" alt="Friendly Octopus Advisor" width="500" height="500"></div>', unsafe_allow_html=True)

        with col2:
            # Placeholder for the pie chart
            # st.markdown("<div class='pie-chart-container'>Placeholder for Pie Chart</div>", unsafe_allow_html=True)
            labels = {}
            billing_history = read_billing_history()

            for index, value in enumerate(billing_history):
                if value["nickname"] not in labels:
                    labels[value["nickname"]] = value["payment_amount"]
                else:
                    labels[value["nickname"]] = labels[value["nickname"]] + value["payment_amount"] 

            keys = list(labels.keys())
            values = list(labels.values())

            fig, ax = plt.subplots(figsize=(40, 40))
            ax.set_facecolor('none')
            fig.set_facecolor('none')
            ax.axis('equal')
            ax.set_frame_on(False)

            wedges, texts, autotexts = ax.pie(values, labels=None, autopct='%.2f%%', labeldistance=1)
            ax.legend(wedges, keys, title="Category", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            plt.rcParams["font.size"] = 50
            plt.title("Spending % by Category", fontsize=150)

            st.pyplot(fig)
        st.markdown(f"<div style='text-align: center; font-size: 2em;'> Sup Squidude! I'm your financial advisor Captain Octavian! </div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center; font-size: 1.5em;'> Ask me anything about your account below: </div>", unsafe_allow_html=True)
        # Modify chat section to use the stored account number
        with st.container():
            # Another text input for user queries
            user_input = st.text_input("Your query here...", key="user_query_input")
            if user_input:
                # Read financial data for the stored account number

                # Get response from chatbot
                chatbot_response = chatCall(user_input)
                st.text_area("Let me help", value=chatbot_response, height=300, key="chatbot_response")

    # Optionally, you can put an else block here to display a message or something else when the account number is not entered
    else:
        st.write("Please enter your account number to view the dashboard.")

if __name__ == "__main__":
    run()
