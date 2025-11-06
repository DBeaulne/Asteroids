# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()     # create a clock object
    dt = 0                          # create a variable to store the delta time

    player_pos_x = SCREEN_WIDTH / 2
    player_pos_y = SCREEN_HEIGHT / 2
    player = Player(player_pos_x, player_pos_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # limit the frame rate to 60 fps
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
