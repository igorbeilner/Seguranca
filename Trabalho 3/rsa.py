from Crypto import Random
from Crypto.PublicKey import RSA
from sys import argv

def abre(i):
	F = open(argv[i])
	text = F.read()
	F.close()
	return text

texto = abre(1)

random_generator = Random.new().read
ChavePrivada = RSA.generate(2**12, random_generator)
ChavePublica = ChavePrivada.publickey()

criptografado = ChavePublica.encrypt(texto, 32)
decriptografado = ChavePrivada.decrypt(criptografado)

print "\nTexto criptografado (chave publica):\n", criptografado
print "\nTexto decriptografado (chave privada):\n", decriptografado
