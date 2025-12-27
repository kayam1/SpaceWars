import pygame
from settings import *

def border():
    border_img = pygame.image.load("assets/hb_border1.png").convert_alpha()
    border_img_rect = border_img.get_rect()
