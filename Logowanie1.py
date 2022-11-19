import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

while(1==1):
    print(Style.RESET_ALL)
    print("Zaloguj sie:")
    print("(Aby anulowac, wpisz end jako login lub haslo)")
    a = input ("Wpisz login: ")
    b = input ("Wpisz haslo: ")

    if(a == "end" or b == "end"):
        break
    else:
        if(a == "Woj"):
            if( b == "password"):
                print(Fore.GREEN + 'Witaj Woj!')
                break
            else:
                print(Fore.RED + 'Nieprawidlowe haslo')
        else:
            print(Fore.RED + 'Brak loginu w bazie danych')