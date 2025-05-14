label AngelaGallery:
stop channel3
play sound "sounds/angel.mp3"
scene angelabackground
show angelamaingallery at gallerypos01 with moveinleft
call screen galleryangela()
screen galleryangela():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Angela{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryangela"), Jump ("MainGallery04b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryangela"), Jump ("AngelaGalleryAnim")]
    
    if renpy.seen_image("angelaroom01"):
        imagebutton:
            focus_mask True
            idle "gallery/angelagallery01.png" xpos 400 ypos 100
            hover "gallery/angelagallery01.png"
            action Jump ("AngelaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Dreamy Handjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("angelaroom01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("AngelaGallery01hint")

    if renpy.seen_image("angelaroom11"):
        imagebutton:
            focus_mask True
            idle "gallery/angelagallery02.png" xpos 750 ypos 100
            hover "gallery/angelagallery02.png"
            action Jump ("AngelaGallery02")
    text "{font=Gui/Heroes Legend.ttf}Dreamy Fuck{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("angelaroom11") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("AngelaGallery02hint")

label AngelaGallery01hint:
show angelamaingallery at gallerypos01
show angelagallery01 at posgalleryhintpic
show angelagalleryhint01 at posgalleryhint
pause
hide angelagalleryhint01
hide angelagallery01
call screen galleryangela()
 
label AngelaGallery02hint:
show angelamaingallery at gallerypos01
show angelagallery02 at posgalleryhintpic
show angelagalleryhint02 at posgalleryhint
pause
hide angelagalleryhint02
hide angelagallery02
call screen galleryangela()

label AngelaGalleryAnim:
stop sound
stop channel3
play channel3 "sounds/sexy01.mp3"
call screen screenanimangela()
screen screenanimangela():
    modal True
    add "gallery/angelabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "angelaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "angelaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimangela"), SetVariable ("animcount", 1), Jump ("AngelaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Angela{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero03
    text "{font=Gui/Heroes Legend.ttf}Age: 6500{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft7{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}32D-22-34{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Handjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Cock Worship{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/angelaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimangela")]
    add "gallery/angelaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimangela")]

label AngelaGallery01:
stop channel3
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
scene intromcsleep02a with dissolve
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
$ angelajerktoldx = False
label AngelaJerkSlowx: 
hide cum
hide faster
hide slower
show angelajerkslowvideo behind angelajerkfastvideo
pause 1.0
hide angelajerkfastvideo with dissolve
if angelajerktoldx == False:
    if age >= 20:
        voice "angel/handjob10a"
        an "I'll start by teasing you with a slow, sensual, two-handed wank on your monstrous shaft..."
    if age >= 18 and age <= 19:
        voice "angel/handjob10b"
        an "I'll start by teasing you with a slow, sensual, two-handed wank on your monstrous teenage shaft..."
    window hide
    $ angelajerktoldx = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen angelajerkslowx()
screen angelajerkslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AngelaJerkFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AngelaJerkEndx")

label AngelaJerkFastx:
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

call screen angelajerkfastx()
screen angelajerkfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("AngelaJerkSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AngelaJerkEndx")

label AngelaJerkEndx:
voice "angel/handjob11"
an "Come for me, [name]. Let's move one ladder step closer to Heavens!"
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
if renpy.seen_image("angeladream01"):
    voice "angel/handjob13"
    an "It's better than jerking off to me in the jacuzzi, isn't it?"
    mc "Err... How did you know I was, like, dreaming about you?"
    voice "angel/handjob14"
    an "Because I'm your GOOD conscience, [name]! I know your every thought..."
if renpy.seen_image("angeladream01") == False:
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
mc "Oh shit, it wasn't real after all... And I came all over myself instead of all over Angela's face... * sigh *"
jump AngelaGallery
label AngelaGallery02:
scene intromcsleep02
play sound "sounds/dream.mp3"
$ renpy.pause(1.0, hard='True')
play music "sounds/introdreaming.mp3"
show angela01a at topleft with moveinleft
hide angela01a
show angelafly01 at topleft
an "Open your eyes, [hero]!"
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
scene angelaroom17 with dissolve
an "Did you notice that I took my angelic bodysuit off for you?"
mc "I sure did, Angela! My cock is ROCK-HARD at the sight of your lovely breasts!"
scene angelaroom18 with dissolve
an "You're such a sweet [age]yo boy! So very romantic. And so very HORNY! You deserve a HEAVENLY FUCK!"
window hide

label AngelaFuckSlowx: 
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

call screen angelafuckslowx()
screen angelafuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AngelaFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AngelaFuckEndx")

label AngelaFuckFastx:
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

call screen angelafuckfastx()
screen angelafuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("AngelaFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AngelaFuckEndx")

label AngelaFuckEndx:    
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
mc "Oh shit, it wasn't real after all... And I came all over myself instead of inside Angela's angelic twat... * sigh *"
stop music
stop channel1
stop channel2
jump AngelaGallery