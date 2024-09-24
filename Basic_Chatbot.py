import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by OpenAI. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.", "No problem at all!"]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that!", "Awesome! Keep it up!"]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to chat with you and help you with your queries!"]
    ],
    [
        r"quit",
        ["Bye! Take care. Have a great day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you say it differently?", "I'm here to help, but I couldn't quite get that."]
    ],
]

# Default reflections
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

def chatbot():
    print("Hi, I'm a chatbot created to talk with you. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()


