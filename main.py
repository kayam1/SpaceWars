import pygame
import sys
from enemy_spaceship import EnemySpaceship
from groups import *
from settings import *
from draw_menu import *
from initialize_game import *
from draw_gameover import *
from music_button import draw_music_button

def main():
	pygame.init()
	#Game start time 
	clock = pygame.time.Clock()

	#Loading Background image and resizing it 
	bg = pygame.image.load(background_image_path)
	bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

	player, player_healthbar, start_time, current_wave, max_spawns, spawn_interval, SPAWN_EVENT, MAX_WAVES = initialize_game()
	
	run = True
	game_active = False
	restart_game = False
	victory = False

	while run:

		#Main Menu
		if not game_active:
			music = pygame.mixer.music.load("music_and_sfx/Ambitious Voyager.mp3")
			pygame.mixer.music.play(-1)
			pygame.mixer.music.set_volume(0.3)
			should_start = draw_menu(bg)
			if should_start:
				game_active = True	
		#Background image
		screen.blit(bg, (0,0)) 
		draw_music_button()

		current_time = pygame.time.get_ticks()
		elapsed_time = (current_time - start_time) / 1000
		wave_complete = elapsed_time > (spawn_interval / 1000) * max_spawns + 0.1 and not enemy_spaceships and current_wave <= MAX_WAVES
		if wave_complete:
			if current_wave == MAX_WAVES:
				victory = True
			else:
				current_wave += 1
				print(current_wave)
				max_spawns += 3
				spawn_interval -= 300
				pygame.time.set_timer(SPAWN_EVENT, spawn_interval, max_spawns)  
				start_time = current_time  
		
		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == SPAWN_EVENT:
				enemy = EnemySpaceship()
				all_sprites.add(enemy)
				enemy_spaceships.add(enemy)

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

		#Game over screen or Victory screen
		if not ally_spaceships or not enemy_spaceships and victory:
			restart_game = draw_gameover(bg, victory)
			if restart_game:	#restart game
				player, player_healthbar, start_time, current_wave, max_spawns, spawn_speed, SPAWN_EVENT, MAX_WAVES = initialize_game()
				music = pygame.mixer.music.load("music_and_sfx/Ambitious Voyager.mp3")
				pygame.mixer.music.play(-1)
				victory = False
				
		pygame.display.flip()
		clock.tick(fps)

	#End of game loop 
	pygame.quit() 
	sys.exit() 

if __name__ == "__main__":
	main()
