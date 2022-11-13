import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
	"""Выпускает пулю, если ее максимум еще не достигнут."""
	#Создание новой пули и включение в группу bullets.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Реагирует на нажатие клавиш."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	#elif event.key == pygame.K_UP:
	#	ship.moving_up = True
	#elif event.key == pygame.K_DOWN:
	#	ship.moving_down = True
		
def check_keyup_events(event, ship):
	"""Реагирует на отпускание клавиш."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	#elif event.key == pygame.K_UP:
	#	ship.moving_up = False
	#elif event.key == pygame.K_DOWN:
	#	ship.moving_down = False
		
def check_events(ai_settings, screen, ship, bullets):
	"""Обрабатывает нажатия клавиш и события мыши."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN: # Нажатие любой кнопки
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP: #Отпускание кнопки
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""Обновляет изображения на экране и отображает новый экран."""		
	screen.fill(ai_settings.bg_color)
	#Все пули выводятся позади изображений корабля и пришельцев.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()	
	# Отображение последнего прорисованного экрана.
	pygame.display.flip() # Будет постоянно отрисовывать новую картинку поверх старой

def update_bullets(bullets):
	"""Обновляет позиции пуль и уничтожает старые пули."""
	#Обновление позиций пуль
	bullets.update()
	# Удаление пуль вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
