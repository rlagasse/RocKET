import pygame

from random import randint

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Health Bar")
class Human:
    def __init__ (self, x, y, scale):
        humanImg = pygame.image.load('human_yellow.png')
        self.human = pygame.transform.scale(self.human, (int(humanImg.get_width()*scale), humanImg.get_height()*scale))