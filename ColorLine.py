from random import randint
x=1000
y=1000
r=255
g=255
b=255
import pygame
pygame.init()
win = pygame.display.set_mode((int(1000), int(1000)))
pygame.display.set_caption("Color render")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x==1000 and y==1000:
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)
        
    if(y>0 and x!=0):
        y=y-1
    if(y==0 and x>0):
        x=x-1
        
    if (x==0 and y<1000):
        y=y+1
        pygame.draw.line(win, (r,g,b) , (500, 500), (0, 0))
    while y==1000 and x<1000:
        x=x+1
        pygame.draw.line(win, (r,g,b) , (500, 500), (x, y))

        pygame.display.update()

    pygame.draw.line(win, (r,g,b) , (500, 500), (x, y))

    pygame.display.update()

