# player.py
from circleshape import *
from constants import *
from shot import *
import random

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shooting_timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shooting_timer = max(0,self.shooting_timer-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self,screen):
        pygame.draw.polygon(screen,'white',self.triangle(),2)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if not(self.shooting_timer > 0):
            new_shot = Shot(*self.position)
            new_shot.velocity = pygame.Vector2((0,1)) * PLAYER_SHOOT_SPEED
            new_shot.velocity = new_shot.velocity.rotate(self.rotation)
            self.shooting_timer = PLAYER_SHOOT_COOLDOWN