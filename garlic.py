import pygame

from random import randrange
from random import randint

# pygame.init()

screen_width = 1024
screen_height = 512
FLOOR = screen_height - 100


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Garlic(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        garlicImg = pygame.image.load('assets/garlic_resize.png')
        self.garlic = pygame.transform.scale(garlicImg, (int(garlicImg.get_width()*scale), garlicImg.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.garlic.get_rect()
        self.rect.center = (x,y)
        self.garlic_mask = pygame.mask.from_surface(self.garlic)

    # def draw(self, surface):
    #     screen.blit(self.garlic, self.rect)

    def update(self):
        speed = 5
        self.rect.x -= speed

# def generate_garlic_sprites():
#     garlic_sprites = []
#     numGarlics = 25
#     #garlic = Garlic( 400, 250, 0.5)

#     for i in range(numGarlics):
#         x = randint(screen_width, screen_width+10000)
#         y = randint(screen_height - FLOOR, screen_height)
#         garlic = Garlic(x, y, 0.5)
#         garlic_sprites.append(garlic)

# run = True
# while run:
#     screen.fill("indigo")

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     for garlic in garlic_sprites: 

#         garlic.update()
#         garlic.draw(screen)

#     pygame.display.flip()

# pygame.quit()