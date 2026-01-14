import pygame
from settings import *
from button import Button

#Load images 
music_btn_img = pygame.image.load("assets/music_button.png")
music_pressed_img = pygame.image.load("assets/music_pressed.png")
music_btn_img = pygame.transform.scale(music_btn_img, (40, 42))
music_pressed_img = pygame.transform.scale(music_pressed_img, (40, 42))

#Create button 
music_button = Button(SCREEN_WIDTH - 50, 10, music_btn_img)
music_muted = False

def toggle_music():
    """Function to toggle mute state"""
    global music_muted, music_button
    
    # Toggle mute state
    music_muted = not music_muted
    
    # Update button image based on mute state
    if music_muted:   
        music_button.image = music_pressed_img 
    else:
        music_button.image = music_btn_img
    
    # Update volume
    if music_muted:
        pygame.mixer.music.set_volume(0)
        pygame.mixer.Channel(ALLY_LASER_CHANNEL_ID).set_volume(0)
        pygame.mixer.Channel(ENEMY_LASER_CHANNEL_ID).set_volume(0)
        pygame.mixer.Channel(EMENY_DEATH_CHANNEL_ID).set_volume(0)
        pygame.mixer.Channel(ALLY_DEATH_CHANNEL_ID).set_volume(0)
    else:
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.Channel(ALLY_LASER_CHANNEL_ID).set_volume(1)
        pygame.mixer.Channel(ENEMY_LASER_CHANNEL_ID).set_volume(1)
        pygame.mixer.Channel(EMENY_DEATH_CHANNEL_ID).set_volume(1)
        pygame.mixer.Channel(ALLY_DEATH_CHANNEL_ID).set_volume(1)

def draw_music_button():    
    if music_button.draw(screen):
        toggle_music()

    mute_text = font.render("press 'M' to mute", True, (255,255,255))
    screen.blit(mute_text, (SCREEN_WIDTH - 210, 18))