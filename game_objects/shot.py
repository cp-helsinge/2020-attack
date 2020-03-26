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

class Shot(gameobject.Gameobject):
  # Variables to store animations and sounds common to all Shot object
  loaded = False
  sprite = None
  sprit_bomb = None
  sprit_shot = None
  sound_die = None
  sound_shoot = None

  # Initialize Shot 
  def __init__(self, boundary = None, position = None, direction = 90, speed = 10):
    # Load animations and sounds first time this class is used
    if not Shot.loaded:
      Shot.sprite = self.Animate("shot.png",) 
      Shot.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position,self.sprite.size, speed, direction)
    
    # Adjust position to be centered on top of position
    self.rect.midbottom = position
    
  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    if scroll[0] or scroll[1]:
      self.rect.move(scroll)
      self.boundary.move(scroll)

    # test if out of boundary and deflect sprite by mirroring direction
    if self.touch_boundary():
      self.delete = True

    self.move()
    self.speed += 1

  # When hit or hitting something
  def hit(self, object_type):
    self.delete = True
