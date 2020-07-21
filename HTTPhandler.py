#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  
from http.server import BaseHTTPRequestHandler, HTTPServer
 
class RequisicaoHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Teste \n meu teste"
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. \n')
        self.wfile.write(response.getvalue())
        return
 
def run():
    print('Iniciando...')
    server_addr = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_addr, RequisicaoHTTP)
    print('rodando...')
    httpd.serve_forever()
 
 
run()