"""============================================================================

  Shot

============================================================================"""
import pygame
import random 

from common import globals, common, animation
from game_objects import setting

class EnemyShot:
  def __init__(self, 
    rect, 
    sprite='enemy_shot.png', 
    boundary = False, 
    direction = 90, 
    speed = 1, 
    sound = False,
  ):

    self.sprite      = sprite
    self.rect       = pygame.Rect(rect)
    self.speed      = speed
    self.direction  = direction
    if boundary:
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.delete      = False

  def draw(self):
    globals.game.window.blit(self.sprite.get_surface(), self.rect)

  def update(self):
    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  

    if common.rect_touch(self.rect, self.boundary):
      self.delete = True

  def hit(self, object_type):
    if object_type == 'player' or object_type == 'shot' or object_type == 'city':
      self.delete = True
