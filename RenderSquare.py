from random import randint
dzielnik=1
print("Turn small mode ON (for 720p and 540p screens)? 1 if yes")
pytanie = int(input("Odpalic tryb maly (dla ekranow 720p lub 540p)? 1 dla tak: "))
if pytanie==1:
    dzielnik = 2
x = int(1000/dzielnik)
print(" ")
print("Type distance between squares (at least 30 (or just number 50) recommended")
y = int(input("Odleglosc miedzy kwadratami (zalecana conajmniej niz 30, lub po prostu 50): "))
if y<1:
    print("Error! Blad. Odleglosc musi byc wieksza niz 1")
    exit()
y=y*-1
y=int(y/dzielnik)
r = 0
g = 0
b = 0
lx = 0
ly = 0
print(" ")
print("Type delay between frames, recommended at least 250")
print("Warning! Making this number low might cause epilepsy attack!")
print("Opoznienie miedzy klatkami (zalecane conajmniej 250) ")
print("Uwaga! Zbyt niska wartosc stanowi zagrozenie epileptyczne!: ")
opoznienie = int(input(""))

import pygame
pygame.init()
win = pygame.display.set_mode((int(1000/dzielnik), int(1000/dzielnik)))
pygame.display.set_caption("Squares")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(win, (r,g,b) , (lx, ly, x, x))
    x = x + y

    if lx+ly==0:
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)

    if x<0:
        lx = int(1000/dzielnik)
        ly = int(1000/dzielnik)
    if x<int(-1000/dzielnik) and lx ==int(1000/dzielnik) and ly == int(1000/dzielnik):
        x = int(1000/dzielnik)
        lx =0
        ly=0
    if event.type == pygame.KEYDOWN:
        exit()
    pygame.display.update()
    pygame.time.delay(opoznienie)
