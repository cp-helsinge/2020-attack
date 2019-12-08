'''============================================================================

Story board for 1200 x 800 screen resolution

Each level board consist of a list of objects, that occur on the level. 
Including background, player and all other objects that occur in the game, but 
also a next_level object, that plays, when the level is successfully completed.

A level board is a dictionary (Associative array) where the index is a class file 
name found in the game_objects directory, or one of the following pseudo 
classes:
next_level
background
music

An entry in the level board dictionary, has a class file name as index, and a 
dictionary of parameters to create that class object:

<class name> : {'rect': <rect>, 'boundry': <rect>, 'color': <color> ...}

Rhe function story.get_level(level) returns the level dictionary

============================================================================'''
import sys
import pygame
from pygame.locals import *
from game_objects import common
from game_objects import setting


def get_level(level):
    board = getattr(sys.modules[__name__], "Level" + str(level),False)
    if board:
        return board().objects
    else:
        return False

# Level 0 =====================================================================
# This level is not used. However the next_level effect will be played, before 
# the game begins.
class Level0:
  def __init__(self):
    self.objects = {}

# Level 1 =====================================================================
class Level1:
  def __init__(self):
    # Load resources
    music             = common.load_music('zeos_-_Photo_theme_Window_like.mp3')
    next_level_sound  = common.load_sound('level2.ogg')

    background_image  = common.load_image('sky2.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_image      = common.load_image('a1a1_rocket2.png',(500,500,80,80))
    player_shot_image = common.load_image('shot.png',(0,0,10,10))
    city_image        = common.load_image('city7.png',(10,580,80,80))
    alien_image       = common.load_image('alien8.png',(800,30,100,50))
    alien_bomb_image  = common.load_image('bomb.png',(0,0,40,40))
    alien_shot_image  = common.load_image('alien_shot.png')
    level1_image      = common.load_image('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound = common.load_sound('big_bang.wav')
    player_shot_sound = common.load_sound('shoot_sound.wav')
    city_dead_sound   = common.load_sound('city_explosion.wav')
    alien_dead_sound  = common.load_sound('small_bang.wav')
    alien_shot_sound  = common.load_sound('small_shoot_sound.wav')

    self.objects = [
      {'music': music},
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'image': background_image,
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'image'           : player_image,
        'boundary'        : (0,500,1000,80),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'image': player_shot_image, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (100,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (190,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (280,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (370,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (460,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (550,580,80,80),  'image': city_image, 'sound': city_dead_sound }},  
      {'city'         : { 'rect': (640,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (730,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (820,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (910,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (1000,580,80,80), 'image': city_image, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},    
      {'alien'        : {
        'rect'        : (100,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},
      {'next_level': { 
        'sound'         : next_level_sound,
        'image'         : level1_image,
        'intro_time'    : 2, 
        'intro_effect'  : 'slide_down', 
        'hold_time'     : 2, 
        'outtro_time'   : 1, 
        'outtro_effect' : 'slide_down'
      }},  
    ]

# Level 2 =====================================================================
class Level2:
  def __init__(self):
    # Load resources
    music             = common.load_music('Yul Anderson - unknown titel.ogg')
    next_level_sound  = common.load_sound('level3.ogg')

    background_image  = common.load_image('sky3.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_image      = common.load_image('a1a1_rocket2.png',(500,500,80,80))
    player_shot_image = common.load_image('shot.png',(0,0,10,10))
    city_image        = common.load_image('city7.png',(10,580,80,80))
    alien_image       = common.load_image('alien8.png',(800,30,100,50))
    alien_bomb_image  = common.load_image('bomb.png',(0,0,40,40))
    alien_shot_image  = common.load_image('alien_shot.png')
    level1_image      = common.load_image('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound = common.load_sound('big_bang.wav')
    player_shot_sound = common.load_sound('shoot_sound.wav')
    city_dead_sound   = common.load_sound('city_explosion.wav')
    alien_dead_sound  = common.load_sound('small_bang.wav')
    alien_shot_sound  = common.load_sound('small_shoot_sound.wav')

    self.objects = [
      {'music': music},
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'image': background_image,
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'image'           : player_image,
        'boundary'        : (0,500,1000,80),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'image': player_shot_image, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (100,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (190,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (280,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (370,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (460,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (550,580,80,80),  'image': city_image, 'sound': city_dead_sound }},  
      {'city'         : { 'rect': (640,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (730,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (820,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (910,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (1000,580,80,80), 'image': city_image, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},    
      {'alien'        : {
        'rect'        : (100,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},
      {'alien'        : {
        'rect'        : (500,90,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},    
      {'alien'        : {
        'rect'        : (300,90,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 5,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},
      {'next_level': { 
        'sound'         : next_level_sound,
        'image'         : level1_image,
        'intro_time'    : 2, 
        'intro_effect'  : 'slide_down', 
        'hold_time'     : 2, 
        'outtro_time'   : 1, 
        'outtro_effect' : 'slide_down'
      }},  
    ]

# Level 3 =====================================================================
class Level3:
  def __init__(self):
    # Load resources
    music             = common.load_music('Yul Anderson - Nightbird.ogg')

    background_image  = common.load_image('sky4.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_image      = common.load_image('a1a1_rocket2.png',(500,500,80,80))
    player_shot_image = common.load_image('shot.png',(0,0,10,10))
    city_image        = common.load_image('city7.png',(10,580,80,80))
    alien_image       = common.load_image('alien8.png',(800,30,100,50))
    alien_bomb_image  = common.load_image('bomb.png',(0,0,40,40))
    alien_shot_image  = common.load_image('alien_shot.png')
    level1_image      = common.load_image('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound = common.load_sound('big_bang.wav')
    player_shot_sound = common.load_sound('shoot_sound.wav')
    city_dead_sound   = common.load_sound('city_explosion.wav')
    alien_dead_sound  = common.load_sound('small_bang.wav')
    alien_shot_sound  = common.load_sound('small_shoot_sound.wav')

<<<<<<< HEAD
    self.objects = [
      {'music': music},
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'image': background_image,
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'image'           : player_image,
        'boundary'        : (0,500,1000,80),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'image': player_shot_image, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (100,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (190,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (280,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (370,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (460,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (550,580,80,80),  'image': city_image, 'sound': city_dead_sound }},  
      {'city'         : { 'rect': (640,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (730,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (820,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (910,580,80,80),  'image': city_image, 'sound': city_dead_sound }},
      {'city'         : { 'rect': (1000,580,80,80), 'image': city_image, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 2, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},    
      {'alien'        : {
        'rect'        : (100,30,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},
      {'alien'        : {
        'rect'        : (500,90,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},    
      {'alien'        : {
        'rect'        : (300,90,100,50),
        'image'       : alien_image,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': alien_bomb_image },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': alien_shot_image },
      }},
      {'next_level': { 
        'image'         : level1_image,
        'intro_time'    : 2, 
        'intro_effect'  : 'slide_down', 
        'hold_time'     : 2, 
        'outtro_time'   : 1, 
        'outtro_effect' : 'slide_down'
      }},  
    ]
=======
# bord level game objects
board = [ [None]] # Level 0 not used

# Level 1 =======================================================================
board.append([ 
  {'next_level'   : { 
    'image': 'level1.png', 
    'intro_time': 2, 
    'intro_effect': 'slide_down', 
    'hold_time': 2, 
    'outtro_time': 1, 
    'outtro_effect': 'slide_down'
  }},  
  {'music'        : 'zeos_-_Photo_theme_Window_like.mp3'},
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky2.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'a1a1_rocket2.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png', 'sound': 'shot.wav'},
  }},
  {'city'         : { 'rect': (10,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (190,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (370,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (550,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},  
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (730,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (910,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'alien'        : {
    'rect'        : (800,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 2,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3,  'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (100,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'image': 'alien_shot.png' },
  }},
])

# Level 2 =======================================================================
board.append([ 
  {'next_level'   : { 
    'image': 'next_level.png', 
    'intro_time': 2, 
    'intro_effect': 'slide_down', 
    'hold_time': 1, 
    'sound': 'level2.ogg',
    'outtro_time': 2, 
    'outtro_effect': 'slide_down',
  }},  
  {'music'        : 'Yul Anderson - unknown titel.ogg'},
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky3.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'a1a1_rocket2.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png', 'sound':'shot.wav' },
  }},
  {'city'         : { 'rect': (10,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (190,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (370,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (550,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},  
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (730,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (910,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'alien'        : {
    'rect'        : (200,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }}, 
  {'alien'        : {
    'rect'        : (800,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (600,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},       
  {'alien'        : {
    'rect'        : (100,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
    {'alien'        : {
    'rect'        : (300,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
    {'alien'        : {
    'rect'        : (500,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
  #{'next_level'         : { 'image': 'end_game.png', 'intro_time': 2, 'hold_time': -1, 'intro_effect': 'slide_down'}},
])

# Level 3 =======================================================================
board.append([ 
  {'next_level'   : { 
    'image': 'next_level.png', 
    'intro_time': 2, 
    'intro_effect': 'slide_down', 
    'hold_time': 1, 
    'sound': 'level3.ogg',
    'outtro_time': 2, 
    'outtro_effect': 'slide_down',
  }},  
  {'music'        : 'Yul Anderson - Nightbird.ogg'},
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky4.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'a1a1_rocket2.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png', 'sound':'shot.wav' },
  }},
  {'city'         : { 'rect': (10,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (190,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (370,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (550,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},  
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav'  }},
  {'city'         : { 'rect': (730,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (910,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png', 'sound': 'city_explosion.wav' }},
  {'alien'        : {
    'rect'        : (800,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (900,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (600,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (500,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (100,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (200,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},    
  {'alien'        : {
    'rect'        : (350,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
    {'alien'        : {
    'rect'        : (750,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
    {'alien'        : {
    'rect'        : (400,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,0,1000,200),
    'speed'       : 5,
    'direction'   : 180,
    'move_pattern': 'horisontal',
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav',
    'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'image': 'bomb.png' },
    'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 5, 'image': 'alien_shot.png' },
  }},
  #{'next_level'         : { 'image': 'end_game.png', 'intro_time': 2, 'hold_time': -1, 'intro_effect': 'slide_down'}},
])
>>>>>>> 234b4303137e1f5ab245a9a6e0dbfc3a5f68b3cb
