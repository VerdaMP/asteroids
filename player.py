import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

# Player object class


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def rotate(self, direction):
        self.rotation += direction * PLAYER_TURN_SPEED

    def move(self, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED

    def shoot(self):
        if (self.shoot_timer <= 0):
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(
                self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shoot_timer = self.shoot_timer - dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1)
        if keys[pygame.K_d]:
            self.rotate(1)
        if keys[pygame.K_w]:
            self.move(1)
        if keys[pygame.K_s]:
            self.move(-1)
        if keys[pygame.K_SPACE]:
            self.shoot()