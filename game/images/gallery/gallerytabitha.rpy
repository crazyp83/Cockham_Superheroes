label TabithaGallery:
stop channel3
play channel3 "sounds/dark.mp3"
scene tabithabackground
show tabithamaingallery at gallerypos01 with moveinleft
call screen gallerytabitha()
screen gallerytabitha():
    text "{font=Gui/Heroes Legend.ttf}Naughty Tabitha Gala-Vag{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerysawyer"), Jump ("MainGallery03b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerytabitha"), Jump ("TabithaGalleryAnim")]
    
    if renpy.seen_image("tabithadance01"):
        imagebutton:
            focus_mask True
            idle "gallery/tabithagallery01.png" xpos 400 ypos 100
            hover "gallery/tabithagallery01.png"
            action Jump ("TabithaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Belly Dancing{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("tabithadance01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("TabithaGallery")

    if renpy.seen_image("sirensbackroom01"):
        imagebutton:
            focus_mask True
            idle "gallery/keengallery02.png" xpos 750 ypos 100
            hover "gallery/keengallery02.png"
            action Jump ("TabithaGallery02")
    text "{font=Gui/Heroes Legend.ttf}Back Room Threesome{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("sirensbackroom01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("KeenGallery")
            
label TabithaGalleryAnim:
stop channel3
play channel3 "sounds/sexy06.mp3"
call screen screenanimtabitha()
screen screenanimtabitha():
    modal True
    add "gallery/tabithabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "tabithaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "tabithaanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "tabithaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimtabitha"), SetVariable ("animcount", 1), Jump ("TabithaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Tabitha Gala-Vag{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero01
    text "{font=Gui/Heroes Legend.ttf}Age: 24{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft4{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}30DD-20-32{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}BDSM{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Male Rape{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/tabithaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimtabitha")]
    add "gallery/tabithaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimtabitha")]
    add "gallery/tabithaanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimtabitha")]
            
label TabithaGallery01:
stop channel3
play music "sounds/bellydance.mp3"
scene tabithadance01 with dissolve
ta "In that case, I'll show you my belly-dance dance routine... Even though I'm not wearing my proper costume for that..."
mc "Fine by me."
scene tabithadance02 with dissolve
ta "It's meant to be highly SENSUAL and EROTIC."
mc "So far so good, I must admit."
scene tabithadance03 with dissolve
ta "Really? You're not saying that just to please me?"
scene tabithadance04 with dissolve
mc "It comes from the bottom of my co... I mean, heart."
scene tabithadance05 with dissolve
ta "I'm glad you're enjoying, I have something SPECIAL for you at the end..."
mc "Ooh, I can't wait!"
scene tabithadance06 with dissolve
ta "It will TAKE YOUR BREATH AWAY..."
mc "Now we're talking!"
scene tabithadance07 with dissolve
ta "You won't soon forget what will happen to you..." 
scene tabithadance08 with dissolve
ta "So come closer, [hero], come and get your REWARD."
mc "I'm READY! Fuck YEAH!"
scene tabithadance09 with dissolve
mc "What the...?"
ta "Here's your REWARD, you dirty boy! You think you can Super-Seduce a trained assassin?"
mc "Well, err, I thought..."
scene tabithadance10 with dissolve
ta "Do you know what dagger this is?"
mc "A very sharp one, please stop pushing it against my beautiful baby-skin!"
ta "It's the dagger that killed Ra's Al-Ghul. It can cut through steel-plated armor like butter..."
mc "I'm not Ra's Al-Ghul! Please spare me, I have nothing to do with that dude, whoever he is!"
scene tabithadance09 with dissolve
ta "Don't fucking come back again to try and stir trouble in Barbara Keen's establishment, [hero]...."
mc "I won't, I won't, I promise!"
ta "Good. You may go...safely."
mc "* Damn, she's beautiful, nuts AND dangerous! *"
stop music
jump TabithaGallery

