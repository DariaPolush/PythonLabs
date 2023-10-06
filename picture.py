import pygame
from pygame.draw import *

FPS = 30
pygame.init()


#фон
screen = pygame.display.set_mode((550, 750))
pygame.draw.rect(screen, (0, 255, 255), (0, 0, 550, 350), 0)
pygame.draw.rect(screen, (128, 255, 0), (0, 350, 550, 400), 0)

#солнце
pygame.draw.circle(screen, (247, 255, 62), (540, 70), 100, width=0)

#ствол
pygame.draw.rect(screen, (215, 215, 215), (95, 350, 30, 170), 0)

#крона
pygame.draw.ellipse(screen, (39, 168, 25), (40, 320, 140, 120), 0)
pygame.draw.ellipse(screen, (39, 168, 25), (-10, 245, 240, 130), 0)
pygame.draw.ellipse(screen, (39, 168, 25), (45, 170, 130, 150), 0)

#плоды
pygame.draw.circle(screen, (255, 195, 142), (125, 210), 18, width=0)
pygame.draw.circle(screen, (255, 195, 142), (205, 320), 18, width=0)
pygame.draw.circle(screen, (255, 195, 142), (30, 310), 18, width=0)
pygame.draw.circle(screen, (255, 195, 142), (140, 420), 18, width=0)

#хвост
pygame.draw.ellipse(screen, (255, 210, 229), (255, 480, 50, 30), 0)
pygame.draw.ellipse(screen, (255, 204, 229), (240, 492, 50, 20), 0)
pygame.draw.ellipse(screen, (255, 204, 250), (220, 505, 80, 30), 0)
pygame.draw.ellipse(screen, (255, 153, 204), (245, 505, 40, 20), 0)
pygame.draw.ellipse(screen, (153, 153, 255), (240, 545, 50, 30), 0)
pygame.draw.ellipse(screen, (255, 153, 204), (230, 520, 50, 20), 0)
pygame.draw.ellipse(screen, (115, 115, 255), (195, 565, 60, 25), 0)
pygame.draw.ellipse(screen, (115, 115, 255), (230, 580, 80, 25), 0)
pygame.draw.ellipse(screen, (255, 153, 255), (215, 525, 25, 10), 0)
pygame.draw.ellipse(screen, (153, 51, 255), (190, 580, 55, 20), 0)
pygame.draw.ellipse(screen, (53, 51, 255), (200, 575, 70, 16), 0)
pygame.draw.ellipse(screen, (53, 51, 255), (190, 605, 70, 16), 0)
pygame.draw.ellipse(screen, (100, 101, 255), (205, 615, 65, 20), 0)
pygame.draw.ellipse(screen, (255, 153, 255), (223, 533, 48, 18), 0)
pygame.draw.ellipse(screen, (204, 153, 255), (200, 533, 49, 25), 0)
pygame.draw.ellipse(screen, (178, 102, 255), (218, 548, 50, 30), 0)
pygame.draw.ellipse(screen, (153, 153, 255), (195, 550, 50, 20), 0)
pygame.draw.ellipse(screen, (153, 153, 255), (245, 565, 50, 20), 0)
pygame.draw.ellipse(screen, (129, 129, 255), (230, 570, 42, 19), 0)
pygame.draw.ellipse(screen, (102, 102, 255), (207, 587, 45, 25), 0)
pygame.draw.ellipse(screen, (153, 51, 255), (240, 600, 55, 20), 0)
pygame.draw.ellipse(screen, (153, 151, 255), (250, 615, 65, 14), 0)
pygame.draw.ellipse(screen, (153, 51, 255), (213, 608, 50, 22), 0)
pygame.draw.ellipse(screen, (53, 51, 255), (240, 625, 70, 16), 0)

#тело+шея
pygame.draw.ellipse(screen, (255, 255, 255), (260, 480, 230, 100), 0)
pygame.draw.rect(screen, (255, 255, 255), (410, 410, 60, 100), 0)

#ноги
pygame.draw.rect(screen, (255, 255, 255), (450, 530, 15, 100), 0)
pygame.draw.rect(screen, (255, 255, 255), (335, 530, 15, 100), 0)
pygame.draw.rect(screen, (255, 255, 255), (295, 550, 20, 100), 0)
pygame.draw.rect(screen, (255, 255, 255), (405, 550, 20, 100), 0)

#голова
pygame.draw.ellipse(screen, (255, 255, 255), (400, 380, 90, 60), 0)
pygame.draw.ellipse(screen, (255, 255, 255), (415, 400, 105, 35), 0)
pygame.draw.circle(screen, (255, 118, 255), (460, 403), 9, width=0)
pygame.draw.circle(screen, (0, 0, 0), (465, 404), 3, width=0)
pygame.draw.polygon(screen, (255, 210, 229), [(460, 386), (440, 384), (457, 325)], width=0)

#грива
pygame.draw.ellipse(screen, (255, 210, 229), (410, 375, 40, 20), 0)
pygame.draw.ellipse(screen, (255, 204, 153), (400, 400, 43, 22), 0)
pygame.draw.ellipse(screen, (255, 210, 229), (390, 388, 45, 18), 0)
pygame.draw.ellipse(screen, (204, 255, 229), (405, 455, 40, 20), 0)
pygame.draw.ellipse(screen, (255, 204, 153), (375, 400, 48, 28), 0)
pygame.draw.ellipse(screen, (229, 255, 204), (385, 435, 50, 30), 0)
pygame.draw.ellipse(screen, (255, 255, 153), (400, 420, 40, 25), 0)
pygame.draw.ellipse(screen, (153, 255, 204), (390, 470, 43, 27), 0)
pygame.draw.ellipse(screen, (255, 255, 204), (363, 418, 48, 26), 0)
pygame.draw.ellipse(screen, (204, 255, 153), (355, 435, 55, 27), 0)
pygame.draw.ellipse(screen, (204, 255, 229), (370, 457, 50, 20), 0)
pygame.draw.ellipse(screen, (153, 255, 204), (345, 455, 40, 23), 0)
pygame.draw.ellipse(screen, (153, 255, 255), (368, 470, 36, 19), 0)
pygame.draw.ellipse(screen, (153, 255, 255), (350, 475, 45, 23), 0)
pygame.draw.ellipse(screen, (102, 255, 255), (325, 470, 70, 22), 0)



def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

draw_ellipse_angle(screen, (255, 255, 255), (455, 398, 7, 4), -44, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
