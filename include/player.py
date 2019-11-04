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
    boundary = False, 
    direction = 0, 
    speed = 1, 
    sound = False,
    shoot_sound = False):
    
    # load image, convert alpha channel (transparrent areas) and resize image
    self.image       = common.load_image(image, rect )
    self.crosshair_image    = common.load_image("crosshair.png")
    self.rect       = pygame.Rect(rect)
    self.boundary   = boundary 
    if not boundary:
      self.boundary = globals.game.rect
    self.speed      = speed
    self.dead       = False

  def draw(self):
    print("Player rect",self.rect)
    globals.game.window.blit(self.image,self.rect)

  def update(self):
    key = globals.game.player_input.key

    if key['left']:
      self.rect = common.move_rect(self.rect, 180, self.speed, self.boundary)
    if key['right']:
      self.rect = common.move_rect(self.rect, 0, self.speed, self.boundary)
    if key['up']:
      self.rect = common.move_rect(self.rect, 90, self.speed, self.boundary)
    if key['down']:
      self.rect = common.move_rect(self.rect, -90, self.speed, self.boundary)

