"""============================================================================

  Shot

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
from game_functions import gameobject

class ShotAlien1(gameobject.Gameobject):
  # Variables to store animations and sounds common to all Shot object
  loaded = False
  sprite = None
  sound_shoot = None
  count = 0

  # Initialize Shot 
  def __init__(self, boundary = None, position = None, direction = 90, speed = 10):
    # Load animations and sounds first time this class is used
    if not ShotAlien1.loaded:
      ShotAlien1.sprite = self.Animate("shot_alien1.png") 
      ShotAlien1.loaded = True # Indicate that all common external attributes are loaded
      ShotAlien1.count += 1

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position,self.sprite.size, speed, direction)
    
    # Adjust position to be centered under position
    self.rect.midtop = position
    self.speed += 10

    # Set charakteristica other than default
    self.type = self.Type.CG_OPPONENT
    self.impact_power = 10
    self.health = 1

  def __del__(self):
    ShotAlien1.count -= 1

  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(ShotAlien1.count),self.rect)
    
  # Movement
  def update(self, scroll):
    if scroll[0] or scroll[1]:
      self.rect.move(scroll)
      self.boundary.move(scroll)

    # test if out of boundary and deflect sprite by mirroring direction
    if self.touch_boundary():
      self.delete = True

    self.move()

  # When hit or hitting something
  def hit(self, object_type):
    self.delete = True
