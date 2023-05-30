import tkinter as tk
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

api_key = os.getenv('API_KEY')
conversation = []

def send_request(event=None):
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


root = tk.Tk()
root.title("Chat Bot")
root.geometry("300x200")

# Create a frame to hold the input box and the send button
input_frame = tk.Frame(root)
input_frame.pack()

input_box = tk.Entry(input_frame)
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(input_frame, text="Send", command=send_request)
send_button.pack(side=tk.LEFT)

response_box = tk.Text(root, height=5, width=30)
response_box.pack(fill=tk.BOTH, expand=True)

root.bind('<Return>', send_request)

root.mainloop()
