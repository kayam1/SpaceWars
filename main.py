import pygame
pygame.init()

import sys
from src.enemy_spaceship import EnemySpaceship
from src.groups import *
from src.settings import *
from src.draw_menu import *
from src.initialize_game import *
from src.draw_gameover import *
from src.music_button import draw_music_button
 
def main():
	#Game start time 
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(False)

	#Loading Background image and resizing it 
	bg = pygame.image.load(resource_path("assets/Game_Background.png"))
	bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

	player, player_healthbar, wave_start_time, current_wave, max_spawns, spawn_interval, SPAWN_EVENT, MAX_WAVES, victory, wave_active = initialize_game()
	run = True
	game_active = False
	
	while run:

		#Main Menu
		if not game_active:
			music = pygame.mixer.music.load(resource_path("music_and_sfx/Ambitious Voyager.mp3"))
			pygame.mixer.music.play(-1)
			pygame.mixer.music.set_volume(0.3)
			should_start = draw_menu(bg)
			if should_start:
				game_active = True	
		#Background image
		screen.blit(bg, (0,0)) 
		draw_music_button()
		
		wave_text = wave_font.render(f"Wave ({current_wave}/{MAX_WAVES})", True, font_color)
		wave_text_pos = (SCREEN_WIDTH * 0.15 - wave_text.get_width(), SCREEN_HEIGHT * 0.08 - wave_text.get_height())
		screen.blit(wave_text, wave_text_pos)
		
		if enemy_spaceships and not wave_active:
			wave_active = True

		current_time = pygame.time.get_ticks()
		elapsed_time = (current_time - wave_start_time) / 1000
		wave_complete = elapsed_time > (spawn_interval / 1000) * max_spawns and not enemy_spaceships and current_wave <= MAX_WAVES and wave_active == True
		if wave_complete:
			if current_wave == MAX_WAVES:
				victory = True
			else:
				current_wave += 1
				max_spawns += 3
				spawn_interval -= 250
				pygame.time.set_timer(SPAWN_EVENT, spawn_interval, max_spawns) 
				wave_start_time = current_time
				
		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == SPAWN_EVENT:
				enemy = EnemySpaceship()
				all_sprites.add(enemy)
				enemy_spaceships.add(enemy)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:  
					toggle_music()

		#Getting mouse position every frame
		mouse_pos = pygame.mouse.get_pos()
		player.set_mouse_pos(mouse_pos)
		
		#Update all
		all_sprites.update()
		player_healthbar.setCurrentHp(player.current_hp)
		player_healthbar.update()
		
		#Draw all
		player_healthbar.blitHealthbar()
		all_sprites.draw(screen)
		
		#Game over screen or Victory screen
		if not ally_spaceships or not enemy_spaceships and victory:
			restart_game = draw_gameover(bg, victory)
			if restart_game:	#restart game
				player, player_healthbar, wave_start_time, current_wave, max_spawns, spawn_interval, SPAWN_EVENT, MAX_WAVES, victory, wave_active = initialize_game()
				music = pygame.mixer.music.load(resource_path("music_and_sfx/Ambitious Voyager.mp3"))
				pygame.mixer.music.play(-1)
				victory = False
				
		pygame.display.flip()
		clock.tick(fps)

	#End of game loop 
	pygame.quit() 
	sys.exit() 

if __name__ == "__main__":
	main()
