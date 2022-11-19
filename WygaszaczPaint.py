from random import randint
rozmiara=1920
rozmiarb=1080
akt = 0
opoznienie = 0
ra = 50
rb= 100
radio = 50
lol = 0
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
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("ScreenSaver")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
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

    if event.type == pygame.KEYDOWN:
        exit()
    pygame.display.update()
    lol = lol+1
    if lol == 5000:
        r = randint(1, 255)
        g =randint(1, 255)
        b =randint(1, 255)
        lol = 0

