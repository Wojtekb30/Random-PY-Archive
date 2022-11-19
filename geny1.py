print("Wpisuj tylko a lub A")
jedenf = str(input("Allel 1 matki: "))
dwaf = str(input("Allel 2 matki: "))
jedenm = str(input("Allel 1 ojca: "))
dwam = str(input("Allel 2 ojca: "))
wa = jedenf +jedenm
wb = jedenf+dwam
wc = dwaf +jedenm
wd = dwaf+dwam
if (wa== "aA"):
    wa = "Aa"
if (wb == "aA"):
    wb = "Aa"
if (wc == "aA"):
    wc = "Aa"
if (wd == "aA"):
    wd = "Aa"
print("ojciec->|  " + jedenm + "  |  "   + dwam + "  |")
print("matka v |     |     |")
print("--------|-----|-----|")
print("    " + jedenf + "   |  "+wa +" |  "+wb+" |") 
print("--------|-----|-----|")
print("    " + dwaf + "   |  "+wc+" |  "+wd+" |")
print("---------------------")
hetero = 0
homod = 0
homor = 0
if (wa == "Aa"):
    hetero = hetero + 25
if (wa == "AA"):
    homod = homod + 25
if (wa == "aa"):
    homor = homor + 25
if (wb == "Aa"):
    hetero = hetero + 25
if (wb == "AA"):
    homod = homod + 25
if (wb == "aa"):
    homor = homor + 25
if (wc == "Aa"):
    hetero = hetero + 25
if (wc == "AA"):
    homod = homod + 25
if (wc == "aa"):
    homor = homor + 25
if (wd == "Aa"):
    hetero = hetero + 25
if (wd == "AA"):
    homod = homod + 25
if (wd == "aa"):
    homor = homor + 25
print("Genotyp:")
print(str(hetero) + "% heterozygoty")
print(str(homod) + "% homozygoty dominujace")
print(str(homor) + "% homozygoty recesywne")
print(" ")
print("Fenotyp:")
print(str(hetero+homod) + "% cecha dominujaca")
print(str(homor) + "% cecha recesywna")
print(" ")
n = str(input("nacisnij ENTER by zakonczyc"))
