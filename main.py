# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()     # create a clock object
    dt = 0                          # create a variable to store the delta time

    # Groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # initial player positioning
    player_pos_x = SCREEN_WIDTH / 2
    player_pos_y = SCREEN_HEIGHT / 2
    player = Player(player_pos_x, player_pos_y)
    asteroid_field = AsteroidField()
    


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # limit the frame rate to 60 fps
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
