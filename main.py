# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}") 

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#Groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	#Containers
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	#Create player once, before the game loop
	player_sprite = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	#Create AsteroidField
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill('black')
		for update in updatable:
			update.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player_sprite) is True:
				print("Game over!")
				sys.exit()
		for thing in drawable:
			thing.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60)/1000



if __name__ == "__main__":
	main()
