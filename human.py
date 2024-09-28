import pygame
import random
import time
import math
from random import randint

pygame.init()




#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 500

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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

pygame.display.set_caption("Get Home")


class human:
    def __init__ (self, x, y, scale, speed):
        #number =random.choice(list) 
        #print(number)
        self.speed= speed
        
        random_num_list = [1,2,3,4]
        if (random.choice(random_num_list) == '1'):
            humanImg = pygame.image.load('assets/human_yellow.png')
        elif (random.choice(random_num_list)  == '2'):
            humanImg = pygame.image.load('assets/human_green.png')
        elif (random.choice(random_num_list)  == '3'):
            humanImg = pygame.image.load('assets/human_red.png')
        else:
            humanImg = pygame.image.load('assets/human_purple.png')

        self.human = pygame.transform.scale(humanImg, (int(humanImg.get_width()*scale), humanImg.get_height()*scale))
        # create a rectangle object
        self.rect = self.human.get_rect()
        self.rect.center = (x,y)



    def draw(self):
        screen.blit(self.human, self.rect)    # draw the vampire on the screen


    def update(self):
        speed = 5
        self.rect.x -= speed


aHuman = human(400, 320, 0.5, 1.5)


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

    
    aHuman.draw() # create user to screen

    pygame.display.update() # display updates

pygame.quit()