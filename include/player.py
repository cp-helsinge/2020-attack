"""============================================================================

  Player


  parameters:
    rect      : Start position and size 
    image     : Image
    boundery  : boundary of movement
    speed     : 2
    direction : in degrees 0-359 counting counter clockwise and 0 = right
    axix      : x, y or xy
    
============================================================================"""
import pygame
from include import globals
from include import common

class Player:
  def __init__(self, 
    rect, 
    image='player.png', 
    crosshair_image='crosshair.png', 
    boundary = globals.game.rect, 
    direction = 0, 
    speed = 1, 
    axix = 'x',
    sound = False,
    hit_sound = False):
    
    # load image, convert alpha channel (transparrent areas) and resize image
    self.image       = common.load_image(image, rect )
    self.crosshair_image    = common.load_image("crosshair.png")
    self.rect       = rect 
    self.boundary   = boundary 
    self.speed      = speed
    self.direction  = direction
    self.axix       = axix
    self.dead       = False

 def draw(self, surface = globals.game.window ):
    surface.blit(self.image,self.rect)

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