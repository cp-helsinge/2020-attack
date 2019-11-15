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
  {'background'   : {
    'color'       : pygame.Color('dodgerblue1'),
    'image'       : 'sky37.jpg'
  }},
  {'player'       : {
    'rect'        : (500,500,80,80),
    'image'       : 'player10.png',
    'crosshair_image' : 'crosshair.png',
    'boundary'    : (0,500,1000,80),
    'speed'       :  10,
    'sound'       : 'big_bang.wav',
    'shoot_sound' : 'shoot_sound.wav',
    'shot'        : { 'rect': (0,0,10,10), 'direction': 90, 'speed': 5, 'image': 'shot.png' },
  }},
  {'city'         : { 'rect': (100,580,80,80), 'image': 'city7.png'  }},
  {'city'         : { 'rect': (280,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (460,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (640,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (820,580,80,80), 'image': 'city7.png' }},
  {'city'         : { 'rect': (1000,580,80,80), 'image': 'city7.png' }},
  {'alien'        : {
    'rect'        : (800,30,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,30,1000,60),
    'speed'       : 5,
    'direction'   : 180,
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav'
  }},    
  {'alien'        : {
    'rect'        : (100,90,100,50),
    'image'       : 'alien8.png',
    'boundary'    : (0,90,1000,60),
    'speed'       : 5,
    'direction'   : 180,
    'sound'       : 'small_bang.wav',
    'shoot_sound' : 'small_shoot_sound.wav'
  }},
])

# Level 2 =======================================================================
board.append([
  {'background' : ['sky1.jpg']},
  {'player'     : [(200,150),0]},
  {'city'       : [(30,700)]},
  {'city'       : [(130,700)]},
  {'city'       : [(230,700)]},
  {'city'       : [(330,700)]},
  {'city'       : [(430,700)]},
  {'alien'      : [(0,50),1]},
])

