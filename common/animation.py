"""============================================================================

Animation

Loads an animation series (or just a still) and creates a pygame surface for it.

Animations are a collection of images, displayed with a given frame rate.
The images can be separate files, named so that only index numbers differ, or
a single image, containing multible frames within

parameters:
  name:       name of image file to load. if the file name contains "{index}"
              it is replaced with an index number, starting with 0. 

* rect:       Images are scaled to "rect" size if specified and rect variable 
              is set to the given position.

* frame_rate: number of images shown pr. second. If omitted, it is assumed that
              the whole series of images represents 1 second of animation

* loop:       The number of loop to perform. 
                 0 = using first image in the series as a still image. 
                 1 = animating the series one time, and ends with the last one
                -1 = loop forever
                n > 1 = number of loops performed, ending with the last image.

* frame_rect: the rectangle (width, height) of the first frame within the image.
              frames are then picked out, from left to right, top to bottom order

* = optional

This class can be used for images, that are not part of an animation. Just 
ommit the text "{index}" in the filename and the frame_rect parameter.

============================================================================"""
import os
import pygame
from common import globals

def tuple2rect(rect):
  if isinstance(rect, pygame.Rect):
    return rect

  if not isinstance(rect, tuple):
    raise ValueError('tuple2rect parameter is not a tuple')

  # convert width, height 
  if len(rect) == 2:
    return pygame.Rect((0,0,rect[0], rect[1]))

  else:
    return pygame.Rect(rect)

class Animate:
  def __init__(
    self, 
    name, 
    rect = False, 
    frame_rate = False,
    loop = -1,
    frame_rect = False
  ):
    self.name = os.path.join(os.getcwd(),globals.gfx_path, name)
    if rect:
      self.rect = tuple2rect(rect)
      
    self.frame_rate = frame_rate
    self.loop = loop
    sprite_map = False
    if frame_rect:
      sprite_map = True
      self.frame_rect = tuple2rect(frame_rect)
    self.collection = []
    self.frames = 0
    self.current_frame = 0
    self.frame_time = 0

    if "{index}" in name: 
      # Load one or multiple image files as frames
      self.collection = self.__load_image_sequence(self.name)

    else:
      try:
        # Load a single image file
        image = pygame.image.load(self.name).convert_alpha()

      except Exception as error:
        if not rect:
          self.rect = tuple2rect((0,0,100,100))
        print(error, self.name, "Using default image")
        image = self.__default_image(self.rect)

      if sprite_map:
        # split image into frames
        self.collection = self.__load_sprite_map(image)
      elif rect:  
        # Use as a single still image, and rescale it
        self.collection = [ pygame.transform.smoothscale(image, ( self.rect.width, self.rect.height )) ]
      else:  
        # Use as a single still image
        self.collection = [ image ]

    # Set meta data
    self.frames = len(self.collection)
    if self.frames > 0:
      # Set animation rect 
      if not rect:
        if frame_rect:
          self.rect = frame_rect
        else:
          self.rect = pygame.Rect(self.collection[0].get_rect(topleft=(0,0)))
      # Set frame rate    
      if not frame_rate: 
        self.frame_rate = self.frames


  # Load one or multiple image files as frames
  def __load_image_sequence(self, name):
    list = []
    index = 0
    done = False
    while not done:
      try:
        image = pygame.image.load(self.name.format(index = index)).convert_alpha()
        image = pygame.transform.smoothscale(image, ( self.rect[2], self.rect[3] ))
      except Exception as error:
        if index <= 0:
          print(error, self.name.format(index = self.frames), "not loaded")
          image = self.__default_image(self.rect)
        done = True
      list.append(image)
      index += 1
    return list


  # Load one image and split it into frames (Sprite map)
  def __load_sprite_map(self, image):
    list = []
    rect = image.get_rect()
    cols = rect.width // self.frame_rect.width 
    rows = rect.height // self.frame_rect.height 

    for row in range(0,rows):
      for col in range(0,cols):
        self.frame_rect.x = self.frame_rect.width * col 
        self.frame_rect.y = self.frame_rect.height * row 
        clip = pygame.Surface((self.frame_rect.width, self.frame_rect.height),pygame.SRCALPHA)
        clip.blit(image, (0,0), self.frame_rect)
        list.append(pygame.transform.smoothscale(clip, ( self.rect.width, self.rect.height )))
    return list

  # Create an image, with a rectangle arround and a cross in it
  def __default_image(self, rect):
    if not self.rect:
      self.rect = tuple2rect(0,0,100,100)
    image = pygame.Surface((self.rect.width, self.rect.height ))
    pygame.draw.rect(image, (200,0,0), (0, 0, self.rect.width, self.rect.height ), 2)
    pygame.draw.line(image, (200,0,0), (0,0) , (self.rect.width, self.rect.height), 2)
    pygame.draw.line(image, (200,0,0), (0,self.rect.height) , (self.rect.width, 0), 2)
    return image
  
  def get_surface(self):
    if self.frame_time < (pygame.time.get_ticks() - 1000  // self.frame_rate) :
      if not self.loop == 0: 
        if len(self.collection) -1  == self.current_frame: 
          if not self.loop == 0: 
            if self.loop > 0: self.loop -= 1
            self.current_frame = 0
            self.frame_time = pygame.time.get_ticks()
        else:    
          self.current_frame += 1
          self.frame_time = pygame.time.get_ticks()
    return self.collection[self.current_frame]

