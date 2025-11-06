import pygame
from circleshape import CircleShape
from constants import *

# Asteroid class that inherits from CircleShape
class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, ASTEROID_MAX_RADIUS)

    def draw(self, screen):
      pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, width=2)

    def update(self, dt):
      # continue here