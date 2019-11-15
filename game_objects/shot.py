"""============================================================================

  Shot

============================================================================"""
import pygame
import random 
from game_objects import globals
from game_objects import setting
from game_objects import common


class Shot:
  def __init__(self, 
    rect, 
    image='shot.png', 
    boundary = False, 
    direction = 90, 
    speed = 1, 
    sound = False,
  ):

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
    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  
    if self.rect.y <= self.boundary.y:
      self.dead = True
      pass

  def hit(self, object_type):
    self.dead = True
