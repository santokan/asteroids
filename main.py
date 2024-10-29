from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                pygame.quit()

        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
