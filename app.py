from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

for _file in os.listdir('chats'):
    chats = open('chats/' + _file, 'r').readlines()
    trainer.train(chats)

while True:
    request = input('You: ')
    response = chatbot.get_response(request)

    print("Bot: %s", response)
