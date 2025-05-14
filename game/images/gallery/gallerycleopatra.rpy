label CleopatraGallery:
stop channel3
play channel3 "v041/egyptianmood.mp3"
scene cleobackground
show cleomaingallery at gallerypos01 with moveinleft
call screen gallerycleo()
screen gallerycleo():
    text "{font=Gui/Heroes Legend.ttf}Naughty Cleopatra{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerycleo"), Jump ("MainGallery05")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerycleo"), Jump ("CleopatraGalleryAnim")]
    
    if renpy.seen_image("laraegypt20"):
        imagebutton:
            focus_mask True
            idle "gallery/cleogallery01.png" xpos 400 ypos 100
            hover "gallery/cleogallery01.png"
            action Jump ("CleopatraGallery01")
    text "{font=Gui/Heroes Legend.ttf}Slave Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("laraegypt20") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("CleopatraGallery")

label CleopatraGalleryAnim:
stop channel3
play channel3 "v041/egyptianmood.mp3"
call screen screenanimcleo()
screen screenanimcleo():
    modal True
    add "gallery/cleobackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "cleoanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "cleoanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimcleo"), SetVariable ("animcount", 1), Jump ("CleopatraGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Cleopatra{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 38+2000{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft8{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}38DD-24-40{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Cock Worship{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Slave Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/cleoanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimcleo")]
    add "gallery/cleoanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimcleo")]
            
label CleopatraGallery01:
stop music
stop channel3
play music "v041/egyptianmood.mp3"
scene laraegypt01 with fade
mc "Oh god, it's sssooo hot. Are we there yet?"
lc "Yes indeed, we have arrived. This must be the temple of Titi-Khok. Queen Cleopatra used it as a private beauty parlor where she would get pampered by her slaves."
scene laraegypt02 with dissolve
mc "Finally! It's like, super-hot in this desert."
lc "I did warn you, didn't I?"
scene laraegypt03 with dissolve
mc "Look, they even have an indoors swimming pool! Last one in is a chicken-shit superhero adventurer!"
lc "[hero], be careful! I didn't have time to give my speech and warn you about pitfalls and snares!"
scene laraegypt04 with dissolve
mc "That's just boring, I NEED to cool down anyway! Geronimo!"
play sound "sounds/diving.mp3"
lc "Oh dear, I should check the time. It might be happening soon."
scene laraegypt05 with dissolve
mc "What's happening? The water is clear and I don't see no sperm-tacle around me, it's safe, I'm telling you!"
lc "I am referring to the apparition of the ghost of Queen Cleopatra."
mc "Ghosts? Come on! They, like, barely exist at all."
lc "Cleopatra was killed right inside this temple by her husband Mark-Anthony. Nobody knows why he got so enraged..."
scene laraegypt06 with dissolve
lc "And it is time for the Queen to appear and seek her vengeance according to my notes, you'd better get out of the water NOW, [name]!"
mc "Pff, I ain't scared of nobo.."
play channel1 "sounds/jacuzzi.mp3"
scene laraegypt07 with dissolve
mc "What's going on, the water is... boiling behind me!"
lc "I told you, when will you listen, it's HER!"
mc "Damn, just when I was cooling down a bit..."
scene laraegypt08 with dissolve
play sound "sounds/healing.mp3"
mc "What the hell is this thing coming out of the water???"
lc "That's her crown. And the Jewel of the Mind Slaves is right there, I see it!"
mc "Ok, I'll try and grab it then and we can get the hell out of..."
stop music
play music "v041/egyptian.mp3"
scene laraegypt09 with dissolve
mc "She's rising from the water! And what a pair of titties!"
scene laraegypt10:
    subpixel True
    ypos -1.0
    ease 8.0 ypos 0.0
