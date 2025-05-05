import pygame
import constants
import circleshape


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    # move in a line       
    def update(self,dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        

       
