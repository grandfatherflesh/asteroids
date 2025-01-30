from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        print(f"Splitting asteroid with radius: {self.radius}, position: {self.position}")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Asteroid radius is too small to split. Exiting split method.")
            return
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2