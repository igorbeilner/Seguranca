#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from sys import argv
from itertools import cycle

file = open(argv[1], 'r')
msg = file.read()

chave = str(argv[2])
chave = [ord(i) for i in chave]

msg_cifrada = '' 
cifra = open('data/cifrado.out', 'w')
for (c,m) in zip(cycle(chave), msg):
	k = chr(int(ord(m) + c) % 256)
	msg_cifrada += k
	cifra.write(k)
print("Cifrado")

decifra = open('data/decifrado.out', 'w')
for (c, m) in zip(cycle(chave), msg_cifrada):
	k = chr(int(ord(m) - c) % 256)
	decifra.write(k)
print("Decifrado")
