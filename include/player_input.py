"""============================================================================

  Palyer input

  Register user input according to key binding



============================================================================"""
import pygame
from pygame import *

class PlayerInput:
  def __init__(self):
    self.key_bind =  {
      pygame.K_a  : 'left',      # A
      pygame.K_d  : 'right',     # D
    }
    self.do = {}
    self.mouse = ( 0,0 )
    self.stop = False

  def update(self):
    events = pygame.event.get()
    for e in events:
      if e.type == pygame.QUIT:
        self.stop = True

      elif e.type == pygame.MOUSEMOTION :
        self.mouse = e.pos

      elif ( hasattr(e, 'key') and self.key_bind[e.key]) or ( hasattr(e, 'button') and self.key_bind[e.button]) :
        if e.type == pygame.KEYDOWN :
          self.do[self.key_bind[e.key]] = True
        elif e.type == pygame.KEYDOWN :
          self.do[self.key_bind[e.key]] = False

        elif e.type == pygame.MOUSEBUTTONDOWN : 
          self.do[self.key_bind[e.button]] = True
        elif e.type == pygame.MOUSEBUTTONUP :  
          self.do[self.key_bind[e.button]] = False


