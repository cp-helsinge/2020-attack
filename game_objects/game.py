#! /usr/bin/env python3
"""============================================================================
Sideways arcade space game

Main

The basics of the program, is that eash object that is active
    - paint it self on the shadow screen
    - move it self
    - does something when coliding with other objects

The main loop makes sure alle active objets paint, move and hit functions is called, at the appropriate time, player input is acted upon, and that the shadow screen is fliped at regular intervals

Game engine by Simon Rigét @ paragi. License MIT

============================================================================"""
# Import python modules
import pygame
from pygame.locals import *
import time
import os
import sys
import traceback

# Import game classes
from game_objects import alien
from game_objects import bomb
from game_objects import background
from game_objects import city
from game_objects import common
from game_objects import dashboard
from game_objects import player
from game_objects import player_input
from game_objects import shot
from game_objects import storry
from game_objects import setting
from game_objects import globals



class GameObject():
  def __init__(self):
    self.list = []
    # Link a game object type to the actual object class definition
    self.object_type = dict(
      alien = alien.Alien,
      bomb = bomb.Bomb,
      background = background.Background,
      city = city.City,
      player = player.Player,
      shot = shot.Shot,
    )

  def add(self, obj_type, parameters):  
    try:
      self.list.append( {
          'type' : obj_type,
          'obj'  : self.object_type[obj_type]( **parameters) 
        }
      )
    except Exception as err:
      print(
        "Error in storry board, when creating",
        obj_type,
        ":",err,
        parameters
      ) 
      #traceback.print_stack()
      #self.__del__()
      sys.exit(1)  



class Game:
  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode(
      (
        setting.screen_width,
        setting.screen_height
      ) 
       #, RESIZABLE | SCALED | FULLSCREEN
    )
    pygame.display.set_caption('Alien Attack')
    pygame.mouse.set_visible(False)

    # Game objects
    self.dashboard = dashboard.Dashboard()
    self.rect = pygame.Rect(0,0,setting.screen_width,setting.screen_height - self.dashboard.rect[3]) 
    self.object = GameObject()
    self.player_input = player_input.PlayerInput()
    self.level = 1
    self.score = 10000
    self.player_health = 100

    if( setting.game_speed < 100 or setting.game_speed > 0 ):
      self.game_speed = setting.game_speed
    else:
      self.game_speed = 1
    
  def __del__(self):
    pygame.display.quit()
    pygame.quit()

  def next_level(self, level = False):
    if( level ):
      self.level = level
    else:
      self.level += 1

    for obj in storry.board[self.level]:
      for obj_type, parameters in obj.items():
        self.object.add(obj_type, parameters)

  # This is the main game loop
  def loop(self):
    # Start using pygame loop timing (Frame rate)
    clock = pygame.time.Clock()

    while not self.player_input.stop:
      # Get player input
      self.player_input.update()

      # move all objects
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'update', None)):
          game_obj['obj'].update()

      # Check for collissions
      #    if getattr(obj, 'dead', False) and obj.dead :
      #      game.all_objects[category].remove(obj)
      for i in range(0, len(self.object.list) ):
        if not getattr( self.object.list[i], 'dead', False) and getattr(self.object.list[i], 'rect', False):
          for ii in range(i, len(self.object.list) ):
            if not getattr( self.object.list[ii], 'dead', False) and getattr(self.object.list[ii], 'rect', False) and self.object.list[i].rect.colliderect(self.object.list[ii].rect):
              if getattr(self.object.list[i], 'hit', False):
                self.object.list[i].hit(self.object.list[ii].type)
              if getattr(self.object.list[ii], 'hit', False):
                self.object.list[ii].hit(self.object.list[i].type)

      # Paint all objects
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'draw', None)):
          game_obj['obj'].draw()

        # Remove dead objects  
        if getattr(game_obj['obj'], 'dead', False):
          self.object.list.remove(game_obj)

      globals.game.dashboard.draw()

      pygame.display.flip()

      # Calculate timing and wait until frame rate is right
      clock.tick( setting.frame_rate * globals.game.game_speed )
  
    
