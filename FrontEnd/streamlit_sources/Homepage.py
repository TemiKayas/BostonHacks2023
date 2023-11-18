import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
from chat import chatCall

def main():
    # Title of your app
    st.title('Financial Assistant and Analyzer')

    # Placeholder for your cute mascot graphic
    st.image('./finoctopus.webp', caption='Our Cute Mascot')

    # Section for GPT Chatbot
    st.header('GPT Chatbot')
    user_input = st.text_input("Ask the Financial Assistant:")
    # Placeholder response, replace with GPT-generated response later
    st.text_area("Response:", value=chatCall(user_input), height=100)

    # Section for Financial Charts
    st.header('Financial Charts')
    # Placeholder for financial charts
    # Later, you can generate these charts using real financial data
    sample_data = pd.DataFrame({
        'x': range(1, 11),
        'y': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    })
    fig, ax = plt.subplots()
    ax.plot(sample_data['x'], sample_data['y'])
    ax.set_xlabel('Sample X Axis')
    ax.set_ylabel('Sample Y Axis')
    st.pyplot(fig)

    # Section for JSON Data Display (temporary example)
    st.header('JSON Data Display')
    # Placeholder for JSON data
    # This can be replaced with actual financial JSON data in the future
    sample_json_data = {"name": "John Doe", "balance": 1000}
    st.json(sample_json_data)

if __name__ == "__main__":
    #main()
    print (main())
