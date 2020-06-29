#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,requests,pycurl,configparser
from time import sleep

class RoboSO:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
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
        print(self.chat_id)
        programa.sendMsg()
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
        json = { "chat_id": "-395670124", "text": "Teste", "parse_mode": "html", "disable_web_page_preview": True }
        return json

    def sendMsg(self):
        url = 'https://api.telegram.org/bot' + self.token + '/sendMessage'
        headers = {'Content-type': 'application/json'}
        texto = programa.mensagem()
        response = requests.post(url, data=texto, headers=headers)
        print(response)
        return

programa = RoboSO()
if __name__ == "__main__":
    try:
        while True:
            saida = input('Digite alguma coisa: ')
            programa.perguntas(saida)
    except:
        sys.exit(1)