label ArkhamAsylum:
scene arkham01 with fade
play channel1 "sounds/dark.mp3"
show scarlet01 with moveinright
show scarlet01 at center:
    breathe
sc "[hero]. What an interesting... visitor."
label ScarletDialogues:
menu:
    "I'd like to check this place out. Please give me a tour." if visitedarkham == False:
        hide scarlet01
        show scarlet03
        with fastdissolve        
        sc "Certainly, I cannot refuse such a request from the Cockham League of Justice. Please follow me."
        jump ArkhamNext
    "I need some strong drug to control She-Hulk." if questhulk and spokemayorshehulk and visitedarkham and sawbreasteval == False and sawmuscleeval == False:
        hide scarlet01
        show scarlet02
        with fastdissolve        
        sc "She Hulk? That would mean a very STRONG drug. Why do you suppose I would have such a dangerous product?"
        mc "Well, cos you're like, some kind of... mad scientist?"
        hide scarlet02
        show scarlet04
        with fastdissolve        
        sc "That is INSULTING! I conduct REAL science here!"
        mc "Okay, sorry, because you're a REAL scientist?"
        hide scarlet04
        show scarlet01
        with fastdissolve        
        show scarlet01 at center:
            breathe
        sc "Now that's better... Still, I would need a favor in return from you before I agree...."
        mc "What's that?"
        hide scarlet01
        show scarlet02
        with fastdissolve        
        sc "I need you to... agree to some psychiatric evaluation."
        mc "I'm perfectly normal! I'm not a looney, like your inmates!"
        sc "And to better understand the crimina mind, I need to find out about the mind of the SUPER-HERO. Like yourself."
        menu:
            "Fine, I'll be your guinea pig. I AM a SUPER-HERO after all.":
                hide scarlet02
                show scarlet03
                with fastdissolve        
                sc "Excellent... Please follow me."
                jump ArkhamPsych
            "No way! I won't let you screw with my perfect mind!":
                hide scarlet02
                show scarlet04
                with fastdissolve   
                sc "And I won't give you the drug you request then. Goodbye, [hero]."
                jump Main
    "I'm here to finish my psych eval. And get those drugs for She-Hulk you promised me." if questhulk and questhulkcompleted == False and spokemayorshehulk and visitedarkham and (sawbreasteval or sawmuscleeval):
        hide scarlet01
        show scarlet02
        with fastdissolve        
        sc "Ah yes, hopefully, your mind has cleared up and you will provide me with VALUABLE information this time."
        mc "I have the mind of a super-hero who has to deal with SEX crime on a daily basis. I can't change that."
        hide scarlet02
        show scarlet04
        with fastdissolve        
        sc "Than maybe I can CHANGE that... Please follow me..."
        jump ArkhamPsych
    "I'm now a Level 2 Superhero. Does this mean anything to you?" if mclevel02:
        hide scarlet01
        show scarlet04
        with fastdissolve        
        sc "Not really. Come back when it finally does!"
        jump Main
    "The CCPD needs to have these flowers analyzed and a cure found." if mclevel02 and quest05 and foundflower and floweranalyzed == False:
        $ floweranalyzed = True
        hide scarlet01
        show scarlet04
        with fastdissolve        
        sc "Is that all? Anything else?"
        mc "No, I think that should be enough. They come from Poison Ivy's lair so they are, like, poisonous and whatnot."
        hide scarlet04
        show scarlet02
        with fastdissolve        
        sc "You DO realize that I cannot make enough antidote to a poisonous compound without its primer."
        mc "Its what? That sounds too technical. And completely made up too I might add."
        hide scarlet02
        show scarlet01
        with fastdissolve        
        sc "Poison Ivy must have the primer. Find it or I won't be able to make enough antidote for the whole town..."
        mc "So I have to go BACK? But she kicked my butt!"
        hide scarlet01
        show scarlet04
        with fastdissolve        
        sc "That is none of my concern. Perhaps you should think about PROTECTING yourself a bit better. You're walking around half-naked in case you didn't notice."
        mc "Yeah, I did notice actually. Good thing it's summer in Cockham or I'd be freezing my nuts."
        hide scarlet04
        show scarlet03
        with fastdissolve        
        sc "Now if you'll excuse me, I need to isolate the venomous compound from these flowers."
        window hide
        play sound "sounds/skill.mp3"
        show questivyprogress02 at poslocation
        $ renpy.pause(0.5, hard='True')
        pause
        if inventorygoldtrunks == False:
            mc "She is right though, I need to find some protective gear. For my COCK!"
        if inventorygoldtrunks:
            mc "She is right though, I need to wear some protective gear on my cock. I'll go back and face off with Poison Ivy again, but this time, I'll be wearing my golden trunks!"
        jump Main
    "I'm done here.":
        hide scarlet01
        show scarlet04
        with fastdissolve        
        sc "Thanks for coming by and wasting my time!"
        jump Main
        
