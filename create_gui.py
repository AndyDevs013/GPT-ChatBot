import tkinter as tk
from send_request import send_request

def create_gui(conversation):
    def toggle_visibility(event=None):
        if root.state() == "withdrawn":
            root.deiconify()  # Show the chat bot window
            input_box.focus()  # Set focus to the input box
        else:
            root.withdraw()  # Hide the chat bot window

    def send_on_enter(event):
        send_request(input_box, response_box, conversation)

    def exit_application():
        root.destroy()  # Close the chat bot window and exit the application

    def start_drag(event):
        x = event.x
        y = event.y

        def drag(event):
            icon.geometry(f"+{event.x_root - x}+{event.y_root - y}")

        icon.bind("<B1-Motion>", drag)

    root = tk.Tk()
    root.title("Chat Bot")
    root.geometry("300x200")
    root.withdraw()  # Hide the chat bot window by default
    root.protocol("WM_DELETE_WINDOW", exit_application)  # Handle window closing event

    # Create a frame to hold the input box and the send button
    input_frame = tk.Frame(root)
    input_frame.pack()

    input_box = tk.Entry(input_frame)
    input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
    input_box.bind("<Return>", send_on_enter)  # Bind Enter key press event to send message

    send_button = tk.Button(input_frame, text="Send", command=lambda: send_request(input_box, response_box, conversation))
    send_button.pack(side=tk.LEFT)

    response_box = tk.Text(root, height=5, width=30)
    response_box.pack(fill=tk.BOTH, expand=True)

    # Create a floating icon
    icon = tk.Toplevel(root)
    icon.overrideredirect(True)
    icon.geometry("+100+100")  # Adjust the initial position of the icon
    icon.wm_attributes("-topmost", True)

    icon_button = tk.Button(icon, text="Chat Bot", command=toggle_visibility)
    icon_button.pack()
    icon_button.bind("<ButtonPress-1>", start_drag)  # Bind left mouse button press event to start dragging

    # Menu options for the icon
    menu = tk.Menu(icon, tearoff=0)
    menu.add_command(label="Toggle", command=toggle_visibility)
    menu.add_command(label="Exit", command=exit_application)

    def show_menu(event):
        menu.post(event.x_root, event.y_root)  # Show the menu when the icon button is right-clicked

    icon_button.bind("<Button-3>", show_menu)  # Bind the right-click event to show the menu

    root.mainloop()

    return root, input_box, response_box
