# GameLogic.py

import pygame
from random import randint

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Health Bar")

class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp


    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "white", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w * ratio, self.h))

class Player:
    def get_damage(self, amount):
        if self.hp > 0:
            self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
    
    def get_health(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
        if self.hp >= self.max_hp:
            self.hp = self.max_hp



health_bar = HealthBar(250, 200, 300, 40, 100)

#run = True
# while run:
#     screen.fill("indigo")
    
#     health_bar.hp = 75
#     health_bar.draw(screen)


#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.flip()


#pygame.quit()

