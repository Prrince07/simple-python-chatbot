while True:
    user = input("You: ").lower()
    if user == "exit":
        print("Bot: Bye!")
        break
    elif user == "hello":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I'm good, thanks!")
    else:
        print("Bot: I don't understand.")