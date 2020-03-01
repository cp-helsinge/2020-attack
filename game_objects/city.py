"""============================================================================

  City

============================================================================"""
import pygame
from common import globals, common, animation

class City:
  def __init__(self, rect, sprite = 'city.png', sound = False):
    self.sprite = sprite
    self.rect = pygame.Rect(rect)
    self.sound = sound
    self.delete = False

  def draw(self, surface = False ):
    if( not surface ):
      surface = globals.game.window
    surface.blit(self.sprite.get_surface(), self.rect)

  def hit(self, object_type):
    if object_type == 'bomb':
      if self.sound:
        self.sound.play()
      self.delete = True
      globals.game.score -= 100