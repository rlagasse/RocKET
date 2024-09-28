import pygame
import math

# run with python get_home.py

# key coordinates
from pygame.locals import *

pygame.init()

screen_width = 1024
screen_height = 512
gravity = 0.5
FLOOR = screen_height - 100
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('assets/forest_background_resize.png').convert()
background_width = background.get_width()
pygame.display.set_caption('Get Home')

clock = pygame.time.Clock()
FPS = 60

# scrolling background
scroll = 0
tiles = math.ceil(screen_width/ background_width) + 50 # adds 50 tiles, may increase as needed
print(tiles)

class Vampire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = 100
        self.speed = speed
        self.jump = False # jumping logic
        self.jump_velocity = 0
        vamp_img = pygame.image.load('assets/vampire_side_resized.png')
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

        if self.jump: # jump detected
            self.jump_velocity = -2
            self.jump = False

        self.jump_velocity += gravity # come back down with gravity
        if self.jump_velocity > 10:
            self.jump_velocity 
        dy += self.jump_velocity
        
        # added floor
        if self.rect.bottom + dy > FLOOR:
            dy = FLOOR - self.rect.bottom
        
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.vampire, self.rect)    # draw the vampire on the screen

    # def gravity(self):
    #     self.movey += 3.2
        
    #     if self.rect.y > screen_height and self.movey >= 0:
    #         self.movey= 0
    #         self.rect.y = screen_height-ty-ty

# generate vampire in center of screen
user = Vampire(400, 320, 0.5, 1.5) # x, y, scale, speed



# main game loop
game = True
while game:

    clock.tick(FPS)

    # scrolling background
    screen.fill((0, 0, 0))
    for i in range (0, tiles):
        screen.blit(background, (i*background_width + scroll, 0))
    
    scroll -= 5
    if scroll > background_width:
        scroll = 0

    #pygame.draw.line(screen, (0, 0, 0), (0, FLOOR), (screen_width, FLOOR))

    for event in pygame.event.get():

        # end game
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    up = keys[pygame.K_w]
    down = keys[pygame.K_s]
    left = keys[pygame.K_a]
    right = keys[pygame.K_d]
    jump = keys[pygame.K_SPACE]
    if jump and user.alive: # user jumped
        user.jump = True
    #user.gravity()

    user.move(up, down, left, right)
    user.draw() # create user to screen

    pygame.display.update() # display updates

pygame.quit()