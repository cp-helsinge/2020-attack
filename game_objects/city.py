"""============================================================================

  City

============================================================================"""
import pygame
from game_objects import globals
from game_objects import common


class City:
  def __init__(self, rect, image = 'city.png', sound = ''):
    self.image = common.load_image(image, rect)
    self.rect = pygame.Rect(rect)

  def draw(self, surface = False ):
    if( not surface ):
      surface = globals.game.window
    surface.blit(self.image,self.rect)

  def hit(self, object_type):
    if object_type == 'bomb':
      self.dead = True
      globals.game.score -= 100