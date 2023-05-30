import requests
import os
import tkinter as tk
from dotenv import load_dotenv

load_dotenv('.env')

api_key = os.getenv('API_KEY')

def send_request(input_box, response_box, conversation):
    user_input = input_box.get()

    conversation.append({'role': 'user', 'content': user_input})

    payload = {
        'messages': conversation,
        'max_tokens': 50,
        'model': 'gpt-3.5-turbo'
    }

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        data = response.json()
        choices = data['choices']
        messages = [message['message']['content'] for message in choices]
        message = '\n'.join(messages)
    else:
        message = 'Error: Failed to retrieve response.'
        print(response.text)

    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, message)
    input_box.delete(0, tk.END)  # Clear the input box

    # Log the conversation and response to a file
    log_conversation(conversation, message)

def log_conversation(conversation, response):
    with open('conversation.log', 'a') as file:
        for i, message in enumerate(conversation):
            role = message['role']
            content = message['content']
            file.write(f'{role}: {content}\n')
        file.write(f'Bot: {response}\n')