with dissolve
$ renpy.pause(6.0, hard='True')
mc "And what a spectacular nose! I am in awe of her pharaonic beauty!"
scene laraegypt11 with dissolve
stop channel1
qc "Who are you? And how dare you be in my regal presence?"
lc "We are advent..."
scene laraegypt12 with dissolve
qc "Is that you, my beloved slave, Mamm-Hoth-Khok?"
lc "She doesn't seem to be hearing me....Maybe she can hear you, Mamm-Hoth-Khok was her favorite male slave, so just say yes [name]!"
scene laraegypt13 with dissolve
mc "Sure, it's me, my Queen. Mammoth...err...Cock."
qc "You have come to please your Queen again? Oh, how long I have waited for this glorious day!"
scene laraegypt14 with dissolve
mc "Yeah, same here. Like 2000 years I think."
lc "Get her to take her crown off if you can!"
scene laraegypt15 with dissolve
lc "There's an upright Egyptian coffin. I wonder who could have been buried here..."
scene laraegypt16 with dissolve
qc "Show your Queen what she's been longing for all these millenia..."
mc "Alright! Here we go, I'm getting hard as a PYRAMID for you, my Queen!"
scene laraegypt17 with dissolve
stop music
play music "sounds/sexy14.mp3"
qc "Mmh, your divine rod is even BIGGER than I remember! And so are your young muscles, my beloved slave..."
mc "Err, yeah, I've been training for the last centuries and practising jelqing on a regular basis. Why don't you take that cumbersome crown off so we can get to the SWEE-EE-ET queen-slave love."
scene laraegypt18 with dissolve
qc "You know how to talk to your Queen, Mamm-Hoth-Khok. I hope you remained FAITHFUL to her during these long millenia."
mc "Oh yeah, like, totally."
scene laraegypt19 with dissolve
qc "Your Queen is ready, come and RAVISH her body, like you used to..."
scene laraegypt20 with dissolve
play sound "sounds/slurp.mp3"
qc "Drink my royal milk, it will make you even STRONGER."
scene laraegypt21 with dissolve
play sound "sounds/moan02.mp3"
qc "Oooh, you are such an adorable slave for your Queen!"
scene laraegypt22 with dissolve
play sound "sounds/moan03.mp3"
qc "You know how to play with my pussy, you haven't lost your sensual touch! AAAAH!"
scene laraegypt23:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
play sound "sounds/moan01.mp3"
pause
mc "I also know how to play with those heavy funbags, my Queen..."
qc "Oooh! Carry over to the edge of the pool and FUCK ME, Mamm-Hoth-Khok!"
scene laraegypt24 with dissolve
play sound "sounds/wow.mp3"
qc "By the beak of Horus, your love muscle is so HUGE!"
mc "All the better to please you, my Queen!"
scene laraegypt25 with dissolve
play sound "sounds/doorsqueak.mp3"
lc "Blimey, that coffin just opened by itself and there's a mummy inside it. I don't like that."
scene laraegypt26 with dissolve
play sound "sounds/hulkgrowl.mp3"
lc "It be must Mamm-Hoth-Khok, judging by the size of this mummy's bulge! And he's NOT happy!"
scene laraegypt27 with dissolve
play sound "sounds/punch.mp3"
lc "Get that jewel as soon as you have the opportunity, [hero], I'll try and fend him off for as long as I can!"
scene laraegypt28 with dissolve
qc "Just fuck me, I can't wait any longer, STICK THAT MIGHTY SLAVE PILLAR INSIDE YOUR QUEEN NOW!"
mc "Err... Right now, I'm kind of busy, she's demanding some HOT SEX, and she wants it RIGHT NOW!"
scene laraegypt29 with dissolve
play sound "sounds/moan02.mp3"
qc "You're DROOLING lots of precum all over your Queen's tummy, this is just so NASTY!"
mc "You ain't see nothing yet my Queen, Mamm-Hoth-Khok is going to take you to the Other World!"
$ cleopoolfuckslowx = False

