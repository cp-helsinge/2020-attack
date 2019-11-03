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

# Import game classes
from include import alien
from include import bomb
from include import background
from include import city
from include import common
from include import dashboard
from include import player
from include import player_input
from include import setting
from include import shot
from include import globals
import storry

# Link a game object type to the actual object class definition
game_object_type = dict(
  alien = alien.Alien,
  bomb = bomb.Bomb,
  background = background.Background,
  city = city.City,
  player = player.Player,
  shot = shot.Shot,
)

class Game:
  def __init__(self):
    globals.game = self
    globals.sessing = setting
    pygame.init()
    self.window = pygame.display.set_mode(
      (
        setting.screen_width,
        setting.screen_height
      ) , pygame.SCALED | pygame.RESIZABLE
       #, FULLSCREEN
    )
    pygame.display.set_caption('Alien Attack')
    pygame.mouse.set_visible(False)

    # Game objects
    self.dashboard = dashboard.Dashboard()
    self.rect = pygame.Rect(0,0,setting.screen_width,setting.screen_height) - dashboard.rect
    self.game_objects = []
    self.player_input = player_input.PlayerInput()
    self.level = 1
    self.score = 10000
    self.player_health = 100

    if( setting.game_speed < 100 or setting.game_speed > 0 ):
      self.game_speed = setting.game_speed
    else:
      self.game_speed = 1
    
    self.next_level(1)
  
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
        try:
          self.game_objects.append( {
              'type' : obj_type,
              'obj'  : game_object_type[obj_type](**parameters) 
            }
          )
        except Exception as err:
          print(
            "Error in storry board, when creating",
            obj_type,
            ":",err,
            parameters
          ) 
          self.__del__()
          sys.exit(1)

  # This is the main game loop
  def loop(self):
    # Start using pygame loop timing (Frame rate)
    clock = pygame.time.Clock()

    while not self.player_input.stop:
      # Get player input
      self.player_input.update()

      # move all objects
      #for category in game.all_objects:
       # for obj in self.all_objects[category]:
        #  if callable(getattr(obj, 'move', None)):
         #   print("moving ",category)
          #  obj.move()

      # claculate collissions
      #    if getattr(obj, 'dead', False) and obj.dead :
      #      game.all_objects[category].remove(obj)
      # paint background

      # Paint all objects
      for game_obj in self.game_objects:
        print("game_obj",game_obj)
        if callable(getattr(game_obj['obj'], 'draw', None)):
          print("Drawing",game_obj['type'])
          game_obj['obj'].paint()

      game.dashboard.draw()

      pygame.display.flip()

      # Calculate timing and wait until frame rate is right
      clock.tick( setting.frame_rate * game.game_speed )
      
# Start a new game
globals.gfx_path = os.path.join(os.path.dirname(__file__), "gfx", "")
game = Game()
game.loop()
del game

