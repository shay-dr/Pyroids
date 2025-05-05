# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player
import asteroid
import asteroidfield


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

    #group association
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)

    #create player(s)
    p1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #create asteroids field
    af = asteroidfield.AsteroidField()

    #create future items (asteroids, bullets, etc...)

    while True:
        for event in pygame.event.get():
            
            # event handling code:
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


        dt =  clock.tick(fps) / 1000
        
        #update game state using dt
        updatable.update(dt)
        
        # draw screen and player
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()