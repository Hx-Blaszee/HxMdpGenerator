from os import name, system
from colorama import Fore, init
from requests import get
from threading import Thread
from random import randint
import random

if name == 'nt':
    system("title Hx Generator")


print(Fore.RED + """
     ██░ ██ ▒██   ██▒     ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
    ▓██░ ██▒▒▒ █ █ ▒░    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒██▀▀██░░░  █   ░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ░▓█ ░██  ░ █ █ ▒    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ░▓█▒░██▓▒██▒ ▒██▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ▒ ░░▒░▒▒▒ ░ ░▓ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ▒ ░▒░ ░░░   ░▒ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
    ░  ░░ ░ ░    ░     ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░  ░  ░ ░    ░           ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                                                  """)
print(Fore.GREEN + """
                                    Discord : discord.gg/23Eu9UPRXJ\n\n\n""")




chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$%^&;:!ù^$*/+-*(`)"

while 1:
    password_len = int(input("De quelle longueur souhaitez-vous que votre mot de passe soit : "))
    password_count = int(input("Combien de mots de passe souhaitez-vous : "))
    for x in range(0,password_count):
        password  = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Votre mot de passe est : ", password)