"""============================================================================

  Alien space ship

  parameters:
    rect      : Start position and size 
    image     : Image
    boundery  : boundary of movement
    speed     : 2
    direction : in degrees 0-359 counting counter clockwise and 0 = right
    axix      : x, y or xy

============================================================================"""
import pygame
import random 
from game_objects import globals
from game_objects import setting
from game_objects import common


class Alien:
  def __init__(self, 
    rect, 
    image='player.png', 
    crosshair_image='crosshair.png', 
    boundary = False, 
    direction = 0, 
    speed = 1, 
    sound = False,
    shoot_sound = False):

    self.image      = common.load_image(image, rect )
    self.rect       = pygame.Rect(rect)
    self.speed      = speed
    self.direction  = direction
    if boundary:
      self.boundary   = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.dead       = False

  def draw(self):
    globals.game.window.blit(self.image,self.rect)

  def update(self):
    if self.rect.left <= self.boundary.left:
      self.direction = 0
    elif self.rect.right >= self.boundary.right:
      self.direction = 180

    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  

  def hit(self, object_type):
    if object_type == 'shot':
      self.dead = True
      globals.game.score += 100
