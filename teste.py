#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,configparser,json,requests#,select,traceback,socket,_thread
from time import sleep
import HTTPhandler

class RoboSO:
    def __init__(self):
        self.http_server_init()
        # self.get_config()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        host = config['rede']['host']
        porta = config['rede']['port']
        self.url = config['config']['url']
        self.chat_id = config['config']['chat_id']
        token = config['config']['token']
        self.rede = (host, int(porta))
        self.link = self.url + token
        return self.rede
        
    def http_server_init(self):
        self.get_config()            
        print('Iniciando...')
        requisicaohttp = HTTPhandler.RequisicaoHTTP
        httpd = HTTPServer(self.rede,requisicaohttp)
        httpd.serve_forever()

    def get_rede(self):
        return self.rede

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
        self.enviar_mensagem()
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

    #Função para enviar a mensagem
    def enviar_mensagem(self):
        url =  self.link + "/sendMessage"
        texto = "Aqui se monta um texto\n teste" + "\n" + "Criar a função para montá-la"
        json = {'chat_id': self.chat_id, 'text': texto}
        requests.post(url, data=json)
        return 

    #Função para separar mensagem, usuário e id da mensagem
    def getMensagem(self):
        linkToGet = self.link + "/getUpdates"
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
idmsn_old = "0"
programa = RoboSO()
if __name__ == "__main__":
    rede = programa.get_rede()
    while True:
        try:
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
            print("FATAL ERROR")
            sys.exit(1)
