"""============================================================================

  Tech screen

  Create a transparent overlay display of internal values usefull for game 
    development and debuging
  
  Activare in-game with F3

============================================================================"""
import pygame

import config

class TechScreen:
  def __init__(self, game_state):
    self.game_state = game_state
    self.font = pygame.font.Font(None,30) 
    self.surface = pygame.Surface((config.screen_width, config.screen_height))
    self.rect = self.surface.get_rect()
    self.text_color = (0,128,0)
    self.idle_avarage = 1

  def display(self, x, y, format_str, *arguments):
    str = format_str.format(*arguments)
    text = self.font.render(str, True, self.text_color)
    self.surface.blit( text, (x, y) )

  def draw(self, screen_surface):
    # Paint background as transparent 
    self.surface.fill((0,0,0))

    self.display(10, 10, "Process time: {0} ms", pygame.time.get_ticks() - self.game_state.frame_start)                   

    self.display(10, 40, "Game objects: {0}", len(self.game_state.object.list))
    
    self.display(10, 70, "Level time: {0} Sec.", (pygame.time.get_ticks() - self.game_state.level_time) // 1000)
 
    self.display(10, 100, "Frame rate: {0}/sec. ({1}ms)", 
      int(self.game_state.frame_rate * self.game_state.game_speed),
      int(1000 / self.game_state.frame_rate / self.game_state.game_speed) )

    self.display(10, 130, "Game speed: {0}", self.game_state.game_speed )

    # Draw box around game objects
    for game_obj in self.game_state.object.list:
      if getattr(game_obj['obj'], 'rect', None):
        pygame.draw.rect(self.surface,self.text_color, game_obj['obj'].rect, 2)
 
    # Make surface transparent and copy unto display surface
    self.surface.set_colorkey((0,0,0))
    self.surface.set_alpha(150)
    screen_surface.blit(self.surface, self.rect)


   