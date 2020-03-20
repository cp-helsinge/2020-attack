"""============================================================================

Animate

Loads an animation series (or just a still) and creates a pygame surface for it.

Animations are a collection of images, displayed with a given frame rate.
The images can be separate files, named so that only index numbers differ, or
a single image, containing multible frames within

parameters:
  name:       name of image file to load. if the file name contains "{index}"
              it is replaced with an index number, starting with 0. 

* frame_size: the rectangle (width, height) of the first frame within the image.
              frames are then picked out, from left to right, top to bottom order

* size:       Images are scaled to size if specified and rect variable is set 
              to the given position.

* frame_rate: number of images shown pr. second. If omitted, it is assumed that
              the whole series of images represents 1 second of animation

* loop:       The number of loop to perform. 
                 0 = using first image in the series as a still image. 
                 1 = animating the series one time, and ends with the last one
                -1 = loop forever
                n > 1 = number of loops performed, ending with the last image.

* = optional

This class can be used for images, that are not part of an animation. Just 
ommit the text "{index}" in the filename and the frame_size parameter.

============================================================================"""
import os
import pygame
from game_functions import globals

class Animation:
  def __init__(self, name, frame_size = None, size = None, frame_rate = None, loop = -1):
    self.file_name = os.path.join(os.getcwd(),globals.gfx_path, name)
   
    if frame_size is None and size is not None:
      frame_size =  size
    if size is None and frame_size is not None:
      size =  frame_size

    self.frame_size = frame_size
    self.size = size
    self.frame_rate = frame_rate
    self.loop = loop

    self.collection = []
    self.frames = 0
    self.current_frame = 0
    self.frame_time = 0
      
    # Load multiple image files as frames 
    if "{index}" in name: 
      self.collection = self.__load_image_sequence(self.file_name)

    # Load a single image file 
    else:
      try:
        image = pygame.image.load(self.file_name).convert_alpha()

      # If failing to load image file, create a default image
      except Exception as error:
        print(error, self.file_name, "Using default image")
        image = self.__default_image(self.rect)

      # split sprite map image into frames
      self.collection = self.__load_sprite_map(image)

    # Set meta data
    self.frames = len(self.collection)
    if self.frames > 0:
      # Set animation size 
      if size is None:
        if frame_size is None:
          self.size = pygame.Rect(self.collection[0].get_rect()).size
          self.frame_size = self.size
        else:
          self.size = frame_size

      # Set default frame rate to all frames in one second   
      if frame_rate is None: 
        self.frame_rate = self.frames


  # Load one or multiple image files as frames
  def __load_image_sequence(self, name):
    frame_list = []
    index = 0
    done = False
    while not done:
      
      try:
        image = pygame.image.load(self.file_name.format(index = index)).convert_alpha()
        if silf.size is not None:
          image = pygame.transform.smoothscale(image, self.size)
      except Exception as error:
        if index <= 0:
          print(error, self.file_name.format(index = self.frames), "not loaded")
          image = self.__default_image(self.rect)
        done = True

      frame_list.append(image)
      index += 1

    return frame_list


  # Load one image and split it into frames (Sprite map)
  def __load_sprite_map(self, image):
    frame_list = []
    rect = image.get_rect()
    if self.frame_size is None:
      cols = 1
      rows = 1
    else:
      cols = rect.width // self.frame_size[0]
      rows = rect.height // self.frame_size[1]

    for row in range(rows):
      for col in range(cols):
        # Mark positions of frame in map
        x = self.frame_size[0] * col 
        y = self.frame_size[1] * row 

        # Create a surface to hold the clip and cut it out
        clip = pygame.Surface(self.frame_size, pygame.SRCALPHA)
        clip.blit(image, (0,0), pygame.Rect((x,y),self.frame_size))
        
        # Scale clip and append it to the frame list
        if self.size is not None:
          clip = pygame.transform.smoothscale(clip, self.size)
        frame_list.append(clip)

    return frame_list

  # Create an image, with a rectangle arround and a cross in it
  def __default_image(self, rect):
    if self.size is None:
      self.size = (100,100)
    image = pygame.Surface(self.size)
    pygame.draw.rect(image, (200,0,0), ((0, 0), self.size), 2)
    pygame.draw.line(image, (200,0,0), (0,0) , self.size, 2)
    pygame.draw.line(image, (200,0,0), (0,self.size[1]) , (self.size[0], 0), 2)
    return image
  
  # return a pointer to the current surface frame of this animation
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

class Sound:
  def __init__(self, file_name):
    if not pygame.mixer.get_init():
      print("Failed to use pygame mixer")

    try:
      self = pygame.mixer.Sound(os.path.join(globals.sound_path, name) )
    except:
      print("Failed to use pygame mixer")
    
class Music:
  def __init__(self, file_name):
    try:
      pygame.mixer.music.load(os.path.join(globals.sound_path, name))
    except Exception as ex:
      print("failed to load music",ex, "using sound file:", file_name)

# Return true at random, on avarage at <freq> times pr. second
def random_frequency(freq):
  return random.randint(0, setting.frame_rate // (freq * globals.game.game_speed) ) == 0