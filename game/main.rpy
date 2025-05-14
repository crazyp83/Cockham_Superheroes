label MCSleep:
if mclevel02 == False:
    scene intromcsleep01:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.04
    with fade
if mclevel02:
    scene mcsleeplevel02a:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.1
    with fade
mc "Time to go to bed... Tomorrow is another day. A SUPERHERO day hopefully."
if frosttoldmc and dreamfrost == False and frostchoseevil:
    hide screen calendar
    $ dreamfrost = True
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    de "That was some kind of twist, hey?"
    window hide
    show intromcsleep02c
    with dissolve
    mc "Yeah, I didn't see it coming. And neither did anyone on the dev's discord."
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "You're gonna follow through with her GREAT OFFER? Right?"
    mc "What offer?"
    hide demonafly03
    show demonafly04 at topright
    with fastdissolve
    de "TO RULE COCKHAM WITH YOUR LANDLORD."
    mc "It does sound appealing..."
    hide demonafly04
    show demonafly02 at topright
    with fastdissolve
    de "You BET! If you ruled Cockham as a Super-Villain, you could get ALL THE POONTANG YOU WANT!"
    mc "That's a good point. Fuck yeah, thanks Demona! And when do I get to fuck YOU?"
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "Patience, young Padawan. You need to train first. With your landlord..."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if frosttoldmc and dreamfrost == False and frostchosegood:
    hide screen calendar
    $ dreamfrost = True
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    an "You don't really believe her, do you?"
    window hide
    show intromcsleep02b
    with dissolve
    mc "Who?"
    hide angelafly01
    show angelafly03 at topleft
    with fastdissolve
    an "Emma Frost. She's a Super-Villain, she LIES for a a living!"
    mc "Yeah, but her story was pretty convincing... I'm confused."
    hide angelafly03
    show angelafly01 at topleft
    with fastdissolve
    an "If only you knew the power of the HERO side! Stay on the right path and you will FEEL ITS FORCE!" 
    mc "Oooh? And then I get to fuck you, right?"
    hide angelafly01
    show angelafly02 at topleft
    with fastdissolve
    an "Well... I suppose... Eventually.... Have sweet dreams, my young hero! Without involving ME naked preferably..."
    mc "I'll try, Angela..."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if mission01dream == 1:
    $ mission01dream = 0
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    an "I'm so proud of you, [name]!"
    window hide
    show intromcsleep02b
    with dissolve
    mc "Why is that, sexy angel with big tits...?"
    hide angelafly01
    show angelafly03 at topleft
    with fastdissolve
    an "You stopped that horrible rapist from escaping, you're becoming a TRUE SUPERHERO!"
    mc "Alright! So, when do I get to fuck you in my dreams as a reward?"
    hide angelafly03
    show angelafly02 at topleft
    with fastdissolve
    an "Err, not quite yet. You're not THAT good... But you're on the right path. Apart from that libido of yours..." 
    mc "But I NEED IT for my job!"
    an "I... suppose so... Have sweet dreams my young hero! Without involving ME naked preferably..."
    mc "I'll try, Angela..."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if mission01dream == 2:
    $ mission01dream = 0
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    de "What a BITCH, hey?"
    window hide
    show intromcsleep02c
    with dissolve
    mc "Who?"
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "That SLUT who said you were useless!"
    mc "Oh yeah, I resented that I remember..."
    hide demonafly03
    show demonafly04 at topright
    with fastdissolve
    de "She's clearly not getting ENOUGH COCK from her hubby..."
    mc "I heard he has a tiny one. Pfff!"
    hide demonafly04
    show demonafly02 at topright
    with fastdissolve
    de "LOSER! Not like YOU, and that MONSTERCOCK of yours! You'd give it to her every night if you were her son, wouldn't you? Even if it meant going against that fucking Patreon Bill, right?"
    mc "Err... I don't think I can say that h..."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if mission02win == True and mission02dream == False:
    $ mission02dream = True
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    de "Why did you do that?"
    window hide
    show intromcsleep02c
    with dissolve
    mc "Do what?"
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "You should have POUNDED that police slut into OBLIVION!"
    mc "But then Sexy Luthor would have escaped!"
    hide demonafly03
    show demonafly04 at topright
    with fastdissolve
    de "Who gives a crap, she'll escape anyway, you KNOW THAT!"
    hide demonafly04
    show demonafly02 at topright
    with fastdissolve
    de "I'm VERY disappointed in you, [name]. Why should I help you get your rocks off if you don't even listen to me?"
    mc "Well, err... I mean, I'm a superhero!"
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "A SUPER-ZERO more like it! You'd better up your game if you ever want to taste those sumptuous titties of mine!"
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if mission02fail == True and mission02dream == False:
    $ mission02dream = True
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    an "That was so naughty of you, [name]!"
    window hide
    show intromcsleep02b
    with dissolve
    mc "What did I do?"
    hide angelafly01
    show angelafly03 at topleft
    with fastdissolve
    an "You let this EVIL Super-Villain escape and you kept on BATTERING that poor officer's ass!"
    mc "But she liked it, remember?"
    hide angelafly03
    show angelafly02 at topleft
    with fastdissolve
    an "Only because you tricked her with your SUPER-STUDLINESS. You're NOT supposed to use your Super-Powers that way!" 
    mc "I do what I want, I'm the Master of my own Destiny!"
    hide angelafly02
    show angelafly01 at topleft
    with fastdissolve
    an "And your destiny is going in the WRONG direction! Pull yourself together or you will be a lost cause forever!"
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if mission03end and chosehonokagood and dreammission03 == False:
    $ dreammission03 = True
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    an "I'm so proud of you, you spared that poor girl who was being blackmailed by villains!"
    window hide
    show intromcsleep02b
    with dissolve
    mc "You mean that little piece of crumpet, Honoka?"
    hide angelafly01
    show angelafly03 at topleft
    with fastdissolve
    an "Don't talk about her that way, that's so naughty!"
    mc "I did have to pound her good to force her to give me that key, remember?"
    hide angelafly03
    show angelafly02 at topleft
    with fastdissolve
    an "Well, err, sometimes, the Lord works in mysterious ways. Very mysterious ways... Like when he gave me those huge knockers... * sigh *"
    mc "He just has good tastes is all."
    hide angelafly02
    show angelafly01 at topleft
    with fastdissolve
    an "But at least you used your Super-powers for good! Ultimately..."
    mc "That's right. Good. AND getting some free poontang. Perfect life."
    hide angelafly01
    show angelafly02 at topleft
    with fastdissolve
    an "I think I need to work on my persuasion powers. Have sweet dreams, young hero!"
    mc "I will, I will. Big-titted angel."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay
    
if mission03end and chosehonokagood == False and dreammission03 == False:
    $ dreammission03 = True
    hide screen calendar
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    scene intromcsleep02a
    with fade
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    de "I see you are really going on that Super-Villain path, aren't you?"
    window hide
    show intromcsleep02c
    with dissolve
    mc "How did you guess?"
    hide demonafly02
    show demonafly03 at topright
    with fastdissolve
    de "You could have spared Honoka, but you made sure that little trollop and her innocent family SUFFERED for what she did!"
    mc "At the same time, she did work for the Chinese Triad. And they're Villains."
    hide demonafly03
    show demonafly04 at topright
    with fastdissolve
    de "And YOU're getting even MORE villainous than they are! You are well on your way to a sumptuous titfuck from my smothering puppies..."
    mc "Alright! I felt a bit bad, but now, I FEEL GOOD!"
    hide demonafly04
    show demonafly02 at topright
    with fastdissolve
    de "Not TOO good I hope! Have sweet dreams. Or nightmares. it doesn't really matter anymore at this stage."
    stop music fadeout 1.0
    show screen calendar
    jump NewDay

