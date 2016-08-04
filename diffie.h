#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <unistd.h>
#include <math.h>

extern int  _CHAVE;
extern int  _PORT;
extern int  _FLAG;
extern int  _PORT_VIZ;
extern char _IP[15];
extern long _BASE, _PRIMO;

/********************* protótipos das funções **********************/
void init 			(void);
void interface 		(void);
void packetSend		(int cifra);
void packetReceive	(void);
void die 			(char *s);
