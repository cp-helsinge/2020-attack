"""============================================================================

  Background

============================================================================"""
import pygame
from common import globals, common, animation
from game_objects import setting

class Background:
  def __init__(self, color = (0,0,0), sprite = False ):
    self.color = False
    if sprite:
      self.sprite = sprite
    else:
      self.color = color
    self.rect = globals.game.rect

  def draw(self):
    if(self.color):
      globals.game.window.fill( self.color )
    else:
      globals.game.window.blit(self.sprite.get_surface(),self.rect)

