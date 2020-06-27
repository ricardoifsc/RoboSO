#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep

class RoboSO:

    def __init__(self):
        config = open('config.ini', 'r')
        for line in config:
            self.token = line
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

programa = RoboSO()
if __name__ == "__main__":
    try:
        while True:
            saida = input('Digite alguma coisa: ')
            programa.perguntas(saida)
    except:
        sys.exit(1)