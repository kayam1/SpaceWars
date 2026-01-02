import pygame
import sys
from settings import *
from button import Button

def draw_gameover(bg):
    # Load menu assets
    logo_img = pygame.image.load("assets/game_over.png")
    replay_btn_img = pygame.image.load("assets/replay_button.png")
    quit_btn_img = pygame.image.load("assets/quit_button.png")
    
    # Scale images
    logo_img = pygame.transform.scale_by(logo_img, 0.5) 
    replay_btn_img = pygame.transform.scale(replay_btn_img, (200, 150))
    quit_btn_img = pygame.transform.scale(quit_btn_img, (200, 150))
    
    # Calculate positions
    logo_pos = (SCREEN_WIDTH // 2 - logo_img.get_width() // 2, 50)
    replay_button = Button(SCREEN_WIDTH // 2 - 100, 500, replay_btn_img)
    quit_button = Button(SCREEN_WIDTH // 2 - 100, 700, quit_btn_img)
    
    menu = True
    while menu:
        # Draw background
        screen.blit(bg, (0, 0))
        
        # Draw logo
        screen.blit(logo_img, logo_pos)
        
        # Draw buttons
        if replay_button.draw(screen):
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