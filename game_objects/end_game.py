"""============================================================================

    End game


============================================================================"""

import pygame
from game_objects import globals
from game_objects import setting

class EndGame:
  def __init__(self):
    self.font = pygame.font.Font(None,100) 
    self.surface = pygame.Surface((setting.screen_width, setting.screen_height))
    self.rect = self.surface.get_rect()
    self.text_color = (128,20,0)
    self.idle_avarage = 1
 
    # Paint background as transparent 
    self.surface.fill((0,0,0))
    center = self.surface.get_rect().center 

    ellipse_rect = pygame.Rect((0,0,setting.screen_width// 2, setting.screen_height // 4))
    ellipse_rect.center = center
    ellipse = pygame.draw.ellipse(self.surface, self.text_color, ellipse_rect, 10)

    text = self.font.render("GAME OVER", True, self.text_color)
    text_rect = text.get_rect()
    text_rect.center = center 
    self.surface.blit( text, text_rect )

    # Make surface transparent and copy unto display surface
    self.surface.set_colorkey((0,0,0))
    self.surface.set_alpha(255)
    globals.game.window.blit(self.surface, self.rect)

   
  def display(self, x, y, format_str, *arguments):
    str = format_str.format(*arguments)
    text = self.font.render(str, True, self.text_color)
    self.surface.blit( text, (x, y) )

  def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
