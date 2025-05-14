label SophiaGallery:
stop channel3
play channel3 "sounds/covertmusic.mp3"
scene sophiabackground
show sophiamaingallery at gallerypos01 with moveinleft
call screen gallerysophia()
screen gallerysophia():
    text "{font=Gui/Heroes Legend.ttf}Naughty Sophia Porker{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
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
            action [Hide ("gallerysophia"), Jump ("SophiaGalleryAnim")]
    
    if renpy.seen_image("sophiaprefuck02"):
        imagebutton:
            focus_mask True
            idle "gallery/sophiagallery01.png" xpos 400 ypos 100
            hover "gallery/sophiagallery01.png"
            action Jump ("SophiaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Street Fuck{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("sophiaprefuck02") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SophiaGallery")

    if renpy.seen_image("sophiaoffice19"):
        imagebutton:
            focus_mask True
            idle "gallery/sawyergallery02.png" xpos 750 ypos 100
            hover "gallery/sawyergallery02.png"
            action Jump ("SophiaGallery02")
    text "{font=Gui/Heroes Legend.ttf}3some w/ Sawyer{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("sophiaoffice19") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SophiaGallery")

label SophiaGalleryAnim:
call screen screenanimsophia()
screen screenanimsophia():
    modal True
    add "gallery/sophiabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "sophiaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "sophiaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimsophia"), SetVariable ("animcount", 1), Jump ("SophiaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Sophia Porker{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 38{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34D-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Massive Cocks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Public Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/sophiaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimsophia")]
    add "gallery/sophiaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimsophia")]
            
label SophiaGallery01:
stop channel3
scene sophiaprefuck01 with dissolve
play channel1 "sounds/sexy02.mp3"
mc "You can call me [name]... Sophia."
so "Ooh, well thank you then... [name]."
scene sophiaprefuck02 with dissolve
so "Now where were we in this re-enactement?"
mc "I was fingering your pussy if I remember correctly."
scene sophiaprefuck03 with dissolve
so "Ah yes. Let me get into position then. So we can do this re-enactement properly. I'll take my panties off for you, since I don't want them ripped off like when I was raped."
scene sophiaprefuck04 with dissolve
mc "Yes, that would be a shame."
scene sophiaprefuck05 with dissolve
so "One of the thugs pulled his great big cock and started slapping my arse with it."
scene sophiaprefuck06 with dissolve
mc "I see, did he leave a bruise on it?"
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
so "AAh, y.. yes, but his dong was not as HEAVY and POWERFUL as yours... [name]..."
scene sophiaprefuck06 with dissolve
mc "So I won't slap you TOO hard then."
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
so "Mmmh, the sound of your fat donkey-dick slapping against my slutty buttocks is making me so wet..."
if age >=18 and age <=19:
    so "Please stick your massive teenage pud inside me, [name]!"
if age >=20:
    so "Please stick your massive pud inside me, [name]!"

scene sophiaprefuck08 with fastdissolve
mc "Let's see if it will fit first... Your pussy looks VERY tight."
so "That's because it's never been STRETCHED by my pindick hubby... Just PUSH IT IN, I can take it, Officer [hero]!"
play sound "sounds/whoosh.mp3"
scene sophiaprefuck09 with fastdissolve
mc "Damn, your pussy really wanted that dick..."
so "Yes it did, Mister Officer [hero]... Now fuck me nice and slow with your giant boycock."
play channel2 "sounds/womansex01.mp3"
show sophiaslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "Like that? You like that Sophia?"
so "Mmh, yes, it feels so good..."
window hide
pause
so "Please... AAAAH, give it to me like a SUPER-STUD!"
mc "You want all 15 inches pounding inside of you?"
so "YY... YES [hero]!"
mc "Beg for it!"
if age >= 20:
    so "Please POUND ME WITH YOUR FIFTEEN INCHES OF MONSTER MEAT!"
if age >=18 and age <= 19:
    so "Please POUND ME WITH YOUR FIFTEEN INCHES OF TEENAGE MONSTER MEAT!"
