"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame
from include import globals
from include import setting

class Dashboard:
  def __init__(self):
    self.font = pygame.font.Font(
      setting.dashboard_font,
      setting.dashboard_font_size
    ) 
    self.rect = pygame.Rect(setting.dashboard_rectangle)

  def paint(self):
    # Paint background
    globals.game.window.fill(
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
    globals.game.window.blit( text, text_rect )

    # Paint health in the center of the dashboard
    text = self.font.render(
      "Health: " + str(globals.game.player_health),
      True, 
      setting.dashboard_color
    )
    text_rect = text.get_rect()
    text_rect.center = pygame.Rect(setting.dashboard_rectangle).center
    globals.game.window.blit( text, text_rect )

    # Paint level middle right of dashboard
    text = self.font.render(
      "Level: " + str(globals.game.level) +" ",
      True, 
      setting.dashboard_color
    )
    text_rect = text.get_rect()
    text_rect.midright = self.rect.midright 
    globals.game.window.blit( text, text_rect )


   