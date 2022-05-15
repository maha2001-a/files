from fileinput import filename
from cryptography.fernet import Fernet
import os
key=Fernet.generate_key()
print(key)
fernet=Fernet(key)
with open('key.key','wb') as filekey:
    filekey.write(key)
with open('key.key','rb') as filekey:
    key=filekey.read()
#filename=input("enter filename.")
dir="E:/fyp2/codes/index_table_generation/files/AudioFiles"
dir_list = os.listdir(dir)
for y in dir_list:
    path=y
    with open(f'AudioFiles/{y}','rb') as file:
      originalaudio=file.read()
      encrypted=fernet.encrypt(originalaudio)
    with open(f"Encrypted_Audio/{path}",'wb') as encrypted_file:
       encrypted_file.write(encrypted)
       fernet=Fernet(key)
dir="E:/fyp2/codes/index_table_generation/files/Encrypted_Audio"
dir_list = os.listdir(dir)
for k in dir_list:
    with open(f"Encrypted_Audio/{k}",'rb') as enc_file:
       encrypted=enc_file.read()
       decrypted=fernet.decrypt(encrypted)
    with open(f"Decrypted_Audio/{k}",'wb') as dec_file:
        dec_file.write(decrypted)
