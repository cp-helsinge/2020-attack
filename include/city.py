"""============================================================================

  City

============================================================================"""
import pygame

class City:
  def __init__(self):
    self.cityImage = pygame.image.load("gfx/grey_city.png").convert_alpha()

  def set_rect(self, rect):
    self.rect = rect