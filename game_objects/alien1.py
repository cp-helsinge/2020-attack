"""============================================================================

  Alien 1: Alien space ship

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
import math
import random
from game_functions import animation

import config


class Object_type:
  NEUTRAL = 'neutral'
  ENEMY = 'enemy'
  PLAYER = 'player'

class Gameobject:
  def __init__(self, boundary = None, position=None, size=None, speed=1, direction=0):
    self.speed      = speed
    self.direction  = direction

    if boundary:
      self.boundary   = pygame.Rect(boundary)
    else: 
      self.boundary = pygame.Rect((0,0), (config.screen_width, config.screen_height))

    if size:
      self.size = size
    else:    
      self.size = (100,100)

    if position:
      self.position = position
    else:
      self.position = self.boundary.center

    self.rect = pygame.Rect(self.position, self.size)

    self.delete     = False
    self.object_type = Object_type.NEUTRAL


class Alien1(Gameobject):
  # Variables to store animations and sounds common to all Alien1 object
  loaded = False
  sprite = None
  sprit_bomb = None
  sprit_shot = None
  sound_die = None
  sound_shoot = None

  # Initialize Alien1 
  def __init__(self, boundary = None, position = None, size = None, direction = 0, speed = 1):
    print("init alien")
    # Load animations and sounds first time this class is used
    if not Alien1.loaded:
      Alien1.sprite           = animation.Animation("alien-{index}.png", (100,50), (100,50)) # Alien sprite map
      Alien1.sprite_bomb      = animation.Animation('bomb.png', (40,40), (40,40))            # Bomb sprite map 
      Alien1.sprite_shot      = animation.Animation('shot.png', (8,8), (8,8))                # Shot sprite map

      Alien1.sound_die        = animation.Sound('small_bang.wav') # Sound to make when dieing
      Alien1.sound_bomb_drop  = animation.Sound('drop_bomb.wav')  # Sound to make when dropping a bomb
      Alien1.sound_shoot      = animation.Sound('plop.wav')       # Sound to make when shooting

      Alien1.loaded = True # Indicate that all comnmon exrternal attributes are loaded

    if not boundary:
      self.boundary = pygame.Rect((0,0),(config.screen_width, config.screen_height))

    # Inherit from game object class
    Gameobject.__init__(self, boundary, position, size, speed, direction)
    print("Alian at",self.rect)


  # Draw on game surface
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 0:
      surface.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    # test if out of boundary
    if animation.rect_touch(self.rect, self.boundary):
      # Change to oposite direction
      self.direction = (self.direction + 180) % 360 // 1

    self.rect = animation.move_rect(self.rect, self.direction, self.speed, self.boundary)  

  # When hit or hitting something
  def hit(self, object_type, game_variable):
    if object_type == 'shot':
      self.delete = True
      game_variable['score'] += 100
