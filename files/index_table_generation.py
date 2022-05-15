from encodings import utf_8
from importlib.metadata import files
from msilib.schema import File
import os
from collections import Counter
from telnetlib import NOP
from xlsxwriter import Workbook
from hashlib import md5
from base64 import b64decode
import random
from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode
import hashlib
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
path_dir="E:/fyp2/codes/index_table_generation/files/Stemming"
dir_list = os.listdir(path_dir)
path_dir_audiofiles="E:/fyp2/codes/index_table_generation/files/AudioFiles"
dir_list_audiofiles = os.listdir(path_dir_audiofiles)
max_word=[]
file_list=[]
audio_file_list=[]
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num
for x in dir_list_audiofiles:
    #define text file to open
    my_file_audio = open(f"AudioFiles/{x}", 'r')
    audio_file_list.append(x)
for x in dir_list:
    #define text file to open
    my_file = open(f"Stemming/{x}", 'r')
    file_list.append(x)
    for line in my_file:
        for i in dir_list:
           i=line.split()
        print(i)
        max_count=most_frequent(i)
        max_word.append(max_count)
    #print(max_word)
    #print(file_list)

workbook = Workbook(f"Excel_Sheets/Ecl.xlsx")
Report_Sheet = workbook.add_worksheet()
# Write the column data.
Report_Sheet.write_column(0, 0, max_word)
Report_Sheet.write_column(0, 1, audio_file_list)

workbook.close()
# Write the column headers if required.
#Report_Sheet.write(0, 0, 'Key Words')
#Report_Sheet.write(0, 1, 'File Names')
seedd=input("enter password..")
pwd=random.seed(seedd)
random.random=random.getrandbits(256)
pwd=random.getrandbits(256)
pwd=str(pwd)
#print(len(pwd))
pwd = hashlib.sha256(pwd.encode())
pwd=pwd.hexdigest()


#read text file into list
   # data = my_file.read()
   # data_into_list= data.replace('\n', ' ').split(".")
  
# printing the data
   # print(data_into_list)
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
    Encrypted_list=[]
    Decrypted_list=[]
    for i in audio_file_list:
        encrypted_text= AESCipher(pwd).encrypt(i).decode('utf-8')
        #print(encrypted_text)
        Encrypted_list.append(encrypted_text)
    print("Encrypted_list",Encrypted_list)
    for j in Encrypted_list:
        decypted_text=AESCipher(pwd).decrypt(j).decode('utf-8')
        Decrypted_list.append(decypted_text)
    print("Decrypted list",Decrypted_list)
hashed_list=[]
for i in max_word :
    result = hashlib.sha256(i.encode())
    reslt=result.hexdigest()
    hashed_list.append(reslt)
print(hashed_list)
workbook2 = Workbook(f"Excel_Sheets/Encrypted.xlsx")
Report_Sheet = workbook2.add_worksheet()

# Write the column headers if required.
#Report_Sheet.write(0, 0, 'Key Words')
#Report_Sheet.write(0, 1, 'File Names')


# Write the column data.
Report_Sheet.write_column(0, 0, hashed_list)
Report_Sheet.write_column(0, 1, Encrypted_list)
my_file.close()
workbook2.close()


