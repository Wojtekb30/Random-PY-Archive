print("Wpisz cene towaru. Nie kupujemy drozszych niz 100")
cena = int(input ("Wpisz cene: "))
if (cena>100):
    print("towar za drogi. Nie kupujemy")
else:
    print("cena ok. Kupuj.")