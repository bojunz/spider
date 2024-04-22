import rsa
import binascii
from time import time
import random
import base64

def encrypt(n,e,data):
    #生成公钥
    key = rsa.PublicKey(n,e)
    res= rsa.encrypt(data.encode(),key)
    return binascii.b2a_hex(res)



word = 'xixi'

pubkey_n = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2MCiePD6J676YdXiNks2Bh/6rwI743T5UXHk6SHo1nvfctsGlDcelZuoaHMvSh4360uaONcen91b09vjfJ7OJhuM2HQdKagdJCQF+apY5V3xazc9NdQmj9weemBeC1KzffoSBeFnVN9tE6vypXbvfHIKtLl/4A6N1Lujdp+T8DQIDAQAB'
pubkey_e = '10001'
pubkey_n_bytes = base64.b64decode(pubkey_n)  # Decode from Base64
pubkey_n_hex = binascii.hexlify(pubkey_n_bytes).decode()
rsa_n = int(pubkey_n_hex,16)
rsa_e = int(pubkey_e,16)

print(encrypt(rsa_n,rsa_e,word))