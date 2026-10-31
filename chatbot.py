class ChatBot:
    
    def __init__(self):
        self.name = "Buddy"

    def start(self):
        print("=" * 40)
        print("      WELCOME TO CHATBOT")
        print("=" * 40)
        print("Type 'bye' to exit.\n")

        while True:

            user = input("You : ").lower()

            if user == "hello" or user == "hi":
                print(self.name + " : Hello! How are you?")

            elif user == "how are you":
                print(self.name + " : I am fine. Thank you!")

            elif user == "what is your name":
                print(self.name + " : My name is Buddy.")

            elif user == "who created you":
                print(self.name + " : I was created using Python.")

            elif user == "python":
                print(self.name + " : Python is an easy programming language.")

            elif user == "college":
                print(self.name + " : Study well and practice coding every day.")

            elif user == "time":
                print(self.name + " : Sorry! I cannot tell the current time.")

            elif user == "thank you":
                print(self.name + " : You are welcome!")

            elif user == "bye":
                print(self.name + " : Goodbye! Have a nice day.")
                break

            else:
                print(self.name + " : Sorry! I don't understand.")


bot = ChatBot()
bot.start()