label TabithaGallery02:
stop channel3
stop music
scene sirensbackroombackground
show tabithalingerie01 at midright
with fade
show keenlingerie01 at midleft with moveinleft
bk "Now let's see if that outfit fits you..."
hide tabithalingerie01
show tabithalingerie02 at midright
with fastdissolve
ta "It clearly doesn't, even though I gave him the one with the LARGEST pouch size available..."
hide keenlingerie01
show keenlingerie02 at midleft 
with fastdissolve
bk "Ooh, INTERESTING. Our clientele are going to LIKE this a LOT..."
hide keenlingerie02
show keenlingerie03 at midleft 
hide tabithalingerie02
show tabithalingerie01 at midright
with fastdissolve
bk "Now step on the stage and show us the goods, [hero]..."
play music "sounds/sexy06.mp3"
scene sirensbackroom01 with dissolve
mc "This is super-embarrassing. My cock is literally hanging out..."
bk "Never mind that. Take a bow, we're your audience."
scene sirensbackroom02 with dissolve
ta "He's a natural."
mc "And next?"
bk "Improvise. We need to get aroused by your routine..."
scene sirensbackroom03 with dissolve
ta "Keep smiling. Our female clientele want to feel appreciated."
bk "And use that pole. It's there for a reason."
scene sirensbackroom04 with dissolve
mc "Err, hi ladies, welcome to my SEXY show!"
ta "Now we're talking."
scene sirensbackroom05 with dissolve
ta "His cock is flying everywhere! * giggles *"
scene sirensbackroom06 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And look at it hanging all the way to the ground... It does look YUMMY!"
scene sirensbackroom07 with dissolve
ta "Maybe we should test-ride it first then? What do you think, Barbara?"
bk "I think I haven't had a cock in a long time... TOO LONG!"
ta "That's cos you've been too busy with my PUSSY! * giggles *"
bk "GET HARD FOR US, BOY!"
scene sirensbackroom08 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I'm definitely test-riding THAT THING!"
scene sirensbackroom09 with dissolve
mc "I feel like a cheap piece of meat."
bk "That's what you are. At our clientele's disposal. And therefore at OUR disposal too."
mc "I get it. I want the job badly so I'll do as I'm told. Plus, I'm just too horny right now."
stop music fadeout 2.0
bk "Your routine was quite good. But it could be better. Why don't you stand next to me while Tabitha shows you how to perform a PROPER pole dance routine?..."
play music "sounds/sexy11.mp3"
scene sirensbackroom10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
bk "Watch her. And learn from her. Then, you'll be ready to be a gigolo waiter at my big party..."
mc "Su.. Sure..."
scene sirensbackroom11 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I feel a HORNY audience tonight..."
scene sirensbackroom12 with dissolve
$ renpy.pause(1.0, hard='True')
ta "HORNY for a HOT, SENSUAL, show..."
bk "See how she engages with her audience?"
scene sirensbackroom13 with dissolve
$ renpy.pause(1.0, hard='True')
mc "Damn, look at that backside!"
bk "She's making you even HARDER, isn't she? I can feel your dong GROWING, [hero]..."
scene sirensbackroom14 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I'm HORNY too..."
scene sirensbackroom15 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And look at how agile she is..."
scene sirensbackroom16 with dissolve
mc "Oh fuck..."
scene sirensbackroom17 with dissolve
bk "Yeah, watch her slide down that pole while my hand slides up YOURS!"
scene sirensbackroom18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
bk "Watch what she's about to do..."
scene sirensbackroom19 with dissolve
$ renpy.pause(1.0, hard='True')
ta "...for the final touch!"
mc "Oh!!!"
scene sirensbackroom20 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And now the Grand Finale! What did you think?"
mc "Spectacular!"
stop music
ta "You ain't seen nothing yet, [hero]... Barbara, why don't you join me on stage?"
scene sirensbackroom21 with dissolve
play music "sounds/sexy13.mp3"
bk "I thought you'd never ask. Let me take my top off..."
scene sirensbackroom22 with dissolve
ta "Your breast are so soft... I never tire of playing with them!"
scene sirensbackroom23 with dissolve
play sound "sounds/moan02.mp3"
bk "And I LOVE how you play so delicately with them too..."
scene sirensbackroom24 with dissolve
ta "There's something else soft and tender that I'd like to play with..."
scene sirensbackroom25 with dissolve
play sound "sounds/moan02.mp3"
bk "Mmmh... In front of this... young muscle stud... You're going to make him so jealous..."
scene sirensbackroom26 with dissolve
mc "You girls are making me so FUCKING HORNY!"
scene sirensbackroom27 with dissolve
bk "Then come and join us..."
mc "FUCK YEAH!"
scene sirensbackroom28 with dissolve
ta "I'm going to lick that sumptuous pussy."
scene sirensbackroom29 with dissolve
mc "While I finger your sumptuous PUSSY!"
play sound "sounds/moan01.mp3"
ta "Oooh, that's so NAUGHTY!"
scene sirensbackroom30 with dissolve
play channel2 "sounds/lick01.ogg"
bk "Oooh... That's so..."
scene sirensbackroom31 with dissolve
play sound "sounds/moan03.mp3"
bk "...GOOOD!"
scene sirensbackroom30 with fastdissolve
play channel1 "sounds/moan02.mp3"
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
scene sirensbackroom30 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
scene sirensbackroom30 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
stop channel1
stop channel2
ta "That was real Tasty, Barbara..."
bk "I... NEED A COCK! Carry us to the fuck area, [hero]..."
stop music
scene sirensbackroom32 with fastdissolve
bk "Oh my, you really are STRONG!"
if mcstrength == 1:
    mc "Super-Strength Level 1 right there, ladies!"
