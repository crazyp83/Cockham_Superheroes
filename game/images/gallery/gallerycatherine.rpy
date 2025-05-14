label CatherineGallery:
stop channel3
play channel3 "sounds/gala.mp3"
scene catherinebackground
show catherinemaingallery at gallerypos01 with moveinleft
call screen gallerycatherine()
screen gallerycatherine():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Catherine Krass{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerycatherine"), Jump ("MainGallery03")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerycatherine"), Jump ("CatherineGalleryAnim")]
     
    if renpy.seen_image("catherineshowercum04"):
        imagebutton:
            focus_mask True
            idle "gallery/catherinegallery01.png" xpos 400 ypos 100
            hover "gallery/catherinegallery01.png"
            action Jump ("CatherineGallery01")
    text "{font=Gui/Heroes Legend.ttf}Shower Sex{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("catherineshowercum04") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("CatherineGallery")

label CatherineGalleryAnim:
stop channel3
play channel3 "sounds/sexy09.mp3"
call screen screenanimcatherine()
screen screenanimcatherine():
    modal True
    add "gallery/catherinebackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "cathanimlin" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "cathanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimcatherine"), SetVariable ("animcount", 1), Jump ("CatherineGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Catherine Krass{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero01
    text "{font=Gui/Heroes Legend.ttf}Age: 26{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft9{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34D-22-38{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Orgies{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Lesbian{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/cathanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimcatherine")]
    add "gallery/cathanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimcatherine")]
            
label CatherineGallery01:
$ catherineshowertold01x = False
stop channel3
scene catherinepost03 with dissolve

ck "Carry me there in your strong arms... HERO."
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play channel1 "sounds/sexy05.mp3"
scene catherineshower01 with fade
ck "Don't be shy, get out of your thong... Your cock looks like it's STRAINING to come out!"
scene catherineshower02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
ck "I'm getting in. Join me when you're ready."
scene catherineshower03 with dissolve
play channel2 "sounds/shower.mp3"
mc " * Damn, what a THICC ass... I'm getting ROCKHARD right now! * "
scene catherineshower04 with dissolve
mc "Is the water hot yet? I only take HOT showers."
ck "It's perfect. And once you join me, I'm sure it will get HOTTER!"
scene catherineshower05 with dissolve
ck "Finally, I can clean myself. Clean yourself too, I don't want to get TOO messy with you..." 
scene catherineshower06 with dissolve
stop channel2
ck "And now... Let's get STEAMY! With that MONSTERCOCK of yours! How big is it exactly?"
if age >= 20:
    mc "Fifteen inches of boymeat for you, Catherine!"
if age >= 18 and age <= 19:
    mc "Fifteen inches of teenage boymeat for you, Catherine!"
ck "Damn, that's ssso BIG! Come closer, [name]..."
scene catherineshower07 with dissolve
play sound "sounds/lick01.ogg"
ck "Mmh, just like that... Lick me clean, [name]!"
scene catherineshower08a with dissolve
mc "How about I rub my shaft against your dirty pussy to make it cleaner..."
window hide
scene catherineshowerdick
pause
if age >= 20:
    ck "Oh FUCK! Your cock is so MASSIVE! I bet you have TONS of virile sperm to unleash, don't you?"
if age >= 18 and age <= 19:
    ck "Oh FUCK! Your cock is so MASSIVE! I bet you have TONS of virile teenage sperm to unleash, don't you?"
