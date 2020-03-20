"""============================================================================

  Common functions

============================================================================"""
import pygame
import math
import os
import random 

from game_functions import globals, setting

"""
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
"""

class Sound:
  def __init__(self, file_name):
    if not pygame.mixer.get_init():
      print("Failed to use pygame mixer")

    try:
      self = pygame.mixer.Sound(os.path.join(globals.sound_path, name) )
    except:
      print("Failed to use pygame mixer")
    
class Music:
  def __init__(self, file_name):
    try:
      pygame.mixer.music.load(os.path.join(globals.sound_path, name))
    except Exception as ex:
      print("failed to load music",ex, "using sound file:", file_name)

# Return true at random, on avarage at <freq> times pr. second
def random_frequency(freq):
  return random.randint(0, setting.frame_rate // (freq * globals.game.game_speed) ) == 0

"""
def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)
"""
