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
             action Jump("partner_choosing.speak_with_tau")
        else:
            action Jump("partner_choosing.ask_tau")

    # Sylvia
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_sylvia):
             action Jump("partner_choosing.speak_with_sylvia")
        else:
            action Jump("partner_choosing.ask_sylvia")

    # Rudy
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_rudy):
             action Jump("partner_choosing.speak_with_rudy")
        else:
            action Jump("partner_choosing.ask_rudy")

    # Rene
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.75
        idle "full_body.png"
        hover "full_body.png"
        if (not spoke_with_rene):
             action Jump("partner_choosing.speak_with_rene")
        else:
            action Jump("partner_choosing.ask_rene")


label partner_choosing:
    show bg central_area

    call screen partner_choosing


label .speak_with_rudy:
    $ spoke_with_rudy = True

    e "What do you think of this?"

    ru "Nothing particularly special."

    e "Really? You seem like you're used to this sort of thing."

    ru "If you're here to ask about being partners, you should get to your point faster."

    e "{i}Oh man. Should I ask Rudy to be my partner?{/i}"

    menu:
        "Yes":
            jump .rudy_yes 

        "I need to think about it more.":
            jump .rudy_no


label .ask_rudy:
    # Show Rudy sprite

    e "Should I ask Rudy to be my partner?"

    menu:
        "Yes":
            jump .rudy_yes 

        "I need to think about it more.":
            jump partner_choosing


label .rudy_yes:
    $ persistent.prologue_partner = "rudy"

    ru "Okay. I expect you'll give your best."

    jump .conclude_choosing


label .rudy_no:
    ru "Come back if you make a decision."

    jump partner_choosing


label .speak_with_tau:
    $ spoke_with_tau = True
    
    e "Hey, Tau."
    
    t "Evaaa! Hi!"
    
    e "Hello!"
    
    e "{i}I don't know how to talk to them, they're… odd.{/i}"
    
    e "Do you think you can do well in the trial?"
    
    t "What's ‘trial'?"
    
    e "{i}Uh oh.{/i}"
    
    e "{i}They're nice, but maybe they'll need some help. Should I?{/i}"

    menu:
        "Yes":
            jump .tau_yes 

        "I need to think about it more.":
            jump .tau_no


label .ask_tau:
    # Show Tau sprite

    e "Should I ask Tau to be my partner?"

    menu:
        "Yes":
            jump .tau_yes 

        "I need to think about it more.":
            jump partner_choosing


label .tau_yes:
    $ persistent.prologue_partner = "tau"

    e "{i}Of course I should. And I'm sure they can help me out too, somehow!{/i}"
    
    e "It's just a test. Like in school."
    
    t "School?"
    
    e "Yes! The place where you go to learn literature, science, maths…"
    
    t "Ooooh! Home!!!"
    
    e "{i}They live in a school…?{/i}"
    
    e "Yes, like home! So… Do you wanna do it together?"
    
    # Tau looks confidently smug
    
    t "Hehe! Yes. Let's do the test in school."

    jump .conclude_choosing


label .tau_no:
    e "{i}I shouldn't underestimate them too much, that's a bit rude. I should let them choose who they want to do the trial with. I may come back to them later, though.{/i}"

    jump partner_choosing


label .speak_with_sylvia:
    $ spoke_with_sylvia = True

    # Dialogue

    menu:
        "Yes. Let's be partners.":
            jump .sylvia_yes 

        "I need to think about it more.":
            jump .sylvia_no


label .ask_sylvia:
    # Show Sylvia sprite

    e "Should I ask Sylvia to be my partner?"

    menu:
        "Will you be my partner, Sylvia?":
            jump .sylvia_yes 

        "I need to think about it more.":
            jump partner_choosing


label .sylvia_yes:
    $ persistent.prologue_partner = "sylvia"

    # Sylvia response

    jump .conclude_choosing


label .sylvia_no:
    # Sylvia response

    jump partner_choosing


label .speak_with_rene:
    $ spoke_with_rene = True

    # Dialogue

    menu:
        "Yes. Let's be partners.":
            jump .rene_yes 

        "I need to think about it more.":
            jump .rene_no


label .ask_rene:
    # Show Rene sprite

    e "Should I ask René to be my partner?"

    menu:
        "Will you be my partner, René?":
            jump .rene_yes 

        "I need to think about it more.":
            jump partner_choosing


label .rene_yes:
    $ persistent.prologue_partner = "rene"

    # Rene response

    jump .conclude_choosing


label .rene_no:
    # Rene response

    jump partner_choosing


label .conclude_choosing:
    "Choosing concluded."

    return
