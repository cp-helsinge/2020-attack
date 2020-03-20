"""============================================================================

  Palyer input

  Register user input according to key binding



============================================================================"""
import pygame
from pygame import *

MOUSE_LEFT  = 1 
MOUSE_WHEEL = 2
MOUSE_RIGHT = 3

key_bind =  {
  pygame.K_a      : 'left',  # A
  pygame.K_LEFT   : 'left',
  pygame.K_d      : 'right', # D  
  pygame.K_RIGHT  : 'right',
  pygame.K_w      : 'up',    # A
  pygame.K_UP     : 'up',
  pygame.K_s      : 'down',  # D
  pygame.K_DOWN   : 'down',
  pygame.K_SPACE  : 'fire',
  pygame.K_RETURN : 'fire',
  
}
mouse_bind = {
  MOUSE_LEFT : 'fire',  
  MOUSE_RIGHT : 'fire',
}

fire_rate = 3


class PlayerInput:
  def __init__(self, game_state):
    self.game_state = game_state
    self.game_state.tech_screen_on = False
    self.reset()

  def reset(self):
    self.game_state.key = {}
    for event, key in key_bind.items():
      self.game_state.key[key] = False
    for event, key in mouse_bind.items():
      self.game_state.key[key] = False
    self.game_state.mouse = ( 0,0 )
    self.game_state.stop = False
    self.game_state.suspend = False

   
  def update(self):
    event_list = pygame.event.get()
    for event in event_list:
      if event.type == pygame.QUIT:
        self.game_state.stop = True

      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
        #self.suspend = not self.suspend
        self.game_state.stop = True

      if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:  
        self.game_state.tech_screen_on = not self.game_state.tech_screen_on

      if not self.game_state.suspend:
        if event.type == pygame.MOUSEMOTION :
          self.game_state.mouse = event.pos

        if event.type == pygame.KEYDOWN and event.key in key_bind:
          self.game_state.key[key_bind[event.key]] = True
        elif event.type == pygame.KEYUP and event.key in key_bind:
          self.game_state.key[key_bind[event.key]] = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button in mouse_bind:
          self.game_state.key[mouse_bind[event.button]] = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button in mouse_bind:
          self.game_state.key[mouse_bind[event.button]] = False

