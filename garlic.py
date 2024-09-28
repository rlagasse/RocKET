import pygame

from random import randint

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Garlic:
    def __init__ (self, x, y, scale):
        garlicImg = pygame.image.load('garlic.png')
        self.garlic = pygame.transform.scale(self.garlic, (int(garlicImg.get_width()*scale), garlicImg.get_height()*scale))


class Enemy(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
