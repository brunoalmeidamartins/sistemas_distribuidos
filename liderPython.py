from processo import Processo as pr
from random import randint
import time
import numpy as np
import os

def buscaIndexElemento(lista,id): #Retorna a posicao do elemento na lista
    i = 0
    index = 0
    for j in lista:
        if j.id == id:
            index = i
            break
        i = i +1
    return index
def verificaFalha(lista):
    print("Verificando se ha falha nos Nodos")
    for i in range(len(lista)):
        if i == 0:
            if lista[i].falha == True:
                pass
            else:
                id_vizinho = buscaIndexElemento(lista,lista[i].vizinho)
                print("Processo "+str(id_vizinho)+" verificando se ha falha")
                time.sleep(1)
                if lista[id_vizinho].falha:
                    #Se houver falha, inicia processo de eleicao
                    print("Erro na comunicao!!!!")
                    time.sleep(2)
                    print('')
                    print("Processo "+str(lista[i].id)+" indentificou que o processo "+str(lista[id_vizinho].id)+" morreu!!")
                    print("Processo "+str(lista[i].id)+" inicia uma eleicao")
                    print('')
                    #Chama eleicao
                    lista[i].comecou_eleicao = True
                    eleicaoLider(lista,lista[i].id,lista[i].prox_vizinho)
                    break
        else:
            id_vizinho = buscaIndexElemento(lista,lista[i].vizinho)
            print("Processo "+str(id_vizinho)+" verificando se ha falha")
            time.sleep(1)
            if lista[id_vizinho].falha:
                #Se houver falha, inicia processo de eleicao
                print("Erro na comunicao!!!!")
                time.sleep(2)
                print('')
                print("Processo "+str(lista[i].id)+" indentificou que o processo "+str(lista[id_vizinho].id)+" morreu!!")
                print("Processo "+str(lista[i].id)+" inicia uma eleicao")
                print('')
                #Chama eleicao
                lista[i].comecou_eleicao = True
                eleicaoLider(lista,lista[i].id,lista[i].prox_vizinho)
                break

def eleicaoLider(lista,id_processo,id_proxVizinho): #Elege um novo lider
    lista_candidatos = []
    print("Nova eleicao!!")
    lista_candidatos.append(id_processo)#Adiciona quem chamou a eleicao na lista
    print(lista_candidatos) #Imprime a lista de candidatos

    index_comecou_eleicao = buscaIndexElemento(lista, id_processo)

    candidato = id_proxVizinho #Chama o proximo vizinho de quem chamou a eleicao
    index_lista = buscaIndexElemento(lista,candidato)
    while(lista[index_lista].comecou_eleicao == False):
        lista_candidatos.append(candidato)
        candidato = lista[index_lista].vizinho
        index_lista = buscaIndexElemento(lista,candidato)
        time.sleep(1)
        print(lista_candidatos)
    #Retira a lideranca de quem era
    for i in lista:
        if i.isLider == True:
            i.isLider = False
            break
    #Seta o novo lider
    print("Buscando no lider na lista")
    time.sleep(1)
    id_novo_lider = np.max(lista_candidatos)
    print('')
    print("Id novo lider: ",id_novo_lider)
    index_lista = buscaIndexElemento(lista,id_novo_lider)
    lista[index_lista].isLider = True #Seta o novo lider

    print('')
    for i in lista:
        if i.isLider == True:
            print("Novo lider eh: ",i.id)
            break

    #Envia mensagem de novo lider para todos saberem
    print('\nEnvia mensagem na rede do novo lider \n')
    lista[index_comecou_eleicao].id_lider = id_novo_lider
    print("Processo "+str(lista[index_comecou_eleicao].id)+" -> Novo lider eh: "+str(id_novo_lider))
    index_lista = buscaIndexElemento(lista,lista[index_comecou_eleicao].prox_vizinho)
    while(lista[index_lista].comecou_eleicao == False):
        #index_processo = buscaIndexElemento(lista,id_vizinho)
        lista[index_lista].id_lider = id_novo_lider
        print("Processo "+str(lista[index_lista].id)+" -> Novo lider eh: "+str(id_novo_lider))
        index_lista = buscaIndexElemento(lista,lista[index_lista].vizinho)
        time.sleep(1)
    print(" ")
    lista[index_comecou_eleicao].comecou_eleicao = False #Seta falso para quem iniciou a eleicao


class main():
    quant_processos = 15
    ultimo_processo = quant_processos -1
    penultimo_processo = quant_processos-2
    primeiro_processo = 1
    segundo_processo = 2

    lista_processos = []

    ####Cria a lista de processos
    for i in range(quant_processos):
        if i == penultimo_processo:
            processo = pr(i+1,i+2,primeiro_processo)
            lista_processos.append(processo)
        elif i == ultimo_processo:
            processo = pr(i+1,primeiro_processo,segundo_processo)
            lista_processos.append(processo)
        else:
            processo = pr(i+1,i+2,i+3)
            lista_processos.append(processo)
    #Lista de Processos criados
    print("Lista de Processos Criados!!!")
    for i in lista_processos:
        #print("Id: "+str(i.id)+' Vizinho1: '+str(i.vizinho)+' Vizinho2: '+str(i.prox_vizinho))
        print("Processo: ",i.id)


    ###Fim da criacao da lista

    ###Inicio dos Testes
    numero_aleatorio = randint(0,quant_processos-1) # Gera um numero aleatorio
    lista_processos[numero_aleatorio].isLider == True #Escolhe um lider
    print('')
    print("Lider atual: "+str(lista_processos[numero_aleatorio].id))
    print('')
    #Preenche todos os processos com o lider escolhido
    for i in lista_processos:
        i.id_lider = lista_processos[numero_aleatorio].id
    for i in range(0,3): #Numero de execucoes
        numero_aleatorio = randint(0,quant_processos-1) # Gera um numero aleatorio
        lista_processos[numero_aleatorio].falha = True #Gera uma falha aleatoria
        #Inicia processo de verificacao na rede
        time.sleep(2)
        os.system('clear')
        print("Inicio de verificacao na rede!!")
        time.sleep(2)
        print(' ')
        verificaFalha(lista_processos) #Verifica se ha falha na rede
        lista_processos[buscaIndexElemento(lista_processos,numero_aleatorio)].falha = False #Seta a falha do processo como falso novamente
        print('\nFim do processo de verificacao \n')
