"""============================================================================

  Game object template

  Inherited by all game objects

============================================================================"""
import pygame
import math
import random
from game_functions import animation
import config

class Gameobject:
  class Type:
    NEUTRAL = 'neutral'
    ENEMY = 'enemy'
    PLAYER = 'player'
    FRIEND = 'friend'
    INACTIVE = 'inactive'
    SHOT = 'shot'
    ENEMY_SHOT = 'enemy_shot'
    ENEMY_BOMB = 'enemy bomb'

  def __init__(self, boundary = None, position=None, size=None, speed=1, direction=0):
    self.speed      = speed
    self.direction  = direction

    if boundary:
      self.boundary   = pygame.Rect(boundary)
    else: 
      self.boundary = pygame.Rect((0,0), (config.screen_width, config.screen_height))

    if not size:
      size = (100,100)

    if not position:
      position = self.boundary.center

    self.rect = pygame.Rect(position, size)

    self.game_state = config.game_state

    self.delete = False
    self.object_type = Gameobject.Type.INACTIVE

  # Move object according to speed and direction, within boundary
  def move(self):
    radie = -math.radians(self.direction)
    x = self.speed * math.cos(radie)
    y = self.speed * math.sin(radie)
    new_rect = self.rect.move(x,y)
    new_rect.clamp_ip(self.boundary)
    self.rect = new_rect

  # Mirror direction, when hittinh boundary
  def mirror_direction(self):
    if self.touch_boundary():
      # Left and Right side
      if self.rect.x == self.boundary.x or self.rect.x + self.rect.width == self.boundary.width:       
        self.direction = -self.direction + 180
      
      # bottom  and top
      if self.rect.y == self.boundary.y or self.rect.y + self.rect.height == self.boundary.height:       
        self.direction = -self.direction 
      
      # reduce angle to 0-360 degrees
      self.direction = (self.direction % 360) // 1  
      # Change to oposite direction

  def touch_boundary(self):
    touching = False
    touching |= self.rect.x == self.boundary.x 
    touching |= self.rect.y == self.boundary.y 
    touching |= self.rect.x == self.boundary.width - self.rect.width 
    touching |= self.rect.y == self.boundary.height - self.rect.height
    return touching

  # Return true at random, on avarage at <freq> times pr. second
  def random_frequency(freq):
    return random.randint(0, config.frame_rate // freq ) == 0