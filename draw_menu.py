import pygame
import sys
from settings import *
from button import Button
from music_button import *
from mouse_cursor import *


def draw_menu(bg):
    #Load menu assets
    logo_img = pygame.image.load(resource_path("assets/game_logo.png")).convert_alpha()
    play_btn_img = pygame.image.load(resource_path("assets/play_button.png")).convert_alpha()
    quit_btn_img = pygame.image.load(resource_path("assets/quit_button.png")).convert_alpha()
    credits_img = pygame.image.load(resource_path("assets/twel.png")).convert_alpha()

    #Resize images
    logo_img = resize_img(logo_img)
    play_btn_img = resize_img(play_btn_img)
    quit_btn_img = resize_img(quit_btn_img)
    credits_img = resize_img(credits_img)
    
    #Calculate positions
    logo_pos = (SCREEN_WIDTH * 0.5 - logo_img.get_width() // 2, SCREEN_HEIGHT * 0.25 - logo_img.get_height() // 2)
    credits_pos = (SCREEN_WIDTH * 0.5 - credits_img.get_width() // 2, SCREEN_HEIGHT * 0.88 - credits_img.get_height() // 2)
    play_button = Button(play_btn_img, 0.5, 0.5)
    quit_button = Button(quit_btn_img, 0.5, 0.7)
    
    menu = True
    while menu:
        #Draw Menu
        screen.blit(bg, (0, 0))
        screen.blit(logo_img, logo_pos)
        screen.blit(credits_img, credits_pos)
        draw_music_button()
    
        #Draw buttons
        if play_button.draw(screen):
            return True  
            
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  
                    toggle_music()

        draw_mouse_cursor() #draw last to be on top of everything
        pygame.display.update()
    
    return False  