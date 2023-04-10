# Entry point, jumps to first scene
label start:
    jump eva_opening


# Eva's final memory before waking up in the lab.
# She says goodnight to her mother and says a bedtime prayer as a hand creeps up on her, symbolizing the end of the dream...
label eva_opening:
    scene bg eva_bedroom
    with fade_2s

    # Start some calming nighttime music

    unknown "Sleep well, Eva."

    e "Goodnight Mom! Love you."

    e "{i}Whew… it’s been quite the day. Work is fun when done together, but it’s still work!{/i}"

    e "{i}At least I’ll get to enjoy the party tomorrow, too. I can’t wait!{/i}"

    e "{i}*Yawn…*{/i}"

    e "{i}Of course, I'd never forget…{/i}"

    # Shuffling sound here?
    # Start new music?
    
    e "Precious Father, I pray that as I lie down and sleep, I will do so in peace."
   
    e "For you make me dwell in safety. I will not fear the nighttime because your presence is with me."
   
    # A hand begins to appear on screen
    
    e "Your love surrounds me, and your protection is upon me."
    
    # The hand opens up and gets bigger
    
    e "I thank you for allowing me to enjoy the day. And I now pray that I can enjoy the night and have peaceful sleep."
    
    # The hand is fully visible and ominous now.
    
    e "Amen."

    # Music fades

    jump wake_up
    return


# Eva wakes up to a strange new place. One by one, the other children also emerge from their chambers
define wake_up_fade = Fade(2, 2, 0.25)
label wake_up:
    # Fade out/in to white
    scene bg white
    with wake_up_fade

    play sound "audio/airlock.ogg" volume 0.6
    
    # Screen flash white
    scene bg central_area
    with white_flash

    play sound "audio/water_spill.ogg" volume 0.5 


    e "..."

    jump meet_and_greet #a0_01

    return