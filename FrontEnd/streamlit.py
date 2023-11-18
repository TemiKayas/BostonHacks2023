
import streamlit as st

# Title of the web app
st.title('*Fin*Octopus ink.')

# Display text
st.write('')

# Taking user input
user_input = st.text_input("Enter your name")

# Display user input
if user_input:
    st.write(f"Hello, {user_input}!")




