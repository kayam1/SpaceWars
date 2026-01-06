import pygame
import sys
from settings import *
from button import Button
from music_button import *


def draw_menu(bg):
    #Load menu assets
    logo_img = pygame.image.load("assets/game_logo.png")
    play_btn_img = pygame.image.load("assets/play_button.png")
    quit_btn_img = pygame.image.load("assets/quit_button.png")
    credits_img = pygame.image.load("assets/layer 2.png")

    #Scale images
    logo_img = pygame.transform.scale_by(logo_img, 0.9) 
    play_btn_img = pygame.transform.scale(play_btn_img, (150, 157))
    quit_btn_img = pygame.transform.scale(quit_btn_img, (150, 157))
    credits_img = pygame.transform.scale(credits_img, (250, 100))
    

    #Calculate positions
    logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, 150)
    play_button = Button(SCREEN_WIDTH // 2 - 100, 400, play_btn_img)
    quit_button = Button(SCREEN_WIDTH // 2 - 100, 600, quit_btn_img)
    
    menu = True
    while menu:
        #Draw background
        screen.blit(bg, (0, 0))
        screen.blit(credits_img, (760, 800))
        draw_music_button()
        
        #Draw logo
        screen.blit(logo_img, logo_pos)
        
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
        
        pygame.display.update()
    
    return False  