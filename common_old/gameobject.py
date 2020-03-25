"""============================================================================

Game object is the base of an in game object

============================================================================"""
import pygame
import globals

class Gameobject:
  def __init__(self, boundry, position, size, speed, direction):
    # Set boundry (Default to screen size)
    if boundary is None:
      self.boundary = globals.game.rect
    else:  
      self.boundary = pygame.Rect(boundary)

    # Place on screen (Default to center of boundry)
    if position is None:
      self.position = (self.boundry.width//2 + self.boundry.x, self.boundry.height//2 + self.boundry.y) 
    else 
      self.position = position
  
    # Set scaled size (Default to real image size)
    if size is None:
      self.size = Alien1.sprite.size
    else
      self.size = size

    self.rect       = pygame.Rect(self.position, self.size)
    self.speed      = speed
    self.direction  = direction
    self.move_pattern = 'horisontal'

    self.delete     = False

  # Needs work ....
  
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


  def rect_touch(rect, boundary):
    return rect.x == boundary.x or rect.y == boundary.y or rect.x == boundary.width - rect.width or rect.y == boundary.height - rect.height


