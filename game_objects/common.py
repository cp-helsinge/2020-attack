"""============================================================================

  Common functions

============================================================================"""
import pygame
import math
import os
import random 

from game_objects import globals
from game_objects import setting

# load image, convert alpha channel (transparrent areas) and resize image
def load_image(name, rect=False):
  if not name:
    return False
  if( rect ):
    return pygame.transform.smoothscale(
      pygame.image.load( os.path.join(globals.gfx_path, name ))
        .convert_alpha(),
      ( rect[2], rect[3] )
    )
  else:
    return pygame.image.load( os.path.join(globals.gfx_path, name) ).convert_alpha()


def load_sound(name):
  if not name or not pygame.mixer.get_init():
    return False
  try:
    return pygame.mixer.Sound(os.path.join(globals.sound_path, name) )
  except:
    return False
    
def load_music(name):
  try:
    pygame.mixer.music.load(os.path.join(globals.sound_path, name))
    return True
  except Exception as ex:
    print("failed to load music",ex)
    return False

# Move a rectangle in a direction, with a equcalent horisontal pixel speed, within a boundary recangle
def move_rect(rect, direction, speed, boundary=False):
  if not boundary:
    boundary = globals.game.rect
  radie = -math.radians(direction)
  x = speed * math.cos(radie)
  y = speed * math.sin(radie)
  new_rect = rect.move(x,y)
  new_rect.clamp_ip(boundary)
  return new_rect

# Return true at random, on avarage at <freq> times pr. second
def random_frequency(freq):
  return random.randint(0, setting.frame_rate // (freq * globals.game.game_speed) ) == 0

def rect_touch(rect, boundary):
  return rect.x == boundary.x or rect.y == boundary.y or rect.x == boundary.width - rect.width or rect.y == boundary.height - rect.height

def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)

