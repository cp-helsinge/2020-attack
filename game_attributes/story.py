'''============================================================================

Story board

The story board is a list (Array) of levels. index is 0 - number of levels.

Each level consist of a list of game objects, that occur on that level. 
Including background, player, music etc. In short: all things that occur in 
that level of the game. 
It also might have a next_level object, that plays, when the level is 
successfully completed.

The game object list contains dictionaries (Associative arrays) That name and 
describe each game object, and its parameters.
Each game object has a member named 'class_name' all subsequent members are 
parameters, specific to that class.


============================================================================'''
#import sys
import pygame
#from pygame.locals import *

level = []

# Level 0 =====================================================================
# This level is not used. However the next_level effect will be played, before 
# the game begins.

level.append( [] )

# Level 1 =====================================================================
level.append([
  {'class_name': 'Player', 'position': (500,500), 'boundary': (0,300,1000,360)},
  {'class_name': 'Alien1', 'position': (800,30), 'boundary': (0,0,1000,300), 'speed': 5,'direction': 20},    
  {'class_name': 'Alien1', 'position': (100,90), 'boundary': (0,0,1000,300), 'speed': 5,'direction': 160},    
])

"""
{
  'class name': 'Next_level',
  'sound'         : 'level2.ogg',
  'sprite'         : 'level_sprite',
  'intro_time'    : 2, 
  'intro_effect'  : 'slide_down', 
  'hold_time'     : 2, 
  'outtro_time'   : 1, 
  'outtro_effect' : 'slide_down'
}, 
{'class name': 'Music', 'file name': 'Test1.ogg'},
{ 
  'class name': 'Background', 
  'color': pygame.Color('dodgerblue1'), 
  'sprite': 'sky2.jpg',
},
{'class_name': 'city', 'position': (  10,580), },
{'class_name': 'city', 'position': ( 100,580), },
{'class_name': 'city', 'position': ( 190,580), },
{'class_name': 'city', 'position': ( 280,580), },
{'class_name': 'city', 'position': ( 370,580), },
{'class_name': 'city', 'position': ( 460,580), },
{'class_name': 'city', 'position': ( 550,580), },
{'class_name': 'city', 'position': ( 640,580), },
{'class_name': 'city', 'position': ( 730,580), },
{'class_name': 'city', 'position': ( 820,580), },
{'class_name': 'city', 'position': ( 910,580), },
{'class_name': 'city', 'position': (1000,580), },
{'class_name': 'Player1', 'position': (500,500), 'boundary': (0,300,1000,360)},
"""

"""
# Level 2 =====================================================================
class Level2:
  def __init__(self):
    # Load resources
    music             = common.load_music('Test1.ogg')
    next_level_sound  = common.load_sound('level2.ogg')

    background_sprite  = animation.Animate('sky3.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_sprite      = animation.Animate('a1a1_rocket2.png',(500,500,80,80))
    player_shot_sprite = animation.Animate('shot.png',(0,0,10,10))
    city_sprite        = animation.Animate('city7.png',(10,580,80,80))
    alien_sprite        = animation.Animate("ufo2.png",(0,0,100,50),5,-1,(0,0,100,50))
    alien_bomb_sprite  = animation.Animate('bomb.png',(0,0,40,40))
    alien_shot_sprite  = animation.Animate('alien_shot.png')
    level_sprite       = animation.Animate('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound = common.load_sound('big_bang.wav')
    player_shot_sound = common.load_sound('shot.wav')
    city_dead_sound   = common.load_sound('city_explosion.wav')
    alien_dead_sound  = common.load_sound('small_bang.wav')
    alien_shot_sound  = common.load_sound('small_shoot_sound.wav')

    self.objects = [
      {'next_level': { 
        'sound'         : next_level_sound,
        'sprite'         : level_sprite,
        'intro_time'    : 2, 
        'intro_effect'  : 'slide_down', 
        'hold_time'     : 2, 
        'outtro_time'   : 1, 
        'outtro_effect' : 'slide_down'
      }}, 
      {'music': music},
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'sprite': background_sprite,
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'sprite'           : player_sprite,
        'boundary'        : (0,300,1000,360),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'sprite': player_shot_sprite, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (100,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (190,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (280,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (370,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (460,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (550,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},  
      {'city'         : { 'rect': (640,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (730,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (820,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (910,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (1000,580,80,80), 'sprite': city_sprite, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (200,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},    
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (600,90,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'sprite': alien_shot_sprite },
      }},    
      {'alien'        : {
        'rect'        : (100,90,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'sprite': alien_shot_sprite },
      }}, 
    ]

# Level 3 =====================================================================
class Level3:
  def __init__(self):
    # Load resources
    music             = common.load_music('Test1.ogg')
    next_level_sound  = common.load_sound('level3.ogg')

    background_sprite  = animation.Animate('sky4.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_sprite      = animation.Animate('a1a1_rocket2.png',(500,500,80,80))
    player_shot_sprite = animation.Animate('shot.png',(0,0,10,10))
    city_sprite        = animation.Animate('city7.png',(10,580,80,80))
    alien_sprite        = animation.Animate("ufo3.png",(0,0,100,50),5,-1,(0,0,100,50))
    alien_bomb_sprite  = animation.Animate('bomb.png',(0,0,40,40))
    alien_shot_sprite  = animation.Animate('alien_shot.png')
    level_sprite       = animation.Animate('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound = common.load_sound('big_bang.wav')
    player_shot_sound = common.load_sound('shot.wav')
    city_dead_sound   = common.load_sound('city_explosion.wav')
    alien_dead_sound  = common.load_sound('small_bang.wav')
    alien_shot_sound  = common.load_sound('small_shoot_sound.wav')

    self.objects = [
      {'next_level': { 
        'sound'         : next_level_sound,
        'sprite'         : level_sprite,
        'intro_time'    : 2, 
        'intro_effect'  : 'slide_down', 
        'hold_time'     : 2, 
        'outtro_time'   : 1, 
        'outtro_effect' : 'slide_down'
      }}, 
      {'music': music},
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'sprite': background_sprite,
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'sprite'           : player_sprite,
        'boundary'        : (0,300,1000,360),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'sprite': player_shot_sprite, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (100,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (190,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (280,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (370,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (460,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (550,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},  
      {'city'         : { 'rect': (640,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (730,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (820,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (910,580,80,80),  'sprite': city_sprite, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (1000,580,80,80), 'sprite': city_sprite, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 2, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},    
      {'alien'        : {
        'rect'        : (900,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (600,90,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},    
      {'alien'        : {
        'rect'        : (500,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (100,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (200,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (350,90,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (750,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},
      {'alien'        : {
        'rect'        : (400,90,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'sprite': alien_shot_sprite },
      }},    
    ]
"""