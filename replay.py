import pygame


# define button class 
class Replay_Button:
    def __init__(self, x, y):
        self.image = pygame.image.load("replay_button.png").convert_alpha()
        self.rect = self.image.get_rect()


    def draw(self, screen):
        screen.blit(self.image, self.rect)



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Replay Button")

background = pygame.image.load("inside_castle.png").convert()

replay_button = Replay_Button(300, 500)







