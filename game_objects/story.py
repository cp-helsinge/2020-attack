'''============================================================================

Storry borad for 800 x 600 screen resolution

'<class type>' : [(rect), (boundry rect), color, diresction, speed, ...]
============================================================================'''
import pygame
from pygame.locals import *


# bord level game objects
board = [ [None]] # Level 0 not used

# Level 1 =======================================================================
board.append([ 
  {'next_level'   : { 
    'image': 'next_level.png', 
    'intro_time': 0, 
    'intro_effect': 'slide_down', 
    'hold_time': 0, 
    'outtro_time': 1, 
    'outtro_effect': 'slide_down'
  }},  
  {'music'        : 'zeos_-_Photo_theme_Window_like.mp3'},
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky37.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'a1a1_rocket2.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png' },
  }},
  {'city'         : { 'rect': (10,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (190,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (370,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (550,580,80,80), 'image': 'city7.png' }},  
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (730,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (910,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png' }},
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
    'outtro_time': 2, 
    'outtro_effect': 'slide_down',
  }},  
  {'music'        : 'zeos_-_Photo_theme_Window_like.mp3'},
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky32.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'a1a1_rocket2.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png' },
  }},
  {'city'         : { 'rect': (10,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (190,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (370,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (550,580,80,80), 'image': 'city7.png' }},  
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (730,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (910,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png' }},
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

