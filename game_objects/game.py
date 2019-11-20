"""============================================================================

  The basics of the program, is that eash object that is active
      - paint it self on the shadow screen
      - move it self
      - does something when coliding with other objects

  The main loop makes sure alle active objets paint, move and hit functions is 
    called, at the appropriate time, player input is acted upon, and that the 
    shadow screen is fliped at regular intervals.

  Game frame by Simon Rigét @ paragi 2019. License MIT

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
from game_objects import enemy_shot
from game_objects import player
from game_objects import player_input
from game_objects import shot
from game_objects import story
from game_objects import tech_screen
from game_objects import setting
from game_objects import globals
from game_objects import next_level
from game_objects import end_game



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
      enemy_shot = enemy_shot.EnemyShot,
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
        "Error in story board, when creating",
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
    self.tech_screen = tech_screen.TechScreen()
    self.level = 1
    self.score = 0
    self.end_game = False    
    self.level_time = 0
    self.frame_start = 0

    if( setting.game_speed < 100 or setting.game_speed > 0 ):
      self.game_speed = setting.game_speed
    else:
      self.game_speed = 1
    
  def __del__(self):
    pygame.display.quit()
    pygame.quit()

  # This is the main game loop
  def loop(self):
    # Start using pygame loop timing (Frame rate)
    self.clock = pygame.time.Clock()

    while not self.player_input.stop:
      self.frame_start = pygame.time.get_ticks()
  
      # Get player input
      self.player_input.update()

      # move all objects
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'update', None)):
          game_obj['obj'].update()

      if not self.end_game:
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
        count = {'alien': 0, 'player': 0, 'city':0}
        for game_obj in self.object.list:
          if callable(getattr(game_obj['obj'], 'draw', None)):
            game_obj['obj'].draw()

          # Remove dead objects  
          if getattr(game_obj['obj'], 'dead', False):
            # print(game_obj['type'],"died")
            self.object.list.remove(game_obj)

          # Count some objects
          if game_obj['type'] in count:
            count[game_obj['type']] += 1

        globals.game.dashboard.draw()
        
        if self.player_input.tech_screen_on:
          self.tech_screen.draw()

        if count['alien'] <= 0:
          next_level.NextLevel()

        if count['player'] <= 0 or count['city'] <= 0:
          self.end_game = True
          end_game.EndGame()

      pygame.display.flip()

      # Calculate timing and wait until frame rate is right
      self.clock.tick( setting.frame_rate * globals.game.game_speed )


    
