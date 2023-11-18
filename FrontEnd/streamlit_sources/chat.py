# import openai
from openai import OpenAI
# client = OpenAI()

# Read API key from apikey.env file
with open("./apikey.env", "r") as file:
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=file.read().strip(),
)
    # openai.api_key = file.read().strip()

def chatCall(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful finnancial assistant. Your job is to act as a kind finnancial teacher and advisor"},
            {"role": "user", "content": question}
        ]
    )
    # Isolate the message content
    # message_content = response['choices'][0]['message']['content']
    msg = response.choices[0].message.content
    return msg

# Call the chat function and print the response message
response_message = chatCall()
print(response_message)






