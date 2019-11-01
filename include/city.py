"""============================================================================

  City

============================================================================"""
import pygame
from include import globals
from include import common


class City:
  def __init__(self, rect):
    self.city_image = common.load_image("grey_city.png",rect)
    self.rect = rect

  def paint(self):
    globals.game.window.blit(self.city_image,self.rect)