if mcstrength == 2:
    mc "Super-Strength Level 2 right there, ladies!"
    ta "Level 2? Wow, almost as strong as SUPERMAN!"

scene sirensbackroom33 with fastdissolve
bk "So what are you going to do, Super-Strong Boy?"
mc "I'm going to stick my giant pud up your twat so far, you'll be able to TASTE IT!"
bk "Let' see if you can keep promises then..."
scene sirensbackroom34 with dissolve
play sound "sounds/moan05.mp3"
bk "OOOOH! It's... * panting * ...already QUITE deep... Just go slow at first..."

label SirensBarbShortFuckSlowxx:
$ barbharderx = False
window hide
show sirensbarbshortslowvideo behind sirensbarbshortfastvideo
show sirensbarbshortslowvideo behind sirensbarbshortpovslowvideo
show sirensbarbshortslowvideo behind sirensbarbslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbshortfastvideo
hide sirensbarbshortpovslowvideo
hide sirensbarbslowvideo
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
call screen sirensbarbshortslowxx()
screen sirensbarbshortslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckFastxx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVSlowxx")

label SirensBarbShortFuckFastxx:
$ barbharderx = False
window hide
show sirensbarbshortfastvideo behind sirensbarbshortslowvideo
show sirensbarbshortfastvideo behind sirensbarbshortpovfastvideo
show sirensbarbshortfastvideo behind sirensbarbfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbshortslowvideo
hide sirensbarbshortpovfastvideo
hide sirensbarbfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen sirensbarbshortfastxx()
screen sirensbarbshortfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckSlowxx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVFastxx")

label SirensBarbShortFuckPOVSlowxx:
$ barbharderx = False
window hide
show sirensbarbshortpovslowvideo behind sirensbarbshortslowvideo
show sirensbarbshortpovslowvideo behind sirensbarbshortpovfastvideo
show sirensbarbshortpovslowvideo behind sirensbarbpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbshortslowvideo
hide sirensbarbshortpovfastvideo
hide sirensbarbpovslowvideo
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
show sceneicon:
     xpos 50 ypos 500     
call screen sirensbarbshortpovslowxx()
screen sirensbarbshortpovslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckPOVFastxx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckSlowxx")

label SirensBarbShortFuckPOVFastxx:
$ barbharderx = False
window hide
show sirensbarbshortpovfastvideo behind sirensbarbshortpovslowvideo
show sirensbarbshortpovfastvideo behind sirensbarbshortfastvideo
show sirensbarbshortpovfastvideo behind sirensbarbpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbshortpovslowvideo
hide sirensbarbshortfastvideo
hide sirensbarbpovfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen sirensbarbshortpovfastxx()
screen sirensbarbshortpovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckPOVSlowxx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckFastxx")

