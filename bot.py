from openai import OpenAI
import os
import customtkinter as ctk


#openai.api_key  = 'ENTER API_KEY'

client = OpenAI(api_key='ENTER YOUR API KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return response.choices[0].message["content"]

def collect_messages(prompt):
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    send_response(response)

def get_prompt():
    message = input_box.get()
    if message:
        chat_box.insert("end", f"You: {message}\n", "user")
        input_box.delete(0, "end")
        collect_messages(message)

def send_response(reply):
    chat_box.insert("end", f"Bot: {reply}\n", "bot")

# Create the main window
root = ctk.CTk()
root.title("Chatbot")
root.geometry("600x500")

# Create a frame for the chat area
chat_frame = ctk.CTkFrame(root)
chat_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create a scrollable text box for the chat history
chat_box = ctk.CTkTextbox(chat_frame, font=("Arial", 12))
chat_box.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Create a scrollbar for the chat box
scrollbar = ctk.CTkScrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side="left", fill="y")
chat_box.configure(yscrollcommand=scrollbar.set)

# Create an entry box for user input
input_box = ctk.CTkEntry(root, font=("Arial", 12), placeholder_text="Type your message...")
input_box.pack(pady=10, padx=10, fill="x")

# Create a button to send the message
send_button = ctk.CTkButton(root, text="Send", command=get_prompt)
send_button.pack(pady=10, padx=10)


context = [ {'role':'system', 'content':"""
You are a Friendly ChatBot named betty.\
    You are first required to greet the user, then ask them how you can help them.\
        You wait to listen to the whole query,\
            and then you provide them with the best possible answer.\
                You respond in a short, very conversational friendly style along with providing clarity.\
"""} ]


# Start the main event loop
root.mainloop()