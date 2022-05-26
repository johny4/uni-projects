/* Declaração de funções auxiliares que fazem verificações necessárias às 
funções principais */
#include "structs.h"

int tcheck(int dia, int mes, int ano);
int vcheck(char codigo[], int dia, int mes, int ano, char partida[], 
	char chegada[], int dminutos, int dhoras, int capacidade);
int data(struct voo voo1, struct voo voo2);
int cdata(struct voo voo1, struct voo voo2);
void datachegada(int index);
int indice_voo(char idvoo[], int dia, int mes, int ano);
void elimina_voo(int index);
int rcheck(char* idreserva, char idvoo[], int dia, int mes, int ano, 
	int passageiros, int i, struct reserva* head); 
struct reserva* elimina_reservas(struct reserva* head, char idvoo[]);
int rcheck2(char idvoo[], int dia, int mes, int ano, int indice);
int valida_codigo(struct reserva* head, char codigo[]);

