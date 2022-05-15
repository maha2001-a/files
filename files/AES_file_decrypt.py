from Crypto import Cipher
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64decode, b64encode
import getpass

key = input(('enter key: '))
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

with open('1.mp3.txt','r') as entry:

        data=entry.read()
        length=len(data)
        iv=data[:24]
        iv=b64decode(iv)
        ciphertext=data[24:length]
        ciphertext=b64decode(ciphertext)
        cipher=AES.new(key,AES.MODE_CFB,iv)
        decrypted=cipher.decrypt(ciphertext)
#        decrypted=unpad(decrypted,AES.block_size)
        with open('1.mp3','wb') as data:
            data.write(decrypted)
        data.close()
