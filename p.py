# sssss

import os
import time
import sys
import socket
import requests
from colorama import Fore

def __target__():
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(Fore.BLUE + "Hello , This Is My Bot For All Requests ;))")
    time.sleep(1)
    target = input(Fore.BLUE + "\n[" + Fore.BLUE + "!" + Fore.BLUE + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "Pleass Enter Domain" + Fore.RED + " ==> ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "[-] ~ Error : Your Domain Is None ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    if not "https://" in target or not "http://" in target:
        target = "http://" + target
    r1 = requests.get(target)
    if r1.status_code == 200:
        print(Fore.GREEN + "[+] ~ Your Domain Is Found ;)")
    if r1.status_code != 200:
        try:
            time.sleep(0.4)
            print(Fore.RED + "[-] ~ Error : Your Domain Is Not Found ;(")
            sys.exit()
        except:
            sys.exit()
    # _______________________________________________________________________
    # Target Is Word Press Or Not Word Press And Ip Target
    #r2 = requests.get(target+"/wp-content/plugins/")
    #s1 = socket.gethostbyname(target)
    #if r2.status_code == 200:
    #    print(Fore.RED + "\n\nWordPress And Ip _______________________________")
    #    print(Fore.GREEN + "        Your Target Is Word Press" + Fore.GREEN + "\n        Your Ip Target Is  :  " + Fore.RED + str(s1))
    #else:
    #    print(Fore.RED + "\n\nNot WordPress And Ip _______________________________")
    #    print(Fore.GREEN + "        Your Target Is Not Word Press" + Fore.GREEN + "\n        Your Ip Target Is  :  " + Fore.RED + str(s1))
    # ___________________________________________________________________________
    # whatweb
    r3 = requests.get("https://api.hackertarget.com/whatweb/?q=" + target).text
    print(Fore.RED + "\n\nWhatweb _______________________________")
    print("\n\n" + Fore.GREEN + str(r3))
    # ________________________________________________________________________
    # whois
    r4 = requests.get("https://api.hackertarget.com/whois/?q=" + target).text
    print(Fore.RED + "\n\nWhois _______________________________")
    print("\n\n" + Fore.GREEN + str(r4))
    # _______________________________________________________________________
    # nmap
    r5 = requests.get("https://api.hackertarget.com/nmap/?q=" + target).text
    print(Fore.RED + "\n\nNmap _______________________________")
    print("\n\n" + Fore.GREEN + str(r5))
    # __________________________________________________________________________
    # dirb
    my_list = ["admin","Admin","ADMIN","admin/login","Admin/Login","ADMIN/LOGIN","admin1","Admin1","ADMIN1","panel/admin","Panel/Admin","PANEL/ADMIN","login/admin","Login/Admin","LOGIN/ADMIN","admins","Admins","ADMINS"]
    print(Fore.RED + "\n\nDirb _______________________________")
    print("\n\n")
    for i in my_list:
        r6 = target + "/" + i
        r7 = requests.get(r6)
        if r7.status_code == 200:
            print(Fore.GREEN + "[+] ~ " + Fore.FREEN + str(r6))
        if r7.status_code != 200:
            print(Fore.RED + "[-] ~ " + Fore.RED + str(r6))
__target__()
