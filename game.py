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
import glob

import config

# Import game classes
#from common import globals, common, animation, dashboard, player_input, level_controle, end_game, tech_screen
from game_functions import dashboard, player_input, level_controle, end_game, tech_screen
# from game_attributes import background, frame

game_name = 'Alien Attack'
screen_width = 1000
screen_height = 700
frame_rate = 60
game_speed = 1
game_objects_from = 'game_objects' # Used to import game objects dynamically as the from part

# Here is stores, the current state of the game 
class GameState:
  def __init__(self):
    self.reset()

  def reset(self):
    self.level = 1
    self.score = 0
    self.player_health = 100
    self.suspend = False
    self.frame_start = 0
    self.level_time = 0
    self.screen_width = config.screen_width
    self.screen_height = config.screen_height
    self.frame_rate = frame_rate
    self.game_speed = game_speed



class GameObject:
  def __init__(self):
    # List og game object for current level
    self.list = []

    # Make list of game objects
    self.class_list = {}
    for file in glob.glob(os.path.join(config.game_obj_path,"*.py")):
      # Extract the file name, without extension and in lower case 
      name = os.path.splitext(os.path.basename(file))[0].capitalize()
      
      # Ignore private and protected files
      if name.startswith("_"): continue

      # Import classes      
      if not name in self.class_list:
        print("loading class",name)
        # from <game_objects_from> import <name>
        cls = __import__(game_objects_from, None, None, [name.lower()], 0)
        # class = <name>.<Name>
        self.class_list[name] = getattr( getattr(cls,name.lower()),name )

        #except Exception as err:
        #  print("Unable to load game object in", name + ".py", err)
      print("Loaded classes",self.class_list)

  # Add a game object to the running game
  def add(self, obj_description):  
    descr = obj_description.copy()
    name = descr['class_name']

    if not name in self.class_list:
      print("Error in story bord: \""+ name + "\" is not a known game object class name")
      sys.exit(1) 

    del descr['class_name']
    print("adding object", name);

    # Create the new object and add it to the list
    #try:
    obj = self.class_list[name](**descr) 
    self.list.append( {
        'type' : obj.object_type,
        'obj'  : obj 
      }
    )
    #except Exception as err:
    #  print("Error in story board, when creating", name, ": \"", err, "\"\n  Unable to create game object with parameters:", obj_description)
    #  sys.exit(1)  

class Game:
  # Constructor
  def __init__(self):
    
    pygame.init()
    # Set up game screen
    self.window = pygame.display.set_mode( (screen_width,screen_height) 
       #, RESIZABLE | SCALED | FULLSCREEN
    )
    pygame.display.set_caption(game_name)
    pygame.mouse.set_visible(False)

    # start sound interface
    try:
      pygame.mixer.init()
    except:
      print("Pygame Sound mixer failed to initialize")

    # Make a place to store the current state of the game
    self.state = GameState()

    # in game objects
    self.state.object = GameObject()

    # Create basic game interface
    self.dashboard = dashboard.Dashboard(self.state)
    
    # Enable input from user
    self.player_input = player_input.PlayerInput(self.state)
    self.state.player_input = self.player_input

    # Define the game screen area
    self.rect = pygame.Rect(0,0,screen_width,screen_height - self.dashboard.rect[3]) 
    
    self.tech_screen = tech_screen.TechScreen(self.state)
    #self.end_game = end_game.EndGame(game_variable)   
    self.level_controle = level_controle.LevelControle(self.state)

  # Destructor  
  def __del__(self):
    # Close the game window
    pygame.display.quit()
    pygame.quit()

  # test if a game object is active and hitable
  def __obj_active(self, obj):
    return not getattr( obj, 'delete', False) and not getattr( obj, 'dead', False) and getattr(obj, 'rect', False) 

  def start(self):
    # Set game variables to start values.
    self.state.reset()
    self.level_controle.set(1)
    self.loop()

  # This is the main game loop
  def loop(self):
    self.player_input.reset()
    
    # Start using pygame loop timing (Frame rate)
    self.clock = pygame.time.Clock()
    while not self.state.stop:
      # Store the time that this frame starts
      self.state.frame_start = pygame.time.get_ticks()
  
      # Get player input
      self.player_input.update()

      scroll = (0,0)
      
      # == move all objects ==
      for game_obj in self.state.object.list:
        if callable(getattr(game_obj['obj'], 'update', None)):
          game_obj['obj'].update(scroll)


      # == Collission check ==
  
      # change to self.collidable_object.list
      # Check for collissions with all objects, that has a defined rectangle. Execpt dead and deleted objects.
      for i in range(0, len(self.state.object.list) ):
        if not self.state.object.list[i]['type'] == 'background' and self.__obj_active(self.state.object.list[i]['obj']):
          for ii in range(i+1, len(self.state.object.list) ):
            if self.__obj_active(self.state.object.list[i]['obj']) and self.state.object.list[i]['obj'].rect.colliderect(self.state.object.list[ii]['obj'].rect):
              # print(i,"hitting",ii)
              if getattr(self.state.object.list[i]['obj'], 'hit', False):
                self.state.object.list[i]['obj'].hit(self.state.object.list[ii]['type'], self.state)
              if getattr(self.state.object.list[ii]['obj'], 'hit', False):
                self.state.object.list[ii]['obj'].hit(self.state.object.list[i]['type'], self.state)

      # == Paint on screen ==
      # Count objects that determins when the game ends
      # Clean up dead objects
      count = {'alien': 0, 'player': 0, 'city':0}

      for game_obj in self.state.object.list:
        # Draw objects
        if callable(getattr(game_obj['obj'], 'draw', None)):
          game_obj['obj'].draw(self.window)

        # Remove dead objects
        if getattr(game_obj['obj'], 'delete', False):
          self.state.object.list.remove(game_obj)

        # Count important objects
        if game_obj['type'] in count:
          count[game_obj['type']] += 1

      # Paint inactive objects
      # for game_obj in self.inactive_object.list:
      #   if callable(getattr(game_obj['obj'], 'draw', None)):
      #     game_obj['obj'].draw()
      
      # Draw basic game interface
      self.dashboard.draw(self.window)

      # Draw tech screen
      if self.state.tech_screen_on:
        self.tech_screen.draw(self.window)

      # Next leven?
      #if count['alien'] <= 0:
      #  self.level_controle.next()

      """
      # Player dead?
      if count['player'] <= 0:
        print("Game ended")
        self.end_game.set()
        self.state.stop = True
      """
      # Show the new frame on screen
      pygame.display.flip()

      # Calculate timing and wait until frame rate is right
      self.clock.tick( frame_rate * self.state.game_speed )



    
 