stop channel2
play channel2 "sounds/pounding.ogg"
show sophiafastvideo with dissolve
pause
so "Are you going to pump my pussy full of yummy cum? Like that thug did...?"
mc "I'm gonna WHITEWASH his load with mine, Mrs Porker!"
$ renpy.pause(2.0, hard='True')
stop channel2
scene sophiafuckcum01 with dissolve
play music "sounds/splooge02.mp3"
mc "AAAH, here it comes!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
so "Oooh, your monster shots are making me cum too!"
scene sophiafuckcum02 with dissolve
so "You're cumming so much!"
window hide
with fastflash
mc "That's cos I'm a SUPER-CUMMER! RHAAA!"
scene sophiafuckcum03 with dissolve
mc "Take some more young spunk, DEEP inside your womb!"
window hide
with fastflash
so "Oooh, Mister [hero], I'm BLOATED with your scalding cream!"
stop music
play music "sounds/boyorgasm01.mp3"
scene sophiafuckcum04 with dissolve
mc "Then I'l come the rest all over your back, RHOAR!"
window hide
with fastflash
so "AAAH!... Your shots are so HOT and POWERFUL, [name]!"
scene sophiafuckcum05 with dissolve
if age >= 20:
    so "My pussy is DRIPPING with your load and you're STILL blasting?"
if age >=18 and age <= 19:
    so "My pussy is DRIPPING with your teenage load and you're STILL blasting?"
window hide
with fastflash
mc "Fuck yeah! Take those final shots Sophia, AAAH!"
window hide
with fastflash
so "So ssooo much young cum!"
stop music
scene sophiafuckcum06 with fade
play sound "sounds/panting.mp3"
so "You... came more than my husband in ALL our years of marriage... Oooh, how am I going to explain all that smelly spunk on me when I get home?"
stop channel1 
stop channel3
jump SophiaGallery

label SophiaGallery02:
stop channel3
stop channel1
scene sophiaoffice10 with fade
cs01 "I hope you come back with good news, [hero]."
mc "I sure do, Captain Sawyer, I soundly defeated Poison Ivy and I now have the antidote!"
scene sophiaoffice16 with dissolve
so "Really? Oh my God, this is the most exciting day of my life, even better than when one of my students went as far as lifting my skirt in the shool corridor! Please give me that antidote!"
cs01 "Please drink only a small amount, we need to make large quantities out of it for the other inflicted women, I'm sure Vayne Industries will oblige."
play music "sounds/sexy04.mp3"
scene sophiaoffice17 with dissolve
mc "And I would suggest you take your top off, you wouldn't want to rip your bra..."
cs01 "* sigh *"
scene sophiaoffice18 with dissolve
play sound "v032/gulp.mp3"
cs01 "That's enough Mrs Porker!"
scene sophiaboobsmall with dissolve
mc "Now let's see if it worked... In real-time."
show sophiaboobgrowvideo
$ renpy.pause(1.0, hard='True')
hide sophiaboobgrowvideo
show sophiaboobbig
play sound "sounds/wow.mp3"
so "Wow!"
show nexticon:
    xpos 1750 ypos 1020    
show slowmoicon:
     xpos 1700 ypos 500     
call screen sophiaslowmox()
screen sophiaslowmox():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBoobsSlowmox")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBoobsEndx")    

label SophiaBoobsSlowmox:
play sound "v032/wowslow.mp3"
hide slowmoicon
hide nexticon
hide sophiaboobbig
show sophiaboobgrowslowvideo
$ renpy.pause(2.97, hard='True')
hide sophiaboobgrowslowvideo
show sophiaboobbig
label SophiaBoobsEndx:
hide nexticon
hide slowmoicon
mc "Wow indeed..."
scene sophiaoffice19 with dissolve
play sound "sounds/moan03.mp3"
so "I just LOVE my new big tits! What about you, Mr [hero]?"
scene sophiaoffice20 with dissolve
mc "I can safely say that I love them too."
so "Oh my God, you've grown BIGGER too, haven't you?"
cs01 "Now this is highly inappropriate, Mrs Porker doesn't need to see your giant menacing phallus, she's a married woman! And a mother might I add."
scene sophiaoffice19 with dissolve
so "Oh but I don't mind, Captain Sawyer! My hubby, he's... I NEED to feel wanted and this boy makes me feel a whole WOMAN again after three years of dev neglect!"
scene sophiaoffice21 with dissolve
cs01 "In that case, I want in. [hero] needs to be punished for this outrageously lewd display. And YOU need to be punished for gulping down too much of the antidote..."
so "But I left some in the vial, I swear!"
scene sophiaoffice22 with dissolve
cs01 "[hero], don't you agree that Mrs Porker has broken the law and deserves a severe punishment?"
mc "I sure do, Captain Sawyer."
if age >= 20:
    cs01 "Do you agree that getting pummeled by your 18-inch superhero cock would constitute an adequate sentence?"
