# Entry point, jumps to first scene
label start:
    # Manage camera
    camera:
        perspective True

    jump eva_opening


# Eva's final memory before waking up in the lab.
# She says goodnight to her mother and says a bedtime prayer as a hand creeps up on her, symbolizing the end of the dream...
label eva_opening:
    scene bg eva_bedroom
    with fade_2s

    # Calming nighttime music starts
    play music "audio/elementary.ogg" fadein 3.0 volume 0.5

    unknown "Sleep well, Eva."

    e "Goodnight Mom! Love you."

    e "{i}Whew… it's been quite the day. Work is fun when done together, but it's still work!{/i}"

    e "{i}At least I'll get to enjoy the party tomorrow, too. I can't wait!{/i}"

    e "{i}*Yawn…*{/i}"

    stop music fadeout 2.0

    e "{i}Of course, I'd never forget…{/i}"

    pause 2.5

    # Shuffling sound here?
    # Start new music?
    play music "audio/falling_star.ogg" volume 0.4 
    
    e "Precious Father, I pray that as I lie down and sleep, I will do so in peace."
   
    e "For you make me dwell in safety. I will not fear the nighttime because your presence is with me."
   
    # A hand begins to appear on screen
    
    e "Your love surrounds me, and your protection is upon me."
    
    # The hand opens up and gets bigger
    
    e "I thank you for allowing me to enjoy the day. And I now pray that I can enjoy the night and have peaceful sleep."
    
    # The hand is fully visible and ominous now.
    
    e "Amen."
    stop music fadeout 3.0

    jump wake_up
    return


# Eva wakes up to a strange new place. One by one, the other children also emerge from their chambers
define wake_up_fade = Fade(2, 2, 0.25)
label wake_up:
    # Fade out/in to white
    scene bg white
    with wake_up_fade

    play sound "audio/airlock.ogg" volume 0.4
    
    # Screen flash white
    scene bg central_area
    with white_flash

    play sound "audio/water_spill.ogg" volume 0.4 
    
    play music "audio/hollow_wind.ogg" fadein 1.5 volume 0.8

    e "Guh..."

    e "{i}What… What's going on?{/i}"
    
    e "{i}... Oh. I must be dreaming.{/i}"
    
    e "{i}But what a dreary place for a dream…{/i}"
    
    e "{i}Let me try this…{/i} "
    
    # Eva pinches herself
    play sound "audio/dog_toy_squeak.ogg" volume 0.5 
    pause 
    
    e "{i}I'm not strong enough to pinch myself awake…{/i}"
    
    e "..."
    
    e "{i}Wait. If I know I'm dreaming in my dream, I can control it!{/i}"
    
    e "{i}I want to fly out of here!{/i}"
    
    "… … …"
    
    e "{i}Maybe I need to shout it?{/i}"
    
    e "{i}*inhale…*{/i}"
    
    e "I WANT TO FLY OUT OF HERE!!!" with vpunch

    stop music
    u_ru "Pipe down, will you?"
    
    e "Huh?"
    
    # Rudy's sprite fades in. He's not happy
    play sound "audio/ding.ogg"
    show rudy neutral:
        subpixel True

        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.7

        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(-10.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
    with dissolve
    
    e "Oh, I'm sorry! I didn't see you there!" 

    play music "audio/hollow_wind.ogg" fadein 1.5 volume 0.8
    u_ru "Then you'd better stay alert or make peace with the consequences."

    e "What do you mean?"
    
    # Rudy straightens
    show rudy neutral:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(-10.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.20)
    show rudy neutral:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    u_ru "Don't play dumb. You know the ropes."
    
    # Rudy turns away to make his point
    show rudy neutral:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, -30.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(0.20)
    show rudy neutral:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, -30.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    u_ru "And put some clothes on. You look indecent."
    
    voice "audio/sudden_interruption.ogg"
    e "Ack! No way!" with hpunch
    
    e "{i}This is all too disorienting. Where would…{/i}"
    
    e "Uhm. Oh. In here?"
    
    # Eva opens nearby chest
    pause 0.5
    play sound "audio/wooden_creak.ogg"
    pause 1.75

    e "Why are my clothes in this chest?"

    e "A-Anyway."
    
    e "Please look away!!!"
    
    # Shuffling noises. Rudy sprite fades out
    
    # More shuffling noises
    scene bg central_area
    with blackout_fade
    
    e "Okay. You can look now."
    
    # Rudy sprite returns
    show rudy neutral:
        subpixel True

        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.7
    with dissolve
    pause 1.5
    
    e "{i}What an embarrassing dream…{/i}"
    
    e "So… What's your name?"
    
    u_ru "Don't ask stupid questions like th--{p=0.4}{nw}"

    # Rudy is cut off by the sound of three more airlocks opening and spilling water
    play sound "audio/airlock.ogg" volume 0.5
    pause 0.5
    play sound "audio/airlock.ogg" volume 0.4
    pause 0.5
    play sound "audio/airlock.ogg" volume 0.3
    pause 0.5
    play sound "audio/water_spill.ogg" volume 0.5
    
    e "{i}Oh! Three more people…{/i}"
    
    e "{i}I don't see any more tubes here. Is this all of us?{/i}"
    
    # Rudy walks off, but one last dialogue appears from him from off-screen
    
    u_ru "Your clothes are in the chest next to your chambers, guys."
    
    stop music

    e "I'm not looking!"
    
    # Shuffling noises as the screen goes dark.
    scene bg central_area
    with blackout_fade
    # Fade back in
    
    play music "audio/lofi_hip_hop_beat_cut.ogg" volume 0.3

    # Sylvia sprite appears, looking very weirded out
    show sylvia neutral:
        xanchor 0.5
        yanchor 0.5

        xpos 0.5
        ypos 0.75

        zoom 1.2
    with dissolve

    u_s "Mmh. Why can't I…?"
    
    # Rene sprite appears. He's in a better mood than most
    show rene neutral:
        xanchor 0.5
        yanchor 0.5

        xpos 0.75
        ypos 0.75

        xzoom -1.0
        zoom 1.3
    with dissolve

    u_re "Oh, that wasn't so bad. Hehe."
    
    # Tau appears, looking curious
    show tau neutral:
        xanchor 0.5
        yanchor 0.5

        xpos 0.25
        ypos 0.75

        xzoom -1.0
        zoom 1.15
    with dissolve
    
    u_t "Fabric… !!!"
    
    e "Excuse me. Do you know these people?"
    
    "..."
    
    e "{i}No answer. Looks like I'm on my own for now…{/i}"

    jump meet_and_greet # a0_01

    return