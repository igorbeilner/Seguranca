#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from sys import argv

f_claro = open(argv[1], 'r')
claro = f_claro.read()

f_escuro = open(argv[2], 'r')
escuro = f_escuro.read()

chave = ''
for i, j in zip(claro, escuro):
    chave += chr((ord(j) - ord(i))%256)

print(chave)