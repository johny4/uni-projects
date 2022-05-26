/* Este projeto consiste num gestor de voos e reservas, permitindo criar
aeroportos, voos e reservas, listá-los ou eliminá-los. Foi desenvolvido no
âmbibto da UC de Introdução aos Algoritmos e Estruturas de Dados.

Autor: João Trocado (ist1103333) */


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "auxiliares.h"


/* Variável global usada para a qualquer momento saber, respetivamente,
o número de aeroportos e voos existentes a qualquer momento */
int apcount = 0;
int vcount = 0;


/* Variáveis globais para armazenar a data do sistema */
int sismes = 01;
int sisdia = 01;
int sisano = 2022;

struct aeroporto aeroportos [MAXAEROS];
struct voo voos [MAXVOOS];

/* Estes arrays serão usado pelas funções p e c para ordenar cópias parciais 
dos voos */
struct voo pvoos [MAXVOOS];
struct voo cvoos [MAXVOOS];



/* Função principal que termina o programa, libertando toda a memórida 
alocada */
void sair(struct reserva* head) {
	struct reserva *temp = head;
	while (head != NULL) {
		free(head->idreserva);
		temp = head->next;
		free(head);
		head = temp;
	}
	exit(0);
}


/* Função insertion sort usada para ordenar os aeroportos quando o comando l é 
executado sem argumentos */
void ordena_aeroportos() {
    int i, j;
    struct aeroporto temp;

	for(i = 1; i < apcount; i++) {
		temp = aeroportos[i];
		j = i - 1;
		
		while((strcmp(temp.id, aeroportos[j].id) < 0) && (j >= 0)) {
			aeroportos[j+1] = aeroportos[j];
			j--; }
		aeroportos[j+1] = temp;
	}
    
    return;
}

/* Função insertion sort usada para ordenar os voos quando o comando p é 
executado */
void ordena_partida(char ID[CID], int nrvoos) {
    int i, j, k, l;
    struct voo temp;

    l = 0;
	for (k = 0; l < nrvoos; k++) { 
		if (strcmp(voos[k].partida, ID) == 0) { 
			pvoos[l] = voos[k];
			l++; }}

	for(i = 1; i < nrvoos ; i++) {
		temp = pvoos[i];
		j = i - 1;

		while((data(temp, pvoos[j]) == 1) && (j >= 0)) {
			pvoos[j+1] = pvoos[j];
			j--; }
		pvoos[j+1] = temp;
	}
    return;
}

/* Função insertion sort usada para ordenar os voos quando o comando c 
é executado */
void ordena_chegada(char id[CID], int cnrvoos) {
    int i, j, k, l;
    struct voo temp;

    l = 0;
	for (k = 0; l < cnrvoos; k++) { 
		if (strcmp(voos[k].chegada, id) == 0) { 
			cvoos[l] = voos[k];
			l++; }}

	for(i = 1; i < cnrvoos ; i++) {
		temp = cvoos[i];
		j = i - 1;

		while((cdata(temp, cvoos[j]) == 1) && (j >= 0)) {
			cvoos[j+1] = cvoos[j];
			j--; }
		cvoos[j+1] = temp;
	}
    return;
}

/* Função insertion sort usada para ordenar e imprimir as reservas quando o 
comando r é executado apenas com um ID de voo e uma data */
void imprime_reservas(struct reserva *vetor, int nrreservas) {
    int i, j, l;
    struct reserva temp;

	for(i = 1; i < nrreservas; i++) {
		temp = vetor[i];
		j = i - 1;


		while((j >= 0) && (strcmp(temp.idreserva, vetor[j].idreserva) < 0)) {
			vetor[j+1] = vetor[j];
			j--; }
		vetor[j+1] = temp;
	}

	for (l = 0; l < nrreservas; l++) {
		printf("%s %d\n", vetor[l].idreserva, vetor[l].passageiros);
	}
    
    return;
}


/* Esta função principal cria um aeroporto quando os argumentos 
necessários são passados */
void cria_aeroporto(char id[CID], char pais[MAXPAIS], char cidade[MAXCIDADE]) {
	int i, j, len;

	if (apcount < MAXAEROS) {

		for (j=0; j < apcount; j++) {
			if (strcmp(id, aeroportos[j].id) == 0) {
				printf("duplicate airport\n");
				return;
			}}

	len = strlen(id);
	i = 0;
	for (i = 0; i < len; i++) {
		if (!(isupper(id[i]))) {
			printf("invalid airport ID\n");
			return;
		}}

	strcpy(aeroportos[apcount].id, id);
	strcpy(aeroportos[apcount].pais, pais);
	strcpy(aeroportos[apcount].cidade, cidade);
	printf("airport %s\n", aeroportos[apcount].id);
	apcount++;
	}

	else {
		printf("too many airports\n");
	}}