if age >= 18 and age <= 19:
    cs01 "Do you agree that getting pummeled by your 18-inch superhero teenage cock would constitute an adequate sentence?"
mc "Ooh yeah! Perfectly adequate!"
scene sophiaoffice23 with dissolve
cs01 "Then let's get her ready for her sentence!"
play sound "sounds/kiss.mp3"
window hide 
with hpunch
so "Oooh! I'm really going to get PUNISHED this time!"
play sound "sounds/moan01.mp3"
scene sophiaoffice24 with dissolve
mc "Interesting pose..."
cs01 "That way, I can lick her pussy while you take her from the other end."
scene sophiaoffice25 with dissolve
so "Oooh, Captain Sawyer!"
play sound "sounds/slurp.mp3"
mc "I'm gonna have to kneel to fuck her mouth properly then."
scene sophiapreblow01 with dissolve
so "Your cock is just... too MASSIVE, Mr Officer [hero]!"
cs01 "Your sentence includes gagging on a monstercock, Mrs Porker!"
mc "Also, the dev somehow always manages to make it fit."
scene sophiapreblow02 with dissolve
play sound "sounds/moan04.ogg"
mc "See? It fits just fine..."
stop sound
play channel1 "v032/blow03.mp3"
$ sophiablowslowx = False

label SophiaBlowSlowx:
window hide
$ sophiablowfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowslowvideo behind sophiablowtopslowvideo
show sophiablowslowvideo behind sophiablowfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowtopslowvideo
hide sophiablowfastvideo
if sophiablowslowx == False:
    $ sophiablowslowx = True       
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show topicon:
     xpos 50 ypos 500     
call screen sophiablowslowx()
screen sophiablowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlowx")

label SophiaBlowFrontSlowx:
$ sophiablowfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowtopslowvideo behind sophiablowslowvideo
show sophiablowtopslowvideo behind sophiablowtopfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowslowvideo
hide sophiablowtopfastvideo
if sophiablowslowx == False:
    $ sophiablowslowx = True
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiablowtopslowx()
screen sophiablowtopslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBlowFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlowx")

label SophiaBlowFastx:
$ sophiablowslowx = False
if sophiablowfastx == False:
    $ sophiablowfastx = True
    mc "I think your throat can take some FASTER skull-fucking now!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowfastvideo behind sophiablowslowvideo
show sophiablowfastvideo behind sophiablowtopfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowslowvideo
hide sophiablowtopfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show topicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen sophiablowfastx()
screen sophiablowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNextx")

label SophiaBlowFrontFastx:
window hide
$ sophiablowslowx = False
if sophiablowfastx == False:
    $ sophiablowfastx = True
    mc "I think your throat can take some FASTER skull-fucking now!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowtopfastvideo behind sophiablowtopslowvideo
show sophiablowtopfastvideo behind sophiablowfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowtopslowvideo
hide sophiablowfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen sophiablowtopfastx()
screen sophiablowtopfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNextx")

label SophiaBlowNextx:
hide  nexticon
hide faster
hide slower
hide sceneicon
hide topicon    
cs01 "Let's give her mouth and pussy some respite..."
if age >= 20:
    mc "Let me first see how far she can take my fat pole..."
if age >= 18 and age <= 19:
    mc "Let me first see how far she can take my fat teen pole..."
scene sophiaoffice30 with dissolve
stop channel1
play sound "sounds/blow02.mp3"
mc "Damn, almost to the balls!"
window hide 
with hpunch
so "GGGGllll..."
scene sophiaoffice31 with dissolve
stop sound
play sound "v031/cough.mp3"
mc "Well done, you must have taken like, 15 inches or something. God only knows where they went."
cs01 "Now for the next part of your sentence. I authorize [hero] here to fuck you senseless on my desk!"
mc "Alright!"
scene sophiaoffice32 with dissolve
mc "Let's get this show on the road. Since Mrs Porker here is still recovering from barely being able to breathe for the last fifteen minutes, I'll take matters in my own hands."
so "Dear Lord, I'm in for a mighty POUNDING!"
scene sophiaoffice33 with dissolve
play sound "sounds/thud.mp3"
so "Oooh, you're so rough and MANLY, Mr Officer [hero]!"
scene sophiaoffice34 with dissolve
mc "I won't ask if you're ready, cos this is part of your SENTENCE!"
so "Still, please be caref..."
$ sophiadeskslowx = False

