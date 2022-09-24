from socket import *
from time import time
from sys import stdout

DEBUG = True
ONE = 0.07
covert_bin = ""

ip = "localhost" #"138.47.99.64"
port = 31337#31337

s = socket(AF_INET, SOCK_STREAM)

s.connect((ip, port))

data = s.recv(4096).decode()

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)

    if(DEBUG):
        stdout.write(f" {delta}\n")
        stdout.flush()


    if delta >= ONE:
        covert_bin += "1"
    else:
        covert_bin += "0"

s.close()

covert = ""
i = 0
while (i < len(covert_bin)):
    b = covert_bin[i:i + 8]
    try:
        covert += chr(int(f"0b{b}", 2))
    except:
        covert += "?"
    i += 8
print(covert)
