<b>Universidade Federal da Fronteira Sul</b><br>
<b>Ciência da Computação - 8 fase</b><br>
<b>Segurança e Auditoria de Sistemas</b><br>

<i>Implementação do Cifra de César.</i>

Cifrar texto:
	$ python cesar.py data/text.in 1 <int(chave)>

Decifrar texto:
	$ python cesar.py data/cifrado.out 2 <int(chave)>

Ataque em claro:
	$ python ataque/ataque_claro.py data/text.in data/cifrado.out

Ataque por força bruta:
	$ python ataque/forca_bruta.py data/cifrado.out