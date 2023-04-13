#--------------------------------------------------------------------
# Set defaults
#--------------------------------------------------------------------
define gui.text_font =              "TitilliumWeb-Regular.ttf"
define gui.name_text_font =         "TitilliumWeb-Regular.ttf"
define gui.interface_text_font =    "TitilliumWeb-Regular.ttf"


#--------------------------------------------------------------------
# Persistent initial values
#--------------------------------------------------------------------
init python:
    persistent.prologue_partner = None


#--------------------------------------------------------------------
# Set up the characters
#--------------------------------------------------------------------
define m =          Character("Mother", color="#880808")
define e =          Character("Eva", color="#abeae5")
define ru =         Character("Rudy", color="#229900")
define re =         Character("René", color="#c04141")
define t =          Character ("Tau", color="#a16ee7")
define s =          Character("Sylvia", color="#fff2cc")

define unknown =    Character("???")

define u_m =        Character("???", color="#880808")
define u_e =        Character("???", color="#abeae5")
define u_ru =       Character("???", color="#229900")
define u_re =       Character("???", color="#c04141")
define u_t =        Character ("???", color="#a16ee7")
define u_s =        Character("???", color="#fff2cc")


#--------------------------------------------------------------------
# Custom definitions
#--------------------------------------------------------------------
define fade_2s = Fade(2, 0, 2)
define white_flash = Fade(0.25, 0, 0.65, color="#ffffff")
define blackout_fade = Fade(0.5, 3, 0.5)


#--------------------------------------------------------------------
# Transforms
#--------------------------------------------------------------------
# Tilt character from start degrees (usually 0) to end degrees in time seconds
transform tilt(start, end, time):
    subpixel True 
    rotate start
    easein time rotate end
    pause time+1
    rotate end

# Character is zoomed slightly and flashes
transform bounce_flash(zoom1, zoom2):
    subpixel True 
    zoom zoom1 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    linear 0.10 zoom zoom2 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.3)*HueMatrix(0.0) 
    linear 0.10 zoom zoom1 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

# Same as bounce_flash but without the flash
# I'd call this jump, but renpy uses 'jump' for other important things
transform bounce(zoom1, zoom2):
    subpixel True 
    zoom zoom1  
    linear 0.10 zoom zoom2 
    linear 0.10 zoom zoom1 
    pause 0.3
    zoom zoom1 

# Rotates character on y axis from start degrees to end degrees in time seconds
transform turn(start, end, time):
    subpixel True        
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, start, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear time matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, end, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    pause time+0.1
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, end, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
