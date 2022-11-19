a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
tura = 1
gra = "TXT"
symbol = "X"
ruchy = 10
while 1==1:



    if (a=="X" and b == "X" and c=="X") or (d=="X" and e == "X" and f=="X") or (g=="X" and h == "X" and i=="X") or (a=="X" and d == "X" and g=="X") or (b=="X" and e == "X" and h=="X") or (c=="X" and f == "X" and i=="X") or (g=="X" and e == "X" and c=="X") or (a=="X" and e == "X" and i=="X"):
        print(" ")
        print(" 1 | 2| 3")
        print("A "+a+"| "+b+"| "+c)
        print("---|--|---")
        print("B "+d+"| "+e+"| "+f)
        print("---|--|---")
        print("C "+g+"| "+h+"| "+i)
        print("   |  |")
        print(" ")

        print("X won!")
        break
    if (a=="O" and b == "O" and c=="O") or (d=="O" and e == "O" and f=="O") or (g=="O" and h == "O" and i=="O") or (a=="O" and d == "O" and g=="O") or (b=="O" and e == "O" and h=="O") or (c=="O" and f == "O" and i=="O") or (g=="O" and e == "O" and c=="O") or (a=="O" and e == "O" and i=="O"):

        print(" ")
        print(" 1 | 2| 3")
        print("A "+a+"| "+b+"| "+c)
        print("---|--|---")
        print("B "+d+"| "+e+"| "+f)
        print("---|--|---")
        print("C "+g+"| "+h+"| "+i)
        print("   |  |")
        print(" ")


        print("O won!")
        break

    ruchy=ruchy-1
    if ruchy==0:


        print(" ")
        print(" 1 | 2| 3")
        print("A "+a+"| "+b+"| "+c)
        print("---|--|---")
        print("B "+d+"| "+e+"| "+f)
        print("---|--|---")
        print("C "+g+"| "+h+"| "+i)
        print("   |  |")
        print(" ")
        print("Tie!")
        break






    
    print(" ")
    print(" 1 | 2| 3")
    print("A "+a+"| "+b+"| "+c)
    print("---|--|---")
    print("B "+d+"| "+e+"| "+f)
    print("---|--|---")
    print("C "+g+"| "+h+"| "+i)
    print("   |  |")
    if tura == 1:
        gra=str(input("X: "))
        tura = tura*-1
        symbol = "X"
    else:
        gra=str(input("O: "))
        tura = tura*-1
        symbol = "O"
        
    if (gra == 'A1' or gra == '1A' or gra == '1a' or gra == 'a1') and a!="X" and a!="O":
        a = symbol
    elif (gra == 'A2' or gra == '2A' or gra == '2a' or gra == 'a2') and b!="X" and b!="O":
        b = symbol
    elif (gra == 'A3' or gra == '3A' or gra == '3a' or gra == 'a3') and c!="X" and c!="O":
        c = symbol
    elif (gra == 'B1' or gra == '1B' or gra == '1b' or gra == 'b1') and d!="X" and d!="O":
        d = symbol
    elif (gra == 'B2' or gra == '2B' or gra == '2b' or gra == 'b2') and e!="X" and e!="O":
        e = symbol
    elif (gra == 'B3' or gra == '3B' or gra == '3b' or gra == 'b3') and f!="X" and f!="O":
        f = symbol
    elif (gra == 'C1' or gra == '1C' or gra == '1c' or gra == 'c1') and g!="X" and g!="O":
        g = symbol
    elif (gra == 'C2' or gra == '2C' or gra == '2c' or gra == 'c2') and h!="X" and h!="O":
        h = symbol
    elif (gra == 'C3' or gra == '3C' or gra == '3c' or gra == 'c3') and i!="X" and i!="O":
        i = symbol
    else:
        print("Wrong space ID or space occupied. Try again")
        tura = tura*-1
        ruchy=ruchy+1




print(" ")
koniec = input("Press any button to end")
