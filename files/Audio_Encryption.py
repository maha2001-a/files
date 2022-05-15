from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import os

key1 = input('enter key: ')
key1=hash(key1)
key=str(key1)
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

def encrypt(file_name, key):
    with open (file_name,'rb') as entry:
        data= entry.read()
        cipher= AES.new(key, AES.MODE_CFB)
        ciphertext= cipher.encrypt(pad(data, AES.block_size))
        iv= b64encode(cipher.iv).decode('UTF-8')
        ciphertext= b64encode(ciphertext).decode('UTF-8')
        to_write= iv +ciphertext
    entry.close()
    dir="E:/fyp2/codes/index_table_generation/files/AudioFiles"
    dir_list = os.listdir(dir)
    for y in dir_list:
       path=y
       with open (f"Encrypted_Audio/{path}.txt", "w") as data:
            data.write(to_write)
       data.close()
path_dir="E:/fyp2/codes/index_table_generation/files/AudioFiles"
dir_list = os.listdir(path_dir)
for x in dir_list:    
    encrypt(f'AudioFiles/{x}', key)