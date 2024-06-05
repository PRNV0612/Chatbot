# Python Chatbot

This is a simple chatbot application built using Python, the OpenAI API, and the customtkinter library for the GUI. The chatbot interacts with users and provides responses using the OpenAI GPT-3.5-turbo model.

## Features
- User-friendly graphical interface
- Chat history with scrollable text box
- Input box for user messages
- Integration with OpenAI GPT-3.5-turbo for generating responses

## Prerequisites
Before running the application, you need to have the following:

- Python 3.6+
- OpenAI API key

## Dependencies
1. **OpenAI**: Library to interact with OpenAI's API.
2. **CustomTkinter**: Library for creating custom widgets in Tkinter.


## Installation

1. Clone the repository:

```bash
git clone https://github.com/PRNV0612/Chatbot.git
cd Chatbot.git
```

2.Install the required dependencies:
```bash
!pip install openai
!pip install customtkinter
```

## Configuration
### Replace with your actual OpenAI API key
client = OpenAI(api_key='your-openai-api-key')

## Running the Application
#### After configuring your API key, you can run the application:
```bash
python chatbot.py
```

## Usage
- Type your message in the input box and click the "Send" button or press Enter.
- The chatbot will respond to your message and display the conversation in the chat history.

## Code Overview
Here's a brief overview of the main components of the script:
- get_completion_from_messages: Sends messages to the OpenAI API and retrieves the response.
- collect_messages: Collects user messages and bot responses, updating the chat history.
- get_prompt: Handles user input and updates the chat history.
- send_response: Updates the chat history with the bot's response.
- Tkinter GUI Setup: Creates the main window, chat frame, chat box, scrollbar, input box, and send button.

## License


