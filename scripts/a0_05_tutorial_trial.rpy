init python:
    prologue_trial_score = 0
    tablet_interactable = False
    partner_interactable = False

    current_question = 0

    # Used to determine if current answer is correct
    is_correct = False

    q4_answer = "0"
    q7_answer = "n"
    q8_answer = "0"


style tablet_question is text:
    size 24
    color "#222222"
    font "VT323-Regular.ttf"


# -----------------------------------------------------------------
# Score displays
# -----------------------------------------------------------------
screen prologue_trial_score_box:
    vbox:
        xpos 0.65
        ypos 0.12

        text "{=tablet_question}Score: [prologue_trial_score]{/=tablet_question}"


screen prologue_trial_final_score_box:
    vbox:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

        text "{=tablet_question}{size=48}Final Score: [prologue_trial_score]{/size}{/=tablet_question}"


# -----------------------------------------------------------------
# Partner display
# -----------------------------------------------------------------
transform prologue_partner_display:
    zoom 0.8

screen prologue_partner_icon:
    imagebutton:
        xanchor 0.5
        yanchor 0.0

        xpos 0.897
        ypos 0.05

        if (persistent.prologue_partner == "Tau"):
            idle "tau mugshot.png" at prologue_partner_display
        elif (persistent.prologue_partner == "Rudy"):
            idle "rudy mugshot.png" at prologue_partner_display
        elif (persistent.prologue_partner == "Rene"):
            idle "rene mugshot.png" at prologue_partner_display
        elif (persistent.prologue_partner == "Sylvia"):
            idle "sylvia mugshot.png" at prologue_partner_display
        else:
            idle "tau mugshot.png" at prologue_partner_display

        # Only interactable if tablet is interactable
        if (tablet_interactable):
            if (current_question == 1):
                action Jump("prologue_trial.q01_assist")
            elif (current_question == 2):
                action Jump("prologue_trial.q02_assist")
            elif (current_question == 3):
                action Jump("prologue_trial.q03_assist")
            elif (current_question == 4):
                action Jump("prologue_trial.q04_assist")
            elif (current_question == 5):
                action Jump("prologue_trial.q05_assist")
            elif (current_question == 6):
                action Jump("prologue_trial.q06_assist")
            elif (current_question == 7):
                action Jump("prologue_trial.q07_assist")
            elif (current_question == 8):
                action Jump("prologue_trial.q08_assist")
            else:
                action None
        else:
            action None

    # Border
    vbox:
        xanchor 0.5
        yanchor 0.0

        xpos 0.897
        ypos 0.05

        image "mugshot_border.png" at prologue_partner_display


# -----------------------------------------------------------------
# Question displays
# -----------------------------------------------------------------
screen prologue_trial_q01:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}1. What is missing from this ordered list?\n\t\t\t{b}7, 6, 5, ?, 3, 2,{/b}{/=tablet_question}"
    
    # Answers
    vbox:
        xpos 0.3
        ypos 0.5

        if (tablet_interactable):
            textbutton "{=tablet_question}A. 8{/=tablet_question}" action Jump("prologue_trial.q01_handle_answer")
        
            textbutton "{=tablet_question}B. 4{/=tablet_question}" action [SetVariable("is_correct", True), Jump("prologue_trial.q01_handle_answer")]

            textbutton "{=tablet_question}C. 1{/=tablet_question}" action Jump("prologue_trial.q01_handle_answer")

            textbutton "{=tablet_question}D. 0{/=tablet_question}" action Jump("prologue_trial.q01_handle_answer")
        
        else:
            textbutton "{=tablet_question}A. 8{/=tablet_question}" action None
        
            textbutton "{=tablet_question}B. 4{/=tablet_question}" action None

            textbutton "{=tablet_question}C. 1{/=tablet_question}" action None

            textbutton "{=tablet_question}D. 0{/=tablet_question}" action None