/* Esta função principal imprime todos os aeroportos existentes no sistema por 
ordem alfabética do seu código */
void lista_aeroportos() {
	char c;
	char ident[4];
	int i, j, flag;
	c = getchar();
	
	if (c == '\n') {
		ordena_aeroportos();
		for (j=0; j < apcount; j++) {
			printf("%s %s %s %d\n", aeroportos[j].id, aeroportos[j].cidade, 
				aeroportos[j].pais, aeroportos[j].nrvoos); }}

	while (c != '\n') {
		flag = 0;
    	scanf("%s", ident);
    	i = 0;
    	for (i = 0; i < apcount; i++) {
        	if (strcmp(ident, aeroportos[i].id) == 0) {
        		flag = 1;
        		printf("%s %s %s %d\n", aeroportos[i].id, aeroportos[i].cidade, 
        			aeroportos[i].pais, aeroportos[i].nrvoos);
    	}}
        
        if (flag==0) {
        	printf("%s: no such airport ID\n", ident); }
        c = getchar(); }
	return;
}


/* Esta função principal cria um aeroporto quando os argumentos 
necessários são passados ou lista todos os voos existentes por ordem
de criação se for chamado sem argumentos */
void cria_voo() {
	char partida[CID], chegada[CID], codigo[MAXCODIGO], c = getchar();
	int dia, mes, ano, horas, minutos, dhoras, dminutos, capacidade, j, k, l, 
	flag, flag2;
	
	if (c == '\n') {
		for (j=0; j < vcount; j++) {
			printf("%s %s %s %02d-%02d-%d %02d:%02d\n", voos[j].codigo, 
				voos[j].partida, voos[j].chegada, voos[j].dia, voos[j].mes, 
				voos[j].ano, voos[j].horas, voos[j].minutos);	}
		return; }

	scanf("%s %s %s", codigo, partida, chegada);
	scanf("%02d-%02d-%d",&dia, &mes, &ano);
	scanf("%02d:%02d", &horas, &minutos);
	scanf("%02d:%02d", &dhoras, &dminutos);
	scanf("%d", &capacidade);

	if (vcheck(codigo, dia, mes, ano, partida, chegada, dminutos, dhoras, 
		capacidade) == 1) {
		return; }

	flag = 0;
	for (k=0; ((k < apcount) && (flag == 0)); k++) {
		if (strcmp(partida, aeroportos[k].id) == 0) {
			aeroportos[k].nrvoos++;
			flag = 1;
		}
	}

	flag2 = 0;
	for (l=0; ((l < apcount) && (flag2 == 0)); l++) {
		if (strcmp(chegada, aeroportos[l].id) == 0) {
			aeroportos[l].cnrvoos++;
			flag2 = 1;
		}
	}

	strcpy(voos[vcount].codigo, codigo);
	strcpy(voos[vcount].partida, partida);
	strcpy(voos[vcount].chegada, chegada);
	voos[vcount].dia = dia;
	voos[vcount].mes = mes;
	voos[vcount].ano = ano;
	voos[vcount].horas = horas;
	voos[vcount].minutos = minutos;
	voos[vcount].dhoras = dhoras;
	voos[vcount].dminutos = dminutos;
	voos[vcount].capacidade = capacidade;
	vcount++; }


/* Esta função principal define o tempo atual do sistema */
void define_tempo() {
	int dia, mes, ano;
	scanf("%02d-%02d-%d",&dia, &mes, &ano);
	if (tcheck(dia, mes, ano) == 1) {
		return;
	}
	else {
		printf("%02d-%02d-%d\n", dia, mes, ano);
		sisdia = dia;
		sismes = mes;
		sisano = ano;
	}}


/* Esta função principal lista todos os voos com partida no aeroporto 
com o código passado como argumento */
void lista_partida() {
	int i, j, flag;
	char id[CID];
	scanf("%s", id);

	flag = 0;
	for (i=0; ((i < apcount) && (flag == 0)); i++) {
		if (strcmp(id, aeroportos[i].id) == 0) {
			flag = 1;
		}
	}

	if (flag == 0) {
		printf("%s: no such airport ID\n", id);
		return; }

	else {
		i--;
		ordena_partida(aeroportos[i].id, aeroportos[i].nrvoos);

		for (j=0; j < vcount; j++) {
			if (strcmp(pvoos[j].partida, id) == 0) {
				printf("%s %s %02d-%02d-%d %02d:%02d\n", pvoos[j].codigo, 
					pvoos[j].chegada, pvoos[j].dia, pvoos[j].mes, pvoos[j].ano,
					 pvoos[j].horas, pvoos[j].minutos);	}
		}
	}
}


