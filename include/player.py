"""============================================================================

  Player

============================================================================"""
import pygame
from include import globals
from include import common

class Player:
  def __init__(self, position, boundry, direction = 0, speed = 1):
    # load image, convert alpha channel (transparrent areas) and resize image
    self.player_image       = common.load_image("player.png", position )
    self.player_shot_image  = common.load_image("shot.png")
    self.crosshair_image    = common.load_image("crosshair.png")
    self.position = position # Rectangle
    self.boundry  = boundry  # Rectangle
    self.speed    = speed
    self.dead     = False

  def paint(self):
    globals.game.window.blit(self.player_image,self.position)

"""
class Player:
  def __init__(self, position):
    self.playerImage = pygame.image.load(globals.gfx_path + "player.png").convert_alpha()
    self.playerShotImage = pygame.image.load(globals.gfx_path + "shot.png").convert_alpha()
    self.crosshairImage = pygame.image.load(globals.gfx_path + "crosshair.png").convert_alpha()
    self.position = position
    self.rect = self.playerImage.get_rect(bottomleft=(position))
    self.alive = True 
    self.shots = []
    self.player_has_fired = False

  def move(self):
    if globals.game.player_input.left and self.rect.left > window.get_rect().left:
        self.rect.x = self.rect.x - 2
    if globals.game.player_input.right and self.rect.right < window.get_rect().right:
        self.rect.x = self.rect.x + 2

    for shot in list(self.shots):
        shot.move()
        if not shot.rect.colliderect(window.get_rect()):
            self.shots.remove(shot)

    if not globals.game.player_input.fire:
        self.player_has_fired = False

  def hit(self):
    self.alive = False

  def pain(self):
    globals.game.window.blit(self.playerImage, self.position)
"""