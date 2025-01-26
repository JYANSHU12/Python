def chatbot():
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a program, but I'm doing well!",
        "bye": "Goodbye!"
    }
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        elif user_input == "exit":
            print("Bot: Bye!")
            break
        else:
            print("Bot: I don't understand that.")

chatbot()
