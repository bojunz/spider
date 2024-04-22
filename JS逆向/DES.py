from Cryptodome.Cipher import DES
from time import time
import random, binascii

word = 'spider'
lts = str(int(time() * 1000))
salt = lts + str(random.randint(0, 9))
sign = 'fanyideskweb' + word + salt + 'Ygy_4c=r#e#4EX^NUGUc5'

key = b'maqudong'
iv = b'12345678'

def encrypt(key,iv,data):
    cipher = DES.new(key=key,mode=DES.MODE_CFB,IV=iv,)
    data = data.encode()
    serect = cipher.encrypt(data)
    return binascii.b2a_hex(serect)#将密文从二进制转换为16进制

def decrypt(key,iv,data):
    data = binascii.a2b_hex(data) #将密文从16进制转换为2进制
    cipher = DES.new(key=key, mode=DES.MODE_CFB, IV=iv) #使用相同的模式进行解密
    plain = cipher.decrypt(data).decode()
    return plain
res = encrypt(key,iv,sign)

print(res)
print(decrypt(key, iv, res))
