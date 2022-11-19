while (1==1):
    ja = int(input("Wpisz swoj wiek:"))
    ktos = int(input("Wpisz wiek kogos z rodziny:"))
    if (ja > ktos):
        wynik = int(ja/ktos)
        print("Wiek tej osoby miesci sie w twoim " + str(wynik) +" razy.")
        print(" ")
    else:
        wynik = int(ktos/ja)
        print("Twoj wiek miesci sie w wieku tej osoby " + str(wynik) +" razy.")
        print(" ")
