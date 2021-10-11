import telepot, json, time
from telepot.loop import MessageLoop

with open("token.json") as jsonFile: #abre o arquivo
    token = json.load(jsonFile) #carrega o arquivo
telegram = telepot.Bot(token) #valida o token

def handle(mensagem):
    content_type, chat_type, chat_id = telepot.glance(mensagem)
    if content_type == "text":
        #telegram.sendMessage(chat_id, mensagem["text"])
        telegram.sendMessage(chat_id, "Sou Éon")

MessageLoop(telegram, handle).run_as_thread() #possibilita processamento paralelo
print("Executando...")

while 1:
    time.sleep(10)
