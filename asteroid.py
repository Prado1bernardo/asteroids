import pygame
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x:float,y:float,radius:float) -> None:
        super().__init__(x, y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:

            a = random.uniform(20,50)
            vect1 = self.velocity.rotate(a)
            vect1 *= 1.2
            log_event("asteroid_split")
            b = a * -1
            vect2 = self.velocity.rotate(b)
            vect2 *= 1.2
            old_radius = self.radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = vect1
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity = vect2
