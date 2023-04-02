import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is ioana",
        ["Hello ioana, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello, how can I help you today?"]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot, nice to meet you!"]
    ],
    [
        r"what do you do?",
        ["I can help you with a variety of things, from answering questions to providing recommendations."]
    ],
    [
        r"can you recommend a city break?",
        ["I would recommend Barcelona."]
    ],
    [
        r"how are you?",
        ["I am doing well, thank you for asking."]
    ],
    [
        r"quit",
        ["Goodbye, have a great day!"]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
