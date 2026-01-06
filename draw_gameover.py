import pygame
import sys
from settings import *
from button import Button
from music_button import *

def draw_gameover(bg, victory):
    #load pics and music
    if victory:
        logo_img = pygame.image.load("assets/victory.png")
        logo_img = pygame.transform.scale_by(logo_img, 0.7) 
        victory_music = pygame.mixer.music.load("music_and_sfx/TWEL - AscendOutro.mp3")
        pygame.mixer.music.play(0)
    else:
        logo_img = pygame.image.load("assets/game_over.png")
        logo_img = pygame.transform.scale_by(logo_img, 0.5) 
        gameover_music = pygame.mixer.music.load("music_and_sfx/Eerie Dreaming.mp3")
        pygame.mixer.music.play(-1)

    #Load buttons
    replay_btn_img = pygame.image.load("assets/replay_button.png")
    quit_btn_img = pygame.image.load("assets/quit_button.png")
    
    replay_btn_img = pygame.transform.scale(replay_btn_img, (150, 157))
    quit_btn_img = pygame.transform.scale(quit_btn_img, (150, 157))
    
    #Calculate positions
    logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, 100)
    replay_button = Button(SCREEN_WIDTH // 2 - 100, 500, replay_btn_img)
    quit_button = Button(SCREEN_WIDTH // 2 - 100, 700, quit_btn_img)
    
    menu = True
    while menu:
        #Draw background
        screen.blit(bg, (0, 0))
        music_button()
        
        #Draw logo
        screen.blit(logo_img, logo_pos)
        
        #Draw buttons
        if replay_button.draw(screen):
            return True  
            
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()
        
        #Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
    
    return False  