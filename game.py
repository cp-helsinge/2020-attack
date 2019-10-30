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
from include import city
from include import common
from include import player
from include import player_input
from include import setting
from include import shot

setting = setting.Setting() 

class Game:
  def __init__(self):
    self.cities = []
    self.bombs = []
    self.player_shots = []
    self.alien_shots = []
    self.max_duration = 0
    self.window = None

  def new(self):
    self.window = pygame.display.set_mode(
      (
        setting.screen_width,
        setting.screen_height
      )
    )
    pygame.init()
    pygame.display.set_caption('Alien Attack')

    self.player_input = player_input.PlayerInput()
    #self.game_state = GameState()
    pygame.mouse.set_visible(False)
    self.speed = 1

    self.cities = []
    self.bombs = []
    self.player_shots = []
    self.alien_shots = []
    self.max_duration = 0

    # Create all game objects that are active when the game starts
    city_distance = self.window.get_width() // (setting.number_of_cities + 1)
    for city_number in range(setting.number_of_cities):
      new_city = city.City()
      left = (city_number + 1) * city_distance - new_city.cityImage.get_width() / 2
      rect = new_city.cityImage.get_rect(bottomleft=(left, game.window.get_height()))
      new_city.set_rect(rect)
      self.cities.append(new_city)

    self.player = player.Player((0, game.window.get_height() - new_city.cityImage.get_height()))
    self.alien = alien.Alien(1.0)

    # yt
    self.player_has_fired = False
    self.statusDisplay = StatusDisplay()


  def __del__(self):
    pygame.display.quit()
    pygame.quit()

class StatusDisplay:
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
    for shot in game_state.player_shots:
        window.blit(game_state.player.playerShotImage, shot.rect)
    for city in game_state.cities:
        window.blit(city.cityImage, city.rect)
    for bomb in game_state.bombs:
        window.blit(bomb.enemyBomb, bomb.rect)
    for shot in game_state.alien_shots:
        window.blit(game_state.alien.alienShotImage, shot.rect)
    window.blit(game_state.player.crosshairImage, 
        game_state.player.crosshairImage.get_rect(center=pygame.mouse.get_pos()))
    window.blit(game_state.statusDisplay.text, game_state.statusDisplay.textRect)
    pygame.display.flip()
  """

def main_loop():
  while not game.player_input.stop:
    pygame.time.delay(5)
    game.player_input.update()
    #game_state.update(player_input)
    #if game_state.alien.has_been_hit and not game_state.alien.stone_dead:
      #pygame.mixer.Sound.play(game_state.alien.crash_sound)
    start_ticks=pygame.time.get_ticks()
      #game_state.alien.stone_dead = True
    paint_screen(game.window,start_ticks)

game = Game()
game.new()
main_loop()
del game
"""
class GameState:

    def update(self, player_input):
        self.player.move(player_input)
        if self.player.alive and len(self.cities) > 0:
            duration = pygame.time.get_ticks()
            self.max_duration = duration
            self.statusDisplay.display_time('%.2f' % (float(duration) / 1000), False)
        else:
            self.statusDisplay.display_time('%.2f' % (float(self.max_duration) / 1000), True)
            


        if self.cities and random.randint(1, 1000) > 999:
            x = random.randint(0, window.get_width())
            y = 0
            pos = (x, y)
            target = random.choice(self.cities).rect.midbottom
            velocity = random.uniform(0.1, 0.5)
            velocity_x = calculate_x_velocity(pos, target, velocity)
            velocity_y = calculate_y_velocity(pos, target, velocity)
            new_bomb = Bomb(pos, velocity_x, velocity_y)
            self.bombs.append(new_bomb)

        for bomb in self.bombs:
            bomb.move()

        self.alien.move()
        self.alien.maybe_shoot(self.player, self.alien_shots)
        for shot in list(self.player_shots):
            shot.move()
            if not shot.rect.colliderect(window.get_rect()):
                self.player_shots.remove(shot)

        for shot in list(self.alien_shots):
            shot.move() 

        for shot in self.alien_shots:
            if shot.rect.colliderect(self.player.rect):
                self.player.hit()       

        for shot in list(self.player_shots):
            if self.alien.rect.colliderect(shot.rect):
                self.alien.hit()      

        for bomb in list(self.bombs):
            for shot in self.player_shots:
                if bomb.rect.colliderect(shot.rect):
                    self.bombs.remove(bomb)

        for bomb in list(self.bombs):
            for city in list(self.cities):
                if bomb.rect.colliderect(city.rect):
                    self.cities.remove(city)
                    self.bombs.remove(bomb)
            if bomb.rect.colliderect(self.player.rect) and self.player.alive:
                self.player.hit()
                self.bombs.remove(bomb)                

        if player_input.fire and not self.player_has_fired and len(self.player_shots) < 3 and self.player.alive:
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
        self.player_shots.append(new_shot)


"""