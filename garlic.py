import pygame

from random import randint

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Garlic(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.init(self)

        garlicImg = pygame.image.load('asset/garlic.png')
        self.garlic = pygame.transform.scale(self.garlic, (int(garlicImg.get_width()*scale), garlicImg.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.garlic.get_rect()
        self.rect.center = (x,y)

    def draw(self):
        screen.blit(self.garlic, self.rect)

garlic = Garlic(400, 250, 0.5)



run = True
while run:
    screen.fill("indigo")

    garlic.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()