label SophiaDeskSlowx:
window hide
$ sophiadeskfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskslowvideo behind sophiadeskpovslowvideo
show sophiadeskslowvideo behind sophiadeskfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sophiadeskpovslowvideo
hide sophiadeskfastvideo
if sophiadeskslowx == False:
    $ sophiadeskslowx = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <=19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophiadeskslowx()
screen sophiadeskslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlowx")

label SophiaDeskFrontSlowx:
$ sophiadeskfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskpovslowvideo behind sophiadeskslowvideo
show sophiadeskpovslowvideo behind sophiadeskpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sophiadeskslowvideo
hide sophiadeskpovfastvideo
if sophiadeskslowx == False:
    $ sophiadeskslowx = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <=19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiadeskpovslowx()
screen sophiadeskpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaDeskFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlowx")

label SophiaDeskFastx:
$ sophiadeskslowx = False
if sophiadeskfastx == False:
    $ sophiadeskfastx = True
    mc "Damn, that pussy is just BEGGING to get fucked HARDER!"
    so "AAAH, YES! pound me like the cheap whore that I am, Mr [hero]!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskfastvideo behind sophiadeskslowvideo
show sophiadeskfastvideo behind sophiadeskpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sophiadeskslowvideo
hide sophiadeskpovfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophiadeskfastx()
screen sophiadeskfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCumx")

label SophiaDeskFrontFastx:
window hide
$ sophiadeskslowx = False
if sophiadeskfastx == False:
    $ sophiadeskfastx = True
    mc "Damn, that pussy is just BEGGING to get fucked HARDER!"
    so "AAAH, YES! pound me like the cheap whore that I am, Mr [hero]!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskpovfastvideo behind sophiadeskpovslowvideo
show sophiadeskpovfastvideo behind sophiadeskfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sophiadeskpovslowvideo
hide sophiadeskfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophiadeskpovfastx()
screen sophiadeskpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCumx")

label SophiaDeskCumx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
cs01 "I think she's begging for your cum, [hero]. Fill her up, turn her slutty pussy into your cum dump!"
mc "Oh fuck, you girls are so nast..."
scene sophiadeskcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play sound "sounds/splooge02.mp3"
mc "...AAAAH!"
window hide
with hpunch
so "My hubby never comes this HARD, OOOOH!"
scene sophiadeskcum02 with dissolve
so "...On the rare occasion when he can get his pindick hard that is, AAAH!"
window hide
with fastflash
cs01 "Keep pumping that fat load deep inside her pussy and shut her up!"
scene sophiadeskcum03 with dissolve
play sound "sounds/moan05.mp3"
mc "Take that Mrs Porker, RHAAA!"
window hide
with hpunch
so "Sssooo much CUM, AAAH!"
scene sophiadeskcum04 with dissolve
play sound "sounds/moan04.ogg"
mc "I've got MORE for your hungry hole!"
window hide
with fastflash
cs01 "Keep going, I want you to empty yourself!"
scene sophiadeskcum03 with dissolve
play sound "sounds/moan05.mp3"
mc "AAAH, yes!"
scene sophiadeskcum04 with dissolve
mc "Here you go!"
scene sophiadeskcum03 with dissolve
so "I beg you, please stop!"
mc "And MORE, RHAAA!"
scene sophiadeskcum04 with dissolve
mc "And MORE, RHAAA!"
with hpunch
cs01 "You did good, she's overfilled with your [age]yo scum..."
scene sophiadeskcum05 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
so "You've turned my fuckhole inside out... I don't think I will ever be able to feel my hubby's tiny dick ever again. Or any of my pupils' for that matter."
mc "Now, as you may have noticed, I am still HARD, despite the monstrous load I just dumped inside Mrs Porker."
scene sophiadeskcum06 with dissolve
cs01 "So, you expect us to make you blow another giant load before you finally leave us in peace?"
mc "That would be the strict minimum in my books, yes."
scene sophiadeskcum07 with dissolve
if age >= 20:
    cs01 "Just because you're such a fucking STUD doesn't give you the right to just nut your sauce anywhere and anytime you want!"
