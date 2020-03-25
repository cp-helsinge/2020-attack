
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


