# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}") 
    print(f"Screen height: {constants.SCREEN_HEIGHT}") 
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    while True:
        for event in pygame.event.get():
            
            # event handling code:
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # game logic and drawing
        screen.fill("black")
        pygame.display.flip()

        dt =  clock.tick(fps) / 1000

if __name__ == "__main__":
    main()