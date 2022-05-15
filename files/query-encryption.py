from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import hashlib
from re import S
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
word=input("enter word to find..")
import random
seedd=input("Enter seed..")
pwd=random.seed(seedd)
random.random=random.getrandbits(256)
pwd=random.getrandbits(256)
pwd=str(pwd)
#print(master_key)
findword_hashed = hashlib.sha256(word.encode('utf-8')).hexdigest()
findword_hashed=str(findword_hashed)
print("Hash..",len(findword_hashed),findword_hashed)
class AESCipher:
   def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

   def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))

   def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    #pwd = input('Password..: ')
    #pwd = hashlib.md5(pwd.encode())
    #pwd=pwd.hexdigest()
    #pwd=str(pwd)
    #pwd=pwd.zfill(128)
   # print("password..",pwd)
    encrypted_text= AESCipher(pwd).encrypt(word).decode('utf-8')
    print(len(encrypted_text),encrypted_text)
    decypted_text=AESCipher(pwd).decrypt(encrypted_text).decode('utf-8')
    print(decypted_text)
#pwd = pwd.encode('utf-8')
#word=word.encode('utf-8')
#print("paww,,",pwd)


binary_converted_a = ''.join(format(ord(c), 'b') for c in findword_hashed)
binary_converted_b = ''.join(format(ord(c), 'b') for c in encrypted_text)
#print("The Binary Representation is:", binary_converted)
#print(len(binary_converted_a),"string",binary_converted_a)
def xor_two_str(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)
print("XOR............")   
c=xor_two_str(binary_converted_a,binary_converted_b)
k=xor_two_str(binary_converted_a,c)
print(k==binary_converted_b)
