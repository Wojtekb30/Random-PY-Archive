liczba = int(input("Liczba: "))
system = int(input("Podstawa systemu: "))
if system<=1:
    print("Błąd, za mały system")
    quit();
i = 0
wo = []
while liczba>0:
    wo.append(liczba%system)
    liczba = int(liczba/system)
    i=i+1
i=i-1
while i>=0:
    print(wo[i])
    i=i-1
