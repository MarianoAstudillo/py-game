from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    forward = pygame.Vector2(0, 1)
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)

    v1 = self.velocity.rotate(random_angle)
    v2 = self.velocity.rotate(-random_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS

    new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
    new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

    new_asteroid_1.velocity = v1 * 1.2;
    new_asteroid_2.velocity = v2 * 1.2;