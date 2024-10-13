def chatbot():
    print("Hello! I'm your chatbot. How can I assist you?")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        if "hello" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but thanks for asking!")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")
        elif "help" in user_input:
            print("Chatbot: Sure! I can respond to greetings, tell you the time, or let you know about myself.")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

chatbot()