label SirensBarbFuckSlowxx:
if barbharderx == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharderx = True        
window hide
show sirensbarbslowvideo behind sirensbarbfastvideo
show sirensbarbslowvideo behind sirensbarbpovslowvideo
show sirensbarbslowvideo behind sirensbarbshortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbfastvideo
hide sirensbarbpovslowvideo
hide sirensbarbshortslowvideo
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
call screen sirensbarbslowxx()
screen sirensbarbslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckFastxx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEndxx")

label SirensBarbFuckFastxx:
if barbharderx == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharderx = True        
window hide
show sirensbarbfastvideo behind sirensbarbslowvideo
show sirensbarbfastvideo behind sirensbarbpovfastvideo
show sirensbarbfastvideo behind sirensbarbshortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbslowvideo
hide sirensbarbpovfastvideo
hide sirensbarbshortfastvideo
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
call screen sirensbarbfastxx()
screen sirensbarbfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckSlowxx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEndxx")

label SirensBarbFuckPOVSlowxx:
if barbharderx == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharderx = True        
window hide
show sirensbarbpovslowvideo behind sirensbarbslowvideo
show sirensbarbpovslowvideo behind sirensbarbpovfastvideo
show sirensbarbpovslowvideo behind sirensbarbshortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbslowvideo
hide sirensbarbpovfastvideo
hide sirensbarbshortpovslowvideo
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
call screen sirensbarbpovslowxx()
screen sirensbarbpovslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckPOVFastxx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEndxx")

label SirensBarbFuckPOVFastxx:
if barbharderx == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharderx = True        
window hide
show sirensbarbpovfastvideo behind sirensbarbpovslowvideo
show sirensbarbpovfastvideo behind sirensbarbfastvideo
show sirensbarbpovfastvideo behind sirensbarbshortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbpovslowvideo
hide sirensbarbfastvideo
hide sirensbarbshortpovfastvideo
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
call screen sirensbarbpovfastxx()
screen sirensbarbpovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckPOVSlowxx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEndxx")

label SirensBarbCumEndxx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
if age >= 20:
    bk "Please cum, [hero], I want to get FILLED UP with your YOUNG CREAM!"
if age >= 18 and age <= 19:
    bk "Please cum, [hero], I want to get FILLED UP with your YOUNG TEENAGE CREAM!"
window hide
show sirensbarbpovfastvideo behind sirensbarbpovslowvideo
show sirensbarbpovfastvideo behind sirensbarbfastvideo
show sirensbarbpovfastvideo behind sirensbarbshortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbpovslowvideo
hide sirensbarbfastvideo
hide sirensbarbshortpovfastvideo
mc "Alright, I'll show you how a SUPERSTUD COMES!"
window hide
pause 1.0
stop channel1
play channel1 "sounds/splooge02.mp3"
show sirenscum01 at truecenter:
    subpixel True
    linear 3.0 zoom 1.2 xoffset 0 yoffset 0 
with dissolve
mc "I'M BLOWING NOOOOWWWW!"
window hide
with fastflash
scene sirenscum02 with dissolve
mc "AND MORE! RHAAA!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
bk "AAAAH!"
window hide
with fastflash
ta "Pull out, she loves to be DOUSED in warm ball-batter!"
scene sirenscum03 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "HERE YOU ARE, WARM CUM COMING YOUR WAY!!!"
window hide
with fastflash
if age >= 20:
    bk "He's CAKING me in red-hot SPUNK!"
if age >= 18 and age <= 19:
    bk "He's CAKING me in red-hot TEEN SPUNK!"
scene sirenscum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Damn it... I'm still HARD. I'm gonna fuck ANOTHER PUSSY!"
bk "I guess it's your turn, Tabitha..."
ta "Is he really STILL HARD?"
scene sirenscum04 with dissolve
play sound "sounds/thud.mp3"
mc "Does this sound answer your question?"
ta "Oh fuck... This is UNREAL..."

scene sirenscum06 with dissolve
play sound "sounds/moan02.mp3"
ta "I can feel his HUGE HELMET... Already distending my pussylips..."

