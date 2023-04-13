# TODO - Rene dialogue

# Conversation tracking
init python:
    met_rudy = 0
    met_rene = 0
    met_sylvia = 0
    met_tau = 0
    seen_mother = 0


# Player can click on each character sprite to get an introductory dialogue
# Define zooms
transform meet_and_greet_sprite_zoom:
    zoom 0.75

transform meet_and_greet_tau_zoom_2:
    zoom 0.5

transform meet_and_greet_mother_zoom:
    zoom 0.3

screen meet_and_greet():
    # Tau
    imagebutton:
        xanchor 0.5
        yanchor 1.0

        if (not met_tau):
            at meet_and_greet_sprite_zoom
            xpos 0.25
            ypos 0.9
        else:
            at meet_and_greet_tau_zoom_2
            xpos 0.925
            ypos 0.8            

        idle "tau neutral.png"

        if (not met_tau):
             action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.meet_tau")
                ]
        elif (met_tau == 1):
            action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.greet_tau")
                ]
        else:
            action Jump("meet_and_greet.greet_tau_2")

    # Sylvia
    imagebutton:
        at meet_and_greet_sprite_zoom

        xanchor 0.5
        yanchor 1.0

        xpos 0.4
        ypos 0.9

        idle "sylvia neutral.png"

        if (not met_sylvia):
             action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.meet_sylvia")
                ]
        elif (met_sylvia == 1):
            action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.greet_sylvia")
                ]
        else:
            action Jump("meet_and_greet.greet_sylvia_2")

    # Rudy
    imagebutton:
        at meet_and_greet_sprite_zoom

        xanchor 0.5
        yanchor 1.0

        xpos 0.6
        ypos 0.9

        idle "rudy neutral.png"

        if (not met_rudy):
             action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.meet_rudy")
                ]
        elif (met_rudy == 1):
            action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.greet_rudy")
                ]
        else:
            action Jump("meet_and_greet.greet_rudy_2")

    # Rene
    imagebutton:
        at meet_and_greet_sprite_zoom

        xanchor 0.5
        yanchor 1.0

        xpos 0.8
        ypos 0.9

        idle "rene neutral.png"

        if (not met_rene):
             action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.meet_rene")
                ]
        elif (met_rene == 1):
            action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.greet_rene")
                ]
        else:
            action Jump("meet_and_greet.greet_rene_2")

    # Mother
    imagebutton:
        at meet_and_greet_mother_zoom

        xanchor 0.5
        yanchor 1.0

        xpos 0.75
        ypos 0.3

        idle "mother neutral.png"

        if (not seen_mother):
             action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.check_mother")
                ]
        elif (seen_mother == 1):
            action [
                Hide(screen="meet_and_greet", transition=fade),
                Jump("meet_and_greet.check_mother_2")
                ]
        else:
            action Jump("meet_and_greet.check_mother_3")


# Scene that calls meet and greet screen
define meet_and_greet_fade = Fade(1, 0, 1)
label meet_and_greet:
    # Go to mother's introduction if all have been met
    if (met_rudy > 1 and met_tau > 1 and met_sylvia > 1 and met_rene > 1):
        stop music fadeout 2.0

        jump mother_introduction # a0_02

    scene bg central_area
    with fade

    pause 0.3
    e "{i}Who should I talk with?{/i}"
    
    call screen meet_and_greet

    # pause 0.5
    # e "{i}Who should I talk with?{/i}"


# Tau introduction
label .meet_tau:  
    show tau neutral:
        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.4
    with dissolve

    e "Hi! It's nice to meet you."
    
    u_t "…"
    
    u_t "…!"
    
    # Tau smiles
    
    e "What's your name?"
    

    # Tau looks confused (rotation animation)
    show tau neutral at tilt(0, 10, 0.2)

    u_t "Nooo… menclature?"
    
    e "Your name? What should we call you?"
    
    # Tau rotates back to neutral
    show tau neutral at tilt(10, 0, 0.2)

    u_t "1.618… 1.695…"
    
    "..."

    # Tau looks intrigued by something. A little ‘ding' plays
    play sound "audio/ding.ogg"
    show tau neutral at bounce_flash(1.4, 1.45)

    u_t "Oh! Hehe…"

    pause 0.25

    # Tau's sprite fades and footsteps play
    hide tau
    with dissolve
    
    # A few taps of finger on glass
    
    e "{i}They're really, really interested in those glass tubes we came out of…{/i}"
    
    e "{i}I should let them be for now.{/i}"
    
    $ met_tau = 1

    jump meet_and_greet


# Tau follow up 1
label .greet_tau:
    show tau neutral:
        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.4
    with dissolve

    e "{i}Are they playing with the water…?{/i}"
    
    e "Hi again! Did you find out anything about the tubes?"

    # Tau tiltsin curiosity
    show tau neutral at tilt(0, 10, 0.2)
    
    u_t "… Eta… double… V…"
    
    u_t "D… Why?"
    
    e "Why what?"
    
    u_t "… 7… 6… 1…"
    
    # Tau returns to standing straight
    show tau neutral at tilt(10, 0, 0.2)

    u_t "… Ohhh! Water!"
    
    e "Yes! Water!"
    
    e "{i}I guess they really like water.{/i}"
    
    play sound "audio/splash_short.ogg"
    show tau neutral at bounce(1.4, 1.45)

    u_t "Water!!!"
    
    # Punchy sound, just to signify quick movement. Tau's raising up their wet hands to show them to Eva.
    
    e "Ah! Careful, I don't have another change of clothes!"
    
    $ met_tau = 2

    jump meet_and_greet


