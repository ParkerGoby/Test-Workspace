import pygame
import player
from sys import exit

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h - 50))
pygame.display.set_caption('Bubbs')
icon_image = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon_image)
clock = pygame.time.Clock()

player_1 = player.Player(infoObject.current_w - 1000, infoObject.current_h - 1000, 50, 50)

while True:
    screen.fill((80, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player_1.main(screen)

    pygame.display.update()
    clock.tick(60)