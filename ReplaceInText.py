text = str(input("Type text: "))
zast = str(input("What to replace in it (single symbol)?: "))
fragment = str(input("With what?: "))

dlugosc = len(text)
dlugosc = dlugosc *-1
wynik = ""
while dlugosc<0:
    if text[dlugosc].upper()==zast[0].upper():
        wynik = wynik + fragment
    else:
        wynik = wynik + text[dlugosc]
    dlugosc = dlugosc +1
 #   print("")
print(wynik)
print("")