screen prologue_trial_q02:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}2. Which two statements prove that Eva has \n\t\t\tbrown hair?{/=tablet_question}"
        text "\t\t{=tablet_question}A. Rudy has black hair{/=tablet_question}"
        text "\t\t{=tablet_question}B. Mother has brown hair{/=tablet_question}"
        text "\t\t{=tablet_question}C. Eva's hair is not the same color as Rudy's{/=tablet_question}"
        text "\t\t{=tablet_question}D. Mother's hair is the same color as Eva's{/=tablet_question}"
        text "\t\t{=tablet_question}E. Eva has long hair{/=tablet_question}"

    
    # Answers
    vbox:
        xpos 0.3
        ypos 0.6

        if (tablet_interactable):
            textbutton "{=tablet_question}A. A and C{/=tablet_question}" action Jump("prologue_trial.q02_handle_answer")
        
            textbutton "{=tablet_question}B. C and D{/=tablet_question}" action Jump("prologue_trial.q02_handle_answer")

            textbutton "{=tablet_question}C. B and D{/=tablet_question}" action [SetVariable("is_correct", True), Jump("prologue_trial.q02_handle_answer")]

            textbutton "{=tablet_question}D. D and E{/=tablet_question}" action Jump("prologue_trial.q02_handle_answer")
        
        else:
            textbutton "{=tablet_question}A. A and C{/=tablet_question}" action None
        
            textbutton "{=tablet_question}B. C and D{/=tablet_question}" action None

            textbutton "{=tablet_question}C. B and D{/=tablet_question}" action None

            textbutton "{=tablet_question}D. D and E{/=tablet_question}" action None


screen prologue_trial_q03:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}3. Given the following clues, when does Sylvia go to bed?{/=tablet_question}"
        text "\t\t{=tablet_question}* The children are named Sylvia, René, Rudy, and Tau{/=tablet_question}"
        text "\t\t{=tablet_question}* They are aged 9.5, 10, 10.5, and 11{/=tablet_question}"
        text "\t\t{=tablet_question}* Their bedtimes are 20:00, 20:30, 21:00, and 21:30{/=tablet_question}"
        text "\t\t{=tablet_question}* The oldest goes to bed 30 minutes after René{/=tablet_question}"
        text "\t\t{=tablet_question}* Rudy sleeps later than Tau{/=tablet_question}"
        text "\t\t{=tablet_question}* Rudy is 10 years old{/=tablet_question}"
        text "\t\t{=tablet_question}* The youngest sleeps at 20:00{/=tablet_question}"
        text "\t\t{=tablet_question}* The child who sleeps at 20:30 is either 10 years \n\t\t\told or René{/=tablet_question}"

    
    # Answers
    vbox:
        xpos 0.3
        ypos 0.7

        if (tablet_interactable):
            textbutton "{=tablet_question}A. 20:00{/=tablet_question}" action Jump("prologue_trial.q03_handle_answer")
        
            textbutton "{=tablet_question}B. 20:30{/=tablet_question}" action Jump("prologue_trial.q03_handle_answer")

            textbutton "{=tablet_question}C. 21:00{/=tablet_question}" action [SetVariable("is_correct", True), Jump("prologue_trial.q03_handle_answer")]

            textbutton "{=tablet_question}D. 21:30{/=tablet_question}" action Jump("prologue_trial.q03_handle_answer")

        else:
            textbutton "{=tablet_question}A. 20:00{/=tablet_question}" action None

            textbutton "{=tablet_question}B. 20:30{/=tablet_question}" action None
           
            textbutton "{=tablet_question}C. 21:00{/=tablet_question}" action None

            textbutton "{=tablet_question}D. 21:30{/=tablet_question}" action None 


screen prologue_trial_q04:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}4. Starting in the top left corner of a 2x2 grid, \n\t\t\tand only being able to move to the right and \n\t\t\tdown, there are exactly 6 routes to the bottom \n\t\t\tright corner. How many such paths are there \n\t\t\tthrough a 6 x 6 grid?{/=tablet_question}"

    
    # Answer input (924)
    hbox:
        xpos 0.3
        ypos 0.5

        text "{=tablet_question}Enter number, then press Return: {/=tablet_question}"

        if (tablet_interactable):
            input:
                length 12
                allow "0123456789"
                color "#222222"
                font "VT323-Regular.ttf"
                size 24


screen prologue_trial_q05:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}5. Which of the following is forbidden under \n\t\t\tMother's rules?{/=tablet_question}"

    
    # Answers
    vbox:
        xpos 0.3
        ypos 0.5

        if (tablet_interactable):
            textbutton "{=tablet_question}A. Attempting an already cleared trial{/=tablet_question}" action [SetVariable("is_correct", True), Jump("prologue_trial.q05_handle_answer")]
        
            textbutton "{=tablet_question}B. Murder{/=tablet_question}" action [SetVariable("is_correct", "murder"), Jump("prologue_trial.q05_handle_answer")]

            textbutton "{=tablet_question}C. Stealing{/=tablet_question}" action Jump("prologue_trial.q05_handle_answer")

            textbutton "{=tablet_question}D. Completing trials with a partner{/=tablet_question}" action Jump("prologue_trial.q05_handle_answer")

        else:
            textbutton "{=tablet_question}A. Attempting an already cleared trial{/=tablet_question}" action None
        
            textbutton "{=tablet_question}B. Murder{/=tablet_question}" action None

            textbutton "{=tablet_question}C. Stealing{/=tablet_question}" action None

            textbutton "{=tablet_question}D. Completing trials with a partner{/=tablet_question}" action None


