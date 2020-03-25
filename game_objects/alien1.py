"""============================================================================

  Alien 1: Alien space ship

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional
    direction : in degrees 0-359 counting counter clockwise and 0 = right (optional)

============================================================================"""
import pygame
from game_functions import animation, gameobject
import config

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
      Alien1.sprite           = animation.Animation("alien-{index}.png", (100,50), Alien1.size) # Alien sprite map
      #Alien1.sprite_bomb      = animation.Animation('bomb.png', (40,40), (40,40))            # Bomb sprite map 
      #Alien1.sprite_shot      = animation.Animation('shot.png', (8,8), (8,8))                # Shot sprite map

      #Alien1.sound_die        = animation.Sound('small_bang.wav') # Sound to make when dieing
      #Alien1.sound_bomb_drop  = animation.Sound('drop_bomb.wav')  # Sound to make when dropping a bomb
      #Alien1.sound_shoot      = animation.Sound('plop.wav')       # Sound to make when shooting

      Alien1.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position, Alien1.size, speed, direction)
    self.object_type = gameobject.Gameobject.Type.ENEMY
    print("Alian at",self.rect)

  # Draw on game surface
  def draw(self, surface):
    # Flip image when direction is left
    if self.direction > 90 and self.direction < 270 :
      surface.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    #if scroll[0] or scroll[1]:
    self.rect.move(scroll)
    self.boundary.move(scroll)

    # test if out of boundary and deflect sprite by mirroring direction
    if self.touch_boundary():
      self.mirror_direction()

    # Move in circles
    self.direction += 3
    # Move sprite according to speed and direction
    self.move()

  # When hit or hitting something
  def hit(self, object_type):
    if object_type == gameobject.Gameobject.Type.PLAYER or object_type == gameobject.Gameobject.Type.FRIEND:
      self.delete = True
      self.game_state.score += 100
