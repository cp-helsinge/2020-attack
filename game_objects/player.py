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
    self.dead       = False
    self.fire_rate  = setting.fire_rate
    self.last_shot  = 0

  def draw(self):
    print("Player rect",self.rect)
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
      player_rect = self.rect
      self.shot['rect'] = ( self.rect.x, self.rect.y, self.shot['rect'][2], self.shot['rect'][3])
      globals.game.object.add('shot',self.shot)

