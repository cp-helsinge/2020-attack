"""============================================================================

  Palyer input

  Register user input according to key binding



============================================================================"""
import pygame
from pygame import *
import pprint

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
  def __init__(self):
    self.reset()

  # Reset all player input states 
  def reset_player_input(self):
    pygame.event.get()
    self.key = {}
    for event, key in key_bind.items():
      self.key[key] = False
    for event, key in mouse_bind.items():
      self.key[key] = False
    self.mouse = ( 0,0 )
    self.stop = False
    self.tech_screen_on = False

  # read player input and set states   
  def update_player_input(self):
    # Get list of events
    event_list = pygame.event.get()
    for event in event_list:
       # == First check for some system events ==
      # Pres X to close window
      if event.type == pygame.QUIT:
        self.stop = True

      # Esc to exit
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
        #self.suspend = not self.suspend
        self.stop = True

      # Resize window
      elif event.type == pygame.VIDEORESIZE:
        self.resize(event.dict['size'])

      # F3 tech screen
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_F3:  
        self.tech_screen_on = not self.tech_screen_on

      # Full screen toggle
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:  
        self.toggle_fullscreen()

      else:
        # Other keys, while pressed 
        if event.type == pygame.KEYDOWN and event.key in key_bind:
          self.key[key_bind[event.key]] = True
        elif event.type == pygame.KEYUP and event.key in key_bind:
          self.key[key_bind[event.key]] = False

        # Mouse buttons while pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in mouse_bind:
          self.key[mouse_bind[event.button]] = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button in mouse_bind:
          self.key[mouse_bind[event.button]] = False

        # Save mouse positon
        if event.type == pygame.MOUSEMOTION :
          self.mouse = event.pos

