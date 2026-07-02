import pygame
from src.settings import *
from src.button import Button

#Load images 
music_btn_img = pygame.image.load(resource_path("assets/music_button.png")).convert_alpha()
music_pressed_img = pygame.image.load(resource_path("assets/music_pressed.png")).convert_alpha()
music_btn_img = resize_img(music_btn_img)
music_pressed_img = resize_img(music_pressed_img)

#Create button 
music_btn_pos = (SCREEN_WIDTH * 0.982 - music_btn_img.get_width() // 2, SCREEN_HEIGHT * 0.03 - music_btn_img.get_height() // 2)
music_muted = False
music_button = music_btn_img

def toggle_music():
    global music_muted, music_button
    
    # Toggle mute state
    music_muted = not music_muted
    
    # Update button image based on mute state
    if music_muted:   
        music_button = music_pressed_img 
    else:
        music_button = music_btn_img
    
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

    draw_music_button()

def draw_music_button():    
    screen.blit(music_button, music_btn_pos)

    mute_text = mute_font.render("press 'M' to mute", True, font_color)
    mute_text_pos = (SCREEN_WIDTH * 0.92 - mute_text.get_width() // 2 , SCREEN_HEIGHT * 0.03 - mute_text.get_height() // 2)
    screen.blit(mute_text, mute_text_pos)