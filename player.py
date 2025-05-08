import pygame
import constants
import circleshape
import shot


class Player(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 180
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        
    def update(self,dt):
        if self.timer > 0:
            self.timer -= dt
        
        keys = pygame.key.get_pressed()
        

        #rotate Left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        #rotate right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
                #rotate Left

        #move forwared        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        #move backward
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        
        #shoot weapon
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    
    def shoot(self):
        # creates a new shot at the player's postion
        if self.timer <= 0:
            
            new_shot = shot.Shot(self.position.x, self.position.y)

            shot_velocity = pygame.Vector2(0,1)
            shot_velocity.rotate_ip(self.rotation)
            new_shot.velocity = shot_velocity * constants.PLAYER_SHOOT_SPEED
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
        




