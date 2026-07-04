def save_chat(text):
    with open("data/chat_history.txt", "a") as file:
        file.write(text + "\n")

def show_history():
    try:
        with open("data/chat_history.txt", "r") as file:
            return file.read()
    except:
        return "No chat history found."

def clear_history():
    with open("data/chat_history.txt", "w") as file:
        file.write("")