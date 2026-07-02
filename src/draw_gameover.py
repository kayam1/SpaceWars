import pygame
import sys
from src.settings import *
from src.button import Button
from src.music_button import *
from src.mouse_cursor import *
 
def draw_gameover(bg, victory):
    #Load win/lose pics and music
    if victory:
        logo_img = pygame.image.load(resource_path("assets/victory.png")).convert_alpha()
        victory_music = pygame.mixer.music.load(resource_path("music_and_sfx/TWEL - AscendOutro.mp3"))
    else:
        logo_img = pygame.image.load(resource_path("assets/game_over.png")).convert_alpha()
        gameover_music = pygame.mixer.music.load(resource_path("music_and_sfx/Eerie Dreaming.mp3"))

    #Load buttons
    replay_btn_img = pygame.image.load(resource_path("assets/replay_button.png")).convert_alpha()
    quit_btn_img = pygame.image.load(resource_path("assets/quit_button.png")).convert_alpha()
    
    #Resize Images
    logo_img = resize_img(logo_img)
    replay_btn_img = resize_img(replay_btn_img)
    quit_btn_img = resize_img(quit_btn_img)

    #Calculate positions
    if victory:
        logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, SCREEN_HEIGHT * 0.35 - logo_img.get_height())
        replay_button = Button(replay_btn_img, 0.5, 0.55)
        quit_button = Button(quit_btn_img, 0.5, 0.75)
    else:
        logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, SCREEN_HEIGHT * 0.45 - logo_img.get_height())
        replay_button = Button(replay_btn_img, 0.5, 0.6)
        quit_button = Button(quit_btn_img, 0.5, 0.8)
    
    
    pygame.mixer.music.play(0)
    menu = True
    while menu:
        #Draw background
        screen.blit(bg, (0, 0))
        draw_music_button()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  
                    toggle_music()
        
        draw_mouse_cursor()
        pygame.display.update()
    
    return False  