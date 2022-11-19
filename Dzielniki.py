print("Znajdz dzielniki")
n = int(input("Wpisz liczbe: "))
k=n
while k>=1:
    if n%k==0:
        print(k)
    k=k-1