label ArkhamNext:
scene arkham02 with dissolve
sc "Please watch your step, the floor can be quite slippery."
mc "Why are the inmates out of their cells? Aren't they supposed to be dangerous criminals?"
sc "That's why they are in straight jackets. They are perfectly incapable of harming us, I can assure you..."
scene arkham03 with dissolve
mc "And how do you deal with the batshit-crazy criminal total lunatics?"
sc "I will show you..."
scene arkham04
show scarlet03 at left
with dissolve
sc "Here is where we \"study\" the minds of the criminally insane to better understand them."
mc "Did they volunteer or are you FORCING them to undergo these procedures?"
hide scarlet03
show scarlet02 at left
with fastdissolve        
sc "Well, since they are considered insane, the signature of their legal guardian is sufficient."
mc "And that would be..."
hide scarlet02
show scarlet01 at left
with fastdissolve        
sc "Me of course."
mc "I see. I cannot find any flaws in that legal argument. I'll be on my way, thank you for the visit, Ms Scarlet."
hide scarlet01
show scarlet02 at left
with fastdissolve        
sc "You are welcome to come back anytime you want during opening hours. In the evening that is."
$ visitedarkham = True
jump Main

label ArkhamPsych:
if sawmuscleeval or sawbreasteval:
    play music "sounds/mental.mp3"
    scene psycheval00 with fade
    sc "Please sit in the armchair and get naked for our SECOND session."
    mc "Sure, as a SUPER-HERO, I have no qualms getting naked."
    scene psycheval01 with dissolve
    sc "And flaunting your MASSIVE appendage... Are you ready?"
    mc "Ready when you are, Miss Scarlet."
    scene psycheval02 with dissolve
    sc "Let me connect your goggles... There."
    show psychevalback:
        zoom 1.1 xoffset 0 yoffset -1000
    with fade
    sc "What do you see?"
    mc "Nothing. Just... a wall like last time."
    sc "That's normal, I will now project myself into your mind."
    if sawmuscleeval:
        jump ScarlettBreast       
    if sawbreasteval:
        jump ScarlettMuscle

if sawmuscleeval == False and sawbreasteval == False:
    $ dideval = True
    play music "sounds/mental.mp3"
    scene psycheval00 with fade
    sc "Please sit in this armchair. And get naked first, clothing hinders our mind reading machine..."
    mc "You plan to read my mind? Prepare to be BLOWN AWAY then!"
    scene psycheval01 with dissolve
    sc "Are you comfortable, [hero]?"
    mc "I can't see anything..."
    scene psycheval02 with dissolve
    sc "That is normal. Once I connect my mind-reading machine to start exploring the meanders of your mind, your vision will get clearer..."
    show psychevalback:
        zoom 1.1 xoffset 0 yoffset -1000
    with fade
    sc "What do you see?"
    mc "Nothing. Just... a wall."
    sc "Let me project myself into your mind. You will still have full control of your thoughts of course..."
    menu:
        "Imagine her in sexy lingerie (Breast Growth Scene)":
            jump ScarlettBreast
        "Imagine her in a sexy sports outfit (Muscle Growth Scene)":
            jump ScarlettMuscle

label ScarlettBreast:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ sawbreasteval = True
stop music
play music "sounds/sexy14.mp3"
window hide
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset -1000
show scarlettpsych01:
    xoffset -50 yoffset -1080    
show psychevalback blurred at scarlettfullzoombackground
show scarlettpsych01 at scarlettfullzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause        
mc "Yeah, now I see you..."
hide psychevalback
hide scarlettpsych01
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset 0
show scarlettpsych02:
    xoffset 50 yoffset 0    
show psychevalback blurred at scarlettfulldownzoombackground
show scarlettpsych02 at scarlettfulldownzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause
scene psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset 0
show scarlettpsych03
with dissolve
sc "You are being very naughty... Your mind is..."
hide scarlettpsych03
show scarlettpsych05
with dissolve
sc "...What is going on????"
hide scarlettpsych05
show scarlettpsych06
with dissolve
sc "AAAH, my tits! They are GROWING!"
hide scarlettpsych06
show scarlettpsych07
with dissolve
play sound "sounds/ripping.mp3"
mc "FUCK YEAH!"
sc "Why are you thinking of me as a SEX OBJECT, [hero]?"
hide psychevalback blurred
hide scarlettpsych07
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset -500
show scarlettpsych08
with dissolve
mc "Cos I like my tiddies HUGE AND FAT!"
sc "Really? So you like MY NEW MONSTER RACK then?"
mc "Yeah..."
hide psychevalback blurred
hide scarlettpsych08
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset -1000
show scarlettpsych09
with dissolve
sc "What about my tight little pussy?"
mc "You'd better work on it to make it LESS TIGHT!"
hide scarlettpsych09
show scarlettpsych10
with dissolve
if age >= 20:
    sc "Are you saying that because you have an ALPHA-COCK?"