label CleoPoolFuckSlowx:
$ cleopoolfuckfastx = False
window hide
show cleopoolslowvideo behind cleopoolfastvideo
show cleopoolslowvideo behind cleopoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide cleopoolfastvideo
hide cleopoolpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckslowx == False:
    $ cleopoolfuckslowx = True
    qc "Mamm-Hoth-Khok... Your dong is divinely HUGE!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleopoolfuckslowx()
screen cleopoolfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckPOVSlowx")

label CleoPoolFuckFastx:
$ cleopoolfuckslowx = False
window hide
show cleopoolfastvideo behind cleopoolslowvideo
show cleopoolfastvideo behind cleopoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide cleopoolpovfastvideo
hide cleopoolslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckfastx == False:
    $ cleopoolfuckfastx = True    
    qc "Give it to me hard and good, my beloved slave, your Queen demands it!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleopoolfuckfastx()
screen cleopoolfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckPOVFastx")

label CleoPoolFuckPOVSlowx:
$ cleopoolfuckfastx = False
window hide
show cleopoolpovslowvideo behind cleopoolslowvideo
show cleopoolpovslowvideo behind cleopoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide cleopoolpovfastvideo
hide cleopoolslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckslowx == False:
    $ cleopoolfuckslowx = True
    qc "Mamm-Hoth-Khok... Your dong is divinely HUGE!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleopoolpovfuckslowx()
screen cleopoolpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckSlowx")

label CleoPoolFuckPOVFastx:
$ cleopoolfuckslowx = False
window hide
show cleopoolpovfastvideo behind cleopoolfastvideo
show cleopoolpovfastvideo behind cleopoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide cleopoolfastvideo
hide cleopoolpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if cleopoolfuckfastx == False:
    $ cleopoolfuckfastx = True    
    qc "Give it to me hard and good, my beloved slave, your Queen demands it!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleopoolpovfuckfastx()
screen cleopoolpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckFastx")

label CleoPoolFuckEndx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
qc "Don't stop thrusting, I've been waiting for this too long!"
scene laraegypt30 with dissolve
stop channel1
lc "Get the jewel now! This mummy is much tougher than I thought and he seems real HORNY too!"
scene laraegypt31 with dissolve
mc "I... can't reach..."
scene laraegypt32 with dissolve
qc "What can't you reach, my beloved? Your Queen will make you reach a mighty orgasm, do not worry!"
scene laraegypt33 with dissolve
mc "Alright, let's switch position then, I'm gonna give it to you HARD and DEEP with your legs spread WIDE OPEN, so get ready for the pounding of the MILLENIUM, Queen Cleopatra!"
qc "Mmh, I can't wait to feel your immense pole RAVISH my horny pussy!"
$ cleosidefuckslowx = False

label CleoSideFuckSlowx:
$ cleosidefuckfastx = False
window hide
show cleosideslowvideo behind cleosidefastvideo
show cleosideslowvideo behind cleosidepovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex06.mp3"
hide cleosidefastvideo
hide cleosidepovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckslowx == False:
    $ cleosidefuckslowx = True
    qc "Yes, fuck like an Egyptian!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleosidefuckslowx()
screen cleosidefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckPOVSlowx")

label CleoSideFuckFastx:
$ cleosidefuckslowx = False
window hide
show cleosidefastvideo behind cleosideslowvideo
show cleosidefastvideo behind cleosidepovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide cleosidepovfastvideo
hide cleosideslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckfastx == False:
    $ cleosidefuckfastx = True    
    qc "You are more godly than Osiris the way you fuck me so DEEP!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleosidefuckfastx()
screen cleosidefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckPOVFastx")

label CleoSideFuckPOVSlowx:
$ cleosidefuckfastx = False
window hide
show cleosidepovslowvideo behind cleosideslowvideo
show cleosidepovslowvideo behind cleosidepovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex06.mp3"
hide cleosidepovfastvideo
hide cleosideslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckslowx == False:
    $ cleosidefuckslowx = True
    qc "Yes, fuck like an Egyptian!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleosidepovfuckslowx()
