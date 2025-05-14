label SheHulkGallery:
stop channel3
play channel3 "sounds/battlemusic.mp3"
scene shehulkbackground
show shehulkmaingallery at gallerypos01 with moveinleft
call screen galleryshehulk()
screen galleryshehulk():
    text "{font=Gui/Heroes Legend.ttf}Naughty She-Hulk{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryshehulk"), Jump ("MainGallery04")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryshehulk"), Jump ("SheHulkGalleryAnim")]
    
    if renpy.seen_image("hulkpreblow01"):
        imagebutton:
            focus_mask True
            idle "gallery/hulkgallery01.png" xpos 400 ypos 100
            hover "gallery/hulkgallery01.png"
            action Jump ("SheHulkGallery01")
    text "{font=Gui/Heroes Legend.ttf}Freedom Sex{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("hulkpreblow01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("SheHulkGallery01hint")

    if renpy.seen_image("frostcontrol01"):
        imagebutton:
            focus_mask True
            idle "gallery/hulkgallery02.png" xpos 750 ypos 100
            hover "gallery/hulkgallery02.png"
            action Jump ("SheHulkGallery02")
    text "{font=Gui/Heroes Legend.ttf}Hulk Mind Control{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("frostcontrol01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("SheHulkGallery02hint")
    text "{font=Gui/Heroes Legend.ttf}Villain{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytexthero02

    if renpy.seen_image("hulkjacuzzi02"):
        imagebutton:
            focus_mask True
            idle "gallery/hulkgallery03.png" xpos 1100 ypos 100
            hover "gallery/hulkgallery03.png"
            action Jump ("SheHulkGallery03")
    text "{font=Gui/Heroes Legend.ttf}Jacuzzi Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("hulkjacuzzi02") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SheHulkGallery")

    if renpy.seen_image("hulkgym05"):
        imagebutton:
            focus_mask True
            idle "gallery/hulkgallery04.png" xpos 1450 ypos 100
            hover "gallery/hulkgallery04.png"
            action Jump ("SheHulkGallery04")
    text "{font=Gui/Heroes Legend.ttf}Punching Bag{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("hulkgym05") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SheHulkGallery")

    if renpy.seen_image("hulkgym20"):
        imagebutton:
            focus_mask True
            idle "gallery/hulkgallery05.png" xpos 400 ypos 380
            hover "gallery/hulkgallery05.png"
            action Jump ("SheHulkGallery05")
    text "{font=Gui/Heroes Legend.ttf}Strength Training{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("hulkgym20") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("SheHulkGallery")

label SheHulkGallery01hint:
show shehulkmaingallery at gallerypos01
show hulkgallery01 at posgalleryhintpic
show shehulkgalleryhint01 at posgalleryhint
pause
hide shehulkgalleryhint01 
hide hulkgallery01
call screen galleryshehulk()
label SheHulkGallery02hint:
show shehulkmaingallery at gallerypos01
show hulkgallery02 at posgalleryhintpic
show shehulkgalleryhint02 at posgalleryhint
pause
hide shehulkgalleryhint02 
hide hulkgallery02
call screen galleryshehulk()

label SheHulkGalleryAnim:
stop channel3
play channel3 "sounds/sexy13.mp3"
call screen screenanimshehulk()
screen screenanimshehulk():
    modal True
    add "gallery/shehulkbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "shehulkanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "shehulkanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimshehulk"), SetVariable ("animcount", 1), Jump ("SheHulkGallery")]
    text "{font=Gui/Heroes Legend.ttf}      She-Hulk{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 6ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}42FF-28-42{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Cock Worship{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Blowjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/hulkanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimshehulk")]
    add "gallery/hulkanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimshehulk")]
            
label SheHulkGallery01:
stop channel3
stop music
scene hulkpreblow01 with dissolve
play music "sounds/sexy07.mp3"
mc "Err, How tall are you She-Hulk?"
hu "I've grown to... 6ft10. Let me get on my knees to your level."
scene hulkpreblow02 with dissolve
hu "Wow! I'm just eye level with your great big monster schlong!"
mc "All the better to suck m..."
$ hulkblowtalkslowx = False
$ hulkblowtalkfastx = False
$ hulkanalslowtalkx = False
$ hulkanalfasttalkx = False
play channel1 "sounds/boymoan02.mp3"
label HulkPreBlowSlowx: 
window hide
hide cum
hide faster
hide slower
show hulkpreblowslowvideo behind hulkpreblowfastvideo
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/blow01.mp3"
hide hulkpreblowfastvideo with dissolve
mc "Oh Fuck! You're gobbling me up so good!"
show nexticon:
     xpos 1750 ypos 1020        
show faster:
     xpos 1700 ypos 500     

call screen hulkpreblowslowx()
screen hulkpreblowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkPreBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowSlowax")

label HulkPreBlowFastx:
show hulkpreblowfastvideo behind hulkpreblowslowvideo
window hide
hide cum
hide faster
hide slower
$ renpy.pause(1.0, hard='True')
mc "Yeah, now slide your throat down my horsedick FASTER!"
window hide
hide hulkpreblowslowvideo with dissolve
show nexticon:
     xpos 1750 ypos 1020        
show slower:
     xpos 50 ypos 500     

call screen hulkpreblowfastx()
screen hulkpreblowfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkPreBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowSlowax")

label HulkBlowSlowax:
hide nexticon
hide hulkpreblowslowvideo
hide hulkpreblowfastvideo
scene hulkpreblow03

