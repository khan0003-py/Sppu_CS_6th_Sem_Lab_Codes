def chatbot():
    print("Hi, I'm Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif user_input == "hello":
            print("Chatbot: Hello there! How are you doing today?")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks for asking. What can I do for you?")
        elif user_input == "phone":
            print("Chatbot: Which brand are you interested in?")
        elif user_input == "apple":
            print("Chatbot: Ok. What is your budget?")
        elif user_input.isdigit():
            budget = int(user_input)
            if budget > 100000:
                print("Chatbot: Sorry, we don't have any Apple phones within your budget.")
            else:
                print("Chatbot: Here are some Apple phone options within your budget.")
                print("1. iPhone 13")
                print("2. iPhone SE")
                print("3. iPhone XR")
        elif user_input == "ok":
            print("Chatbot: Here are some top models:")
            print("1. Samsung Galaxy S21")
            print("2. Google Pixel 6")
            print("3. OnePlus 9 Pro")
        elif user_input == "thank you":
            print("Chatbot: You're welcome!")
            print("Chatbot: If you need any further assistance, feel free to ask.")
        else:
            print("Chatbot: I'm sorry, I didn't understand what you said. Can you please rephrase?")
            
chatbot()
