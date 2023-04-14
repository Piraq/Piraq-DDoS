from pystyle import *
import os
import subprocess
import requests
from colorama import *
from tqdm import tqdm
import time

chromdriver = ("chromedriver.exe")
API = ("python API.py")

with open("./recources/proxy.txt", "r") as fichier:
    proxy = fichier.read()

with open("./src/host.txt", "r") as fichier:
    host = fichier.read()

with open("./src/port.txt", "r") as fichier:
    port = fichier.read()

with open("./src/method.txt", "r") as fichier:
    method = fichier.read()

intro = """
 _______ _________ _______  _______  _______ 
(  ____ )\__   __/(  ____ )(  ___  )(  ___  )
| (    )|   ) (   | (    )|| (   ) || (   ) |
| (____)|   | |   | (____)|| (___) || |   | |
|  _____)   | |   |     __)|  ___  || |   | |
| (         | |   | (\ (   | (   ) || | /\| |
| )      ___) (___| ) \ \__| )   ( || (_\ \ |
|/       \_______/|/   \__/|/     \|(____\/_)
                 Press enter                     
"""
Anime.Fade(Center.Center(intro), Colors.cyan_to_blue, Colorate.Vertical, interval=0.035, enter=True)

os.system("title Piraq DDoS Panel")

import time

for i in tqdm(range(100), desc="Loading Proxy"): 
    time.sleep(0.1) 

os.system(chromdriver)

print (f"""

Proxy Loaded : 

""")   

time.sleep(1.5)

print (f"""{proxy}""")

time.sleep(2)

os.system('cls' if os.name=='nt' else 'clear')

print (f"""
                                    _______ _________ _______  _______  _______ 
                                   (  ____ )\__   __/(  ____ )(  ___  )(  ___  )
                                   | (    )|   ) (   | (    )|| (   ) || (   ) |
                                   | (____)|   | |   | (____)|| (___) || |   | |
                                   |  _____)   | |   |     __)|  ___  || |   | |
                                   | (         | |   | (\ (   | (   ) || | /\| |
                                   | )      ___) (___| ) \ \__| )   ( || (_\ \ |
                                   |/       \_______/|/   \__/|/     \|(____\/_)
                                                     DDOS PANEL
                                    host : {host}  port : {port} method : {method}   
                                                                                                                                              """)
input("                                            Press enter to start attack")            

import time

message = "Starting Attack"
for i in range(3):
    print(message + "." * i, end="\r")
    time.sleep(1)

os.system(API)
os.system('cls' if os.name=='nt' else 'clear')

print (f"""
                                    _______ _________ _______  _______  _______ 
                                   (  ____ )\__   __/(  ____ )(  ___  )(  ___  )
                                   | (    )|   ) (   | (    )|| (   ) || (   ) |
                                   | (____)|   | |   | (____)|| (___) || |   | |
                                   |  _____)   | |   |     __)|  ___  || |   | |
                                   | (         | |   | (\ (   | (   ) || | /\| |
                                   | )      ___) (___| ) \ \__| )   ( || (_\ \ |
                                   |/       \_______/|/   \__/|/     \|(____\/_)
                                                     DDOS PANEL
                                                                                                                                                                                                                                                         
                              Attacking {host} on the port {port} with the method {method}                                                                                                                                    
                                                                                                                                              """)
input("                                            Press enter to stop attack")

print("The attack stop")

print("The cmd gonna be close in 3 seconds")

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

os.system('taskkill /f /im cmd.exe')

