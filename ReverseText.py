while 1==1:
    text = str(input("Type text to write backwards: "))
    dlugosc = len(text)
    dlugosc = dlugosc - 1
    wynik = ""
    while dlugosc>=0:
        wynik = wynik + text[dlugosc]
        dlugosc = dlugosc -1
 #   print("")
    print(wynik)
    print("")
