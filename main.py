def main():
    import pygame
    from constants import SCREEN_WIDTH
    from constants import SCREEN_HEIGHT
    from logger import log_state
    from logger import log_event
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    from shot import Shot
    import sys

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroidfield = AsteroidField()
    #shot = Shot(x,y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for i in drawable:
            i.draw(screen)

        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player) == True:
                log_event("player_hit")
                print("game over!")
                sys.exit()

        for i in asteroids:
            for shot in shots:
                if shot.collides_with(i) == True:
                    log_event("asteroid_split")
                    i.split()



        pygame.display.flip()

if __name__ == "__main__":
    main()
