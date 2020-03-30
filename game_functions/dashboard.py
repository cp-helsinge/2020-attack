"""============================================================================

  Dashboard
  
  Show game and player status

============================================================================"""
import pygame
from game_functions import animation

# Settings
background_color = (16,64,96)
color = (0,82,255)
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

    # Load dashboard animation
    self.sprite = animation.Animation("dashboard.png",(1000,50),self.rect.size,2,-1) 
    
    # Define a rectangle that contains the actual health bar
    self.health_bar_rect = pygame.Rect( (0,0), (self.rect.width // 5, height // 2) )
    self.health_bar_rect.center = self.rect.center

    # Create a font 
    self.font = pygame.font.Font( font_name, height // 2 )
 
  def draw(self, surface):
    # Paint background
    surface.fill(background_color, self.rect)

    # Paint health in the center of the dashboard
    if self.game_state.player.health > 0:
      hb_rect = pygame.Rect(self.health_bar_rect)
      hb_rect.width = (self.health_bar_rect.width * min(self.game_state.player.health, 100)) // 100 
      pygame.draw.rect(surface,(0,200,0),hb_rect)

    surface.blit(self.sprite.get_surface(), self.rect)

    # Score in left middle of dashboard
    text = self.font.render(" Score: " + str(self.game_state.score), True, color)
    text_rect = text.get_rect()
    text_rect.midleft = (self.rect.width // 60, self.rect.y + self.rect.height // 1.6) 
    surface.blit( text, text_rect )
 
    # Level at middle right of dashboard
    text = self.font.render(
      "Level: " + str(self.game_state.level) +" ",
      True, 
      color
    )
    text_rect = text.get_rect()
    text_rect.midright = (self.rect.width - self.rect.width // 60, self.rect.y + self.rect.height // 1.6) 
    surface.blit( text, text_rect )

   