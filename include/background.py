"""============================================================================

  Background

============================================================================"""
import pygame
from include import globals
from include import setting
from include import common


class Background:
  def __init__(self, color = (0,0,0), image = False ):
    self.color = False
    if image:
      self.image = common.load_image(image, setting.screen_rect)
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

