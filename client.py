#!/usr/bin/python
'''
Author : Bruno
Referencia: https://www.youtube.com/watch?v=8FDkCEJn4f8&index=22&list=UUcX6pS9qepQEez4uVP6JqJA
'''
import xmlrpclib

def main():
    print("Esse eh o cliente!")

    client = xmlrpclib.ServerProxy("http://localhost:8081")
    valor1 = input("Digite o valor 1: ")
    valor2 = input("Digite o valor 2: ")
    resultado = client.adiciona(valor1, valor2)
    print("Resultado da soma == "+str(resultado))

if __name__ == "__main__":
    main()