if evilness <= 3 and dreamangel >= 7 and mission04end and mclevel02 == False:
    $ dreamangel = 0   
    hide screen calendar
    hide screen statscreenicon
    hide screen questscreenicon
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    voice "angel/handjob01"
    an "Open your eyes, [hero]!"
    menu:
        "See scene":
            pass
        "Skip scene":
            stop music
            jump NewDay            
    scene intromcsleep02a
    show intromcsleep02b
    with dissolve
    hide angelafly01 with dissolve
    mc "But... You're gone?"
    voice "angel/handjob02"
    an "I'm still here, just REALLY open your eyes and look down this time..."
    stop music
    play sound "sounds/angel.mp3"
    scene angelaroom01 with fade
    mc "Are... Are you for real?"
    voice "angel/handjob03"
    an "Maybe. Maybe not. Does it matter?"
    scene angelaroom02 with dissolve
    play music "sounds/sexy12.mp3"
    mc "Oh wow, it's like a DREAM come TRUE then!"
    voice "angel/handjob04"
    an "That's right, because you've been such a GOOD boy!"    
    scene angelaroom03 with dissolve
    mc "Cool! So I get to fuck your ass, right?"
    scene angelaroom04 with dissolve
    voice "angel/handjob05"
    an "What? NO! You need to take the \"Stairway to Heaven\", young hero!"
    mc "Hang on, does that mean I only get a lousy..."
    scene angelaroom05 with dissolve
    voice "angel/handjob06"
    an "...handjob? Yes. But it won't be lousy, I promise!"
    scene angelaroom06 with dissolve
    play sound "sounds/kiss.mp3"
    voice "angel/handjob07"
    an "Mmmh, I love your big cock..."
    mc "Aren't angels supposed to be sexless?"
    voice "angel/handjob08"
    an "We are allowed to reward GOOD BOYS. Like you. Especially those with HUGE COCKS!"
    scene angelaroom07 with dissolve
    voice "angel/handjob09a"
    an "It's just so GIGANTIC, [name]! Even in the heavens, we don't have boys THAT big!"
    voice "angel/handjob09b"
    an "I'm going to jerk you so HARD, you'll come all over the place!"
    play channel1 "sounds/wank.mp3"
    play channel2 "sounds/boymoan02.mp3"
    window hide
    label AngelaJerkSlow: 
    hide cum
    hide faster
    hide slower
    show angelajerkslowvideo behind angelajerkfastvideo
    pause 1.0
    hide angelajerkfastvideo with dissolve
    if angelajerktold == False:
        if age >= 20:
            voice "angel/handjob10a"
            an "I'll start by teasing you with a slow, sensual, two-handed wank on your monstrous shaft..."
        if age >= 18 and age <= 19:
            voice "angel/handjob10b"
            an "I'll start by teasing you with a slow, sensual, two-handed wank on your monstrous teenage shaft..."
        window hide
        $ angelajerktold = True
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     

    call screen angelajerkslow()
    screen angelajerkslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AngelaJerkFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AngelaJerkEnd")

    label AngelaJerkFast:
    show angelajerkfastvideo behind angelajerkslowvideo
    hide cum
    hide faster
    hide slower
    mc "Oh please... Jerk me faster, I need to come!"
    hide angelajerkslowvideo with dissolve
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     

    call screen angelajerkfast()
    screen angelajerkfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AngelaJerkSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AngelaJerkEnd")

    label AngelaJerkEnd:
    voice "angel/handjob11"
    an "Come for me, [name]. Let's move one ladder step closer to Heaven!"
    scene angelajerkcum01 with dissolve
    hide angelajerkfastvideo
    hide angelajerkslowvideo
    stop channel1
    stop channel2
    play channel1 "sounds/boyorgasm01.mp3"
    voice "angel/handjob12"
    an "Mmh, release that pent-up baby-batter, young hero!"
    window hide
    with fastflash
    if seenangeladream:
        voice "angel/handjob13"
        an "It's better than jerking off to me in the jacuzzi, isn't it?"
        mc "Err... How did you know I was, like, dreaming about you?"
        voice "angel/handjob14"
        an "Because I'm your GOOD conscience, [name]! I know your every thought..."
    if seenangeladream == False:
        voice "angel/handjob15"
        an "It's GOOD, isn't it? To be able to relieve yourself of such a burden!"    
    scene angelajerkcum02 with dissolve
    voice "angel/handjob16"
    an "Oh my Heavens! You had a LOT to release, didn't you?"
    window hide
    with fastflash
    mc "Fuck, YEAH! Always a LOT for big-titted angel babes like you!"
    scene angelajerkcum03 with dissolve
    voice "angel/handjob17"
    an "Mmmh, then cover my angel face with your hot, young SPUNK!"
    window hide
    with fastflash
    voice "angel/handjob18"
    an "Your load is UNGODLY HUGE, young hero!"
    scene angelajerkcum04 with dissolve
    voice "angel/handjob19"
    an "You're still PUMPING that fat load?"
    window hide
    with fastflash
    mc "Not done, yet, Angela, AAAAH!"
    scene angelajerkcum05 with dissolve
    voice "angel/handjob20"
    an "Oh no, I'm disappearing! You must be waking up..."
    window hide
    with fastflash
    mc "Nooooo, don't go!!!"    
    stop music
    stop channel1
    stop channel2
    scene intromcsleep04 with fade
    show screen calendar
    show screen statscreenicon
    show screen questscreenicon
    mc "Oh shit, it wasn't real after all... And I came all over myself instead of all over Angela's face... * sigh *"
    jump NewDay

