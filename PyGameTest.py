import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 540))
pygame.display.set_caption("Pierwsza gra")
x = 0
y = 40
szerokosc = 20
wysokosc = 20
krok = 20
run = True
while run:
    # opóźnienie w grze
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń 
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_LEFT]:
        x -= krok
    if keys[pygame.K_RIGHT]:
        x += krok
    if keys[pygame.K_UP]:
        y -= krok
    if keys[pygame.K_DOWN] :
        y += krok
    # "czyszczenie" ekranu
    win.fill((0, 0, 0))
    # rysowanie prostokąta
    aa = random.randint(0,255)
    ab = random.randint(0,255)
    ac = random.randint(1,255)
    pygame.draw.rect(win, (aa, ab, ac), (x, y, szerokosc, wysokosc))
    # odświeżenie ekranu 
    pygame.display.update()
