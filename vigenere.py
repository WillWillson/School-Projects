import sys

# retrieve mode and key
mode = sys.argv[1]
key = sys.argv[2]

try: 
    while (True):
        # retrieve message to be encrypted or decrypted
        message = input()

        # create list of int values that correspond to each letter in the key
        keyInts = []
        for i in range(len(key)):
            if (97 <= ord(key[i]) <= 122):
                keyInts.append(ord(key[i]) - 97)
            elif (65 <= ord(key[i]) <= 90):
                keyInts.append(ord(key[i]) - 65)

        # encrypt mode
        if (mode == "-e"):
            encryptedMessage = ""
            # counter for key
            j = 0
            
            # encrypt the message
            for i in range(len(message)):
                # letter is lowercase
                if (97 <= ord(message[i]) <= 122):
                    encryptedMessage += chr((((ord(message[i]) - 97) + (keyInts[j % len(keyInts)])) % 26) + 97)
                    j = j + 1
                
                # letter is uppercase
                elif (65 <= ord(message[i]) <= 90):
                    encryptedMessage += chr((((ord(message[i]) - 65) + (keyInts[j % len(keyInts)])) % 26) + 65)
                    j = j + 1
                
                # not a letter
                else:
                    encryptedMessage += message[i]
                    
            print(encryptedMessage)
                    
        # decrypt mode
        elif (mode == "-d"):
            decryptedMessage = ""
            # counter for key
            j = 0
            
            # decrypt the message
            for i in range(len(message)):
                # letter is lowercase
                if (97 <= ord(message[i]) <= 122):
                    decryptedMessage += chr(((26 + (ord(message[i]) - 97) - (keyInts[j % len(keyInts)])) % 26) + 97)
                    j = j + 1
                    
                # letter is uppercase
                elif (65 <= ord(message[i]) <= 90):
                    decryptedMessage += chr(((26 + (ord(message[i]) - 65) - (keyInts[j % len(keyInts)])) % 26) + 65)
                    j = j + 1
                    
                # not a letter
                else:
                    decryptedMessage += message[i]
                    
            print(decryptedMessage)
            
except EOFError:
    pass