if evilness >= 13 and dreamdemon >= 7 and mission04end and mclevel02 == False:
    $ dreamdemon = 0   
    hide screen calendar
    hide screen statscreenicon
    hide screen questscreenicon
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    voice "demona/titjob01"
    de "Hey wake up, [hero]!"
    menu:
        "See scene":
            pass
        "Skip scene":
            stop music
            jump NewDay            
    scene intromcsleep02a
    show intromcsleep02c
    with dissolve
    hide demonafly02 with dissolve
    mc "But... You're gone?"
    voice "demona/titjob02"
    de "I'm still here, just REALLY open your eyes and look down this time..."
    stop music
    play sound "sounds/demon.mp3"
    scene demonaroom01 with fade
    mc "Is... Is this for real?"
    voice "demona/titjob03"
    de "Maybe. Maybe not. Who cares?"
    scene demonaroom02 with dissolve
    play music "sounds/sexy13.mp3"
    mc "Aaaah, what are you doing, Demona?!"
    voice "demona/titjob04"
    de "What does it look like? I'm licking your fat pole with my super-long tongue!"    
    scene demonaroom03 with dissolve
    mc "Nice! And next, you're gonna RIDE IT WITH YOUR ASS, right?"
    voice "demona/titjob05"
    de "Humh, No, I don't want to. Just yet."
    mc "But... why not???"
    scene demonaroom04 with dissolve
    if age >= 20:
        voice "demona/titjob06a"
        de "Cos I'm evil and I like to torture you, that's why! What did you expect? That we would sing \"kumbaya\" while you ass-fucked me with 15 inches of MEGA-COCK?"
    if age >= 18 and age <= 19:
        voice "demona/titjob06b"
        de "Cos I'm evil and I like to torture you, that's why! What did you expect? That we would sing \"kumbaya\" while you ass-fucked me with 15 inches of TEEN MEGA-COCK?"
    mc "So... What do I get?"
    scene demonaroom05 with dissolve
    voice "demona/titjob07"
    de "A titjob. Still better than the lousy handjob the losers who chose the Hero route are getting! So get your legs up higher!"
    scene demonaroom06 with dissolve
    if age >= 20:
        voice "demona/titjob08a"
        de "Well, look at you, your giant dong is drooling pre-cum all over the place. That's just NASTY! You're a FILTHY boy, just like I like 'em!"
    if age >= 18 and age <= 19:
        voice "demona/titjob08b"
        de "Well, look at you, your giant teenage dong is drooling pre-cum all over the place. That's just NASTY! You're a FILTHY boy, just like I like 'em!"
    mc "Oh God, you're nasty too..."
    voice "demona/titjob09"
    de "You ain't seen nothing yet, you horse-hung muscle EVIL boy!"
    play channel1 "sounds/wank.mp3"
    play channel2 "sounds/boymoan02.mp3"
    window hide
    label DemonaTitfuckSlow: 
    hide cum
    hide faster
    hide slower
    show demonatitfuckslowvideo behind demonatitfuckfastvideo
    pause 1.0
    hide demonatitfuckfastvideo with dissolve
    if demonatitfucktold == False:
        if age >= 20:
            voice "demona/titjob10a"
            de "I'll start by teasing you with a slow, sensual, titfuck on your monstrous shaft..."
        if age >= 18 and age <= 19:
            voice "demona/titjob10b"
            de "I'll start by teasing you with a slow, sensual, titfuck on your monstrous teenage shaft..."
        window hide
        $ demonatitfucktold = True
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     

    call screen demonatitfuckslow()
    screen demonatitfuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("DemonaTitfuckFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("DemonaTitfuckEnd")

    label DemonaTitfuckFast:
    show demonatitfuckfastvideo behind demonatitfuckslowvideo
    hide cum
    hide faster
    hide slower
    mc "Oh please... Titfuck me faster, I need to come!"
    hide demonatitfuckslowvideo with dissolve
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     

    call screen demonatitfuckfast()
    screen demonatitfuckfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("DemonaTitfuckSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("DemonaTitfuckEnd")

    label DemonaTitfuckEnd:
    hide cum
    hide slower
    hide faster
    voice "demona/titjob11"
    de "Come for me, [name]. I want to see that NASTY cock SPEW ITS LOAD!"
    scene demonaroomcum01 with dissolve
    stop channel1
    stop channel2
    play channel1 "sounds/boyorgasm01.mp3"
    voice "demona/titjob12"
    de "You're really close, the pre-cum is flowing..."
    if demonawankevil:
        voice "demona/titjob13"
        de "It's better than jerking off to me in the jacuzzi, isn't it?"
        mc "Err... How did you know I was, like, dreaming about you?"
        voice "demona/titjob14"
        de "Because I'm your DIRTY conscience, [name]! I know your every thought...Now COME FOR DEMONA!"
    if demonawankevil == False:
        voice "demona/titjob15"
        de "I can tell you're enjoying this, you DIRTY BOY! Now COME FOR DEMONA!"    
    scene demonaroomcum02 with dissolve
    mc "AAAAH!"
    window hide
    with fastflash
    voice "demona/titjob16"
    de "That's so hot, you're cumming like a STALLION! You have a LOT of NASTY, YOUNG CUM for me, don't you?"
    scene demonaroomcum03 with dissolve
    mc "Fuck, YEAH! Always a LOT for big-titted demon babes like you!"
    window hide
    with fastflash
    voice "demona/titjob17"
    de "My tits are going to EMPTY your balls, aren't they?"    
    scene demonaroomcum04 with dissolve
    voice "demona/titjob18"
    de "That's it, let it RAIN DOWN ON ME!"
    window hide
    with fastflash
    mc "RHAAA, CUMMING SO MUCH!"
    scene demonaroomcum05 with dissolve
    voice "demona/titjob19"
    de "I'm fading out! Why are you waking up just when I was going to SLURP up all the salty nectar, godammit!"
    mc "I...err..."
    stop music
    stop channel1
    stop channel2
    scene intromcsleep04 with fade
    show screen calendar
    show screen statscreenicon
    show screen questscreenicon
    mc "Oh shit, it wasn't real after all... And I came all over myself instead of all over Demona's tits... * sigh *"
    jump NewDay

if evilness <= 5 and dreamangel >= 7 and mclevel02:
    $ dreamangel = 0   
    hide screen calendar
    hide screen statscreenicon
    hide screen questscreenicon
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    show angela01a at topleft with moveinleft
    hide angela01a
    show angelafly01 at topleft
    an "Open your eyes, [hero]!"
    menu:
        "See scene":
            pass
        "Skip scene":
            stop music
            jump NewDay            
    scene intromcsleep02a
    show intromcsleep02b
    with dissolve
    hide angelafly01 with dissolve
    mc "But... You're gone?"
    an "I'm still here, just REALLY open your eyes and look down this time..."
    stop music
    play sound "sounds/angel.mp3"
    scene angelaroom11 with fade
    mc "Are... Are you for real?"
    an "Maybe. Maybe not. Does it matter?"
    scene angelaroom12 with dissolve
    play music "sounds/sexy12.mp3"
    mc "Oh wow, it's like a DREAM come TRUE then!"
    an "That's right, because you've been such a GOOD boy!"    
    scene angelaroom13 with dissolve
    if angelavisitlevel02:
        "And I can't get enough of these eighteen inches of young meat you're carrying between your muscular legs!"
        mc "To fuck you in tha ass this time, right?"
        scene angelaroom14 with dissolve
        an "No, we're still on the pussy step."
        mc "Pussy step?"    
        scene angelaroom15 with dissolve
        an "On the Stairway to Heavens!"
        scene angelaroom16 with dissolve
        an "So you're STILL on the step where you get to fuck my tender angel pussy with your great big hard whopper, young hero!"
        mc "Good enough, I'll take it!"
    if angelavisitlevel02 == False:
        $ angelavisitlevel02 = True
        an "And your young love muscle has grown even BIGGER since my last visit!"
        mc "Now I remember. You promised me I would be able to fuck you in the ass!"
        scene angelaroom14 with dissolve
        an "Ah yes. But I was lying."
        mc "WHAT??? Angels can lie???"    
        scene angelaroom15 with dissolve
        an "We are allowed white lies. Cos they're not REAL lies. You believe me, right?"
        scene angelaroom16 with dissolve
        an "But don't worry, I'll make it up to you by letting you fuck my tender angel pussy with your great big hard whopper, young hero!"
        mc "Alright!"
    scene angelaroom17 with dissolve
    an "Did you notice that I took my angelic bodysuit off for you?"
    mc "I sure did, Angela! My cock is ROCK-HARD at the sight of your lovely breasts!"
    scene angelaroom18 with dissolve
    an "You're such a sweet [age]yo boy! So very romantic. And so very HORNY! You deserve a HEAVENLY FUCK!"
    window hide
    
    label AngelaFuckSlow: 
    stop channel2
    play channel2 "sounds/womansex06.mp3"
    hide cum
    hide faster
    hide slower
    show angelafuckslowvideo behind angelafuckfastvideo
    pause 1.0
    hide angelafuckfastvideo with dissolve
    if angelafucktold == False:
        an "Do you like my pussy? Is it tight enough to give you lots of HEAVENLY PLEASURE?"
        mc "Ggg... It sure is..."
        window hide
        $ angelafucktold = True
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     

    call screen angelafuckslow()
    screen angelafuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AngelaFuckFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AngelaFuckEnd")

    label AngelaFuckFast:
    show angelafuckfastvideo behind angelafuckslowvideo
    hide cum
    hide faster
    hide slower
    an "What if I rode you even FASTER? Would you enjoy this better, young hero?"
    mc "YY... Yes... Angela!"
    hide angelafuckslowvideo with dissolve
    stop channel1
    play channel2 "sounds/womansex06.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     

    call screen angelafuckfast()
    screen angelafuckfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AngelaFuckSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AngelaFuckEnd")

    label AngelaFuckEnd:    
    hide cum
    hide slower
    hide faster
    an "Are you going to blow your HUGE load, my sweet young hero?"
    mc "Y... Yes, just about to..."
    scene angelafuckcum01 with dissolve
    stop channel1
    stop channel2
    play channel1 "v031/boyorgasm02.mp3"
    mc "...CUUU-UUU-M! AAAH!"
    window hide 
    with hpunch
    an "Mmmh, I can FEEL IT! But I want it DEEPER in my pussy!"
    scene angelafuckcum02 with dissolve    
    if age >= 20:
        an "Like THIS! So you can drive your convulsing giant dong all the way up my angelic fuckhole!"
    if age >= 18 and age <= 19:
        an "Like THIS! So you can drive your convulsing giant teenage dong all the way up my angelic fuckhole!"
    window hide
    with fastflash
    mc "God, you're pussy is so TIGHT! RHAAA!"
    scene angelafuckcum03 with dissolve
    an "You shouldn't invoke Her Name while you're cumming inside an angel, that's just NAUGHTY!"
    window hide
    with vpunch
    mc "Sorry, oh Lord, oh Lord, AAAH!"
    scene angelafuckcum04 with dissolve
    an "But... You're waking up? So SOON?!?!"
    mc "I...err..."
    stop music
    stop channel1
    stop channel2
    scene mcwakecumlevel02 with fade
    show screen calendar
    show screen statscreenicon
    show screen questscreenicon
    mc "Oh shit, it wasn't real after all... And I came all over myself instead of inside Angela's angelic twat... * sigh *"
    jump NewDay

if evilness >= 18 and dreamdemon >= 7 and mclevel02:
    $ dreamdemon = 0   
    hide screen calendar
    hide screen statscreenicon
    hide screen questscreenicon
    scene intromcsleep02
    with dissolve
    play sound "sounds/dream.mp3"
    $ renpy.pause(1.0, hard='True')
    play music "sounds/introdreaming.mp3"
    show demona02a at topright with moveinright
    hide demona02a
    show demonafly02 at topright
    de "Hey wake up, [hero]!"
    menu:
        "See scene":
            pass
        "Skip scene":
            stop music
            jump NewDay            
    scene intromcsleep02a
    show intromcsleep02c
    with dissolve
    hide demonafly02 with dissolve
    mc "But... You're gone?"
    de "I'm still here, just REALLY open your eyes and look down this time..."
    stop music
    play sound "sounds/demon.mp3"
    scene demonaroom11 with fade
    mc "Is... Is this for real?"
    de "Maybe. Maybe not. Who cares?"
    scene demonaroom12 with dissolve
    stop sound
    play music "sounds/sexy13.mp3"
    if ivyharem == False or tolddemonaharem:
        de "What's important right now is that you have a GIANT 18-inch cum-cannon that needs some DEMONIC release!"
    if ivyharem and tolddemonaharem == False:
        de "What's important right now is that you got yourself a new WHORE for your EVIL HAREM!"
        mc "Ah yes, Poison Ivy. Although her tits have gone back to their normal size now that she's in my harem..."
        $ tolddemonaharem = True
    scene demonaroom13 with dissolve
    if age >= 20:
        de "And since you've been such a NAUGHTY boy, I'm absolutely POSSESSED by your behemoth dong!"
    if age >= 18 and age <= 19:
        de "And since you've been such a NAUGHTY boy, I'm absolutely POSSESSED by your behemoth teen dong!"
    mc "Y... You are? So you're going to let me pummel your backdoor, right?"
    scene demonaroom14 with dissolve
    de "What is it with you and your obsession with ass-fucking me? It's just not healthy."
    mc "Well, err..."
    scene demonaroom15 with dissolve
    de "There might be a stairway to heavens in most VN games, but right now, you're on the slide down to HELL!"
    scene demonaroom16 with dissolve
    de "Therefore, you're allowed to fuck my PUSSY. But let ME do the RIDING, cowboy!"
    scene demonaroom17 with dissolve
    play sound "sounds/moan05.mp3"
    if age >= 20:
        de "Dear Beelzebub, I didn't expect such a... HUGE monstercock on such a young [age]yo man! But it's my job to entice young STALLIONS, so let's DO IT!"
    if age >= 18 and age <= 19:
        de "Dear Beelzebub, I didn't expect such a... HUGE monstercock on such a young [age]yo teenage boy! But it's my job to entice young STALLIONS, so let's DO IT!"
    window hide
    
    label DemonaFuckSlow: 
    stop channel2
    play channel2 "sounds/womansex06.mp3"
    hide cum
    hide faster
    hide slower
    show demonafuckslowvideo behind demonafuckfastvideo
    pause 1.0
    hide demonafuckfastvideo with dissolve
    if demonafucktold == False:
        mc "Damn, your pussy is SCALDING HOT!"
        de "That's right, its walls are lined with embers from the INFERNO OF HELL!"
        window hide
        $ demonafucktold = True
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     

    call screen demonafuckslow()
    screen demonafuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("DemonaFuckFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("DemonaFuckEnd")

    label DemonaFuckFast:
    show demonafuckfastvideo behind demonafuckslowvideo
    hide cum
    hide faster
    hide slower
    mc "Oh please... Fuck me faster, I need to come!"
    hide demonafuckslowvideo with dissolve
    stop channel1
    play channel2 "sounds/womansex06.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     

    call screen demonafuckfast()
    screen demonafuckfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("DemonaFuckSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("DemonaFuckEnd")

    label DemonaFuckEnd:    
    hide cum
    hide slower
    hide faster
    de "It's time for you to FILL ME UP with your SPUNK!"
    scene demonacum01 with dissolve
    stop channel1
    stop channel2
    play channel1 "v031/boyorgasm02.mp3"
    de "That's it, let it EXPLODE out of your cumslit and into my hungry snatch!"
    window hide 
    with hpunch
    mc "AAAAH! Your pussy is so tight!"
    scene demonacum02 with dissolve
    if age >= 20:
        de "That's cos I'm CLAMPING down on your convulsing dong while you're cumming!"
    if age >= 18 and age <= 19:
        de "That's cos I'm CLAMPING down on your convulsing teenage dong while you're cumming!"
    window hide
    with fastflash
    mc "That's so NAAAA-AAASTY! UUUHH!"
    scene demonacum03 with dissolve
    de "DEEPER! FLOOD my 6500yo uterus!"
    window hide
    with vpunch
    mc "OH MY GOD, YOUR PUSSY IS LIKE A VICE! AAAH!"
    scene demonacum04 with dissolve
    play sound "sounds/moan04.ogg"
    de "Just there... just there, I'm gonna cum too!"
    scene demonacum05 with dissolve
    de "You're such an evil jerk! You're waking up just when I was getting MY rocks off!"
    mc "I...err..."
    stop music
    stop channel1
    stop channel2
    scene mcwakecumlevel02 with fade
    show screen calendar
    show screen statscreenicon
    show screen questscreenicon
    mc "Oh shit, it wasn't real after all... And I came all over myself instead of inside Demona's hellish twat... * sigh *"
    jump NewDay

label NewDay:
if evilness <= 5 and dreamangel <= 7:
    $ dreamangel += 1 
if evilness >= 13 and dreamdemon <= 7:
    $ dreamdemon += 1
$ day +=1
$ period = 0

$ seenpool = False
$ seengym = False
$ seenlibrary = False
$ seenhall = False
$ agstink += 1
if questhulkcompleted:
    $ hulksexneed += 1
    
if mission01 and mission01end == False:
    $ mission01day += 1
if mission03 and mission03end == False:
    $ mission03day += 1
if mission04 and mission04end == False:
    $ mission04day += 1
if mission05 and mission05end == False:
    $ mission05day += 1
if mission06 and mission06end == False:
    $ mission06day += 1
if mission04win and mcagility >= 1 and mccombat >= 1 and seenstroheimwonder == False:
    jump StroheimWonder
    
$ d10locday = renpy.random.randint(1,10)
$ d10locnight = renpy.random.randint(1,10)
$ d10locnightpoolmilf = renpy.random.randint(1,2)
$ d10locnightpgroom = renpy.random.randint(1,2)
if mission05end == False and mission05 and seenembassy:
        $ d10locnight = 5

if mclevel02 == False:
    scene mcwake01:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.04
    with fade
if mclevel02:
    scene mcwakelevel02 with fade
play sound "sounds/yawn.mp3"
pause
stop sound

if mcsenses >= 1 and mcagility >= 1 and mcseduction >= 2 and mcstrength >= 2 and (mccombat >= 2 or mcmind >= 1) and seenstroheimwonder and supergirltraining and (seenmilfgymendlevel01 == False or not mclevel02) and locquiff == False:
    if lpspeakhq01:
        mc "My Super-Senses tell me it would be a good idea to go on the beat woth Captain Sawyer to Porkher Row. Like TODAY. So I can unlock levelling up..."
    if lpspeakhq01 == False:
        mc "My Super-Senses tell me it would be a good idea to gatehr some info on Harley Quiff from Lois Pane at the Cockham Planet. Like TODAY. So I can unlock levelling up..."

if mission06end and quest07end and mission07 == False and mission07win == False and harleypicture == False:
    mc "My Super-Senses tell me it would be a good idea to visit the lingerie store. Like TODAY. So I can unlock mission07..."

if mission05end and quest06end and mission06 == False and evilness >= 6 and evilness <= 12:
    mc "It seems I might have screwed up by not picking a route, which I really should have done at this stage of the game..."
    mc "But the dev, in all his magnanimity, is me allowing to pick one now so I can continue the game and not be stuck..."
    menu:
        "Pick Hero route.":
            $ evilness = 3
        "Pick Villain route.":
            $ evilness = 15
    if evilness <= 5 and wondertalkpregnant:
        mc "Now I can finally start mission06 by talking to Captain MILF in the Hall..."
    if evilness <= 5 and wondertalkpregnant == False:
        mc "Now I should talk to Wonder Woman about her pregancy some more, then to Captain MILF in the Hall to finally start mission06..."
    if evilness >= 15 and frostfucked:
        mc "Now I can finally start mission06 by talking to Emma Frost in her office..."
    if evilness >= 15 and not frostfucked:
        mc "Now I need to visit Emma Frost, fuck her, and then go and visit her again to finally start mission06..."

if seensupergirl and seensuperpowergirl and supergirltraining == False:
    mc "Okay, time for me to TRAIN with Supergirl. First on my list is going on the beat with her. Let's head to the hall."
    $ supergirltraining = True
    jump SuperGirlDay01

if mission02end and milftoldmission02end == False:
    mc "Maybe I should go to the main Hall for a mission de-briefing."
    jump CompoundHallMILF

if mission03day >= 5 and mission03end == False:
    mc "Uh ho, it looks like I screwed up my mission... It's been over four days now. Carol ain't gonna be happy..."
    scene compoundhall01d
    show compoundmilf02
    with fade
    cm "Ah, there you are. The Mayor called me. You STILL haven't resolved this important mission I put you in charge of!"
    mc "Oh, really? How time flies."
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve
    cm "I'm so disappointed in you, [name]..."
    show missionicon03 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission03fail = True
    $ mission03end = True
    mc "I'm sorry Captain MILF, it won't happen again..."
    hide compoundmilf06
    show compoundmilf05
    with fastdissolve
    cm "It better not! How can you expect to become the ULTIMATE superhero if you fail your missions?"
    call Evil
    cm "Now go back to your room, you are GROUNDED. Until the evening."
    mc "What???? I'm grounded? Can you even do that to a tenant?"
    jump Main

if mission05day >= 4 and mission05end == False:
    mc "Uh ho, it looks like I screwed up my mission... It's been over three days now. Mom ain't gonna be happy..."
    scene compoundhall01d
    show compoundmilf02
    with fade
    cm "Ah, there you are. I just saw Natasha. And she called me an imperialist swine! You FAILED to de-program her and now she turned into a leftist radical!"
    mc "Damn those commies. I knew they couldn't be trusted."
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve
    cm "I'm so disappointed in you, son..."
    show missionicon05 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission05fail = True
    $ mission05end = True
    mc "I'm sorry mom, it won't happen again..."
    hide compoundmilf06
    show compoundmilf05
    with fastdissolve
    cm "It better not! How can you expect to become the ULTIMATE superhero if you fail your missions?"
    cm "Now go back to your room, you are GROUNDED. Until the evening."
    mc "What???? I'm grounded? Can you even do that to a superhero?"
    jump Main

if questhulkcompleted and hulkescaped == False:
    if hulksexneed == 6:
        mc "Maybe I should think about visiting the She-Hulk to satisfy her sexual needs or she might go berserk again..."
        jump MCRoomDay

    if hulksexneed == 8:
        $ hulkescaped = True
        mc "I think I might have screwed up. By not screwing She-Hulk lately... I need to go to the Hall to check if everything is still fine and dandy..."
        scene compoundhall01d
        show compoundmilf02
        with fade
        cm "Ah, there you are. Things are NOT fine and dandy around town!"
        mc "Uh oh..."
        hide compoundmilf02
        show compoundmilf06
        with fastdissolve
        cm "You were in charge of keeping She-Hulk UNDER CONTROL! And now she left the compound and has wreaked havoc around town!"
        mc "I'm sorry Captain MILF, I was... distracted this week..."
        hide compoundmilf06
        show compoundmilf05
        with fastdissolve
        cm "If a Super-Villain gets a hold on her, God knows what will happen! Get a grip for once in your life,[name]!"
        jump MCRoomDay

if questhulkcompleted and seensupergirl == False:
    $ seensupergirl = True
    mc "I heard that Supergirl would be arriving today for an internship in our League. So let's go straight to the Hall to be part of the welcoming party."
    scene compoundhall01d
    show compoundmilf02 at farright
    with fade
    cm "You are just in time to welcome Supergirl. She just flew in from Smallcoxville this morning."
    window hide
    show sgirl01 with moveinleft
    show pgirl02 at farleft02 with moveinleft
    sg "Howdy, [name]. I heard a LOT about you."
    mc "I bet you did, I bet you did. * wink *"
    hide sgirl01
    show sgirl02 behind pgirl01
    with fastdissolve
    sg "Not necessarily GOOD things I might add..."
    hide pgirl02
    show pgirl01 at farleft
    with fastdissolve
    pg "Supergirl is my very, very distant cousin and her name is also Kara because the people at DC can't seem to make up their minds about who either of us is."
    hide sgirl02
    show sgirl01 behind pgirl01
    with fastdissolve
    sg "But you can call me Linda. So that it doesn't get too confusing."
    hide compoundmilf02
    show compoundmilf06 at farright behind sgirl01
    with fastdissolve
    cm "Kar..., I mean, Linda will be doing a rotation amongst League members. She'll start of by being paired with Powergirl."
    hide sgirl01
    show sgirl03 behind pgirl01
    with fastdissolve
    sg "I'm real excited about learning the ropes here. Nothing interesting ever happens in Smallcoxville..."
    hide compoundmilf06
    show compoundmilf05 at farright behind sgirl03
    with fastdissolve
    cm "Of course, you are not to disturb her until your turn comes to be paired with her, understood?"
    hide pgirl01
    show pgirl02 at farleft02
    with fastdissolve
    pg "Especially since she will first be paired with ME."
    mc "Yep, got it, Captain MILF!"
    jump MCRoomDay

label MainTime:
stop channel1
stop channel2
stop music
if period == 0:
    jump MCRoomDay
if period >= 1:
    jump MCRoomNight
    
label Main:
stop channel1
stop channel2
stop music
if period == 0:
    $ period += 1
    jump MCRoomNight
if period >= 1:
    jump MCSleep

label MCRoomDay:
scene mcroombase with fade
show screen calendar
mc "What should I do today?..."
if seenstroheimwonder and questhulk == False:
    mc "I'm thinking. Maybe I should surprise Lara by visiting her. Even if it says she's not around..."
if mission04win and mcagility == 0 and seenstroheimwonder == False and seenwonderbeast == False:
    mc "I feel a need for some muscle SEXY BEAST sparring with Wonder Woman. In the gym when she's around. Like RIGHT NOW."
    $ d10locday = 8
if mission04win and mcagility == 0 and seenstroheimwonder == False and seenwonderbeast:
    mc "I feel... clumsy and slow. I need to train in Super-Agility. With Wonder Woman in the gym when she's around. Like RIGHT NOW."    
    $ d10locday = 8
if mission04win and mccombat == 0 and seenstroheimwonder == False:
    mc "I feel... weak and not willing to fight anymore. I need to train in Super-Combat. With the Black Widow in the gym in the evening when she's around. And she will be tonight."
    $ d10locnight = 9
    
call screen locchoiceday()
screen locchoiceday():
    modal True
    add "icons/passtime.png"
    button:
        xpos 1720
        ypos 1020
        xysize(200, 70)        
        action [Jump ("Main")]
    imagebutton:
        focus_mask True
        idle "icons/mcroomjacuzziidle.png"
        hover "icons/mcroomjacuzzihover.png"
        action Jump ("MCJacuzzi")
    imagebutton:
        focus_mask True
        idle "icons/mcroomshoweridle.png"
        hover "icons/mcroomshowerhover.png"
        action Jump ("MCShower")
    imagebutton:
        focus_mask True
        idle "icons/statsiconscreenidle.png"
        hover "icons/statsiconscreenhover.png"
        action ui.callsinnewcontext("Statscreen")
    imagebutton:
        focus_mask True
        idle "icons/questsiconscreenidle.png"
        hover "icons/questsiconscreenhover.png"
        action ui.callsinnewcontext("Questscreen")

    add "icons/placegym.png" at posgym
    button:
        xpos .25
        ypos .09
        xysize(140, 130)        
        action Jump ("CompoundGym")
    if d10locday == 5 or d10locday == 6:
        add "icons/loccm.png" at posgym01
    if d10locday == 7:
        add "icons/locbw.png" at posgym01        
    if d10locday >= 9:
        add "icons/locpg.png" at posgym01        
    if d10locday == 8:
        add "icons/locww.png" at posgym01        
    if d10locday <= 1 and mclevel02 == False:
        add "icons/locsm.png" at posgym01        
    if d10locday <= 3 and mclevel02:
        add "icons/locag.png" at posgym01        

    add "icons/placehall.png" at poshall
    button:
        xpos .05
        ypos .09
        xysize(140, 130)        
        action Jump ("CompoundHallDay")
    if d10locday >= 7 and ((mission01end and mission02 == False) or (milftoldmission02end and mission03 == False)):
        add "loccmblink" at poshall01        

    if d10locday == 9 or d10locday == 10 and (mission01end == False or mission02 or milftoldmission02end == False or mission03):
        add "icons/loccm.png" at poshall01
        add "icons/locag.png" at poshall02
    if d10locday >= 7 and (mission01end == False or mission02 or milftoldmission02end == False or mission03):
        add "icons/loccm.png" at poshall01        
#    if d10locday == 3 or d10locday == 4:
#        add "icons/locbw.png" at poshall01

    add "icons/placepool.png" at pospool
    button:
        xpos .15
        ypos .09
        xysize(140, 130)        
        action Jump ("CompoundPoolDay")
    if d10locday == 3 or d10locday == 4:
        add "icons/loccm.png" at pospool01
    if d10locday == 5 or d10locday == 6:
        add "icons/locbw.png" at pospool01
    if d10locday == 7 or d10locday == 8 and mclevel02:
        add "icons/locpg.png" at pospool01

    add "icons/placelibrary.png" at poslib      
    button:
        xpos .35
        ypos .09
        xysize(140, 130)        
        action Jump ("CompoundLibrary")
    if d10locday <= 8 and mclevel02 == False:
        add "icons/locag.png" at poslib01
    if d10locday >= 4 and  d10locday <= 5 and mclevel02:
        add "icons/locag.png" at poslib01
    if d10locday == 1 or d10locday == 2:
        add "icons/loccm.png" at poslib02
        
#    add "icons/placebwroom.png" at posbwr        
#    button:
#        xpos .06
#        ypos .26
#        xysize(140, 130)        
#        action Jump ("BWRoomDay")
    add "icons/placebwroomgrey.png" at posbwr 

    add "icons/placecmroom.png" at poscmr      
    button:
        xpos .16
        ypos .26
        xysize(140, 130)        
        action Jump ("CMRoomDay")
        
    add "icons/placepgroom.png" at pospgr      
    button:
        xpos .26
        ypos .26
        xysize(140, 130)        
        action Jump ("PGRoomDay")
    if d10locday >= 2 and d10locday <= 4:
        add "icons/locpg.png" at pospgr

    add "icons/placewwroom.png" at poswwr      
    button:
        xpos .36
        ypos .26
        xysize(140, 130)        
        action Jump ("WWRoomDay")
    if d10locday <= 3 and wonderbirth:
        add "icons/locww.png" at poswwr
    if d10locday >= 4 and  d10locday <= 6 and wonderbirth:
        add "icons/locag.png" at poswwr

    add "icons/placelara.png" at poslcr      
    button:
        xpos .46
        ypos .26
        xysize(140, 130)
        if any([seenstroheimwonder and not hulkescaped, hulkharem]):
            action Jump ("HulkCompound")
        else:
            action Jump ("LaraRoomDay")

    if any([questhulk and not hulkescaped, hulkharem]):
        add "icons/lochu.png" at poslcr01

    add "icons/placecockham.png" at posmap     
    button:
        xpos .5
        ypos .6
        xysize(280, 230)        
        action Jump ("CockhamMapDay")

label MCRoomNight:
stop music
scene mcroombase with fade
show screen calendar
mc "What should I do this evening?..."
call screen locchoicenight()
screen locchoicenight():
    modal True
    imagebutton:
        focus_mask True
        idle "icons/mcroombedidle.png"
        hover "icons/mcroombedhover.png"
        action Jump ("MCSleep")
    imagebutton:
        focus_mask True
        idle "icons/mcroomjacuzziidle.png"
        hover "icons/mcroomjacuzzihover.png"
        action Jump ("MCJacuzzi")
    imagebutton:
        focus_mask True
        idle "icons/mcroomshoweridle.png"
        hover "icons/mcroomshowerhover.png"
        action Jump ("MCShower")
    imagebutton:
        focus_mask True
        idle "icons/statsiconscreenidle.png"
        hover "icons/statsiconscreenhover.png"
        action ui.callsinnewcontext("Statscreen")
    imagebutton:
        focus_mask True
        idle "icons/questsiconscreenidle.png"
        hover "icons/questsiconscreenhover.png"
        action ui.callsinnewcontext("Questscreen")

    if seengym:
        add "icons/placegymgrey.png" at posgym
    if seengym == False:    
        add "icons/placegym.png" at posgym
        button:
            xpos .25
            ypos .09
            xysize(140, 130)        
            action Jump ("CompoundGym")
        if (d10locnight == 5 or d10locnight == 6) and (mcagility == 0 or mcsenses == 0 or mcstrength == 1 or (mccombat <= 1 and mcmind == 0) or seenstroheimwonder == False or supergirltraining == False or mclevel02 == True):
            add "icons/loccm.png" at posgym01        
        if (d10locnight == 5 or d10locnight == 6) and mcsenses >= 1 and mcagility >= 1 and mcstrength >= 2 and (mccombat >= 2 or mcmind >= 1) and seenstroheimwonder and supergirltraining and seenmilfgymendlevel01 == False and sawharley:
            add "loccmblink" at posgym01        
        if d10locnight == 9 or d10locnight == 10:
            add "icons/locbw.png" at posgym01        
        if d10locnight == 7 or d10locnight == 8:
            add "icons/locww.png" at posgym01        
        if d10locnight <= 1:
            add "icons/locpg.png" at posgym01        

    add "icons/placehall.png" at poshall
    button:
        xpos .05
        ypos .09
        xysize(140, 130)        
        action Jump ("CompoundHallNight")
    if d10locnight == 1 or d10locnight == 2:
        add "icons/locag.png" at poshall01
    if d10locnight == 9:
        add "icons/loccm.png" at poshall01
    if d10locnight == 3 or d10locnight == 4:
        add "icons/locsm.png" at poshall01

    if seenpool:
        add "icons/placepoolgrey.png" at pospool

    if seenpool == False:
        add "icons/placepool.png" at pospool
        button:
            xpos .15
            ypos .09
            xysize(140, 130)        
            action Jump ("CompoundPoolNight")
    if d10locnight == 1 or d10locnight == 10:
        add "icons/loccm.png" at pospool01
#    if d10locnight == 6:
#        add "icons/locww.png" at pospool01
    if d10locnight == 2 or d10locnight == 8:
        add "icons/locbw.png" at pospool01
    if d10locnight == 3 or d10locnight == 4:
        add "icons/locpg.png" at pospool01
            
    if seenlibrary:
        add "icons/placelibrarygrey.png" at poslib

    if seenlibrary == False:
        add "icons/placelibrary.png" at poslib      
        button:
            xpos .35
            ypos .09
            xysize(140, 130)        
            action Jump ("CompoundLibrary")
        if d10locnight >= 3:
            add "icons/locag.png" at poslib01
        if d10locnight == 7:
            add "icons/loccm.png" at poslib02
        
    add "icons/placebwroom.png" at posbwr        
    button:
        xpos .06
        ypos .26
        xysize(140, 130)        
        action Jump ("BWRoomNight")
    if d10locnight >= 4 and d10locnight <= 7:
        add "icons/locbw.png" at posbwr01

    add "icons/placecmroom.png" at poscmr      
    button:
        xpos .16
        ypos .26
        xysize(140, 130)        
        action Jump ("CMRoomNight")
    if d10locnight == 2 or d10locnight == 3 or d10locnight == 4 or d10locnight == 8:
        add "icons/loccm.png" at poscmr01
        
    add "icons/placepgroom.png" at pospgr      
    button:
        xpos .26
        ypos .26
        xysize(140, 130)        
        action Jump ("PGRoomNight")
    if d10locnight >= 6:
        add "icons/locpg.png" at pospgr01
    if seensupergirl and seensuperpowergirl == False:
        add "icons/locpg.png" at pospgr01
        add "v03/locsg.png" at pospgr02        

    add "icons/placewwroom.png" at poswwr      
    button:
        xpos .36
        ypos .26
        xysize(140, 130)        
        action Jump ("WWRoomNight")
    if d10locnight == 1 or d10locnight == 2 or d10locnight == 9 or d10locnight == 10:
        add "icons/locww.png" at poswwr01

    add "icons/placelara.png" at poslcr      
    button:
        xpos .46
        ypos .26
        xysize(140, 130)        
        action Jump ("LaraRoomNight")
    if d10locnight >= 5 and d10locnight <= 10:
        add "icons/loclc.png" at poslcr01

    add "icons/placecockham.png" at posmap     
    button:
        xpos .5
        ypos .6
        xysize(280, 230)        
        action Jump ("CockhamMapNight")
        
label MCShower:
stop music
if mclevel02 == False:
    scene intromcshower01:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.04
    with fade
if mclevel02:
    scene mcshowerlevel02a:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.1
    with fade
play music "sounds/shower.mp3"
mc "Mmh yeah, that hot water is clearing my mind..."
if mclevel02 == False:
    scene intromcshower02 with dissolve
if mclevel02:
    scene mcshowerlevel02b with dissolve
mc "Just a while longer..."
stop music
jump MainTime
    
label MCJacuzzi:
stop music
if mclevel02 == False:
    scene mcjacuzzi00 with dissolve
    mc "Mmmh, the water is already nice and warm, this is going to be very relaxing..."
    play channel1 "sounds/jacuzzi.mp3"
    scene mcjacuzzi01 with dissolve
    mc "Ah yeah, I needed that..."
    scene mcjacuzzi02 with dissolve
    mc "God this is making me ROCK-HARD... Gotta take the edge of this massive erection..."
    play sound "sounds/dream.mp3"
    scene mcjacuzzi03
    
if mclevel02:
    play channel1 "sounds/jacuzzi.mp3"
    scene mcwanklevel02a:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.1        
    with dissolve
    mc "Ah yeah, I needed that..."
    scene mcwanklevel02b with dissolve
    mc "God this is making me ROCK-HARD... Gotta take the edge of this massive erection..."
    play sound "sounds/dream.mp3"
    scene mcwanklevel02c

$ d6dreamgirl = renpy.random.randint(1,11)
if d6dreamgirl == 1:
    if mclevel02 == False:
        show milfdream01 at posdream
    if mclevel02:
        show milfdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Fuck yeah, nice MILF tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show milfdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show milfdream at posdream02
    with dissolve
if d6dreamgirl == 2:
    if mclevel02 == False:
        show widowdream01 at posdream
    if mclevel02:
        show widowdream01 at posdream02
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Ooh yeah, big fat tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show widowdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show widowdream at posdream02
    with dissolve
if d6dreamgirl == 3:
    if mclevel02 == False:
        show frostdream01 at posdream
    if mclevel02:
        show frostdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, super-evil super-tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show frostdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show frostdream at posdream02
    with dissolve
if d6dreamgirl == 4:
    if mclevel02 == False:
        show powerdream01 at posdream
    if mclevel02:
        show powerdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, young firm tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show powerdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show powerdream at posdream02
    with dissolve
if d6dreamgirl == 5:
    if mclevel02 == False:
        show wonderdream01 at posdream
    if mclevel02:
        show wonderdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, wonderful tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show wonderdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show wonderdream at posdream02
    with dissolve
if d6dreamgirl == 6:
    if mclevel02 == False:
        show auditdream01 at posdream
    if mclevel02:
        show auditdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, giant monster tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show auditdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show auditdream at posdream02
    with dissolve
if d6dreamgirl == 7:
    if mclevel02 == False:
        show laradream01 at posdream
    if mclevel02:
        show laradream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, enhanced video game babe tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show laradream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show laradream at posdream02
    with dissolve
if d6dreamgirl == 8:
    $ seenangeladream = True
    if mclevel02 == False:
        show angeladream01 at posdream
    if mclevel02:
        show angeladream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Sexy angel tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show angeladream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show angeladream at posdream02
    with dissolve
if d6dreamgirl == 9:
    if mclevel02 == False:
        show demonadream01 at posdream
    if mclevel02:
        show demonadream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Mmmh, tiddies from Hell..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show demonadream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show demonadream at posdream02
    with dissolve
if d6dreamgirl == 10:
    if mclevel02 == False:
        show sawyerdream01 at posdream
    if mclevel02:
        show sawyerdream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Yeah, black MILF tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show sawyerdream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show sawyerdream at posdream02
    with dissolve
if d6dreamgirl == 11:
    if mclevel02 == False:
        show supergirldream01 at posdream
    if mclevel02:
        show supergirldream01 at posdream02
    with dissolve
    stop channel1
    play channel1 "sounds/sexy04.mp3"
    mc "Yeah, super-tiddies..."
    play channel2 "sounds/wank.mp3"
    if mclevel02 == False:
        scene jacuzzijo
        show supergirldream at posdream
    if mclevel02:
        scene jacuzzijolevel02
        show supergirldream at posdream02
    with dissolve
window hide
pause
mc "Oh God... It's coming..."
if mclevel02 == False:
    scene jacuzzijofast with fastdissolve
    if d6dreamgirl == 1:
        show milfdream01 at posdream
    if d6dreamgirl == 2:
        show widowdream01 at posdream
    if d6dreamgirl == 3:
        show frostdream01 at posdream
    if d6dreamgirl == 4:
        show powerdream01 at posdream
    if d6dreamgirl == 5:
        show wonderdream01 at posdream
    if d6dreamgirl == 6:
        show auditdream01 at posdream
    if d6dreamgirl == 7:
        show laradream01 at posdream
    if d6dreamgirl == 8:
        show angeladream01 at posdream
    if d6dreamgirl == 9:
        show demonadream01 at posdream
    if d6dreamgirl == 10:
        show sawyerdream01 at posdream
    if d6dreamgirl == 11:
        show supergirldream01 at posdream
if mclevel02:
    scene jacuzzijofastlevel02 with fastdissolve
    if d6dreamgirl == 1:
        show milfdream01 at posdream02
    if d6dreamgirl == 2:
        show widowdream01 at posdream02
    if d6dreamgirl == 3:
        show frostdream01 at posdream02
    if d6dreamgirl == 4:
        show powerdream01 at posdream02
    if d6dreamgirl == 5:
        show wonderdream01 at posdream02
    if d6dreamgirl == 6:
        show auditdream01 at posdream02
    if d6dreamgirl == 7:
        show laradream01 at posdream02
    if d6dreamgirl == 8:
        show angeladream01 at posdream02
    if d6dreamgirl == 9:
        show demonadream01 at posdream02
    if d6dreamgirl == 10:
        show sawyerdream01 at posdream02
    if d6dreamgirl == 11:
        show supergirldream01 at posdream02
window hide
$ renpy.pause(3.0, hard='True')
stop channel2
if mclevel02 == False:
    scene mcjacuzzi05 with dissolve
    if d6dreamgirl == 1:
        show milfdream05 at posdream
    if d6dreamgirl == 2:
        show widowdream05 at posdream
    if d6dreamgirl == 3:
        show frostdream05 at posdream
    if d6dreamgirl == 4:
        show powerdream05 at posdream
    if d6dreamgirl == 5:
        show wonderdream05 at posdream
    if d6dreamgirl == 6:
        show auditdream05 at posdream
    if d6dreamgirl == 7:
        show laradream05 at posdream
    if d6dreamgirl == 8:
        show angeladream05 at posdream
    if d6dreamgirl == 9:
        show demonadream05 at posdream
    if d6dreamgirl == 10:
        show sawyerdream05 at posdream
    if d6dreamgirl == 11:
        show supergirldream05 at posdream
if mclevel02:
    scene mcwanklevel02e with dissolve
    if d6dreamgirl == 1:
        show milfdream05 at posdream02
    if d6dreamgirl == 2:
        show widowdream05 at posdream02
    if d6dreamgirl == 3:
        show frostdream05 at posdream02
    if d6dreamgirl == 4:
        show powerdream05 at posdream02
    if d6dreamgirl == 5:
        show wonderdream05 at posdream02
    if d6dreamgirl == 6:
        show auditdream05 at posdream02
    if d6dreamgirl == 7:
        show laradream05 at posdream02
    if d6dreamgirl == 8:
        show angeladream05 at posdream02
    if d6dreamgirl == 9:
        show demonadream05 at posdream02
    if d6dreamgirl == 10:
        show sawyerdream05 at posdream02
    if d6dreamgirl == 11:
        show supergirldream05 at posdream02
play sound "sounds/boymoan02.mp3"
mc "AAAH..."
window hide
with fastflash
mc "Cumming big time!"
if mclevel02 == False:
    scene mcjacuzzi06 with dissolve
if mclevel02:
    scene mcwanklevel02f with dissolve
play sound "sounds/boymoan.mp3"
mc "FU-U-UCK!"
window hide
with fastflash
mc "CUMMING EVERYWHERE, RHAAA!"
stop channel1
if mclevel02 == False:
    scene mcjacuzzi07 with dissolve
if mclevel02:
    scene mcwanklevel02g with dissolve
play sound "sounds/panting.mp3"
mc "Damn that was good..."
if d6dreamgirl == 9 and demonawankevil == False:
    call Evil
    $ demonawankevil = True
    mc "And evil apparently..."
if period == 0:
    mc "And it was LONG and took AGES. So much so that it's already the evening..."
if period == 1:
    mc "And it was LONG and took AGES. So much so that it's already time to go to bed..."
jump Main

label SensesPlus:
window hide
play sound "sounds/achievement.mp3"
show supersensesplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide supersensesplus
$ mcsenses += 1
return

label CombatPlus:
window hide
play sound "sounds/achievement.mp3"
show supercombatplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide supercombatplus
$ mccombat += 1
return

label AgilityPlus:
window hide
play sound "sounds/achievement.mp3"
show superagilityplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superagilityplus
$ mcagility += 1
return

label ResistancePlus:
window hide
play sound "sounds/achievement.mp3"
show superresistanceplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superresistanceplus
$ mcresistance += 1
return

label StrengthPlus:
window hide
play sound "sounds/achievement.mp3"
show superstrengthplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superstrengthplus
$ mcstrength += 1
return

label HealingPlus:
window hide
play sound "sounds/achievement.mp3"
show superhealingplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superhealingplus
$ mchealing += 1
return

label SeductionPlus:
window hide
play sound "sounds/achievement.mp3"
show superseductionplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superseductionplus
$ mcseduction += 1
return

label ControlPlus:
window hide
play sound "sounds/achievement.mp3"
show supercontrolplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide supercontrolplus
$ mcmind += 1
return

label StudPlus:
window hide
play sound "sounds/achievement.mp3"
show superstudplus at poslocation
$ renpy.pause(0.5, hard='True')
pause
hide superstudplus
$ mcstud += 1
return

label AuditJacuzzi:
stop music
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ agstink = 0
scene auditjacuzzi01 with fade
mc "I'll get in first and turn the water heating up for you..."
ag "I'll... change in my bikini in the meantime then..."
play channel1 "sounds/jacuzzi.mp3"
scene auditjacuzzi02 with dissolve
ag "Is it warm yet? Can I get in?"
mc "Yeah, sure, it's the perfect temperature right now..."
play channel2 "sounds/sexy03.mp3"
scene auditjacuzzi03:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
mc "Damn fine fat booty right there..."
scene auditjacuzzi04 with dissolve
mc "Look at her, she looks so relaxed and peaceful..."
scene auditjacuzzi05 with dissolve
mc "Wakey, wakey! Time for that thorough CLEANING!"
ag "Uh, what? Oh... Yes, you're right..."
mc "You should take your top off to clean yourself properly."
ag "I... suppose you're right."
stop channel1
scene auditjacuzzi05b with dissolve
mc "* Bingo, she's going topless... *"
scene auditjacuzzi06:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "Don't look, this is embarrassing..."
mc "Well, turn round, then you won't see me looking..."
scene auditjacuzzi07:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
pause
scene auditjacuzzi08 with dissolve
ag "I just KNOW you're still looking. At my fat ass..."
mc "If you don't want me to look at your booty, then let me help you clean your breasts. I think it's a two-man job considering their size..." 
scene auditjacuzzi09 with dissolve
ag "What..., but... I just cleaned them, I don't think they nee..."
mc "But you didn't clean your nipples properly. And there's only one proper way to do it. With my tongue! So just sit back and let me do the job..."
ag "Al...alright, if you say so..."
scene auditjacuzzi10 with dissolve
mc "Try not to move as I suck up all the dirt from those fat nipples of yours..."
play channel1 "sounds/lick03.mp3"
scene auditjacuzzi11 with dissolve
play sound "sounds/moan01.mp3"
ag "Oooh, I can feel some...milk coming out...!"
scene auditjacuzzi12 with dissolve
mc "And I can taste it... Definitely yummy warm breastmilk!"
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
pause
scene auditjacuzzi13 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
ag "You're... MILKING ME! AAAH!"
scene auditjacuzzi14 with dissolve
mc "Damn, there was a LOT of milk in those fat udders of yours..."
scene auditjacuzzi14 with fastflash
play sound "sounds/splooge01.mp3"
ag "Plese don't say that, I'm not a cow!"
scene auditjacuzzi14b with dissolve
play sound "sounds/moan02.mp3"
mc "Now, there's still another place that might still be dirty and needs cleaning..."
ag "Wh... What? But where?...."
mc "Turn around and I'll show you where..."
scene auditjacuzzi15 with dissolve
mc "Let me take that bikini bottom off you."
ag "But... You'll expose my filthy snatch!"
mc "And if it's filthy, then it needs cleaning..."
scene auditjacuzzi16 with dissolve
mc "Damn, these are some FAT pussylips...!"
ag "Don't say that, this is just so embarrassing..."
mc "I'm gonna have to really stick my tongue in there to clean you up properly, Kayla!"
ag "O...Okay, but try and be quick please, it feels so LEWD!"
play channel1 "sounds/lick01.ogg"
window hide
show auditmunchvideo
with dissolve
$ renpy.pause(4.0, hard='True')
play sound "sounds/moan03.mp3"
ag "OOOH, your tongue... It's so... ROUGH!"
window hide
pause
scene auditjacuzzi17 with dissolve
play sound "sounds/splooge02.mp3"
ag "AAAH!"
scene auditjacuzzi18 with dissolve
mc "Damn girl, you're squirting BIG TIME!"
play sound "sounds/moan03.mp3"
window hide
with fastflash
ag "It's your fault, you made me do it, UUUH, AAAH!"
stop sound
stop channel1
scene auditjacuzzi19 with dissolve
mc "I reckon you're squeaky clean now, Kayla..."
ag "Thanks... I guess. Can I go now? I'm clean but I feel so... dirty."
menu:
    "Yes, you can go. You won't smell bad for another five days at least I reckon.":
        stop channel2
        show screen calendar
        show screen statscreenicon
        show screen questscreenicon
        jump Main        
    "Not so fast. The back of your womb needs cleaning. From my COCK! (+ 1 Super-Villain if not already obtained)":
        ag "You're...sure this is the correct way to do it?"
        scene auditfuckpre00 with dissolve
        mc "Abso-fucking-lutely! So turn round and stick that fat ass in the air. I'm going in!"
        if gotevilauditjacuzzi == False:
            call Evil
            $ gotevilauditjacuzzi = True
        pass

scene auditfuckpre01 with dissolve
mc "You'll see, once I'm done with your womb, it will be squeaky clean!"
scene auditfuckpre02 with dissolve
play sound "sounds/moan01.mp3"
ag "It's so BIG!"
mc "I'm not even halway in yet! Wait for the remaining 12 inches before you start moaning."
ag "TWELVE more inches! But..."
window hide

label AuditJacuzziSlowFuck:
window hide
show auditjacuzzislowvideo behind auditjacuzzifastvideo
show auditjacuzzislowvideo behind auditjacuzzipovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide auditjacuzzifastvideo
hide auditjacuzzipovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if toldauditjacuzzi == False:
    mc "I'll go slow at first to let you get used to my size..."
    $ toldauditjacuzzi = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen auditjacuzzifuckslow()
screen auditjacuzzifuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziFastFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSideSlow")

label AuditJacuzziFastFuck:
window hide
show auditjacuzzifastvideo behind auditjacuzzislowvideo
show auditjacuzzifastvideo behind auditjacuzzipovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide auditjacuzzislowvideo
hide auditjacuzzipovfastvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if age >= 20:
    ag "You're fucking me so HARD with your giant cock!"
if age >= 18 and age <= 19:
    ag "You're fucking me so HARD with your giant teen cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen auditjacuzzifuckfast()
screen auditjacuzzifuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSideFast")

label AuditJacuzziSideSlow:
window hide
show auditjacuzzipovslowvideo behind auditjacuzzislowvideo
show auditjacuzzipovslowvideo behind auditjacuzzipovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide auditjacuzzislowvideo
hide auditjacuzzipovfastvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen auditjacuzzisidefuckslow()
screen auditjacuzzisidefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSideFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSlowFuck")

label AuditJacuzziSideFast:
window hide
show auditjacuzzipovfastvideo behind auditjacuzzipovslowvideo
show auditjacuzzipovfastvideo behind auditjacuzzifastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide auditjacuzzifastvideo
hide auditjacuzzipovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if age >= 20:
    ag "You're fucking me so HARD with your giant cock!"
if age >= 18 and age <= 19:
    ag "You're fucking me so HARD with your giant teen cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen auditjacuzzisidefuckfast()
screen auditjacuzzisidefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSideSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziFastFuck")

label AuditJacuzziFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "I'm gonna clean your womb, Kayla!"
ag "How???"
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
scene auditjacuzzicum01 with dissolve
hide auditjacuzzipovfastvideo
hide auditjacuzzipovslowvideo
hide auditjacuzzifastvideo
hide auditjacuzzislowvideo
mc "Like this, RHAAAA!"
play sound "sounds/boymoan05.mp3"
window hide
with hpunch
ag "With your CUM? AAAAH!"
scene auditjacuzzicum02 with dissolve
ag "You're PUMPING your seed so DEE-EEP inside my womb!"
window hide
with fastflash
mc "Yeah, that's the idea, WHITEWASHING YOU! AAAH!"
scene auditjacuzzicum03 with dissolve
mc "Fuck yeah, need to BLOW some MOARRRR!"
play channel1 "sounds/boyorgasm01.mp3"
window hide
with hpunch
ag "My poor pussy, I'm FULL already!"
scene auditjacuzzicum04 with dissolve
stop channel1
play sound "sounds/moan02.mp3"
mc "Then I'll clean your back too with my SPECIAL GEL!!!"
window hide
with fastflash
ag "But I just cleaned myself back there! UUUGGHH!"
scene auditjacuzzicum05 with dissolve
mc "This is BETTER than your soap! At least for me! RHAAA!"
window hide
with hpunch
if age >= 20:
    ag "I'm getting DRENCHED with your filthy scum!"
if age >= 18 and age <= 19:
    ag "I'm getting DRENCHED with your filthy teenage scum!"
scene auditjacuzzicum06 with dissolve
stop channel1
mc "Phew, that was damn GOOD? Audit Girl..."
ag "You're very naughty, I didn't ask for this..."
play sound "sounds/slap.mp3"
scene auditjacuzzicum07 with dissolve
mc "I told you you had to get cleaned very THOROUGHLY..."
play channel1 "sounds/moan02.mp3"
play music [ "sounds/slap.mp3", "<silence .8>"]
scene auditjacuzzisplash
$ renpy.pause(3.0, hard='True')
pause
stop music
scene auditjacuzzicum08 with dissolve
ag "Mmmh, you're still spewing small aftershots on my back... I feel so DIRTY..."
mc "Then you need to CLEAN YOURSELF again!"
scene auditjacuzzicum09 with dissolve
mc "I was thinking, my shaft is dirty. And kinda reeks of cum...."
ag "Wh... What? You need to clean it then..."
mc "No, YOU need to clean it! With your TONGUE!"
ag "But I..."
mc "No buts, the faster you clean my knob, the faster you'll be able to get back to your library and your nerdy books."
scene auditjacuzzicum10 with dissolve
play sound "sounds/lick03.mp3"
ag "Like this?"
mc "It's a good start but you have 15 full inches to clean with your tongue..."
scene auditjacuzzicum11 with dissolve
play sound "sounds/lick02.mp3"
ag "Gblike... glthat?"
if age >= 20:
    mc "Yeah, keep going... Slide that fat mouth of yours on my giant dong!"
if age >= 18 and age <= 19:
    mc "Yeah, keep going... Slide that fat mouth of yours on my giant teenage dong!"

label AuditJacuzziSuckSlow:
hide nexticon
hide faster
hide slower
play music "sounds/blow01.mp3"
window hide
show auditsuckslowvideo behind auditsuckfastvideo
$ renpy.pause(1.0, hard='True')
hide auditsuckfastvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen auditjacuzzisuckslow()
screen auditjacuzzisuckslow():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditJacuzziSuckFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziSuckEnd")

label AuditJacuzziSuckFast:
hide faster
hide slower
hide nexticon
play music "sounds/blow02.mp3"
mc "You might clean FASTER if you SUCKED FASTER!"
window hide
show auditsuckfastvideo behind auditsuckslowvideo
$ renpy.pause(1.0, hard='True')
hide auditsuckslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen auditjacuzzisuckfast()
screen auditjacuzzisuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditJacuzziSuckSlow")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziSuckEnd")

label AuditJacuzziSuckEnd:
hide nexticon
hide slower
hide faster
mc "Fuck yeah, that was nice, I think I'll almost all clean now..."
stop music
scene auditjacuzzicum12 with dissolve
mc "Yep, just as I predicted, ALMOST all clean. Still some spunk on my fat balls though... So get going, Kayla."
scene auditjacuzzicum13 with dissolve
play sound "sounds/lick01.ogg"
mc "Oooh, I love your warm tongue on my balls..."
scene auditjacuzzicum14 with dissolve
ag "Gglllbbb...."
play sound "sounds/lick02.mp3"
mc "Mmmh, yeah, that's it, lick all that nasty cum, SWALLOW IT TOO!"
scene auditjacuzzicum15 with dissolve
play sound "sounds/lick03.mp3"
mc "And the final dregs... Still enough to give you a mouthfull..."
scene auditjacuzzicum16 with dissolve
play sound "sounds/moan02.mp3"
ag "Your fat dong is resting on my head... But I hope it's clean enough for you to remove it now..."
mc "I'd say you did a decent job and you're fine to go. My jacuzzi is full of spunk however, I'm gonna have to change the water..."
stop channel2
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label AuditJacuzziLevel02:
stop music
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ agstink = 0
scene auditjacuzzi41 with fade
play channel1 "sounds/jacuzzi.mp3"
mc "Come on Kayla, the water is super-warm and I can smell your stench from here."
play channel2 "sounds/sexy03.mp3"
scene auditjacuzzi42:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "I'm coming, don't rush me, I'm not used to this..."
stop channel1
scene auditjacuzzi43:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "And I don't want you to look at me like that when my swimsuit is clinging to my fat rump because of the heat..."
mc "Is it? Let me have a look then, maybe I can help you..."
scene auditjacuzzi44 with dissolve
mc "I see the problem. It's so tiny it's just being swallowed up by your crack. The best thing to do is to remove your bikini bottom altogether."
ag "You... really think so?"
mc "Absolutely. It's getting off at one stage or another anyway."
scene auditjacuzzi45:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
ag "Just don't look at my disgustingly fat butt."
mc "Not looking, not looking at all!"
scene auditjacuzzi46 with dissolve
ag "Oh no, now my bikini top is all clingy and... almost see-thru."
mc "Since I can basically see everything, you might as well take it off too."
ag "I... I guess it makes sense."
scene auditjacuzzi47:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "Now I'm going to be totally naked. And all wet."
mc "It's the idea behind a steamy jacuzzi cleaning session."
scene auditjacuzzi08 with dissolve
ag "I'm cleaning myself now. So you don't say nasty things about how... I smell. For a week at least."
mc "Do you need any help?"
ag "No I don't. Let me do it myself, last time you were too naughty!"
scene auditjacuzzi48 with dissolve
mc "* God, look at that hot plump wet bod and those fat nipples... *"
scene auditjacuzzi49 with dissolve
mc "That's it, I can't take it anymore because you got me ROCK-HARD!"
ag "I... I did?"
scene auditjacuzzi50 with dissolve
mc "Yes, you're RESPONSIBLE. So I have no choice. I'm gonna pound your fat ass until my cock goes down!"
ag "My ass? But..."
scene auditjacuzzi51 with dissolve
mc "No ifs or buts, you OWE me this!"
if fuckedauditlevel02:
    scene auditjacuzzi52 with dissolve
    ag "O...okay, I guess it's my fault. Again!"
    scene auditjacuzzi53 with dissolve
    mc "So get ready for a mighty superhero ANAL PUMMELING!"
    scene auditjacuzzi53 with dissolve
    play sound "sounds/moan04.ogg"
    mc "My abundant pre-cum is making my helmet SLIDE inside your hungry hole so easily..."
if fuckedauditlevel02 == False:
    scene auditjacuzzi52 with dissolve
    ag "O...okay, but your cock... It might be TOO big!"
    scene auditjacuzzi53 with dissolve
    mc "There's only one way to find out!"
    scene auditjacuzzi54 with dissolve
    play sound "sounds/moan04.ogg"
    mc "See? It fits just PERFECTLY.. Thanks to my abundant pre-cum and your FAT backdoor hole!"
    $ fuckedauditlevel02 = True

label AuditUpFuckSlow:
$ auditupfast = False
window hide
show auditupslowvideo behind auditupfastvideo
show auditupslowvideo behind auditupsideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditupfastvideo
hide auditupsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupslow == False and auditupfirst:
    $ auditupslow = True
    mc "That's it, just open up and let me slide my 18-incher right up your poop chute like that..."
if auditupfirst == False:
    $ auditupfirst = True
    mc "Yeah, it slides down nice and easy..."
    ag "Uggh... it's so BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500    
call screen auditupslow()
screen auditupslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckPOVSlow")

label AuditUpFuckFast:
$ auditupslow = False
window hide
show auditupfastvideo behind auditupslowvideo
show auditupfastvideo behind auditupsidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditupsidefastvideo
hide auditupslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupfast == False:
    $ auditupfast = True    
    mc "It's so slimy up there, I can POUND your ass FASTER now!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500    
call screen auditupfast()
screen auditupfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckPOVFast")

label AuditUpFuckPOVSlow:
$ auditupfast = False
window hide
show auditupsideslowvideo behind auditupslowvideo
show auditupsideslowvideo behind auditupsidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditupsidefastvideo
hide auditupslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupslow == False:
    $ auditupslow = True
    mc "That's it, just open up and let me slide my 18-incher right up your poop chute like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditupsidefuckslow()
screen auditupsidefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckSlow")

label AuditUpFuckPOVFast:
$ auditupslow = False
window hide
show auditupsidefastvideo behind auditupfastvideo
show auditupsidefastvideo behind auditupsideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditupfastvideo
hide auditupsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
if auditupfast == False:
    $ auditupfast = True    
    mc "It's so slimy up there, I can POUND your ass FASTER now!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditupsidefuckfast()
screen auditupsidefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckFast")

label AuditUpFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
stop channel2
mc "That ass... It's just too good!"
scene auditfuckcum01 with dissolve
play channel2 "sounds/boyorgasm01.mp3"
mc "So good I'm gonna FLOOD IT with spunk! AAAAH!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
ag "You're going to make it all DIRTY again!"
scene auditfuckcum02 with dissolve
mc "Nonsense, a cum enema is good for CLEANING the insides of naughty girls like you, RHAAAA!"
window hide
with hpunch
ag "Then clean me WELL and DEEP [name] with your giant [age]yo SUPERDONG!"
scene auditfuckcum01
show auditfuckcum01b
with dissolve
mc "Can't stop nutting inside your fat hole!"
window hide
with fastflash
ag "You're blowing so HARD!"
scene auditfuckcum02
show auditfuckcum02b
with dissolve
mc "Not done yet, got more cream for your hungry rosebud, AAAH!"
window hide
with fastflash
ag "You're gonna make me..."
scene auditfuckcum03 with dissolve
play sound "sounds/womancum01.mp3"
ag "... AAAH, I'm cumming too! AAAH!"
window hide
with fastflash
mc "Feel the POWER of my SUPERHERO BLASTS!"
scene auditfuckcum04 with dissolve
play sound "sounds/womancum02.mp3"
mc "I'm coming so much, I think I'd better pull out..."
window hide
with fastflash
ag "Yes please, I've have too much of your heavy spunk inside me!"
scene auditfuckcum05 with dissolve
stop channel2
play sound "sounds/splooge02.mp3"
ag "Your cum is just... POURING out of my ass! It's so filthy!"
mc "Maybe, but now you're squeaky clean up there I reckon."
scene auditfuckcum06 with dissolve
mc "It's time to check more closely how clean your ass is. Keep it open while I inspect it, Kayla!"
ag "But... That's just so naughty!"
scene auditfuckcum07 with dissolve
mc "Yeah, I can't see any dirt anymore. This was a complete success."
ag "Oh good. now I can get back dressed and..."
scene auditfuckcum08 with dissolve
mc "Hang on a minute. There's ANOTHER HOLE that needs cleaning."
ag "But.. You're STILL HARD???"
scene auditfuckcum09 with dissolve
if age >= 20:
    mc "Of course I am. I'm a SEX SUPERHERO after all. So let my ROCK-HARD dong take care of your filthy poontang."
if age >= 18 and age <= 19:
    mc "Of course I am. I'm a SEX SUPERHERO after all. So let my ROCK-HARD teen dong take care of your filthy poontang."

label AuditSidePoonSlow:
$ auditsidefast = False
window hide
show auditsideslowvideo behind auditsidefastvideo
show auditsideslowvideo behind auditpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditsidefastvideo
hide auditpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsideslow == False:
    $ auditsideslow = True
    ag "Your huge pole feels so BIG inside my poor little pussy!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen auditsideslow()
screen auditsideslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonPOVSlow")

label AuditSidePoonFast:
$ auditsideslow = False
window hide
show auditsidefastvideo behind auditsideslowvideo
show auditsidefastvideo behind auditpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditpovfastvideo
hide auditsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsidefast == False:
    $ auditsidefast = True    
    mc "I NEED to pound FASTER! Gotta get my rocks off one more time!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen auditsidefast()
screen auditsidefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonPOVFast")

label AuditSidePoonPOVSlow:
$ auditsidefast = False
window hide
show auditpovslowvideo behind auditsideslowvideo
show auditpovslowvideo behind auditpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditpovfastvideo
hide auditsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsideslow == False:
    $ auditsideslow = True
    ag "Your huge pole feels so BIG inside my poor little pussy!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditpovfuckslow()
screen auditpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonSlow")

label AuditSidePoonPOVFast:
$ auditsideslow = False
window hide
show auditpovfastvideo behind auditsidefastvideo
show auditpovfastvideo behind auditpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditsidefastvideo
hide auditpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if auditsidefast == False:
    $ auditsidefast = True    
    mc "I NEED to pound FASTER! Gotta get my rocks off one more time!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditpovfuckfast()
screen auditpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonFast")

label AuditSidePoonEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "I think I'm about to clean your dirty fuck..."
scene auditfucknewcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge03.mp3"
mc "... HOLE! RHAAA!"
window hide
with fastflash
ag "I hope it works, I really need to smell nice for a week!"
scene auditfucknewcum02 with dissolve
ag "[name], you're going... TOO DEEP! AAH!"
window hide 
with hpunch
mc "You can take it Kayla, TAKE ALL MY CUM AND COCKMEAT UP THERE!"
scene auditfucknewcum03 with dissolve
ag "Your cumblasts are just so ENORMOUS! I don't know if I can..."
window hide
with fastflash
mc "Yes you CAN, you NEED to, I'm STILLLLLL CUMMMING!"
scene auditfucknewcum04 with dissolve
play sound "sounds/moan05.mp3"
ag "I'm also cumming now, I can't help myself, OOOOHHH!"
window hide
with fastflash
mc "That's good, come with me, don't ever stop, just like me, RHAAA!"
scene auditfucknewcum05 with dissolve
mc "I'm gonna whitewash your insides once and for all, AAAH!"
window hide
with fastflash
ag "Noooo, you're cumming like a firehose, I'm gonna lose my grip!"
stop channel2
scene auditfucknewcum06 with dissolve
mc "Damn, my cumshots are just BLASTING OUT of my enraged cock, RHAAA! And Kayla went FLYING across the room!"
window hide 
with vpunch
mc "Oh God, it's soo fucking GOOOODDD! NEED.. TO..."
window hide 
with fastflash
mc "..STOP AND CHECK ON HER!"
scene auditfucknewcum07 with dissolve
stop channel1
mc "I might have overdone it a bit. I didn't realize my cumshots could be so POWERFUL."
ag "Gggg..."
mc "I suppose I should carry her back to her bed in the cold library and hope for the best..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
