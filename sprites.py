import pygame

screen_width = 1024
screen_height = 512

FLOOR = screen_height - 100

class Sunlight(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        sun_img = pygame.image.load('assets/sunlight_beam_resize.png')
        self.sunlight = pygame.transform.scale(sun_img, (int(sun_img.get_width()*scale), sun_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.sunlight.get_rect()
        self.rect.center = (x,y)
        self.sunlight_mask = pygame.mask.from_surface(self.sunlight)

    # def draw(self):
    #     screen.blit(self.sunlight, self.rect)    # draw the vampire on the screen


class Vampire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = 100
        self.speed = speed
        self.jump = False # jumping logic
        self.jump_velocity = 0
        self.x = x
        self.y = y
        vamp_img = pygame.image.load('assets/vampire_side_resized.png')
        self.vampire = pygame.transform.scale(vamp_img, (int(vamp_img.get_width()*scale), vamp_img.get_height()*scale)) # scale to screen
        # create a rectangle object
        self.rect = self.vampire.get_rect()
        self.rect.center = (x,y)
        self.vampire_mask = pygame.mask.from_surface(self.vampire)


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

    # def draw(self):
    #     screen.blit(self.vampire, self.rect)    # draw the vampire on the screen

