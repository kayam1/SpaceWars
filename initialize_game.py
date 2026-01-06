import pygame
from ally_spaceship import AllySpaceship
from healthbar import Healthbar
from groups import *

def initialize_game():
    #Clear all sprite groups
    all_sprites.empty()
    ally_spaceships.empty()
    enemy_spaceships.empty()
    
    #Create player instance and add to groups
    player = AllySpaceship()
    all_sprites.add(player)
    ally_spaceships.add(player)
    
    #Create healthbar instance
    player_healthbar = Healthbar(player.max_hp)
    
    #Wave management
    start_time = pygame.time.get_ticks()
    MAX_WAVES = 2
    current_wave = 1
    max_spawns = 3
    spawn_interval = 2000
    
    #Set up 1st wave spawn event
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, spawn_interval, max_spawns)
    
    return player, player_healthbar, start_time, current_wave, max_spawns, spawn_interval, SPAWN_EVENT, MAX_WAVES