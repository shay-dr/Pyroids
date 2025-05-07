# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import constants
import player
import asteroid
import asteroidfield
import shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}") 
    print(f"Screen height: {constants.SCREEN_HEIGHT}") 
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    #group config
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #group association
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    shot.Shot.containers = (shots, updatable, drawable)

    #create player(s)
    p1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #create asteroids field
    af = asteroidfield.AsteroidField()

    #create future items (asteroids, bullets, etc...)

    while True:
        for event in pygame.event.get():
            
            # event handling code:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        dt =  clock.tick(fps) / 1000
        
        #update game state using dt
        updatable.update(dt)
        
        # draw screen and player
        screen.fill("black")
        
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        
        for asteroid_obj in asteroids:
            if asteroid_obj.collide(p1):
                print("Game over!")
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()