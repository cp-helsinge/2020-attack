"""============================================================================

  Shot

============================================================================"""
import pygame
import random 
from game_objects import globals
from game_objects import setting
from game_objects import common
from game_objects import animation

class Shot:
  def __init__(self, 
    rect, 
    sprite='shot.png', 
    boundary = False, 
    direction = 90, 
    speed = 1, 
    sound = False,
  ):

    self.sprite     = sprite
    self.sound      = sound
    if self.sound:
      self.sound.play()
    self.rect       = pygame.Rect(rect)
    self.speed      = speed
    self.direction  = direction
    if boundary:
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.delete       = False

  def draw(self):
    globals.game.window.blit(self.sprite.get_surface(),self.rect)

  def update(self):
    self.rect = common.move_rect(self.rect, self.direction , self.speed, self.boundary)  

    if common.rect_touch(self.rect, self.boundary):
      self.delete = True

  def hit(self, object_type):
    self.delete = True
