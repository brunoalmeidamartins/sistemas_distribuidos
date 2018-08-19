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

    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0",8081))
    server.register_function(adiciona)
    print("Precione CRTL + C para finalizar...")
    server.serve_forever()

if __name__== "__main__":
    main()
