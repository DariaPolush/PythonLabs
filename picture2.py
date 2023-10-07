import pygame
from pygame.draw import *

FPS = 30
pygame.init()
screen = pygame.display.set_mode((800, 350))

body_color = [(0, 153, 0), (255, 129, 1)]
eyes_color = [(182, 182, 182), (0, 171, 255)]
hair_color = [(252, 243, 4), (255, 0, 255)]

pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 500), width=0)

x = 0

for i in range(2):
    pygame.draw.circle(screen, body_color[i], (250+x, 350), 110, width=0)
    
    pygame.draw.polygon(screen, (255, 204, 204), [(130+x, 280), (145+x, 280), (90+x, 70), (75+x, 70)], width=0)
    pygame.draw.polygon(screen, (255, 204, 204), [(350+x, 280), (365+x, 280), (425+x, 70), (410+x, 70)], width=0)
    
    pygame.draw.circle(screen, (255, 204, 204), (83+x, 70), 25, width=0)
    pygame.draw.circle(screen, (255, 204, 204), (414+x, 70), 25, width=0)
    pygame.draw.circle(screen, (255, 255, 255), (83+x, 70), 25, width=1)
    pygame.draw.circle(screen, (255, 255, 255), (414+x, 70), 25, width=1)

    pygame.draw.polygon(screen, body_color[i], [(160+x, 300), (168+x, 277), (146+x, 263), (122+x, 277), (135+x, 305)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(160+x, 300), (168+x, 277), (146+x, 263), (122+x, 277), (135+x, 305)], width=1)
    pygame.draw.polygon(screen, body_color[i], [(343+x, 300), (328+x, 277), (350+x, 263), (375+x, 277), (363+x, 302)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(343+x, 300), (328+x, 277), (350+x, 263), (375+x, 277), (363+x, 302)], width=1)

    #лицо
    pygame.draw.circle(screen, (255, 204, 204), (250+x, 190), 95, width=0)
    pygame.draw.polygon(screen, (153, 76, 0), [(250+x, 225), (240+x, 210), (260+x, 210)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(250+x, 225), (240+x, 210), (260+x, 210)], width=1)
    pygame.draw.polygon(screen, (255, 0, 0), [(250+x, 260), (210+x, 235), (290+x, 235)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(250+x, 260), (210+x, 235), (290+x, 235)], width=1)

    #глаза
    pygame.draw.circle(screen, eyes_color[i], (220+x, 175), 20, width=0)
    pygame.draw.circle(screen, eyes_color[i], (280+x, 175), 20, width=0)
    pygame.draw.circle(screen, (0, 0, 0), (220+x, 175), 20, width=1)
    pygame.draw.circle(screen, (0, 0, 0), (280+x, 175), 20, width=1)
    pygame.draw.circle(screen, (0, 0, 0), (220+x, 177), 5, width=0)
    pygame.draw.circle(screen, (0, 0, 0), (280+x, 177), 5, width=0)

    #волосы
    pygame.draw.polygon(screen, hair_color[i], [(165+x, 146), (156+x, 103), (189+x, 120)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(165+x, 146), (156+x, 103), (189+x, 120)], width=1)
    pygame.draw.polygon(screen, hair_color[i], [(185+x, 122), (190+x, 80), (220+x, 101)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(185+x, 122), (190+x, 80), (220+x, 101)], width=1)
    pygame.draw.polygon(screen, hair_color[i], [(218+x, 101), (232+x, 68), (250+x, 96)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(218+x, 101), (232+x, 68), (250+x, 96)], width=1)
    pygame.draw.polygon(screen, hair_color[i], [(250+x, 95), (273+x, 67), (282+x, 100)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(250+x, 95), (273+x, 67), (282+x, 100)], width=1)
    pygame.draw.polygon(screen, hair_color[i], [(280+x, 100), (310+x, 77), (312+x, 118)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(280+x, 100), (310+x, 77), (312+x, 118)], width=1)
    pygame.draw.polygon(screen, hair_color[i], [(310+x, 117), (347+x, 103), (336+x, 150)], width=0)
    pygame.draw.polygon(screen, (0, 0, 0), [(310+x, 117), (347+x, 103), (336+x, 150)], width=1)

    x += 335






pygame.draw.rect(screen, (0, 255, 0), (0, 0, 800, 50), width=0)

pygame.font.SysFont('arial', 152)
f1 = pygame.font.Font(None, 60)
text1 = f1.render('PYTHON is REALLY AMAZING!', 1, (0, 0, 0))
screen.blit(text1, (100, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