/* Esta função principal lista todos os voos com chegada ao aeroporto 
com o código passado como argumento */
void lista_chegada() {
	int i, j, k, flag;
	char id[CID];
	scanf("%s", id);

	flag = 0;
	for (i=0; ((i < apcount) && (flag == 0)); i++) {
		if (strcmp(id, aeroportos[i].id) == 0) {
			flag = 1; }}

	if (flag == 0) {
		printf("%s: no such airport ID\n", id);
		return; }

	else {
		for (k = 0; k < vcount; k++) {
			if (strcmp(voos[k].chegada, id) == 0) {
				datachegada(k);
			}}
		i--;
		ordena_chegada(aeroportos[i].id, aeroportos[i].cnrvoos);

		for (j=0; j < vcount; j++) {
			if (strcmp(cvoos[j].chegada, id) == 0) {
				printf("%s %s %02d-%02d-%d %02d:%02d\n", cvoos[j].codigo, 
					cvoos[j].partida, cvoos[j].cdia, cvoos[j].cmes, 
					cvoos[j].cano, cvoos[j].choras, cvoos[j].cminutos);	}
		}}
}

struct reserva* cria_reserva(struct reserva *head) {
	char idvoo[MAXCODIGO], idreserva[MAXINPUT], c;
	int dia, mes, ano, passageiros, i, j;

	scanf("%s", idvoo);
	scanf("%02d-%02d-%d", &dia, &mes, &ano);

	c = getchar();
	i = indice_voo(idvoo, dia, mes, ano);

	/* Criação de nova reserva */
	if (c != '\n') {
		struct reserva *newHead;
		scanf("%s %d", idreserva, &passageiros); 
		newHead = malloc(sizeof(struct reserva));
		if (newHead == NULL) {
			printf("No memory\n");
			sair(head);
		}
		newHead->idreserva = malloc(sizeof(char)*(strlen(idreserva)+1));
		if (newHead->idreserva == NULL) {
			printf("No memory\n");
			sair(head);
		}
		strcpy(newHead->idreserva, idreserva);

		if (rcheck(newHead->idreserva, idvoo, dia, mes, ano, passageiros, 
			i, head) == 1) {

			/* Insere uma nova reserva à cabeça da lista ligada */
	    	newHead->next = head;
			newHead->passageiros = passageiros;
			newHead->dia = dia;
			newHead->mes = mes;
			newHead->ano = ano;
	    	strcpy(newHead->idvoo, idvoo);

	    	voos[i].reservas++;
	    	voos[i].capacidade -= passageiros;
			return newHead;
		}
		else {
			free(newHead->idreserva);
			free(newHead);
			return head;
		}
	}


	/* É criado um vetor-ponteiro temporário para ordenar e imprimir as 
	reservas associadas ao voo dado como input */
	else {
		if (rcheck2(idvoo, dia, mes, ano, i) == 1) { 
			struct reserva *atual, *temp; 
			int k;
			k = 0;
			j = indice_voo(idvoo, dia, mes, ano);
			temp = malloc(sizeof(struct reserva)*voos[j].reservas);

			if (temp == NULL) {
				printf("No memory\n");
				sair(head);
			}

			atual = head;
			while (atual != NULL && k < voos[j].reservas) {
				if (strcmp(atual->idvoo, idvoo) == 0 && atual->dia == dia &&
				atual->mes == mes && atual->ano == ano) {
					temp[k] = *atual;
					k++;
				}
				atual = atual->next;
			}

			imprime_reservas(temp, k);
			free(temp);
			return head;
		}
	}
	return head;
}	


/* Esta função principal recebe um código de voo ou reserva e elimina,
respetivamente, o voo e todas as reservas associadas a este ou a reserva com o 
código passado */
struct reserva* eliminar(struct reserva *head) {
	char* codigo = malloc(MAXINPUT);
	int i, verifica;
	struct reserva *atual, *anterior, *newHead;

	if (codigo == NULL) {
			printf("No memory\n");
			sair(head);
	}