screen cleosidepovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckSlowx")

label CleoSideFuckPOVFastx:
$ cleosidefuckslowx = False
window hide
show cleosidepovfastvideo behind cleosidefastvideo
show cleosidepovfastvideo behind cleosidepovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide cleosidefastvideo
hide cleosidepovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if cleosidefuckfastx == False:
    $ cleosidefuckfastx = True    
    qc "You are more godly than Osiris the way you fuck me so DEEP!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleosidepovfuckfastx()
screen cleosidepovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckFastx")

label CleoSideFuckEndx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Get ready for my mighty load, my Queen!"
qc "Pump me FULL of your seed, I don't care if Mark-Anthony finds out, I just want your BABY!"
scene laraegyptcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "Then here it CUMS, RHAAA!"
window hide
with fastflash
qc "By the scepter of Osiris, I can feel your seed BLASTING inside me!"
scene laraegyptcum02 with dissolve
mc "Wait, there's MORE for you, AAAH!"
window hide
with fastflash
qc "With such a load, I will surely get pregnant and finally have a worthy heir to my Egyptian throne!"
scene laraegyptcum03 with dissolve
qc "Just keep filling me up, make sure you KNOCK ME UP GOOD!"
mc "Damn right, I'm got tons more in store, don't you worry about that!"
scene laraegyptcum04 with dissolve
mc "Like So, RHAAA!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
qc "AAAH, your giant spunk shots are making me cumming too!"
scene laraegyptcum05 with dissolve
mc "* I just need to keep pumping and keep her distracted, AAAH! *"
window hide
with vpunch
qc "You're filling me up with so much yummy slave spunk, my royal belly looks pregnant already!"
stop channel1
scene laraegypt36 with dissolve
play sound "sounds/hulkgrowl.mp3"
lc "Just get that jewel, this mummy is getting too close for comfort!"
scene laraegypt37 with dissolve
mc "I definitely don't want to see any NTR mummy shit, so I'm gonna grab it right now. Hang on, there are several jewels on this crown, which one is it?"
mc "Damn it, I just can't remember anything... Gotta focus..."
play sound "sounds/dream.mp3"
scene laraegyptrecall with dissolve
lc "... This sparkling green jewel would be immensely dangerous if it fell into..."
mc "Ah yeah, I remember, its's the GREEN one!"

label JewelChoicex:
scene laraegypt31 with dissolve
menu:
    "Pick the Green jewel":
        mc "I have the jewel now, Lara!"
        jump CleoNextx
    "Pick the Blue Jewel":
        scene laraegypt38 with dissolve
        mc "I have the jewel now, Lara!"
        jump CleoNextWrongx

label CleoNextWrongx:
scene laraegypt50 with dissolve
qc "Who is this \"Lara\" that you speak of? Have you been unfaithful to your Queen?"
mc "Err... Nobody, I swear!"
scene laraegypt53 with dissolve
qc "I curse you, impostor!"
mc "No, please what did I do?"
lc "You picked the WRONG jewel!"
scene laraegypt54 with dissolve
play sound "sounds/healing.mp3"
"You have been cursed by Queen Cleopatra and turned into her zombie sex slave."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
stop channel1
stop music
jump CleopatraGallery

label CleoNextx:
scene laraegypt50 with dissolve
qc "Who is this \"Lara\" that you speak of? Have you been unfaithful to your Queen?"
scene laraegypt51 with dissolve
stop music
play music "v041/egyptianmood.mp3"
lc "Let's get out of here NOW!"
mc "I think it's a good idea, she just saw the mummy and she's coming to her senses it seems..."
scene laraegypt52 with dissolve
lc "Run, [name], run!"
mc "But I forgot my thong and I'm all naked!"
lc "We'll get you a new one back in the gallery! Run faster!"
stop channel1
stop music
jump CleopatraGallery
