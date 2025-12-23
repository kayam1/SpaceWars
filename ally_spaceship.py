import pygame
from ally_laser import PlayerLaser
from groups import *
from settings import *

class AllySpaceship(pygame.sprite.Sprite):
    laser_offset_left = -45  # Pixels left of center
    laser_offset_right = 15   # Pixels right of center
    laser_offset_top = -40 #pixels lower from top
    laser_cooldown = 200  # Milliseconds between shots
    last_shot_time = 0  # When last laser was fired
    mouse_pos = (0,0)
    max_health = 100
    current_health = max_health

    def __init__(self):
        super().__init__()
        # Load the image
        self.image = pygame.image.load("assets/Playerlvl1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.healthbar_img = pygame.image.load("assets/HealthBar.png").convert_alpha()
        self.healthbar_img_rect = self.healthbar_img.get_rect()
        self.border_img = pygame.image.load("assets/HealthBarBorder.png").convert_alpha()
        self.border_img_rect = self.healthbar_img.get_rect()
        self.healthbar_img = pygame.transform.scale_by(self.healthbar_img, 0.5)
        self.border_img = pygame.transform.scale_by(self.border_img, 0.5)
        # If border is larger than health bar align them this way
        self.healthbar_rect = self.healthbar_img.get_rect()
        self.border_rect = self.border_img.get_rect()
        center_pos = (screen_rect.centerx, 850)
        self.healthbar_rect.center = center_pos
        self.border_rect.center = center_pos

       
    def update(self):
        """Update spaceship position."""
        current_time = pygame.time.get_ticks()
        if self.mouse_pos:
        # Follow mouse in BOTH directions (center on mouse)
            self.rect.centerx = self.mouse_pos[0]  # X coordinate
            self.rect.centery = self.mouse_pos[1]  # Y coordinate 

        if current_time - self.last_shot_time > self.laser_cooldown:
            self.fire()
            self.last_shot_time = current_time

        # Keep the spaceship within screen bounds 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # Draw border first (background)
        screen.blit(self.border_img, self.border_rect)
        # Draw health bar on top
        screen.blit(self.healthbar_img, self.healthbar_rect)
        self.collision()


    def fire(self):
        left_laser = PlayerLaser(self.rect.centerx + self.laser_offset_left, self.rect.centery + self.laser_offset_top)
        right_laser = PlayerLaser(self.rect.centerx + self.laser_offset_right, self.rect.centery + self.laser_offset_top)
        all_sprites.add(left_laser, right_laser)
        ally_lasers.add(left_laser, right_laser)

    def set_mouse_pos(self, mouse_pos):
        self.mouse_pos = mouse_pos

    def collision(self):
        for laser in enemy_lasers:
            if pygame.Rect.colliderect(self.rect, laser):
                self.current_health -= laser.damage
                self.healthBar()
                laser.kill()
                if self.current_health <= 0:
                    self.kill()

    def healthBar(self):
        ratio = self.current_health / self.max_health * 100
        print (ratio)
        