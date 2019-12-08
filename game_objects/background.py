"""============================================================================

  Background

============================================================================"""
import pygame
from game_objects import common
from game_objects import setting
from game_objects import globals


class Background:
  def __init__(self, color = (0,0,0), image = False ):
    self.color = False
    if image:
      self.image = image
    else:
      self.color = color
    self.rect = globals.game.rect

  def draw(self, surface = False ):
    if( not surface ):
      surface = globals.game.window

    if(self.color):
      surface.fill( self.color )
    else:
      surface.blit(self.image,self.rect)

