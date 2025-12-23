import pygame
SCREEN_WIDTH,  SCREEN_HEIGHT = 1820, 980

#Setting game window name and size 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('MyGame')
background_image_path = "assets/Game_Background.png"
fps = 60