label ScarletGallery:
stop channel3
play channel3 "sounds/mental.mp3"
scene scarletbackground
show scarletmaingallery at gallerypos01 with moveinleft
call screen galleryscarlet()
screen galleryscarlet():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Scarlet{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryscarlet"), Jump ("MainGallery04b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryscarlet"), Jump ("ScarletGalleryAnim")]
    
    if renpy.seen_image("scarlettpsych03"):
        imagebutton:
            focus_mask True
            idle "gallery/scarletgallery01.png" xpos 400 ypos 100
            hover "gallery/scarletgallery01.png"
            action Jump ("ScarletGallery01")
    text "{font=Gui/Heroes Legend.ttf}Mind BE/PE{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("scarlettpsych03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("ScarletGallery")

    if renpy.seen_image("scarlettpsychmuscle03"):
        imagebutton:
            focus_mask True
            idle "gallery/scarletgallery02.png" xpos 750 ypos 100
            hover "gallery/scarletgallery02.png"
            action Jump ("ScarletGallery02")
    text "{font=Gui/Heroes Legend.ttf}Mind FMG/PE{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("scarlettpsychmuscle03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("ScarletGallery")

label ScarletGalleryAnim:
call screen screenanimscarlet()
screen screenanimscarlet():
    modal True
    add "gallery/scarletbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "scarletanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "scarletanimbig" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "scarletanimmus" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "scarletanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimscarlet"), SetVariable ("animcount", 1), Jump ("ScarletGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Scarlet{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero03
    text "{font=Gui/Heroes Legend.ttf}Age: 40{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}36GG-25-35{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Hypno-Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/scarletanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimscarlet")]
    add "gallery/scarletanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimscarlet")]
    add "gallery/scarletanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimscarlet")]
    add "gallery/scarletanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimscarlet")]
            
label ScarletGallery01:
stop channel3
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
label PsychFuckSlowx:
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
call screen psychfuckslowscreenx()
screen psychfuckslowscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("PsychFuckSlowPOVx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckFastx")

label PsychFuckFastx:
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
call screen psychfuckfastscreenx()
screen psychfuckfastscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PsychFuckFastPOVx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PsychFuckEndx")

label PsychFuckSlowPOVx:
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
call screen psychfuckslowpovscreenx()
screen psychfuckslowpovscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("PsychFuckSlowx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckFastPOVx")

label PsychFuckFastPOVx:
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
call screen psychfuckfastpovscreenx()
screen psychfuckfastpovscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PsychFuckFastx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PsychFuckSlowPOVx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PsychFuckEndx")

label PsychFuckEndx:
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
stop music
stop channel1
stop channel2
jump ScarletGallery

label ScarletGallery02:
stop channel3
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
stop music
stop channel1
stop channel2
jump ScarletGallery