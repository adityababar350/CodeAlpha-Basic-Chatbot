
def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi! How can I help you?")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm doing great! Thanks for asking.")
        elif user_input == "what is codealpha":
            print("🤖 Chatbot: CodeAlpha provides internship opportunities for students.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

chatbot()
