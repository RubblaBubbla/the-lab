# TODO - Rene dialogue

# Conversation tracking
init python:
    met_rudy = 0
    met_rene = 0
    met_sylvia = 0
    met_tau = 0
    seen_mother = 0


# Player can click on each character sprite to get an introductory dialogue
screen meet_and_greet():
    # Tau
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not met_tau):
             action Jump("meet_tau")
        elif (met_tau == 1):
            action Jump("greet_tau")
        else:
            action Jump("greet_tau_2")

    # Sylvia
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not met_sylvia):
             action Jump("meet_sylvia")
        elif (met_sylvia == 1):
            action Jump("greet_sylvia")
        else:
            action Jump("greet_sylvia_2")

    # Rudy
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not met_rudy):
             action Jump("meet_rudy")
        elif (met_rudy == 1):
            action Jump("greet_rudy")
        else:
            action Jump("greet_rudy_2")

    # Rene
    # imagebutton:
    #     xanchor 0.5
    #     yanchor 0.5
    #     xpos 0.25
    #     ypos 0.75
    #     idle "full_body.png"
    #     hover "full_body.png"
    #     if (not met_rene):
    #          action Jump("meet_rene")
    #     elif (met_rene == 1):
    #         action Jump("greet_rene")
    #     else:
    #         action Jump("greet_rene_2")

    # Mother
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.75
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not seen_mother):
             action Jump("check_mother")
        elif (seen_mother == 1):
            action Jump("check_mother_2")
        else:
            action Jump("check_mother_3")


# Scene that calls meet and greet screen
define meet_and_greet_fade = Fade(1, 0, 1)
label meet_and_greet:
    # Go to mother's introduction if all have been met
    if (met_rudy > 1 and met_tau > 1 and met_sylvia > 1):
        jump mother_introduction # a0_02

    scene bg central_area

    pause 0.5
    e "{i}Who should I talk with?{/i}"
    pause 0.5

    call screen meet_and_greet
    with meet_and_greet_fade


# Tau introduction
label meet_tau:
    e "Hi! It’s nice to meet you."
    
    u_t "…"
    
    u_t "…!"
    
    # Tau smiles
    
    e "What’s your name?"
    
    u_t "Nooo… menclature?"
    
    # Tau looks confused
    
    e "Your name? What should we call you?"
    
    u_t "1.618… 1.695…"
    
    # Tau looks intrigued by something. A little ‘ding’ plays
    
    u_t "Oh! Hehe…"
    
    # Tau’s sprite fades and footsteps play
    
    # A few taps of finger on glass
    
    e "{i}They’re really, really interested in those glass tubes we came out of…{/i}"
    
    e "{i}I should let them be for now.{/i}"
    
    $ met_tau = 1

    jump meet_and_greet

# Tau follow up 1
label greet_tau:
    e "{i}Are they playing with the water…?{/i}"
    
    e "Hi again! Did you find out anything about the tubes?"
    
    u_t "… Eta… double… V…"
    
    u_t "D… Why?"
    
    e "Why what?"
    
    u_t "… 7… 6… 1…"
    
    # Tau looks overjoyed
    
    u_t "… Ohhh! Water!"
    
    e "Yes! Water!"
    
    e "{i}I guess they really like water.{/i}"
    
    u_t "Water!!!"
    
    # Punchy sound, just to signify quick movement. Tau’s raising up their wet hands to show them to Eva.
    
    e "Ah! Careful, I don’t have another change of clothes!"
    
    $ met_tau = 2

    jump meet_and_greet


# Tau follow up final
label greet_tau_2:
    e "{i}Interrupting their bath would be kind of rude…{/i}"

    jump meet_and_greet


# Rudy introduction
label meet_rudy:
    e "It sounds to me like you know these people."
    
    e "Would you please explain?"
    
    u_ru "…"
    
    u_ru "No."
    
    u_ru "… I think I understand what’s going on. But you should figure it out for yourself."
    
    e "Oh… Okay. I’ll try my best."
    
    e "{i}At least that confirms he’s less confused than me?{/i}"
    
    $ met_rudy = 1

    jump meet_and_greet


# Rudy follow up 1
label greet_rudy:
    u_ru "…"
    
    u_ru "… Have you realized it yet?"
    
    e "Not at all…"
    
    u_ru "Talk to me again when you do."
    
    e "{i}*sigh.*{/i}"
    
    $ met_rudy = 2

    jump meet_and_greet


# Rudy follow up final
label greet_rudy_2:
    e "{i}I still have no idea what’s going on. And he said I need to figure it out on my own…{/i}"

    jump meet_and_greet



# Sylvia introduction
label meet_sylvia:
    e "{i}She’s so elegant…{/i}"
    
    e "Hello!"
    
    u_s "…"
    
    # Sylvia looks confused
    
    e "…"
    
    e "{i}Maybe she needs a moment to take in her surroundings?{/i}"
    
    u_s "Excuse me, hello. I was spacing out."
    
    e "That’s fine, I’m still trying to figure out what’s going on, too."
    
    u_s "Waking up in an unknown place isn’t the only weird thing going on, either."
    
    e "What do you mean?"
    
    u_s "I’m still not so sure myself, it’s only a hunch. I’ll let you know once I have a clearer picture."
    
    $ met_sylvia = 1

    jump meet_and_greet


# Sylvia follow up 1
label greet_sylvia:
    e "{i}I don’t wanna pry, but I’m too curious…{/i}"
    
    e "What’s your hunch? Maybe I can help you figure things out."
    
    u_s "I just feel like this place is drastically different from every place I’ve ever been to before."
    
    e "Because it’s dreary and colorless…? Like a hospital?"
    
    u_s "No. It’s more of a weird… *vibe* it gives me."
    
    e "What kind of vibe?"
    
    u_s "I genuinely cannot describe it, that’s why I didn’t want to talk about it. Best not to overanalyze something as subjective as a feeling, right?"
    
    e "Right. I’m sorry."
    
    u_s "Don’t worry about it."
    
    $ met_sylvia = 2

    jump meet_and_greet


# Sylvia follow up final
label greet_sylvia_2:
    e "{i}She looks like she’s in deep thought…{/i}"
   
    e "{i}I shouldn’t annoy her more than I already have.{/i}"

    jump meet_and_greet


# Mother check 1
label check_mother:
    #Close up of figure in distance
    
    e "{i}There’s a person there…{/i}"
    
    e "{i}They’re not moving an inch.{/i}"
    
    e "{i}Maybe it’s just a mannequin put there to scare us?{/i}"
    
    e "{i}If that’s so, it’s not very scary…{/i}"
    
    e "{i}They could’ve put horns on it! Give it some glowy red eyes and BIG teeth!{/i}"
    
    e "{i}Haha, uhm…{/i}"
    
    # Mother’s sight shifts to look straight down at Eva
    
    e "{i}It’s not a mannequin. It’s staring back at me.{/i}"
    
    e "{i}Oh man…{/i}"
    
    $ seen_mother = 1

    jump meet_and_greet


# Mother check 2
label check_mother_2:
    e "{i}That person is still staring down at us…{/i}"
    
    e "{i}No. I should assume the best of them! Maybe this place only *looks* scary!{/i}"
    
    $ seen_mother = 2

    jump meet_and_greet


# Mother check final
label check_mother_3:
    e "..."

    jump meet_and_greet



