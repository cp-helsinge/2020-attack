"""============================================================================

  Shot

============================================================================"""

class Shot:
    def __init__(self, rect, x_speed, y_speed):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y