"""============================================================================
Sideways arcade space game

Main

The basics of the program, is that eash object that is active
    - paint it self on the shadow screen
    - move it self
    - does something when coliding with other objects

The main loop makes sure alle active objets paint, move and hit functions is called, at the appropriate time, player input is acted upon, and that the shadow screen is fliped at regular intervals


============================================================================"""
# Import python modules
import pygame

import time

# Import game classes
from include import alien
from include import bomb
from include import background
from include import city
from include import common
from include import dashboard
from include import player
from include import player_input
from include import setting
from include import shot
from include import globals


class Game:
  def __init__(self):
    # Game objects
    self.alien = []
    self.alien_shot = []
    self.background = []
    self.bomb = []
    self.city = []
    self.player = []
    self.player_shot = []

    self.all_objects = dict(
      alien = self.alien,
      alien_shot = self.alien_shot, 
      background = self.background,  
      bomb = self.bomb, 
      city = self.city, 
      player = self.player, 
      player_shot = self.player_shot, 
    )
    self.dashboard = None
    self.max_duration = 0
    self.player_input = player_input.PlayerInput()
    self.game_speed = 1

  def new(self):
    self.window = pygame.display.set_mode(
      (
        setting.screen_width,
        setting.screen_height
      )
    )
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Alien Attack')

    if( setting.game_speed < 100 or setting.game_speed > 0 ):
      self.game_speed = setting.game_speed
    

    self.dashboard = dashboard.Dashboard()

    # Create all game objects that are active when the game starts

    self.background.append(background.Background())
    self.player.append(player.Player(setting.player_start_position))

    city_distance = self.window.get_width() // (setting.number_of_cities + 1)
    for city_number in range(setting.number_of_cities):
      new_city = city.City()
      left = (city_number + 1) * city_distance - new_city.cityImage.get_width() / 2
      rect = new_city.cityImage.get_rect(bottomleft=(left, game.window.get_height()))
      new_city.set_rect(rect)
      self.city.append(new_city)

    self.alien.append(alien.Alien(1.0))

    # yt
    self.player_has_fired = False



  def __del__(self):
    pygame.display.quit()
    pygame.quit()



def paint_screen(window, start_ticks):
    ticks = pygame.time.get_ticks()-start_ticks
"""    
    if ticks < 1000 and ticks > 0:
        remainder = ticks % 3
        if remainder == 0:
            window.fill(black)
        elif remainder == 1:
            window.fill(white)
        elif remainder == 2:
            window.fill(lilla)
    else:
        window.fill((0,0,0))
    if game_state.player.alive:  
        window.blit(game_state.player.playerImage, game_state.player.rect)
    if game_state.alien.alive:
        window.blit(game_state.alien.alienImage, game_state.alien.rect)
    for shot in game_state.player_shot:
        window.blit(game_state.player.playerShotImage, shot.rect)
    for city in game_state.city:
        window.blit(city.cityImage, city.rect)
    for bomb in game_state.bomb:
        window.blit(bomb.enemyBomb, bomb.rect)
    for shot in game_state.alien_shot:
        window.blit(game_state.alien.alienhotImage, shot.rect)
    window.blit(game_state.player.crosshairImage, 
        game_state.player.crosshairImage.get_rect(center=pygame.mouse.get_pos()))
    window.blit(game_state.statusDisplay.text, game_state.statusDisplay.textRect)
    pygame.display.flip()
  """

def main_loop():
  frame_start_time = 0

  while not game.player_input.stop:
    # Time frame update and game speed
    now = pygame.time.get_ticks()
    time_lapsed = now - frame_start_time
    frame_start_time = now
    interval = 1000 // ( setting.frame_rate * game.game_speed )
    pause = interval - time_lapsed
    if( pause < 1 ):
      pause = 1
    elif( pause > 1000 ):
      pause = 1000    

    pygame.time.delay( pause )
    print(time_lapsed ,pause)

    # Get player input
    game.player_input.update()

    # move all objects
    for category in game.all_objects:
      for obj in game.all_objects[category]:
        if callable(getattr(obj, 'move', None)):
          obj.move()

    # claculate collissions
    # paint background
    # paint all objects

    for category in game.all_objects:
      for obj in game.all_objects[category]:
        if callable(getattr(obj, 'paint', None)):
          obj.paint()

    # paint dashboard
    dashboard.update()


    #game_state.alien.stone_dead = True
    pygame.display.flip()

 

# Start a new game
globals.setting = setting = setting.Setting() 
globals.game = game = Game()
game.new()
dashboard = dashboard.Dashboard()
main_loop()
del game


"""
class GameState:

    def update(self, player_input):
        self.player.move(player_input)
        if self.player.alive and len(self.city) > 0:
            duration = pygame.time.get_ticks()
            self.max_duration = duration
            self.statusDisplay.display_time('%.2f' % (float(duration) / 1000), False)
        else:
            self.statusDisplay.display_time('%.2f' % (float(self.max_duration) / 1000), True)
            


        if self.city and random.randint(1, 1000) > 999:
            x = random.randint(0, window.get_width())
            y = 0
            pos = (x, y)
            target = random.choice(self.city).rect.midbottom
            velocity = random.uniform(0.1, 0.5)
            velocity_x = calculate_x_velocity(pos, target, velocity)
            velocity_y = calculate_y_velocity(pos, target, velocity)
            new_bomb = Bomb(pos, velocity_x, velocity_y)
            self.bomb.append(new_bomb)

        for bomb in self.bomb:
            bomb.move()

        self.alien.move()
        self.alien.maybe_shoot(self.player, self.alien_shot)
        for shot in list(self.player_shot):
            shot.move()
            if not shot.rect.colliderect(window.get_rect()):
                self.player_shot.remove(shot)

        for shot in list(self.alien_shot):
            shot.move() 

        for shot in self.alien_shot:
            if shot.rect.colliderect(self.player.rect):
                self.player.hit()       

        for shot in list(self.player_shot):
            if self.alien.rect.colliderect(shot.rect):
                self.alien.hit()      

        for bomb in list(self.bomb):
            for shot in self.player_shot:
                if bomb.rect.colliderect(shot.rect):
                    self.bomb.remove(bomb)

        for bomb in list(self.bomb):
            for city in list(self.city):
                if bomb.rect.colliderect(city.rect):
                    self.city.remove(city)
                    self.bomb.remove(bomb)
            if bomb.rect.colliderect(self.player.rect) and self.player.alive:
                self.player.hit()
                self.bomb.remove(bomb)                

        if player_input.fire and not self.player_has_fired and len(self.player_shot) < 3 and self.player.alive:
            self.player_has_fired = True
            self.add_shot()
        if not player_input.fire:
            self.player_has_fired = False

    def add_shot(self):
        pos = self.player.rect.center
        new_shot_rect = self.player.playerShotImage.get_rect(center=pos)
        target = pygame.mouse.get_pos()
        velocity = 1.5
        velocity_x = calculate_x_velocity(pos, target, velocity)
        velocity_y = calculate_y_velocity(pos, target, velocity)
        new_shot = Shot(new_shot_rect, velocity_x, velocity_y)
        self.player_shot.append(new_shot)


"""