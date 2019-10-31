"""============================================================================

  Dashboard

============================================================================"""
import pygame
from include import globals
from include import setting

setting = globals.setting
game = globals.game

class Dashboard:
  def __init__(self):
    self.font = pygame.font.Font('freesansbold.ttf', 32) 

  def display_time(self, millisecs, game_over):
    if not game_over:
      self.text = self.font.render(bytes(str(millisecs),"ascii"), True, green, blue)
      self.textRect = self.text.get_rect()
      self.border_rect = window.get_rect()
      self.textRect.center = (self.border_rect.width - 70, self.border_rect.height - 30) 
    else:
      self.font = pygame.font.Font('freesansbold.ttf', 50) 
      self.text = self.font.render("Game Over in "  +    
              bytes(str(millisecs),"ascii").decode("utf-8") +
              " seconds" , True, lilla, blue)
      self.textRect = self.text.get_rect()
      self.border_rect = window.get_rect()
      self.textRect.center = (self.border_rect.width // 2, self.border_rect.height // 2) 

  def update(self):
    scoreStr = self.font.render("Score: " + str(1000), True, (0,0,0),(128,128,128))
    scoreRect = scoreStr.get_rect()  
    scoreRect.bottomleft = (0, globals.setting.screen_height) 

    globals.game.window.blit(scoreStr, scoreRect)    