label HulkBlowSlowx:
$ hulkblowtalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowslowvideo behind hulkblowpovslowvideo
show hulkblowslowvideo behind hulkblowfastvideo
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/blow02.mp3"
hide hulkblowpovslowvideo
hide hulkblowfastvideo
with dissolve
if hulkblowtalkslowx == False:
    mc "Let me help you, I want to PUMMEL your throat!"
    $ hulkblowtalkslowx = True
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkblowslowx()
screen hulkblowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkBlowPOVSlowx")

label HulkBlowFastx:
$ hulkblowtalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowfastvideo behind hulkblowpovfastvideo
show hulkblowfastvideo behind hulkblowslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowpovfastvideo
hide hulkblowslowvideo
with dissolve
if hulkblowtalkfastx == False:
    mc "Oh Yeah, that's great... I'm so hard for you, hot She-Hulk!"
    $ hulkblowtalkfastx = True
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkblowfastx()
screen hulkblowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkBlowPOVFastx")

label HulkBlowPOVSlowx:
$ hulkblowtalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowpovslowvideo behind hulkblowslowvideo
show hulkblowpovslowvideo behind hulkblowpovfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowslowvideo
hide hulkblowpovfastvideo
with dissolve
if hulkblowtalkslowx == False:
    mc "Let me help you, I want to PUMMEL your throat!"
    $ hulkblowtalkslowx = True
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkblowpovslowx()
screen hulkblowpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkBlowSlowx")

label HulkBlowPOVFastx:
$ hulkblowtalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowpovfastvideo behind hulkblowfastvideo
show hulkblowpovfastvideo behind hulkblowpovslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowfastvideo
hide hulkblowpovslowvideo
with dissolve
window hide
if hulkblowtalkfastx == False:
    mc "Oh Yeah, that's great... I'm so hard for you, hot She-Hulk!"
    $ hulkblowtalkfastx = True
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkblowpovfastx()
screen hulkblowpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkBlowFastx")

label HulkBlowEndx:
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
mc "I'm getting close... Your sucking skills are just too much to..."
hide hulkblowfastvideo
hide hulkblowpovslowvideo
hide hulkblowslowvideo
hide hulkblowpovfastvideo
scene hulkblowcum01
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAAH, you're making me spill my sauce!"
window hide 
with fastflash
hu "GGllll..."
scene hulkblowcum02 with dissolve
mc "RHAAA! Take my spunk DEEP down your throat!"
window hide
with hpunch
mc "So damn GOOO-OOOOD!!!!"
scene hulkblowcum03 with dissolve
stop channel2
mc "AAAH, still NUTTING BIG TIME!!!"
window hide
with fastflash
hu "Cover my face with your SUPER-SPUNK!"
stop channel1
scene hulkblowcum04 with dissolve
play sound "sounds/panting.mp3"
hu "You're FILTHY! You just come and come, like a SEX MACHINE!"
mc "You're the one who made me blow SUPER-HARD, She-Hulk."
scene hulkblowcum05 with dissolve
hu "Now I want this MONSTERCOCK up my pussy! Get on the floor!"
mc "Uh oh..."
scene hulkprefuck14 with dissolve
hu "Let me stick this fuckstick where it belongs..."
scene hulkprefuck15 with dissolve
hu "Mmh, right there, it just fits perfectly..."

label HulkFuckSlowx:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckslowvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex06.mp3"
hu "UHH OOOH, I needed a HUGE cock so bad!"
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen hulkfuckslowx()
screen hulkfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkFuckHardSlowx")

label HulkFuckFastx:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckfastvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex06.mp3"
if age >= 20:
    hu "This MASSIVE HORSEDICK is sssooo good! AAAH!"
if age >= 18 and age <= 19:
    hu "This MASSIVE TEENAGE HORSEDICK is sssooo good! AAAH!"
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen hulkfuckfastx()
screen hulkfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkFuckHardFastx")

label HulkFuckHardSlowx:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckharderslowvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex05.mp3"
hu "I want it HARDER and DEEPER!"
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen hulkfuckharderslowx()
screen hulkfuckharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkFuckSlowx")

label HulkFuckHardFastx:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckharderfastvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex05.mp3"
window hide
if age >= 20:
    hu "Your MONSTERCOCK is drilling me so DEEP!!!"
if age >= 18 and age <= 19:
    hu "This MASSIVE TEENAGE HORSEDICK is sssooo good! AAAH!"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen hulkfuckharderfastx()
screen hulkfuckharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckHardSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkFuckFastx")

label HulkFuckEndx:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
hu "I want you to BLAST inside my snatch! NOW!"
window hide
$ renpy.pause(1.0, hard='True')
scene hulkfuckcum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play channel1 "sounds/boyorgasm01.mp3"
mc "Yeah, AAAAH, FUCK!"
window hide
with hpunch
hu "Give me MORE SPUNK [hero]!"
scene hulkfuckcum02 with dissolve
hu "You're FILLING ME UP! I've never been filled so much in my life!"
window hide
with hpunch
mc "Take my SUPER-SPUNK, SHE-HULK!"
play sound "sounds/moan05.mp3"
hu "Pull out and dump the rest on me, [hero]!"
scene hulkfuckcum03 with dissolve
stop channel2
play sound "sounds/splooge03.mp3"
hu "Cover my body in your scalding scum!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "FUCK YEAH! RHAAA!"
scene hulkfuckcum04 with dissolve
stop channel1
play sound "sounds/moan01.mp3"
hu "Mmmh, that was so nice of you... I really needed that."
mc "Happy to oblige."
scene hulkfuckcum05 with dissolve
hu "I hope you still have some cream left in your bull-balls. There's another hole that NEEDS to be filled!"
mc "I'm still ROCK-HARD for you, She-Hulk, don't you worry! Let me demonstrate my POWER!"
scene hulkfuckcum06 with dissolve
hu "Oooh, you're lifting me up with such ease!"
scene hulkfuckcum07 with dissolve
mc "That's cos I'm SUPER-STRONG, on top of being SUPER-HUNG!"
hu "Please FUCK me HARD in the ass! I NEED your young GIANT cock in there!!!"
scene hulkanalprefuck01 with dissolve
if age >= 20:
    hu "Don't hold back, I want ALL 15 inches of prime fuckmeat!"
