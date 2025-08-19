from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 10)

  def update(self, dt):
    forward = pygame.Vector2(0, 1)
    self.position += self.velocity * dt