import random
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

print("Type the highest number to ever appear in calculations:")
zakres = int(input ("Wpisz najwyzsza liczbe, jaka pojawi sie w obliczeniach: "))
while (1==1):
    print(Style.RESET_ALL)
    ziarno = random.randint(0,4)
    jeden = random.randint(0,zakres)
    dwa = random.randint(0,zakres)
    first = str(jeden)
    second = str(dwa)
    if (ziarno==0 or ziarno==1):
            dzialanie = "+"
            wynik = jeden + dwa
            print(first + "+" + second + "=")
    if(ziarno==2 or ziarno == 3):
           dzialanie = "-"
           wynik = jeden - dwa
           print(first + "-" + second + "=")
    if(ziarno==4):
             dzialanie = "*"
             wynik = jeden * dwa
             print(first + "*" + second + "=")

    odp = int(input ("Wpisz wynik | Type answer here: "))
    if(wynik == odp):
        print(Fore.GREEN + "Prawidlowa odpowiedz")
        print("Answer correct")
    else:
        print(Fore.RED + "Nieprawidlowa odpowiedz. Prawidlowa odpowiedz to:")
        print("Answer incorrect. Correct answer is:")
        print(wynik)