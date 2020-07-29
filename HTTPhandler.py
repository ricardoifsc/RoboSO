#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  
from http.server import BaseHTTPRequestHandler, HTTPServer
 
class RequisicaoHTTP(BaseHTTPRequestHandler):
    def do_LER(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Ler alguma coisa"
        self.wfile.write(bytes(message, "utf8"))
        response = "get"
        return response

    def do_FAZ(self):
        self.send_response(200)
        self.end_headers()
        message = ('Fazer alguma coisa \n')
        self.wfile.write(bytes(message, "utf8"))
        response = "post"
        return response

# host = 'localhost' 
# port = 8081
def run(ip, porta):
    print('Iniciando...')
    server_addr = (ip, porta)
    httpd = HTTPServer(server_addr, RequisicaoHTTP)
    print('rodando...')
    httpd.serve_forever()
 

run(host, port)