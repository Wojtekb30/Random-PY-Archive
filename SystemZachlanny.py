kasa = float(input("Wpisz sume pieniedzy w PLN (mozesz po . wpisac grosze, np. 12.34): "))
kasa = kasa*100

ps = 0
ds = 0
sto = 0
pz = 0
dz = 0
ten = 0
five = 0
two = 0
one = 0
pigr = 0
dwdzgr = 0
tengroszy = 0
pgroszy = 0
dwagr = 0
jedengrosz = 0

if kasa<1:
    print("Za mala lub bledna kwota")
    quit()

while kasa >=1:
    if kasa>=50000:
        kasa=kasa-50000
        ps = ps+1
    elif kasa>=20000:
        kasa=kasa-20000
        ds = ds+1
    elif kasa>=10000:
        kasa=kasa-10000
        sto = sto+1
    elif kasa>=5000:
        kasa=kasa-5000
        pz = pz+1
    elif kasa>=2000:
        kasa=kasa-2000
        dz=dz+1
    elif kasa>=1000:
        kasa=kasa-1000
        ten = ten+1
    elif kasa>=500:
        kasa=kasa-500
        five=five+1
    elif kasa>=200:
        kasa=kasa-200
        two = two + 1
    elif kasa>=100:
        kasa=kasa-100
        one = one+1
        
    elif kasa>=50:
        kasa=kasa-50
        pigr = pigr+1
    elif kasa>=20:
        kasa=kasa-20
        dwdzgr = dwdzgr+1
    elif kasa>=10:
        kasa=kasa-10
        tengroszy = tengroszy+1
    elif kasa>=5:
        kasa=kasa-5
        pgroszy = pgroszy+1
    elif kasa>=2:
        kasa=kasa-2
        dwagr = dwagr+1
    else:
        kasa=kasa-1
        jedengrosz = jedengrosz + 1
        
print("Wydano:")

if ps>0:
    print(str(ps)+" banknot(ow) 500 PLN")
if ds>0:
    print(str(ds)+" banknot(ow) 200 PLN")
if sto>0:
    print(str(sto)+" banknot(ow) 100 PLN")
if pz>0:
    print(str(pz)+" banknot(ow) 50 PLN")
if dz>0:
    print(str(dz)+" banknot(ow) 20 PLN")
if ten>0:
    print(str(ten)+" banknot(ow) 10 PLN")
if five>0:
    print(str(five)+" monet(e) 5 PLN")
if two>0:
    print(str(two)+" monet(e) 2 PLN")
if one>0:
    print(str(one)+" monet(e) 1 PLN")

if pigr>0:
    print(str(pigr)+" monet(e) 50 groszy")
if dwdzgr>0:
    print(str(dwdzgr)+" monet(e) 20 groszy")
if tengroszy>0:
    print(str(tengroszy)+" monet(e) 10 groszy")
if pgroszy>0:
    print(str(pgroszy)+" monet(e) 5 groszy")
if dwagr>0:
    print(str(dwagr)+" monet(e) 2 grosze")
if jedengrosz>0:
    print(str(jedengrosz)+" monet(e) 1 grosz")

