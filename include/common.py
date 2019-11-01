"""============================================================================

  Common functions

============================================================================"""
import pygame
import math
from include import globals

# load image, convert alpha channel (transparrent areas) and resize image
def load_image(name, rect=False):
  if( rect ):
    return pygame.transform.smoothscale(
      pygame.image.load( globals.gfx_path + name )
        .convert_alpha(),
      ( rect[2], rect[3] )
    )
  else:
    return pygame.image.load( globals.gfx_path + name ).convert_alpha()


def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)

