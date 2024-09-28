import pygame
import math
import time
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

## Clock information
time = pygame.time.Clock()
FPS = 60
countdown_time = 60000  # 1 minute # # Set the countdown time to 1 minute (60000 milliseconds)
timer_has_started = False
program_is_running = True
font = pygame.font.Font(None, 74)  # None uses the default font, size 74


# scrolling background
scroll = 0
tiles = math.ceil(screen_width/ background_width) + 100 # adds 50 tiles, may increase as needed


class Sunlight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        sun_img = pygame.image.load('assets/sunlight_beam_resize.png')
        self.sunlight = pygame.transform.scale(sun_img, (int(sun_img.get_width()*scale), sun_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.sunlight.get_rect()
        self.rect.center = (x,y)
        self.sunlight_mask = pygame.mask.from_surface(self.sunlight)

    def draw(self):
        screen.blit(self.sunlight, self.rect)    # draw the vampire on the screen


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
        self.vampire_mask = pygame.mask.from_surface(self.vampire)


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


user = Vampire(400, 320, 0.5, 1.5) # x, y, scale, speed
sunlight = Sunlight(0, 450, 1) # spawn in corner

# main game loop
game = True
while game:

    # exit if menu closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    time.tick(FPS)

    # scrolling background
    screen.fill((0, 0, 0))
    for i in range (0, tiles):
        screen.blit(background, (i*background_width + scroll, 0))
    scroll -= 5
    if scroll > background_width:
        scroll = 0


    # check key pressed events
    keys = pygame.key.get_pressed()

    up = keys[pygame.K_w]
    down = keys[pygame.K_s]
    left = keys[pygame.K_a]
    right = keys[pygame.K_d]
    jump = keys[pygame.K_SPACE]
    if jump and user.alive: # user jumped
        user.jump = True
    #user.gravity()

    # Stopwatch

    # If the timer hasn't started yet, start it
    if not timer_has_started:
        timer_has_started = True
        start_time = pygame.time.get_ticks()  # Get the current ticks when the timer starts
    time_elapsed = pygame.time.get_ticks() - start_time      # Calculate how much time has passed since the timer started# Elapsed time in milliseconds

    time_left = countdown_time - time_elapsed

    if time_left <= 0:
        print("Time's up!")
        time_left = 0  # Set to zero to avoid negative time
        program_is_running = False  # Stop the loop for demonstration purposes

    # Convert remaining time to seconds and format it
    sec = (time_left // 1000) % 60
    min = (time_left // 60000) % 60
    display_time = f"{min:02}:{sec:02}"  # Format as MM:SS

    # Render the timer text
    text_surface = font.render(display_time, True, (255, 255, 255))  # White color
    text_rect = text_surface.get_rect(center=(950, 30))  # Top-Right corner

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)



    # Vampire
    user.move(up, down, left, right)
    user.draw() # create user to screen

    # Sunlight and Collision
    sunlight.draw()
    offset = (user.rect.x - sunlight.rect.x, user.rect.y - sunlight.rect.y)
    if sunlight.sunlight_mask.overlap(user.vampire_mask, offset):
        print("collision detected")

    pygame.display.update() # display updates

pygame.quit()