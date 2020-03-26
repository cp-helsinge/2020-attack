"""============================================================================

  Tech screen

  Create a transparent overlay display of internal values usefull for game 
    development and debuging
  
  Activare in-game with F3

============================================================================"""
import pygame
import pygame.freetype
import pprint
import config

class TechScreen:
  def __init__(self, game_state):
    self.game_state = game_state
    self.font = pygame.freetype.SysFont('Arial', 30, bold=True)
    self.font.origin = True
    self.surface = pygame.Surface((config.screen_width, config.screen_height))
    self.rect = self.surface.get_rect()
    self.text_color = (0,128,0)

  # Display text on transparent tech screen
  # Respect new line and do word wrap
  def text_display(self, start_x, start_y, format_str, *arguments):
    text = format_str.format(*arguments)
    chars = list(text)
    width, height = self.surface.get_size()
    width -= start_x
    height -= start_y
    line_spacing = self.font.get_sized_height() + 2
    space = self.font.get_rect(' ')
    x = start_x
    y = start_y + line_spacing

    for char in chars:
      # Check for new line
      if char == "\n": 
        x, y = start_x, y + line_spacing

      # Check for word wrap 
      elif char == " " and x + space.width >= width :
        x, y = start_x, y + line_spacing

      # Display letter
      else:
        self.font.render_to(self.surface, (x, y), char, self.text_color)
        x += self.font.get_rect(char).width + 1

    return x, y

  def draw(self, screen_surface):
    # Paint background as transparent 
    self.surface.fill((0,0,0))

    # Game engine numbers
    x, y = self.text_display(10, 10, "Process time: {0} ms", pygame.time.get_ticks() - self.game_state.frame_start)                   
    x, y = self.text_display(10, y, "Frame rate: {0}/sec. ({1}ms)", 
      int(self.game_state.frame_rate * self.game_state.game_speed),
      int(1000 / self.game_state.frame_rate / self.game_state.game_speed) )
    x, y = self.text_display(10, y, "Game speed: {0}", self.game_state.game_speed )

    # Player info
    x, y = self.text_display(10, y, "Level time: {0} Sec.", (pygame.time.get_ticks() - self.game_state.level_time) // 1000)
    x, y = self.text_display(10, y, "Player position X:{0} Y:{1}", self.game_state.player.rect.x, self.game_state.player.rect.y)
    x, y = self.text_display(10, y, "Pleayer health: {0}", self.game_state.player.health)

    # Show player input
    x, y = self.text_display(10, y, "Player inputs:")
    for k, v in self.game_state.key.items():
      x, y = self.text_display(10, y, "     {0}: {1}",k,v) 

    x, y = self.text_display(10, y, "Mouse X:{0} Y:{1}",*self.game_state.mouse)     
    # List object count
    x, y = self.text_display(10, y, "Game objects: {0}", len(self.game_state.object.list))
    # x, y  = self.text_display(10,y, "Object count: \n{0}", pprint.pformat(self.game_state.count, indent=5))
    for k, v in self.game_state.count.items():
      x, y = self.text_display(10, y, "     {0}: {1}",k,v) 



    # Draw box around game objects
    for game_obj in self.game_state.object.list:
      if getattr(game_obj, 'rect', None):
        pygame.draw.rect(self.surface,self.text_color, game_obj.rect, 2)
 
    # Make surface transparent and copy unto display surface
    self.surface.set_colorkey((0,0,0))
    self.surface.set_alpha(150)
    screen_surface.blit(self.surface, self.rect)


   