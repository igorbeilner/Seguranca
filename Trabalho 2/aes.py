from Crypto import Random
from Crypto.Cipher import AES
from sys import argv

def abre(i):
	F = open(argv[i])
	text = F.read()
	F.close()
	return text

chave = abre(1)
texto = abre(2)

IV = Random.new().read(AES.block_size)
try:
	cipher = AES.new(chave, mode=AES.MODE_CFB, IV=IV)
except ValueError as error:
	print error
	exit(0)

criptografado = IV + cipher.encrypt(texto)

descriptografado = cipher.decrypt(criptografado)[AES.block_size:]

print "\nTexto criptografado:\n", criptografado
print "\nTexto descriptografado:\n", descriptografado
