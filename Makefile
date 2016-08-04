all:
	gcc *.c -o DiffieHellman -Wall -pthread -lm
clean:
	rm DiffieHellman
run:
	./DiffieHellman
