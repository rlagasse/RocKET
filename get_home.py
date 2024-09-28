import pygame

# reference for starting: https://www.geeksforgeeks.org/introduction-to-pygame/
# reference for also starting: https://www.youtube.com/watch?v=DHgj5jhMJKg&list=PLjcN1EyupaQm20hlUE11y9y8EY2aXLpnv
# key coordinates
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Get Home')

# generate
x = 100
y = 200
vamp_img = pygame.image.load('vampire_filler.png')

# create a rectangle object
rect = vamp_img.get_rect()
rect.center = (x,y)

run = True
while run:


    screen.blit(vamp_img, rect) # draw the vampire on the screen
    for event in pygame.event.get():
        # end
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # display character

pygame.quit()