screen prologue_trial_q06:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}6. What was the correct answer to question 1?{/=tablet_question}"

    
    # Answers
    vbox:
        xpos 0.3
        ypos 0.5

        if (tablet_interactable):
            textbutton "{=tablet_question}A. 3{/=tablet_question}" action Jump("prologue_trial.q06_handle_answer")
        
            textbutton "{=tablet_question}B. 4{/=tablet_question}" action [SetVariable("is_correct", True), Jump("prologue_trial.q06_handle_answer")]

            textbutton "{=tablet_question}C. 5{/=tablet_question}" action Jump("prologue_trial.q06_handle_answer")

            textbutton "{=tablet_question}D. 6{/=tablet_question}" action Jump("prologue_trial.q06_handle_answer")

        else:
            textbutton "{=tablet_question}A. 3{/=tablet_question}" action None
        
            textbutton "{=tablet_question}B. 4{/=tablet_question}" action None

            textbutton "{=tablet_question}C. 5{/=tablet_question}" action None

            textbutton "{=tablet_question}D. 6{/=tablet_question}" action None


screen prologue_trial_q07:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}7. Five students, Ru, S, Re, T, E, took part in a \n\t\t\tcontest. One prediction was that the contestants \n\t\t\twould finish in the same order (RuSReTE). \n\t\t\tThis prediction was very poor. In fact no \n\t\t\tcontestant finished in the position predicted,\n\t\t\tand no two contestants predicted to finish \n\t\t\tconsecutively actually did so. A second prediction \n\t\t\thad the contestants finishing in the order TRuEReS. \n\t\t\tThis prediction was better. Exactly two of the \n\t\t\tcontestants finished in the places predicted, and \n\t\t\ttwo disjoint pairs of students predicted to finish \n\t\t\tconsecutively actually did so. \n\t\t\tDetermine the order in which the contestants \n\t\t\tfinished.{/=tablet_question}"

    
   # Answer input (ETRuReS)
    hbox:
        xpos 0.3
        ypos 0.7

        text "{=tablet_question}Enter (ex. TRuReSE), then press Return: {/=tablet_question}"

        if (tablet_interactable):
            input:
                length 7
                allow "ETRueS"
                color "#222222"
                font "VT323-Regular.ttf"
                size 24


screen prologue_trial_q08:
    # Question
    vbox:
        xpos 0.3
        ypos 0.17

        text "{=tablet_question}8. Eva and Sylvia play a game with three piles \n\t\t\tof stones. On each player's turn, the player \n\t\t\tmay remove one or more stones from the piles. \n\t\t\tHowever, if the player takes stones from more \n\t\t\tthan one pile, then the same number of stones \n\t\t\tmust be removed from each of the selected piles. \n\t\t\tThe player taking the last stone(s) is the winner. \n\t\t\tAs the second player, Sylvia gets to choose how \n\t\t\tmany stones each pile starts with (x, y, z) from \n\t\t\t0 to 100 inclusive, smallest to largest (or equal). \n\t\t\tShe also knows that there are many ways to set \n\t\t\tthe game up so she wins no matter what Eva does. \n\t\t\tIf Sylvia adds up all these numbers (x+y+z) across \n\t\t\tall starting configurations that guarantee she \n\t\t\twins, what value will she get?{/=tablet_question}"

    
   # Answer input (173895)
    hbox:
        xpos 0.3
        ypos 0.75

        text "{=tablet_question}Enter a number, then press Return: {/=tablet_question}"

        if (tablet_interactable):
            input:
                length 12
                allow "0123456789"
                color "#222222"
                font "VT323-Regular.ttf"
                size 24


# -----------------------------------------------------------------
# Labels (trial start and answer handling )
# -----------------------------------------------------------------
label prologue_trial:
    scene tablet:
        subpixel True 
        yanchor 0.0
        xanchor 0.5 
        ypos 0.0
        xpos 0.5 
        zoom 1.50
    with fade

    show screen prologue_partner_icon
    show screen prologue_trial_score_box

    jump .start_test


