#!/usr/bin/python
'''
Author : Bruno
Referencia: https://www.youtube.com/watch?v=8FDkCEJn4f8&index=22&list=UUcX6pS9qepQEez4uVP6JqJA
'''
import SimpleXMLRPCServer

def adiciona(a,b):
    return a+b

def main():
    print("Esse eh um servidor!")

    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0",8081)) #Habilita o servidor no IP e Porta
    server.register_function(adiciona) #Registra a funcao
    print("Precione CRTL + C para finalizar...")
    server.serve_forever() # Loop

if __name__== "__main__":
    main()
