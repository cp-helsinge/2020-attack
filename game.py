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
import pprint
from collections import defaultdict
import config

# Import game classes
from game_functions import dashboard, player_input, level_controle, tech_screen, gameobject, end_game

game_name = 'Alien Attack CP-20'
game_speed = 1
game_objects_from = 'game_objects' # Used to import game objects dynamically as the from part

class GameObjects:
  def __init__(self):
    print("Loading game object classes...")
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
        print("..loading",name)
        # from <game_objects_from> import <name>
        cls = __import__(game_objects_from, None, None, [name.lower()], 0)
        # class = <name>.<Name>
        self.class_list[name] = getattr( getattr(cls,name.lower()),name )

        #except Exception as err:
        #  print("Unable to load game object in", name + ".py", err)
    print(len(self.class_list)," Game Classes loaded.")

  # Add a game object to the running game
  def add(self, obj_description):  
    descr = obj_description.copy()
    name = descr['class_name']

    if not name in self.class_list:
      print("Error when adding game object: \""+ name + "\" is not a known object class name")
      sys.exit(1) 

    del descr['class_name']

    # Create the new object and add it to the list
    try:
      obj = self.class_list[name](**descr) 
      self.list.append(obj)
    except Exception as err:
      print("Error when creating game object", name, ": \"", err, "\"\n  Unable to create object with parameters:", obj_description)
      sys.exit(1)  

