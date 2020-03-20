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
from common import *

class Object_type:
  NEUTRAL = 'neutral'
  ENEMY = 'enemy'
  PLAYER = 'player'

class Gameobject:
  def __init__(self, boundry=None, position=None, size=None, speed=1, direction=0):
 
    self.sprite     = sprite
    self.rect       = pygame.Rect(rect)
    self.speed      = speed
    self.direction  = direction
    if boundary:
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.bomb       = bomb
    self.shot       = shot
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
    # Load animations and sounds first time this class is used
    if not Alien1.loaded:
      Alien1.sprite           = Animate("alien-{index}.png", (100,50), (100,50)) # Alien sprite map
      Alien1.sprite_bomb      = Animate('bomb.png', (40,40), (40,40))            # Bomb sprite map 
      Alien1.sprite_shot      = Animate('shot.png', (8,8), (8,8))                # Shot sprite map

      Alien1.sound_die        = Sound('small_bang.wav') # Sound to make when dieing
      Alien1.sound_bomb_drop  = Sound('drop_bomb.wav')  # Sound to make when dropping a bomb
      Alien1.sound_shoot      = Sound('plop.wav')       # Sound to make when shooting

      Alien1.loaded = true # Indicate that all comnmon exrternal attributes are loaded

    # Inherit from game object class
    Gameobject.__init__(self, boundry, position, size, speed, direction)

  # Draw on game surface
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 0:
      surface.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    # test if out of boundry
    if common.rect_touch(self.rect, self.boundary):
      # Change to oposite direction
      self.direction = (self.direction + 180) % 360 // 1

    self.rect = common.move_rect(self.rect, self.direction, self.speed, self.boundary)  

  # When hit or hitting something
  def hit(self, object_type, game_variable):
    if object_type == 'shot':
      self.delete = True
      game_variable['score'] += 100