label SirensTabFuckSlowxx:
$ tabharderx = False
window hide
show sirenstabslowvideo behind sirenstabfastvideo
show sirenstabslowvideo behind sirenstabpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sirenstabfastvideo
hide sirenstabpovslowvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen sirenstabslowxx()
screen sirenstabslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckPOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEndxx")

label SirensTabFuckFastxx:
if tabharderx == False:
    ta "I need to come, fuck me FASTER, STUD!"
    $ tabharderx = True        
window hide
show sirenstabfastvideo behind sirenstabslowvideo
show sirenstabfastvideo behind sirenstabpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sirenstabslowvideo
hide sirenstabpovfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen sirenstabfastxx()
screen sirenstabfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckPOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEndxx")

label SirensTabFuckPOVSlowxx:
$ tabharderx = False
window hide
show sirenstabpovslowvideo behind sirenstabslowvideo
show sirenstabpovslowvideo behind sirenstabpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sirenstabslowvideo
hide sirenstabpovfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen sirenstabpovslowxx()
screen sirenstabpovslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckPOVFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEndxx")

label SirensTabFuckPOVFastxx:
if tabharderx == False:
    ta "I need to come, fuck me FASTER, STUD!"
    $ tabharderx = True        
window hide
show sirenstabpovfastvideo behind sirenstabpovslowvideo
show sirenstabpovfastvideo behind sirenstabfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sirenstabpovslowvideo
hide sirenstabfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen sirenstabpovfastxx()
screen sirenstabpovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckPOVSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEndxx")

label SirensTabCumEndxx:
ta "You're gonna cum again, aren't you?"
mc "Fuck yeah..."
bk "He's gonna pump you FULL of his seed, Tabitha. You'd better get prepared!"
ta "Oh, I AM READY!"
scene sirenstabcum01 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
mc "Fuck, AAAAAHHH!"
window hide
with fastflash
ta "YES, YES, I'M CUMMING TOO!"
scene sirenstabcum02 with dissolve
play sound "sounds/moan06.ogg"
mc "ALL THE WAY IN!"
window hide
with hpunch
ta "AAAAH, IT'S SO DEEP!!!"
scene sirenstabcum03 with dissolve
play sound "sounds/boymoan03.mp3"
mc "OH GOD, I still NEED TO CUM SO MUCH, AAAH!"
window hide
with fastflash
bk "EMPTY THOSE BALLS, COME ON, COVER ME AGAIN IN YOUR SPUNK!"
scene sirenstabcum04 with dissolve
play sound "sounds/boymoan05.mp3"
mc "I'm CUMMING, BIG TIIIIMMME!"
window hide
with fastflash
ta "I can even HEAR his MASSIVE cumblasts!"
window hide 
with hpunch
play sound "sounds/boymoan03.mp3"
mc "Take those last few shots, my little cum-sluts! RHAAA!"
scene sirenstabcum05 with dissolve
bk "He did it again... I'm absolutely DRENCHED in his [age]yo scum..."
ta "I can feel his goo sliding down my poor ass... And he called us \"cum-sluts\", you heard that?"
bk "Yes, that was highly inappropriate, even though some of our clientele DO like to be domin..."
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "Ouch! What.. what are you doing?"
mc "You deserve a punishment for being my little cock-sluts today..."
scene sirenstabcum05 with dissolve
bk "He's so MANLY, even though he's just a BOY!"
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "AAAH, yes, slap me Daddy!"
scene sirenstabcum05 with dissolve
bk "Daddy? Why are you calling him that???"
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "Ow! Err... I don't know, I just blurted it out..."

scene sirensbackroombackground
show tabithacum01 at midright
show keencum02 at midleft
with fade
ta "So, do you reckon he passed the test, Barbara?"
hide keencum02
show keencum01 at midleft
with fastdissolve
bk "I suppose we could hire him for ONE night at least and see how he BEHAVES!"
hide tabithacum01
show tabithacum02 at midright
with fastdissolve
ta "I'll keep an eye on him. And I'll SLIT HIS THROAT if he does!"
mc "Wow. Is there an union I can join to fight these violent corporate threats?"
bk "No."
hide tabithacum02
show tabithacum01 at midright
with fastdissolve
ta "We'll let you know when we need you. Now GO. Back to the gallery"
jump TabithaGallery