if age >= 18 and age <= 19:
    sc "Are you saying that because you have a teenage ALPHA-COCK?"
hide psychevalback blurred
hide scarlettpsych10
show psychevalback blurred:
    zoom 1.1 xoffset -50 yoffset -1100
show scarlettpsych11
with dissolve
sc "And you would like to... AAAH!... stick it up my wet snatch?"
hide scarlettpsych11
show scarlettpsych12
with dissolve
play sound "sounds/womancum01.mp3"
mc "Yeah, now you're READY for my GIANT COCK!"
scene scarlettpsychbackground02
show scarlettpsych13
with dissolve
play sound "sounds/gasp.mp3"
sc "What the??? This is MUCH BIGGER than I anticipated!"
mc "Is it? I thought that was my normal size."
sc "It's your IMAGINARY size! And it's much TOO LARGE, it will never fit!"
scene scarlettpsychbackground02:
    zoom 1.1 xoffset 0 yoffset -100
show scarlettpsych14
with dissolve
mc "Na. In my mind, I imagine it will fit just snugly..."
sc "Dear Lord, I'm about to get IMPALED on a BATTERING RAM!"
scene scarlettpsychbackground05
show psychprefuck01
with dissolve
if age >= 20:
    mc "Don't be scared and spread those thighs open for me. My 21-inch CUM-CANNON is about to give you a 21-gun salute!"
if age >= 18 and age <= 19:
    mc "Don't be scared and spread those thighs open for me. My 21-inch teen CUM-CANNON is about to give you a 21-gun salute!"
hide psychprefuck01
show psychprefuck02
with dissolve
play sound "sounds/moan05.mp3"
sc "AAAH, your cock is already so deep inside me!"
mc "What? That's just like the helmet. Brace yourself for the rest of my arm-thick shaft!"
stop channel1
play channel1 "sounds/womansex04.mp3"
label PsychFuckSlow:
scene scarlettpsychbackground05
show psychfuckslowvideo 
with dissolve
$ renpy.pause(1.0, hard='True')
sc "It's sooo big... You're stretching me so MUCH!"
window hide
show pov:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen psychfuckslowscreen()
screen psychfuckslowscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("PsychFuckSlowPOV")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckFast")

label PsychFuckFast:
if age >= 20:
    sc "I LOVE your giant horsedick! FUCK ME FASTER!"
if age >= 18 and age <= 19:
    sc "I LOVE your giant teenage horsedick! FUCK ME FASTER!"
scene scarlettpsychbackground05
show psychfuckfastvideo 
with dissolve
$ renpy.pause(1.0, hard='True')
show pov:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
show cum:
    xpos 1750 ypos 1020    
call screen psychfuckfastscreen()
screen psychfuckfastscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PsychFuckFastPOV")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PsychFuckEnd")

label PsychFuckSlowPOV:
scene scarlettpsychbackground04
show psychfuckslowpovvideo 
with dissolve
$ renpy.pause(1.0, hard='True')
mc "Yeah, this is the imaginary eye view of my MONSTER cock DESTROYING your tight pussy!"
sc "AAAH, I've never been STRETCHED like this before!"
window hide
show sceneicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen psychfuckslowpovscreen()
screen psychfuckslowpovscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("PsychFuckSlow")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckFastPOV")

label PsychFuckFastPOV:
scene scarlettpsychbackground04
show psychfuckfastpovvideo 
with dissolve
sc "My GIANT BOOBIES are just wiggling all over the place, you fuck me so good, [hero]!"
window hide
show sceneicon:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
show cum:
    xpos 1750 ypos 1020    
call screen psychfuckfastpovscreen()
screen psychfuckfastpovscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PsychFuckFast")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckSlowPOV")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PsychFuckEnd")

