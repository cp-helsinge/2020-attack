"""============================================================================

  Alien 1: Alien space ship

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
from game_functions import gameobject

class Alien1(gameobject.Gameobject):
  # Variables to store animations and sounds common to all Alien1 object
  loaded = False
  sprite = None
  sprit_bomb = None
  sprit_shot = None
  sound_die = None
  sound_shoot = None

  # Initialize Alien1 
  def __init__(self, boundary = None, position = None, direction = 0, speed = 1):
    print("init alien")
    # Load animations and sounds first time this class is used
    if not Alien1.loaded:
      Alien1.size = (100,50)
      Alien1.sprite = self.Animate("alien-{index}.png", (100,50), Alien1.size) # Alien sprite map
      Alien1.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position, self.sprite.size, speed, direction)
    self.health=100
    print("Alian at",self.rect)
    print(self.__class__)
    print(self.__class__.__name__)

  # Draw on game surface
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 90 and self.direction < 270 :
      surface.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    if scroll[0] or scroll[1]:
      self.boundary.move(scroll)
      self.rect.move(scroll)

    # test if out of boundary and deflect sprite by mirroring direction
    if self.touch_boundary():
      self.mirror_direction()

    # Move in circles
    self.direction += 3
    # Move sprite according to speed and direction
    self.move()

  # When hit or hitting something
  def hit(self, object_type):
    if object_type == 'Player':
      self.health-=99

    if object_type == 'Shot':
      self.health -= 50

    # Check if i'm dead
    if self.health <=0:  
      self.delete = True
      self.game_state.score += 50
