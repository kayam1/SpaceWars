import pygame
import sys
from ally_spaceship import AllySpaceship
from enemy_spaceship import EnemySpaceship
from groups import *
from settings import *

pygame.init()

#Setting game window name and size 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MyGame')

#Getting game start time 
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

#Loading Background image and resizing it 
BG = pygame.image.load(background_image_path)
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Creating instance of Player1 and adding to groups 
player = AllySpaceship()
all_sprites.add(player)
ally_spaceships.add(player)

max_spawns = 3
spawn_speed = 2000
wave = 1
# Set up a custom event
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, spawn_speed, max_spawns)  # Every 5000ms (5 seconds)

run = True
while run:
	
	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == SPAWN_EVENT:
			enemy = EnemySpaceship()
			all_sprites.add(enemy)
			enemy_spaceships.add(enemy)

	
	# Calculating elapsed time
	current_time = pygame.time.get_ticks()
	elapsed_time = (current_time - start_time) / 1000 # Convert to seconds
	
	if elapsed_time > (spawn_speed / 1000) * max_spawns + 0.1 and wave == 1 and not enemy_spaceships:
		wave += 1
		max_spawns = 5
		spawn_speed = 1000
		pygame.time.set_timer(SPAWN_EVENT, spawn_speed, max_spawns)  # Every 5000ms (5 seconds)
		start_time = current_time

	#Setting background image
	screen.blit(BG, (0,0)) 
		
	#Getting mouse position every frame
	mouse_pos = pygame.mouse.get_pos()
	player.set_mouse_pos(mouse_pos)
	
	#Update all
	all_sprites.update()
	
	#Draw all
	all_sprites.draw(screen)
	
	#Managing fps (from setting file)
	pygame.display.flip()
	clock.tick(fps)

#End of game loop 
pygame.quit() 
sys.exit() 
