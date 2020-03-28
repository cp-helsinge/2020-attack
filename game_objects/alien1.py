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
  count = 0

  # === Initialize Alien1 ===
  def __init__(self, boundary = None, position = None, direction = 0, speed = 1):
    print("init alien")
    # Load animations and sounds first time this class is used
    if not Alien1.loaded:
      Alien1.size = (100,50)
      Alien1.sprite = self.Animate("ufo1-{index}.png", (100,50), Alien1.size) # Alien sprite map
      Alien1.loaded = True # Indicate that all common external attributes are loaded

    # Get a animation offset that animation of the same class, looks different
    self.animation_offset = Alien1.count
    Alien1.count += 1

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position, self.sprite.size, speed, direction)
    self.health = 100

 
  # === Draw on game surface ===
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 90 and self.direction < 270 :
      surface.blit(pygame.transform.flip(self.sprite.get_surface(self.animation_offset),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(self.animation_offset),self.rect)

    # Draw healt bar  
    if self.health > 0:
      pygame.draw.line(
        surface,
        (200-self.health, self.health * 2, 0),
        (self.rect.x, self.rect.y),
        (self.rect.x + self.rect.width * self.health / 100, self.rect.y)
        ,(3)
      )

  # === Movement ===
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

  # === When hit or hitting something ===
  def hit(self, object_type):
    if object_type.startswith('Player'):
      self.health -= 100

    if object_type.startswith('Shot'):
      self.health -= 10

    # Check if i'm dead
    if self.health <=0:  
      self.delete = True
      self.game_state.score += 50
