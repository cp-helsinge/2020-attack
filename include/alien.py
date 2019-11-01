"""============================================================================

  Alien space ship

============================================================================"""
import pygame
import random
from include import globals


class Alien:
  def __init__(self, position, direction = 1, speed=1):
    self.alien_image = pygame.image.load(globals.gfx_path + "alien.png").convert_alpha()
    self.position = position

  def paint(self):
    globals.game.window.blit(self.alien_image,self.position)


"""
class Alien:
  def __init__(self, position, direction=1, speed=1):
    self.alienImage = pygame.image.load(globals.gfx_path + "alien.png").convert_alpha()
    self.alienShotImage = pygame.image.load(globals.gfx_path + "alien_shot.png").convert_alpha()
    self.crash_sound = pygame.mixer.Sound("sound/Flashbang-Kibblesbob-899170896.wav")
    self.rect = self.alienImage.get_rect(topright=(0,0))
    self.x = self.rect.x
    self.position = position
    self.speed = speed
    self.speed_x = 1
    self.direction = direction
    self.has_been_hit = False
    self.alive = True
    self.stone_dead = False
    self.time_to_shoot = random.randint(100, 1000)

  def move(self):
    self.bounds = globals.game.window.get_rect()
    self.x = self.x + self.direction * self.speed_x
    self.rect.x = self.x
    if self.rect.right > self.bounds.right:
      self.direction = -1
    if self.rect.left < self.bounds.left:
      self.direction = 1

  def hit(self):
    self.alive = False
    self.has_been_hit = True

  def paint(self):
    globals.game.window.blit(self.alienImage, self.position)


  def maybe_shoot(self, player, shot_list):
    self.time_to_shoot = self.time_to_shoot - 1
    if self.time_to_shoot <= 0 and player.alive and self.alive:
      self.time_to_shoot = random.randint(100, 1000)
      rect = self.alienShotImage.get_rect(center=self.rect.midbottom)
      speed = 1
      x_speed = calculate_x_velocity(self.rect.midbottom, player.rect.center, speed)
      y_speed = calculate_y_velocity(self.rect.midbottom, player.rect.center, speed)
      shot = Shot(rect, x_speed, y_speed)
      shot_list.append(shot)   

"""