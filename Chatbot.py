import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot.", "You can call me ChatAI.", "I'm just a chatbot."]
    ],
    [
        r"who develop you?",
        ["Pankaj Darade developed me"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!"]
    ],
    [
        r"what can you do?",
        ["I answer you with basic questions"]
    ],
    [
        r"quit",
        ["Goodbye!"]
    ],
]


chatbot = Chat(pairs, reflections)

def run_chatbot():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    nltk.download('punkt') 
    run_chatbot()