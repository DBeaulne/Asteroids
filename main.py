# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()     # create a clock object
    dt = 0                          # create a variable to store the delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        clock.tick(60)  # pause the game loop for 1/60th of a second
        dt = clock.tick()/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
