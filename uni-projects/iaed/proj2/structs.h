/* Os define associdados a vetores do tipo char têm um incremento de uma 
unidade devido ao \0 */
#define MAXAEROS 40
#define MAXVOOS 30000
#define CID 4
#define MAXCIDADE 51
#define MAXPAIS 31
#define MAXCODIGO 7
#define MAXINPUT 65536


/* Adicionada a variável cnrvoos para saber o #voos a aterrar neste aeroporto */
struct aeroporto {
	char id[CID];
	char pais[MAXPAIS];
	char cidade[MAXCIDADE];
	int nrvoos;
	int cnrvoos;
};

struct voo {
	char codigo[MAXCODIGO], partida[CID], chegada[CID];
	int dia, mes, ano;
	int horas, minutos;
	int dhoras, dminutos;
	int capacidade;
	int cdia, cmes, cano;
	int choras, cminutos;
	int reservas;
};

struct reserva {
	char idvoo[MAXCODIGO];
	char* idreserva;
	int dia, mes, ano;
	int passageiros;
	struct reserva *next;
};
