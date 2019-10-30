"""============================================================================

  Player

============================================================================"""
import pygame

class Player:
    def __init__(self, position):
        self.playerImage = pygame.image.load("gfx/player.png").convert_alpha()
        self.playerShotImage = pygame.image.load("gfx/shot.png").convert_alpha()
        self.crosshairImage = pygame.image.load("gfx/crosshair.png").convert_alpha()
        self.rect = self.playerImage.get_rect(bottomleft=(position))
        self.alive = True 
        self.shots = []
        self.player_has_fired = False

    def move(self, player_input):
        if player_input.left and self.rect.left > window.get_rect().left:
            self.rect.x = self.rect.x - 2
        if player_input.right and self.rect.right < window.get_rect().right:
            self.rect.x = self.rect.x + 2

        for shot in list(self.shots):
            shot.move()
            if not shot.rect.colliderect(window.get_rect()):
                self.shots.remove(shot)

        if not player_input.fire:
            self.player_has_fired = False

    def hit(self):
        self.alive = False