from sys import argv

data = open(argv[1], 'r').read()

words = open('../data/palavras.in', 'rb').read()
words = words.split()

for chave in range(0, 255):
	k = ''
	for l in data:
		k = int((ord(l) - chave) % 256)
	string = chr(k)
	lista_palavras = str(string).split()
	words = []
	for word in lista_palavras:
		if word in words:
			words.append(word)
	
	if(len(words) > 0):
		print(chave)
		break
		