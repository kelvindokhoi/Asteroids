# asteroid.py

from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_asteroid_angle = random.uniform(20,50)
            new_vector_1 = self.velocity.rotate(-new_asteroid_angle)
            new_vector_2 = self.velocity.rotate(new_asteroid_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(*self.position,new_radius)
            new_asteroid_2 = Asteroid(*self.position,new_radius)
            new_asteroid_1.velocity = new_vector_1*1.2
            new_asteroid_2.velocity = new_vector_2*1.2