class Game(player_input.PlayerInput):
  # Constructor
  def __init__(self):
    self.level = 1
    self.score = 0
    self.player = None
    self.frame_start = 0
    self.level_time = 0
    self.frame_rate = config.frame_rate
    self.game_speed = game_speed
    self.fullscreen = False
    self.game_over = False
    self.suspended = False

    # Set up game screen
    pygame.init()

    # Set up a canvas to paint the game on
    self.canvas = pygame.Surface((config.screen_width,config.screen_height))

    # Set up the screen to match window size
    self.resize((config.screen_width,config.screen_height))
    
    pygame.display.set_caption(game_name)
    pygame.mouse.set_visible(False)

    # start sound interface
    try:
      pygame.mixer.init()
    except:
      print("Pygame Sound mixer failed to initialize")

    # in game objects
    self.game_objects = GameObjects()

    # Create basic game interface
    self.dashboard = dashboard.Dashboard(self)

    # Define the game screen area
    self.rect = pygame.Rect(0,0,config.screen_width,config.screen_height - self.dashboard.rect[3]) 
    
    # Add functionality
    self.tech_screen = tech_screen.TechScreen(self)
    self.level_controle = level_controle.LevelControle(self)
    self.end_game = end_game.EndGame(self)

    # Make game states globally available
    config.game_state = self

  # Destructor  
  def __del__(self):
    self.exit()

  def exit(self):
    if self.fullscreen:
      self.toggle_fullscreen()

    # Close the game window
    pygame.display.quit()
    pygame.quit()

  def resize(self, new_size=None):
    if new_size is None:
      size = [config.screen_width,config.screen_height]
    else:
      size = [new_size[0], new_size[1]]

    # Maintain aspect ratio
    aspect_ratio = config.screen_width / config.screen_height
    # Too wide
    if size[0] / size[1] > config.screen_width / config.screen_height:
      size[0] = int(size[1] * aspect_ratio)

    # Too tall
    elif size[0] / size[1] < config.screen_width / config.screen_height:    
      size[1] = int(size[0] / aspect_ratio)

    self.screen = pygame.display.set_mode(  size , pygame.RESIZABLE )  # RESIZABLE | SCALED | FULLSCREEN | HWSURFACE | DOUBLEBUF
    self.screen_width, self.screen_height = size
    print("Resizing to:", size)

  def toggle_fullscreen(self):
    self.fullscreen = not self.fullscreen
    if self.fullscreen == 42: # Not working properly
      if pygame.display.get_driver()=='x11c':
        pygame.display.toggle_fullscreen()
      else:
        self.screen = pygame.display.set_mode( (0, 0), pygame.FULLSCREEN )
      self.screen_width, self.screen_height = self.screen.get_size()
    else:  
      self.resize()
    print("Full screen:", self.fullscreen, pygame.display.get_driver())
    

  # test if a game object is active and hitable
  def __obj_active(self, obj):
    return not getattr( obj, 'delete', False) and not getattr( obj, 'dead', False) and getattr(obj, 'rect', False) 

  def start(self):
    # Set game variables to start values.
    self.game_over = False
    self.suspended = False
    self.level_controle.set(1)
    self.loop()

  # This is the main game loop
  def loop(self):
    self.resize()
    self.reset_player_input()

    # Start using pygame loop timing (Frame rate)
    self.clock = pygame.time.Clock()
    while not self.stop:

      # Store the time that this frame starts
      self.frame_start = pygame.time.get_ticks()
  
      # Get player input
      self.update_player_input()

      self.canvas.fill((0,0,70))
      
      # == move all objects ==
      scroll = (0,1)

      for game_obj in self.game_objects.list:
        if callable(getattr(game_obj, 'update', None)):
          game_obj.update(scroll)

      if not self.suspended:
        
        # == Collission check ==
        # change to self.collidable_object.list
        # Check for collissions with all objects, that has a defined rectangle. Execpt dead and deleted objects.

        # Loop through all active objects
        for i in range(0, len(self.game_objects.list) ):
          # Skip objects that are not active game objects
          if not self.__obj_active(self.game_objects.list[i]): continue

          # Loop through the rest of the list 
          for ii in range(i+1, len(self.game_objects.list) ):
            # Skip objects that are not active game objects
            if not self.__obj_active(self.game_objects.list[ii]): continue

            # Compare rectangle of all other objects
            if self.game_objects.list[i].rect.colliderect(self.game_objects.list[ii].rect):

              # Tell 1st. object that it has been hit by a 2nd. object class
              if getattr(self.game_objects.list[i], 'hit', False):
                self.game_objects.list[i].hit(self.game_objects.list[ii].__class__.__name__)
              # Tell 2nd. object that it has been hit by a 1st. object class
              if getattr(self.game_objects.list[ii], 'hit', False):
                self.game_objects.list[ii].hit(self.game_objects.list[i].__class__.__name__)

        # == Paint on screen ==
        # Make a counter of game object class names
        self.count = defaultdict(int)

        for game_obj in self.game_objects.list:
          # Count number of ocurences of each Class
          self.count[game_obj.__class__.__name__] += 1 
          
          # Count Player
          if game_obj.__class__.__name__.startswith('Player'):
            self.count['player_items'] += 1

          if game_obj.__class__.__name__.startswith('Alien'):
            self.count['alien_items'] += 1
        
        # Check for level end
        self.level_controle.check()
   
      # == Display level and end game graphics ==
      else: 
        if self.game_over:  
          self.end_game.draw(self.canvas)
        else:
          self.level_controle.draw(self.canvas)

      # == Delete obsolite objects ==
      for game_obj in self.game_objects.list:
        # Remove deleted objects
        if getattr(game_obj, 'delete', False):
          self.game_objects.list.remove(game_obj)

      # Draw tech screen
      if self.tech_screen_on:
        self.tech_screen.draw(self.canvas)
    
      # Draw basic game interface
      self.dashboard.draw(self.canvas)

      # Draw all game objects
      for game_obj in self.game_objects.list:
        # Draw objects
        if callable(getattr(game_obj, 'draw', None)):
          game_obj.draw(self.canvas)

      # scale and show the new frame on screen
      self.screen.blit(pygame.transform.scale(self.canvas, self.screen.get_size()),(0,0))
      pygame.display.flip() 

      # Calculate timing and wait until frame rate is right
      self.clock.tick( config.frame_rate * self.game_speed )

    self.exit()

    
 