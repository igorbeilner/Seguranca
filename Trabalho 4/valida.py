#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
import base64
import sys

public_key = RSA.importKey(open('data/cert.pem').read())

file = open(sys.argv[1], 'r')
list_text = file.readlines()
text = list_text[0].replace('\n', '')
signature_orig = list_text[2].replace('\n', '')

hash = SHA256.new()
hash.update(text.encode('utf-8'))
sha = hash.digest()

signature = public_key.encrypt(sha, 32)

if str(signature) == str(signature_orig):
	print("Assinatura valida")
else:
	print("Assinatura invalida")
