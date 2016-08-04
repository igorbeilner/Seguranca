/*
 * Project name:
	Diffie Hellman

 * Autor:
	Igor Beilner

 * Revision History:
	Versão 1.0
	01/08/2016

 * Description:

 * Test configuration:

 * NOTES:
*/

#include "diffie.h"

int  _PORT;
int  _FLAG;
int  _PORT_VIZ;
int  _CHAVE;
char _IP[15];
long _BASE, _PRIMO;

void init(void) {
	FILE *F = fopen("config/init.config", "rb");

	if(F == NULL) {
		printf("ERRO: Arquivo init.config nao encontrado\n");
		exit(1);
	}

	fscanf(F, "%ld %ld %s", &_BASE, &_PRIMO, _IP);
	fclose(F);

	printf("PORTA		 :");
	scanf("%d", &_PORT);
	printf("PORTA VIZINHO 	 :");
	scanf("%d", &_PORT_VIZ);
	printf("CHAVE 		 :");
	scanf("%d", &_CHAVE);

	_FLAG = 0;
}

int main(void) {
	pthread_t recThread, sendThread;

	init();

	pthread_create(&recThread, 	NULL, 	(void *)packetReceive, 	NULL);
	pthread_create(&sendThread, NULL, 	(void *)interface, 	NULL);

	pthread_join(recThread, 	NULL);
	pthread_cancel(recThread);

	pthread_join(sendThread, 	NULL);
	
	return 0;
}
