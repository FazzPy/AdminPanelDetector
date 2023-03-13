from colorama import Fore
import colorama
import sys
import requests

colorama.init()


print(Fore.BLUE+"""

  ___ _________  ________ _   _  ______  ___   _   _  _____ _     
 / _ \|  _  \  \/  |_   _| \ | | | ___ \/ _ \ | \ | ||  ___| |    
/ /_\ \ | | | .  . | | | |  \| | | |_/ / /_\ \|  \| || |__ | |    
|  _  | | | | |\/| | | | | . ` | |  __/|  _  || . ` ||  __|| |    
| | | | |/ /| |  | |_| |_| |\  | | |   | | | || |\  || |___| |____
\_| |_/___/ \_|  |_/\___/\_| \_/ \_|   \_| |_/\_| \_/\____/\_____/
                                                                  
                                                                  

ADMIN PANEL FINDER TOOL BY FAZZ | VERSION 0.1

""")

print("Example Url : https://www.fazztech.net/, https://fazztech.net/")

www = input("Target Url : ")

r = requests.get(www)

if r.status_code == 200 or r.status_code == "200":
    print(f"Try Connection : {www}, {r.status_code}, Connection succesfuly! ")
else:
    print(f"Try Connection : {www}, {r.status_code}, Connection failed! ")
    sys.exit()

URLS = []

with open("admin-wl.txt","r",encoding="utf-8") as file:
    dork = file.readlines()

    new_lines = []
    for line in dork:
        line = line.strip()
        if line.startswith(".") or line.startswith("/"):
            line = line[1:]
        new_lines.append(line)

    for i in new_lines:
        i = i.strip()
        target = www+i
        URLS.append(target)


    for i in URLS:

        v = f"{i}" 

        r = requests.get(v)

        print("\n")

        if r.status_code == 200 or r.status_code == "200":
            print(Fore.GREEN+v, f" Connection Succesfuly! This is admin panel!")
            with open("output.txt", "a", encoding="utf-8") as file:
                file.write(f"""   
{v}       
                """)
        else:
            print(Fore.RED+v, f" No Connection.")