if age >= 18 and age <= 19:
    hu "Don't hold back, I want ALL 15 inches of prime teen fuckmeat!"
scene hulkanalprefuck02 with dissolve
mc "Don't worry, I'll definitely make them fit, even if I have to FORCE them in."

label HulkAnalFuckSlowx:
$ hulkanalfasttalkx = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckslowvideo behind hulkanalfuckfastvideo
show hulkanalfuckslowvideo behind hulkanalfuckbackslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
if hulkanalslowtalkx == False:
    if age >= 20:
        hu "Mmmh, just like that... Your giant cock... in my ass..."
    if age >= 18 and age <= 19:
        hu "Mmmh, just like that... Your giant teenage cock... in my ass..."
    $ hulkanalslowtalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen hulkanalfuckslowx()
screen hulkanalfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkAnalFuckFrontSlowx")

label HulkAnalFuckFastx:
$ hulkanalslowtalkx = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckfastvideo behind hulkanalfuckslowvideo
show hulkanalfuckfastvideo behind hulkanalfuckbackfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckslowvideo
hide hulkanalfuckbackfastvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
if hulkanalfasttalkx == False:
    mc "That ass needs to be pounded HARDER and FASTER!"
    $ hulkanalfasttalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen hulkanalfuckfastx()
screen hulkanalfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkAnalFuckFrontFastx")

label HulkAnalFuckFrontSlowx:
$ hulkanalfasttalkx = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckbackslowvideo behind hulkanalfuckslowvideo
show hulkanalfuckbackslowvideo behind hulkanalfuckbackfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckslowvideo
hide hulkanalfuckbackfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
if hulkanalslowtalkx == False:
    if age >= 20:
        hu "Mmmh, just like that... Your giant cock... in my ass..."
    if age >= 18 and age <= 19:
        hu "Mmmh, just like that... Your giant teenage cock... in my ass..."
    $ hulkanalslowtalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkanalfuckbackslowx()
screen hulkanalfuckbackslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckSlowx")

label HulkAnalFuckFrontFastx:
$ hulkanalslowtalkx = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckbackfastvideo behind hulkanalfuckfastvideo
show hulkanalfuckbackfastvideo behind hulkanalfuckbackslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
if hulkanalfasttalkx == False:
    mc "That ass needs to be pounded HARDER and FASTER!"
    $ hulkanalfasttalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen hulkanalfuckbackfastx()
screen hulkanalfuckbackfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFastx")

label HulkAnalFuckEndx:
hide cum
hide assview
hide faster
hide slower
hide sceneicon
window hide
hu "* Puff * I... can't take it anymore, you're PULVERIZING my ass... Please fill it up NOW!"
hide hulkanalfuckbackfastvideo
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
hide hulkanalfuckbackslowvideo
scene hulkanalcum01
stop channel1
play channel1 "sounds/splooge01.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "There you go, my third MEGA-LOAD of the day! RHAAA!"
window hide 
with hpunch
hu "You're such a STALLION! You're cumming so much AGAIN!"
scene hulkanalcum02 with dissolve
play sound "sounds/moan05.mp3"
hu "Yes, Yes, I'm cumming too! Your spunk in my ass is making me EXPLODE!"
window hide
with fastflash
mc "CUM with me, She-HULK! RHAAA!"
scene hulkanalcum03 with dissolve
play sound "sounds/boymoan05.mp3"
mc "Take more, take ALL OF MY CUM, AAAH!"
window hide
with hpunch
play sound "sounds/moan04.ogg"
hu "AAAHHH! My ass is already full to the brim!"
scene hulkanalcum04 with dissolve
play sound "sounds/moan04.ogg"
stop channel1
stop channel2
hu "Mmmh, are you alright back there?"
play sound "sounds/panting.mp3"
mc "Rhhhhooo...."
hu "You poor thing, She-Hulk totally DRAINED your bull-balls. And now you're out of commission and need to go back to your bedroom..."
stop music
jump SheHulkGallery

