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
from game_objects import animation
from game_objects import level_controle
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
    try:
      pygame.mixer.init()
    except:
      pass

    self.window = pygame.display.set_mode(
      (
        setting.screen_width,
        setting.screen_height
      ) 
       #, RESIZABLE | SCALED | FULLSCREEN
    )
    pygame.display.set_caption('Alien Attack')
    pygame.mouse.set_visible(False)

    self.dashboard = dashboard.Dashboard()
    self.rect = pygame.Rect(0,0,setting.screen_width,setting.screen_height - self.dashboard.rect[3]) 
    self.object = GameObject()
    self.player_input = player_input.PlayerInput()
    self.tech_screen = tech_screen.TechScreen()
    self.level = 1
    self.score = 0
    self.suspend = False    
    self.end_game = end_game.EndGame()   
    self.level_controle = level_controle.LevelControle()
    self.level_time = 0
    self.frame_start = 0

    if( setting.game_speed < 100 or setting.game_speed > 0 ):
      self.game_speed = setting.game_speed
    else:
      self.game_speed = 1
    
    # Start using pygame loop timing (Frame rate)
    self.clock = pygame.time.Clock()
    
  def __del__(self):
    pygame.display.quit()
    pygame.quit()

  # test is the game object is active and hitable
  def __obj_active(self, obj):
    return not getattr( obj, 'delete', False) and not getattr( obj, 'dead', False) and getattr(obj, 'rect', False) 


  # This is the main game loop
  def loop(self):
    while not self.player_input.stop:
      self.frame_start = pygame.time.get_ticks()
  
      # Get player input
      self.player_input.update()

      # move all objects
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'update', None)):
          game_obj['obj'].update()

      # change to self.collidable_object.list
      # Check for collissions with all objects, that has a defined rectangle. Execpt dead and deleted objects.
      for i in range(0, len(self.object.list) ):
        if not self.object.list[i]['type'] == 'background' and self.__obj_active(self.object.list[i]['obj']):
          for ii in range(i+1, len(self.object.list) ):
            if self.__obj_active(self.object.list[i]['obj']) and self.object.list[i]['obj'].rect.colliderect(self.object.list[ii]['obj'].rect):
              # print(i,"hitting",ii)
              if getattr(self.object.list[i]['obj'], 'hit', False):
                self.object.list[i]['obj'].hit(self.object.list[ii]['type'])
              if getattr(self.object.list[ii]['obj'], 'hit', False):
                self.object.list[ii]['obj'].hit(self.object.list[i]['type'])
      
      # Paint collidable ojects and clean up
      count = {'alien': 0, 'player': 0, 'city':0}
      for game_obj in self.object.list:
        if callable(getattr(game_obj['obj'], 'draw', None)):
          game_obj['obj'].draw()

        # Remove objects marked for deletion
        if getattr(game_obj['obj'], 'delete', False):
          self.object.list.remove(game_obj)

        # Count some objects
        if game_obj['type'] in count:
          count[game_obj['type']] += 1

      # Paint inactive objects
      # for game_obj in self.inactive_object.list:
      #   if callable(getattr(game_obj['obj'], 'draw', None)):
      #     game_obj['obj'].draw()


      self.dashboard.draw()
      
      if self.player_input.tech_screen_on:
        self.tech_screen.draw()

      if count['alien'] <= 0:
        self.level_controle.next()

      if count['player'] <= 0 or count['city'] <= 0:
        self.end_game.set()
        self.player_input.stop = True

      pygame.display.flip()

      # Calculate timing and wait until frame rate is right
      self.clock.tick( setting.frame_rate * self.game_speed )


    
 