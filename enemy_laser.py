import pygame
from settings import *

class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, damage, velocity):
        super().__init__()

        self.image = pygame.image.load("assets/EnemyLaser1.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.velocity = velocity
        self.damage = damage
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def update(self):
        self.rect.y += self.velocity
        
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
