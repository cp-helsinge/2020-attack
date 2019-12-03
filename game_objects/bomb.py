"""============================================================================

  Bomb (Alien)

============================================================================"""
import pygame
import random 
from game_objects import globals
from game_objects import setting
from game_objects import common


class Bomb:
  def __init__(self, 
    rect, 
    image='bomb.png', 
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
    self.delete     = False

  def draw(self):
    globals.game.window.blit(self.image,self.rect)

  def update(self):
    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  
    if self.rect.y + self.rect.height >= self.boundary.height:
      self.delete = True

  def hit(self, object_type):
    if not object_type == 'alien' and not object_type == 'bomb' and not object_type == 'enemy_shot':
      self.delete = True
      globals.game.score += 10