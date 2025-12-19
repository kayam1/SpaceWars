import pygame
import random
from groups import *
from settings import *
from enemy_laser import EnemyLaser

class EnemySpaceship(pygame.sprite.Sprite):
    velocity = 10
    moving = True
    
    #Laser handling
    laser_cooldown = 800  # Milliseconds between shots
    last_shot_time = 0  # When last laser was fired
    laser_offset_left = -30  # Pixels left of center
    laser_offset_right = 10   # Pixels right of center
    laser_offset_top = 25 #pixels higher from top
    damage = 10
    laser_velocity = 10
    health = 50

    def __init__(self):
        super().__init__()
        if random.randint(0,100) <= 50:
            self.image = pygame.image.load("assets/RedEnemylvl1.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/YellowEnemylvl1.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.starting_posx = random.randint(0, SCREEN_WIDTH)
        self.starting_posy = -10
        self.center = (self.starting_posx, self.starting_posy)
        self.ending_posx = random.randint(100 , 1720)
        self.ending_posy = random.randint(100, 300)

    def update(self):

        dx = self.ending_posx - self.rect.centerx
        dy = self.ending_posy - self.rect.centery
        distance = (dx**2 + dy**2)**0.5
    
        # If we're close enough, snap to target
        if distance <= self.velocity:
            self.rect.centerx = self.ending_posx
            self.rect.centery = self.ending_posy
            self.moving = False
        else:
            # Move toward target
            self.rect.centerx += self.velocity * (dx / distance)
            self.rect.centery += self.velocity * (dy / distance)

        current_time = pygame.time.get_ticks()
        if not self.moving:
            if current_time - self.last_shot_time > self.laser_cooldown:
                self.fire()
                self.last_shot_time = current_time

        self.collision()
        

    def fire(self):
        left_laser = EnemyLaser(self.rect.centerx + self.laser_offset_left, self.rect.centery + self.laser_offset_top, self.damage, self.laser_velocity)
        right_laser = EnemyLaser(self.rect.centerx + self.laser_offset_right, self.rect.centery + self.laser_offset_top, self.damage, self.laser_velocity)
        all_sprites.add(left_laser, right_laser)
        enemy_lasers.add(left_laser, right_laser)


    def collision(self):
        for laser in ally_lasers:
            if pygame.Rect.colliderect(self.rect, laser):
                self.health -= laser.damage
                laser.kill()
                if self.health <= 0:
                    self.kill()



       
       