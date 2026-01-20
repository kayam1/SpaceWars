import os
import pygame
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resize_img(image):
    image = pygame.transform.scale_by(image, (SCREEN_WIDTH / MAX_WIDTH, SCREEN_HEIGHT / MAX_HEIGHT))
    return image

os.environ['SDL_VIDEO_CENTERED'] = '1'

windowed_width_offset = 10
windowed_height_offset = 60
MAX_WIDTH, MAX_HEIGHT = 1920 - windowed_width_offset, 1080 - windowed_height_offset

info = pygame.display.Info()
#SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w - windowed_width_offset, info.current_h - windowed_height_offset
#CREEN_WIDTH, SCREEN_HEIGHT = 1366 - windowed_width_offset, 768 - windowed_height_offset  #Test for laptop resolution
SCREEN_WIDTH, SCREEN_HEIGHT = 2000 - windowed_width_offset, 1500 - windowed_height_offset #Test for higher unsupported resolution

if SCREEN_WIDTH > MAX_WIDTH and SCREEN_HEIGHT > MAX_HEIGHT:
    SCREEN_WIDTH, SCREEN_HEIGHT = MAX_WIDTH, MAX_HEIGHT
    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('SpaceWars')
screen_area = SCREEN_WIDTH * SCREEN_HEIGHT

pygame.font.init()
def init_mute_font():
    base_font_size = int(SCREEN_HEIGHT * 0.02)  # 2% of screen height
    return pygame.font.Font(resource_path("fonts/fugazOne.ttf"), base_font_size)

def init_wave_font():
    base_font_size = int(SCREEN_HEIGHT * 0.05)  # 2% of screen height
    return pygame.font.Font(resource_path("fonts/fugazOne.ttf"), base_font_size)
font_color = 71, 215, 255
mute_font = init_mute_font()
wave_font = init_wave_font()

fps = 60
ALLY_LASER_CHANNEL_ID = 0
ALLY_DEATH_CHANNEL_ID = 1
ENEMY_LASER_CHANNEL_ID = 2
EMENY_DEATH_CHANNEL_ID = 3