import pygame
from settings import *
from button import Button

# Load images once
music_btn_img = pygame.image.load("assets/music_button.png")
music_pressed_img = pygame.image.load("assets/music_pressed.png")
music_btn_img = pygame.transform.scale(music_btn_img, (40, 42))
music_pressed_img = pygame.transform.scale(music_pressed_img, (40, 42))

# Create button once
music_button = Button(SCREEN_WIDTH - 50, 10, music_btn_img)
music_muted = False

def draw_music_button():
    global music_muted, music_button
    
    # Update button image based on mute state
    if music_muted:   
        current_img = music_pressed_img 
    else:
        current_img = music_btn_img

    music_button.image = current_img
    
    # Check for button click
    if music_button.draw(screen):
        # Toggle mute state
        music_muted = not music_muted
        
        # Update volume
        if music_muted:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(0.3)