import pygame
import sys
pygame.init()
screen_game=pygame.display.set_mode((700,700))
screen_rect=screen_game.get_rect()#tworzymy prostokat ekranu
limegreen = (50, 205, 50)
black = (0, 0, 0)
chocolate = (210, 105, 30)
white = (255, 255, 255)
x=50#poczatkowe polozenie kubka
y=50#poczatkowe polozenie kubka
x_stolika=screen_rect.centerx - 110#minus polowa dlugosci stolika
y_stolika=screen_rect.bottom - 126#minus wysokosc stolika
stolik_image = pygame.image.load("stolik_220x126.png")
kawa_image = pygame.image.load("pani_fral_70x70.png")
zegar=pygame.time.Clock()#ustawiamy zegar

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    przycisk = pygame.key.get_pressed()#nacisniecie przycisku
    if przycisk[pygame.K_d] and x < screen_rect.width - 70:
        x=x+4
    if przycisk[pygame.K_a] and x > 0:
        x=x-4
    if przycisk[pygame.K_w] and y > 0:
        y=y-4
    if przycisk[pygame.K_s] and y < screen_rect.height - 70:
        y=y+4

    screen_game.fill(black)
    kawa = pygame.Rect(x,y,70,70)
    stolik = pygame.Rect(x_stolika,y_stolika,220,120)
    
    if kawa.colliderect(stolik):
        if przycisk[pygame.K_d]:
            x = 170
        if przycisk[pygame.K_a]:
            x = 460
        if przycisk[pygame.K_w]:
            pass
        if przycisk[pygame.K_s]:
            y = 504
            
    screen_game.blit(kawa_image, (x,y))
    screen_game.blit(stolik_image, (x_stolika,y_stolika))
    zegar.tick(60)#odswiezamy ekran po przesunieciu kubka
    pygame.display.update()
