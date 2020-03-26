"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame

# Settings
background_color = (16,64,96)
color = (192,128,0)
font_name = 'freesansbold.ttf'
  
# Dashboard
# Depending on child class using helth, score and level variables
class Dashboard:
  def __init__(self, game_state):
    # Store referance to game state
    self.game_state = game_state

    # Set dashboard dimensions
    height = self.game_state.screen_height // 15
    self.rect = pygame.Rect(0, game_state.screen_height - height, game_state.screen_width, height)

    # Create a background image template
    self.surface = pygame.Surface((self.rect.width, self.rect.height))

    # Paint background
    self.surface.fill(background_color)

    # Paint health in the center of the dashboard
    w = self.rect.width // 5    # Width
    h = self.rect.height // 2   # Height
    cx = self.rect.width // 2   # Center x 
    cy = h                      # Center y
    bw = 2                      # border line width
    
    # Draw health bar inner background
    pygame.draw.polygon(
      self.surface,
      color,
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

    # Draw health bar outer background
    pygame.draw.polygon(
     self.surface,
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
 
    # Define a rectangle that contains the actual health bar
    self.health_bar_rect = pygame.Rect((cx - w//2 + 2* bw, cy - h//2 - 2 * bw, w - 4 * bw, h - 4 * bw) )
    self.health_bar_rect.center = self.rect.center

    # Create a font 
    self.font = pygame.font.Font( font_name, int(height * 0.8) )
 
  def draw(self, surface):
    # Paint background
    surface.blit( self.surface, self.rect )

    # Paint Score in left middle of dashboard
    text = self.font.render(" Score: " + str(self.game_state.score), True, color)
    text_rect = text.get_rect()
    text_rect.midleft = self.rect.midleft 
    surface.blit( text, text_rect )

    # Paint health in the center of the dashboard
    if self.game_state.player.health > 0:
      hb_rect = pygame.Rect(self.health_bar_rect)
      hb_rect.width = (self.health_bar_rect.width * min(self.game_state.player.health, 100)) // 100 
      pygame.draw.rect(surface,(255,10,10),hb_rect)
 
    # Paint level middle right of dashboard
    text = self.font.render(
      "Level: " + str(self.game_state.level) +" ",
      True, 
      color
    )
    text_rect = text.get_rect()
    text_rect.midright = self.rect.midright 
    surface.blit( text, text_rect )

   