
#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
import base64
import sys

text = open(sys.argv[1], 'r')
lista = text.readlines()

padroes = {}

for palavra in lista:
	palavra = palavra.replace("\n","")
	count = 0
	padrao = ''
	padrao_palavra = {}

	for c in palavra:
		if count == 0:
			padrao_palavra.update({c: count})
			padrao += str(count)
			count += 1
		else:
			if padrao_palavra.get(c) == None:
				padrao_palavra.update({c: count})
				padrao += str(count)
				count += 1
			else:
				padrao += str(padrao_palavra.get(c))
	
	padroes.update({palavra: padrao})

print(padroes)
