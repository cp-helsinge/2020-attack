"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame
from common import globals
from game_objects import setting

class Dashboard:
  def __init__(self):
    self.rect = pygame.Rect(setting.dashboard_rectangle)

    # Create a background image
    self.background = pygame.Surface((self.rect.width, self.rect.height))

    # Paint background
    self.background.fill(setting.dashboard_background_color)

    # Paint health in the center of the dashboard
    w = self.rect.width // 5    # Width
    h = self.rect.height // 2   # Height
    cx = self.rect.width // 2   # Center x 
    cy = h                      # Center y
    bw = 2                      # border line width
    
    # Draw health bar background
    pygame.draw.polygon(
      self.background,
      setting.dashboard_color,
      (
        (cx - w//2, cy - h//2), # Top left
        (cx + w//2, cy - h//2), # Top right
        (cx + w//2 + 3 * bw   , cy       ), # middel right
        (cx + w//2, cy + h//2), # bottom right
        (cx - w//2, cy + h//2), # Bottom left
        (cx - w//2 - 3 * bw , cy       ), # middel right
        (cx - w//2, cy - h//2), # Top left
      )
    )
    pygame.draw.polygon(
     self.background,
      (0,0,0),
      (
        (cx - w//2 + bw, cy - h//2 + bw ), # Top left
        (cx + w//2 - bw, cy - h//2 + bw ), # Top right
        (cx + w//2 + bw    , cy       ), # middel right
        (cx + w//2 - bw, cy + h//2 - bw ), # bottom right
        (cx - w//2 + bw, cy + h//2 - bw ), # Bottom left
        (cx - w//2 - bw , cy          ), # middel right
        (cx - w//2 + bw, cy - h//2 + bw ), # Top left
      )
    )
 
    self.health_bar_rect = pygame.Rect((cx - w//2 + 2* bw, cy - h//2 - 2 * bw, w - 4 * bw, h - 4 * bw) )
    self.health_bar_rect.center = self.rect.center

    # Create a font 
    self.font = pygame.font.Font(
      setting.dashboard_font,
      setting.dashboard_font_size
    ) 
 
  def draw(self, surface = False ):
    if( not surface ):
      surface = globals.game.window

    surface.blit( self.background, self.rect )
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
    if globals.player.health > 0:
      hb_rect = pygame.Rect(self.health_bar_rect)
      hb_rect.width = (self.health_bar_rect.width * min(globals.player.health, 100)) // 100 
      pygame.draw.rect(surface,(200,0,0),hb_rect)

    # Paint level middle right of dashboard
    text = self.font.render(
      "Level: " + str(globals.game.level) +" ",
      True, 
      setting.dashboard_color
    )
    text_rect = text.get_rect()
    text_rect.midright = self.rect.midright 
    surface.blit( text, text_rect )


   