if age >= 18 and age <= 19:
    cs01 "Just because you're such a fucking TEEN STUD doesn't give you the right to just nut your sauce anywhere and anytime you want!"
mc "It doesn't?"
so "We're gonna tease you so much, you'll be BEGGING for release, Mr Officer [hero]..."
mc "Try me!"
cs01 "Fine, go and sit down on the sofa and wait for us..."
scene sophiadeskcum08 with dissolve
cs01 "I'm gonna hold this monster tight while we slowly lick the whole shaft to a mighty explosion!"
play channel1 "sounds/lick01.ogg"
$ sophialickslowx = False

label SophiaLickSlowx:
window hide
$ sophialickfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickslowvideo behind sophialicksceneslowvideo
show sophialickslowvideo behind sophialickfastvideo
$ renpy.pause(1.0, hard='True')
hide sophialicksceneslowvideo
hide sophialickfastvideo
if sophialickslowx == False:
    $ sophialickslowx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophialickslowx()
screen sophialickslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlowx")

label SophiaLickSceneSlowx:
$ sophialickfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialicksceneslowvideo behind sophialickslowvideo
show sophialicksceneslowvideo behind sophialickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sophialickslowvideo
hide sophialickscenefastvideo
if sophialickslowx == False:
    $ sophialickslowx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophialicksceneslowx()
screen sophialicksceneslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaLickSceneFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlowx")

label SophiaLickFastx:
$ sophialickslowx = False
if sophialickfastx == False:
    $ sophialickfastx = True
    mc "That's it, my little cock-hungry whores, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickfastvideo behind sophialickslowvideo
show sophialickfastvideo behind sophialickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sophialickslowvideo
hide sophialickscenefastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophialickfastx()
screen sophialickfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCumx")

label SophiaLickSceneFastx:
window hide
$ sophialickslowx = False
if sophialickfastx == False:
    $ sophialickfastx = True
    mc "That's it, my little cock-hungry whores, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickscenefastvideo behind sophialicksceneslowvideo
show sophialickscenefastvideo behind sophialickfastvideo
$ renpy.pause(1.0, hard='True')
hide sophialicksceneslowvideo
hide sophialickfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophialickpovfastx()
screen sophialickpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCumx")

label SophiaLickCumx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "Oh God, oh..."
scene sophialickcum01 with dissolve
play sound "sounds/boymoan03.mp3"
so "He's leaking pre-slime like a faucet!"
cs01 "That means he's about to bust his nut."
scene sophialickcum02 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
so "Let my tongue take him over the edge then..."
scene sophialickcum03 with dissolve
mc "AAAH!"
window hide
with hpunch
play sound "sounds/wow.mp3"
so "Oh my God, it's flying so high up!"
scene sophialickcum04 with dissolve
if age >= 20:
    cs01 "Look at that shot, more manly cum in that single shot than a hundred men combined!"
if age >= 18 and age <= 19:
    cs01 "Look at that shot, more manly teenage cum in that single shot than a hundred men combined!"
window hide
with fastflash
so "He had a LOT of cum left!"
scene sophialickcum05 with dissolve
mc "FFF..FFFFFUUUUCCCKK, RHAAA!"
window hide
with hpunch
cs01 "Keep pumping boy, let it RAIn down upon us!"
window hide
with fastflash
so "My face has been BUKKAKED! And so has yours, Captain Sawyer!"
scene sophialickcum06 with dissolve
stop channel1
play sound "sounds/lick03.mp3"
so "Mmmh, it's so thick and chunky."
cs01 "And there's so much of it..."
play sound "sounds/slurp.mp3"
so "* lick * I'm going to have to buy new outfits to fit my bigger tits... Hopefully, that will lead to some of my students feeling up some new fabric."
cs01 "I think it's time for you to get cleaned up and go back to your family, Mrs Porker."
cs01 "And for you to go back to the gallery..."
stop channel1 
stop channel3
stop music
jump SophiaGallery