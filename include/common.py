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




def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)

