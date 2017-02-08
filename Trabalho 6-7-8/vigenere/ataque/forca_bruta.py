#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from itertools import cycle
from sys import argv
import itertools

lista = '0123456789abcdefghijklmnopqrstuvwxyz'

data = open(argv[1], 'rb').read()

words_english = open('data/palavras.in', 'rb').read()
words_english = words_english.split()

chaves_invalidas = []

for i in range(1, 4):
    r = itertools.product(lista, repeat=i)
    for i in r:
        chave = [-ord(j) for j in i]
        msg_decifrada = bytes((c + m) % 256 for (c, m) in zip(cycle(chave), data))
        lista_palavras = msg_decifrada.split()
        
        words = []
        for word in lista_palavras[0:30]:
            if word in words_english:
                words.append(word)

        if(len(words) > 5):
            open('data/decifrado.out', 'wb').write(msg_decifrada)
