/*********************************
Autor: Fernando Krein Pinheiro
Data: 06/04/2011
Linguagem: C
========= IMPORTANTE ===========
O código esta livre para usar,
citar e compartilhar desde que
mantida sua fonte e seu autor.
Obrigado.
*********************************
 Esse algoritmo é apenas uma
 simulação do que um algoritmo
 de eleição em anel faz nos
 sistemas distribuidos.
********************************/
#include <stdlib.h>
#include <stdio.h>
#define TAM 5 /*aqui pode-se definir o numero de processos que se quer, precisa ser (>=2) */

struct Processos{
    int pid;
};
typedef struct Processos Processos;

int falha(){
      int falha;
      srand(time(NULL));
      falha = rand() % TAM;
      return falha;
}

int promove_eleicao(){
      int eleicao;
      eleicao = rand() % TAM;
      return eleicao;
}

int main(){
    Processos proc[TAM];
    int proc_falha = 0;

    int proc_eleicao = 0;
    int proc_lider = 0;
    int vet_proc[TAM],i,cont;

    if(TAM<2)
    {
      system("clear");
      printf("\033[31mERRO 666 :\033[37mVoce precisa ter pelo menos 2 processos.\n");
      sleep(3);
      exit(0);
    }
    system("clear");

    for(; cont<TAM+TAM; cont++){
      //inicializa os processo preenchendo a struct com numero do processo (PID)
       for(i=0; i<TAM; i++){
            vet_proc[i] = proc[TAM].pid = i;
       }
       do{
           proc_falha = falha();
           proc_eleicao = promove_eleicao();
       }while(proc_eleicao == proc_falha);

       //inicializa o processo com falha colocando -1
       for(i=0; i<TAM; i++){
           if(vet_proc[i] == proc_falha)
           vet_proc[i] = -1;
       }

       proc_lider = vet_proc[0];
       for(i=0; i<TAM; i++){//faz a escolha do novo lider
           if(vet_proc[i] > proc_lider)
           proc_lider = vet_proc[i];
       }
       printf("|\033[32m PROC PID\033[37m |\n");//faz a impressão na tela
       for(i=0; i<TAM; i++){
           printf("| [%d] [%d] |\n",vet_proc[i],proc[TAM].pid=i);
       }
       sleep(1);
       printf("\n\nProcesso de PID\033[31m [%d]\033[37m falhou.\n",proc_falha);
       sleep(2);
       printf("Processo de PID\033[33m [%d]\033[37m iniciou eleicao.\n",proc_eleicao);
       sleep(2);
       printf("\033[36mEscolhendo novo lider...\033[37m \n");
       sleep(3);
       printf("Processo de PID\033[33m [%d]\033[37m e o novo lider.\n",proc_lider);
       sleep(3);
       system("clear");
    }
return 0;
}
