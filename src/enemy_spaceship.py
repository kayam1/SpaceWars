import pygame
import random
from src.groups import *
from src.settings import *
from src.enemy_laser import EnemyLaser

class EnemySpaceship(pygame.sprite.Sprite):
    
    velocity = 20
    moving = True
    laser_cooldown = 800  # Milliseconds between shots
    last_shot_time = 0  # When last laser was fired
    health = 50
    contact_damage = 10

    def __init__(self):
        super().__init__()
        if random.randint(0,100) <= 50:
            self.image = pygame.image.load(resource_path("assets/RedEnemylvl1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(resource_path("assets/YellowEnemylvl1.png")).convert_alpha()
        self.image = resize_img(self.image)
        self.rect = self.image.get_rect()

        #Spawn and movement
        self.starting_posx = random.randint(0, SCREEN_WIDTH)
        self.starting_posy = -10
        self.rect.center = (self.starting_posx, self.starting_posy)
        self.ending_posx = random.randint(int(SCREEN_WIDTH*5/100) , int(SCREEN_WIDTH - SCREEN_WIDTH*5/100))
        self.ending_posy = random.randint(int(SCREEN_HEIGHT*10/100) , int(SCREEN_HEIGHT*30/100))

        #Laser Firing Offsets
        self.laser_horizontal_offset = self.image.get_width() // 4
        self.laser_vertical_offset = self.image.get_height() - self.image.get_height() * 0.4 

        #Load SFX
        self.laser_sfx = pygame.mixer.Sound(resource_path("music_and_sfx/laser2.wav"))
        self.laser_sfx.set_volume(0.2)
        self.laser_sfx_channel = pygame.mixer.Channel(ENEMY_LASER_CHANNEL_ID)
        self.death_sfx = pygame.mixer.Sound(resource_path("music_and_sfx/enemy_death.wav"))
        self.death_sfx.set_volume(0.2)
        self.death_sfx_channel = pygame.mixer.Channel(EMENY_DEATH_CHANNEL_ID)


    def update(self):

        dx = self.ending_posx - self.rect.centerx
        dy = self.ending_posy - self.rect.centery
        distance = (dx**2 + dy**2)**0.5
    
        #If we're close enough, snap to target
        if distance <= self.velocity:
            self.rect.centerx = self.ending_posx
            self.rect.centery = self.ending_posy
            self.moving = False
        else:
            #Move toward target
            self.rect.centerx += self.velocity * (dx / distance)
            self.rect.centery += self.velocity * (dy / distance)

        current_time = pygame.time.get_ticks()
        if not self.moving:
            if current_time - self.last_shot_time > self.laser_cooldown:
                self.fire()
                self.last_shot_time = current_time

        self.collision()
        

    def fire(self):
        left_laser = EnemyLaser(self.rect.centerx + self.laser_horizontal_offset, self.rect.centery + self.laser_vertical_offset)
        right_laser = EnemyLaser(self.rect.centerx - self.laser_horizontal_offset, self.rect.centery + self.laser_vertical_offset)
        all_sprites.add(left_laser, right_laser)
        enemy_lasers.add(left_laser, right_laser)

        #Play sfx
        self.laser_sfx_channel.play(self.laser_sfx)

    def collision(self):
        for laser in ally_lasers:
            if pygame.Rect.colliderect(self.rect, laser.rect):
                self.health -= laser.damage
                laser.kill()
                if self.health <= 0:
                    self.kill()
                    self.death_sfx_channel.play(self.death_sfx)

        

    