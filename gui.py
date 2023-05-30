import tkinter as tk

def create_gui():
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

    return root, input_box, response_box
