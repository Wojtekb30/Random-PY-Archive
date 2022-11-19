from random import randint
print("Spacja zmieni kolor, C zeruje ekran")
rozmiara = int(input("Podaj szerokosc ekranu (najlepiej 1920): "))
rozmiarb = int(input("Podaj wysokosc ekranu (najlepiej 1015): "))
akt = int(input("Wpisz 1 by wlaczyc czyszczenie ekranu: "))
opoznienie = int(input("Opoznienie w milisekundach (0 dla brak): "))
ra = int(input("Wpisz minimalna wartosc dla losowania (zalecane 1): "))
rb= int(input("Wpisz maksymalna wartosc dla losowania (zalecane 3): "))
radio = int(input("Wpisz srednice kuli (zalecane 5): "))
if ra < 0 or rb < 0 or radio < 0:
    print("Blad. Losowania i srednica ma byc wieksza niz 0")
    exit()
if ra == 0 or rb == 0 or radio == 0:
    print("Blad. Losowania i srednica ma byc wieksza niz 0")
    exit()
if ra > rb:
    print("Blad. LosowanieMin musi byc mniejsze niz LosowanieMax")
    exit()
x = 10
y = 10
r = 255
g = 255
b = 255
mx = 1
my = 1
if rozmiara<10 or rozmiarb<10 or rozmiara<radio or rozmiarb<radio:
    print("Blad. Podaj inne dane")
    exit()
import pygame
pygame.init()
win = pygame.display.set_mode((rozmiara, rozmiarb))
pygame.display.set_caption("Bounce")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(win, (r, g, b), (x, y), radio)
    x = x+mx
    y = y+my

    if x<0:
        mx = randint(ra, rb)
    
    if x>rozmiara:
        mx = randint(ra, rb)
        mx = mx*-1

    if y<0:
        my = randint(ra, rb)

    if y>rozmiarb:
        my = randint(ra, rb)
        my = my*-1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c] :
        win.fill((0, 0, 0))
    if keys[pygame.K_SPACE] :
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
    pygame.display.update()
    pygame.time.delay(opoznienie)
    if akt == 1:
        win.fill((0, 0, 0))
