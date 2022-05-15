import random
import Crypto.Random.random 
seedd=input("Enter seed..")
key = random.getrandbits(256)
key=random.seed(seedd)
#random.random=random.getrandbits(256)
master_key=random.getrandbits(256)
master_key=str(master_key)
print(master_key)
print(len(master_key))