"""============================================================================
  Next_level

  - Start new levels
  - load game objects
  - run new level graphics

============================================================================"""
import pygame
import os

from game_functions import end_game, animation
from game_attributes import story

import config



class LevelControle:
  def __init__(self, game_state):
    self.game_state = game_state
    self.music = False
    self.active = False

  def add(self, 
    movie = False,
    sprite = False, 
    color = (0,0,0),
    intro_time = 2,
    intro_effect = False,  
    hold_time = 1, 
    outtro_time = 1,
    outtro_effect = False,
    sound = False
  ):
    self.movie = False
    self.sprite = sprite
    self.color = color
    self.intro_time = intro_time
    self.intro_effect = intro_effect
    self.hold_time = hold_time
    self.outtro_time = outtro_time
    self.outtro_effect = outtro_effect
    self.active = True
    self.sound = sound

  # Set a new game level
  def set(self, level = False):
    # remove queued player input 
    self.game_state.player_input.reset()

    # Turn music off
    try:
      pygame.mixer.music.stop()
    except: pass

    if( level ):
     self.game_state.level = level
    else:
      self.game_state.level += 1

    # Load game objects for the new level
    print("Loading level",self.game_state.level)
    if len(story.level) > self.game_state.level:
      # Empty game object list
      self.game_state.object.list = []

      # Loop through list of game object on this level
      for obj in story.level[self.game_state.level]:
        # Load pseudo classes
        if obj['class_name'] == 'next_level':
          self.add(**parameters)
        elif obj['class_name'] == 'music': 
          self.music = parameters
        # Load in-game objects  
        else:
          self.game_state.object.add(obj)

      # run next level graphics
      if self.active:
        self.play_new_level_effect() 

      # Start music for next level
      if self.music:
        pygame.mixer.music.play(loops=-1)

      # Reset play time for level
      self.game_state.level_time = pygame.time.get_ticks() 

    else:  
      self.game_state.stop = True
      # globals.game.end_game.set()

    
  def next(self):
    self.set()

  # Next level grapichs effects
  # There are 3 stages of level graphics:
  # - intro, hold and outtro
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
            for game_object in self.game_state.object.list:
              if game_object['type'] == 'background' and game_object['obj'].sprite:
                self.sprite = game_object['obj'].sprite
          else:
            stage += 1

        if stage > 3:

          effect = False
          duration = 0
          self.active = False  

      # Video http://sbirch.net/tidbits/pygame_video.html

      if effect == 'slide_down':
        inc = int( setting.screen_height / duration / setting.frame_rate )
        if self.sprite:
          step += inc
          if self.sprite:
            self.game_state.window.blit(self.sprite.get_surface(), (0, step - setting.screen_height))
          else:
            self.game_state.window.fill(self.color, (0, step - setting.screen_height))
          self.game_state.window.scroll(0, inc)
          
          if step >= setting.screen_height:
            next_stage = True

      if effect == 'hold':
        step += 1
        if step >= duration * setting.frame_rate:
          next_stage = True
      
      pygame.display.flip()
      self.game_state.clock.tick( setting.frame_rate )

      # Check for user input
      event_list = pygame.event.get()
      for event in event_list:
        if event.type == pygame.QUIT:
          self.game_state.player_input.stop
          self.active = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          self.active = False 
