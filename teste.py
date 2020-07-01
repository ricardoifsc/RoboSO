#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import telegram
from time import sleep


class RoboSO:

    def __init__(self):
        config = open('config.ini', 'r')
        self.chat_id = config.readlines()[0]
        config.close()
        config = open('config.ini', 'r')
        self.token = config.readlines()[1]
        config.close()
        
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
        print(self.chat_id)
        programa.enviar_mensagem()
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

    def mensagem(self):
        json = { "chat_id": self.chat_id.replace("\n",""), "text": "Teste", "parse_mode": "html", "disable_web_page_preview": True }
        return json

    def enviar_mensagem(self):
        texto = programa.mensagem()
        bot = telegram.Bot(token=self.token.replace("\n",""))
        bot.sendMessage(chat_id=self.chat_id.replace("\n",""), text=texto)
        return 

programa = RoboSO()
if __name__ == "__main__":
    try:
        while True:
            saida = input('Digite alguma coisa: ')
            programa.perguntas(saida)
    except:
        sys.exit(1)