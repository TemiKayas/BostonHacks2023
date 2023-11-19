# import openai
from openai import OpenAI
from chat_data_reader import *
# client = OpenAI()

# Read API key from apikey.env file
with open("./apikey.env", "r") as file:
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=file.read().strip(),
)
    # openai.api_key = file.read().strip()

def chatCall(question):
    # Get formatted financial data from the helper function
    financial_info = read_and_format_financial_data()

    # Proceed with the chatbot API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant. Your job is to act as a kind financial teacher and advisor. " + financial_info},
            {"role": "user", "content": question}
        ]
    )

    msg = response.choices[0].message.content
    return msg


# Call the chat function and print the response message