label .start_test:
    show screen prologue_trial_q01
    with dissolve

    pause 0.5

    e "Huh? This is pretty easy!"

    $ current_question = 1
    $ tablet_interactable = True

    call screen prologue_trial_q01


label .q01_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q02
    with dissolve

    if (is_correct):
        $ prologue_trial_score += 1
        
        e "Yes, I got it right!"

        e "Next question..."

    else:
        e "Oh, my score didn't change. I guess I got it wrong..."

    $ current_question = 2
    $ tablet_interactable = True
    $ is_correct = False

    call screen prologue_trial_q02


label .q02_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q03
    with dissolve

    if (is_correct):
        $ prologue_trial_score += 1
        
        e "Oh, that was worth more points!"

        e "This one is definitely harder though..."

    else:
        e "Oh, too bad... And the next one's even harder..."

    $ current_question = 3
    $ tablet_interactable = True
    $ is_correct = False

    call screen prologue_trial_q03


label .q03_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q04
    with dissolve

    if (is_correct):
        $ prologue_trial_score += 1
        
        e "Whew. Okay. I can do this."

    else:
        e "Aw no..."

    window hide

    $ current_question = 4
    $ tablet_interactable = True
    $ is_correct = False

    $ q4_answer = renpy.call_screen("prologue_trial_q04")

    window show

    jump .q04_handle_answer


label .q04_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q05
    with dissolve

    if (q4_answer == "924"):
        $ prologue_trial_score += 4
        
        e "Wow! I got it!"
    else:
        e "No dice."

    window hide 

    $ current_question = 5
    $ tablet_interactable = True

    call screen prologue_trial_q05

    window show


label .q05_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q06
    with dissolve

    if (is_correct == "murder"):
        e "Wait. Murder isn't forbidden???"

    elif (is_correct):
        $ prologue_trial_score += 5
        
        e "That was a nice breather."

        e "Wait a second..."

    else:
        e "Rats."

    window hide 

    $ current_question = 6
    $ tablet_interactable = True
    $ is_correct = False

    call screen prologue_trial_q06

    window show


label .q06_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q07
    with dissolve

    if (is_correct):
        $ prologue_trial_score += 6
        e "Whew. I remembered."

    else:
        e "Aw."

    window hide

    $ current_question = 7
    $ tablet_interactable = True
    $ is_correct = False

    $ q7_answer = renpy.call_screen("prologue_trial_q07")

    window show

    jump .q07_handle_answer


label .q07_handle_answer:
    $ tablet_interactable = False

    show screen prologue_trial_q08
    with dissolve

    if (q7_answer.lower() == "etrures"):
        $ prologue_trial_score += 7
        
        e "Yes! I got it!"
    else:
        e "Too bad."

    window hide

    $ current_question = 8
    $ tablet_interactable = True

    $ q8_answer = renpy.call_screen("prologue_trial_q08")

    window show

    jump .q08_handle_answer


label .q08_handle_answer:
    $ tablet_interactable = False

    hide screen prologue_trial_score_box

    $ current_question = 9

    if (q8_answer == "173895"):
        $ prologue_trial_score += 8

        show screen prologue_trial_final_score_box with dissolve
        
        e "Wow! That was right!"
    else:
        show screen prologue_trial_final_score_box with dissolve
        e "That was impossible!"

        e "At least it's over now."

    # Segue to conclusion
    $ persistent.prologue_trial_score = prologue_trial_score

    e "I'll have to see how this score stacks up."

    e "But what would it mean to win if the others lose...?"

    hide screen prologue_trial_final_score_box
    hide screen prologue_partner_icon
    
    jump prologue_trial_conclude


# -----------------------------------------------------------------
# Labels for partner assist
# -----------------------------------------------------------------
label .q01_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q01

    t "Hi!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q01


label .q02_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q02

    t "Hi2!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q02


label .q03_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q03

    t "Hi3!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q03


label .q04_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q04

    t "Hi4!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q04
    jump .q04_handle_answer


label .q05_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q05

    t "Hi5!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q05


label .q06_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q06

    t "Hi6!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q06


label .q07_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q07

    t "Hi7!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q07
    jump .q07_handle_answer


label .q08_assist(partner=persistent.prologue_partner):
    $ tablet_interactable = False
    show screen prologue_trial_q08

    t "Hi8!"
    
    $ tablet_interactable = True
    call screen prologue_trial_q08
    jump .q08_handle_answer


# -----------------------------------------------------------------
# Trial conclusion
# -----------------------------------------------------------------
label prologue_trial_conclude:
    scene bg central_area
    with fade

    e "Conclude."

    return
