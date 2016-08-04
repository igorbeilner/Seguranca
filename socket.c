#include "diffie.h"

void die(char *s) {
	perror(s);
	exit(1);
}

void interface(void) {
	int cifra;

	cifra = (int)pow(_BASE, _CHAVE) % _PRIMO;
	
	while(!_FLAG)
		packetSend(cifra);

}

void packetSend(int cifra) {

	struct sockaddr_in si_other;
	int s;
	socklen_t slen = sizeof(si_other);

	if((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
		die("socket");

	memset((char *) &si_other, 0, sizeof(si_other));
	si_other.sin_family = AF_INET;
	si_other.sin_port = htons(_PORT_VIZ);

	if(inet_aton(_IP, &si_other.sin_addr) == 0) {
		fprintf(stderr, "inet_aton() failed\n");
		exit(1);
	}

	if(sendto(s, &cifra, sizeof(int) , 0, (struct sockaddr *) &si_other, slen)==-1)
		die("sendto()");

	close(s);
}

void packetReceive(void) {

	struct sockaddr_in si_me, si_other;
	int s, recv_len, receive, cifra, flag=0;
	socklen_t slen = sizeof(si_other);

	if((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
		die("socket");

	memset((char *) &si_me, 0, sizeof(si_me));

	si_me.sin_family = AF_INET;
	si_me.sin_port = htons(_PORT);
	si_me.sin_addr.s_addr = htonl(INADDR_ANY);

	if(bind(s, (struct sockaddr*)&si_me, sizeof(si_me)) == -1)
		die("bind");

	while(1) {
		fflush(stdout);

		receive = 0;

		if((recv_len = recvfrom(s, &receive, sizeof(int), 0, (struct sockaddr *) &si_other, &slen)) == -1)
			die("recvfrom()");

		cifra = (int)pow(receive, _CHAVE) % _PRIMO;

		if(receive != -1 && !flag) {
			printf("|-----------------------------|\n");
			printf("|--------- Cifra: %-3d --------|\n", receive);
			printf("|--------- Chave: %-3d --------|\n", cifra);
			printf("|-----------------------------|\n");

			flag = 1;
			packetSend(-1);
			if(_FLAG == 1) return;
		} else if(receive == -1) {
			_FLAG = 1;
			if(flag == 1) return;
		}
	}
	close(s);
}
