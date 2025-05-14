label IvyGallery:
stop channel3
play channel3 "v03/ivymusic.mp3"
scene ivybackground
show ivymaingallery at gallerypos01 with moveinleft
call screen galleryivy()
screen galleryivy():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Poison Ivy{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryivy"), Jump ("MainGallery05")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryivy"), Jump ("IvyGalleryAnim")]
    
    if renpy.seen_image("robinson01"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery01.png" xpos 400 ypos 100
            hover "gallery/poisongallery01.png"
            action Jump ("IvyGallery01")
    text "{font=Gui/Heroes Legend.ttf}Poison Ivy Combat{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("robinson01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("IvyGallery")

    if renpy.seen_image("ivyhumcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery02.png" xpos 750 ypos 100
            hover "gallery/poisongallery02.png"
            action Jump ("IvyGallery02")
    text "{font=Gui/Heroes Legend.ttf}Femdom Tease{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("ivyhumcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("IvyGallery")

    if renpy.seen_image("ivyprefuck01"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery03.png" xpos 1100 ypos 100
            hover "gallery/poisongallery03.png"
            action Jump ("IvyGallery03")
    text "{font=Gui/Heroes Legend.ttf}Maledom Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("ivyprefuck01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("IvyGallery")

    if renpy.seen_image("ivyprefuckharem06"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery04.png" xpos 1450 ypos 100
            hover "gallery/poisongallery04.png"
            action Jump ("IvyGallery04")
    text "{font=Gui/Heroes Legend.ttf}Harem Doggy{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("ivyprefuckharem06") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("PoisonGallery04hint")

    if renpy.seen_image("ivypretitfuckharem01"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery05.png" xpos 400 ypos 380
            hover "gallery/poisongallery05.png"
            action Jump ("IvyGallery05")
    text "{font=Gui/Heroes Legend.ttf}Harem Titfuck{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("ivypretitfuckharem01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("PoisonGallery05hint")

label PoisonGallery04hint:
show ivymaingallery at gallerypos01
show poisongallery04 at posgalleryhintpic
show poisongalleryhint04 at posgalleryhint
pause
hide poisongalleryhint04
hide poisongallery04
call screen galleryivy()

label PoisonGallery05hint:
show ivymaingallery at gallerypos01
show poisongallery05 at posgalleryhintpic
show poisongalleryhint04 at posgalleryhint
pause
hide poisongalleryhint04
hide poisongallery05
call screen galleryivy()

label IvyGalleryAnim:
call screen screenanimivy()
screen screenanimivy():
    modal True
    add "gallery/ivybackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "ivyanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "ivyanimnak" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "ivyanimtit" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimivy"), SetVariable ("animcount", 1), Jump ("IvyGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Poison Ivy{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 22{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft7{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}32E-22-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Femdom{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Titfucking/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    add "gallery/ivyanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimivy")]
    add "gallery/ivyanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimivy")]
    if quest05end:
        add "gallery/ivyanim03.png" xpos 1340 ypos 800
        button:
            xpos 1340
            ypos 800
            xysize(100, 100)        
            action [SetVariable ("animcount", 3), Show ("screenanimivy")]
            
label IvyGallery01:
stop channel3
stop sound
scene robinson01
play music "v03/parkambience.mp3"
mc "So, let's look for some sex crime. * Damn, look at that hot chick jogging our way... *"
sg "Fine. What about this derelict greenhouse over there? It looks out of place..."
scene robinson02 with dissolve
mc "What greenhouse?"
sg "The one over there. The OTHER WAY, [name]!"
scene robinson03 with dissolve
mc "Err, what?"
scene robinson04 with dissolve
mc " *She's smiling at me...*"
sg "You're NOT listening to me!"
scene robinson05 with dissolve
mc "Sure, sure. The... greenhouse."
sg "You're not looking at it! You're just looking at that girl's big tits! That's the only thing you boys care about!"
scene robinson06 with dissolve
mc "What girl?"
sg "Don't try and pretend I didn't see you ogle her. I'm sick and tired of girls who get all the attention just because they have a bigger rack than mine!"
scene robinson07 with dissolve
mc "You rack is... just fine, Linda, I promise. I was just... distracted for a moment. But ok, let's investigate this greenhouse."
sg "Umpf! I don't feel like I'm getting any proper training from YOU!"
mc "I'll show you! We'll go there and we'll fight some SEX CRIME together!"

scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
show ivy01 with moveinleft
show ivy01:
    breathe
pi "Who are you? I didn't invite you HERE!"
mc "We're SUPERHEROES! And my specific job is to fight the scourge of SEX CRIME in this city! And you're, like, topless, which I believe is probably against the law."
hide ivy01
show ivy04
with dissolve
pi "The only LAW I obey is the MOTHER EARTH LAW! To be ONE with Mother Nature, in all its GLORIOUS BEAUTY!"
sg "She's just a hippy I think. There were a few in Smallcoxville and they smoked some disgusting stuff so I put them in jail."
hide ivy04
show ivy03
with dissolve
pi "The history of Humanity, people against people, WAR, DESTRUCTION OF OUR PLANET, you ALL deserve to be in jail! You all deserve to DIE!"
mc "Now let's all calm down here. I'll forgive your...err... toplessness, cos I'm a nice guy and all but..."
sg "You're defending her because she's got big boobs! But she's a fucking FREAK who lives in a DUMP!"
hide ivy03
show ivy05
with dissolve
pi "How dare you call the only plant paradise left in this filthy town a dump!"
sg "It is a DUMP! And I bet you're a Super-Villainess!"
window hide
play sound "v03/rumble.mp3"
hide ivy05
show ivy06
with dissolve
hide ivy06
show ivy07
with dissolve
hide ivy07
show ivy08
with dissolve
mc "What the??? Oh shit..."
sg "I KNEW it! Supergirl will show her the might of the Cockham League of Justice!"
hide ivy08
show ivy09
with dissolve
play sound "sounds/whoosh.mp3"
sg "Take that, MUTANT FREAK!"
mc "Hang on there for a moment, Sup..."
play sound "v03/rumble.mp3"
scene ivy10 with dissolve
pi "My venomous snapping friends will take care of you, Supergirl!"
mc "[hero] to the rescue!"
scene ivy11 with dissolve
play sound "sounds/bonecrack.mp3"
sg "AAAh, it bit me! Right on my sensitive nipple too!"
scene ivy12 with dissolve
mc "Stop biting Supergirl, Poison Ivy!"
pi "You desecrated my paradise with your presence, now you must DIE!"
scene ivy13 with dissolve
play sound "sounds/bonecrack.mp3"
mc "I'm gonna rip those creatures off your back! And get them off my back too..."
pi "Noooo, my Preciouses, my Preciouses!"
mc "I think I'll add of your carnivorous vines to my inventory, thank you very much!"
scene ivy14 with dissolve
play sound "sounds/punch.mp3"
pi "I will avenge you, my Preciouses!"
mc "Ouch, not thank you very much for that!"
scene ivy15 with dissolve
mc "She's escaping, but it's probably for the best, I need to tend to Supergirl..."
sg "Uuuhhh... I can't stand up..."
scene ivy16 with dissolve
sg "I feel... weak and tired..."
mc "The toxins must be starting to act, despite your Super-Resistance."
sg "I... I can't fight them, they are too strong!"
scene ivy17 with dissolve
sg "What... what are you doing?"
mc "There is no time to waste, I must suck the poison out or you'll probably die!"
scene ivy18 with dissolve
play sound "sounds/slurp.mp3"
sg "But... You're sucking right on my poor little nipple..."
scene ivy19 with dissolve
play sound "v03/spit.mp3"
mc "And now I spit it out..."
sg "Eew..."
scene ivy18 with dissolve
play sound "sounds/slurp.mp3"
sg "Again? But..."
scene ivy19 with dissolve
play sound "v03/spit.mp3"
mc "I need to suck it ALL out."
scene ivy20 with dissolve
sg "I feel... much better. Thank you so much, [name]... You saved my life. Probably."
mc "Let's get out of this gallery before she comes back."
stop channel2
stop channel1
stop music
jump IvyGallery

label IvyGallery02:
stop channel3
stop music
play music "v03/fightmusic.mp3"
scene ivyfight01a with dissolve
mc "I'm ready, Poison Ivy! And I'll defeat you, just like last time!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene ivyfight02a with dissolve
mc "* She's coming on fast, I need to use my SUPERPOWERS QUICK! *"
scene ivyfight03a with dissolve
play sound "sounds/whoosh.mp3"
mc "* Damn, she's SUPER-FAST! *"
scene ivyfight04a with dissolve
play sound "sounds/punch.mp3"
if mcagility == 1:
    mc "* And I'm not FAST ENOUGH! *"
if mcagility >= 2:
    mc "* And I'm not FAST ENOUGH! Even with Level 2 Super-Agility! *"
scene ivyfight05a with dissolve
stop music
pi "Pff, that was too easy. Your cock might be massive, but it's USELESS against me!"
mc "Err, how about we make it best of three?"
scene ivyfight06a with dissolve
play sound "sounds/bonecrack.mp3"
pi "Feed on his MEAT, my carnivorous familiars!"
mc "AAAAH, not my sensitive cock!"
scene ivyfight07a with dissolve
pi "And now for your final gasp of air... Enjoy the view!"
play sound "sounds/panting.mp3"
mc "Uuuuh..."
scene ivyfight08a with dissolve
play sound "v03/rumble.mp3"
pi "Mmmh, now that he's passed out, let's have some FUN with his MASSIVE DONG! You can leave, my familiars..."
play music "sounds/sexy07.mp3"
scene ivyfight09a with dissolve
pi "Let's have a peak, he clearly won't mind, HA HA HA!"
scene ivyfight08 with dissolve
pi "Even soft, it's really BIG. And to think he's only [age]... Let's get some STEEL in it!"
scene ivyfight09 with dissolve
pi "That's better, now the REAL fun can begin!"
scene ivypretwerk01 with dissolve
pi "Mmmh, his balls are so MASSIVE. I'm gonna get a lot of seedjuice out of them!"
scene ivypretwerk02 with dissolve
pi "He deserves a scent of my moist snatch. That might even revive him a little bit!"
$ ivytwerkslowx = False

label IvyTwerkSlowx:
window hide
$ ivytwerkfastx = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkslowvideo behind ivytwerkfrontslowvideo
show ivytwerkslowvideo behind ivytwerkfastvideo
show ivytwerkslowvideo behind ivytwerkbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytwerkbackground
hide ivytwerkfrontslowvideo
hide ivytwerkfastvideo
if ivytwerkslowx == False:
    $ ivytwerkslowx = True
    pi "It's so much fun to twerk my ass on an unconscious superhero's face!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
call screen ivytwerkslowx()
screen ivytwerkslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontSlowx")

label IvyTwerkFrontSlowx:
$ ivytwerkfastx = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkbackground behind ivytwerkslowvideo
show ivytwerkbackground behind ivytwerkfrontfastvideo
show ivytwerkfrontslowvideo behind ivytwerkslowvideo
show ivytwerkfrontslowvideo behind ivytwerkfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytwerkslowvideo
hide ivytwerkfrontfastvideo
if ivytwerkslowx == False:
    $ ivytwerkslowx = True
    pi "It's so much fun to twerk my ass on an unconscious superhero's face!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivytwerkfrontslowx()
screen ivytwerkfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyTwerkFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkSlowx")

label IvyTwerkFastx:
window hide
$ ivytwerkslowx = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkfastvideo behind ivytwerkslowvideo
show ivytwerkfastvideo behind ivytwerkfrontfastvideo
show ivytwerkfastvideo behind ivytwerkbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytwerkbackground
hide ivytwerkslowvideo
hide ivytwerkfrontfastvideo
if ivytwerkfastx == False:
    $ ivytwerkfastx = True
    pi "When he wakes up, he'll have the smell of my snatch all over his face, hee hee!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen ivytwerkfastx()
screen ivytwerkfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumTransx")

label IvyTwerkFrontFastx:
window hide
$ ivytwerkslowx = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkbackground behind ivytwerkfrontslowvideo
show ivytwerkbackground behind ivytwerkfastvideo
show ivytwerkfrontfastvideo behind ivytwerkfrontslowvideo
show ivytwerkfrontfastvideo behind ivytwerkfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytwerkfrontslowvideo
hide ivytwerkfastvideo
if ivytwerkfastx == False:
    $ ivytwerkfastx = True
    pi "When he wakes up, he'll have the smell of my snatch all over his face, hee hee!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen ivytwerkfrontfastx()
screen ivytwerkfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumTransx")

label IvyHumTransx:
hide front
hide nexticon
hide nexticon
hide faster
hide slower
hide sceneicon
scene ivyposttwerk01 with dissolve
stop channel1
pi "Let's do something else... Something that's more appropriate considering he's unconscious yet sporting a GIANT HARDON! And I want him to SPURT his SEED!"
$ ivyhumslowx = False

label IvyHumSlowx:
window hide
$ ivyhumfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumslowvideo behind ivyhumsideslowvideo
show ivyhumslowvideo behind ivyhumfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyhumsideslowvideo
hide ivyhumfastvideo
if ivyhumslowx == False:
    $ ivyhumslowx = True
    pi "Now what happens if I caress your giant dick while you're passed out I wonder?"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
call screen ivyhumslowx()
screen ivyhumslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideSlowx")

label IvyHumSideSlowx:
$ ivyhumfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumsideslowvideo behind ivyhumslowvideo
show ivyhumsideslowvideo behind ivyhumsidefastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyhumslowvideo
hide ivyhumsidefastvideo
if ivyhumslow == False:
    $ ivyhumslow = True
    pi "Now what happens if I caress your giant dick while you're passed out I wonder?"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivyhumsideslowx()
screen ivyhumsideslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHumSideFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSlowx")

label IvyHumFastx:
window hide
$ ivyhumslowx = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumfastvideo behind ivyhumslowvideo
show ivyhumfastvideo behind ivyhumsidefastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyhumslowvideo
hide ivyhumsidefastvideo
if ivyhumfastx == False:
    $ ivyhumfastx = True
    pi "Maybe I should increase the pace of my snatch rubbing against your nose to trigger a response... A CUM response!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivyhumfastx()
screen ivyhumfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumEndx")

label IvyHumSideFastx:
window hide
$ ivyhumslowx = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumsidefastvideo behind ivyhumsideslowvideo
show ivyhumsidefastvideo behind ivyhumfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyhumsideslowvideo
hide ivyhumfastvideo
if ivyhumfastx == False:
    $ ivyhumfastx = True
    pi "Maybe I should increase the pace of my snatch rubbing against your nose to trigger a response... A CUM response!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivyhumsidefastx()
screen ivyhumsidefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumEndx")

label IvyHumEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
pi "Mmmh, yeah, I can feel your spermtub BEGGGING for release!"
scene ivyhumcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
pi "There you go, spurting while you're unconscious, that's just so NASTY!"
scene ivyhumcum02 with dissolve
pi "Oooh! And now, you're REALLY disgorging THICK jets of cum, aren't you?"
window hide
with fastflash
if age >= 20:
    pi "Yeah, keep going, EMPTY THOSE FAT BALLS!"
if age >= 18 and age <= 19:
    pi "Yeah, keep going, EMPTY THOSE FAT TEENAGE BALLS!"
scene ivyhumcum03 with dissolve
pi "Naughty boy! You're nutting over my thick asscheeks!"
window hide
with hpunch
mc "Ggggg..."
scene ivyhumcum04 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
pi "Oh look, you're waking up, just while you're PUMPING YOUR SEED ALL OVER YOUR FACE, HA HA HA!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "What the...?"
scene ivyhumcum05 with dissolve
play sound "sounds/splat.ogg"
pi "I should really add my own juices to your face to MARK MY TERRITORY!"
mc "Yuck!"
scene ivyhumcum06 with dissolve
stop music
pi "Now listen loser, I'll let you go cos it was so much fun seeing you in PAIN, but don't ever come back into this gallery, you're not strong enough to beat me clearly!"
mc "Tha... Thanks for not killing me I guess."
stop channel2
stop channel1
jump IvyGallery

label IvyGallery03:
stop channel3
stop music
scene ivyfight15 with dissolve
mc "Perhaps, but not today. In the meantime..."
scene ivyprefuck01 with dissolve
play music "sounds/sexy14.mp3"
mc "...you've lost the fight, and I have vanquished you Poison Ivy! So now, you'll do as you're told!"
pi "N...NO! NEVER!"
scene ivyprefuck02 with dissolve
mc "In that case, I'll have some sexy fun with you until you SUBMIT! So let me get those panties off you, you won't need them."
pi "You don't scare me! Your cock is... quite big indeed, but..."
scene ivyprefuck03 with dissolve
mc "The more you resist, the more PAINFUL it will be, Poison Ivy."
pi "You're just... a BEAST! Just get on with it, you filthy boy!"
scene ivyprefuck04 with dissolve
if age >= 20:
    mc "Now, these nice huge titties are just about the right size for my SUPERHERO MEGA-DONG!"
if age >= 18 and age <= 19:
    mc "Now, these nice huge titties are just about the right size for my SUPERHERO TEENAGE MEGA-DONG!"
play sound "sounds/moan01.mp3"
pi "My milkbags are too sensitive for a rough titfuck, they are the nourishing fertilizer for my plants!"
mc "Not anymore, they're just huge mounds of titflesh for my horny love muscle!"
$ ivytitslowx = False

play channel2 "sounds/wetmassage.mp3"
label IvyTitSlowx:
window hide
$ ivytitfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitslowvideo behind ivytitfrontslowvideo
show ivytitslowvideo behind ivytitfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytitfrontslowvideo
hide ivytitfastvideo
if ivytitslowx == False:
    $ ivytitslowx = True
    mc "Yeah, I LOVE your ample titflesh rubbing against my shaft..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
call screen ivytitslowx()
screen ivytitslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontSlowx")

label IvyTitFrontSlowx:
$ ivytitfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfrontslowvideo behind ivytitslowvideo
show ivytitfrontslowvideo behind ivytitfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytitslowvideo
hide ivytitfrontfastvideo
if ivytitslowx == False:
    $ ivytitslowx = True
    mc "Yeah, I LOVE your ample titflesh rubbing against my shaft..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivytitfrontslowx()
screen ivytitfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyTitFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitSlowx")

label IvyTitFastx:
$ ivytitslowx = False
if ivytitfastx == False:
    $ ivytitfastx = True
    mc "Now I'm gonna pummel my giant cock between those soft pillows even FASTER!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfastvideo behind ivytitslowvideo
show ivytitfastvideo behind ivytitfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytitslowvideo
hide ivytitfrontfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivytitfastx()
screen ivytitfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyTitCumx")

label IvyTitFrontFastx:
window hide
$ ivytitslowx = False
if ivytitfastx == False:
    $ ivytitfastx = True
    mc "Now I'm gonna pummel my giant cock between those soft pillows even FASTER!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfrontfastvideo behind ivytitfrontslowvideo
show ivytitfrontfastvideo behind ivytitfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytitfrontslowvideo
hide ivytitfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivytitfrontfastx()
screen ivytitfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyTitCumx")

label IvyTitCumx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
mc "Fuck yeah, I feel it coming..."    
pi "Just spew your vile load already and be gone!"
scene ivytitcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
mc "I'll come but... RHAAA!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
mc "I doubt I'll be gone after this, AAAH!"
scene ivytitcum02 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "I've got a HUGE SUPPLY of young spunk for you, Poison Ivy, YEAH!"
window hide
with fastflash
pi "Just EMPTY your fat sack, do your worst, you vile creature!"
scene ivytitcum03 with dissolve
mc "Oh yeah, you want some MORE? HERE'S SOME MOOOAAAARRRR!"
window hide
with hpunch
pi "Your filthy scum is flying EVERYWHERE!"
scene ivytitcum04 with dissolve
mc "More importantly, it's covering your ample bosom, RHAAA!"
window hide
with fastflash
pi "You're not done yet?"
scene ivytitcum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Phew, I am now. For THIS LOAD."
pi "Wh... What? You can't be serious?"
scene ivytitcum06 with dissolve
mc "I'm still hard and you still haven't told me where the antidote is. You leave me no choice but to FUCK YOU MERCILESSLY!"
scene ivytitcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
mc "So get ready for some SERIOUS POUNDING!"
scene ivytitcum08 with dissolve
pi "I won't tell you, even if you..."
scene ivytitcum09 with dissolve
play sound "sounds/moan04.ogg"
pi "...AAAH!"
mc "You were saying? It's rude to talk with your pussy full..."
pi "I'll resist, my vaginal muscles will REJECT your pile-driving non-vegan meat!"
mc "We'll see about that! I'll begin the ploughing!"

label IvyFuckSoftx:
window hide
$ ivyharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfucksoftvideo behind ivyfuckhardslowvideo
show ivyfucksoftvideo behind ivyfucksoftsidevideo
show ivyfucksoftvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ivyfuckbackground
hide ivyfuckhardslowvideo
hide ivyfucksoftsidevideo
mc "I'm gonna re-arrange your pussy in the shape of my MEGACOCK, Poison Ivy!"
window hide
pause
show harder:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckshortslowx()
screen ivyfuckshortslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckSoftSidex")

label IvyFuckSoftSidex:
$ ivyharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfucksoftvideo
show ivyfuckbackground behind ivyfuckhardsideslowvideo
show ivyfucksoftsidevideo behind ivyfucksoftvideo
show ivyfucksoftsidevideo behind ivyfuckhardsideslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ivyfucksoftvideo
hide ivyfuckhardsideslowvideo
pi "You won't get what you want from... * puff * me, I'm immune to... AAAAH, pain!"
window hide
pause
show harder:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckshortfastx()
screen ivyfuckshortfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckSoftx")

label IvyFuckHardSlowx:
if ivyharderx == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharderx = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckhardslowvideo behind ivyfuckhardvideo
show ivyfuckhardslowvideo behind ivyfucksoftvideo
show ivyfuckhardslowvideo behind ivyfuckhardsideslowvideo
show ivyfuckhardslowvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckbackground
hide ivyfuckhardfastvideo
hide ivyfucksoftvideo
hide ivyfuckhardsideslowvideo
window hide
pause
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckhardslowx()
screen ivyfuckhardslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("IvyFuckSoftx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSideSlowx")

label IvyFuckHardFastx:
if ivyharderx == False:
    mc "You're trying to resist but you won't for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharderx = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckhardfastvideo behind ivyfuckhardslowvideo
show ivyfuckhardfastvideo behind ivyfuckhardsidefastvideo
show ivyfuckhardfastvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckbackground
hide ivyfuckhardslowvideo
hide ivyfuckhardsidefastvideo
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckhardfastx()
screen ivyfuckhardfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSideFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyFuckEndx")

label IvyFuckHardSideSlowx:
if ivyharderx == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharderx = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfuckhardslowvideo
show ivyfuckbackground behind ivyfucksoftsidevideo
show ivyfuckbackground behind ivyfuckhardsidefastvideo
show ivyfuckhardsideslowvideo behind ivyfuckhardslowvideo
show ivyfuckhardsideslowvideo behind ivyfucksoftsidevideo
show ivyfuckhardsideslowvideo behind ivyfuckhardsidefastvideo
$ renpy.pause(.1, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckhardslowvideo
hide ivyfucksoftsidevideo
hide ivyfuckhardsidefastvideo
window hide
pause
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckhardsceneiconslowx()
screen ivyfuckhardsceneiconslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("IvyFuckSoftSidex")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSlowx")

label IvyFuckHardSideFastx:
if ivyharderx == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharderx = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfuckhardsideslowvideo
show ivyfuckbackground behind ivyfuckhardfastvideo
show ivyfuckhardsidefastvideo behind ivyfuckhardsideslowvideo
show ivyfuckhardsidefastvideo behind ivyfuckhardslowvideo
$ renpy.pause(.1, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckhardsideslowvideo
hide ivyfuckhardfastvideo
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckhardsceneiconfastx()
screen ivyfuckhardsceneiconfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyFuckEndx")

label IvyFuckEndx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
mc "Are you giving up yet, Poison Ivy? Are you yielding to my [age]yo SUPERHERO ALPHA-DONG?"
pi "* Puff * FUCK YOU!"
stop channel1
scene ivyfuckbackground
show ivyfuckcum01
with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "Then I will flood your insides with my ALPHA-SPUNK!"
window hide
with hpunch
pi "Noooo! You BASTARD, PULL OUT!"
scene ivyfuckbackground
show ivyfuckcum02
with dissolve
mc "Pull out? Why would I do that when I'm emptying my balls directly into your WOMB, RHAAAA!"
window hide
with fastflash
stop channel1
play sound "sounds/boymoan05.mp3"
pi "I'll give you the antidote I swear! Just don't make me pregnant!"
scene ivyfuckcum03 with dissolve
mc "AAAH! still pumping! Tell me NOW where it is cos I'm NUTTING BIG TIME!"
window hide
with hpunch
pi "In my boots, now PULL OUT BEFORE IT'S TOO LATE!"
menu:
    "Keep your word and pull out":
        jump IvyCumOutx
    "Keep blasting inside her and impregnate her":
        jump IvyCumMorex

label IvyCumOutx:
stop channel2
play sound "sounds/boymoan03.mp3"
scene ivyfuckcum04a with dissolve
mc "Still gonna PLASTER your body in my cream though, FU-UUU-UCCCK!"
window hide
with hpunch
play sound "sounds/moan03.mp3"
pi "You filthy boy, I don't want your vile scum on me!"
scene ivyfuckcum04b with dissolve
play sound "sounds/boymoan05.mp3"
mc "You're in luck, I'm cumming so forcefully, it's sailing over your head, AAAH!"
window hide
with fastflash
pi "It's not true, I can feel heavy blasts on my back, LIAR!"
scene ivyfuckcum04c with dissolve
play sound "sounds/boymoan03.mp3"
mc "Here's the last of it anyway, phew!"
window hide
with fastflash
pi "Human sperm is just DISGUSTING!"
scene ivyfuckcum05a with dissolve
stop sound
mc "Yeah, well, I don't spurt pollen, sorry... Now where's that godamn primer antidote? Ah, yes I remember."
jump IvyGallery

label IvyCumMorex:
play sound "sounds/boymoan03.mp3"
scene ivyfuckcum03b with dissolve
mc "I lied bitch, take that! RHAAA!"
window hide
with fastflash
pi "NOOOO, you're BLASTING insde me!"
scene ivyfuckcum03c with dissolve
play sound "sounds/boymoan05.mp3"
mc "I've got some more for you, whether you like or not, RHAAA!"
window hide
with hpunch
pi "ASSHOLE! * sob*"
scene ivyfuckcum03b with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "And even MORE to come! I'm seeding you, you should like that being a plant person and all that, no?"
scene ivyfuckcum03c with dissolve
$ renpy.pause(.5, hard='True')
window hide
with hpunch
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03b with dissolve
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03c with dissolve
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03b with dissolve
mc "FFUUUCCK, I totally impregnated you now, AAAH! You're MY bitch now, you hear me?"
stop channel1
stop channel2
pi "Y... Yes... * sob *"
scene ivyfuckcum05b with dissolve
mc "Phew, that was intense... Now where's that godamn primer antidote? Ah, yes I remember."
stop music
jump IvyGallery

label IvyGallery04:
stop channel3
stop music
play music "sounds/sexy07.mp3"
scene ivyprefuckharem01
mc "So get into the doggy position, I'm HARD and I don't have all day!"
pi "I'm kind of busy, I need to feed my pl..."
scene ivyprefuckharem02 with dissolve
mc "What part of \"you're in my harem and you will OBEY me\" did you not understand?"
pi "You're such a BRUTAL HAREM MASTER!"
scene ivyprefuckharem03 with dissolve
mc "First, I'll take these panties off, they won't be necessary..."
pi "Just hurry, I'm getting HORNY too! And I need to feed my plants."
scene ivyprefuckharem04 with dissolve
mc "Mmh, yeah, I can see that my little harem slave. You're VERY wet down there. You're really looking forward to getting teared apart by my humongous 18-incher, aren't you?"
if evilness >= 13:
    pi "I... You're just so EVIL!"
if evilness <= 12:
    pi "Y...YES, I know it will feel so GOOD!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "Sure, but you're a super-villainess so you like that, right?"
if evilness <= 12:
    mc "That's right, I'll do you HARD and GOOD!"
scene ivyprefuckharem04 with dissolve
if evilness >= 13:
    pi "No I don't! I like to be evil on my OWN!"
if evilness <= 12:
    pi "I'm so evil, I deserve it, I deserve to be put into my place by my GOOD harem Master!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "You sure? Your wet fuckhole says otherwise. Now take your boots off, I like to fuck \"au naturel\"."
if evilness <= 12:
    pi "That's right, and I can tell that your wet fuckhole is really looking forward to it! Now take your boots off, I like to fuck \"au naturel\"."
scene ivyprefuckharem06 with fastdissolve
if age >= 20:
    pi "Like this? I'm ready for your monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
if age >= 18 and age <= 19:
    pi "Like this? I'm ready for your teenage monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
mc "That's what I thought... You're horny for my massive weapon and you're going to get it. HARD and DEEP!"

$ ivyharemfuckfirstx = False
play channel1 "sounds/womansex04.mp3"
label IvyHaremFuckSlowx:
$ ivyharemfuckfastx = False
window hide
show ivyharemfuckslowvideo behind ivyharemfuckfastvideo
show ivyharemfuckslowvideo behind ivyharemfuckpovslowvideo
pause 1.0
hide ivyharemfuckfastvideo
hide ivyharemfuckpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if ivyharemfuckfirstx == False:
    $ ivyharemfuckfirstx = True
    mc "I've enlarged your hole so much that first time I banged it, now my shaft just goes in real smoothly!"
    pi "I'm... opening up as wide as I can for you, Master!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen ivyharemfuckslowx()
screen ivyharemfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckPOVSlowx")

label IvyHaremFuckFastx:
window hide
show ivyharemfuckfastvideo behind ivyharemfuckslowvideo
show ivyharemfuckfastvideo behind ivyharemfuckpovfastvideo
pause 1.0
hide ivyharemfuckpovfastvideo
hide ivyharemfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if ivyharemfuckfastx == False:
    $ ivyharemfuckfastx = True    
    mc "Now I'm really giving to you, cos you're my HAREM BITCH!"
    pi "Oh Master, you're so BRUTAL! But I LOVE IT!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen ivyharemfuckfastx()
screen ivyharemfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckPOVFastx")

label IvyHaremFuckPOVSlowx:
$ ivyharemfuckfastx = False
window hide
show ivyharemfuckpovslowvideo behind ivyharemfuckslowvideo
show ivyharemfuckpovslowvideo behind ivyharemfuckpovfastvideo
pause 1.0
hide ivyharemfuckpovfastvideo
hide ivyharemfuckslowvideo
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
call screen ivyharemfuckpovfuckslowx()
screen ivyharemfuckpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckSlowx")

label IvyHaremFuckPOVFastx:
window hide
show ivyharemfuckpovfastvideo behind ivyharemfuckfastvideo
show ivyharemfuckpovfastvideo behind ivyharemfuckpovslowvideo
pause 1.0
hide ivyharemfuckfastvideo
hide ivyharemfuckpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if ivyharemfuckfastx == False:
    $ ivyharemfuckfastx = True    
    mc "Now I'm really giving to you, cos you're my HAREM BITCH!"
    pi "Oh Master, you're so BRUTAL! But I LOVE IT!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemfuckpovfuckfastx()
screen ivyharemfuckpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckFastx")

label IvyHaremFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "You did good, Poison Ivy, you're about to make my [age]yo ALPHA-DONG CUM BIG TIME?"
pi "* Puff * Well, get on with it then!"
scene ivyfuckharemcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "First, I will flood your insides with my ALPHA-SPUNK! RHAAA!"
window hide
with hpunch
play sound "sounds/moan05.mp3"
pi "Noooo! I can't get pregnant, I need to take care of my plants!"
scene ivyfuckharemcum02 with dissolve
mc "Too late, here comes my baby-making ball-batter, AAAHH!"
window hide
with fastflash
pi "Pull out, pull out you bastard!"
scene ivyfuckharemcum03 with dissolve
stop channel2
mc "Fine, but still gonna PLASTER your body in my cream though, FU-UUU-UCCCK!"
window hide
with hpunch
play sound "sounds/moan03.mp3"
pi "You filthy boy, I can feel your vile scum on me!"
scene ivyfuckharemcum04 with dissolve
mc "I'm your HAREM MASTER, so take these heavy shots to remind you, OOOOH!"
window hide
with vpunch
pi "Please stop spewing your vile load all over me, Master!"
scene ivyfuckharemcum05 with dissolve
mc "You're in luck, here's the last of it, phew!"
window hide
with fastflash
pi "My Master's cum is so... disgusting. But so enthralling at the same time."
scene ivyfuckharemcum06 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "You got that right. And I'll be back to give you MORE. And remind you that you belong to MY Harem now!"
pi "Y.. Yes Master..."
stop music
jump IvyGallery

label IvyGallery05:
stop channel3
stop music
play music "sounds/sexy07.mp3"
scene ivyprefuckharem01
mc "I want a nice titfuck between your soft pillows until I blow my nut, you hear me?"
pi "I'm kind of busy, I need to feed my pl..."
scene ivyprefuckharem02 with dissolve
mc "What part of \"you're in my harem and you will OBEY me\" did you not understand?"
pi "You're such a BRUTAL HAREM MASTER!"
scene ivyprefuckharem03 with dissolve
mc "First, I'll take these panties off, they won't be necessary..."
pi "Just hurry, I'm getting HORNY too! And I need to feed my plants."
scene ivyprefuckharem04 with dissolve
mc "Mmh, yeah, I can see that my little harem slave. You're VERY wet down there. You're really looking forward to getting teared apart by my humongous 18-incher, aren't you?"
if evilness >= 13:
    pi "I... You're just so EVIL!"
if evilness <= 12:
    pi "Y...YES, I know it will feel so GOOD!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "Sure, but you're a super-villainess so you like that, right?"
if evilness <= 12:
    mc "That's right, I'll do you HARD and GOOD!"
scene ivyprefuckharem04 with dissolve
if evilness >= 13:
    pi "No I don't! I like to be evil on my OWN!"
if evilness <= 12:
    pi "I'm so evil, I deserve it, I deserve to be put into my place by my GOOD harem Master!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "You sure? Your wet fuckhole says otherwise. Now take your boots off, I like to fuck \"au naturel\"."
if evilness <= 12:
    pi "That's right, and I can tell that your wet fuckhole is really looking forward to it! Now take your boots off, I like to fuck \"au naturel\"."
scene ivyprefuckharem06 with fastdissolve
if age >= 20:
    pi "Like this? I'm ready for your monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
if age >= 18 and age <= 19:
    pi "Like this? I'm ready for your teenage monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
mc "That's what I thought... You're horny for my massive weapon and you're going to get it. HARD and DEEP!"

$ ivyharemtitfuckslowx = False
play channel2 "sounds/wetmassage.mp3"
label IvyHaremTitfuckSlowx:
$ ivyharemtitfuckfastx = False
window hide
show ivyharemtitfuckslowvideo behind ivyharemtitfuckfastvideo
show ivyharemtitfuckslowvideo behind ivyharemtitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyharemtitfuckfastvideo
hide ivyharemtitfuckfrontslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckslowx == False:
    $ ivyharemtitfuckslowx = True
    if age >= 20:
        pi "Do you like my tits Master? Do they wrap nicely around your giant ALPHA-DICK?"
    if age >= 18 and age <= 19:
        pi "Do you like my tits Master? Do they wrap nicely around your giant TEEN ALPHA-DICK?"
    mc "Even though your tits are not as MASSIVE than that first time, there's still plenty of boobflesh to rub against my hard pole!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen ivyharemtitfuckslowx()
screen ivyharemtitfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckPOVSlowx")

label IvyHaremTitfuckFastx:
$ ivyharemtitfuckslowx = False
window hide
show ivyharemtitfuckfastvideo behind ivyharemtitfuckslowvideo
show ivyharemtitfuckfastvideo behind ivyharemtitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyharemtitfuckfrontfastvideo
hide ivyharemtitfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckfastx == False:
    $ ivyharemtitfuckfastx = True    
    pi "Go on, pile-drive that throbbing horsecock between my breasts faster, I want to make you CUM, Master!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfastx()
screen ivyharemtitfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckPOVFastx")

label IvyHaremTitfuckPOVSlowx:
$ ivyharemtitfuckfastx = False
window hide
show ivyharemtitfuckfrontslowvideo behind ivyharemtitfuckslowvideo
show ivyharemtitfuckfrontslowvideo behind ivyharemtitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyharemtitfuckfrontfastvideo
hide ivyharemtitfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckslowx == False:
    $ ivyharemtitfuckslowx = True
    if age >= 20:
        pi "Do you like my tits Master? Do they wrap nicely around your giant ALPHA-DICK?"
    if age >= 18 and age <= 19:
        pi "Do you like my tits Master? Do they wrap nicely around your giant TEEN ALPHA-DICK?"
    mc "Even though your tits are smaller than that first time, there's still plenty of boobflesh to rub against my hard pole!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfrontfuckslowx()
screen ivyharemtitfuckfrontfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckSlowx")

label IvyHaremTitfuckPOVFastx:
$ ivyharemtitfuckslowx = False
window hide
show ivyharemtitfuckfrontfastvideo behind ivyharemtitfuckfastvideo
show ivyharemtitfuckfrontfastvideo behind ivyharemtitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyharemtitfuckfastvideo
hide ivyharemtitfuckfrontslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
if ivyharemtitfuckfastx == False:
    $ ivyharemtitfuckfastx = True    
    pi "Go on, pile-drive that throbbing horsecock between my breasts faster, I want to make you CUM, Master!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfrontfuckfastx()
screen ivyharemtitfuckfrontfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckFastx")

label IvyHaremTitfuckEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
mc "Fuck yeah, I feel it coming..."    
pi "Spew that load already and be gone!"
scene ivytitfuckharemcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
mc "...anytime... RHAAA!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
pi "You're EXPLODING like a cum firehose!"
scene ivytitfuckharemcum02 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "I've got a HUGE SUPPLY of young spunk for you, Poison Ivy, YEAH!"
window hide
with fastflash
pi "Just EMPTY your fat sack, do your worst!"
scene ivytitfuckharemcum03 with dissolve
mc "Oh yeah, you want some MORE? HERE'S SOME MOOOAAAARRRR!"
window hide
with hpunch
pi "Your filthy scum is flying EVERYWHERE!"
scene ivytitfuckharemcum04 with dissolve
mc "More importantly, it's covering your ample bosom, RHAAA!"
window hide
with fastflash
pi "Your huge cumstreaks are so... scalding hot!"
scene ivytitfuckharemcum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
pi "My Master's cum is so... disgusting. But so enthralling and tasty at the same time."
scene ivytitfuckharemcum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "It's NOT disgusting! And I'll be back to give you MORE. And remind you that you belong to MY Harem now!"
pi "Y.. Yes Master..."
stop music
jump IvyGallery