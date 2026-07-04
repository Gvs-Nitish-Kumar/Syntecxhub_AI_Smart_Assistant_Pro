from chatbot.knowledge import knowledge
from chatbot.calculator import calculate
from chatbot.memory import save_name, get_name
from chatbot.history import save_chat, show_history, clear_history
from chatbot.utils import get_time, get_date
from chatbot.voice import speak

from colorama import Fore, init
import time
import random

init()

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer get cold? Because it forgot to close Windows.",
    "Why was the computer tired? Because it had too many tabs open."
]

quotes = [
    "The best way to predict the future is to create it.",
    "Success is the sum of small efforts repeated every day.",
    "Never stop learning because life never stops teaching."
]


def bot_reply(text):
    print(Fore.CYAN + "Bot: ", end="")

    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)

    print()

    speak(text)


print(Fore.GREEN + "=" * 55)
print("🤖 Syntecxhub AI Smart Assistant Pro")
print("Type 'help' for commands")
print("Type 'bye' to exit")
print("=" * 55)

while True:
    user = input(Fore.YELLOW + "\nYou: ").lower()

    save_chat("You: " + user)

    if user in ["hi", "hello", "hey", "hii"]:
        bot_reply("Hello! Welcome to AI Smart Assistant Pro.")

    elif user in ["how are you", "how are you?"]:
        bot_reply("I am doing great! Thanks for asking.")

    elif user == "help":
        bot_reply(
            "Commands: hi, time, date, calculate, "
            "my name is, what is my name, joke, quote, "
            "/history, /clear, bye"
        )

    elif user in knowledge:
        bot_reply(knowledge[user])

    elif user == "time":
        bot_reply(get_time())

    elif user == "date":
        bot_reply(get_date())

    elif user.startswith("calculate"):
        expression = user.replace("calculate", "").strip()
        result = calculate(expression)
        bot_reply(str(result))

    elif user.startswith("my name is"):
        name = user.replace("my name is", "").strip()
        save_name(name)
        bot_reply(f"Nice to meet you, {name}!")

    elif user == "what is my name":
        name = get_name()

        if name:
            bot_reply(f"Your name is {name}.")
        else:
            bot_reply("I don't know your name yet.")

    elif user == "joke":
        bot_reply(random.choice(jokes))

    elif user == "quote":
        bot_reply(random.choice(quotes))

    elif user == "/history":
        history = show_history()
        print(Fore.MAGENTA + "\n----- CHAT HISTORY -----")
        print(history)
        print("------------------------")

    elif user == "/clear":
        clear_history()
        bot_reply("Chat history cleared successfully.")

    elif user == "bye":
        bot_reply("Goodbye! Have a wonderful day.")
        break

    else:
        bot_reply("Sorry, I don't understand that command.")