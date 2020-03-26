"""============================================================================

  Player space ship

  parameters:
    boundery  : boundary of movement
    position  : Start position. (default to center of boundry)
    speed     : Optional

============================================================================"""
import pygame
from game_functions import gameobject
import config

fire_rate = 3

class Player(gameobject.Gameobject):
  # Variables to store animations and sounds common to all Player object
  loaded = False
  sprite = None
  sprit_bomb = None
  sprit_shot = None
  sound_die = None
  sound_shoot = None

  # Initialize Player 
  def __init__(self, boundary = None, position = None, speed = 20):
    print("init Player")
    # Load animations and sounds first time this class is used
    if not Player.loaded:
      Player.size = (50,50)
      Player.sprite = self.Animate("playerX.png", (50,50), Player.size) # sprite map
      Player.loaded = True # Indicate that all common external attributes are loaded

    # Inherit from game object class
    gameobject.Gameobject.__init__(self, boundary, position, self.sprite.size, speed)
     
    self.fire_rate = fire_rate
    self.last_shot = 0
    self.health = 100

    # Make this object accessable to other objects
    self.game_state.player = self

  # Draw on game surface
  def draw(self, surface):
    surface.blit(self.sprite.get_surface(),self.rect)
    
  # Movement
  def update(self, scroll):
    if scroll[0] or scroll[1]:
      self.boundary.move(scroll)
      self.rect.move(scroll)

    # Move player according to input
    if self.game_state.key['left']:
      self.direction = 180
      self.move()
    
    if self.game_state.key['right']:
      self.direction = 0
      self.move()
    
    if self.game_state.key['up']:
      self.direction = 90
      self.move()
    
    if self.game_state.key['down']:
      self.direction = 270
      self.move()
    
    # Fire, but only if  1 / fire_rate seconds has passed since last shot
    if self.game_state.key['fire'] and ( ( pygame.time.get_ticks() - self.last_shot ) > 1000 / self.fire_rate ):
      # Save stooting time
      self.last_shot = pygame.time.get_ticks()
      self.game_state.object.add({
        'class_name': 'Shot',
        'position': self.rect.midtop,
        'boundary': None,
        'speed': 5,
        'direction': 90
      })

  # When hit or hitting something
  def hit(self, object_type):
    print("I was hit by",object_type)
    if object_type == 'Shot':
      self.health -= 15
    if object_type == 'Bomd':
      self.health -= 40
    if object_type == 'Alien1':
      self.health -= 70