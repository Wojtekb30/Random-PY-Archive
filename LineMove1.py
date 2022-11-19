import os
clear = lambda: os.system('clear')
a = "■"
b = " "
c = " "
d = " "
e = " "
f = " "
g = 0
mi = 1 -2
win = " "
while 1==1:
    clear()
    print(a+b+c+d+e+f)
    print("■■■■■■")
    print(win)
    n = 0
    
    n = int(input("1 for left, 2 for right: "))
    if (n==2):
        g=g+1

    if (g==0):
        g = 1
        
    if (g==6):
        g = 5
        
        
    if (n==2 and g==1):
        a = " "
        b = "■"
        
    if (n==2 and g==2):
        b = " "
        c = "■"
        
    if (n==2 and g==3):
        c = " "
        d = "■"
        
    if (n==2 and g==4):
        d = " "
        e = "■"
        
    if (n==2 and g==5):
        e = " "
        f = "■"
        win = "You won!"
        






    if (n==1 and g==1):
        a = "■"
        b = " "
        
    if (n==1 and g==2):
        b = "■"
        c = " "
        
    if (n==1 and g==3):
        c = "■"
        d = " "
        
    if (n==1 and g==4):
        d = "■"
        e = " "
        
    if (n==1 and g==5):
        e = "■"
        f = " "
    if (n==1):
        g=g-1