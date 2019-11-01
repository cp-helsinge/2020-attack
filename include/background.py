"""============================================================================

  Background

============================================================================"""
import pygame
from include import globals

class Background:
  def __init__(self, color = (0,0,0)):
    self.color = color

  def paint(self):
    globals.game.window.fill( self.color )
    
