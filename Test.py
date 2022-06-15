import pygame
from sys import exit

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption('Bubbs')
icon_image = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)