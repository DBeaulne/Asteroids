# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()     # create a clock object
    dt = 0                          # create a variable to store the delta time


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

        # limit the frame rate to 60 fps
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
