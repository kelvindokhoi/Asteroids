# main.py

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    all_shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    Shot.containers = (all_shots,updatables,drawables)
    AsteroidField.containers = (updatables,)
    Asteroid.containers = (all_asteroids, updatables, drawables)
    Player.containers = (updatables,drawables)

    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        for asteroid in all_asteroids:
            if asteroid.collision_check(player1):
                print("Game over!")
                exit()
            for a_shot in all_shots:
                if asteroid.collision_check(a_shot):
                    a_shot.kill()
                    # asteroid.kill()
                    asteroid.split()
                    # if asteroid.radius > ASTEROID_MIN_RADIUS:
                    #     new_asteroid_angle = random.uniform(20,50)
                    #     new_vector_1 = asteroid.velocity.rotate(-new_asteroid_angle)
                    #     new_vector_2 = asteroid.velocity.rotate(new_asteroid_angle)
                    #     new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
                    #     new_asteroid_1 = Asteroid(*asteroid.position,new_radius)
                    #     new_asteroid_2 = Asteroid(*asteroid.position,new_radius)
                    #     new_asteroid_1.velocity = new_vector_1*1.2
                    #     new_asteroid_2.velocity = new_vector_2*1.2
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()