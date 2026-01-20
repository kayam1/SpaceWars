import pygame
from settings import *

class Healthbar():
    def __init__(self, max_hp):
        self.healthbar_img = pygame.image.load(resource_path("assets/healthbar.png")).convert_alpha()
        self.border_img = pygame.image.load(resource_path("assets/hb_border.png")).convert_alpha()
        
        self.healthbar_img = resize_img(self.healthbar_img)
        self.border_img = resize_img(self.border_img)
        self.healthbar_img_rect = self.healthbar_img.get_rect()
        self.border_img_rect = self.border_img.get_rect()
        self.width = self.healthbar_img.get_width()
        self.height = self.healthbar_img.get_height()

        self.current_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        #Create rect for healthbar and border, center them horizontally and give them height value
        self.hb_height = SCREEN_HEIGHT - SCREEN_HEIGHT*8/100
        self.healthbar_rect = self.healthbar_img.get_rect()
        self.border_rect = self.border_img.get_rect()
        center_pos = (screen_rect.centerx, self.hb_height)
        self.healthbar_rect.center = center_pos
        self.border_rect.center = center_pos

        self.max_hp = max_hp

    def update(self):

        health_ratio = self.current_hp / self.max_hp
        visible_width = int(self.width * health_ratio)
        
        #Clear the surface
        self.current_surface.fill((0, 0, 0, 0))
        
        if visible_width > 0:
            health_portion = pygame.Rect(0, 0, visible_width, self.height)
            self.current_surface.blit(self.healthbar_img, (0, 0), health_portion)  
        
    def setCurrentHp(self, hp):
        self.current_hp = hp

    def blitHealthbar(self):
        screen.blit(self.border_img, self.border_rect)
        screen.blit(self.current_surface, self.healthbar_rect)