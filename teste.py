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

programa = RoboSO()
if __name__ == "__main__":
    try:
        while True:
            saida = input('Digite alguma coisa: ')
            programa.perguntas(saida)
    except:
        sys.exit(1)
        