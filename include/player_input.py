"""============================================================================

  Palyer input

============================================================================"""
import pygame

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