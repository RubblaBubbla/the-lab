init python:
    met_rudy = False
    met_rene = False
    met_sylvia = False
    met_tau = False

# Player can click on each character sprite to get an introductory dialogue
screen meet_and_greet:
    text "Who should I talk to?"

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.25
        idle "full_body.png"
        hover "full_body.png"
        if (not met_tau):
             action Jump("meet_tau")
        else:
            action Jump("greet_tau")


label meet_and_greet:
    call screen meet_and_greet


# Tau introduction
label meet_tau:
    t "..."

    t "Hi."

    $ met_tau = True

    call screen meet_and_greet


# Tau follow-up
label greet_tau:
    e "Hello again!"

    t "..."

    t "{i}Tau smiles cheerfully!{/i}"

    call screen meet_and_greet
