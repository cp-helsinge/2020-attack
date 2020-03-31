"""============================================================================

  Settings

Rect(left, top, width, height) 
============================================================================"""
import pygame

game_name = 'Alien Attack'
number_of_cities = 5
screen_width = 1000
screen_height = 700
screen_rect = (0 , 0, screen_width, screen_height)
frame_rate = 60
game_speed = 1
fire_rate = 3

dashboard_background_color = (16,64,96)
dashboard_color = (192,128,0)
dashboard_rectangle = (0,660,1000,40)
dashboard_font = 'freesansbold.ttf'
dashboard_font_size = 32

MOUSE_LEFT  = 1 
MOUSE_WHEEL = 2
MOUSE_RIGHT = 3

key_bind =  {
  pygame.K_a      : 'left',  # A
  pygame.K_LEFT   : 'left',
  pygame.K_d      : 'right', # D  
  pygame.K_RIGHT  : 'right',
  pygame.K_w      : 'up',    # A
  pygame.K_UP     : 'up',
  pygame.K_s      : 'down',  # D
  pygame.K_DOWN   : 'down',
  pygame.K_SPACE  : 'fire',
  pygame.K_RETURN : 'fire',
  
}
mouse_bind = {
  MOUSE_LEFT : 'fire',  
  MOUSE_RIGHT : 'fire',
}

