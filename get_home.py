import pygame
import math
import time
from healthbar import *
from garlic import Garlic

import random
# run with python get_home.py

# key coordinates
from pygame.locals import *

pygame.init()

screen_width = 1024
screen_height = 512

FLOOR = screen_height - 100
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('assets/forest_background_resize.png').convert()
background_width = background.get_width()
pygame.display.set_caption('Get Home')

## Clock information
clock = pygame.time.Clock()
FPS = 60
countdown_time = 30000  # 1 minute # # Set the countdown time to 1 minute (60000 milliseconds)
timer_has_started = False
program_is_running = True
font = pygame.font.Font(None, 74)  # None uses the default font, size 74
prev_sec = 30 # used in timing 

# scrolling background
scroll = 0
tiles = math.ceil(screen_width/ background_width) + 100 # adds 50 tiles, may increase as needed


class Sunlight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.sun_img = pygame.image.load('assets/sunlight_beam_resize.png')
        self.sunlight = pygame.transform.scale(self.sun_img, (int(self.sun_img.get_width()*scale), self.sun_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.sunlight.get_rect()
        self.rect.center = (x,y)
        self.sunlight_mask = pygame.mask.from_surface(self.sunlight)

    def update(self, scale_speed):
        self.scale += scale_speed
        self.sunlight = pygame.transform.scale(self.sun_img, (int(self.sun_img.get_width() * self.scale), int(self.sun_img.get_height() * self.scale)))
        self.rect = self.sunlight.get_rect(center=self.rect.center)
        self.sunlight_mask = pygame.mask.from_surface(self.sunlight)

    def draw(self):
        screen.blit(self.sunlight, self.rect)    # draw the vampire on the screen


class Vampire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = 100
        self.speed = speed
        self.scale = scale
        self.jump = False # jumping logic
        self.jump_velocity = 0
        self.x = x
        self.y = y
        self.type = "Vampire"
        self.vamp_img = pygame.image.load('assets/vampire_side_resized.png') # initially a vampire
        self.vampire = pygame.transform.scale(self.vamp_img, (int(self.vamp_img.get_width()*scale), self.vamp_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.vampire.get_rect()
        self.rect.center = (x,y)
        self.vampire_mask = pygame.mask.from_surface(self.vampire)

    def update_position(self):
        # Update x and y based on the current rectangle's center
        self.x, self.y = self.rect.center

    def bat_transform(self): # Change sprite into bat
        self.update_position()
        self.vamp_img = pygame.image.load('assets/purple_bat_resize.png') # initially a vampire
        self.vampire = pygame.transform.scale(self.vamp_img, (int(self.vamp_img.get_width()*self.scale), self.vamp_img.get_height()*self.scale)) # scale to screen
        # create a rectangle object
        self.rect = self.vampire.get_rect()
        self.rect.center = (self.x,self.y)
        self.vampire_mask = pygame.mask.from_surface(self.vampire)
        self.type = "Bat"
        self.speed = 8
    
    def vampire_transform(self): # Change sprite into vampire
        self.update_position()
        self.vamp_img = pygame.image.load('assets/vampire_side_resized.png') # initially a vampire
        self.vampire = pygame.transform.scale(self.vamp_img, (int(self.vamp_img.get_width()*self.scale), self.vamp_img.get_height()*self.scale)) # scale to screen
        # create a rectangle object
        self.rect = self.vampire.get_rect()
        self.rect.center = (self.x,self.y)
        self.vampire_mask = pygame.mask.from_surface(self.vampire)
        self.type = "Vampire"
        self.speed = 5

    def move(self, up, down, left, right): # move the rectangle around

        dx = 0
        dy = 0
        gravity = 0.5 
        if up:
            dy = -self.speed
            gravity = 0
            self.jump_velocity = 0
        if down:
            dy = self.speed
        if left:
            dx = -self.speed

        if right:
            dx = self.speed

        if self.jump: # jump detected
            self.jump_velocity = -5
            self.jump = False
        
        self.jump_velocity += gravity

        if self.jump_velocity > 10:
            self.jump_velocity
        dy += self.jump_velocity
        
        # added floor
        if self.rect.bottom + dy > FLOOR:
            dy = FLOOR - self.rect.bottom
        
        self.rect.x += dx
        self.rect.y += dy

        # Add vampire boundaries
        if self.rect.x < 0: 
            self.rect.x = 0  # Left side of the screen
        elif self.rect.x + self.rect.width > screen_width:
            self.rect.x = screen_width - self.rect.width  # Right side of the screen

        if self.rect.y < 0:
            self.rect.y = 0  # Top side of the screen
        elif self.rect.y + self.rect.height > screen_height:
            self.rect.y = screen_height - self.rect.height  # Bottom side of the screen

    def draw(self):
        screen.blit(self.vampire, self.rect)    # draw the vampire on the screen


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
        self.human_mask = pygame.mask.from_surface(self.human)

    def draw(self):
        screen.blit(self.human, self.rect)    # draw the vampire on the screen

    def update(self):
        speed = 5
        self.rect.x -= speed


aHuman = human(300, 370, 0.05, 1.5)

user = Vampire(400, screen_height - 100, 0.5, 5) # x, y, scale, speed
sunlight = Sunlight(0, 450, 1) # spawn in corner
health_bar = HealthBar(450, 10, 300, 40, 100)
test_garlic = Garlic(200, 250, 0.5)
# Used for Vampire/Bat conversion check
start_time_y = None
previous_y = None

# Garlic Generations
garlic_sprites = []
numGarlics = 30
for i in range(numGarlics):
    x = randint(screen_width, screen_width+10000)
    y = randint(screen_height - FLOOR, screen_height)
    garlic = Garlic(x, y, 0.5)
    garlic_sprites.append(garlic)

# Human Generations
human_sprites = []
numHumans = 10
for i in range(numHumans):
    x = randint(screen_width, screen_width+10000)
    aHuman = human(x, screen_height-150, 0.05, 1.5)
    human_sprites.append(aHuman)

def collision_detected(damage):
    user.health -= damage # decrease health and update
    health_bar.hp = user.health

def human_collision():
    if health_bar.hp < 100:
        user.health += 0.5
        health_bar.hp = user.health


# main game loop
game = True
while game:

    # exit if menu closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)

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


    # If the timer hasn't started yet, start it
    if not timer_has_started:
        timer_has_started = True
        start_time = pygame.time.get_ticks()  # Get the current ticks when the timer starts
    time_elapsed = pygame.time.get_ticks() - start_time      # Calculate how much time has passed since the timer started# Elapsed time in milliseconds

    time_left = countdown_time - time_elapsed
    if time_left <= 0:
        print("You win!")
        time_left = 0  # Set to zero to avoid negative time
        game = False
        # TODO: go to end screen

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
    # Vampire -> Bat if flying
    if up and user.type == "Vampire": # or user.: # Flying mode, speed up
        user.bat_transform()
    
    # Bat -> Vampire if on the ground for long enough
    if user.rect.y == 355 and user.type == "Bat":
        if previous_y != 355:
            previous_y = 355
            start_time_y = time.time()  # Start the timer when user.rect.y becomes 355
        elif start_time_y and time.time() - start_time_y >= 0.25: # wait 0.25 before becoming vampire
            user.vampire_transform()
    else: # not 355 anymore
        previous_y = None
        start_time_y = None

    #human
    for aHuman in human_sprites:
        aHuman.update()
        aHuman.draw()
        offset2 = (user.rect.x - aHuman.rect.x, user.rect.y - aHuman.rect.y)
        if aHuman.human_mask.overlap(user.vampire_mask, offset2):
            human_collision()

    # Health Bar
    health_bar.draw(screen)

    # Sunlight and Collision
    sunlight.draw()
    if sec != prev_sec: 
        if sec < 10: # last 10 seconds sun speeds up
            sunlight.update(0.1)
        elif sec < 25:
            sunlight.update(0.05)
        prev_sec = sec

    # Garlic and Collision
    for garlic in garlic_sprites: 
        garlic.update()
        screen.blit(garlic.garlic, garlic.rect)
        gar_offset = (user.rect.x - garlic.rect.x, user.rect.y - garlic.rect.y)
        if garlic.garlic_mask.overlap(user.vampire_mask, gar_offset):
            collision_detected(1)

    # Sunlight and Collision
    sun_offset = (user.rect.x - sunlight.rect.x, user.rect.y - sunlight.rect.y)
    if sunlight.sunlight_mask.overlap(user.vampire_mask, sun_offset):
        collision_detected(0.5)


    if health_bar.hp == 0:
        print("Game over!")
        game = False
        # TODO: go to end screen

    pygame.display.update() # display updates

pygame.quit()