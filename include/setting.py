"""============================================================================

  Settings

Rect(left, top, width, height) 
============================================================================"""
import pygame

number_of_cities = 5
screen_width = 800
screen_height = 600
screen_rect = (0 , 0, screen_width, screen_height)
frame_rate = 60
game_speed = 1

dashboard_background_color = (128,128,64)
dashboard_color = (0,0,0)
dashboard_rectangle = (0,560,800,40)
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
}
mouse_bind = {
  MOUSE_LEFT : 'fire',
}

