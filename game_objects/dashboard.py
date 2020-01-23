"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame
from game_objects import globals
from game_objects import setting

class Dashboard:
  def __init__(self):
    self.font = pygame.font.Font(
      setting.dashboard_font,
      setting.dashboard_font_size
    ) 
    self.rect = pygame.Rect(setting.dashboard_rectangle)

  def draw(self, surface = False ):
    if( not surface ):
      surface = globals.game.window

    # Paint background
    surface.fill(
      setting.dashboard_background_color,
      self.rect
    )

    # Paint Score in left middle of dashboard
    text = self.font.render(
      " Score: " + str(globals.game.score),
      True, 
      setting.dashboard_color
    )
    text_rect = text.get_rect()
    text_rect.midleft = self.rect.midleft 
    surface.blit( text, text_rect )

    # Paint health in the center of the dashboard
    w = self.rect.width // 5
    h = self.rect.height // 2
    rect = pygame.Rect(0, 0, w, h)
    rect.center = self.rect.center
    pygame.draw.rect(surface,(100,100,30),(rect.x-3, rect.y-3, w+6, h + 6))
    rect.width = rect.width * min(globals.player.health, 100) // 100 
    pygame.draw.rect(surface,(200,0,0),rect)

    # Paint level middle right of dashboard
    text = self.font.render(
      "Level: " + str(globals.game.level) +" ",
      True, 
      setting.dashboard_color
    )
    text_rect = text.get_rect()
    text_rect.midright = self.rect.midright 
    surface.blit( text, text_rect )


   