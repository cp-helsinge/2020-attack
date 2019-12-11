"""============================================================================
    Next_level
============================================================================"""
import pygame
import os

from game_objects import story
from game_objects import globals
from game_objects import common
from game_objects import end_game
from game_objects import setting

class LevelControle:
  def __init__(self):
    self.music = False
    self.active = False

  def add(self, 
    movie = False,
    image = False, 
    color = (0,0,0),
    intro_time = 2,
    intro_effect = False,  
    hold_time = 1, 
    outtro_time = 1,
    outtro_effect = False,
    sound = False
  ):
    self.movie = False
    self.image = image
    self.color = color
    self.intro_time = intro_time
    self.intro_effect = intro_effect
    self.hold_time = hold_time
    self.outtro_time = outtro_time
    self.outtro_effect = outtro_effect
    self.active = True
    self.sound = sound

  def set(self, level = False):
    try:
      pygame.mixer.music.stop()
    except:
      pass

    if( level ):
      globals.game.level = level
    else:
      globals.game.level += 1

    # Start new level
    globals.game.player_input.reset()
    board = story.get_level(globals.game.level)
    if board:
      globals.game.object.list = []
      for obj in board:
        for object_type, parameters in obj.items():
          # Load pseudo classes
          if object_type == 'next_level':
            self.add(**parameters)
          elif object_type == 'music': 
            self.music = parameters
          # Load in-game objects  
          else:
            globals.game.object.add(object_type, parameters)

      globals.game.level_time = pygame.time.get_ticks() 

      if self.active:
        self.play_new_level_effect() 
      
      if self.music:
        pygame.mixer.music.play(loops=-1)
          
    else:  
      globals.game.end_game.set()

    
  def next(self):
    self.set()

  def play_new_level_effect(self):
    end = False
    stage = 0
    next_stage = True

    if self.sound: 
      self.sound.play()

    while self.active:

      if next_stage:
        next_stage = False
        stage += 1
        step = 0
        if stage == 1: # Intro
          if self.intro_time > 0:
            effect = self.intro_effect
            duration = self.intro_time
          else:
            stage += 1

        if stage == 2: # middle
          if self.hold_time > 0:
            effect = 'hold'
            duration = self.hold_time
          else:
            stage += 1

        if stage == 3: # outtro
          if self.outtro_time > 0:
            effect = self.outtro_effect
            duration = self.outtro_time
            for game_object in globals.game.object.list:
              if game_object['type'] == 'background' and game_object['obj'].image:
                self.image = game_object['obj'].image
          else:
            stage += 1

        if stage > 3:

          effect = False
          duration = 0
          self.active = False  

      # Video http://sbirch.net/tidbits/pygame_video.html

      if effect == 'slide_down':
        inc = int( setting.screen_height / duration / setting.frame_rate )
        if self.image:
          step += inc
          if self.image:
            globals.game.window.blit(self.image, (0, step - setting.screen_height))
          else:
            globals.game.window.fill(self.color, (0, step - setting.screen_height))
          globals.game.window.scroll(0, inc)
          
          if step >= setting.screen_height:
            next_stage = True

      if effect == 'hold':
        step += 1
        if step >= duration * setting.frame_rate:
          next_stage = True
      
      pygame.display.flip()
      globals.game.clock.tick( setting.frame_rate )

      # Check for user input
      event_list = pygame.event.get()
      for event in event_list:
        if event.type == pygame.QUIT:
          globals.game.player_input.stop
          self.active = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          self.active = False 
