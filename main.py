import pygame
import sys
from ally_spaceship import AllySpaceship
from enemy_spaceship import EnemySpaceship
from healthbar import Healthbar
from groups import *
from settings import *
from draw_menu import *
from initialize_game import *
from draw_gameover import *


def main():
	pygame.init()
	#Getting game start time 
	clock = pygame.time.Clock()

	#Loading Background image and resizing it 
	bg = pygame.image.load(background_image_path)
	bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

	player, player_healthbar, start_time, wave, max_spawns, spawn_speed, SPAWN_EVENT = initialize_game()

	run = True
	game_active = False
	restart_game = False

	while run:

		if not game_active:
			should_start = draw_menu(bg)
			if should_start:
				game_active = True
		
		#Setting background image
		screen.blit(bg, (0,0)) 

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

		#Getting mouse position every frame
		mouse_pos = pygame.mouse.get_pos()
		player.set_mouse_pos(mouse_pos)
		
		#Update all
		player_healthbar.setCurrentHp(player.current_hp)
		all_sprites.update()
		player_healthbar.update()
		
		#Draw all
		all_sprites.draw(screen)
		player_healthbar.blitHealthbar()

		if not ally_spaceships:
			restart_game = draw_gameover(bg)
			if restart_game:
				player, player_healthbar, start_time, wave, max_spawns, spawn_speed, SPAWN_EVENT = initialize_game()
				
			
		#Managing fps (from setting file)
		pygame.display.flip()
		clock.tick(fps)

	#End of game loop 
	pygame.quit() 
	sys.exit() 

if __name__ == "__main__":
	main()