	scanf("%s", codigo);
	verifica = valida_codigo(head, codigo);

	if (verifica == -2) {
		printf("not found\n");
		return head;
	}

	/* Elimina a reserva de código dado como input */
	if (verifica == -1) {
		atual = head;

		/* Elimina o primeiro node e altera a head */
		if (atual != NULL && strcmp(atual->idreserva, codigo) == 0) {
			i = indice_voo(atual->idvoo, atual->dia, atual->mes, atual->ano);
			voos[i].reservas--;
			voos[i].capacidade += atual->passageiros;
			newHead = atual->next;
			free(atual->idreserva);
			free(atual);
			return newHead;
		}


		while ((atual != NULL) && (strcmp(atual->idreserva, codigo) != 0)) {
			anterior = atual;
			atual = atual->next;
		}

		if (atual == NULL) {
			return head;
		}


		i = indice_voo(atual->idvoo, atual->dia, atual->mes, atual->ano);
		voos[i].reservas--;
		voos[i].capacidade += atual->passageiros;

		anterior->next = atual->next;
		free(atual->idreserva);
		free(atual);
		return head;

	}

	/* Eliminar um voo e todas as reservas associadas a este */
	else {
		newHead = elimina_reservas(head, codigo);
		elimina_voo(verifica);
		free(codigo);
		return newHead; 
	}
}

int main() {
	struct reserva *head = NULL;
	char arg1[CID], arg2[MAXPAIS], arg3[MAXCIDADE], cmd;
	while(1) {
	cmd = getchar();

	switch(cmd) {
		case 'q': {
			sair(head);
			break; }
		case 'a': {
			scanf("%s %s %[^\n]s", arg1, arg2, arg3);
			cria_aeroporto(arg1, arg2, arg3);
			break; }
		case 'l':
			lista_aeroportos();
			break;
		case 'v':
			cria_voo();
			break;
		case 'p':
			lista_partida();
			break;
		case 'c':
			lista_chegada();
			break;
		case 't':
			define_tempo();
			break;
		case 'r':
			head = cria_reserva(head);
			break;
		case 'e':
			head = eliminar(head);
			break; }}
	return 0; }


/* Função auxiliar que retorna -2, j ou -1 se o código introduzir for,
respetivamente, inexistente, de um voo, ou de uma reserva 
j é o índice do voo no array global */
int valida_codigo(struct reserva* head, char codigo[]) {
    struct reserva* atual = head;
    int j;

    for (j=0; j < vcount; j++) {
		if (strcmp(voos[j].codigo, codigo) == 0) {
			return j;
		}
	}

    while (atual != NULL) {
        if (strcmp(atual->idreserva, codigo) == 0) {
            return -1; 
        }
        atual = atual->next;
    }
    return -2;
}

/* Função auxiliar que elimina um voo do arry global de voos */
void elimina_voo(int index) {
	int i, j, k, l, m, count;
	struct voo copia[MAXVOOS];
	l = 0, count = 0;


	/* index é um índice do array global de voos onde está um armazenado um
	voo. todos os voos que este código serão elimindados */

	for (i = 0; i < vcount; i++) {
		if (strcmp(voos[i].codigo, voos[index].codigo) != 0) {
			copia[l] = voos[i];
			l++; }
		else {
			count++;
		}
	}

	vcount -= count;
	for (m = 0; m < vcount; m++) {
		voos[m] = copia[m];
	}
	

	for (j = 0; j < apcount; j++) {
		if (strcmp(voos[index].partida, aeroportos[j].id) == 0) {
			aeroportos[j].nrvoos -= count;
		}
	}

	for (k = 0; k < apcount; k++) {
		if (strcmp(voos[index].chegada, aeroportos[k].id) == 0) {
			aeroportos[k].nrvoos -= count;
		}
	}
}


/* Função auxiliar que elimina todas as reservas associadas a um voo, quando
este é eliminado */
struct reserva* elimina_reservas(struct reserva* head, char idvoo[]) {
    struct reserva *atual, *anterior, *newHead;
    atual = head;
    newHead = head;
    anterior = NULL;
 
    /* Elimina o primeiro node e altera a head */
    while (atual != NULL && strcmp(atual->idvoo, idvoo) == 0) {
        newHead = atual->next;
        free(atual->idreserva);
        free(atual);
        atual = newHead;
    }
 
