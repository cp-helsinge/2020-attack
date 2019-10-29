import pygame
import math
import random

def calculate_x_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.cos(direction)

def calculate_y_velocity(position, target, velocity):
    direction = math.atan2(target[1] - position[1], target[0] - position[0])
    return velocity * math.sin(direction)

class PlayerInput:
    def __init__(self):
        self.stop = False
        self.left = False
        self.right = False
        self.fire = False

    def update(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                self.stop = True
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    self.left = True
                if e.key == pygame.K_d:
                    self.right = True
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    self.left = False
                if e.key == pygame.K_d:
                    self.right = False
        self.fire = pygame.mouse.get_pressed()[0]

class Player:
    def __init__(self, city):
        self.playerImage = pygame.image.load("gfx/player.png").convert_alpha()
        self.playerShotImage = pygame.image.load("gfx/shot.png").convert_alpha()
        self.crosshairImage = pygame.image.load("gfx/crosshair.png").convert_alpha()
        self.rect = self.playerImage.get_rect(bottomleft=(0, window.get_height() - city.get_height()))
        self.alive = True 
        self.shots = []
        self.player_has_fired = False

    def move(self, player_input):
        if player_input.left and self.rect.left > window.get_rect().left:
            self.rect.x = self.rect.x - 2
        if player_input.right and self.rect.right < window.get_rect().right:
            self.rect.x = self.rect.x + 2

        for shot in list(self.shots):
            shot.move()
            if not shot.rect.colliderect(window.get_rect()):
                self.shots.remove(shot)

        if not player_input.fire:
            self.player_has_fired = False

    def hit(self):
        self.alive = False

class Shot:
    def __init__(self, rect, x_speed, y_speed):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

class Alien:
    def __init__(self, speed_x):
        self.alienImage = pygame.image.load("gfx/alien.png").convert_alpha()
        self.alienShotImage = pygame.image.load("gfx/alien_shot.png").convert_alpha()
        self.crash_sound = pygame.mixer.Sound("sound/Flashbang-Kibblesbob-899170896.wav")
        self.rect = self.alienImage.get_rect(topright=(0,0))
        self.x = self.rect.x
        self.speed_x = speed_x
        self.bounds = window.get_rect()
        self.direction = 1
        self.has_been_hit = False
        self.alive = True
        self.stone_dead = False
        self.time_to_shoot = random.randint(100, 1000)

    def move(self):
        self.x = self.x + self.direction * self.speed_x
        self.rect.x = self.x
        if self.rect.right > self.bounds.right:
            self.direction = -1
        if self.rect.left < self.bounds.left:
            self.direction = 1

    def hit(self):
        self.alive = False
        self.has_been_hit = True

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

class City:
    def __init__(self):
        self.cityImage = pygame.image.load("gfx/grey_city.png").convert_alpha()

    def set_rect(self, rect):
        self.rect = rect

class Bomb:
    def __init__(self, pos, x_speed, y_speed):
        self.enemyBomb = pygame.image.load("gfx/enemy_bomb.png").convert_alpha()
        self.rect = self.enemyBomb.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

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

class GameState:
    def __init__(self):
        self.cities = []
        self.bombs = []
        self.player_shots = []
        self.alien_shots = []
        number_of_cities = 5
        self.max_duration = 0
        city_distance = window.get_width() // (number_of_cities + 1)
        for city_number in range(number_of_cities):
            new_city = City()
            left = (city_number + 1) * city_distance - new_city.cityImage.get_width() / 2
            rect = new_city.cityImage.get_rect(bottomleft=(left, window.get_height()))
            new_city.set_rect(rect)
            self.cities.append(new_city)
        self.player = Player(self.cities[0].cityImage)
        self.alien = Alien(1.0)
        self.player_has_fired = False
        self.statusDisplay = StatusDisplay()

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

def paint_screen(window, start_ticks):
    ticks = pygame.time.get_ticks()-start_ticks
    if ticks < 1000 and ticks > 0:
        remainder = ticks % 3
        if remainder == 0:
            window.fill(black)
        elif remainder == 1:
            window.fill(white)
        elif remainder == 2:
            window.fill(lilla)
    else:
        window.fill(black)
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

def main_loop():
    pygame.mouse.set_visible(False)
    start_ticks = 10000000
    while not player_input.stop:
        pygame.time.delay(5)
        player_input.update()
        game_state.update(player_input)
        if game_state.alien.has_been_hit and not game_state.alien.stone_dead:
            pygame.mixer.Sound.play(game_state.alien.crash_sound)
            start_ticks=pygame.time.get_ticks()
            game_state.alien.stone_dead = True
        paint_screen(window,start_ticks)
    pygame.display.quit()
    pygame.quit()

pygame.init()
black = (0,0,0)
white = (255, 255, 255)
lilla = (255, 0, 255)
green = (0, 255, 0)
blue = (0, 0, 128) 
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Alien Attack')
player_input = PlayerInput()
game_state = GameState()
main_loop()