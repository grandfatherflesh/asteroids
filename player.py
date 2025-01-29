from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    #Sprite's actual shape
    def __init__(self, x, y):
            super().__init__(x, y, PLAYER_RADIUS)
            self.x = x
            self.y = y
            self.rotation = 0
    #Sprite's skin
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    #Render player's sprite
    def draw(self, screen):
         pygame.draw.polygon(screen, "white", self.triangle() , width = 2)
    #Rotate sprite
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    #Updates sprite according to the buttons pressed
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
             self.move(dt)
        if keys[pygame.K_s]:
             self.move(-dt)
    def shoot(self): 
         print("Shooting!")
         bullet = Shot(self.position.x, self.position.y)
         bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
         return bullet