label SheHulkGallery02:
stop channel3
stop music
play music "sounds/underworld.mp3"
scene frostcontrol01
ef "There she is. I have created an astral projection around her. She cannot see you, she is totally oblivious to her surroundings right now."
mc "Oh good, cos she's super-strong and can go berserk pretty easily."
scene frostcontrol02 with dissolve
ef "Indeed. Which is why you will have to face your own worst fears once I remove her projection. In order to control her, you must first learn to control your OWN MIND!"
mc "Err... And how do I do that?"
scene frostcontrol03 with dissolve
ef "You will feel the pain and torment inside your head. I will mentally guide you."
mc "Thanks God for that, it doesn't sound very ni..."
scene frostcontrol02 with dissolve
ef "But I'll also make sure to be several feet behind you when your training starts. I don't want any blood stains on my costume."
mc "Ah. So you're mentally predicting she's gonna beat me to a pulp then?"
scene frostcontrol03 with dissolve
ef "If she attacks you, use both your Super-Strength AND Mind Control to TAME HER!"
scene frostcontrol04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
ef "Are you ready?"
scene frostcontrol05 with dissolve
mc "Yeah. Hang on. Control my mind, use Super-Strength, control her mind. Yep, ready now!"
ef "NOW!"
scene frostcontrol06 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "Uh- oh..."
scene frostcontrol07 with dissolve
play sound "sounds/punch.mp3"
mc "FU-UUUCK! That did nothing against her superior strength, she still head-butted me!"
hu "AAAARRHH!"
scene frostcontrol08 with dissolve
play sound "sounds/punch.mp3"
mc "Put the shield back on please, Landlord! She's gonna tear me apart!"
play sound "sounds/hulkgrowl.mp3"
ef "* grunt * Fine, but for ONLY THIS ONCE TIME!"
scene frostcontrol09 with dissolve
play sound "sounds/panting.mp3"
mc "I don't want to do this, I can't, this is too hard!"
ef "Go back in there, you wimp! I will not tolerate your cowardice!"
mc "Gee, maybe I should have stayed neutral. I would be less bloodied."
scene frostcontrol10 with dissolve
mc "I have an idea. As usual with all my great ideas, it involves my ALPHA-COCK!"
ef "Whatever it takes, although I would prefer for your dick to remain intact. As your landlord, I am very proud of your tenant dong."
scene frostcontrol11 with dissolve
if age >= 20:
    mc "I will mesmerize her with the Super-Studliness of my ungodly phallus."
if age >= 18 and age <= 19:
    mc "I will mesmerize her with the Super-Studliness of my ungodly teenage phallus."
ef "Not as beautiful as I am, but I get where you're going."
mc "And then, I will be able to control her mind. With my COCK!"
scene frostcontrol02 with dissolve
ef "Interesting theory. It sure worked with Captain MILF when I turned into a monstrously-hung titan [age] years ago."
scene frostcontrol12 with dissolve
mc "And now, let's see how you react to THIS Super-Cock, She-Hulk!"
play sound "sounds/hulkgrowl.mp3"
mc "Oh, you're growling? You'll be MOANING soon when I'm CONTROLLING your mind! Remove the barrier Emma, I AM READY!"
scene frostcontrol13 with dissolve
hu "GRRRLLLL! RH????...."
mc "Yeah, yeah, that's right, now you're already subdued, aren't you?"
ef "Project your tormented mind onto hers to CONTROL her now, [hero]!"
mc "Alright..."
scene frostcontrol14 with dissolve
play channel1 "sounds/radiation02.mp3"
mc "AAAAH, it's... painful! MUST... FIGHT... THE PAIN!"
ef "And the torment. Don't forget the torment. Project all your dark feelings inside her mind, may the villain Force be with you!"
scene frostcontrol15 with dissolve
play sound "sounds/effort01.mp3"
mc "She's holding me tight... I need to resist while she's still confused about my cock!"
scene frostcontrol16 with dissolve
mc "And now... Transfer my TORMENT INTO HER MIND!"
stop channel1
play sound "sounds/magic.mp3"
mc "It's working! I'm a Super-Villain mind controller!"
scene frostcontrol17 with dissolve
mc "And now PRAISE MY COCK, She-Hulk!"
hu "AAARH! Ssso BIG, Master!"
mc "Damn right it's big. And so are my balls and they demand some WORSHIP from your tongue!"
play channel2 "sounds/lick01.ogg"
scene frostcontrol18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
ef "What the hell do you think you're doing?"
play sound "sounds/boymoan02.mp3"
mc "Errr, AAAAH! I'm getting my balls licked by She-Hulk, why do you ask?"
scene frostcontrol19 with dissolve
play sound "sounds/boymoan03.mp3"
mc "Oh God, she's sticking a finger up my arse, I didn't ask her to do that!"
ef "She's feeding on your emotions. POSITIVE emotions. You'd better get rid of them quickly, [name]!"
scene frostcontrol20 with dissolve
stop channel2
play sound "sounds/lick03.mp3"
mc "Uuuuh, she's going to make me..."
scene frostcontrol21 with dissolve
play channel2 "sounds/boyorgasm01.mp3"
mc "....COME, AAAAHHHHH!"
window hide
with fastflash
ef "That's TOO MUCH positive emotions!"
scene frostcontrol22 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "FUUU-UUUCK, she's grabbing my nuts!"
window hide
with hpunch
ef "I told you to be VILLAINOUS when you use Mind Control!"
scene frostcontrol23 with dissolve
mc "That's it, you cum-hungry whore, I'm gonna blow my wads directly onto your filthy green breasts, like a villain would do!"
window hide
with fastflash
ef "That's more like it!"
scene frostcontrol24 with dissolve
mc "RHAA, thake that, She-Hulk!"
window hide
with hpunch
if age >= 20:
    ef "You're taming her again, thanks to your endless supply of virile scum!"
if age >= 18 and age <= 19:
    ef "You're taming her again, thanks to your endless supply of virile teenage scum!"
hu "UUUUH..."
scene frostcontrol25 with dissolve
stop channel2
play sound "sounds/panting.mp3"
mc "Phew! I almost got my nuts squashed into pancakes by her..."
ef "That's because you used Mind Control to get your rocks off instead of using it to make your mind slave do EVIL things!"
scene frostcontrol26 with dissolve
mc "ALright, I get it now. I'm on the Super-Villain path and I should stick to it."
scene frostcontrol27 with dissolve
ef "Exactly. And with our combined forces, we shall RULE COCKHAM TOGETHER!"
mc "And then do what exactly?"
scene frostcontrol03 with dissolve
ef "Just go back to your compound, you clearly need more TRAINING before you are READY. Also, please reach Level 2 soon, you're too weak an assistant as it stands."
stop channel1
stop channel2
stop sound
stop music
jump SheHulkGallery

