# Set default font
define gui.text_font =              "TitilliumWeb-Regular.ttf"
define gui.name_text_font =         "TitilliumWeb-Regular.ttf"
define gui.interface_text_font =    "TitilliumWeb-Regular.ttf"


# Set up the characters
define m =          Character("Mother", color="red")
define e =          Character("Eva", color="#abeae5")
define ru =         Character("Rudy", color="#229900")
define re =         Character("René", color="#c04141")
define t =          Character ("Tau", color="#a16ee7")
define s =          Character("Sylvia", color="#fff2cc")

define unknown =    Character("???")

define u_m =        Character("???", color="red")
define u_e =        Character("???", color="#abeae5")
define u_ru =       Character("???", color="#229900")
define u_re =       Character("???", color="#c04141")
define u_t =        Character ("???", color="#a16ee7")
define u_s =        Character("???", color="#fff2cc")


# Custom definitions
define fade_2s = Fade(2, 0, 2)
define white_flash = Fade(0.25, 0, 0.65, color="#ffffff")
define blackout_fade = Fade(0.5, 3, 0.5)


# Persistent initial values
init python:
    persistent.prologue_partner = None