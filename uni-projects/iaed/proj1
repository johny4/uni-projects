#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


/* Os define associdados a vetores do tipo char têm um incremento de uma 
unidade devido ao \n */
#define MAXAEROS 40
#define MAXVOOS 30000
#define CID 4
#define MAXCIDADE 51
#define MAXPAIS 31
#define MAXCODIGO 7


/* Variável global usada para a qualquer momento saber o número de aeroportos/
voos existentes e ser usado como índice */
int apcount = 0;
int vcount = 0;


/* Variáveis globais para armazenar a data do sistema */
int sismes = 01;
int sisdia = 01;
int sisano = 2022;


/* Adicionada a variável cnrvoos para saber o #voos a aterrar neste aeroporto */
struct aeroporto {
	char id[CID];
	char pais[MAXPAIS];
	char cidade[MAXCIDADE];
	int nrvoos;
	int cnrvoos;
};


struct aeroporto aeroportos [MAXAEROS];


struct voo {
	char codigo[MAXCODIGO], partida[CID], chegada[CID];
	int dia, mes, ano;
	int horas, minutos;
	int dhoras, dminutos;
	int capacidade;
	int cdia, cmes, cano;
	int choras, cminutos;
};


struct voo voos [MAXVOOS];

/* Estes array serão usado pelas funções p e c para ordenar cópias parciais 
dos voos */
struct voo pvoos [MAXVOOS];
struct voo cvoos [MAXVOOS];


/* Declaração de funções auxiliares que fazem verificações necessárias */
int tcheck(int dia, int mes, int ano);
int vcheck(char codigo[MAXCODIGO], int dia, int mes, int ano, char partida[CID], 
	char chegada[CID], int dminutos, int dhoras, int capacidade);
int data(struct voo voo1, struct voo voo2);
int cdata(struct voo voo1, struct voo voo2);
void chegada(int index);


/* Função insertion sort usada para ordenar os aeroportos quando o comando l é 
executado sem argumentos */
void asort() {
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
void psort(char ID[CID], int nrvoos) {
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
void csort(char id[CID], int cnrvoos) {
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


void a(char id[CID], char pais[MAXPAIS], char cidade[MAXCIDADE]) {
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


void l() {
	char c;
	char ident[4];
	int i, j, flag;
	c = getchar();
	
	if (c == '\n') {
		asort();
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


void v() {
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


void t() {
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


void p() {
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
		psort(aeroportos[i].id, aeroportos[i].nrvoos);

		for (j=0; j < vcount; j++) {
			if (strcmp(pvoos[j].partida, id) == 0) {
				printf("%s %s %02d-%02d-%d %02d:%02d\n", pvoos[j].codigo, 
					pvoos[j].chegada, pvoos[j].dia, pvoos[j].mes, pvoos[j].ano,
					 pvoos[j].horas, pvoos[j].minutos);	}
		}
	}
}

void c() {
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
				chegada(k);
			}}
		i--;
		csort(aeroportos[i].id, aeroportos[i].cnrvoos);

		for (j=0; j < vcount; j++) {
			if (strcmp(cvoos[j].chegada, id) == 0) {
				printf("%s %s %02d-%02d-%d %02d:%02d\n", cvoos[j].codigo, 
					cvoos[j].partida, cvoos[j].cdia, cvoos[j].cmes, 
					cvoos[j].cano, cvoos[j].choras, cvoos[j].cminutos);	}
		}}
}


int main() {
	char arg1[CID], arg2[MAXPAIS], arg3[MAXCIDADE], cmd;
	while(1) {
	cmd = getchar();

	switch(cmd) {
		case 'q':
			exit(0);
		case 'a': {
			scanf("%s %s %[^\n]s", arg1, arg2, arg3);
			a(arg1, arg2, arg3);
			break; }
		case 'l':
			l();
			break;
		case 'v':
			v();
			break;
		case 'p':
			p();
			break;
		case 'c':
			c();
			break;
		case 't':
			t();
			break; }}
	return 0; }


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

		if (capacidade > 100 || capacidade < 10) {
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
void chegada(int index) {
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
