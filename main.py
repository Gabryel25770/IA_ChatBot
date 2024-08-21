from chatbot import ChatBot
import os

myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

os.system("cls")

print("Olá, seja bem vindo ao Chatbot da FAPESP! Aqui você pode tirar todas as suas dúvidas relacionadas ao PIPE.")

pergunta = input("Como posso te ajudar?\n - ")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(" > " + resposta)
#print(resposta + " > ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    pergunta = input("\nPosso lhe ajudar com algo a mais?\n - ")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(" > " + resposta)
    #print(resposta + " > [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
