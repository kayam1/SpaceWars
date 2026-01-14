import pygame
from ally_laser import PlayerLaser
from groups import *
from settings import *

class AllySpaceship(pygame.sprite.Sprite):
    laser_offset_left = -45  
    laser_offset_right = 15   
    laser_offset_top = -40 
    laser_cooldown = 200  #Milliseconds between shots
    last_shot_time = 0  #When last laser was fired
    mouse_pos = (0,0)
    
    
    def __init__(self):
        super().__init__()

        #Load the image
        self.image = pygame.image.load("assets/Playerlvl1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.max_hp = 100
        self.current_hp = self.max_hp
        self.spaceship_damage = 10
        self.last_damage_time = 0
        self.damage_cooldown = 1000


        #Load SFX
        self.laser_sfx = pygame.mixer.Sound("music_and_sfx/laser1.wav")
        self.laser_sfx.set_volume(0.1)
        self.laser_sfx_channel = pygame.mixer.Channel(ALLY_LASER_CHANNEL_ID)
        self.death_sfx = pygame.mixer.Sound("music_and_sfx/ally_death.wav")
        self.death_sfx.set_volume(0.1)
        self.death_sfx_channel = pygame.mixer.Channel(ALLY_LASER_CHANNEL_ID)

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.mouse_pos:
        #Follow mouse in both directions 
            self.rect.centerx = self.mouse_pos[0]  #X coordinate
            self.rect.centery = self.mouse_pos[1]  #Y coordinate 

        if current_time - self.last_shot_time > self.laser_cooldown:
            self.fire()
            self.last_shot_time = current_time

        #Keep the spaceship within screen bounds 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        #Check collision
        self.collision(current_time)
        
 
    def fire(self):
        left_laser = PlayerLaser(self.rect.centerx + self.laser_offset_left, self.rect.centery + self.laser_offset_top)
        right_laser = PlayerLaser(self.rect.centerx + self.laser_offset_right, self.rect.centery + self.laser_offset_top)
        all_sprites.add(left_laser, right_laser)
        ally_lasers.add(left_laser, right_laser)

        #SFX
        self.laser_sfx_channel.play(self.laser_sfx)

    def set_mouse_pos(self, mouse_pos):
        self.mouse_pos = mouse_pos

    def collision(self, current_time):
        for laser in enemy_lasers:
            if pygame.Rect.colliderect(self.rect, laser):
                self.current_hp -= laser.damage
                laser.kill()
                if self.current_hp <= 0:
                    self.kill()
                    self.death_sfx_channel.play(self.death_sfx)

        for spaceship in enemy_spaceships:
            if pygame.Rect.colliderect(self.rect, spaceship.rect):
                if current_time - self.last_damage_time > self.damage_cooldown:
                    self.current_hp -= self.spaceship_damage
                    self.last_damage_time = current_time
                    if self.current_hp <= 0:
                        self.kill()
                        self.death_sfx_channel.play(self.death_sfx)