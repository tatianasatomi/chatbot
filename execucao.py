import telepot
import json
from chatbot import Eon

with open('token.json') as jsonFile:
    token = json.load(jsonFile)

telegram = telepot.Bot(token)
bot = Eon("memoria")

def receiveMsg(msg):
    frase = bot.listen(phrase=msg['text'])
    resposta = bot.think(frase)
    bot.speak(resposta)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resposta)

telegram.message_loop(receiveMsg)

while True:
    pass