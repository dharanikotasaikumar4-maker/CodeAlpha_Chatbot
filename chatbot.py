import datetime

def chatbot():
    print("👋 Welcome to RoyBot – Sai's Smart Chatbot!")

    user_name = input("Bot: What's your name?\nYou: ")
    print(f"Bot: Nice to meet you, {user_name}! You can chat with me. Type 'bye' to exit.")

    while True:
        user_input = input(f"{user_name}: ").lower()

        # Greetings
        if user_input == "hello" or user_input == "hi" or user_input == "hey":
            print(f"Bot: Hello {user_name}! How can I help you today?")
        
        # How are you
        elif user_input == "how are you":
            print("Bot: I'm great! Thanks for asking ")
        
        # Name and Creator
        elif user_input == "what is your name":
            print("Bot: I'm RoyBot 🤖")
        elif user_input == "who created you":
            print("Bot: I was created by Jaswanth Roy ")

        # Jokes
        elif user_input == "tell me a joke":
            print("Bot: Why did the computer go to therapy? Because it had too many 'bytes' of sadness 😄")

        # Favorites
        elif user_input == "your favorite movie":
            print("Bot: I love 'HI NANNA' movie ")
            
        elif user_input == "your favorite food":
            print("Bot: I eat electricity and drink data packets")

        # Time and Date
        elif user_input == "what's the time" or user_input == "time":
            now = datetime.datetime.now()
            print("Bot: Current time is", now.strftime("%H:%M:%S"))
        elif user_input == "what's the date" or user_input == "date":
            today = datetime.date.today()
            print("Bot: Today's date is", today.strftime("%Y-%m-%d"))

        # Math Solver
        elif "what is" in user_input and any(op in user_input for op in ["+", "-", "*", "/"]):
            try:
                expression = user_input.replace("what is", "").strip()
                result = eval(expression)
                print(f"Bot: The answer is {result}")
            except:
                print("Bot: Oops! I couldn't solve that. Try again.")
        
        # Exit
        elif user_input == "bye":
            print(f"Bot: Goodbye {user_name}! Have a great day 👋")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I didn't understand that. Try asking something else 🤔")

# Run the chatbot
chatbot()