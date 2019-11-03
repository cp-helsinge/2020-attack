'''============================================================================

Storry borad for 800 x 600 screen resolution

'<class type>' : [(rect), (boundry rect), color, diresction, speed, ...]
============================================================================'''
import pygame
from pygame.locals import *


# bord level game objects
board = [
  [], # Level 0 not used
  [ # Level 1
    {'background' : {
      'color' : pygame.Color('dodgerblue1'),
      'image' : 'sky32.jpg'
    }},
    {'player'     : {
      'rect': (200,150,50,50),
      'image' : 'player.png',
      'crosshair_image.png' : 'crosshair.png'
      'boundary' : (0,550,800,100),
      'speed':    :2,
      'axix' :    : 'x',
      'sound' : 'big_bang.wav'
      'shoot_sound' : 'shoot_sound.wav'
    }},
    {'city'       : { 'rect' : (30,700,50,50), 'image' : 'city.png'  }},
    {'city'       : { 'rect' : (130,700,50,50), 'image' : 'city.png' }},
    {'city'       : { 'rect' : (230,700,50,50), 'image' : 'city.png' }},
    {'city'       : { 'rect' : (330,700,50,50), 'image' : 'city.png' }},
    {'city'       : { 'rect' : (430,700,50,50), 'image' : 'city.png' }},
    {'city'       : { 'rect' : (530,700,50,50), 'image' : 'city.png' }},
    {'alien'      : {
      'rect': (750,0,50,50),
      'image' : 'alien.png',
      'boundary' : (0,0,800,100),
      'speed':    :2,
      'direction' : (-1,0),
      'axix' :    : 'x',
      'sound' : 'small_bang.wav'
      'shoot_sound' : 'small_shoot_sound.wav'

    }},
  ],  
  [ # Level 2
    {'background' : ['sky1.jpg']},
    {'player'     : [(200,150),0]},
    {'city'       : [(30,700)]},
    {'city'       : [(130,700)]},
    {'city'       : [(230,700)]},
    {'city'       : [(330,700)]},
    {'city'       : [(430,700)]},
    {'alien'      : [(0,50),1]},
  ],
]