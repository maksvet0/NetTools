#Version 0.0.2 build 23.03.08\2:39(Ekaterenburg)
from colorama import *
import requests
def iposint(ip):
    data = requests.get(f'http://ip-api.com/json/{ip}').json()
    if data["status"] != "fail":
          print("Country : " + data["country"])
    else:
         print(Fore.RED + f"Error:" + data["massage"])
def main():
        init()
        while True:
            userinput = input(Fore.CYAN + Back.BLACK + "Please input command\n=NetTools=>>")
            if userinput == "q":
                break
            elif userinput == "help":
                print(Fore.WHITE + Back.YELLOW + "iposint - Allows you to get some data from an IP address")
            elif userinput == "iposint":
                 targetip = input(Fore.GREEN + "Please input target ip\n=NetTools\\IPOSINT=>>")
                 iposint(targetip)
            else:
                print(Back.BLACK)
                print(Fore.RED + f"Error:'{userinput}' is not command or value!")
                print(Back.YELLOW + Fore.WHITE + "Note: Use the 'help' command to display a list of all program functions")
                print(Back.BLACK)

if __name__ == "__main__":
    main()
