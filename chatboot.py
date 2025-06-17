def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("ChatBot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("ChatBot: I'm your friendly semester chatbot!")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, but I'm doing great! How about you?")
        elif "help" in user_input:
            print("ChatBot: I can answer simple questions like greetings, programming, and fun facts!")
        elif "what is python" in user_input:
            print("ChatBot: Python is a popular programming language known for its simplicity.")
        elif "what can you do" in user_input:
            print("ChatBot: I can chat, answer basic questions, and make you smile!")
        elif "tell me a joke" in user_input:
            print("ChatBot: Why don't programmers like nature? It has too many bugs!")
        elif "who made you" in user_input:
            print("ChatBot: I was created by a student for a semester project!")
        elif "what is ai" in user_input:
            print("ChatBot: AI stands for Artificial Intelligence — machines that can mimic human thinking.")
        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a great day.")
            break
        else:
            print("ChatBot: I'm sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()
