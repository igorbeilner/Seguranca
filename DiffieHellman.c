#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
	long base, chave, secreto, cifra, cifra2, chave2;

	scanf("%ld %ld %ld", &base, &chave, &secreto);

	cifra = (long)pow(base, secreto) % chave;

	printf("[  %ld  ]\n", cifra);

	scanf("%ld", &cifra2);

	chave2 = (long)pow(cifra2, secreto) % chave;

	printf("[  %ld  ]\n", chave2);

	return 0;
}