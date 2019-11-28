"""============================================================================

  Shot

============================================================================"""
import pygame
import random 
from game_objects import globals
from game_objects import setting
from game_objects import common


class EnemyShot:
  def __init__(self, 
    rect, 
    image='enemy_shot.png', 
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
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.delete      = False

  def draw(self):
    globals.game.window.blit(self.image,self.rect)

  def update(self):
    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  

    if common.rect_touch(self.rect, self.boundary):
      self.delete = True

  def hit(self, object_type):
    if object_type == 'player':
      self.delete = True
