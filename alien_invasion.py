import pygame
from pygame.sprite import Group
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
	# Создание группы для хранения пуль.
	bullets = Group()

	# Запуск основного цикла игры
	while True:
		# Отслеживание событий клавиатуры и мыши
		gf.check_events(ai_settings, screen, ship, bullets)
		# Нажатие - отпускание кнопок
		ship.update()
		gf.update_bullets(bullets)
		# При каждом проходе цикла перерисовывается экран
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
