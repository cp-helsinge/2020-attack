"""============================================================================

  Player


  parameters:
    rect      : Start position and size 
    image     : Image
    boundery  : boundary of movement
    speed     : 2
    direction : in degrees 0-359 counting counter clockwise and 0 = right
    axix      : x, y or xy
    
============================================================================"""
import pygame
from game_objects import globals
from game_objects import common
from game_objects import setting



class Player:
  def __init__(self, 
    rect, 
    image='player.png', 
    crosshair_image='crosshair.png', 
    boundary = False, 
    direction = 0, 
    speed = 1, 
    sound = False,
    shoot_sound = False,
    shot = False,
    ):
    
    # load image, convert alpha channel (transparrent areas) and resize image
    self.image       = common.load_image(image, rect )
    self.crosshair_image    = common.load_image("crosshair.png")
    self.rect       = pygame.Rect(rect)
    self.boundary   = boundary 
    if not boundary:
      self.boundary = globals.game.rect
    self.speed      = speed
    self.shot       = shot
    self.delete       = False
    self.fire_rate  = setting.fire_rate
    self.last_shot  = 0
    self.health     = 100
    globals.player  = self

  def draw(self):
    globals.game.window.blit(self.image,self.rect)

  def update(self):
    key = globals.game.player_input.key

    if key['left']:
      self.rect = common.move_rect(self.rect, 180, self.speed, self.boundary)
    
    if key['right']:
      self.rect = common.move_rect(self.rect, 0, self.speed, self.boundary)
    
    if key['up']:
      self.rect = common.move_rect(self.rect, 90, self.speed, self.boundary)
    
    if key['down']:
      self.rect = common.move_rect(self.rect, -90, self.speed, self.boundary)
    
    if key['fire'] and ( ( pygame.time.get_ticks() - self.last_shot ) > 1000 / self.fire_rate ):
      self.last_shot = pygame.time.get_ticks()
      
      # Place shot on top of player (without touching)
      player_midtop = self.rect.midtop
      x = player_midtop[0] - self.shot['rect'][2] // 2
      y = player_midtop[1] - self.shot['rect'][3] - 1 
      self.shot['rect'] = ( x, y, self.shot['rect'][2], self.shot['rect'][3])
      
      globals.game.object.add('shot',self.shot)

  def hit(self, object_type):
    print("I was hit by",object_type)
    if object_type == 'bomb':
      self.health -= 50
    elif object_type == 'enemy_shot':
      self.health -= 10

    if self.health <=0:   
      self.delete = True
      self.health = 0
    