label SheHulkGallery03:
stop channel3
stop music
play music "sounds/sexy10.mp3"
scene hulkjacuzzi02 with dissolve
mc "The water is warm and I'm getting hotter by the minute..."
scene hulkjacuzzi03 with dissolve
hu "BIG COCK... NEED TO SEE IT!"
mc "Well come and get it then, She-Hulk..."
scene hulkjacuzzi04 with dissolve
hu "Me can't wait."
play sound "sounds/ripping.mp3"
mc "Yet another speedo to the garbage chute..."
scene hulkjacuzzi05 with dissolve
play sound "sounds/wow.mp3"
hu "So, so BIG!"
mc "That's right, Superhero Level TWO and Cock Size level two TOO!"
scene hulkjacuzzi06 with dissolve
play sound "sounds/lick01.ogg"
mc "Fuck yeah..."
scene hulkjacuzzi07 with dissolve
hu "ME gonna make you blow your NUT with my MOUTH in no time!"
mc "Oh, be my gu..."
stop channel1
play channel1 "sounds/blow02.mp3"
$ hulkjacuzziblowslowx = False

label HulkJacuzziBlowSlowx:
$ hulkjacuzziblowfastx = False
$ hulkjacuzziblowharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide nexticon
if hulkjacuzziblowslowx == False and hulkjacuzzistart:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslowx = True
window hide
show hulkjacuzziblowslowvideo behind hulkjacuzziblowfastvideo
show hulkjacuzziblowslowvideo behind hulkjacuzziblowslowpovvideo
show hulkjacuzziblowslowvideo behind hulkjacuzziblowharderslowvideo
pause 1.0
hide hulkjacuzziblowfastvideo
hide hulkjacuzziblowslowpovvideo
hide hulkjacuzziblowharderslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if hulkjacuzziblowslowx == False and hulkjacuzzistart == False:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslowx = True
    $ hulkjacuzzistart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowslowx()
screen hulkjacuzziblowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVSlowx")

label HulkJacuzziBlowFastx:
$ hulkjacuzziblowslowx = False
$ hulkjacuzziblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzziblowfastx == False:
    mc "Go on, get that cock nice and wet..."
    $ hulkjacuzziblowfastx = True
show hulkjacuzziblowfastvideo behind hulkjacuzziblowslowvideo
show hulkjacuzziblowfastvideo behind hulkjacuzziblowfastpovvideo
show hulkjacuzziblowfastvideo behind hulkjacuzziblowharderfastvideo
pause 1.0
hide hulkjacuzziblowslowvideo
hide hulkjacuzziblowfastpovvideo
hide hulkjacuzziblowharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowfastx()
screen hulkjacuzziblowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVFastx")

label HulkJacuzziBlowPOVSlowx:
$ hulkjacuzziblowfastx = False
$ hulkjacuzziblowharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide nexticon
if hulkjacuzziblowslowx == False:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslowx = True
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowslowvideo
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowfastpovvideo
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowharderpovslowvideo
pause 1.0
hide hulkjacuzziblowslowvideo
hide hulkjacuzziblowfastpovvideo
hide hulkjacuzziblowharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowslowpovx()
screen hulkjacuzziblowslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowSlowx")

label HulkJacuzziBlowPOVFastx:
$ hulkjacuzziblowslowx = False
$ hulkjacuzziblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzziblowfastx == False:
    mc "Go on, get that cock nice and wet..."
    $ hulkjacuzziblowfastx = True
window hide
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowslowpovvideo
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowfastvideo
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowharderpovfastvideo
pause 1.0
hide hulkjacuzziblowslowpovvideo
hide hulkjacuzziblowfastvideo
hide hulkjacuzziblowharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowfastpovx()
screen hulkjacuzziblowfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowFastx")

label HulkJacuzziBlowHarderSlowx:
if hulkjacuzziblowharderx == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharderx = True        
window hide
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowharderfastvideo
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowharderpovslowvideo
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderfastvideo
hide hulkjacuzziblowharderpovslowvideo
hide hulkjacuzziblowslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowharderslowx()
screen hulkjacuzziblowharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCumx")

label HulkJacuzziBlowHarderFastx:
if hulkjacuzziblowharderx == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharderx = True        
window hide
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowharderslowvideo
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowharderpovfastvideo
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderslowvideo
hide hulkjacuzziblowharderpovfastvideo
hide hulkjacuzziblowfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowharderfastx()
screen hulkjacuzziblowharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCumx")

label HulkJacuzziBlowHarderPOVSlowx:
if hulkjacuzziblowharderx == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharderx = True        
window hide
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowharderslowvideo
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowharderpovfastvideo
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderslowvideo
hide hulkjacuzziblowharderpovfastvideo
hide hulkjacuzziblowslowpovvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowharderpovslowx()
screen hulkjacuzziblowharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCumx")

label HulkJacuzziBlowHarderPOVFastx:
if hulkjacuzziblowharderx == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharderx = True        
window hide
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowharderpovslowvideo
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowharderfastvideo
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderpovslowvideo
hide hulkjacuzziblowharderfastvideo
hide hulkjacuzziblowfastpovvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowharderpovfastx()
screen hulkjacuzziblowharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCumx")

label HulkJacuzziBlowCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide nexticon
mc "Oh, it's sso good, I..."
scene hulkjacuzzi08 with dissolve
stop channel1
play sound "sounds/lick01.ogg"
hu "I don't want you to cum just yet!"
window hide
with hpunch
mc "Oh God, but..."
scene hulkjacuzzi09 with dissolve
play sound "sounds/slurp.mp3"
mc "Aaaah... I'm leaking pre-cum like crazy..."
hu "Then it's time for you to FUCK ME!"
scene hulkjacuzzi10 with dissolve
mc "You don't need to ask me twice! I'm gonna POUND you missionary-style, cos that is my MISSION!"
scene hulkjacuzzi11 with dissolve
play sound "sounds/wow.mp3"
hu "You're MAN-handling me again! This is making me feel so HORNY!"
mc "Then we're BOTH horny as hell! Now turn around, I want to play with that sweet pussy a bit!"
scene hulkjacuzzi12 with dissolve
play sound "sounds/moan02.mp3"
hu "Oooh! Your fingers..."
if age >= 20:
    mc "Yeah, get nice and wet for me... I can't wait to plunge my giant shaft inside that nice DEEP pussy of yours!"
if age >= 18 and age <=19:
    mc "Yeah, get nice and wet for me...I can't wait to plunge my giant teen shaft inside that nice DEEP pussy of yours!"
scene hulkjacuzzi13 with dissolve
mc "Enough foreplay, time for the MAIN PLAY!"
hu "Huuu! Fuck me please!"
scene hulkjacuzzi14 with dissolve
mc "That's what I'm about to do!"
hu "Your cock is so BIG! Even for me..."
play channel1 "sounds/womansex05.mp3"
$ hulkjacuzzifuckslowx = False

label HulkJacuzziFuckSlowx:
$ hulkjacuzzifuckfastx = False
$ hulkjacuzzifuckharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if hulkjacuzzifuckslowx == False and hulkjacuzzifuckstart:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslowx = True
window hide
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckfastvideo
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckslowpovvideo
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckharderslowvideo
pause 1.0
hide hulkjacuzzifuckfastvideo
hide hulkjacuzzifuckslowpovvideo
hide hulkjacuzzifuckharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if hulkjacuzzifuckslowx == False and hulkjacuzzifuckstart == False:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslowx = True
    $ hulkjacuzzifuckstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckslowx()
screen hulkjacuzzifuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVSlowx")

label HulkJacuzziFuckFastx:
$ hulkjacuzzifuckharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzzifuckfastx == False:
    hu "Just like that, but faster please!"
    $ hulkjacuzzifuckfastx = True
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckslowvideo
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckfastpovvideo
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckharderfastvideo
pause 1.0
hide hulkjacuzzifuckslowvideo
hide hulkjacuzzifuckfastpovvideo
hide hulkjacuzzifuckharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckfastx()
screen hulkjacuzzifuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVFastx")

label HulkJacuzziFuckPOVSlowx:
$ hulkjacuzzifuckharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if hulkjacuzzifuckslowx == False:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslowx = True
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckslowvideo
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckfastpovvideo
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckharderpovslowvideo
pause 1.0
hide hulkjacuzzifuckslowvideo
hide hulkjacuzzifuckfastpovvideo
hide hulkjacuzzifuckharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckslowpovx()
screen hulkjacuzzifuckslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckSlowx")

label HulkJacuzziFuckPOVFastx:
$ hulkjacuzzifuckharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzzifuckfastx == False:
    hu "Just like that, but faster please!"
    $ hulkjacuzzifuckfastx = True
window hide
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckslowpovvideo
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckfastvideo
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckharderpovfastvideo
pause 1.0
hide hulkjacuzzifuckslowpovvideo
hide hulkjacuzzifuckfastvideo
hide hulkjacuzzifuckharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckfastpovx()
screen hulkjacuzzifuckfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckFastx")

label HulkJacuzziFuckHarderSlowx:
if hulkjacuzzifuckharderx == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharderx = True        
window hide
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckharderfastvideo
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckharderpovslowvideo
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckslowvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderfastvideo
hide hulkjacuzzifuckharderpovslowvideo
hide hulkjacuzzifuckslowvideo
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
call screen hulkjacuzzifuckharderslowx()
screen hulkjacuzzifuckharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCumx")

label HulkJacuzziFuckHarderFastx:
if hulkjacuzzifuckharderx == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharderx = True        
window hide
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckharderslowvideo
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckharderpovfastvideo
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckfastvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderslowvideo
hide hulkjacuzzifuckharderpovfastvideo
hide hulkjacuzzifuckfastvideo
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
call screen hulkjacuzzifuckharderfastx()
screen hulkjacuzzifuckharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCumx")

label HulkJacuzziFuckHarderPOVSlowx:
if hulkjacuzzifuckharderx == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharderx = True        
window hide
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckharderslowvideo
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckharderpovfastvideo
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckslowpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderslowvideo
hide hulkjacuzzifuckharderpovfastvideo
hide hulkjacuzzifuckslowpovvideo
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
call screen hulkjacuzzifuckharderpovslowx()
screen hulkjacuzzifuckharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCumx")

label HulkJacuzziFuckHarderPOVFastx:
if hulkjacuzzifuckharderx == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharderx = True        
window hide
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckharderpovslowvideo
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckharderfastvideo
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckfastpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderpovslowvideo
hide hulkjacuzzifuckharderfastvideo
hide hulkjacuzzifuckfastpovvideo
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
call screen hulkjacuzzifuckharderpovfastx()
screen hulkjacuzzifuckharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCumx")

label HulkJacuzziFuckCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "I don't think I can last much longer without..."
stop channel1
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge02.mp3"
scene hulkjacuzzicum01 with dissolve
mc "...BLOWING MY NUT! AAAH!"
window hide
with hpunch
hu "Do it, me want your cum, LOTS of it!"
scene hulkjacuzzicum02 with dissolve
mc "Here it comes! RHAAA!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
hu "I'm feeling it! Feeling every MONSTER SHOT OF YOUR CREAM!!!"
scene hulkjacuzzicum03 with dissolve
mc "Well, get ready for MORE!!!"
window hide
with vpunch
play sound "sounds/moan06.ogg"
hu "ME WANT MORE! MUCH MORE!"
scene hulkjacuzzicum04 with dissolve
play sound "sounds/moan03.mp3"
mc "I'm delivering my baby-making ball-batter directly into your womb!"
window hide
with fastflash
hu "MY EGGS ARE GETTING DROWNED IN YOUR SPERMS!"
scene hulkjacuzzicum05 with dissolve
mc "Damn right, you're in MY HAREM now She-Hulk! AAAH!"
window hide
with hpunch
hu "AAAAH! YOU SO DEEEEEPPP! TOO MUCH CUM!"
window hide
with fastflash
mc "I should probably pull out, I think you've got enough of my spunk to make one hundred babies..."
scene hulkjacuzzicum06 with dissolve
stop channel2
mc "So I can give you the rest of my load, AAAH!"
window hide
with fastflash
hu "STILL SO MUCH? SUCH A STUD FOR ME!!!"
scene hulkjacuzzicum07 with dissolve
mc "For you, your STUDMASTER always comes that much!"
window hide
with fastflash
hu "That's why ME LOVES BEING YOUR HAREM SLAVE!"
scene hulkjacuzzicum08 with dissolve
stop channel1
stop music
play sound "sounds/panting.mp3"
mc "Phew! That was a MEGA-ORGASM FROM YOURS TRULY..."
if age >= 20:
    hu "You such a STALLION!"
if age >= 18 and age <= 19:
    hu "You such a TEENAGE STALLION!"
stop music
stop channel1
stop channel2
jump SheHulkGallery

label SheHulkGallery04:
stop music
stop channel3
stop channel1
scene hulkgym01 with fade
mc "* Nice outfit. Totally hugs her muscled booty... *"
scene hulkgym02 with dissolve
hu "What do you want me to do today?"
mc "Let's see how you deal with that punching bag..."
scene hulkgym16 with dissolve
mc "First, you should do some exercise to get yourself ready. Wrap your legs around the punching bag and do some ab crunches."
scene hulkgym17 with dissolve
hu "Like this?"
mc "Yeah, just like that. I'll watch from afar. And from above too."
window hide
play music "sounds/gymmusic.mp3"

label HulkGymLiftSidex:
hide topicon
hide sideicon
hide nexticon
show hulkgymliftsidevideo behind hulkgymlifttopvideo
$ renpy.pause(1.0, hard='True')
hide hulkgymlifttopvideo
with dissolve
mc "* Damn, she makes it look so easy. *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    

call screen hulkgymliftsidex()
screen hulkgymliftsidex():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftTopx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndx")

label HulkGymLiftTopx:
hide topicon
hide sideicon
hide nexticon
show hulkgymlifttopvideo behind hulkgymliftsidevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymliftsidevideo
with dissolve
mc "* Even better view even though I'm not actually there. *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymlifttopx()
screen hulkgymlifttopx():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftSidex")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndx")


label HulkGymLiftEndx:
hide topicon
hide sideicon
hide nexticon
mc "Now that she's getting all sweaty, I should use my Super-Senses and see her doing it in the nude... Ain't even gonna ask for permission from the player."

label HulkGymLiftSideNudex:
hide topicon
hide sideicon
hide nexticon
show hulkgymliftsidenudevideo behind hulkgymlifttopnudevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymlifttopnudevideo
with dissolve
mc "* Now we're talking. Naked She-Hulk... *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymliftsidenudex()
screen hulkgymliftsidenudex():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftTopNudex")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndNudex")

label HulkGymLiftTopNudex:
hide topicon
hide sideicon
hide nexticon
show hulkgymlifttopnudevideo behind hulkgymliftsidenudevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymliftsidenudevideo
with dissolve
mc "* Look at those abs flexing so HARD! *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymlifttopnudex()
screen hulkgymlifttopnudex():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftSideNudex")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndNudex")

label HulkGymLiftEndNudex:
stop music
scene hulkgym18 with dissolve
mc "I think you've trained enough, you can come down now."
scene hulkgym19 with dissolve
play sound "sounds/femalegrunt01.mp3"
hu "I liked this exercise, it's making my muscles SWELL UP!"
mc "I see that. Just stand behind the punching bag and wait for me to begin the PROPER training."
scene hulkgym03 with dissolve
mc "Okay, are you ready?"
hu "Ready for what?"
scene hulkgym04 with dissolve
play sound "sounds/punch.mp3"
mc "Well, for THAT!"
hu "What was that for?"
scene hulkgym03 with dissolve
mc "I see. Not enough for you?"
scene hulkgym05 with dissolve
play sound "sounds/punch.mp3"
mc "Then take this!"
scene hulkgym06 with dissolve
hu "I still don't get it. What are you trying to do exactly?"
mc "Push it back as hard as you can, I'll show you!"
scene hulkgym07 with dissolve
play sound "sounds/whoosh.mp3"
hu "Like this?"
scene hulkgym08 with dissolve
play sound "sounds/punch.mp3"
mc "Hey!"
scene hulkgym09 with dissolve
play sound "v032/ouch.mp3"
hu "What happened, are you alright? Why didn't you simply stop the punching bag?"
scene hulkgym10 with dissolve
mc "You... kind of hit it too hard. Let's do some stretching to get you more supple."
scene hulkgym11 with dissolve
hu "You're the one who told me to hit it hard, remember?"
mc "Yeah, sure, but I didn't expect you to be that strong... Now bend your body to the side..."
scene hulkgym12 with dissolve
hu "Like this?"
mc "Almost perfect. I'll give you a slight nudge..."
scene hulkgym13 with dissolve
mc "Right here..."
scene hulkgym14 with dissolve
play sound "sounds/punch.mp3"
hu "Don't touch my tits when I'm stretching, it makes me ANGRY!"
scene hulkgym15 with dissolve
play sound "v032/ouch.mp3"
mc "I.... I think I need to find a steak to put on my jaw. Thanks God we have a huge supply of them in the kitchen..."
hu "So it's over? It's YOUR fault! I'll do some stretching ON MY OWN while you nurse that well-deserved injury!"
stop music
stop channel1
stop channel2
jump SheHulkGallery

