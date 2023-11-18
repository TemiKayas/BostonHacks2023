import openai

# Read API key from apikey.env file
with open("./apikey.env", "r") as file:
    openai.api_key = file.read().strip()

def chat():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello!"}
        ]
    )
    # Isolate the message content
    message_content = response['choices'][0]['message']['content']
    return message_content

# Call the chat function and print the response message
response_message = chat()
print(response_message)