# Tau follow up final
label .greet_tau_2:
    e "{i}Interrupting their bath would be kind of rude…{/i}"

    jump meet_and_greet


# Rudy introduction
label .meet_rudy:
    show rudy neutral
    with dissolve

    e "It sounds to me like you know these people."
    
    e "Would you please explain?"
    
    u_ru "…"
    
    u_ru "No."
    
    u_ru "… I think I understand what's going on. But you should figure it out for yourself."
    
    e "Oh… Okay. I'll try my best."
    
    e "{i}At least that confirms he's less confused than me?{/i}"
    
    $ met_rudy = 1

    jump meet_and_greet


# Rudy follow up 1
label .greet_rudy:
    show rudy neutral
    with dissolve

    u_ru "…"
    
    u_ru "… Have you realized it yet?"
    
    e "Not at all…"
    
    u_ru "Talk to me again when you do."
    
    e "{i}*sigh.*{/i}"
    
    $ met_rudy = 2

    jump meet_and_greet


# Rudy follow up final
label .greet_rudy_2:
    e "{i}I still have no idea what's going on. And he said I need to figure it out on my own…{/i}"

    jump meet_and_greet


# Sylvia introduction
label .meet_sylvia:
    show sylvia neutral:
        subpixel True

        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.6

        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, -36.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with dissolve

    e "{i}She's so elegant…{/i}"
    
    e "Hello!"
    
    u_s "…"
    
    # Sylvia looks confused
    
    e "…"
    
    e "{i}Maybe she needs a moment to take in her surroundings?{/i}"

    # Sylvia turns toward player
    show sylvia neutral at turn(-36, 0, 0.34)
    
    u_s "Excuse me, hello. I was spacing out."
    
    e "That's fine, I'm still trying to figure out what's going on, too."
    
    u_s "Waking up in an unknown place isn't the only weird thing going on, either."
    
    e "What do you mean?"
    
    u_s "I'm still not so sure myself, it's only a hunch. I'll let you know once I have a clearer picture."
    
    $ met_sylvia = 1

    jump meet_and_greet


# Sylvia follow up 1
label .greet_sylvia:
    show sylvia neutral:
        subpixel True

        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.6
    with dissolve

    e "{i}I don't wanna pry, but I'm too curious…{/i}"
    
    e "What's your hunch? Maybe I can help you figure things out."
    
    u_s "I just feel like this place is drastically different from every place I've ever been to before."
    
    e "Because it's dreary and colorless…? Like a hospital?"
    
    u_s "No. It's more of a weird… *vibe* it gives me."
    
    e "What kind of vibe?"
    
    u_s "I genuinely cannot describe it, that's why I didn't want to talk about it. Best not to overanalyze something as subjective as a feeling, right?"
    
    e "Right. I'm sorry."
    
    u_s "Don't worry about it."
    
    $ met_sylvia = 2

    jump meet_and_greet


# Sylvia follow up final
label .greet_sylvia_2:
    e "{i}She looks like she's in deep thought…{/i}"
   
    e "{i}I shouldn't annoy her more than I already have.{/i}"

    jump meet_and_greet


# Rene introduction
label .meet_rene:
    show rene neutral
    with dissolve

    e "{i}This guy looks just like the first one I met. Are they siblings?{/i}"
    
    u_re "Hey Eva, how are you doing?"
    
    e "Wait, how do you know my name?!"
    
    u_re "The same reason I know your favorite food is plain bread, silly!"
    
    e "{i}Uh. That's not quite it. I really prefer it with strawberry jam.{/i}"
    
    u_re "Especially with strawberry jam!"
    
    e "Haha, yeah. Silly me!"
    
    e "{i}Dear God, please help me. I don't want anyone reading my mind but you.{/i}"

    $ met_rene = 1

    jump meet_and_greet


# Second time talking to Rene
label .greet_rene:
    show rene neutral
    with dissolve

    e "{i}There is no way he can actually read my mind, right?{/i}"
    
    e "{i}That must've been a coincidence.{/i}"
    
    e "{i}Let me try again.{/i}"

    e "Hey."
    
    u_re "Yo."
    
    e "Can you tell me what I'm thinking about right now?"
    
    e "{i}Seven. Seven. Seven.{/i}"
    
    u_re "Uhh… I don't really know."
    
    e "Haha. I knew it!"
    
    u_re "Knew what?"
    
    e "Nothing…"

    $ met_rene = 2

    jump meet_and_greet


# Rene follow up final
label .greet_rene_2:
    e "{i}CAN'T read my mind.{/i}"

    jump meet_and_greet

# Mother check 1
label .check_mother:
    #Close up of figure in distance
    
    e "{i}There's a person there…{/i}"
    
    e "{i}They're not moving an inch.{/i}"
    
    e "{i}Maybe it's just a mannequin put there to scare us?{/i}"
    
    e "{i}If that's so, it's not very scary…{/i}"
    
    e "{i}They could've put horns on it! Give it some glowy red eyes and BIG teeth!{/i}"
    
    e "{i}Haha, uhm…{/i}"
    
    # Mother's sight shifts to look straight down at Eva
    
    e "{i}It's not a mannequin. It's staring back at me.{/i}"
    
    e "{i}Oh man…{/i}"
    
    $ seen_mother = 1

    jump meet_and_greet


# Mother check 2
label .check_mother_2:
    e "{i}That person is still staring down at us…{/i}"
    
    e "{i}No. I should assume the best of them! Maybe this place only *looks* scary!{/i}"
    
    $ seen_mother = 2

    jump meet_and_greet


# Mother check final
label .check_mother_3:
    e "..."

    jump meet_and_greet



