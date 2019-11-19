"""============================================================================

    Next_level

============================================================================"""
import pygame

from game_objects import story
from game_objects import globals
from game_objects import end_game

def NextLevel(level = False):
  if( level ):
    globals.game.level = level
  else:
    globals.game.level += 1

  if globals.game.level < len(story.board):
    globals.game.object.list = []
    for obj in story.board[globals.game.level]:
        for object_type, parameters in obj.items():
            globals.game.object.add(object_type, parameters)

    globals.game.level_time = pygame.time.get_ticks() 

  else:
    end_game.EndGame()
    globals.game.end_game = True  
