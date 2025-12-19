import pygame

class PlayerLaser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.image.load("PlayerLaser1.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.velocity = 20
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = 10
        
    def update(self):
        self.rect.y -= self.velocity
        
        if self.rect.bottom < 0:
            self.kill()



