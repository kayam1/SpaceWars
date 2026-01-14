import pygame
SCREEN_WIDTH,  SCREEN_HEIGHT = 1820, 980

#Setting game window name and size 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('MyGame')
background_image_path = "assets/Game_Background.png"
pygame.font.init()
font = pygame.font.Font("Assets/FugazOne-Regular.ttf", 18)
fps = 60
ALLY_LASER_CHANNEL_ID = 0
ALLY_DEATH_CHANNEL_ID = 1
ENEMY_LASER_CHANNEL_ID = 2
EMENY_DEATH_CHANNEL_ID = 3