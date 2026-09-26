from datetime import datetime


def chatbot_response(user_input, user_name):
    user_input = user_input.lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey", "salam", "assalam o alaikum"]:
        return f"Hi {user_name}! How can I help you?"

    # How are you
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! I hope you are doing well too."

    # Name
    elif user_input in ["what is your name", "what's your name", "your name"]:
        return "My name is CodeAlpha Bot. I am a simple rule-based chatbot."

    # User asks who created the bot
    elif user_input in ["who created you", "who made you", "who developed you"]:
        return "I was created as a Basic Chatbot project for the CodeAlpha internship."

    # Help
    elif user_input in ["help", "what can you do", "what do you do"]:
        return (
            "I can greet you, respond to basic questions, "
            "tell you the current time and date, and have a simple conversation."
        )

    # Time
    elif user_input in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Date
    elif user_input in ["date", "what is the date", "today's date", "current date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    # Thanks
    elif user_input in ["thanks", "thank you", "thankyou"]:
        return "You're welcome!"

    # Goodbye
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! It was nice talking to you."

    # Unknown input
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("=" * 50)
    print("        WELCOME TO CODEALPHA CHATBOT")
    print("=" * 50)

    user_name = input("Bot: What is your name? ")

    print(f"\nBot: Nice to meet you, {user_name}!")
    print("Bot: You can type 'help' to see what I can do.")
    print("Bot: Type 'bye' whenever you want to exit.\n")

    while True:
        user_input = input(f"{user_name}: ")

        response = chatbot_response(user_input, user_name)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()