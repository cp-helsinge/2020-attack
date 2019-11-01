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
    {'background' : [pygame.Color('dodgerblue1')]},
    {'player'     : [(200,150,50,50),(0,150,800,100),0]},
    {'city'       : [(30,700,50,50)]},
    {'city'       : [(130,700,50,50)]},
    {'city'       : [(230,700,50,50)]},
    {'city'       : [(330,700,50,50)]},
    {'city'       : [(430,700,50,50)]},
    {'alien'      : [(0,50),1]},
  ],  
  [ # Level 2
    {'background' : [pygame.Color('darkblue')]},
    {'player'     : [(200,150),0]},
    {'city'       : [(30,700)]},
    {'city'       : [(130,700)]},
    {'city'       : [(230,700)]},
    {'city'       : [(330,700)]},
    {'city'       : [(430,700)]},
    {'alien'      : [(0,50),1]},
  ],
]