import pygame
from src.settings import *

class PlayerLaser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.image.load(resource_path("assets/PlayerLaser1.png")).convert_alpha()
        self.image = resize_img(self.image)

        self.rect = self.image.get_rect()
        self.velocity = 25
        self.damage = 10
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        
    def update(self):
        self.rect.y -= self.velocity
        
        if self.rect.bottom < 0:
            self.kill()