    while (atual != NULL) {
        while ((atual != NULL) && (strcmp(atual->idvoo, idvoo) != 0)) {
            anterior = atual;
            atual = atual->next;
        }
 
 		/* Se o voo não tem reservas */
        if (atual == NULL) {
            return newHead;
        }
 
        anterior->next = atual->next;
        free(atual->idreserva);
		free(atual);
        atual = anterior->next;
    }
    return newHead;
}


/* Função auxiliar que devolve o índice de um voo no array global de voos,
recebendo como argumento o seu código e data */
int indice_voo(char idvoo[], int dia, int mes, int ano) {
	int j;
	for (j = 0; j < vcount; j++) {
    	if (strcmp(voos[j].codigo, idvoo) == 0 && voos[j].dia == dia &&
    		voos[j].mes == mes && voos[j].ano == ano) {
    		return j;
    	}
    }
    return -1;
}

/* Função auxiliar que verifica se os argumentos passados para a criação de
uma reserva são válidos e imprime erros, quando uma reserva é duplicada,
tem código inválido, está associdada a um voo inexistente, ou 
número de passageiros ou data inválidos, impedindo a sua criação */
int rcheck(char* idreserva, char idvoo[], int dia, int mes, int ano, 
	int passageiros, int indice, struct reserva* head) {

	int j, lenreserva;
	struct reserva *atual;

	lenreserva = strlen(idreserva);
	for (j = 0; j < lenreserva; j++) {
		if (!(lenreserva >= 10 && (isupper(idreserva[j]) || 
			isdigit(idreserva[j])))) {
			printf("invalid reservation code\n");
			return 0;
		}
	}

	if (indice == -1) {
		printf("%s: flight does not exist\n", idvoo);
		return 0;
	}

	atual = head;
	while (atual != NULL) {
		if (strcmp(atual->idreserva, idreserva) == 0) {
			printf("%s: flight reservation already used\n", idreserva);
			return 0;
		}
		else {
		atual = atual->next; 
		}
	}

	if ((voos[indice].capacidade - passageiros) < 0) {
		printf("too many reservations\n");
		return 0;
	}

	if (tcheck(dia, mes, ano) == 1) {
		return 0;
	}

	if (passageiros < 1) {
		printf("invalid passenger number\n");
		return 0;
	}
	return 1;
}

/* Função auxiliar que verifica se os argumentos passados para a listagem de
reservas de um voo são válidos e imprime erros, quando um voo não existe ou 
a data fornecida é inválida, impedido a sua listagem */
int rcheck2(char idvoo[], int dia, int mes, int ano, int indice) {

	if (indice == -1) {
		printf("%s: flight does not exist\n", idvoo);
		return 0;
	}

	if (tcheck(dia, mes, ano) == 1) {
		return 0;
	}

	return 1;
}

/* Função auxiliar que verifica se os argumentos passados para a criação de
um voo são válidos e imprime erros, quando um voo é duplicado, tem código
inválido, aeroporto de partida ou chegada inexistentes, ou capacidade ou 
duração inválidas, impedindo a sua criação */
int vcheck(char codigo[MAXCODIGO], int dia, int mes, int ano, char partida[CID],
 char chegada[CID], int dminutos, int dhoras, int capacidade) {
	int flag, flag2, flag3, i, k, l, m, len;

	if (vcount < MAXVOOS-1) {

		for (i=0; i < vcount; i++) {
			if (strcmp(codigo, voos[i].codigo) == 0) {
				if (dia == voos[i].dia && mes == voos[i].mes && ano == 
					voos[i].ano) {
				printf("flight already exists\n");
				return 1;
				}

			}
		}


		len = strlen(codigo);
		flag = 0;

		if (len < 7 && len > 2) {
			if (isupper(codigo[0]) && isupper(codigo[1])) {
				for (k=2; k < len; k++) {
					if (!(isdigit(codigo[k]))) {
						flag = 1;
					}
				}
			}

			else {
				flag = 1;
			}
		}

		else {
			flag = 1;
		}

		if (flag == 1) {
			printf("invalid flight code\n");
			return 1;
		}


		flag2 = 0;
		for (l=0; l < apcount; l++) {
			if (strcmp(partida, aeroportos[l].id) == 0) {
				flag2 = 1; 
			}
		}

		if (flag2 == 0) {
			printf("%s: no such airport ID\n", partida);
			return 1;
		}


		flag3 = 0;
		for (m=0; m < apcount; m++) {
			if (strcmp(chegada, aeroportos[m].id) == 0) {
				flag3 = 1;
			}
		}

		if (flag3 == 0) {
			printf("%s: no such airport ID\n", chegada);
			return 1;
		}

		if (tcheck(dia, mes, ano) == 1) {
			return 1;
		}

		if (dhoras > 12 || (dhoras == 12 && dminutos > 0)) {
			printf("invalid duration\n");
			return 1;
		}

		if (capacidade < 10) {
			printf("invalid capacity\n");
			return 1;
		}
	}

	else {
		printf("too many flights\n");
		return 1;
	}


	return 0;
}

