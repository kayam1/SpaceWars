import pygame
import sys
from settings import *
from button import Button

def draw_menu(bg):
    # Load menu assets
    logo_img = pygame.image.load("assets/game_logo.png")
    play_btn_img = pygame.image.load("assets/play_button.png")
    quit_btn_img = pygame.image.load("assets/quit_button.png")
    
    # Scale images
    logo_img = pygame.transform.scale_by(logo_img, 0.7) 
    play_btn_img = pygame.transform.scale(play_btn_img, (200, 150))
    quit_btn_img = pygame.transform.scale(quit_btn_img, (200, 150))
    
    # Calculate positions
    logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, 150)
    play_button = Button(SCREEN_WIDTH // 2 - 100, 400, play_btn_img)
    quit_button = Button(SCREEN_WIDTH // 2 - 100, 600, quit_btn_img)
    
    menu = True
    while menu:
        # Draw background
        screen.blit(bg, (0, 0))
        
        # Draw logo
        screen.blit(logo_img, logo_pos)
        
        # Draw buttons
        if play_button.draw(screen):
            # Play button clicked - start the game
            return True  # Return True to indicate game should start
            
        if quit_button.draw(screen):
            # Quit button clicked - exit the game
            pygame.quit()
            sys.exit()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
    
    return False  # This line is reached if menu loop exits without play being clicked