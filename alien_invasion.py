import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Инициализирует pygame, settings и объект экрана.
	pygame.init() # Инициализирует настройки для нормальной работы
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)) # Создаёт отображаемую область экрана ширина, высота
	pygame.display.set_caption("Alien Invasion")
	# Создание корабля
	ship = Ship(ai_settings, screen)

	# Запуск основного цикла игры
	while True:
		# Отслеживание событий клавиатуры и мыши
		gf.check_events(ship)
		# Нажатие - отпускание кнопок
		ship.update()
		# При каждом проходе цикла перерисовывается экран
		gf.update_screen(ai_settings, screen, ship)

run_game()