label PsychFuckEnd:
sc "I can feel your monster cock RUMBLING! Like a VOLCANO!"
hide psychfuckfastpovvideo
hide psychfuckfastvideo
hide psychfuckslowpovvideo
hide psychfuckslowvideo
hide sceneicon
hide slower
hide faster
hide pov
show psychfuckcum01
with dissolve
stop channel1
play channel1 "sounds/splooge01.mp3"
play sound "sounds/boymoan05.mp3"
mc "And I can feel it ERUPTING, like a VOLCANO!"
window hide
with hpunch
mc "RHAAA! Take my scalding seed!"
play channel2 "sounds/boyorgasm01.mp3"
hide psychfuckcum01
show psychfuckcum02
with dissolve
play sound "sounds/moan04.ogg"
sc "You're BLASTING so DEEP inside my poor pussy! And you're OVERFLOWING IT!!!"
window hide
with fastflash
mc "FUCK, CAN'T STOP CUMMING!!!"
hide psychfuckcum02
show psychfuckcum03
with dissolve
stop channel1
play sound "sounds/moan02.mp3"
sc "Mmmmh, COVER my body in your filthy spunk, you horse-hung SUPERHERO!"
window hide
with fastflash
mc "YEAH, TAKE THOSE MIGHTY SUPERHERO SHOTS!"
hide psychfuckcum03
show psychfuckcum04
with dissolve
mc "Hang on, why are you disappearing???"
sc "I mmust be disconnecti..."
stop channel2
stop music
jump PsychEnd

label ScarlettMuscle:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
$ sawmuscleeval = True
play music "sounds/sexy04.mp3"
window hide
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset -1000
show scarlettpsychmuscle01:
    xoffset -50 yoffset -1080    
show psychevalback blurred at scarlettfullzoombackground
show scarlettpsychmuscle01 at scarlettfullzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause        
mc "Yeah, now I see you..."
hide psychevalback
hide scarlettpsychmuscle01
show psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset 0
show scarlettpsychmuscle02:
    xoffset 50 yoffset 0    
show psychevalback blurred at scarlettfulldownzoombackground
show scarlettpsychmuscle02 at scarlettfulldownzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause
scene psychevalback blurred:
    zoom 1.1 xoffset 0 yoffset 0
show scarlettpsychmuscle03
with dissolve
sc "I need to stretch for some reason..."
mc "Please do. Stretch away..."
hide scarlettpsychmuscle03
show scarlettpsychmuscle04
with dissolve
sc "...What is going on????"
hide psychevalback
hide scarlettpsychmuscle04
show psychevalback blurred:
    zoom 1.1 xoffset -50 yoffset -200
show scarlettpsychmuscle05
with dissolve
sc "My... muscles... ARE GROWING! What have you done?"
mc "Me? Nothing, I'm just sitting in a chair somewhere else, remember?"
hide scarlettpsychmuscle05
show scarlettpsychmuscle06
with dissolve
sc "I can feel all my muscles TENSING UP!"
mc "Damn, and you're getting SUPER-BUFF!"
hide scarlettpsychmuscle06
show scarlettpsychmuscle07
with dissolve
sc "Look at those biceps! I've never seen BIGGER ones on a woman before!"
mc "Neither have I! Not quite as big as mine though..."
hide scarlettpsychmuscle07
show psychevalback blurred:
    zoom 1.0 xoffset 0 yoffset -800
show scarlettpsychmuscle08
with dissolve
sc "I feel so RIPPED, I'm going to do some HEAVY CURLING. NAKED!"
mc "FUCK YEAH!"
hide scarlettpsychmuscle08
show scarlettpsychmuscle09
with dissolve
play sound "sounds/womangroan.mp3"
pause 1.0
hide scarlettpsychmuscle09
show scarlettpsychmuscle10
with dissolve
play sound "sounds/womangroan.mp3"
pause 1.0
mc "Pump those muscles, Ms Scarlet, you're getting me HARD!"
hide scarlettpsychmuscle10
show scarlettpsychmuscle08
with dissolve
sc "Now watch THIS!"
hide scarlettpsychmuscle08
show scarlettpsychmuscle13
with dissolve
play sound "sounds/womangroan.mp3"
pause 1.0
hide scarlettpsychmuscle13
show scarlettpsychmuscle11
with dissolve
play sound "sounds/womangroan.mp3"
sc "BOTH OF THEM!"
hide scarlettpsychmuscle11
show scarlettpsychmuscle12
with dissolve
sc "I feel so STRONG!"
hide scarlettpsychmuscle12
show scarlettpsychmuscle14
with dissolve
play sound "sounds/womangroan.mp3"
sc "I could do it with weights that are TEN TIMES HEAVIER!"
show scarlettpsychmuscle14 at farright with move
show scarlettpsychmuscle16 at left with moveinleft
mc "How about you swing my kettlebell then?"
hide scarlettpsychmuscle14
show scarlettpsychmuscle15 at farright
with dissolve
play sound "sounds/gasp.mp3"
sc "What is this??? Your cock has grown absolutely MASSIVE!!! I NEED to WORSHIP IT!"
hide scarlettpsychmuscle15
hide scarlettpsychmuscle16
scene scarlettpsychbackground02
show scarlettpsychmuscle17
with dissolve
mc "Yeah, now it's definitely the BIGGEST cock in Cockam, Ms Scarlet!"
sc "I LOVE IT! I can't even get halfway around its GIGANTIC girth!"
hide scarlettpsychmuscle17
show scarlettpsychmuscle18
with dissolve
play sound "sounds/lick03.mp3"
mc "Oh God, you're licking directly INSIDE my cumhole!"
hide scarlettpsychmuscle18
show scarlettpsychmuscle19
with dissolve
if age >= 20:
    sc "And now... Ggglbb... I'm going to SUCK YOUR HUGE DONG!"
