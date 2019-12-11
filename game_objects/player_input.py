"""============================================================================

  Palyer input

  Register user input according to key binding



============================================================================"""
import pygame
from pygame import *
from game_objects import globals
from game_objects import setting

class PlayerInput:
  def __init__(self):
    self.tech_screen_on = False
    self.reset()

  def reset(self):
    self.key = {}
    for event, key in setting.key_bind.items():
      self.key[key] = False
    for event, key in setting.mouse_bind.items():
      self.key[key] = False
    self.mouse = ( 0,0 )
    self.stop = False
    self.suspend = False

   
  def update(self):
    event_list = pygame.event.get()
    for event in event_list:
      if event.type == pygame.QUIT:
        self.stop = True

      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
        #self.suspend = not self.suspend
        self.stop = True

      if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:  
        self.tech_screen_on = not self.tech_screen_on

      if not self.suspend:
        if event.type == pygame.MOUSEMOTION :
          self.mouse = event.pos

        if event.type == pygame.KEYDOWN and event.key in setting.key_bind:
          self.key[setting.key_bind[event.key]] = True
        elif event.type == pygame.KEYUP and event.key in setting.key_bind:
          self.key[setting.key_bind[event.key]] = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button in setting.mouse_bind:
          self.key[setting.mouse_bind[event.button]] = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button in setting.mouse_bind:
          self.key[setting.mouse_bind[event.button]] = False