scene catherineshower08c with dissolve
play sound "sounds/boymoan03.mp3"
mc "AAAH! Look what you've made me do with your sexy talk!"
window hide
with fastflash
ck  "You're cumming already?"
scene catherineshower08a with dissolve
ck "You've got more for me, STUD?"
scene catherineshower08c
show catherineshower08d
with dissolve
play sound "sounds/boymoan02.mp3"
mc "AH, FUCK!"
window hide
with fastflash
ck "Mmmh, yeah, pump that cream, [name], all over the place!"
scene catherineshower08a with dissolve
ck "Keep blasting, I want to see how POWERFUL your superhero monstercock is!"
scene catherineshower08c with dissolve
play sound "sounds/boymoan03.mp3"
mc "Damn it, RHAAAA!"
window hide
with fastflash
ck "Oooh, still more for ME?"
scene catherineshower08c
show catherineshower08d
with fastdissolve
play sound "sounds/boymoan.mp3"
ck "Now I wonder if you'll even have some left for my PUSSY..."
scene catherineshower08b with dissolve
mc "That was just a small appetizer. I'll show you how truly POWERFUL my cock is NOW!"
ck "You're still HARD? YES, show me how POWERFUL it is please!"
scene catherineshower09 with dissolve
ck "What? You're LIFTING ME UP ON YOUR SUPERHERO DONG???"
scene catherineshower10 with dissolve
mc "That's right, Catherine, and now I'm ready to IMPALE you on it!"
ck "You're going to fuck me MERCILESSLY? Using your POWERFUL MUSCLECOCK?"
scene catherineshower11 with dissolve
mc "You got that right!"
ck "THEN POUND IT INTO ME, I WANT TO FEEL IT TOTALLY FILLING ME UP!"
window hide

label CatherineShowerSlowx:  
hide cum
hide faster
hide slower
stop music
play music "sounds/womansex03.mp3"
show catherineshowerslowvideo behind catherineshowerfastvideo
$ renpy.pause(1.0, hard='True')
hide catherineshowerfastvideo
with dissolve
if catherineshowertold01x == False:
    mc "I'll fuck you slowly at first... So you get used to my MASSIVE size..."
    window hide
    $ catherineshowertold01x = True
show faster:
     xpos 1700 ypos 500     

call screen catherineshowerslowx()
screen catherineshowerslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatherineShowerFastx")

label CatherineShowerFastx:
hide cum
hide faster
hide slower
mc "And now get ready for some HEAVY POUNDING!"
window hide
show catherineshowerfastvideo behind catherineshowerslowvideo
$ renpy.pause(1.0, hard='True')
hide catherineshowerslowvideo
with dissolve
ck "Oh God, yes, YES, DO IT!"
stop music
play music "sounds/womansex04.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen catherineshowerfastx()
screen catherineshowerfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("CatherineShowerSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatherineShowerEndx")

label CatherineShowerEndx:
hide cum
hide faster
hide slower
ck "Please CUM! My pussy... It's getting numb. You're STRETCHING it so much..."
mc "Hang on, just a few more fifteen-inch stabs and..."
stop music
scene catherineshowercum01 with dissolve
hide catherineshowerfastvideo
hide catherineshowerslowvideo
play music "sounds/splooge02.mp3"
play channel1 "sounds/boyorgasm01.mp3"
mc "...AAAAH, here it COMES!"
window hide
with fastflash
ck "What? But... You just came TONS and you're spewing ANOTHER MEGA-LOAD???"
scene catherineshowercum02 with dissolve
mc "You'd better believe it! RHAAA!"
play sound "sounds/womancum01.mp3"
window hide
with fastflash
ck "You cum factories must have been so BLOATED!"
scene catherineshowercum03 with dissolve
mc "You got that right! Take some more OUNCES of my virile cum!"
window hide
with fastflash
ck "Pull out, my womb is gonna EXPLODE!"
scene catherineshowercum04 with dissolve
ck "AAAH, my stomach... It's distending like it's gonna BURST!"
window hide
with fastflash
mc "I'm TRYING to pull out but I'm STUCK!"
window hide
with fastflash
ck "FORCE IT OUT, I beg you!"
scene catherineshowercum05 with dissolve
stop music
stop channel1
play sound "sounds/splooge01.mp3"
play music "sounds/boymoan02.mp3"
mc "Ah, finally! And now I can liberally DOUSE your shower room!"
stop music
window hide
with fastflash
play sound "sounds/moan01.mp3"
ck "Oh my God, your baby-batter is CASCADING out of my pussy... Ooooh!"
scene catherineshowercum06 with dissolve
mc "Your pussy must have been cleaned up pretty good by now, I think we should probably call it a day. And call Honoka to clean up the shower room."
ck "Ooh... My poor pussy..."                                                                                         
jump CatherineGallery