if age >= 18 and age <= 19:
    sc "And now... Ggglbb... I'm going to SUCK YOUR HUGE TEENAGE DONG!"
hide scarlettpsychmuscle19
show scarlettpsychmuscle20
with dissolve
play sound "sounds/lick01.ogg"
mc "Yeah, you're doing good, Ms Scarlet! Take a few more inches in!"
hide scarlettpsychmuscle20
show scarlettpsychmuscle21
with dissolve
mc "Oh FUCK! You're gonna suck the cum out of me!..."
hide scarlettpsychmuscle21
show scarlettpsychmuscle22
with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play sound "sounds/splooge01.mp3"
mc "AAAAH! CUMMING DIRECTLY DOWN YOUR GULLET!"
window hide
with fastflash
sc "* Ggggllllbbbb *"
scene scarlettpsychbackground03
show scarlettpsychmuscle23
with dissolve
play sound "sounds/splooge02.mp3"
mc "FFF-UUUU-CCCKKK!!!!"
window hide
with hpunch
mc "DAMN IT, AAAAH!"
hide scarlettpsychmuscle23
show scarlettpsychmuscle24
with dissolve
mc "STILL BLOWING!!!!"
window hide
with fastflash
sc " *gulp * You're... gglll.. cumming SO MUCH!"
hide scarlettpsychmuscle24
show scarlettpsychmuscle25
with dissolve
stop channel1
stop sound
if age >= 20:
    sc "Wow, your TITANIC fuckstick just came a gallon of cum all over me... I feel so DIRTY."
if age >= 18 and age <= 19:
    sc "Wow, your TITANIC TEEN fuckstick just came a gallon of cum all over me... I feel so DIRTY."
mc "It's full of proteins, it will make your muscles GROW even more!"
hide scarlettpsychmuscle25
show scarlettpsychmuscle26
with dissolve
mc "Hang on, why are you disappearing?"
sc "I must have disconnec..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop channel1
stop music

label PsychEnd:
scene psycheval03
show scarlet01
with fade
if sawmuscleeval == False or sawbreasteval == False:
    sc "That was a disaster. Your mind is just clogged with... pervert thoughts!"
    mc "I fight SEX CRIME all the time, what did you expect?"
    hide scarlet01
    show scarlet02
    with fastdissolve
    sc "* sigh * I suppose it makes sense. Still, I need some more data, there are too many missing pieces of your brain that I didn't manage to collect yet."
    mc "Hey! You said you would give me the sedative for She-Hulk if I volunteered!"
    hide scarlet02
    show scarlet04
    with fastdissolve
    sc "AND finished the psychological evaluation. You need to come back ONE MORE TIME. Then, I'll give you what you are looking for."
    mc "Umpf... I'll be back."
    jump Main

if sawmuscleeval and sawbreasteval:
    sc "I have no words to describe the state of your tangled mind..."
    mc "I like to describe it myself as \"SPOT-ON\"."
    hide scarlet01
    show scarlet03
    with fastdissolve
    sc "* sigh * I suppose I should give you that drug you requested since you completed the psych eval. Let me get it for you."
    hide scarlet03 with moveoutright
    mc "This had better be good."
    window hide
    show scarlet02 with moveinright
    sc "There you are. One dose should be sufficient to tame She-Hulk by my calculations..."
    window hide
    $ inventorysedative = True
    play sound "sounds/achievement.mp3"
    show acquiredsedative at poslocation
    $ renpy.pause(0.5, hard='True')
    pause
    mc "Thank you Ms Scarlet, pleasure doing business with you..."    
    jump Main
