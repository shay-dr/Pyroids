import pygame
import constants
import circleshape


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)


    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    # move in a line       
    def update(self,dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        

       