/* Função auxiliar que verifica se uma data é válida para a criação de um voo,
face à data atual do sistema */
int tcheck(int dia, int mes, int ano) {
	if ((ano < sisano) || (ano == sisano && mes == sismes && dia < sisdia) ||
	 (ano == sisano && mes < sismes) || (ano > sisano && mes > sismes) ||
	  (ano > sisano && mes == sismes && dia > sisdia)) {
			printf("invalid date\n");
			return 1;
	}
	return 0;
}

/* Função auxiliar que compara datas e devolve 1 ou 2, respetivamente se o voo1 
for mais antigo ou recente que o voo2 */
int data(struct voo voo1, struct voo voo2) {
	if (voo1.ano > voo2.ano) {
		return 2; }
	else if (voo1.ano < voo2.ano) {
		return 1; }
	else {
		if (voo1.mes > voo2.mes) {
			return 2; }
		else if (voo1.mes < voo2.mes) {
			return 1; }
		else {
			if (voo1.dia > voo2.dia) {
				return 2; }
			else if (voo1.dia < voo2.dia) {
				return 1; }
			else {
				if (voo1.horas > voo2.horas) {
					return 2; }
				else if (voo1.horas < voo2.horas) {
					return 1; }
				else {
					if (voo1.minutos > voo2.minutos) {
						return 2; }
					else if (voo1.minutos < voo2.minutos) {return 1; }}}}}
	return 0; }

/* Função auxiliar que compara datas e devolve 1 ou 2, respetivamente se o voo1
for mais antigo ou recente que o voo2 */
int cdata(struct voo voo1, struct voo voo2) {
	if (voo1.cano > voo2.cano) {
		return 2; }
	else if (voo1.cano < voo2.cano) {
		return 1; }
	else {
		if (voo1.cmes > voo2.cmes) {
			return 2; }
		else if (voo1.cmes < voo2.cmes) {
			return 1; }
		else {
			if (voo1.cdia > voo2.cdia) {
				return 2; }
			else if (voo1.cdia < voo2.cdia) {
				return 1; }
			else {
				if (voo1.choras > voo2.choras) {
					return 2; }
				else if (voo1.choras < voo2.choras) {
					return 1; }
				else {
					if (voo1.cminutos > voo2.cminutos) {
						return 2; }
					else if (voo1.cminutos < voo2.cminutos) {return 1; }}}}}
	return 0; }

/*Função auxiliar para criar as datas de chegada */
void datachegada(int index) {
	voos[index].cminutos = voos[index].minutos + voos[index].dminutos;
	voos[index].choras = voos[index].horas + voos[index].dhoras;
	voos[index].cdia = voos[index].dia; voos[index].cmes = voos[index].mes;
	voos[index].cano = voos[index].ano;

	if (voos[index].cminutos > 59) {
		voos[index].cminutos -= 60;
		voos[index].choras++; }

	if (voos[index].choras > 23) {
		voos[index].choras -= 24;
		voos[index].cdia++; }

	/*  novembro abril junho setembro */
	if ((voos[index].cdia > 30) && (voos[index].cmes == 11 || voos[index].cmes 
		== 4 || voos[index].cmes == 6 || voos[index].cmes == 9)) {
		voos[index].cmes++;
		voos[index].cdia -= 30; }

	/*  janeiro março maio julho agosto outubro dezembro */
	if ((voos[index].cdia > 31) && (voos[index].cmes == 1 || voos[index].cmes 
		== 3 || voos[index].cmes == 5 || voos[index].cmes == 7 || 
		voos[index].cmes == 8 || voos[index].cmes == 10)) {
		voos[index].cmes++;
		voos[index].cdia -= 31; }

	/*  fevereiro comum */
	if ((voos[index].cdia > 28) && (voos[index].cmes == 2)) {
		voos[index].cmes++;
		voos[index].cdia -= 28; }

	/*  dezembro com passagem de ano */
	if ((voos[index].cdia > 31) && (voos[index].cmes == 12)) {
		voos[index].cano++;
		voos[index].cmes = 1;
		voos[index].cdia = 1; }
	
	return;
}
