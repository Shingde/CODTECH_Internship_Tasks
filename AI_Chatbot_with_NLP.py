import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Kshitija. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm here to help! How can I assist you?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ]
]

# Create chatbot
def chatbot():
    print("Chatbot: Hello! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main execution
if __name__ == "__main__":
    chatbot()
