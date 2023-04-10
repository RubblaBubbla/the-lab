init python:
    spoke_with_rudy = False
    spoke_with_tau = False
    spoke_with_sylvia = False
    spoke_with_rene = False

    # If partner is Rudy:
        # Eva-Rudy
        # Rene-Sylvia
        # Tau

    # If partner is Tau:
        # Eva-Tau
        # Rene-Sylvia
        # Rudy

    # If partner is Sylvia:
        # Eva-Sylvia
        # Rene-Tau
        # Rudy

    # If partner is René:
        # Eva-René
        # Sylvia-Tau
        # Rudy


screen partner_choosing():
    
    # Tau
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_tau):
             action Jump("speak_with_tau")
        else:
            action Jump("ask_tau")

    # Sylvia
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_sylvia):
             action Jump("speak_with_sylvia")
        else:
            action Jump("ask_sylvia")

    # Rudy
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_rudy):
             action Jump("speak_with_rudy")
        else:
            action Jump("ask_rudy")

    # Rene
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_rene):
             action Jump("speak_with_rene")
        else:
            action Jump("ask_rene")


label partner_choosing:
    show bg central_area

    call screen partner_choosing


label speak_with_rudy:
    $ spoke_with_rudy = True

    e "What do you think of this?"

    ru "Nothing particularly special."

    e "Really? You seem like you're used to this sort of thing."

    ru "If you're here to ask about being partners, you should get to your point faster."

    e "{i}Oh man. Should I ask Rudy to be my partner?{/i}"

    menu:
        "Yes. Let's be partners.":
            jump rudy_yes 

        "I need to think about it more.":
            jump rudy_no


label ask_rudy:
    # Show Rudy sprite

    e "Should I ask Rudy to be my partner?"

    menu:
        "Will you be my partner, Rudy?":
            jump rudy_yes 

        "I need to think about it more.":
            jump partner_choosing


label rudy_yes:
    $ persistent.prologue_partner = "rudy"

    ru "Okay. I expect you'll give your best."

    jump conclude_choosing


label rudy_no:
    ru "Come back if you make a decision."

    jump partner_choosing


label speak_with_tau:
    $ spoke_with_tau = True
    
    # Dialogue

    menu:
        "Yes. Let's be partners.":
            jump tau_yes 

        "I need to think about it more.":
            jump tau_no


label ask_tau:
    # Show Tau sprite

    e "Should I ask Tau to be my partner?"

    menu:
        "Will you be my partner, Tau?":
            jump tau_yes 

        "I need to think about it more.":
            jump partner_choosing


label tau_yes:
    $ persistent.prologue_partner = "tau"

    # Tau response

    jump conclude_choosing


label tau_no:
    # Tau response

    jump partner_choosing


label speak_with_sylvia:
    $ spoke_with_sylvia = True

    # Dialogue

    menu:
        "Yes. Let's be partners.":
            jump sylvia_yes 

        "I need to think about it more.":
            jump sylvia_no


label ask_sylvia:
    # Show Sylvia sprite

    e "Should I ask Sylvia to be my partner?"

    menu:
        "Will you be my partner, Sylvia?":
            jump sylvia_yes 

        "I need to think about it more.":
            jump partner_choosing


label sylvia_yes:
    $ persistent.prologue_partner = "sylvia"

    # Sylvia response

    jump conclude_choosing


label sylvia_no:
    # Sylvia response

    jump partner_choosing


label speak_with_rene:
    $ spoke_with_rene = True

    # Dialogue

    menu:
        "Yes. Let's be partners.":
            jump rene_yes 

        "I need to think about it more.":
            jump rene_no


label ask_rene:
    # Show Rene sprite

    e "Should I ask René to be my partner?"

    menu:
        "Will you be my partner, René?":
            jump rene_yes 

        "I need to think about it more.":
            jump partner_choosing


label rene_yes:
    $ persistent.prologue_partner = "rene"

    # Rene response

    jump conclude_choosing


label rene_no:
    # Rene response

    jump partner_choosing


label conclude_choosing:
    "Choosing concluded."

    return
