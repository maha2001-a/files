from importlib.metadata import files
from msilib.schema import File
import os
import random
from Crypto import Random
from collections import Counter
from xlsxwriter import Workbook
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64
BS = 32
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]
path_dir="E:/fyp2/codes/index_table_generation/files/Stemming"
dir_list = os.listdir(path_dir)
max_word=[]
file_list=[]
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num
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
    print(max_word)
    print(file_list)

workbook = Workbook(f"Stemming/Ecl.xlsx")
Report_Sheet = workbook.add_worksheet()

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

# Write the column data.
Report_Sheet.write_column(0, 0, max_word)
Report_Sheet.write_column(0, 1, file_list)

workbook.close()
#read text file into list
   # data = my_file.read()
   # data_into_list= data.replace('\n', ' ').split(".")
  
# printing the data
   # print(data_into_list)
class AESCipher:

    def __init__( self, key ):
        self.key = sha256(key.encode('utf8')).digest()


    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

   


cipher = AESCipher(pwd)
Encrypted_list=[]
Decrypted_list=[]
for i in file_list:
    encrypted_text= str(cipher.encrypt(i))
    print(len(encrypted_text))
    Encrypted_list.append(encrypted_text)
print("Encrypted_list",Encrypted_list)

hashed_list=[]
for i in max_word :
    result = hashlib.sha256(i.encode())
    result=result.hexdigest()
    hashed_list.append(result)
print(hashed_list)
workbook2 = Workbook(f"Stemming/Encrypted.xlsx")
Report_Sheet = workbook2.add_worksheet()

# Write the column headers if required.
#Report_Sheet.write(0, 0, 'Key Words')
#Report_Sheet.write(0, 1, 'File Names')


# Write the column data.
Report_Sheet.write_column(0, 0, hashed_list)
Report_Sheet.write_column(0, 1, Encrypted_list)
my_file.close()
workbook2.close()
find_word=input("Enter word to find..")
