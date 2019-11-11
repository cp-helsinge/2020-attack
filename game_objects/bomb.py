"""============================================================================

  Bomb (Alien)

============================================================================"""

class Bomb:
    def __init__(self, pos, x_speed, y_speed):
        self.enemyBomb = pygame.image.load("gfx/enemy_bomb.png").convert_alpha()
        self.rect = self.enemyBomb.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
