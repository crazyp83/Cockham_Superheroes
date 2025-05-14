label MILFGallery:
stop channel3
play channel3 "sounds/sexy06.mp3"
scene milfbackground with dissolve
show milfmaingallery at gallerypos01 with moveinleft

call screen gallerymilf()
screen gallerymilf():
    text "{font=Gui/Heroes Legend.ttf}Naughty Captain MILF{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerymilf"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerymilf"), Jump ("MILFGalleryAnim")]

    if renpy.seen_image("milfnight04"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery01.png" xpos 400 ypos 100
            hover "gallery/milfgallery01.png"
            action Jump ("MILFGallery01")
    text "{font=Gui/Heroes Legend.ttf}Room Sexy{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("milfnight04") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("poolmilfsauna03"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery02.png" xpos 750 ypos 100
            hover "gallery/milfgallery02.png"
            action Jump ("MILFGallery02")
    text "{font=Gui/Heroes Legend.ttf}Sauna Blowjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("poolmilfsauna03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("milfroomnightyoga02"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery03.png" xpos 1100 ypos 100
            hover "gallery/milfgallery03.png"
            action Jump ("MILFGallery03")
    text "{font=Gui/Heroes Legend.ttf}Yoga Stretching{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("milfroomnightyoga02") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("milfseduction07"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery04.png" xpos 1450 ypos 100
            hover "gallery/milfgallery04.png"
            action Jump ("MILFGallery04")
    text "{font=Gui/Heroes Legend.ttf}Seduction Training{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("milfseduction07") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("MILFGallery04hint")

    if renpy.seen_image("milfmaledom01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery05.png" xpos 400 ypos 380
            hover "gallery/milfgallery05.png"
            action Jump ("MILFGallery05")
    text "{font=Gui/Heroes Legend.ttf}MILF Maledom{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("milfmaledom01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("MILFGallery05hint")

    if renpy.seen_image("gymmilfnew01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery06.png" xpos 750 ypos 380
            hover "gallery/milfgallery06.png"
            action Jump ("MILFGallery06")
    text "{font=Gui/Heroes Legend.ttf}Gym Squats{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06
    if renpy.seen_image("gymmilfnew01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("MILFGallery06hint")

    if renpy.seen_image("mcroomsex01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery07.png" xpos 1100 ypos 380
            hover "gallery/milfgallery07.png"
            action Jump ("MILFGallery07")
    text "{font=Gui/Heroes Legend.ttf}Supergirl 3some{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext07
    if renpy.seen_image("mcroomsex01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("mcroomsex43"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery08.png" xpos 1450 ypos 380
            hover "gallery/milfgallery08.png"
            action Jump ("MILFGallery08")
    text "{font=Gui/Heroes Legend.ttf}Massage Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext08
    if renpy.seen_image("mcroomsex43") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("gymmcmilflevel10"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery09.png" xpos 400 ypos 660
            hover "gallery/milfgallery09.png"
            action Jump ("MILFGallery09")
    text "{font=Gui/Heroes Legend.ttf}Gym Thigh Wank{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext09
    if renpy.seen_image("gymmcmilflevel10") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("milfpoolresistance01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery10.png" xpos 750 ypos 660
            hover "gallery/milfgallery10.png"
            action Jump ("MILFGallery10")
    text "{font=Gui/Heroes Legend.ttf}Sauna Heat{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext10
    if renpy.seen_image("milfpoolresistance01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("milfnewlingerie01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery11.png" xpos 1100 ypos 660
            hover "gallery/milfgallery11.png"
            action Jump ("MILFGallery11")
    text "{font=Gui/Heroes Legend.ttf}Reward Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext11
    if renpy.seen_image("milfnewlingerie01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")

    if renpy.seen_image("milfoilpussycum05"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery12.png" xpos 1450 ypos 660
            hover "gallery/milfgallery12.png"
            action Jump ("MILFGallery11")
    text "{font=Gui/Heroes Legend.ttf}Harem Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext12
    if renpy.seen_image("milfoilpussycum05") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("MILFGallery")
    text "{font=Gui/Heroes Legend.ttf}Hero{/font}" color "#008000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytexthero12

label MILFGallery04hint:
show milfmaingallery at gallerypos01
show milfgallery04 at posgalleryhintpic
show milfgalleryhint04 at posgalleryhint
pause
hide milfgalleryhint04
hide milfgallery04
call screen gallerymilf()

label MILFGallery05hint:
show milfmaingallery at gallerypos01
show milfgallery05 at posgalleryhintpic
show milfgalleryhint05 at posgalleryhint
pause
hide milfgalleryhint05
hide milfgallery05
call screen gallerymilf()

label MILFGallery06hint:
show milfmaingallery at gallerypos01
show milfgallery06 at posgalleryhintpic
show milfgalleryhint06 at posgalleryhint
pause
hide milfgalleryhint06
hide milfgallery06
call screen gallerymilf()

label MILFGalleryAnim:
call screen screenanimmilf()
screen screenanimmilf():
    modal True
    add "gallery/milfbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "milfanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "milfanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "milfanimbik" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "milfanimgym" xalign -0.1 yalign 1.0
    if animcount == 5:
        add "milfanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimmilf"), SetVariable ("animcount", 1), Jump ("MILFGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Captain MILF{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 40{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft6{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}36FFF-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Massive Cocks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Cock Worship{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Blowjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    text "{font=Gui/Heroes Legend.ttf}Male Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink04
    add "gallery/milfanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimmilf")]
    add "gallery/milfanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimmilf")]
    add "gallery/milfanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimmilf")]
    add "gallery/milfanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimmilf")]
    add "gallery/milfanim05.png" xpos 1580 ypos 800
    button:
        xpos 1550
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 5), Show ("screenanimmilf")]

label MILFGallery01:
stop channel3
play channel1 "sounds/sexy06.mp3"
scene compoundmilfbedroomnight with fade
show milfnight01 at centerleft with moveinright
show milfnight01 at centerleft:
    breathe
voice "milf/room01"
cm "Hello sweetie, what are you doing visiting me in my room that late?"
mc "Oh, I didn't realize it was that late."
hide milfnight01
show milfnight02 at centerleft
with fastdissolve
voice "milf/room02"
cm "I was about to go to bed actually..."
mc "Fine, err... I'll go to bed too then. Just making sure you were safe and all..."
hide milfnight02
show milfnight06 at centerleft
with fastdissolve
voice "milf/room03"
cm "I'm pretty sure I'll be fine... But I'll let you watch just in case. So you can go back to your room completely reassured."
hide milfnight06
show milfnight03 at centerleft
with fastdissolve
voice "milf/room04"
cm "That's really why you came, isn't it?"
mc "Err..."
hide milfnight03
show milfnight04 at centerleft
with fastdissolve
voice "milf/room05"
cm "To watch me take off my night robe and expose my muscular body in sexy lingerie..."
mc "Well, now that you mention it..."
hide milfnight04
show milfnight05 at centerleft
with fastdissolve
voice "milf/room06"
cm "And admire my tight glutes as I head off to bed..."
mc "Damn, they sure are TIGHT!"
window hide
show compoundmilfbedroomnight blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.2
    ease 3.5 xpos 0.42 ypos 1.3           
show milfnight05b:
    subpixel True
    ypos 0.0
    linear 3.0 ypos -0.1
$ renpy.pause(3.0, hard='True')
voice "milf/room07"
cm "So, are you reassured that nothing will happen to me?"
window hide
mc "I think I am..."
voice "milf/room08"
cm "Then go back to your room and go to the sleep..."
stop channel1
jump MILFGallery

label MILFGallery02:
scene poolmilfsauna00
cm "Then I'll be waiting for you inside, sweetie! Get youself a towel to cover... your bulge please."
scene poolmilfsauna01 with dissolve
mc "Right, I'll get a towel, but I'll get out of my speedo too. Don't want it to cling to my sweaty body while we're in there..."
scene poolmilfsauna02 with fade
play music "sounds/sexy05.mp3"
cm "This will rid your body of toxins, you just need to sweat them out..."
mc "Aaahh, this is nice and relaxing..."
scene poolmilfsauna03 with dissolve
cm "* It's getting so hot in here, I'll sneakily get rid of my towel while he's slowly drifting away... *"
scene poolmilfsauna04 with dissolve
cm "* And now I can relax. Although I don't need to get rid of toxins myself since I'm super-resistant to them... *"
scene poolmilfsauna05 with dissolve
mc "* Damn, she went topless while I was drifting away... What a HUGE pair of MILF funbags... I think I'm getting a...* "
scene poolmilfsauna06 with dissolve
mc "* Oh shit... *"
cm "I thought you weren't looking!"
scene poolmilfsauna07 with dissolve
mc "I WAS looking and now I can't stop my cock from hardening!"
scene poolmilfsauna08 with dissolve
cm "Oh dear me, you dropped your towel and now I can see your... HUGE COCK!"
scene poolmilfsauna09 with dissolve
play sound "sounds/thud.mp3"
mc "I can't hide it anymore, Carol, sorry..."
cm "I'm getting weak in the knees..."
scene poolmilfsauna10 with dissolve
cm "We have to do SOMETHING about it, I can sense I've lost my superpowers and if the compound gets attacked, I'll be useless!"
mc "Well, there's only one way to get it down..."
scene poolmilfsauna11 with dissolve
cm "You mean... You want me to blow you?"
mc "It's the only way, Captain MILF..."
scene poolmilfsaunapreblow01 with dissolve
if age >= 20:
    cm "I... can't resist. That HUGE schlong is... mesmerizing."
if age == 18 or age == 19:
    cm "I... can't resist. That HUGE teenage schlong is... mesmerizing."
mc "Go right ahead, it's all yours!"
cm "My hand can't even get halfway around its GIRTH... I want to feel its POWER!"
window hide
show poolmilftonguevideo with dissolve
play channel2 [ "<silence .75>", "sounds/thud.mp3" ]
pause
cm "It's so HEAVY! Like a battering ram!"
window hide
pause
stop channel2
scene poolmilfsaunapreblow02 with dissolve
hide poolmilftonguevideo
play sound "sounds/lick01.ogg"
cm "And now, let me DRAIN your fat balls with my MOUTH!"
mc "Yeah... I'm ready for it, Carol!"
play channel2 "sounds/wank.mp3"
window hide

label SaunaMILFSlowx:
hide cum
hide faster
hide slower
window hide
show milfsaunablowslowvideo behind milfsaunablowfastvideo
$ renpy.pause(2.0, hard='True')
hide milfsaunablowfastvideo
with dissolve
mc "Damn that's good... Nice and slow..."
window hide
show faster:
     xpos 1700 ypos 500
play channel1 "sounds/blow01.mp3"
call screen screensaunaMILFslowx()
screen screensaunaMILFslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SaunaMILFFastx")

label SaunaMILFFastx:
hide cum
hide slower
hide faster
mc "Please... DO it faster!"
window hide
show milfsaunablowfastvideo behind milfsaunablowslowvideo
$ renpy.pause(1.0, hard='True')
hide milfsaunablowslowvideo
with dissolve
stop channel1
play channel1 "sounds/blow02.mp3"
show slower:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen screensaunaMILFfastx()
screen screensaunaMILFfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("SaunaMILFSlowx")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("SaunaMILFCumx")

label SaunaMILFCumx:
hide cum
hide faster
hide slower
mc "I'm about to bust my nut, Carol..."
window hide
$ renpy.pause(2.0, hard='True')
stop channel2
stop channel1
scene poolmilfsaunacum01 with dissolve
hide milfsaunablowslowvideo
hide milfsaunablowfastvideo
play sound "sounds/boymoan03.mp3"
mc "AAAH! Directly into your mouth!"
window hide
with fastflash
cm "Gllluub..."
play sound "sounds/boyorgasm01.mp3"
scene poolmilfsaunacum02 with dissolve
mc "Fuck! AAAH, my cream is flowing out of your mouth!"
window hide
with fastflash
mc "STIIIILLL... BLLAAA-AAA-STING!"
play sound "sounds/boymoan02.mp3"
scene poolmilfsaunacum03:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "Oh God..."
play sound "sounds/panting.mp3"
stop music
scene poolmilfsaunacum04 with dissolve
cm "Is it.... finally going to go down now?"
mc "Not if you're ready for some mo..."
cm "No [name], you must get this thing DOWN now! The security of the compound is at stakes!"
mc "Alright, Captain MILF, I'll... go back to my room then. Thanks for the blowjob."
jump MILFGallery

label MILFGallery03:
stop channel3
scene milfroomnightyoga01 with fade
play channel1 "sounds/relax.mp3"
mc "I'll go and see what Captain MILF is doing..."
scene milfroomnightyoga02 with dissolve
cm "Oh, hello sweetie. I was just doing a bit of yoga stretching before heading to bed..."
mc "And I was just passing by in the hope you were..."
scene milfroomnightyoga03 with dissolve
cm "You can watch, but don't disturb me. I need to concentrate on all my MUSCLES."
scene milfroomnightyoga04 with dissolve
cm "It's important that I stay in shape, don't you agree?"
mc "Oh yeah, totally."
scene milfroomnightyoga05 with dissolve
cm "If our enemies were to attack us, I would be READY to REPEAL them."
mc "So would I! Although maybe not quite right now."
scene milfroomnightyoga06 with dissolve
cm "And why is that, [name]?"
mc "Well, I'm, like, too focused on something else right now..."
scene milfroomnightyoga07 with dissolve
cm "Ooh? And what would that be?"
scene milfroomnightyoga08 with dissolve
mc "...Gllrr..."
cm "Why don't you help me stretch my leg muscles instead of mumbling to yourself? Hold my left foot for me while I stretch them."
scene milfroomnightyoga09 with dissolve
cm "[name]! Your... thing... it's getting awfully BIG! What is happening?"
scene milfroomnightyoga10 with dissolve
mc "It's not my fault, I..."
scene milfroomnightyoga11 with dissolve
mc "...can't help it!"
if seenmilfsauna or seenmilfyoga:
    cm "Oh dear, you're getting a HARDON! In front of your landlady! AGAIN!"
else:
    cm "Oh dear, you're getting a HARDON! In front of your landlady!"
scene milfroomnightyoga12 with dissolve
cm "This can't be happening! I need to..."
scene milfroomnightyoga13 with dissolve
if seenmilfsauna or seenmilfyoga:
    cm "...look away NOW! Please leave [name], I can't afford to lose my superpowers! Yet AGAIN!"
else:
    cm "...look away NOW! Please leave [name], I can't afford to lose my superpowers!"
mc "I'm sorry Carol! I'll... leave now. And take care of that hardon myself..."
scene milfroomnightyoga14 with dissolve
if age >= 20:
    cm "Don't say that, I'm imagining you jerking off that fat donkey-dick of yours! Please go away, I'm having terrible landlady-tenant thoughts! "
if age >= 18 and age <= 19:
    cm "Don't say that, I'm imagining you jerking off that fat teenage donkey-dick of yours! Please go away, I'm having terrible landlady-tenant thoughts! "
jump MILFGallery

label MILFGallery04:
stop music
stop channel3
play music "sounds/sexy05.mp3"
scene compoundmilfnightseduction01
show milfseduction01
with dissolve
cm "This is why you came, isn't it. To SEDUCE me again. Without your cock again." 
mc "I was hoping you weren't going to say that second part. * sigh *"
hide milfseduction01
show milfseduction02
with dissolve
cm "I will enjoy it. You playing softly with my body." 
mc "Alright, I'll do it then!"
hide milfseduction02
show milfseduction03
with dissolve
cm "Come forward, [name], your landlady is ready for some SENSUAL loving..."        
scene compoundmilfnightseduction02
show milfseduction04
with dissolve
play sound "sounds/moan02.mp3"
cm "Mmmh, go slowly, [name]. We have plenty of time..."        
hide milfseduction04
show milfseduction05
with dissolve
play sound "sounds/moan01.mp3"
cm "That's better, [name]..."
mc "Let me slowly slide your gown off before I..."
hide milfseduction05
show milfseduction06
with dissolve
play sound "sounds/moan03.mp3"
mc "...play with your belly button..."
cm "Oooh, I didn't expect that..."
scene milfseduction07 with dissolve
play sound "sounds/moan01.mp3"
cm "Oooh, what are you doing, naughty boy?"
scene milfseduction08 with dissolve
play sound "sounds/lick01.ogg"
mc "Just making sure your pussy is nice and wet..."
scene milfseduction09 with dissolve
play sound "sounds/moan02.mp3"
cm "Push my panties aside slowly, [name]..."        
scene milfseduction10 with dissolve
cm "Mmh, just like that, gently pull them down now..."
scene milfseduction11 with dissolve
mc "And now I can lick your sweet nectar direct from the source..."
cm "Please hurry up, I'm so wet..."
scene milfseduction12 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH!"
window hide
with hpunch
mc "Did I just make you cum, CArol?"
cm "Yes, a little bit... I need to play with my big titties..." 
mc "Allow me... As a landboy, it is my duty to pleasure my landlady..."
scene milfseduction13 with dissolve
play channel1 "sounds/moan02.mp3"
cm "Mmmh, knead them for me, make them all YOURS!"
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
stop music
mc "They feel so fucking big, Carol... You are the epitome of the SUPER-heroine! And SUPER-LANDLADY."
if age >= 20:
    cm "Oh, I'm gonna cum again, my dear hunk of a tenant!"
if age >= 18 and age <= 19:
    cm "Oh, I'm gonna cum again, my dear teenage hunk of a tenant!"
stop channel1
window hide
play sound "sounds/womancum01.mp3"
with hpunch
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
cm "Now play with my pussy and make me EXPLODE with pleasure, sweetie pie!"
scene milfseduction15 with dissolve
play sound "sounds/moan01.mp3"
cm "Mmh, yes, just like that..."
scene milfseduction16 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH, it's so good!"
play channel1 "sounds/moan03.mp3"
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
mc "And now for the Grand Finale..."
stop channel1
scene milfseduction17 with dissolve
play sound "sounds/womancum02.mp3"
cm "OOOOOHHHH!"
window hide
with hpunch
mc "Yeah, squirt for me, Carol!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
cm "AAAAH!"
mc "I did, I made you squirt!"
cm "So you did, and you deserve a reward. A MILKY REWARD!"
scene milfseduction18 with dissolve
cm "So come and get it, your landlady still has breast milk from when, err... whatever."
scene milfseduction19 with dissolve
play sound "sounds/slurp.mp3"
cm "Oooh, yes, pinch my right nipple while you suckled on my left tit..."
play sound "sounds/moan01.mp3"
mc "I love your landlady milk, I want more!"
scene milfseduction18 with dissolve
cm "It's all for you, my sweet boy."
scene milfseduction19 with dissolve
play sound "sounds/slurp.mp3"
cm "That's it, slurp it all up, you deserve it, you've been  such a GOOD boy!"
scene milfseduction20 with dissolve
cm "Was it good, my sweet landboy?"
mc "Super-Tasty, Carol!"
cm "Then let ME taste it too..."
stop music
stop music
scene milfseduction21:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
play sound "sounds/kiss.mp3"
cm "Now kiss me tenderly..."
play sound "sounds/kiss.mp3"
cm "And go back to your room, my dear young landboy."
stop music
stop channel1
jump MILFGallery

label MILFGallery05:
stop channel3
stop channel1
play music "sounds/sexy12.mp3"
scene compoundmilfnightseduction02
show milfmaledom01
with dissolve
if evilness <= 12:
    cm "My sweet landboy, I'll do whatever you want cos you've been such a GOOD boy, but we must be quick about it."
    mc "Let's see how it goes. I might need multiple releases, Carol."
if evilness >= 13:
    cm "The compound is at our enemies' mercy without my Super-powers. Don't you care?"
    mc "Nope. I care about only one thing right now... Fucking you on your bed. And you only care about that too, admit it, Captain MILF!"
hide milfmaledom01
show milfmaledom02
with dissolve
if evilness <= 12:
    cm "Alright, I can't say no to you, you're such an ASSET to the compound... And your cock... Is making me weak in the knees..."
    mc "I know but I chose you because you're the hottest MILF here! And you're my landlady too..."
    hide milfmaledom02
    show milfmaledom01
    with fastdissolve
    cm "Really?? You think that? I'm not too old for such a strapping young SUPERSTUD like you?"
    mc "Of course not, Carol! Now please show me that sumptuous ass of yours..."
if evilness >= 13:
    cm "I... Yes, I admit it. I am just a filthy landlady who can't help but lust after her horse-hung tenant's [age]year-old MONSTER COCK..."
    mc "Turn round Carol, I want to see that sumptuous ass of yours again..."
window hide
hide milfmaledom01
hide milfmaledom02
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 1.8
    xpos 0.4 ypos 1.6
    ease 7.5 xpos 0.42 ypos 1.0           
show milfmaledom03:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
if evilness <= 12:
    mc "Fuck yeah! I'm going to ENJOY working that hot landlady ass tonight!"
    cm "You're being VERY naughty. But you're just so horny, aren't you? My poor sweet tenant..."
    mc "Yeah, you're just so hot I'm getting a MASSIVE hardon... You need to do something about it, Carol."    
if evilness >= 13:
    mc "Fuck yeah! I'm going to DESTROY that ass tonight!"
    cm "You want to destroy's your landlady's ass? That's so... filthy, [name]!"
    mc "It's not filthy, it's the natural stage of landboy superhero evolution. Now worship my cock!"
scene milfmaledom04 with dissolve
cm "[name], your cock! It's just so ENORMOUS!"
mc "That's right, and YOU'RE the one who rents a room to this SUPER-STUD."
scene milfmaledom05 with dissolve
play sound "sounds/kiss.mp3"
cm "I'm such a proud landlady. * kisses *"
play sound "sounds/kiss.mp3"
cm "Having such a HORSE-HUNG landboy... * kiss *"
scene milfmaledom06 with dissolve
play sound "sounds/lick02.mp3"
if age >= 20:
    cm "And your balls... They're just so MANLY. So full of hot, young VIRILE CUM!"
if age >= 18 and age <= 19:
    cm "And your balls... They're just so MANLY. So full of hot, young VIRILE TEENAGE CUM!"
mc "AAAH..."
scene milfmaledom07 with dissolve
play sound "sounds/lick03.mp3"
cm "You like it when I worship your HUGE BULL-BALLS?"
mc "FUCK!!! Yes, I do, you're doing a great job, Carol!"
scene milfmaledom08 with dissolve
cm "You're making me so horny, [name]! I need to take this bra off..."
mc "Yeah, you do... And your panties too... SO I can POUND THAT ASS!"
scene milfmaledom09 with dissolve
cm" But... Your love muscle is just so BIG! DO you think it will fit inside my tight little butthole?"
mc "I'll make it fit. Even if it means I have to DESTROY YOUR HOLE!"
scene milfmaledom10 with dissolve
cm "Maybe you should lubricate my rosebud with your abundant precum, [name]."
mc "Damn, Captain MILF, you're making me LEAK so damn much!"
scene milfmaledom11 with dissolve
play sound "sounds/moan02.mp3"
cm "Rub your giant pecker against my puckered backdoor then..."
scene milfmaledom12 with dissolve
play sound "sounds/moan03.mp3"
cm "Yes, just like that, [name]..."
if evilness <= 12:
    scene milfmaledom13a with dissolve
    mc "Let me carry you to the bed so we can make sweet anal love, Carol."
    cm "You're such a GOOD superhero landboy... I'll let you do ANYTHING you want to my poor little hole..."
if evilness >= 13:
    scene milfmaledom13b with dissolve
    cm "Wh.. What are you doing?"
    mc "I can't wait any longer, prepare to get ANALLY IMPALED on my giant cock!"
    cm "Oh, you're so ROUGH! You treat your landlady like a cheap whore!"
    mc "That's cos you ARE a CHEAP WHORE, Captain MILF!"
scene milfmaledom14 with dissolve
play sound "sounds/moan04.ogg"
if evilness <= 12:
    cm "Aaah, you're so STRONG, [name]! And I've lost all my superpowers anyway... PLease RAVISH me like the young STUD that you are!"
    mc "Are you ready to get STRETCHED by my massive dong, Carol?"
    if age >= 20:
        cm "Yes I am, go on, you can stick your giant pud in me as far as it will go, [name]!"
    if age >= 18 and age <= 19:
        cm "Yes I am, go on, you can stick your giant teenage pud in me as far as it will go, [name]!"
if evilness >= 13:
    cm "Aaah, You're holding my legs in such a tight muscular armlock, I can't move, I'm totally at the mercy of your HOLE-DESTROYER!"
    mc "That's right, so get ready for the ASS-POUNDING of your lifetime, Carol!"
    if age >= 20:
        cm "Go on, stick your giant pud as far as it will go and do your filthy deed with my landlady hole!"
    if age >= 18 and age <= 19:
        cm "Go on, stick your giant teenage pud as far as it will go and do your filthy deed with my landlady hole!"
window hide
stop music

label MilfAssFuckSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckslowvideo behind milfassfuckfastvideo
show milfassfuckslowvideo behind milfassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ milfassfuckfast = False
if milfassfuckslow == False:
    cm "Oh my God, you're stretching me so much with your enormous dong, [name]!"
    $ milfassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfassfuckslowx()
screen milfassfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfAssFuckFrontSlowx")

label MilfAssFuckFastx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfastvideo behind milfassfuckslowvideo
show milfassfuckfastvideo behind milfassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckslowvideo
hide milfassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ milfassfuckslow = False
if milfassfuckfast == False:
    mc "I'm gonna POUND that ass even FASTER now, Carol!"
    $ milfassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen milfassfuckfastx()
screen milfassfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfAssFuckFrontFastx")

label MilfAssFuckFrontSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfrontslowvideo behind milfassfuckslowvideo
show milfassfuckfrontslowvideo behind milfassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckslowvideo
hide milfassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ milfassfuckfast = False
if milfassfuckslow == False:
    cm "Oh my God, you're stretching me so much with your enormous dong, [name]!"
    $ milfassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen milfassfuckfrontslowx()
screen milfassfuckfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckSlowx")

label MilfAssFuckFrontFastx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfrontfastvideo behind milfassfuckfastvideo
show milfassfuckfrontfastvideo behind milfassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ milfassfuckslow = False
if milfassfuckfast == False:
    mc "I'm gonna POUND that ass even FASTER now, Carol!"
    $ milfassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen milfassfuckfrontfastx()
screen milfassfuckfrontfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFastx")

label MilfAssFuckEndx:
hide cum
hide assview
hide faster
hide slower
hide front
mc "Your ass is milking my dong..."
cm "I can feel every ridge of your MONSTERCOCK, I KNOW you're about to blow! Do it for your landlady, paint her insides with your spunk!" 
scene milffuckcum01 with dissolve
play channel1 "sounds/splooge02.mp3"
hide milfassfuckslowvideo
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
hide milfassfuckfrontfastvideo
play sound "sounds/boymoan05.mp3"
if evilness <= 12:
    mc "AAAH, take that, Carol, filling your ass with my cream!"
if evilness >= 13:
    mc "AAAH, take that you filthy cock-whore, filling your ass with my cream!"
window hide
with fastflash
cm "AAAH, you're so naughty, but your cock is just so good!"
window hide
with fastflash
cm "I can feel every MONSTERSHOT inside my ass!"
scene milffuckcum02 with dissolve
play sound "sounds/moan04.ogg"
play channel2 "sounds/boyorgasm01.mp3"
cm "[name], you're... PUMPING ME FULL! There's SO MUCH of it!"
window hide
with fastflash
mc "There's more where that came from, RHAAA!"
scene milffuckcum03 with dissolve
if evilness <= 12:
    cm "I need to SEE your CONVULSING cock as it BLASTS all that hot young sperm!"
if evilness >= 13:
    mc "Pull it out, I'm gonna repaint your body in my spunk and CLAIM you as MY slut, Carol!"
window hide
with fastflash
if evilness <= 12:
    mc "Go on, take it out, I'll BLAST all over your hot bod, AAAH!"
if evilness >= 13:
    cm "You're treating me like your SEX SLAVE, [name]! And I can't resist!"
    mc "That's cos you're MY SEX SLAVE NOW!"
scene milffuckcum04 with dissolve
stop channel1
play sound "sounds/moan01.mp3"
if age >= 20:
    cm "You're STILL cumming so MUCH, [name]! You're such a HUGE-DICKED STALLION!"
if age >= 18 and age <= 19:
    cm "You're STILL cumming so MUCH, [name]! You're such a HUGE-DICKED TEEN STALLION!"
window hide
with fastflash
mc "You're making me cum NON-STOP, FFFUUUUUUCCCCKKKK!"
scene milffuckcum05 with dissolve
play sound "sounds/moan03.mp3"
if evilness <= 12:
    cm "I'm so happy to be satisfying your sexual needs, [name]!"
if evilness >= 13:
    cm "More, MORE, cover your filthy cock-whore landlady with your scalding scum, [name]!"
window hide
with fastflash
mc "Take those shots, RHAAA!"
scene milffuckcum06 with dissolve
stop channel2
play sound "sounds/moan02.mp3"
if evilness <= 12:
    cm "You took my ass and turned it inside out, [name]... But I've never been pleasured so much in my life before! You deserve a REWARD!"
if evilness >= 13:
    cm "You totally DESTROYED my ass... And then you CAKED me in your red-hot sperm... I feel so filthy..."
scene milffuckcum07 with dissolve
if evilness <= 12:
    mc "Oooh, what do you have in store for me, Carol?"
    cm "I'm offering you... My tits! Stick your monster shaft between them and I will take you to heavens!"
if evilness >= 13:
    mc "You ARE filthy, Carol. And you deserve a PUNISHMENT for that."
    cm "Wh.. What? Please, I need to get my superpowers back. You've been fucking me for way too long, [name]!"
if evilness <= 12:
    scene milffuckcum08a with dissolve
    if age >= 20:
        cm "See how BIG they are? Perfect for your HUGE MONSTERDONG!"
    if age >= 18 and age <= 19:
        cm "See how BIG they are? Perfect for your HUGE TEEN MONSTERDONG!"
if evilness >= 13:
    scene milffuckcum08b with dissolve
    mc "My cock is DEMANDING more attention. From your MASSIVE funbags!"
    cm "But [name]... Oh, I can't say no to my GIANT-COCKED tenant! Just fuck my tits to your heart's content, [name]!"
scene milffuckcum09 with dissolve
if evilness <= 12:
    cm "Just FUCK MY TITS TO YOUR HEART'S CONTENT!"
    mc "I sure will. They are so fucking big. It will be the BEST titfuck I ever had."
if evilness >= 13:
    mc "I sure will. They are so fucking big. It will be the BEST titfuck I ever had."
play sound "sounds/moan01.mp3"
cm "You like your landlady's enormous breasts, don't you, you naughty boy?"
scene milffuckcum10 with dissolve
mc "Fuck yeah, I'm gonna PUMMEL my shaft between those soft pillows."
cm "I will make sure you cum a HUGE load again, until you are completely satisfied. I can't leave you like that with such an aching hardon!"
play channel1 "sounds/wank.mp3"
window hide

label MilfTitFuckSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckslowvideo behind milftitfuckfastvideo
show milftitfuckslowvideo behind milftitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
with dissolve
play channel2 "sounds/boymoan04.mp3"
$ milftitfuckfast = False
if milftitfuckslow == False:
    cm "Your cock is so big, it's stretching all the way to my face!"
    $ milftitfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milftitfuckslowx()
screen milftitfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFrontSlowx")

label MilfTitFuckFastx:
$ milftitfuckslow = False
if milftitfuckfast == False:
    mc "Damn, those big tits are so good around my shaft, Carol!"
    cm "Then pump that big fucking dick between them FASTER, [name]!"
    $ milftitfuckfast = True
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfastvideo behind milftitfuckslowvideo
show milftitfuckfastvideo behind milftitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckslowvideo
hide milftitfuckfrontfastvideo
with dissolve
play channel2 "sounds/boymoan02.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen milftitfuckfastx()
screen milftitfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFrontFastx")

label MilfTitFuckFrontSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfrontslowvideo behind milftitfuckslowvideo
show milftitfuckfrontslowvideo behind milftitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckslowvideo
hide milftitfuckfrontfastvideo
with dissolve
play channel2 "sounds/boymoan04.mp3"
$ milftitfuckfast = False
if milftitfuckslow == False:
    cm "Your cock is so big, it's stretching all the way to my face!"
    $ milftitfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen milftitfuckfrontslowx()
screen milftitfuckfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckSlowx")

label MilfTitFuckFrontFastx:
$ milftitfuckslow = False
if milftitfuckfast == False:
    mc "Damn, those big tits are so good around my shaft, Carol!"
    cm "Then pump that big fucking dick between them FASTER, [name]!"
    $ milftitfuckfast = True
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfrontfastvideo behind milftitfuckfastvideo
show milftitfuckfrontfastvideo behind milftitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
with dissolve
play channel2 "sounds/boymoan02.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sideicon:
     xpos 1700 ypos 500     
call screen milftitfuckfrontfastx()
screen milftitfuckfrontfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFastx")

label MilfTitFuckEndx:
window hide
hide cum
hide sideicon
hide faster
hide slower
hide front
if evilness <= 12:
    cm "Are you going to BLAST that hot load for me?"
if evilness >= 13:
    cm "Are you going to BLAST that hot load for your filthy slut of a landlady?"
mc "Any minute now, Carol, any min..."
window hide
scene milftitfuckcum01 with dissolve
hide milftitfuckslowvideo
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
hide milftitfuckfrontfastvideo
stop channel1
stop channel2
play sound "sounds/boymoan05.mp3"
cm "Oh, look at your huge pole cumming, my horny landboy!"
window hide
with fastflash
mc "AAAH, your giant milkbags did that!"
scene milftitfuckcum02 with dissolve
play sound "sounds/boymoan03.mp3"
cm "I'm so PROUD that your landlady's big fat filthy tits made you cum so hard, [name]!"
window hide
with fastflash
mc "I'm not done Captain MILF, RHAAA!"
scene milftitfuckcum03 with dissolve
play sound "sounds/boymoan05.mp3"
cm "I KNOW you still have a LOT of creamy fuckjuices for your landlady, don't you, my sweet young boy?"
window hide
with fastflash
mc "Oh, CAROL, AAAAH! You're such a dirty talker, you're making me CUUU-UUUUM!!!"
scene milftitfuckcum04 with dissolve
play sound "sounds/panting.mp3"
cm "You gave me so MUCH cum... I'm COVERED in your tenant splooge..."
mc "Then clean my cock up, I need to go back to my room. We wouldn't want the whole compound turning up here and seeing us like that, now would we?"
scene milftitfuckcum05 with dissolve
play sound "sounds/lick03.mp3"
if evilness <= 12:
    mc "Yeah, slurp it all up, Carol, I need a clean cock to fight our super-villain ENEMIES!"
if evilness >= 13:
    mc "Yeah, slurp it all up, like a good cum-whore..."
scene milftitfuckcum06 with dissolve
play sound "sounds/lick02.mp3"
if evilness <= 12:
    cm "I agree, [name]... * slurp * You can't go out like that with such a DIRTY, CUM-COVERED DONG!"
if evilness >= 13:
    cm "I'm a cum-whore for... * slurp * ...my horse-hung landboy who just came all over my big titties!"
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(1.0, hard='True')
scene milftitfuckcum06 with fastdissolve
play sound "sounds/lick02.mp3"
$ renpy.pause(0.5, hard='True')
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(1.0, hard='True')
scene milftitfuckcum06 with fastdissolve
play sound "sounds/lick02.mp3"
$ renpy.pause(0.5, hard='True')
mc "Fuck yeah, that's good, Carol... I'll give you your super-powers back now..."
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
cm "By going back to your room?"
mc "Yeah, that's right."
stop channel2
stop channel1
stop music
jump MILFGallery

label MILFGallery06:
stop channel3
scene gymmilfnew01 with dissolve
mc "There's Captain MILF doing some squats. Let's get closer..."
scene gymmilfnew02 with dissolve
cm "Well hello there, sweetie pie!"
mc "Man, that outfit is like ssooo 80s."
cm "Yes, it is very modern isn't it? I love this avant-garde style! Don't you?"
mc "Err... Yeah I guess. When YOU wear it that is."
cm "Hum, I don't know if what you said was sweet or had some kind of sexual connotation..."
cm "Anyway, you can watch Captain MILF squat over 3 tons of Krypton steel weights if you want."
mc "I do want."
show gymmilfsquatvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020
call screen GymMILFsquatx()
screen GymMILFsquatx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEndx")

label GymMILFSquatEndx:
if mcsenses >= 1:
    call screen usepower("usesenses", "GymMILFSquatEnd02x", "GymMILFNudePreSquatx") with dissolve
if mcsenses == 0:
    jump GymMILFSquatEnd02x

label GymMILFNudePreSquatx:
hide nexticon
mc "Let's focus my Super-Senses on her Super-Tits..."
window hide

label GymMILFNudeSquatx:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedfastvideo behind gymmilfsquatnakedslowvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedslowvideo
with dissolve

show nexticon:
    xpos 1750 ypos 1020
show slower:
     xpos 50 ypos 500     
call screen GymMILFnudesquatx()
screen GymMILFnudesquatx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquatSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02x")

label GymMILFNudeSquatSlowx:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedslowvideo behind gymmilfsquatnakedfastvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedfastvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen GymMILFnudesquatslowx()
screen GymMILFnudesquatslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquatx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02x")

label GymMILFSquatEnd02x:
scene gymmilfnew03 with dissolve
cm "And now, lifted high above my head!"
if mcstrength >= 2:
    mc "Not bad, I can do it too though, it's easy with Super-Strength level 2."
if mcstrength == 1:
    mc "Not bad, but I can do it too even with just Super-Strength level 1."
scene gymmilfnew04:
    zoom 0.5 xoffset 0 yoffset 0
with dissolve
cm "But can you do it with one hand while FLEXING your biceps?"
mc "Damn, Captain MILF! Your biceps... They're BULGING!..."
scene gymmilfnew04:
    subpixel True
    zoom 0.5 xoffset 0 yoffset 0
    linear 5.0 zoom 1.0 xoffset -600 yoffset -600
$ renpy.pause(4.0, hard='True')
cm "Maybe I should turn round to prove to you how FIT your League Captain is..."
mc "Indeed you should. I need convincing right NOW!"
scene gymmilfnew05:
    subpixel True
    ypos 0.0
    ease 4.0 xpos -0.02 ypos -0.99
$ renpy.pause(4.0, hard='True')
mc "* What a tight ass! Maybe I should get h... *"
cm "Don't get any funny ideas, [name]. You wouldn't want to mess with me while I'm in this PUMPED-UP state!"
scene gymmilfnew06 with dissolve
cm "Imagine the DAMAGE those iron-hard abs could cause on some unsuspecting victim..."
mc "By victim you're talking about ME and my COCK?"
scene gymmilfnew07 with dissolve
cm "Maybe I am... Let's see how YOU fare in the muscle department now that your superpowers have improved a bit... Flex those guns for me, sweetie pie!"
scene gymmilfnew08 with dissolve
mc "Alright, I've been practising my routine after watching a movie with a new young Austrian muscled actor in it. It was a rubbish B-flick but I learnt a few things about..."
scene gymmilfnew09 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "...MUSCLE FLEXING!"
cm "Mmmh, they really are getting VERY BIG! Captain MILF has a big announcement for you, come closer my dear boy..."
scene gymmilfnew10 with dissolve
cm" It's time for you to reach Super-Hero LEVEL 2. My machine is ready."
mc "ALRIGHT! Can we do it, like, right now?"
cm "Not really, you're in the gallery and this section is about to end."
stop channel2
stop channel1
stop music
jump MILFGallery

label MILFGallery07:
$ milfdptalkfirstx = False
$ supdptalkfirstx = False
$ dpmilfcamex = 0
$ dpsupcamex = 0
$ milfdptalkcumfirstx = False
$ supdptalkcumfirstx = False
$ talkedswitchmilfx = False
$ talkedswitchsupx = False
$ talkedswitchmilfcumx = False
$ talkedswitchsupcumx = False
stop channel3
scene mcroomsex01
stop music
play music "sounds/sexy04.mp3"
cm "Oh... Where am I? It's you, sweetie pie?"
mc "Yes Carol, you fainted when...err... I came out of your radiation machine."
scene mcroomsex02 with dissolve
cm "And why is Supergirl so... BIG???"
mc "She also entered the machine. I told her not to but..."
play sound "sounds/moan02.mp3"
sg "Look, I can flex my biceps into BOULDERS OF MUSCLE!"
scene mcroomsex03 with dissolve
sg "And I just can't keep my eyes off my new enhanced SUPER-BOOBS!"
mc "Neither can I... I still have a massive aching hardon..."
scene mcroomsex04 with dissolve
cm "I need to take my top off, I'm still all flushed..."
mc "I can give you a nice massage to help you recover your superpowers."
scene mcroomsex05 with dissolve
cm "That would be lovely, sweetie pie! Let me get some nice cushion so I can lie down comfortably on the bed."
scene mcroomsex06 with dissolve
cm "I'm ready! And looking the other way so I don't see your huge... thingie."
mc "I'll try and keep it out of the way but damn! It's at least three inches bigger than it used to be!"
play sound "sounds/moan03.mp3"
cm "THREE INCHES? Ooohhh...."
scene mcroomsex07 with dissolve
cm "Mmh, that's nice, sweetie pie..."
scene mcroomsex08 with dissolve
mc "Your buns are just so... amazingly tight, Captain MILF!"
cm "I can crush a walnut between my cheeks."
mc "Right, err... You'll have to show me that one day."
scene mcroomsex09 with dissolve
mc "In the meantime..."
play sound "sounds/moan02.mp3"
cm "Oooh, what are you doing, naughty boy?"
mc "Massaging the INSIDE of your snatch. It needs to dilate quite a bit, considering my NEW size."
cm "Are you planning on... fucking your landlady with your monster cock?"
mc "I can't say it didn't cross my mind."
scene mcroomsex10 with dissolve
play sound "sounds/moan01.mp3"
cm "That was VERY good, my lovely tenant... Now it is MY turn to show my appreciation."
scene mcroomsex11a with dissolve
play sound "sounds/gasp.mp3"
cm "Oh my dear Lord! You HAVE grown quite a bit, haven't you, sweetie pie?"
mc "Yes, and I'm so hard, it's literally aching!"
sg "It's...even more beautiful that before..."
scene mcroomsex12 with dissolve
cm "I think I should test your level 2 Super-Studliness power before... you use it badly on someone."
mc "Why would I use it badly?"
cm "I sense that you are... still hesitant about where you stand..."
if evilness >= 13:
    mc "Has Wonder Woman said anything?"
    cm "About what?"
    mc "Err... nothing. Let's do it, Carol, I'm still sporting a giant hardon for you!"
if evilness <= 12:
    mc "I'm a Superhero and I'll prove it to you. With my Super-Cock!"
scene mcroomsex13 with dissolve
cm "I can see that, sweetie pie... Show me how you please a woman with that giant pecker!"
mc "Oh God, this is about to get real HOT!"
scene mcroomsex18 with dissolve
mc "Fuck, I'm just so fucking HUGE for you, Captain MILF!"
cm "I can't even watch, I fear I might faint again seeing your behemoth plowing through my love canal..."
scene mcroomsex19a with dissolve
play sound "sounds/thud.mp3"
mc "Can you feel how HEAVY it is Carol?"
play channel2 "sounds/moan02.mp3"
window hide
scene mcroomsex19b with dissolve
$ renpy.pause(.8, hard='True')
play channel1 [ "sounds/thud.mp3", "<silence .9>"]
scene milfcockslap
pause
cm "Oh God... It's the BIGGEST piece of [age]yo boymeat on Earth, sweetie pie! Just Give it to me, I WANT IT!"
stop channel1
stop channel2
scene mcroomsex20 with dissolve
play sound "sounds/moan06.ogg"
mc "I'll make you recover your superpowers by giving you my Super-Cock!"
$ milfmassagetalkslowx = True

label MILFMassageSlowx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
window hide
show milfmassageslowvideo behind milfmassagepovslowvideo
show milfmassageslowvideo behind milfmassagefastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovslowvideo
hide milfmassagefastvideo
with dissolve

show faster:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milfmassageslowx()
screen milfmassageslowx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageFastx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVSlowx")

label MILFMassageFastx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
window hide
show milfmassagefastvideo behind milfmassagepovfastvideo
show milfmassagefastvideo behind milfmassageslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovfastvideo
hide milfmassageslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milfmassagefastx()
screen milfmassagefastx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVFastx")

label MILFMassagePOVSlowx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
window hide
show milfmassagepovslowvideo behind milfmassageslowvideo
show milfmassagepovslowvideo behind milfmassagepovfastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassageslowvideo
hide milfmassagepovfastvideo
with dissolve
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfmassagepovslowx()
screen milfmassagepovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageSlowx")

label MILFMassagePOVFastx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
window hide
show milfmassagepovfastvideo behind milfmassagefastvideo
show milfmassagepovfastvideo behind milfmassagepovslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagefastvideo
hide milfmassagepovslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfmassagepovfastx()
screen milfmassagepovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageFastx")

label MILFMassageEndx:
hide cum
hide faster
hide slower
hide pov
hide sceneicon
play sound "sounds/moan05.mp3"
cm "Sweetie, I... PLEASE CUM INSIDE ME, YOU STALLION!"
mc "I wonder if my loads have also increased in..."
stop channel2
scene mcroomsex21 with dissolve
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boyorgasm01.mp3"
mc "...size. AAAAH! Here it comes!"
window hide
with fastflash
mc "And it feels so fucking good!"
scene mcroomsex22 with dissolve
cm "Oh dear me, is that still the same shot? You've been pumping your seed for so long already, sweetie pie!"
window hide
with hpunch
mc "Oh Fuck, can't stop NU-UU-TTING!!"
scene mcroomsex23 with dissolve
cm "Maybe you should dump the rest on me, I'm starting to feel a bit... bloated with your young spunk!"
window hide
with fastflash
mc "Oh damn, alright, gonna try and pull it out while I'm still spewing my sauce, RHAAAA!"
scene mcroomsex24 with dissolve
stop channel2
if age >= 20:
    cm "Oh my goodness, you're splattering your potent goo all over my body!"
if age >= 18 and age <= 19:
    cm "Oh my goodness, you're splattering your potent teenage goo all over my body!"
window hide
with fastflash
cm "Give me more [name], DROWN ME IN YOUR SWEET CUM!"
scene mcroomsex25 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE YOU GO CAROL, AAAHHH!"
window hide
with fastflash
sg "This is crazy! He's coming like a FIREHOSE!"
scene mcroomsex26 with dissolve
play sound "sounds/panting.mp3"
play channel2 "sounds/splooge02.mp3"
cm "You came so much inside me, sweetie pie... Oooh..."
mc "Damn, I can see that..."
scene mcroomsex27 with dissolve
play sound "sounds/lick02.mp3"
cm "Why don't you come and help me clean up this cummy mess, Linda?"
scene mcroomsex28 with dissolve
stop channel2
sg "But... This is so lewd! He's my distant cousin!"
cm "So? It's not incest, you're way TOO distant. And you've been a NAUGHTY girl testing my machine without my authorization!"
sg "Uh... Alright, Captain MILF."
scene mcroomsex30 with dissolve
play sound "sounds/lick01.ogg"
cm "There you go, slurp his cum slowly... And lick my giant MILF funbags..."
scene mcroomsex31 with dissolve
play sound "sounds/lick02.mp3"
sg "*slurp *  He's made such a MESS!"
cm "That's why you have to be thorough... My pussy is DRIPPING with his spunk."
scene mcroomsex32 with dissolve
play channel2 "sounds/lick03.mp3"
play sound "sounds/moan03.mp3"
cm "Yes, just like that! AAAH!"
mc "Damn, I'm getting HARD again! Actually, I didn't even lose my MONSTER erection, but now I feel like I NEED to FUCK some MORE!"
scene mcroomsex33 with dissolve
stop channel2
cm "Lick my fingers clean Linda, I think [name] is about to give you something BIG to eat!"
play sound "sounds/lick03.mp3"
scene mcroomsex34 with dissolve
sg "What? Gggllll...."
mc "You'd better open up REAL WIDE distant cuz, show me that you DESERVE this dick!"
scene mcroomsex35 with dissolve
mc "Yeah, that's better... My knobhead just fits PERFECTLY inside your tiny cock-hungry mouth, doesn't it?"
sg "* Gllbbbb.... *"
cm "Now sweetie, be gentle when you POUND her face with your giant HORSEDICK!"
play channel1 "sounds/blow01.mp3"

label LindaDeepThroatSlowx:
hide slower
hide faster
hide cum
show lindasuckslowvideo behind lindasuckfastvideo
$ renpy.pause(1.0, hard='True')
hide lindasuckfastvideo
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen lindasuckslowx()
screen lindasuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEndx")

label LindaDeepThroatFastx:
show lindasuckfastvideo behind lindasuckslowvideo
hide cum
hide faster
hide slower
mc "That throat is so warm, I think I'm going to face-fuck you FASTER, whether you're ready or not!"
sg "* gllur *"
hide lindasuckslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500

call screen lindasuckfastx()
screen lindasuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEndx")

label LindaDeepThroatEndx:
hide nexticon
hide slower
hide faster
cm "Sweetie, I think she's struggling a bit, you'd better give it a rest. We'll lick your dong for you. BOTH OF US."
mc "Alright, that sounds like a good deal!"
stop channel1
scene supthroatpost01 with dissolve
play sound "v031/cough.mp3"
cm "Are you alright, Linda?"
sg "I can't... feeel my jaw...."
mc "Well, use your tongue instead then. On my knob."
scene supthroatpost02 with dissolve
play sound "sounds/kiss.mp3"
sg "Mmmh, it's so BEAUTIFUL! I want to lick it all over!"
cm "Me too, I'm totally under its spell right now..."
play channel1 "sounds/lick01.ogg"
scene massagelickthreesomevideo with dissolve
$ renpy.pause(1.0, hard='True')
mc "Mmh, two warm tongues... I'm in heavens!"
pause
cm "Just wait till you start FUCKING our pussies in unison, that will be TRUE heavens!"
scene supthroatpost03 with dissolve
stop channel1
mc "Oooh, wow, where do I sign up?"
cm "You can sign up very soon, sweetie pie. Let us worship that HUMONGOUS dong a bit more first... Especially Linda, she seems ENTRANCED by it!"
scene doublethroatsup with dissolve
play channel1 [ "sounds/blow02.mp3", "<silence .9>"]
pause
scene supthroatpost02 with dissolve
stop channel1
play sound "sounds/kiss.mp3"
cm "I think we're ready. Let us lign up our fuckholes for your great big whopper!"
scene dpprefuck01 with dissolve
mc "Are you ready to receive my mighty love muscle, Captain MILF?"
cm "Yes, sweetie pie. We're going to make you cum so many times that it will finally go down and I won't be under its gorgeous spell..."
scene dpprefuck02 with dissolve
play sound "sounds/moan05.mp3"
cm "OOOH! I can already feel your apple-sized helmet STRETCHING my pussylips... Be careful with that thing, [name]!"
$ milfdptalk01slowx = True
$ supdptalk01slowx = True

label DoubleFuckNoMilfSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slowx = True
window hide
show doublefuckslowvideo behind doublefuckfastvideo
show doublefuckslowvideo behind doublefuckslowpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckslowpovvideo
hide doublefuckfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkfirstx == False:
    if age >= 20:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milfdptalkfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknomilfslowx()
screen doublefucknomilfslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlowx") 

label DoubleFuckNoMilfFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
window hide
show doublefuckfastvideo behind doublefuckslowvideo
show doublefuckfastvideo behind doublefuckfastpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckfastpovvideo
hide doublefuckslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknomilffastx()
screen doublefucknomilffastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfPOVFastx") 

label DoubleFuckNoMilfPOVSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slowx = True
window hide
show doublefuckslowpovvideo behind doublefuckfastpovvideo
show doublefuckslowpovvideo behind doublefuckslowvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckfastpovvideo
hide doublefuckslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknomilfpovslowx()
screen doublefucknomilfpovslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSlowx") 

label DoubleFuckNoMilfPOVFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
window hide
show doublefuckfastpovvideo behind doublefuckslowpovvideo
show doublefuckfastpovvideo behind doublefuckfastvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckslowpovvideo
hide doublefuckfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknomilfpovfastx()
screen doublefucknomilfpovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfFastx") 

label DoubleFuckNoSupSwitchx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupslowvideo
if talkedswitchsupx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    cm "As long as you come back to cum inside me, sweetie pie!"
    $ talkedswitchsupx = True
window hide
show doublefuckmilfswitchvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupslowvideo behind doublefuckmilfswitchvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchvideo
hide doublefuckmilfswitchvideo
if supdptalkfirstx == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirstx = True
window hide
$ supdptalk01slowx = True
jump DoubleFuckNoSupSlowx

label DoubleFuckNoMilfSwitchx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckslowvideo
if talkedswitchmilfx == False:
    mc "I'm gonna switch for a while and ram my shaft inside Captain MILF's pussy again!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilfx = True
window hide
show doublefucksupswitchvideo
$ renpy.pause(0.6, hard='True')
show doublefuckslowvideo behind doublefucksupswitchvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchvideo
hide doublefucksupswitchvideo
$ milfdptalk01slowx = True
jump DoubleFuckNoMilfSlowx

label DoubleFuckNoSupSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slowx = True
window hide
show doublefucksupslowvideo behind doublefucksupfastvideo
show doublefucksupslowvideo behind doublefucksupslowpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupslowpovvideo
hide doublefucksupfastvideo
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknosupslowx()
screen doublefucknosupslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlowx") 

label DoubleFuckNoSupFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
window hide
show doublefucksupfastvideo behind doublefucksupslowvideo
show doublefucksupfastvideo behind doublefucksupfastpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupfastpovvideo
hide doublefucksupslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknosupfastx()
screen doublefucknosupfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupPOVFastx") 

label DoubleFuckNoSupPOVSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slowx = True
window hide
show doublefucksupslowpovvideo behind doublefucksupfastpovvideo
show doublefucksupslowpovvideo behind doublefucksupslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupfastpovvideo
hide doublefucksupslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknosuppovslowx()
screen doublefucknosuppovslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSlowx") 

label DoubleFuckNoSupPOVFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
window hide
show doublefucksupfastpovvideo behind doublefucksupslowpovvideo
show doublefucksupfastpovvideo behind doublefucksupfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupslowpovvideo
hide doublefucksupfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknosuppovfastx()
screen doublefucknosuppovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupFastx") 

label DoubleFuckNoMilfCumx:
$ milfdptalk01slowx = True
$ dpmilfcamex += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "I feel like I'm ready to blow a load, Captain MILF!"
cm "Then pump your seed inside me [name]!"
scene dpmilfnocum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene dpmilfnocum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene dpmilfnocum03 with dissolve
stop channel1
mc "There you go, Captain MILF, RHOOO!"
window hide
with fastflash
sg "He's really cumming like a STALLION!"
scene dpmilfnocum04 with dissolve
mc "Still more shots BLASTING, RHAAA!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
scene dpmilfcum05 with dissolve
mc "Getting back in that tight snatch of yours, Captain MILF!"
cm "Damn, you're still raring to go! How are we going to TAME your BEAST?"
stop channel2
jump DoubleFuckMilfSlowx

label DoubleFuckNoSupCumx:
$ supdptalk01slowx = True
$ dpsupcamex += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
sg "Your cock... It's becoming even BIGGER inside my pussy!"
mc "That's cos I'm about to blow another load!"
scene dpsupnocum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boymoan05.mp3" 
mc "AAAAH!"
window hide
with hpunch
sg "You're pumping so much spunk inside me, aaah!"
scene dpsupnocum02 with dissolve
play sound "sounds/boymoan04.mp3" 
mc "There's more where that came from, RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
if dpsupcamex == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcamex >= 1:
    sg "I'm getting BLOATED again by your MONSTER LOAD, you just cum like a FIREHOSE!"
scene dpsupnocum03 with dissolve
play sound "sounds/boymoan03.mp3" 
mc "Endless supplies of young, virile cum from THIS Super-Stud!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
sg "Don't stop, keep cumming, AAAH, I'm gonna squirt!"
window hide
with fastflash
mc "There you go, the last few shots just for you, Supergirl!"
window hide
with fastflash
stop channel2
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndx
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcamex == 0:
    jump DoubleFuckNoSupSlowx
jump DoubleFuckSupSlowx

label DoubleFuckMilfSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slowx = True
window hide
show doublefuckcumslowvideo behind doublefuckcumfastvideo
show doublefuckcumslowvideo behind doublefuckcumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckcumpovslowvideo
hide doublefuckcumfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkcumfirstx == False:
    if age >= 20:
        cm "You just came and you're STILL hard? My tenant is such a STALLION!"
    if age >= 18 and age <= 19:
        cm "You just came and you're STILL hard? My tenant is such a TEENAGE STALLION!"
        $ milfdptalkcumfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefuckmilfslowx()
screen doublefuckmilfslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlowx") 

label DoubleFuckMilfFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
window hide
show doublefuckcumfastvideo behind doublefuckcumslowvideo
show doublefuckcumfastvideo behind doublefuckcumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckcumpovfastvideo
hide doublefuckcumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefuckmilffastx()
screen doublefuckmilffastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfPOVFastx") 

label DoubleFuckMilfPOVSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slowx = True
window hide
show doublefuckcumpovslowvideo behind doublefuckcumpovfastvideo
show doublefuckcumpovslowvideo behind doublefuckcumslowvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckcumpovfastvideo
hide doublefuckcumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefuckmilfpovslowx()
screen doublefuckmilfpovslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSlowx") 

label DoubleFuckMilfPOVFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
window hide
show doublefuckcumpovfastvideo behind doublefuckcumpovslowvideo
show doublefuckcumpovfastvideo behind doublefuckcumfastvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckcumpovslowvideo
hide doublefuckcumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefuckmilfpovfastx()
screen doublefuckmilfpovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfFastx")

label DoubleFuckSupSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slowx = True
if supdptalkcumfirstx == False and dpsupcamex >= 1:
    sg "You're fucking me again! In my already cum-filled pussy... Mmmh, this is so good!"
    mc "It's so slippery with my spunk now, I can pound away even deeper!"
    $ supdptalkcumfirstx = True
window hide
show doublefucksupcumslowvideo behind doublefucksupcumfastvideo
show doublefucksupcumslowvideo behind doublefucksupcumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovslowvideo
hide doublefucksupcumfastvideo
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucksupslowx()
screen doublefucksupslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlowx") 

label DoubleFuckSupFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
window hide
show doublefucksupcumfastvideo behind doublefucksupcumslowvideo
show doublefucksupcumfastvideo behind doublefucksupcumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovfastvideo
hide doublefucksupcumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucksupfastx()
screen doublefucksupfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupPOVFastx") 

label DoubleFuckSupPOVSlowx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slowx = True
window hide
show doublefucksupcumpovslowvideo behind doublefucksupcumpovfastvideo
show doublefucksupcumpovslowvideo behind doublefucksupcumslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovfastvideo
hide doublefucksupcumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucksuppovslowx()
screen doublefucksuppovslowx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSwitchx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSlowx") 

label DoubleFuckSupPOVFastx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
window hide
show doublefucksupcumpovfastvideo behind doublefucksupcumpovslowvideo
show doublefucksupcumpovfastvideo behind doublefucksupcumfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovslowvideo
hide doublefucksupcumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucksuppovfastx()
screen doublefucksuppovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupFastx")

label DoubleFuckSupSwitchx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupcumslowvideo
if talkedswitchsupcumx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    if dpmilfcamex <= 1:
        cm "As long as you give me another BIG load, sweetie pie!"
    if dpmilfcamex >= 2:
        cm "Alright-ee, sweetie pie. You already gave your landlady so many MASSIVE cumloads!"
    $ talkedswitchsupcumx = True
window hide
show doublefuckmilfswitchcumvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupcumslowvideo behind doublefuckmilfswitchcumvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchcumvideo
hide doublefuckmilfswitchcumvideo
if supdptalkfirstx == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirstx = True
window hide
$ supdptalk01slowx = True
jump DoubleFuckSupSlowx

label DoubleFuckMilfSwitchx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckcumslowvideo
if talkedswitchmilfcumx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilfcumx = True
window hide
show doublefucksupswitchcumvideo
$ renpy.pause(0.6, hard='True')
show doublefuckcumslowvideo behind doublefucksupswitchcumvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchcumvideo
hide doublefucksupswitchcumvideo
$ milfdptalk01slowx = True
jump DoubleFuckMilfSlowx

label DoubleFuckMilfCumx:
$ milfdptalk01slowx = True
$ dpmilfcamex += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "Gonna cum again, Captain MILF, I can feel it!"
cm "Then pump your seed inside me and all over my back [name]!"
scene dpmilfcum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene dpmilfcum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene dpmilfcum03 with dissolve
stop channel1
mc "There you go, Captain MILF, RHOOO!"
window hide
with fastflash
sg "He's really cumming like a STALLION!"
scene dpmilfcum04 with dissolve
mc "Still more shots BLASTING, RHAAA!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndx
scene dpmilfcum05 with dissolve
mc "Getting back in that tight snatch of yours, Captain MILF!"
cm "Damn, you're STILL raring to go? How are we going to TAME your BEAST?"
stop channel2
jump DoubleFuckMilfSlowx

label DoubleFuckSupCumx:
$ supdptalk01slowx = True
$ dpsupcamex += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
sg "Your cock... It's becoming even BIGGER inside my pussy!"
mc "That's cos I'm about to blow another load!"
scene dpsupcum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boymoan05.mp3" 
mc "AAAAH!"
window hide
with hpunch
sg "You're pumping so much spunk inside me, aaah!"
scene dpsupcum02 with dissolve
play sound "sounds/boymoan04.mp3" 
mc "There's more where that came from, RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
if dpsupcamex == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcamex >= 1:
    sg "I'm getting BLOATED again by your MONSTER LOAD, you just cum like a FIREHOSE!"
scene dpsupcum03 with dissolve
play sound "sounds/boymoan03.mp3" 
mc "Endless supplies of young, virile cum from THIS Super-Stud!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
sg "Don't stop, keep cumming, AAAH, I'm gonna squirt!"
window hide
with fastflash
mc "There you go, the last few shots just for you, Supergirl!"
window hide
with fastflash
stop channel2
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndx
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcamex == 0:
    jump DoubleFuckNoSupSlowx
jump DoubleFuckSupSlowx

label DoubleFuckEndx:
stop channel2
play sound "sounds/panting.mp3"
scene doublefuckend01 with dissolve
mc "That's it, I think you girls finally drained me... After I came over 5 MEGA-LOADS..."
if age >= 18:
    sg "I still can't believe a man can cum so many times in a row and never lose his hardon... Uuuhhhh...."
scene doublefuckend02 with dissolve
cm "Your landlady is very proud of you, [name]. You've definitely MASTERED Level02 Super-Studliness! * slurp *"
scene doublefuckend03 with dissolve
play sound "sounds/moan03.mp3"
sg "My pussy is so full of warm cream... Mmhhh..."
scene doublefuckend02 with dissolve
cm "Now I'd better go back to my room and clean up before some Super-Villains attack the compound."
scene doublefuckend04 with dissolve
mc "With my new BIGGER muscles, I could defeat anyone that dares set foot in our compound, Captain MILF!"
cm "Yeah, I know, you're VERY muscular my young tenant... But you're still only Super-Strength level 02. Superman is less muscular than you but he's STRONGER..."
mc "Pff! I'll become STRONGER than this wimp in no time, mark my words!"
scene doublefuckend05 with dissolve
sg "What's going on? My body... It's getting smaller! NOOOOOO!"
scene doublefuckend06 with dissolve
cm "Did you press ctrl+alt+Shift+F8 before hitting Enter?"
sg "Ctrl+alt+WHAT???"
cm "Ctrl+alt+Shift+F8. It's required to make the radiation-induced body enhancements permanent. You must have forgotten to press it, thanks God."
cm "Now you'll become the sweet little girl I've always known you as again."
scene doublefuckend07 with dissolve
sg "But I DON'T WANT TO! * sob *"
mc "Look on the bright side. Your costume will fit you again and you can fly back to Smallville without the hassle of finding a new one."
sg "I HATE YOU! GO BACK TO THE GALLERY"
stop channel2
stop channel1
stop music
jump MILFGallery

label MILFGallery08:
stop channel3
$ milflonetalk01slowx = False
$ milflonetalk01fastx = False
$ milflonetalkfirstx = False
play music "sounds/sexy04.mp3"
scene milfmassage01 with fade
voice "milf/room20"
cm "Where would you like me to go, sweetie pie?"
mc "You can just lie on the bed, Captain MILF."
scene milfmassage02 with dissolve
voice "milf/room21"
cm "And what kind of \"massage\" did you have in mind exactly?"
mc "I was thinking... Swedish."
scene milfmassage03 with dissolve
voice "milf/room22"
cm "Isn't that a bit naughty for a tenant to give to his old landlady?"
mc "Well, err... I already gave you one, remember?"
scene milfmassage04 with dissolve
voice "milf/room23"
cm "Ah yes, that's true, you ended up pounding me with your great big enhanced whopper. So I have to get naked then."
mc "Correctomundo!"
scene milfmassage05 with dissolve
voice "milf/room24"
cm "And YOU have to get naked too, my sweet tenant... Maybe I could help you achieve a hardon faster..."
mc "You certainly could, Carol! It's already starting to work!"
scene milfmassage06 with dissolve
voice "milf/room25"
cm "So soon? Does your landlady make you THAT horny, [name]?"
mc "Damn right she is!"
scene mcroomsex15 with dissolve
voice "milf/room26"
cm "But before that, I need to make sure I'm REALLY wet down there. Your level 02 dong is just so... HUGE now!"
scene mcroomsex16 with dissolve
play sound "sounds/moan04.ogg"
voice "milf/room27"
cm "Mmh, my pussy feels so tender..."
scene mcroomsex17 with dissolve
play sound "sounds/moan06.ogg"
mc "Yeah, you got yourself off, Carol!"
scene mcroomsex05 with dissolve
voice "milf/room28"
cm "Now I'm ready to lie down so you can start off with your SENSUOUS massage. Before FUCKING your landlady with your GIGANTIC pussy-wrecker!"
mc "Alright!"
scene mcroomsex06 with dissolve
voice "milf/room29"
cm "And I'm looking the other way so I don't see your huge... thingie and faint in admiration."
mc "I'll try and keep it out of the way for the moment..."
scene mcroomsex07 with dissolve
play sound "sounds/moan03.mp3"
voice "milf/room30"
cm "Mmh, that's nice, sweetie pie..."
scene mcroomsex08 with dissolve
mc "Your buns are just so... amazingly tight, Captain MILF!"
voice "milf/room31"
cm "I can crush a walnut between my cheeks, [name]."
mc "Right, err... You'll have to show me that one day."
scene mcroomsex09 with dissolve
mc "In the meantime..."
play sound "sounds/moan02.mp3"
voice "milf/room32"
cm "Oooh, what are you doing, naughty boy?"
mc "Massaging the INSIDE of your snatch. It needs to dilate quite a bit, considering the size of my level 02 Super-Dong..."
voice "milf/room33"
cm "Mmmh, my machine really did work, didn't it..."
mc "It sure did, Carol."
scene mcroomsex10 with dissolve
play sound "sounds/moan01.mp3"
voice "milf/room34"
cm "That was VERY good, my sweet young tenant... Now it is MY turn to show my appreciation."
scene mcroomsex11b with dissolve
play sound "sounds/gasp.mp3"
voice "milf/room35"
cm "Oh my dear Lord! Look at that GIANT boymeat you're sporting, sweetie pie!"
mc "Yes, and I'm so hard, it's literally aching!"
scene mcroomsex12 with dissolve
voice "milf/room36"
cm "Then I need to do something about it, don't I?"
mc "Ooh yeah!"
scene mcroomsex13 with dissolve
voice "milf/room37"
cm "Show me again how you please a woman with that giant pecker!"
mc "Oh God, this is about to get real HOT!"
scene mcroomsex18 with dissolve
mc "Fuck, I'm just so fucking HUGE for you!"
voice "milf/room38"
cm "I can't even watch, I fear I might faint seeing your behemoth plowing through my love canal..."
scene mcroomsex19a with dissolve
play sound "sounds/thud.mp3"
mc "Can you feel how HEAVY it is, Carol?"
play channel2 "sounds/moan02.mp3"
window hide
scene mcroomsex19b with dissolve
$ renpy.pause(.8, hard='True')
play channel1 [ "sounds/thud.mp3", "<silence .8>"]
scene milfcockslap
pause
voice "milf/room39"
cm "Oh God... It's the BIGGEST piece of [age]yo manmeat on Earth, sweetie pie! Just Give it to me, I WANT IT!"
stop channel1
stop channel2
scene mcroomsex20 with dissolve
play sound "sounds/moan06.ogg"
mc "I'll make you cum in no time with my Super-Cock!"
$ milfmassagetalkslowx = True

label MILFloneMassageSlowx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
window hide
show milfmassageslowvideo behind milfmassagepovslowvideo
show milfmassageslowvideo behind milfmassagefastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovslowvideo
hide milfmassagefastvideo
with dissolve

show faster:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milflonemassageslowx()
screen milflonemassageslowx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFloneMassageFastx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFloneMassagePOVSlowx")

label MILFloneMassageFastx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    voice "milf/room40"
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
window hide
show milfmassagefastvideo behind milfmassagepovfastvideo
show milfmassagefastvideo behind milfmassageslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovfastvideo
hide milfmassageslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milflonemassagefastx()
screen milflonemassagefastx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFloneMassageSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEndx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFloneMassagePOVFastx")

label MILFloneMassagePOVSlowx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
window hide
show milfmassagepovslowvideo behind milfmassageslowvideo
show milfmassagepovslowvideo behind milfmassagepovfastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassageslowvideo
hide milfmassagepovfastvideo
with dissolve
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milflonemassagepovslowx()
screen milflonemassagepovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFloneMassagePOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFloneMassageSlowx")

label MILFloneMassagePOVFastx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    voice "milf/room40"
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
window hide
show milfmassagepovfastvideo behind milfmassagefastvideo
show milfmassagepovfastvideo behind milfmassagepovslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagefastvideo
hide milfmassagepovslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milflonemassagepovfastx()
screen milflonemassagepovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFloneMassagePOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFloneMassageFastx")

label MILFloneMassageEndx:
hide cum
hide faster
hide slower
hide pov
hide sceneicon
play sound "sounds/moan05.mp3"
voice "milf/room41"
cm "Sweetie, I... PLEASE CUM INSIDE ME, YOU STALLION!"
mc "Sure Carol, I'm right on the edge and..."
stop channel2
scene mcroomsex21 with dissolve
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boyorgasm01.mp3"
mc "...AAAAH! Here it comes!"
window hide
with fastflash
mc "And it feels so fucking good!"
scene mcroomsex22 with dissolve
voice "milf/room42"
cm "Oh dear me, is that still the same shot? You've been pumping your seed for so long already, sweetie pie!"
window hide
with hpunch
mc "Oh Fuck, can't stop NU-UU-TTING!!"
scene mcroomsex23 with dissolve
voice "milf/room43"
cm "Maybe you should dump the rest on me, I'm starting to feel a bit... bloated with young spunk!"
window hide
with fastflash
mc "Oh damn, alright, gonna try and pull it out while I'm still spewing my sauce, RHAAAA!"
scene mcroomsex24 with dissolve
stop channel2
if age >= 20:
    voice "milf/room44a"
    cm "Oh my goodness, you're splattering your potent goo all over my body!"
if age >= 18 and age <= 19:
    voice "milf/room44b"
    cm "Oh my goodness, you're splattering your potent teenage goo all over my body!"
window hide
with fastflash
voice "milf/room45"
cm "Give me more [name], DROWN YOUR FILTHY LANDLADY IN YOUR SWEET CUM!"
scene mcroomsex25 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE YOU GO, AAAHHH!"
window hide
with fastflash
voice "milf/room46"
cm "You're blasting so FURIOUSLY for your landlady, you dirty tenant!"
scene mcroomsex26 with dissolve
play sound "sounds/panting.mp3"
play channel2 "sounds/splooge02.mp3"
voice "milf/room47"
cm "You came so much inside me, sweetie pie... Oooh..."
mc "Damn, I can see that..."
scene mcroomsex40 with dissolve
play sound "sounds/slurp.mp3"
voice "milf/room48"
cm "Let me slurp as much as I can of your sweet young nectar..."
mc "There's a LOT of cum to slurp up, Carol. And I'm still HARD for you!"
scene mcroomsex41 with dissolve
stop channel2
voice "milf/room49"
cm "Mmh, then why don't you come and sit on the bed so I can take care of your massive erection..."
scene mcroomsex42 with dissolve
voice "milf/room50"
cm "I'm totally under the spell of your giant [age]yo dong right now..."
mc "That's great but my hard-on is demanding attention, Captain MILF!"
voice "milf/room51"
cm "Then I guess I'll have to lick it and taste its manly musk."
scene mommassagelickvideo with dissolve
$ renpy.pause(1.0, hard='True')
mc "Fuck Carol, your tongue... I'm in heavens!"
pause
scene mcroomsex43 with dissolve
voice "milf/room52"
cm "I just want to care of you and your needs, like a good landlady."
mc "You're the best landlady ever!"
scene mcroomsex44 with dissolve
voice "milf/room53"
cm "And I'll prove it to you, [name]. By letting you fuck me until your balls are DRAINED! Let me get on the bed for you."
scene mcroomsex45 with dissolve
mc "Are you ready to receive my mighty love muscle, Captain MILF?"
voice "milf/room54"
cm "Yes, sweetie pie. I'm going to make you cum so many times that it will finally go down and I won't be under its gorgeous spell..."
scene mcroomsex45 with dissolve
play sound "sounds/moan05.mp3"
voice "milf/room55"
cm "OOOH! I can already feel your apple-sized helmet STRETCHING my pussylips... Be careful with that thing, [name]!"
$ milflonetalk01slowx = True

label MILFLoneNoMilfSlowx:
$ milflonetalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slowx == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slowx = True
window hide
show milfloneslowvideo behind milflonefastvideo
show milfloneslowvideo behind milfloneslowpovvideo
$ renpy.pause(1.0, hard='True')
hide milfloneslowpovvideo
hide milflonefastvideo
stop channel2
play channel2 "sounds/womansex03.mp3"
if milflonetalkfirstx == False:
    if age >= 20:
        voice "milf/room57a"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        voice "milf/room57b"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milflonetalkfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500  
call screen milflonenomilfslowx()
screen milflonenomilfslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVSlowx") 

label MILFLoneNoMilfFastx:
$ milflonetalk01slowx = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fastx == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fastx = True
window hide
show milflonefastvideo behind milfloneslowvideo
show milflonefastvideo behind milflonefastpovvideo
$ renpy.pause(1.0, hard='True')
hide milflonefastpovvideo
hide milfloneslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonenomilffastx()
screen milflonenomilffastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfPOVFastx") 

label MILFLoneNoMilfPOVSlowx:
$ milflonetalk01fastx = False
stop channel2
play channel2 "sounds/womansex03.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slowx == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slowx = True
window hide
show milfloneslowpovvideo behind milflonefastpovvideo
show milfloneslowpovvideo behind milfloneslowvideo
$ renpy.pause(1.0, hard='True')    
hide milflonefastpovvideo
hide milfloneslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500   
call screen milflonenomilfpovslowx()
screen milflonenomilfpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfSlowx") 

label MILFLoneNoMilfPOVFastx:
$ milflonetalk01slowx = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fast == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fast = True
window hide
show milflonefastpovvideo behind milfloneslowpovvideo
show milflonefastpovvideo behind milflonefastvideo
$ renpy.pause(1.0, hard='True')    
hide milfloneslowpovvideo
hide milflonefastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonenomilfpovfastx()
screen milflonenomilfpovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfFastx") 
        
label MILFLoneNoMilfCumx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
$ milflonetalk01slowx = True
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "I feel like I'm ready to blow a load, Carol!"
voice "milf/room59"
cm "Then pump your seed inside your landlady!"
scene milflonenocum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
voice "milf/room60"
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene milflonenocum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
voice "milf/room61"
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene milflonenocum03 with dissolve
stop channel1
mc "There you go, Catain MILF, RHOOO!"
window hide
with fastflash
voice "milf/room62"
cm "You're really cumming like a STALLION!"
window hide
with fastflash
mc "Still more shots BLASTING, RHAAA!"
play sound "sounds/moan05.mp3"
window hide
with fastflash
voice "milf/room63"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
scene milflonecum04 with dissolve
stop channel2
mc "Getting back in that tight snatch of yours, Carol!"
voice "milf/room64"
cm "Damn, you're still raring to go! How am I going to TAME your manly BEAST?"
jump MilfCameSlowx   

label MilfCameSlowx:
$ milflonetalkfirstx = False
$ milflonetalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slowx == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slowx = True
window hide
show milflonecumslowvideo behind milflonecumfastvideo
show milflonecumslowvideo behind milflonecumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide milflonecumpovslowvideo
hide milflonecumfastvideo
stop channel2
play channel2 "sounds/womansex03.mp3"
if milflonetalkfirstx == False:
    if age >= 20:
        voice "milf/room57a"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        voice "milf/room57b"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milflonetalkfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500  
call screen milflonecumnomilfslowx()
screen milflonecumnomilfslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCameFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVSlowx") 

label MilfCameFastx:
$ milflonetalk01slowx = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fastx == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fastx = True
window hide
show milflonecumfastvideo behind milflonecumslowvideo
show milflonecumfastvideo behind milflonecumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide milflonecumpovfastvideo
hide milflonecumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonecumnomilffastx()
screen milflonecumnomilffastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MilfCameCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCameSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCamePOVFastx") 

label MilfCamePOVSlowx:
$ milflonetalk01fastx = False
stop channel2
play channel2 "sounds/womansex03.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slowx == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slowx = True
window hide
show milflonecumpovslowvideo behind milflonecumpovfastvideo
show milflonecumpovslowvideo behind milflonecumslowvideo
$ renpy.pause(1.0, hard='True')    
hide milflonecumpovfastvideo
hide milflonecumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500   
call screen milflonecumnomilfpovslowx()
screen milflonecumnomilfpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVFastx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCameSlowx") 

label MilfCamePOVFastx:
$ milflonetalk01slowx = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fastx == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fastx = True
window hide
show milflonecumpovfastvideo behind milflonecumpovslowvideo
show milflonecumpovfastvideo behind milflonecumfastvideo
$ renpy.pause(1.0, hard='True')    
hide milflonecumpovslowvideo
hide milflonecumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonecumnomilfpovfastx()
screen milflonecumnomilfpovfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MilfCameCumx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVSlowx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCameFastx") 
        
label MilfCameCumx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
play sound "sounds/boymoan02.mp3"
mc "Gonna cum again, Captain MILF, I can feel it!"
voice "milf/room65"
cm "Then pump your sweet boyseed inside me and all over my back again!"
scene milflonecum01 with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge01.mp3"
mc "FLOODING YOUR SNATCH AGAIN, RHAAAA!"
window hide
with hpunch
voice "milf/room66"
cm "I can feel it [name], you're pumping all that sweet young cum inside me, you're such a good boy!"
scene milflonecum02 with dissolve
mc "Her's more for you, DEEP INSIDE, AAAH!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
voice "milf/room67"
cm "I'm coming too, your giant horsedick is sssooo virile!"
scene milflonecum03 with dissolve
stop channel1
mc "I'll add some more to your already spunk-covered back, FU-UUU-CK!"
window hide
with fastflash
voice "milf/room68"
cm "You shouldn't swear when you're blasting your spunk all over your horny landlady's body, my sweet tenant!"
window hide
with fastflash
mc "Sorry Carol, just can't stop NUTTING!"
stop channel2
play sound "sounds/panting.mp3"
scene milflonecumend01 with dissolve
mc "That's it, I think you finally drained me... After I came 3 MEGA-LOADS..."
scene milflonecumend02 with dissolve
play sound "sounds/moan03.mp3"
voice "milf/room69"
cm "I'm very proud of you, [name]. You've definitely MASTERED Level02 Super-Studliness! * slurp *"
scene milflonecumend03 with dissolve
stop sound
voice "milf/room70"
cm "Now I'd better go back to my room and clean up before some Super-Villains attack the compound."
mc "With my new BIGGER muscles, I could defeat anyone that dares set foot in our compound, Captain MILF!"
voice "milf/room71"
cm "Yeah, I know, you're VERY muscular my young sweet boy... But you're still only Super-Strength level 02. Superman is less muscular than you but he's STRONGER..."
mc "Pff! I'll become STRONGER than this wimp in no time, mark my words!"
$ dpmilfcamex = 0
$ dpsupcamex = 0
stop music
jump MILFGallery

label MILFGallery09:
stop channel3
stop channel1
stop music
scene gymmcprecurl02 with dissolve
mc "That's it. Ready to RUMBLE!"
window hide
play channel2 "sounds/effort01.mp3"
show gymmccurlvideo with dissolve
pause
mc "Fuck yeah! Chest-pressing over 20 TONS! A few more reps..."
window hide
pause
stop channel2
scene gymmcpostcurl01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
mc "Wow, look at those damn MASSIVE biceps! Need to pose and admire my hot muscled body like a total narcisssist pronto!"
$ d3rollgymworkoutx = renpy.random.randint(1, 3)
if d3rollgymworkoutx == 1:
    scene gymmcpost04 with dissolve
    mc "That was a nice workout... I feel like my biceps have really GROWN even MORE..."
if d3rollgymworkoutx == 2:
    scene gymmcpost05 with dissolve
    mc "Grrr! I could scare away any enemy with THOSE muscles now!"
if d3rollgymworkoutx == 3:
    scene gymmcpost06 with dissolve
    if age >= 20:
        mc "Damn! Check those biceps, monster muscle STUD right there!"
    if age >= 18 and age <= 19:
        mc "Damn! Check those biceps, monster teenage muscle STUD right there!"

play music "sounds/sexy03.mp3"
scene gymmcmilflevel01 with dissolve
cm "Ooh, my landboy is getting so BIG!" 
mc "Err, Captain MILF?"
scene gymmcmilflevel02 with dissolve
cm "I also finished my gym session and was feeling like POSING in front of the mirror too!" 
mc "So maybe we should do it together? Like, some superhero COUPLE facing the most DASTARDLY Super-Villains."
scene gymmcmilflevel03 with dissolve
cm "Why not, I like your way of thinking. Let's make sure they can sense their imminent DOOM!"
mc "I'll talk them down until they SUBMIT to the Cockham League of Justice! Watch me."
scene gymmcmilflevel04 with dissolve
mc "Are you talking to me? Are YOU talking to ME?"
cm "Look at them, I can read the FEAR on their faces... Get on your knees in front of me, please [name], I want to see us like that..."
scene gymmcmilflevel05 with dissolve
cm "Mmmh, yes, you look so MENACING, even though you're crouching, we're definitely the PERFECT superhero couple!"
scene gymmcmilflevel06 with dissolve
mc "So if we are a perfect couple, we should hold each other tight."
scene gymmcmilflevel07 with dissolve
cm "But, what are you doing, [name]? I'm... your League Captain, this is..."
scene gymmcmilflevel08 with dissolve
mc "Please Carol, you can't leave me like this, my cock... It's getting HARD!"
scene gymmcmilflevel09 with dissolve
play sound "sounds/ripping.mp3"
if age >= 20:
    cm "Oh dear, I can see that, it's getting so BIG too! You've got take it out of your thong or you'll RIP it apart! Bring that giant fuckstick over here, I want to FEEL it!"
if age >= 18 and age <= 19:
    cm "Oh dear, I can see that, it's getting so BIG too! You've got take it out of your thong or you'll RIP it apart! Bring that giant teen fuckstick over here, I want to FEEL it!"
scene gymmcmilflevel10 with dissolve
cm "It's so BIG... You keep GROWING and GROWING, like a true SEX Superhero!"
mc "Please let me take your bottom off now, Carol, I'm dying to CUM inside you again!"
cm "Right here, where everyone could see us if they walked in? I... can't allow this. But stick it between my legs and pretend you're fucking my wet snatch..."
scene gymmcmilflevel11 with dissolve
play sound "sounds/moan01.mp3"
mc "At least help me get your top off, Carol..."
cm "Fine, just this once..."
scene gymmcmilflevel12 with dissolve
mc "You have the best titties of the whole League, captain MILF!"
cm "What a charmer! Are you ready now? You'll see, the feel of the lycra rubbing against your hard dong will send ELECTRIC shockwaves down your shaft all the way to your balls!"
play channel2 "sounds/wetmassage.mp3"
$ milfwankgymtalkslowx = False

label MilfGymWankSlowx:
play channel1 "sounds/moan02.mp3"
$ milfwankgymtalkfastx = False
window hide
hide nexticon
hide faster
hide slower
hide front
hide sceneicon
show milfwankgymslowvideo behind milfwankgymfrontslowvideo
show milfwankgymslowvideo behind milfwankgymfastvideo
$ renpy.pause(1.0, hard='True')
hide milfwankgymfrontslowvideo
hide milfwankgymfastvideo
with dissolve
if milfwankgymtalkslowx == False:
    if age >= 20:
        cm "Look at that huge monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
    if age >= 18 and age <= 19:
        cm "Look at that huge teenage monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
    $ milfwankgymtalkslowx = True
window hide

show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfwankgymslowx()
screen milfwankgymslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymWankFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfGymWankFrontSlowx")

label MilfGymWankFastx:
play channel1 "sounds/moan03.mp3"
$ milfwankgymtalkslowx = False
window hide
hide nexticon
hide faster
hide slower
hide front
hide sceneicon
if milfwankgymtalkfastx == False:
    mc "I'm gonna slide my shaft between those legs faster now, Captain MILF!"
    cm "Oooh God, it's gonna be so HOT!"
    $ milfwankgymtalkfastx = True
window hide
show milfwankgymfastvideo behind milfwankgymfrontfastvideo
show milfwankgymfastvideo behind milfwankgymslowvideo
$ renpy.pause(1.0, hard='True')
hide milfwankgymfrontfastvideo
hide milfwankgymslowvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfwankgymfastx()
screen milfwankgymfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymWankSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymWankEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfGymWankFrontFastx")

label MilfGymWankFrontSlowx:
play channel1 "sounds/moan02.mp3"
$ milfwankgymtalkfastx = False
window hide
hide nexticon
hide faster
hide slower
hide front
hide sceneicon
show milfwankgymfrontslowvideo behind milfwankgymslowvideo
show milfwankgymfrontslowvideo behind milfwankgymfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfwankgymslowvideo
hide milfwankgymfrontfastvideo
with dissolve
if milfwankgymtalkslowx == False:
    if age >= 20:
        cm "Look at that huge monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
    if age >= 18 and age <= 19:
        cm "Look at that huge teenage monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
    $ milfwankgymtalkslowx = True
window hide

show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfwankgymfrontslowx()
screen milfwankgymfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymWankFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymWankEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MilfGymWankSlowx")

label MilfGymWankFrontFastx:
play channel1 "sounds/moan03.mp3"
$ milfwankgymtalkslowx = False
window hide
hide nexticon
hide faster
hide slower
hide front
hide sceneicon
if milfwankgymtalkfastx == False:
    mc "I'm gonna slide my shaft between those legs faster now, Captain MILF!"
    cm "Oooh God, it's gonna be so HOT!"
    $ milfwankgymtalkfastx = True
window hide
show milfwankgymfrontfastvideo behind milfwankgymfastvideo
show milfwankgymfrontfastvideo behind milfwankgymfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfwankgymfastvideo
hide milfwankgymfrontslowvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfwankgymfrontfastx()
screen milfwankgymfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymWankFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymWankEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MilfGymWankFastx")

label MilfGymWankEndx:
hide nexticon
hide faster
hide slower
hide front
hide sceneicon
stop channel1
mc "Why don't you grab it with your hands and slowly wank me off, Captain MILF? YOu know you want to..."
cm "Oooh, you're such a naughty landboy... But you're right, I can't help myself, I want to just hold this beautiful piece of boymeat in my hands!"
play sound "sounds/moan01.mp3"
scene milfwankhold01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
cm "Sssoo huge.. So STURDY..."
stop channel2
play channel2 "sounds/wank.mp3"
$ milfhjgymtalkslowx = False

label MilfGymHandjobSlowx:
play channel1 "sounds/womansex06.mp3"
$ milfhjgymtalkfastx = False
window hide
hide cum
hide faster
hide slower
hide front
hide sceneicon
if milfhjgymtalkslowx == False:
    cm "It's like I have my own huge futa cock!"
    $ milfhjgymtalkslowx = True
window hide
show milfhjgymslowvideo behind milfhjgymfrontslowvideo
show milfhjgymslowvideo behind milfhjgymfastvideo
$ renpy.pause(1.0, hard='True')
hide milfhjgymfrontslowvideo
hide milfhjgymfastvideo
with dissolve

show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfhjgymslowx()
screen milfhjgymslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymHandjobFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfGymHandjobFrontSlowx")

label MilfGymHandjobFastx:
play channel1 "sounds/womansex02.mp3"
$ milfhjgymtalkslowx = False
window hide
hide cum
hide faster
hide slower
hide front
hide sceneicon
if milfhjgymtalkfastx == False:
    mc "Do it faster, I'm right on the edge, ready to BLAST OFF for you!"
    $ milfhjgymtalkfastx = True
window hide
show milfhjgymfastvideo behind milfhjgymfrontfastvideo
show milfhjgymfastvideo behind milfhjgymslowvideo
$ renpy.pause(1.0, hard='True')
hide milfhjgymfrontfastvideo
hide milfhjgymslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfhjgymfastx()
screen milfhjgymfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymHandjobSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymHandjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfGymHandjobFrontFastx")

label MilfGymHandjobFrontSlowx:
play channel1 "sounds/womansex06.mp3"
$ milfhjgymtalkfastx = False
window hide
hide cum
hide faster
hide slower
hide front
hide sceneicon
if milfhjgymtalkslowx == False:
    cm "It's like I have my own huge futa cock!"
    $ milfhjgymtalkslowx = True
window hide
show milfhjgymfrontslowvideo behind milfhjgymslowvideo
show milfhjgymfrontslowvideo behind milfhjgymfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfhjgymslowvideo
hide milfhjgymfrontfastvideo
with dissolve
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfhjgymfrontslowx()
screen milfhjgymfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymHandjobFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymHandjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MilfGymHandjobSlowx")

label MilfGymHandjobFrontFastx:
play channel1 "sounds/womansex02.mp3"
$ milfhjgymtalkslowx = False
window hide
hide cum
hide faster
hide slower
hide front
hide sceneicon
if milfhjgymtalkfastx == False:
    mc "Do it faster, I'm right on the edge, ready to BLAST OFF for you!"
    $ milfhjgymtalkfastx = True
window hide
show milfhjgymfrontfastvideo behind milfhjgymfastvideo
show milfhjgymfrontfastvideo behind milfhjgymfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfhjgymfastvideo
hide milfhjgymfrontslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfhjgymfrontfastx()
screen milfhjgymfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfGymHandjobFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfGymHandjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MilfGymHandjobFastx")

label MilfGymHandjobEndx:
hide cum
hide faster
hide slower
hide front
hide sceneicon
mc "I'm gonna come, Carol!"
scene milfholdcum01 with dissolve
play sound "sounds/boyorgasm01.mp3"
stop channel2
cm "No, I'm coming, not YOU, AAAH!"
window hide
with fastflash
cm "I've got so much pent-up cum to discharge, I wanna cum and cum and cum!"
scene milfholdcum02 with dissolve
play sound "sounds/boymoan05.mp3"
mc "Ooooh, AAAAH!"
window hide
with hpunch
stop channel1
play sound "sounds/moan02.mp3"
cm "Mmmh, look at how much MY cock is spewing, it's flying just EVERYWHERE!"
scene milfholdcum03 with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
cm "Sssooo, ssooo much CUM! I want to keep BLASTING! I NEED to, you hear me, [name]?"
window hide
with fastflash
mc "I... RHAAAA!"
scene milfholdcum04 with dissolve
cm "Yes, hold your landlady's milkbags while she holds her HUGE convulsing MEGADONG!"
window hide
with hpunch
cm "My cock is just on FULL BLAST, isn't it?"
scene milfholdcum05 with dissolve
cm "OOoh, I'm still got some MORE, more YUMMY CREAM to pump out of this monster!"
window hide
with fastflash
mc "Oh God... AAAH!"
scene milfholdcum06 with dissolve
cm "And it's so tasty too? Do you want to taste some of MY cream, [hero]?"
window hide
with vpunch
mc "Ggggg..."
cm "I seem to be have drained myself GOOD. * wink *"
scene milfholdcum07 with dissolve
stop channel2
play sound "sounds/panting.mp3"
cm "I came so MUCH, I guess I'm gonna need to ask Consuela to come and clean the gym again..."
mc "* pant * I didn't even know we had a cleaning lady..."
stop music
jump MILFGallery

label MILFGallery10:
stop channel3
stop music
play music "sounds/sexy01.mp3"
scene milfpoolresistance01 with dissolve
cm "You'll have to get totally NAKED for this resistance test. And please try not to get a hardon in front of your League Captain..."
mc "Not a problem. I'm good at getting naked."
scene milfpoolresistance02 with dissolve
cm "I will of course wear a towel so you don't get all excited from watching my Super-MILF figure..."
mc "* Damn it! *"
cm "Now I'm going to turn the sauna heat to MAXIMUM LEVEL."
scene milfpoolresistance03 with dissolve
cm "Just relax. And make sure that dong of yours is also totally RELAXED, understood?"
mc "Yes, Captain MILF..."
scene milfpoolresistance04 with dissolve
cm "How are you feeling?"
mc "Its getting...  HOT! Like. SUPER-HOT!"
cm "You're sweating, that's good. Super-Resistance is about controlling your BODY to withstand extreme temperatures."
scene milfpoolresistance05 with dissolve
cm "So focus on that. Focus on using your skin surface to let the heat OUT of your..."
scene milfpoolresistance06 with dissolve
cm "* Oh no, I think my tenant is getting hard... He's so SEXY looking like this with his massive... *"
scene milfpoolresistance07 with dissolve
cm "* ... YOUNG HORSECOCK and HUGE MUSCLES! *"
scene milfpoolresistance08 with dissolve
mc "Uh oh! The extreme heat made me SUPER-HARD! I didn't mean to, I swear Captain MILF!"
scene milfpoolresistance09 with dissolve
cm "Your cock... Your GIANT [age]yo MONSTERDICK!..."
mc "Are you alright, Carol?"
scene milfpoolresistance10 with dissolve
cm "No! My Super-Resistance is... failing me because of your MASSIVE erection!"
mc "It's getting ... so HOT!"
scene milfpoolresistance11 with dissolve
mc "Must... RESIST!"
scene milfpoolresistance12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
mc "AAAH! The extreme HEAT is lifting my body in the air and tearing at my skin!"
cm "My skin is... BURNING!"
mc "I need to use my cock skin surface to let the HEAT out and save Captain MILF before it's too late!"
scene milfpoolresistance13 with dissolve
mc "Focus, FOCUS!"
play sound "sounds/mangrunt01.mp3"
mc "It's working! I can feel the heat escaping through my dong!"
scene milfpoolresistance14 with dissolve
cm "Hurry up, my skin..."
mc "I'll turn the heat down now, Captain MILF, hang in there!"
scene milfpoolresistance15 with dissolve
mc "Damn, it's not enough, there's too much steam inside the sauna cabin. I need to break this strong glass window!"
scene milfpoolresistance16 with dissolve
play sound "sounds/brokenglass.mp3"
mc "Fortunately, I'm SUPER-STRONG!" 
scene milfpoolresistance17 with dissolve
mc "I'll get you out of this steaming sauna, Captain MILF!"
scene milfpoolresistance18 with dissolve
cm "I'm feeling... BETTER. My Super-Resistance is back up and running! I hope my breasts weren't too damaged..."
scene milfpoolresistance19 with dissolve
mc "Let me check that for you..."
play sound "sounds/kiss.mp3"
cm "Oooh, what are you doing, naughty boy?"
scene milfpoolresistance20 with dissolve
play sound "sounds/moan04.ogg"
mc "Just checking that everything is functional..."
scene milfpoolresistance21 with dissolve
play sound "sounds/kiss.mp3"
cm "And?..."
mc "It all seems to be, Captain MILF..."
cm "You're making me so horny, I need to go back to my gallery and REALLY cool down..."
stop music
jump MILFGallery

label MILFGallery11:
stop channel3
stop music
play music "sounds/sexy14.mp3"
scene compoundmilfnightseduction02
show milfnewlingerie01
with dissolve
if renpy.seen_image("milfoilpussycum05"):
    cm "Hello sweetie pie... You're back to visit your VERY grateful landlady... For a HOT HAREM SEX NIGHT!"
    mc "Precisely, Carol!"
    hide milfnewlingerie01
    show milfnewlingerie05:
        zoom 0.5 xpos 0.2
    with dissolve
    cm "Well, let's start off our very special night with some LANDLADY-TENANT ANAL SEX, shall we?"
    mc "That sounds perfectly appropriate indeed."
    jump NewMILFAnalx
cm "Hello sweetie pie... You're back to visit your grateful landlady... in the evening..."
mc "That's right, there are still rewards I haven't received..."
hide milfnewlingerie01
show milfnewlingerie05:
    zoom 0.5 xpos 0.2
with dissolve
cm "In that case, you'd better choose what you want to do for our special  night time, [name]! Only rewards you already received are available in this gallery..."
menu:
    "I choose a nice sumptuous landlady titjob." if chosemilftitjob:
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "Oooh, you want my BIG tits wrapped around your HUGE cock, [name]? I can do that. Even better, I'm going to OIL myself up for it!"
        mc "Alright!"
        hide milfnewlingerie01
        show milfnewlingerie02
        with dissolve
        cm "Just stay put while I go to the bathroom and wait for me..."
        hide milfnewlingerie02 with moveoutright
        jump OilyMILFtitjobx
    "I want your lovely feet to make my rod convulse with orgasmic bliss." if chosemilffootjob:
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "Oooh, I didn't know you were a FOOT FETISHIST, [name]. I am too! And I'm going to OIL myself up to make it even more memorable for both of us!"
        hide milfnewlingerie01
        show milfnewlingerie02
        with dissolve
        cm "Just stay put while I go to the bathroom and wait for me..."
        hide milfnewlingerie02 with moveoutright
        jump OilyMILFfootjobx
    "I choose... ANAL SEX!" if chosemilfanal:
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "I knew you might... You just can't get enough of my booty, can you? Well, I'm ready to receive a mighty anal pounding from your giant pillar, [name]!"
        mc "Alright!"
        cm "Let me just get out of this frilly lingerie outfit first... Before I put a blindfold on, so I never get to see your immense lovesword...."
        jump NewMILFAnalx

label MilfSaunaRewardMenuCx:
scene compoundmilfnightseduction02
show milfoillingerie05 with dissolve
cm "So, what else would you like to do my sweet tenant?"
menu:
    "I choose a nice sumptuous landlady titjob.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Oooh, you want my BIG tits wrapped around your HUGE cock, [name]? I can do that. For my HAREM MASTER!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump OilyMILFtitjobBx
    "I want your feet to make my rod convulse with orgasmic bliss.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Oooh, you want my lovely little feet wrapped around your huge pole, my sweet tenant? Your landlady can do that!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump OilyMILFfootjobBx
    "I choose... ANAL SEX AGAIN!":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "I knew you might... You just can't get enough of my booty, can you? Well, I'm ready to receive a mighty anal pounding from your giant pillar, [name]!"
        mc "Alright!"
        jump NewMILFAnalBx
    "I choose... to have some intimate mating between my cock and your tight landlady pussy.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Vanilla vaginal sex? Why not. We've hardly ever tried that, and a normal landlady-landboy relationship should always include wholesome sex!"
        mc "Damn right! Stop the PERVERSION!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump NewMILFPussyx
    "I choose... to go back to the gallery.":
        jump MILFGallery
        
label OilyMILFtitjobx:
scene compoundmilfnightseduction02 blurred with fade
show milfoillingerie01 with moveinright
cm "Mmmh, I'm all oiled up for my horse-hung tenant..."
hide milfoillingerie01
show milfoillingerie02
with dissolve
if age >= 20:
    cm "Maybe you want to see a bit better the tits that will softly wrap around your mighty rod..."
if age >= 18 and age <= 19:
    cm "Maybe you want to see a bit better the tits that will softly wrap around your mighty teenage rod..."
mc "God, I'm gonna get hard..."
hide milfoillingerie02
show milfoillingerie03:
    xpos 0.2 zoom 0.5
with dissolve
cm "Not yet [name]! I can't actually {i}see{/i} your enormous fuckstick, remember?"
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.0
    ease 5.5 xpos 0.42 ypos 1.3           
show milfoillingerie03:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -1.0
    linear 6.0 xpos 0.1 ypos -0.2
with dissolve
$ renpy.pause(5.0, hard='True')
mc "But how are you supposed to give me that titjob reward without me getting HARD!!!"
scene compoundmilfnightseduction02 blurred
show milfoillingerie04:
    xpos 0.2 zoom 0.5
with dissolve
cm "Don't worry, I've thought of everything. I'll be wearing a blindfold..."
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.4
    ease 5.5 xpos 0.42 ypos 1.0           
show milfoillingerie04:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -0.1
    linear 6.0 xpos 0.1 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "That's a good idea. Especially since I'm getting hard anyway..."
scene compoundmilfnightseduction02 blurred
show milfoillingerie05
with dissolve
cm "There, I've put it on. Now you can get that massive [age]yo cock out of your thong, sweetie pie!"
mc "About time, Carol!"
play sound "sounds/ripping.mp3"
cm "Ooh, that sounds tells me you got an INSTANT BONER for your landlady!"
hide milfoillingerie05
show milfoillingerie06
with dissolve
label OilyMILFtitjobBx:
mc "Damn right! Let me guide you to the bed..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm feeling something really BIG brushing against my back!"
scene milfnewtitjob01 with dissolve
mc "Now get on your knees on the floor."
scene milfnewtitjob02 with dissolve
mc "Here, let me help you guide your hand to..."
scene milfnewtitjob03 with dissolve
mc "...my ROCK-HARD shaft!"
cm "Oooh, it feels so HUGE, my over-hung tenant!"
scene milfnewtitjob04 with dissolve
cm "I have to imagine I'm holding something else. Like a large iron bar."
mc "Yeah, that sounds about right. Now get those tits around that giant iron bar!"
scene milfnewtitjob05 with dissolve
cm "Like this, [name]? Is the iron bar fitting snugly between my breasts?"
mc "It sure is, Carol..."

play channel1 "sounds/wetmassage.mp3"
$ milftitjobsofterx = False
$ milftitjobharderx = False

label MilfTitjobSlowx:
play channel2 "sounds/boymoan02.mp3"
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharderx:
    mc "Let's go back to some softer titfucking, Carol..."
    window hide
    show milftittransitionsoftervideo
    $ renpy.pause(.5, hard='True')
    scene milfnewtitjob05    
    $ milftitjobharderx = False
show milftitjobslowvideo behind milftitjobfastvideo
show milftitjobslowvideo behind milftitjobharderslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitjobfastvideo
hide milftitjobharderslowvideo
with dissolve
if milftitjobsofterx == False:
    cm "Does it feel good, [name]?"
    mc "It sure does, Carol!"
    $ milftitjobsofterx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen milftitjobslowx()
screen milftitjobslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitjobHarderSlowx")

label MilfTitjobFastx:
play channel2 "sounds/boymoan02.mp3"
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharderx:
    mc "Let's go back to some softer titfucking, Carol..."
    window hide
    show milftittransitionsoftervideo
    $ renpy.pause(.5, hard='True')
    scene milfnewtitjob05    
    $ milftitjobharderx = False
show milftitjobfastvideo behind milftitjobslowvideo
show milftitjobfastvideo behind milftitjobharderfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitjobslowvideo
hide milftitjobharderfastvideo
with dissolve
if milftitjobsofterx == False:
    cm "Does it feel good, [name]?"
    mc "It sure does, Carol!"
    $ milftitjobsofterx = True
window hide
pause
show slower:
     xpos 50 ypos 500     
show harder:
     xpos 1700 ypos 500     
call screen milftitjobfastx()
screen milftitjobfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitjobHarderFastx")

label MilfTitjobHarderSlowx:
$ milftitjobsofterx = False
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharderx == False:
    mc "I just want to bury my dong between those soft mounds!"
    cm "Oooh, I'll move forward and make sure MORE titflesh rubs against it then!"
    $ milftitjobharderx = True
    show milftittransitionhardervideo
    $ renpy.pause(.5, hard='True')
    scene milftittransitionharderend01
show milftitjobharderslowvideo behind milftitjobslowvideo
show milftitjobharderslowvideo behind milftitjobharderfastvideo
show milftitjobharderslowvideo behind milftittransitionhardervideo
$ renpy.pause(.5, hard='True')
hide milftitjobslowvideo
hide milftitjobharderfastvideo
hide milftittransitionhardervideo
with dissolve
play channel2 "sounds/boyorgasm01.mp3"
window hide
pause
show cum:
     xpos 1750 ypos 1020
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen milftitjobharderslowx()
screen milftitjobharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobSlowx")

label MilfTitjobHarderFastx:
$ milftitjobsofterx = False
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharderx == False:
    mc "I just want to bury my dong between those soft mounds!"
    cm "Oooh, I'll move forward and make sure MORE titflesh rubs against it then!"
    $ milftitjobharderx = True
    show milftittransitionhardervideo
    $ renpy.pause(.5, hard='True')
    scene milftittransitionharderend01
show milftitjobharderfastvideo behind milftitjobfastvideo
show milftitjobharderfastvideo behind milftitjobharderslowvideo
$ renpy.pause(0.5, hard='True')
hide milftitjobfastvideo
hide milftitjobharderslowvideo
with dissolve
play channel2 "sounds/boyorgasm01.mp3"
window hide
pause
show cum:
     xpos 1750 ypos 1020
show slower:
     xpos 50 ypos 500     
show softer:
     xpos 1700 ypos 500     
call screen milftitjobharderfastx()
screen milftitjobharderfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobFastx")

label MilfTitjobEndx:
hide nexticon
hide slower
hide faster
hide harder
hide softer
cm "I can feel your shaft trembling... Are you going to come for me?"
mc "Oh God, I..."
scene milfnewtitjobcum01 with dissolve
stop channel2
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "...AAAAH!"
window hide
with fastflash
cm "Are you blasting for your landlady? Her funbags wrapped around your [age]yo horny cock was just too much?"
scene milfnewtitjobcum02 with dissolve
mc "Y...YES! Your tits are the BEST, Carol! RHAAA!"
window hide
with hpunch
cm "Oooh, I can FEEL the heavy splatters of your HOT SPUNK on my tits now!"
scene milfnewtitjobcum03 with dissolve
play sound "sounds/moan02.mp3"
cm "Your shaft is CONVULSING even more and I can tell it's RAINING cum on me!"
window hide
with fastflash
mc "AAAH! Those HUGE TITS!!!! I can't stop NUTTING!!!"
scene milfnewtitjobcum04 with dissolve
cm "Ooh, so you're coming like a STALLION because of my mounds of titflesh rubbing against your veiny rod? Is that what you're saying, [name]?"
window hide
with vpunch
mc "Y... YYYYEEESSSS! RHAAAA!"
scene milfnewtitjobcum05 with dissolve
play sound "sounds/lick01.ogg"
cm "You're STILL pumping that load for me?"
window hide
with fastflash
if age >= 20:
    cm "Mmmmh, I need to get my tongue on that convulsing rod!"
if age >= 18 and age <= 19:
    cm "Mmmmh, I need to get my tongue on that convulsing teenage rod!"
scene milfnewtitjobcum06 with dissolve
stop channel1
play sound "sounds/slurp.mp3"
cm "Mmmh, it's so tasty, [name]! And I can tell you really came a LOT, didn't you?"
mc "I... I guess I did... Uuuhhh..."
scene milfnewtitjobcum07 with dissolve
play sound "sounds/panting.mp3"
cm "Did your landlady totally drain your fat balls?"
mc "Gggg... Yes, Carol, you were great..."
if renpy.seen_image("milfoilpussycum05"):
    cm "But we're not done yet are we? That huge thing can remain HARD for some more fun?"
    mc "Damn right!"
    jump MilfSaunaRewardMenuCx              
cm "Well, I guess you got your reward for the evening, you'd better go back to the gallery, I need to get back in VIGILANT SUPER-HEROINE mode."
jump MILFGallery

label OilyMILFfootjobx:
scene compoundmilfnightseduction02 blurred with fade
show milfoillingerie01 with moveinright
cm "Mmmh, I'm all oiled up for my horse-hung tenant..."
mc "I'm about to get SO HARD for you, Carol!"
hide milfoillingerie01
show milfoillingerie03:
    xpos 0.2 zoom 0.5
with dissolve
cm "Not yet [name]! I can't actually {i}see{/i} your enormous fuckstick, remember?"
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.0
    ease 5.5 xpos 0.42 ypos 1.3           
show milfoillingerie03:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -1.0
    linear 6.0 xpos 0.1 ypos -0.2
with dissolve
$ renpy.pause(5.0, hard='True')
mc "But how are you supposed to give me that titjob reward without me getting HARD!!!"
scene compoundmilfnightseduction02 blurred
show milfoillingerie04:
    xpos 0.2 zoom 0.5
with dissolve
cm "Don't worry, your landlady has thought of everything. I'll be wearing a blindfold..."
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.4
    ease 5.5 xpos 0.42 ypos 1.0           
show milfoillingerie04:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -0.1
    linear 6.0 xpos 0.1 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "That's a good idea. Especially since I'm getting hard anyway..."
scene compoundmilfnightseduction02 blurred
show milfoillingerie05
with dissolve
cm "There, I've put it on. Now you can get that massive [age]yo cock out of your thong, sweetie pie!"
mc "About time!"
play sound "sounds/ripping.mp3"
cm "Ooh, that sounds tells me you got an INSTANT BONER for your landlady!"
hide milfoillingerie05
show milfoillingerie06
with dissolve
label OilyMILFfootjobBx:
mc "Damn right! Let me guide you to the bed, Carol..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm feeling something really BIG brushing against my back, [name]!"
scene milffootjob01 with dissolve
mc "There, get on the bed while I place your feet..."
scene milffootjob02 with dissolve
mc "...around my fat dong!"
cm "Mmmh, I can FEEL the warmth of your HOT shaft on my little feet..."
scene milffootjob03 with dissolve
mc "Yeah, let's start this. Your oily feet on my rock-hard dong!"
play channel2 "sounds/wank.mp3"
$ milffootjobslowx = False

label MilfFootjobSlowx:
$ milffootjobfastx = False
$ milffootharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milffootjobslowx == False and milffootstart:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslowx = True
window hide
show milffootjobslowvideo behind milffootjobfastvideo
show milffootjobslowvideo behind milffootjobslowpovvideo
show milffootjobslowvideo behind milffootjobharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide milffootjobfastvideo
hide milffootjobslowpovvideo
hide milffootjobharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if milffootjobslowx == False and milffootstart == False:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslowx = True
    $ milffootstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobslowx()
screen milffootjobslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVSlowx")

label MilfFootjobFastx:
$ milffootharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milffootjobfastx == False:
    cm "You can use my feet to jerk yourself off faster if you want, sweetie pie!"
    $ milffootjobfastx = True
show milffootjobfastvideo behind milffootjobslowvideo
show milffootjobfastvideo behind milffootjobfastpovvideo
show milffootjobfastvideo behind milffootjobharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowvideo
hide milffootjobfastpovvideo
hide milffootjobharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobfastx()
screen milffootjobfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVFastx")

label MilfFootjobPOVSlowx:
$ milffootharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milffootjobslowx == False:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslowx = True
show milffootjobslowpovvideo behind milffootjobslowvideo
show milffootjobslowpovvideo behind milffootjobfastpovvideo
show milffootjobslowpovvideo behind milffootjobharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowvideo
hide milffootjobfastpovvideo
hide milffootjobharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobslowpovx()
screen milffootjobslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobSlowx")

label MilfFootjobPOVFastx:
$ milffootharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milffootjobfastx == False:
    cm "You can use my feet to jerk yourself off faster if you want, sweetie pie!"
    $ milffootjobfastx = True
window hide
show milffootjobfastpovvideo behind milffootjobslowpovvideo
show milffootjobfastpovvideo behind milffootjobfastvideo
show milffootjobfastpovvideo behind milffootjobharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowpovvideo
hide milffootjobfastvideo
hide milffootjobharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobfastpovx()
screen milffootjobfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobFastx")

label MilfFootjobHarderSlowx:
if milffootharderx == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharderx = True        
window hide
show milffootjobharderslowvideo behind milffootjobharderfastvideo
show milffootjobharderslowvideo behind milffootjobharderpovslowvideo
show milffootjobharderslowvideo behind milffootjobslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderfastvideo
hide milffootjobharderpovslowvideo
hide milffootjobslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobharderslowx()
screen milffootjobharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCumx")

label MilfFootjobHarderFastx:
if milffootharderx == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharderx = True        
window hide
show milffootjobharderfastvideo behind milffootjobharderslowvideo
show milffootjobharderfastvideo behind milffootjobharderpovfastvideo
show milffootjobharderfastvideo behind milffootjobfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderslowvideo
hide milffootjobharderpovfastvideo
hide milffootjobfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobharderfastx()
screen milffootjobharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCumx")

label MilfFootjobHarderPOVSlowx:
if milffootharderx == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharderx = True        
window hide
show milffootjobharderpovslowvideo behind milffootjobharderslowvideo
show milffootjobharderpovslowvideo behind milffootjobharderpovfastvideo
show milffootjobharderpovslowvideo behind milffootjobslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderslowvideo
hide milffootjobharderpovfastvideo
hide milffootjobslowpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobharderpovslowx()
screen milffootjobharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCumx")

label MilfFootjobHarderPOVFastx:
if milffootharderx == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharderx = True        
window hide
show milffootjobharderpovfastvideo behind milffootjobharderpovslowvideo
show milffootjobharderpovfastvideo behind milffootjobharderfastvideo
show milffootjobharderpovfastvideo behind milffootjobfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderpovslowvideo
hide milffootjobharderfastvideo
hide milffootjobfastpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobharderpovfastx()
screen milffootjobharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCumx")

label MilfFootjobCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
play sound "sounds/boymoan02.mp3"
mc "That's it Carol, I think I'm about to..."
scene milffootjobcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "... CUUUUMMMM!!!"
window hide
with fastflash
cm "I want you to COVER your dear landlady in your fat load, you hear me?"
scene milffootjobcum02 with dissolve
mc "FUCK, AAAH!!!"
window hide
with hpunch
cm "Your iron bar is like a CUM-FIREHOSE!"
scene milffootjobcum03 with dissolve
if age >= 20:
    cm "I can feel really HEAVY splatters of spunk raining down on my back!"
if age >= 18 and age <= 19:
    cm "I can feel really HEAVY splatters of teenage spunk raining down on my back!"
window hide
with fastflash
mc "UUUH, There's MORE!"
scene milffootjobcum04 with dissolve
play sound "sounds/wow.mp3"
cm "Oh, wow! You're cumming like a WILD BRONCO for your landlady!"
window hide
with vpunch
mc "Just a... few more shots, RHAAA!"
scene milffootjobcum05 with dissolve
play sound "sounds/panting.mp3"
cm "Mmmh, all that slimy red-hot cream dripping down my back.... And my hair... You really made a CUM-MESS out of your landlady, didn't you?"
mc "Yeah, sorry... I just..."
cm "Don't you apologize sweetheart, it's perfectly natural for a horny young tenant like you to blast such a powerful load on his landlady."
if renpy.seen_image("milfoilpussycum05"):
    cm "But we're not done yet are we? That huge thing can remain HARD for some more fun?"
    mc "Damn right!"
    jump MilfSaunaRewardMenuCx              
cm "I'll clean everything up. You can go back to your room and have a good night's sleep, sweetie pie!"
jump MILFGallery

label NewMILFAnalx:
scene milfnewanal01 with dissolve
cm "But first, I'm going to lather my big tits with some oily lotion, you don't mind waiting a bit [name]?"
mc "Not at all, not at all..."
scene milfnewanal02 with dissolve
cm "And now on the legs..."
mc "Hurry up Carol, I don't think I can hold off getting hard much longer!"
scene milfnewanal03 with dissolve
cm "That's it, sweetie, the blindfold is on and I'm ready! You can get hard now and join me on the bed..."
play sound "sounds/ripping.mp3"
mc "Finally..."
label NewMILFAnalBx:
scene milfnewanal04 with dissolve
play sound "sounds/moan02.mp3"
cm "Oooh, is that your hand on my breast, [name]?"
mc "Yes it is. I just want to play with those oiled-up funbags a bit first..."
cm "Then kiss me while you fondle my giant funbags..."
scene milfnewanal05 with dissolve
play sound "sounds/kiss.mp3"
pause
scene milfnewanal06 with dissolve
play sound "sounds/kiss.mp3"
cm "Keep going, you're doing good. You're becoming such a SUPER-SEDUCER!"
scene milfnewanal07 with dissolve
play sound "sounds/moan01.mp3"
cm "Oooh, [name]! Your tongue on my breast... Mmmh..."
scene milfnewanal08 with dissolve
play sound "sounds/lick01.ogg"
cm "You're playing with my sensitive nipple... Aaaah... You're making me so horny! I just want you to FUCK ME now!"
mc "ALright, let's get into ANAL DESTRUCTION POSITIONS then!"
scene milfnewanal09 with dissolve
mc "You're going to have to really open that backdoor up, Carol!"
cm "Ooh, what did I let myself into..."
scene milfnewanal10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/moan01.mp3"
pause
mc "I'll help you by slowly inserting my lubricated glans..."
scene milfnewanal11 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH!"
mc "And a few inches of my ARM-THICK [age]yo MEGA-DONG!"
$ milfnewanalslowx = False

label MilfNewAnalSlowx:
$ milfnewanalfastx = False
$ milfanalharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewanalslowx == False:
    if age >= 20:
        cm "Please go slowly so that I can get used to the size of your MASSIVE ass-breaker..."
    if age >= 18 and age <= 19:
        cm "Please go slowly so that I can get used to the size of your MASSIVE teenage ass-breaker..."
    $ milfnewanalslowx = True
window hide
show milfnewanalslowvideo behind milfnewanalfastvideo
show milfnewanalslowvideo behind milfnewanalslowpovvideo
show milfnewanalslowvideo behind milfnewanalharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalfastvideo
hide milfnewanalslowpovvideo
hide milfnewanalharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewanalslowx()
screen milfnewanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVSlowx")

label MilfNewAnalFastx:
$ milfanalharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewanalfastx == False:
    cm "Go on, now I'm ready for your monster rod to fuck my ass FASTER!"
    $ milfnewanalfastx = True
show milfnewanalfastvideo behind milfnewanalslowvideo
show milfnewanalfastvideo behind milfnewanalfastpovvideo
show milfnewanalfastvideo behind milfnewanalharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowvideo
hide milfnewanalfastpovvideo
hide milfnewanalharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewanalfastx()
screen milfnewanalfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVFastx")

label MilfNewAnalPOVSlowx:
$ milfanalharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewanalslowx == False:
    if age >= 20:
        cm "Please go slowly so that I can get used to the size of your MASSIVE ass-breaker..."
    if age >= 18 and age <= 19:
        cm "Please go slowly so that I can get used to the size of your MASSIVE teenage ass-breaker..."
    $ milfnewanalslowx = True
show milfnewanalslowpovvideo behind milfnewanalslowvideo
show milfnewanalslowpovvideo behind milfnewanalfastpovvideo
show milfnewanalslowpovvideo behind milfnewanalharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowvideo
hide milfnewanalfastpovvideo
hide milfnewanalharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalslowpovx()
screen milfnewanalslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalSlowx")

label MilfNewAnalPOVFastx:
$ milfanalharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewanalfastx == False:
    cm "Go on, now I'm ready for your monster rod to fuck my ass FASTER!"
    $ milfnewanalfastx = True
window hide
show milfnewanalfastpovvideo behind milfnewanalslowpovvideo
show milfnewanalfastpovvideo behind milfnewanalfastvideo
show milfnewanalfastpovvideo behind milfnewanalharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowpovvideo
hide milfnewanalfastvideo
hide milfnewanalharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalfastpovx()
screen milfnewanalfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalFastx")

label MilfNewAnalHarderSlowx:
if milfanalharderx == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharderx = True        
window hide
show milfnewanalharderslowvideo behind milfnewanalharderfastvideo
show milfnewanalharderslowvideo behind milfnewanalharderpovslowvideo
show milfnewanalharderslowvideo behind milfnewanalslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderfastvideo
hide milfnewanalharderpovslowvideo
hide milfnewanalslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewanalharderslowx()
screen milfnewanalharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCumx")

label MilfNewAnalHarderFastx:
if milfanalharderx == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharderx = True        
window hide
show milfnewanalharderfastvideo behind milfnewanalharderslowvideo
show milfnewanalharderfastvideo behind milfnewanalharderpovfastvideo
show milfnewanalharderfastvideo behind milfnewanalfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderslowvideo
hide milfnewanalharderpovfastvideo
hide milfnewanalfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewanalharderfastx()
screen milfnewanalharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCumx")

label MilfNewAnalHarderPOVSlowx:
if milfanalharderx == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharderx = True        
window hide
show milfnewanalharderpovslowvideo behind milfnewanalharderslowvideo
show milfnewanalharderpovslowvideo behind milfnewanalharderpovfastvideo
show milfnewanalharderpovslowvideo behind milfnewanalslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderslowvideo
hide milfnewanalharderpovfastvideo
hide milfnewanalslowpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalharderpovslowx()
screen milfnewanalharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCumx")

label MilfNewAnalHarderPOVFastx:
if milfanalharderx == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharderx = True        
window hide
show milfnewanalharderpovfastvideo behind milfnewanalharderpovslowvideo
show milfnewanalharderpovfastvideo behind milfnewanalharderfastvideo
show milfnewanalharderpovfastvideo behind milfnewanalfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderpovslowvideo
hide milfnewanalharderfastvideo
hide milfnewanalfastpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalharderpovfastx()
screen milfnewanalharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCumx")

label MilfNewAnalCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "Gonna nut inside that tight ass!"
cm "Go on, fill me up with your sweet cum!"
scene milfanalnewcum01 with dissolve
stop channel1
play channel2 "sounds/splooge01.mp3"
play channel1 "v031/boyorgasm02.mp3"
mc "Here it CO-O-MES!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
cm "AAAH, it's so STRONG!"
scene milfanalnewcum02 with dissolve
play sound "sounds/moan06.ogg"
cm "Mommy loves your cum, [name]! AAAH!"
window hide
with hpunch
mc "RHAAA! Fuck yeah, anal cum-plosion!"
scene milfanalnewcum03 with dissolve
play sound "sounds/womancum01.mp3"
cm "Oooh, that's just so naughty, it's making me come too!"
window hide
with fastflash
mc "Yeah, cum with me Carol, AAAAH!"
scene milfanalnewcum04 with dissolve
cm "You're coming so DEEP inside my ass!"
window hide
with vpunch
mc "AAAH!"
scene milfanalnewcum05 with dissolve
mc "Here, a few more shots for you!"
window hide
with fastflash
cm "You're such a good boy, coming so much for your dear old landlady!"
scene milfanalnewcum06 with dissolve
stop channel1
play sound "sounds/panting.mp3"
stop channel2
mc "That's it, I gave you all I had... Phew..."
play sound "sounds/splat.ogg"
cm "I can see that. My ass is leaking like a cum-faucet..."
scene milfanalnewcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
if renpy.seen_image("milfoilpussycum05"):
    cm "I can Super-Sense that your monster dong is still READY for some more HAREM SEX! You're such a STALLION, my sweet tenant!"
    mc "Damn right!"
    jump MilfSaunaRewardMenuCx              
cm "I'm going to have to take the blindfold off to clean up all this cummy mess on my bed, [name]. You'd better leave so I don't see what caused it..."
mc "Sure Carol, good night then. And thanks for offering me your ass as a reward..."
stop music
jump MILFGallery

label NewMILFPussyx:
mc "Let me guide you to the bed, Carol..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm going to have to imagine that it's not your enormous fuckstick I feel against my back."
mc "Not at all, it's...err... A piece of large tubing I was carrying around to fix your plumbing."
scene milfoilpussy01:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
cm "I prefer that... My pussy is already so... WET!"
scene milfoilpussy02 with dissolve
mc "Let me inspect the grounds first... Yes, I see the problem. You have some leakage."
cm "Ooh, can you do something about it?"
mc "I will attempt a sealing procedure. I must get underneath you for easier access."
scene milfoilpussy03 with dissolve
play sound "sounds/moan02.mp3"
cm "Mmmh, you're such a handyman, my sweet tenant!"
mc "In a tongue-in-cheek way, yes."
scene milfoilpussy04 with dissolve
play sound "sounds/moan05.mp3"
cm "Aaaah! Is it working?"
mc "I don't know yet, I feel some rumbling down the pipe..."
scene milfoilpussy05 with dissolve
play sound "sounds/womancum02.mp3"
cm "Ooooh!"
mc "I fear the leak is more severe than previously anticipated."
scene milfoilpussy06 with dissolve
cm "I sure hope you have the tools to fix it!"
mc "I've brought the biggest one available on the market. It should be to your satisfaction, Carol."
scene milfoilpussy07 with dissolve
play sound "sounds/moan02.mp3"
cm "Ooh, what are you doing naughty boy? You're so STRONG!"
mc "Sorry, I couldn't resist..."
scene milfoilpussy08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/lick01.ogg"
mc "And I can't resist this either. But it's time to lay on your back and start the procedure..."
cm "Alright, sweetie pie! I entrust my body into your hands. And BIG tool."
scene milfoilpussy09 with dissolve
cm "I feel something slimy falling on my tits..."
mc "Yeah, I'm preparing the lubricant. Gonna need LOTS of it to clean that clogged pipe!"
scene milfoilpussy10 with dissolve
cm "Ooh, now I feel something real BIG rubbing against my tender pussylips..."
mc "Yep, that's the BIG tool I was talking about."
scene milfoilpussy11 with dissolve
cm "It's INSIDE me! AAAH, it's so HUGE!"
mc "Need it that size for maximum friction! Here we go, Carol!"
$ milfnewpussyslowx = False

label MilfNewPussySlowx:
$ milfnewpussyfastx = False
$ milfpussyharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewpussyslowx == False:
    mc "Just relax while I start de-clogging that DEEP pipe of yours, Carol!"
    $ milfnewpussyslowx = True
window hide
show milfnewpussyslowvideo behind milfnewpussyfastvideo
show milfnewpussyslowvideo behind milfnewpussyslowpovvideo
show milfnewpussyslowvideo behind milfnewpussyharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyfastvideo
hide milfnewpussyslowpovvideo
hide milfnewpussyharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewpussyslowx()
screen milfnewpussyslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVSlowx")

label MilfNewPussyFastx:
$ milfpussyharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewpussyfastx == False:
    cm "Uuuh, I can feel your TOOL being RAMMED right up inside me!"
    $ milfnewpussyfastx = True
show milfnewpussyfastvideo behind milfnewpussyslowvideo
show milfnewpussyfastvideo behind milfnewpussyfastpovvideo
show milfnewpussyfastvideo behind milfnewpussyharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowvideo
hide milfnewpussyfastpovvideo
hide milfnewpussyharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewpussyfastx()
screen milfnewpussyfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussySlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVFastx")

label MilfNewPussyPOVSlowx:
$ milfpussyharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewpussyslowx == False:
    mc "Just relax while I start de-clogging that DEEP pipe of yours, Carol!"
    $ milfnewpussyslowx = True
show milfnewpussyslowpovvideo behind milfnewpussyslowvideo
show milfnewpussyslowpovvideo behind milfnewpussyfastpovvideo
show milfnewpussyslowpovvideo behind milfnewpussyharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowvideo
hide milfnewpussyfastpovvideo
hide milfnewpussyharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyslowpov()
screen milfnewpussyslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussySlowx")

label MilfNewPussyPOVFastx:
$ milfpussyharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewpussyfastx == False:
    cm "Uuuh, I can feel your TOOL being RAMMED right up inside me!"
    $ milfnewpussyfastx = True
window hide
show milfnewpussyfastpovvideo behind milfnewpussyslowpovvideo
show milfnewpussyfastpovvideo behind milfnewpussyfastvideo
show milfnewpussyfastpovvideo behind milfnewpussyharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowpovvideo
hide milfnewpussyfastvideo
hide milfnewpussyharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyfastpov()
screen milfnewpussyfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyFastx")

label MilfNewPussyHarderSlowx:
if milfpussyharderx == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharderx = True        
window hide
show milfnewpussyharderslowvideo behind milfnewpussyharderfastvideo
show milfnewpussyharderslowvideo behind milfnewpussyharderpovslowvideo
show milfnewpussyharderslowvideo behind milfnewpussyslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderfastvideo
hide milfnewpussyharderpovslowvideo
hide milfnewpussyslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewpussyharderslowx()
screen milfnewpussyharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussySlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCumx")

label MilfNewPussyHarderFastx:
if milfpussyharderx == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharderx = True        
window hide
show milfnewpussyharderfastvideo behind milfnewpussyharderslowvideo
show milfnewpussyharderfastvideo behind milfnewpussyharderpovfastvideo
show milfnewpussyharderfastvideo behind milfnewpussyfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderslowvideo
hide milfnewpussyharderpovfastvideo
hide milfnewpussyfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewpussyharderfastx()
screen milfnewpussyharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCumx")

label MilfNewPussyHarderPOVSlowx:
if milfpussyharderx == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharderx = True        
window hide
show milfnewpussyharderpovslowvideo behind milfnewpussyharderslowvideo
show milfnewpussyharderpovslowvideo behind milfnewpussyharderpovfastvideo
show milfnewpussyharderpovslowvideo behind milfnewpussyslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderslowvideo
hide milfnewpussyharderpovfastvideo
hide milfnewpussyslowpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyharderpovslowx()
screen milfnewpussyharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCumx")

label MilfNewPussyHarderPOVFastx:
if milfpussyharderx == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharderx = True        
window hide
show milfnewpussyharderpovfastvideo behind milfnewpussyharderpovslowvideo
show milfnewpussyharderpovfastvideo behind milfnewpussyharderfastvideo
show milfnewpussyharderpovfastvideo behind milfnewpussyfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderpovslowvideo
hide milfnewpussyharderfastvideo
hide milfnewpussyfastpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyharderpovfastx()
screen milfnewpussyharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCumx")

label MilfNewPussyCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "Full-blown pressure down the hose coming!"
cm "I'm bracing myself for it!"
scene milfoilpussycum01 with dissolve
stop channel1
play channel2 "sounds/splooge01.mp3"
play channel1 "v031/boyorgasm02.mp3"
mc "BLASTING! RHAAA!!!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
cm "AAAH, it's a DELUGE!"
scene milfoilpussycum02 with dissolve
play sound "sounds/moan06.ogg"
cm "My insides are turning RED-HOT from your HUGE POUNDING TOOL!"
window hide
with hpunch
mc "Hold on, I'm gonna..."
scene milfoilpussycum03 with dissolve
play sound "sounds/womancum01.mp3"
mc "...COME BIG TIME, AAAH!"
window hide
with fastflash
play sound "sounds/womancum02.mp3"
cm "So much for me, I'm CONVULSING!"
scene milfoilpussycum04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
cm "I'm getting PUMPED FULL!"
window hide
with vpunch
mc "CAN'T HOLD THE HOSE STEADY! AAAH!"
scene milfoilpussycum05 with dissolve
stop channel2
mc "It slipped out but I'm still at FULL BLAST POWER, RHAAA!!!"
window hide
with fastflash
cm "That's because you've filled me up so full of CREAM!"
scene milfoilpussycum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "I'm gonna say the procedure worked and that your pipes are cleaned..."
play sound "sounds/moan02.mp3"
cm "Uuuhh..."
scene milfoilpussycum07 with dissolve
cm "I feel there's still a MASSIVE leakage down there."
mc "Yeah, but it's the good type."
cm "Is your tool ready for more handiwork?"
mc "Of course, Carol!"
jump MilfSaunaRewardMenuCx