import pygame
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def main(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.height, self.width))