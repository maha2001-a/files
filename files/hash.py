from ctypes.wintypes import PDWORD
import hashlib
import hmac
import random
update_bytes = 'Python123'.encode('utf-8')
password = "12345".encode('utf-8')
import secrets
sys_random = secrets.SystemRandom()
seedd=input("enter password..")
pwd=random.seed(seedd)
pwd=random.getrandbits(256)
pwd=str(pwd)
#print(pwd)
#print(len(pwd))
pwd = hashlib.sha256(pwd.encode())
pwd=pwd.hexdigest()
#print("Password length..",len(pwd))
session_key=sys_random.getrandbits(256)
session_key=str(session_key).encode('utf-8')
#print(session_key)
pwd=pwd.encode('utf-8')
my_hmac = hmac.new(update_bytes, session_key, hashlib.sha256) #Create hash using md5 algorithm
print("The first digest: " + str(my_hmac.digest()))
#print("The Canonical Name: " + my_hmac.name)
#my_hmac_cpy = my_hmac.copy() #Create a copy of the hmac object
#print("The Copied digest: " + str(my_hmac_cpy.digest()))
my_hmac=str(my_hmac)
print(my_hmac)