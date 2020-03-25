"""============================================================================

  Global variables

============================================================================"""import sys

# Set some global variables
class Global: 
    root_path     = os.path.join(os.path.dirname(__file__))    # Root of this package
    qt_path       = os.path.join(root_path,'qt')               # root of QT application files
    game_obj_path = os.path.join(root_path,'game_objects')     # Game program objects
    html_path     = os.path.join(root_path,'qt','html')        # QT HTML pages
    gfx_path      = os.path.join(root_path,'gfx')              # Graphic art and sprites
    sound_path    = os.path.join(root_path,'sound')            # sound effects and music
    screen_width  = 1000
    screen_height = 700
    window        = None
    app           = None