import pygame
from pygame.draw import *

FPS = 30
pygame.init()
screen = pygame.display.set_mode((500, 350))
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 500, 350), width=0)


#тело+руки
pygame.draw.circle(screen, (255, 129, 1), (250, 350), 110, width=0)

pygame.draw.polygon(screen, (255, 204, 204), [(130, 280), (145, 280), (90, 70), (75, 70)], width=0)
pygame.draw.polygon(screen, (255, 204, 204), [(350, 280), (365, 280), (425, 70), (410, 70)], width=0)
pygame.draw.circle(screen, (255, 204, 204), (83, 70), 25, width=0)
pygame.draw.circle(screen, (255, 204, 204), (414, 70), 25, width=0)
pygame.draw.circle(screen, (255, 255, 255), (83, 70), 25, width=1)
pygame.draw.circle(screen, (255, 255, 255), (414, 70), 25, width=1)

pygame.draw.polygon(screen, (255, 129, 1), [(160, 300), (168, 277), (146, 263), (122, 277), (135, 305)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(160, 300), (168, 277), (146, 263), (122, 277), (135, 305)], width=1)
pygame.draw.polygon(screen, (255, 129, 1), [(343, 300), (328, 277), (350, 263), (375, 277), (363, 302)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(343, 300), (328, 277), (350, 263), (375, 277), (363, 302)], width=1)

#лицо
pygame.draw.circle(screen, (255, 204, 204), (250, 190), 95, width=0)
pygame.draw.polygon(screen, (153, 76, 0), [(250, 225), (240, 210), (260, 210)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(250, 225), (240, 210), (260, 210)], width=1)
pygame.draw.polygon(screen, (255, 0, 0), [(250, 260), (210, 235), (290, 235)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(250, 260), (210, 235), (290, 235)], width=1)

#глаза
pygame.draw.circle(screen, (0, 171, 255), (220, 175), 20, width=0)
pygame.draw.circle(screen, (0, 171, 255), (280, 175), 20, width=0)
pygame.draw.circle(screen, (0, 0, 0), (220, 175), 20, width=1)
pygame.draw.circle(screen, (0, 0, 0), (280, 175), 20, width=1)
pygame.draw.circle(screen, (0, 0, 0), (220, 177), 5, width=0)
pygame.draw.circle(screen, (0, 0, 0), (280, 177), 5, width=0)

#волосы
pygame.draw.polygon(screen, (255, 0, 255), [(165, 146), (156, 103), (189, 120)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(165, 146), (156, 103), (189, 120)], width=1)
pygame.draw.polygon(screen, (255, 0, 255), [(185, 122), (190, 80), (220, 101)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(185, 122), (190, 80), (220, 101)], width=1)
pygame.draw.polygon(screen, (255, 0, 255), [(218, 101), (232, 68), (250, 96)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(218, 101), (232, 68), (250, 96)], width=1)
pygame.draw.polygon(screen, (255, 0, 255), [(250, 95), (273, 67), (282, 100)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(250, 95), (273, 67), (282, 100)], width=1)
pygame.draw.polygon(screen, (255, 0, 255), [(280, 100), (310, 77), (312, 118)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(280, 100), (310, 77), (312, 118)], width=1)
pygame.draw.polygon(screen, (255, 0, 255), [(310, 117), (347, 103), (336, 150)], width=0)
pygame.draw.polygon(screen, (0, 0, 0), [(310, 117), (347, 103), (336, 150)], width=1)



pygame.draw.rect(screen, (0, 255, 0), (0, 0, 500, 50), width=0)
 
pygame.font.SysFont('arial', 165)
f1 = pygame.font.Font(None, 60)
text1 = f1.render('PYTHON is AMAZING', 1, (0, 0, 0))
screen.blit(text1, (30, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
