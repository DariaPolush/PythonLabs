import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 700))

WHITE = (255, 255, 255)
BLUE = (65, 105, 225)

screen.fill(BLUE)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
x = 10
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = 10
                for i in range(700):
                    circle(screen, WHITE, event.pos, x, 5)
                    circle(screen, BLUE, event.pos, x-1, 5)
                    pygame.display.update()
                    x += 1
            

pygame.quit()
