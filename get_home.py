import pygame

# run with python get_home.py

# key coordinates
from pygame.locals import *

pygame.init()

screen_width = 1024
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background_filler.png')
pygame.display.set_caption('Get Home')

class Vampire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed

        vamp_img = pygame.image.load('vampire_filler.png')
        self.vampire = pygame.transform.scale(vamp_img, (int(vamp_img.get_width()*scale), vamp_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.vampire.get_rect()
        self.rect.center = (x,y)

    def move(self, up, down, left, right): # move the rectangle around

        dx = 0
        dy = 0

        if up:
            dy = -self.speed
        if down:
            dy = self.speed
        if left:
            dx = -self.speed
        if right:
            dx = self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.vampire, self.rect)    # draw the vampire on the screen


# generate vampire in center of screen
user = Vampire(400, 320, 0.5, 1) # x, y, scale, speed



# main game loop
game = True
while game:

    # background image
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():

        # end game
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    up = keys[pygame.K_w]
    down = keys[pygame.K_s]
    left = keys[pygame.K_a]
    right = keys[pygame.K_d]

    user.move(up, down, left, right)
    user.draw() # create user to screen




        # # keyboard button press and add to movement
        # if event.type == KEYDOWN:
        #     if event.key == (pygame.K_UP or pygame.K_w):
        #         moving_up = True
        #     elif event.key == (pygame.K_DOWN or pygame.K_s):
        #         moving_down = True
        #     elif event.key == (pygame.K_LEFT or pygame.K_a):
        #         moving_left = True
        #     elif event.key == (pygame.K_RIGHT or pygame.K_d):
        #         moving_right = True
        #     elif event.key == pygame.K_ESCAPE:
        #         game = False
        
        # # keyboard button release
        # if event.type == KEYUP:
        #     if event.key == (pygame.K_UP or pygame.K_w):
        #         moving_up = True
        #     elif event.key == (pygame.K_DOWN or pygame.K_s):
        #         moving_down = True
        #     elif event.key == (pygame.K_LEFT or pygame.K_a):
        #         moving_left = True
        #     elif event.key == (pygame.K_RIGHT or pygame.K_d):
        #         moving_right = True
        



    pygame.display.update() # display updates

pygame.quit()