import pygame
from settings import *

cursor_img = pygame.image.load(resource_path("assets/mouse_cursor.png"))
cursor_img = resize_img(cursor_img)
cursor_img_rect = cursor_img.get_rect()

def draw_mouse_cursor():
    cursor_img_rect.center = pygame.mouse.get_pos()  
    screen.blit(cursor_img, cursor_img_rect) 