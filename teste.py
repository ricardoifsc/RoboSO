#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,configparser,json,requests
# import telegram
from time import sleep

class RoboSO:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.url = config['config']['url']
        self.chat_id = config['config']['chat_id']
        self.token = config['config']['token']        

    def perguntas(self, cmd):
        if cmd == 'start':
            programa.start()
            return
        elif cmd == 'stop':
            programa.stop()
            return
        elif cmd == 'restart':
            programa.restart()
            return
        elif cmd == 'sair':
            sys.exit(1)
        else:
            retorno = print('Não entendi o que você quer')
        return retorno

    def start(self):
        print('Iniciando serviço...')
        sleep(1)
        linkToSend = self.url + self.token + "/sendMessage"
        programa.enviar_mensagem(linkToSend,self.chat_id)
        return

    def stop(self):
        print('Serviço parado')
        sleep(1)
        return

    def restart(self):
        print('Aguarde, o serviço está sendo parado')
        sleep(1)
        print('Serviço reiniciado.')
        sleep(1)
        return

    #Função para criar a mensagem
    def mensagem(self):
        text = "Aqui se monta um texto\n teste" + "\n" + "Criar a função para montá-la"
        return text

    #Função para enviar a mensagem
    def enviar_mensagem(self,url,chat):
        texto = programa.mensagem()
        json = {'chat_id': chat, 'text': texto}
        requests.post(url, data=json)
        return 

    #Função para separar mensagem, usuário e id da mensagem
    def getMensagem(self):
        linkToGet = self.url + self.token + "/getUpdates"
        response = requests.get(linkToGet)
        content = response.content.decode("utf8")
        convertJson = json.loads(content)
        totalMensagens = len(convertJson["result"])
        ultimaMensagem = totalMensagens -1
        idMensagem = convertJson["result"][ultimaMensagem]["message"]["message_id"]
        mensagem = convertJson["result"][ultimaMensagem]["message"]["text"]
        autor = convertJson["result"][ultimaMensagem]["message"]["chat"]["first_name"]
        return (mensagem, autor, str(idMensagem))


###################### INICIO DO PROGRAMA ######################
programa = RoboSO()
idmsn_old = "0"
if __name__ == "__main__":
    try:
        while True:
            msn, autor, idmsn = programa.getMensagem()
            if not msn: continue
            if idmsn_old == idmsn: continue
            else:
                idmsn_old = idmsn
                if msn[0] == "/":
                    print("O usuário " + autor + " vai executar: " + msn[1:])
                    programa.perguntas(msn[1:])
                else:
                    print("O usuário " + autor + " digitou: " + msn)
    except:
        sys.exit(1)
