import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.BLUE + 'niebieski tekst')
print(Fore.RED + 'czerwony tekst')
print(Fore.GREEN + 'zielony tekst')

print(Style.RESET_ALL)
print('normal')
while 1==1:
    a = input ("Wpisz tekst: ")
    print(a)
    if(a=="Easter egg"):
        print(":-)")
    if(a=="koniec"):
        break
    if(a=="powitanie"):
        print("Program powitalny")
        login = input ("Podaj swoje imie: ")
        print("-------------------------")
        print(" ")
        print(Fore.WHITE + Back.CYAN + "Uzytkownik " + login + " zostal programista!")
        print(Style.RESET_ALL)
        print("-------------------------")