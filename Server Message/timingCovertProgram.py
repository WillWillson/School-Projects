from socket import *
from time import sleep

port = 31337
zero = 0.025
ONE = 0.1

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", port))

s.listen(0)
print("Server is listening...")

c, addr = s.accept()

# Start of program

def zeros_ones(j):
    temp = ord(j)
    binStr = bin(temp)[2:].zfill(8)
    return binStr

# Overt message
msg = "Some message..\n"

covertMessage = "secret code" + "EOF"
covertMessageBin = ""
for j in covertMessage:
    covertMessageBin += zeros_ones(j)

n = 0
for i in msg:
    c.send(i.encode())
    if covertMessageBin[n] == 0:
        sleep(zero)
    else:
        sleep(ONE)
    sleep(0.1)
    n = (n + 1) % len(covertMessageBin)

# End
c.send("EOF".encode())
print("Message sent...")
c.close()
    
# ord command coverts characters to ascii
# bin coverts into binary
#.zfill(8) will determine how many zeros need to be added
#[2:] will get rid of the first 2 characters