label SheHulkGallery05:
stop music
stop channel3
stop channel1
scene hulkgym20 with dissolve
mc "This is Superman's own Kryptonium kettlebell. Not to be confused with Kryptonite, which the weakling wouldn't be able to lift at all."
scene hulkgym21 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "Even I can barely move it and I'm Super-Strong. Level 2 to be more precise."
hu "Level 2?"
scene hulkgym22 with dissolve
play sound "sounds/panting.mp3"
mc "Yeah, on a scale that goes to 3 apparently. Now let's see how you fare with it. Try and pick it up."
scene hulkgym23 with dissolve
mc "It weighs 100 tons."
hu "Is that a lot?"
mc "Err, YEAH! It's the heaviest thing you'll find in this gym, so be careful with it, don't drop it or anything."
scene hulkgym24 with dissolve
hu "Oh, I thought it would be heavier that that."
mc "What do you mean?"
scene hulkgym25 with dissolve
hu "Well, it's like, super-light really."
mc "You're kidding me, right?"
scene hulkgym26 with dissolve
hu "No. Look, I can lift it easily with just one arm."
mc "What the????"
scene hulkgym27 with dissolve
hu "I bet I could even crush it in my hand."
play sound "sounds/femalegrunt01.mp3"
mc "I doubt that. Kryptonium is unbreakable."
scene hulkgym28 with dissolve
play sound "sounds/bonecrack.mp3"
hu "SHe-Hulk can BREAK anything she wants!"
mc "Err, yeah, I see that."
scene hulkgym29 with dissolve
mc "Uh oh, you droppped it now..."
scene hulkgym30 with dissolve
play sound "v06/thump.mp3" volume 2.0
mc "The whole building is SHAKING!!!"
scene hulkgym10 with dissolve
mc "Damn, you almost BROKE THE FLOOR, you've got to be more careful."
scene hulkgym31 with dissolve
hu "But I feel so GOOD! I think my muscles are..."
scene hulkgym32:
    subpixel True
    zoom 1 xpos -0.03 ypos -0.03
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/womangroan.mp3"
hu "...growing!"
mc "Damn!"
scene hulkgym33a:
    subpixel True
    zoom 0.5
    ease 8.0 zoom 1.0 xpos -0.3 ypos -0.2    
$ renpy.pause(4.0, hard='True') 
with dissolve
mc "Yeah, those biceps are definitely BIGGER and even more MENACING!"
scene hulkgym33b with dissolve
mc "* And they look even better with Super-Senses activated, he he... *"
mc "That's it, I want to compare our muscled bodies, let's pose in front of the mirror, She-Hulk!"
hu "Alright, but you might not appreciate the DIFFERENCE between us two, I'm warning you!"
scene hulkgym34 with dissolve
mc "* Damn, she's right, she's twice as big as I am... I feel like a weakling next to her... *"
scene hulkgym35 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "Okay, you're asking for it, MAXIMUM MUSCLE FLEX!!!"
hu "Not bad, [name], but you still have a long way to go to reach MY size."
scene hulkgym36 with dissolve
mc "When I level up to Super-Hero Level 03, you'll see!"
hu "Maybe, but right now, my muscles feel like they're on level TEN at least!"
scene hulkgym37:
    subpixel True
    zoom 1 xpos -0.03 ypos -0.03
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
hu "I mean, just look at my arms. Aren't they just ENORMOUS? Doesn't it make you want to KISS THEM?"
mc "I..."
scene hulkgym38:
    zoom 0.5
with dissolve
play sound "sounds/kiss.mp3"
mc "Yes, I just NEED to kiss those MASSIVE muscles!"
scene hulkgym38:
    subpixel True
    zoom 0.5
    ease 8.0 zoom 1.0 xpos -0.4 ypos -0.4 
with fastdissolve
play sound "sounds/kiss.mp3"
$ renpy.pause(4.0, hard='True') 
play sound "sounds/kiss.mp3"
hu "Go ahead... And LICK them too."
scene hulkgym39 with dissolve
hu "Keep going, there's some MUSCLE SWEAT that needs to be LICKED UP!"
play sound "sounds/lick02.mp3"
scene hulkgym40 with dissolve
hu "You like doing this don't you? Even though you're my harem Master..."
play sound "sounds/lick03.mp3"
mc "I... err..."
scene hulkgym41 with dissolve
hu "It looks like worshipping my muscles is making you horny, [name]..."
mc "Err... No! I mean, yes. I guess."
hu "You'd better leave. What if somebody sees you like that in the gym? Your reputation would take a big blow..."
mc "I guess you're right... I'd better leave, there are no more renders to this scene anyway."
stop music
stop channel1
stop channel2
jump SheHulkGallery
