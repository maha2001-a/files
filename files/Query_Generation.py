from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import random
word=input("Enter word to find..")
BS = 32
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = sha256(key.encode('utf8')).digest()


    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')
seedd=input("enter password..")
pwd=random.seed(seedd)
random.random=random.getrandbits(256)
pwd=random.getrandbits(256)
pwd=str(pwd)
#print(len(pwd))
pwd = hashlib.sha256(pwd.encode())
pwd=pwd.hexdigest()
#print("Password length..",len(pwd))
random.random=random.getrandbits(256)
session_key=random.getrandbits(256)
session_key=str(session_key)
cipher = AESCipher(session_key)
encrypted_text = cipher.encrypt(word)
encrypted_text = encrypted_text.decode('utf-8')
decrypted_text = cipher.decrypt(encrypted_text)
print(len(encrypted_text),"Encrypted Text....",encrypted_text)
#print(decrypted_text)

#Hashing.......
findword_hashed = hashlib.sha256(word.encode('utf-8')).hexdigest()
findword_hashed=str(findword_hashed)
print(len(findword_hashed),"Hash..",findword_hashed)
k=findword_hashed
l=encrypted_text
#Coverting to binary
binary_converted_a = ''.join(format(ord(c), 'b') for c in k)
binary_converted_b = ''.join(format(ord(c), 'b') for c in l)
if (len(binary_converted_a)>=len(binary_converted_b)):
    n=len(binary_converted_a)
    binary_converted_b=binary_converted_b.ljust(n,'0')
else:
    l=len(binary_converted_b)
    binary_converted_a=binary_converted_a.ljust(l,'0')
#binary_converted_a=binary_converted_a.ljust(60, '0')
#binary_converted_b=binary_converted_b.ljust(60,'0')
print(binary_converted_a)
print(binary_converted_b)
def xor_two_str(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)
    
c=xor_two_str(binary_converted_a,binary_converted_b)
print(c)
o=xor_two_str(binary_converted_b,c)
print(o==binary_converted_a)

d = hashlib.sha256(k.encode('utf-8')).hexdigest()
d=str(d)
