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
    self.class_list = dict(
      alien = alien.Alien,
      bomb = bomb.Bomb,
      background = background.Background,
      city = city.City,
      player = player.Player,
      shot = shot.Shot,
    )

  def add(self, object_type, parameters):  
    try:
      self.list.append( {
          'type' : object_type,
          'obj'  : self.class_list[object_type]( **parameters) 
        }
      )
    except Exception as err:
      print(
        "Error in storry board, when creating",
        object_type,
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
    self.end_game = False    
    self.level_time = 0

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

    if self.level < len(storry.board):
      self.object.list = []
      for obj in storry.board[self.level]:
        for object_type, parameters in obj.items():
          self.object.add(object_type, parameters)

      self.level_time = pygame.time.get_ticks() 
    else:
      self.end_game = True      

  # This is the main game loop
  def loop(self):
    # Start using pygame loop timing (Frame rate)
    clock = pygame.time.Clock()

    while not self.player_input.stop and not self.end_game:
      # Get player input
      self.player_input.update()

      # move all objects
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'update', None)):
          game_obj['obj'].update()

      # Check for collissions with all non dead objects, that has a defined rectangle
      for i in range(0, len(self.object.list) ):
        if not self.object.list[i]['type'] == 'background' and not getattr( self.object.list[i]['obj'], 'dead', False) and getattr(self.object.list[i]['obj'], 'rect', False):
          for ii in range(i+1, len(self.object.list) ):
            if not getattr( self.object.list[ii]['obj'], 'dead', False) and getattr(self.object.list[ii]['obj'], 'rect', False) and self.object.list[i]['obj'].rect.colliderect(self.object.list[ii]['obj'].rect):
              # print(i,"hitting",ii)
              if getattr(self.object.list[i]['obj'], 'hit', False):
                self.object.list[i]['obj'].hit(self.object.list[ii]['type'])
              if getattr(self.object.list[ii]['obj'], 'hit', False):
                self.object.list[ii]['obj'].hit(self.object.list[i]['type'])
      
      # Paint all objects and cleanm up
      aliens = 0
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'draw', None)):
          game_obj['obj'].draw()

        # Remove dead objects  
        if getattr(game_obj['obj'], 'dead', False):
          # print(game_obj['type'],"died")
          self.object.list.remove(game_obj)

        # Count aliens
        if game_obj['type'] == 'alien':
          aliens += 1

      globals.game.dashboard.draw()

      pygame.display.flip()

      if aliens <= 0:
        self.next_level()

      # Calculate timing and wait until frame rate is right
      clock.tick( setting.frame_rate * globals.game.game_speed )


    
