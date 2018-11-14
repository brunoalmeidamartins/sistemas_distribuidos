
from processo import Processo as pr
from random import randint

def buscaIndexElemento(lista,id): #Retorna a posicao do elemento na lista
    i = 0
    index = 0
    for j in lista:
        if j.id == id:
            index = i
            break
        i = i +1
    return index




quant_processos = 10
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

for i in lista_processos:
    print("Id: "+str(i.id)+' Vizinho1: '+str(i.vizinho)+' Vizinho2: '+str(i.prox_vizinho))

###Fim da criacao da lista

#lista_processos[2].falha = True
for y in range(10):
    numero_aleatorio = randint(0,quant_processos-1)
    print("Numero Aleatorio: ",numero_aleatorio)
    lista_processos[numero_aleatorio].falha = True #Causa falha no processo
    for i in lista_processos:
        #print("Processo: "+str(i.id)+" verificando se seu vizinho "+str(i.vizinho)+" esta Online")
        id_vizinho = i.vizinho
        #print("Posicao do viznho: ",buscaIndexElemento(lista_processos,id_vizinho))
        indice_vizinho = buscaIndexElemento(lista_processos,id_vizinho)
        if lista_processos[indice_vizinho].falha:
            print("Processo "+str(lista_processos[indice_vizinho].id)+" Morreu")
            print("Nova Eleicao")
        else:
            print(' ')
            #print("Processo Ativo")
