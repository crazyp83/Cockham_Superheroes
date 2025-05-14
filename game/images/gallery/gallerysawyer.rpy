label SawyerGallery:
stop channel3
play channel3 "sounds/policemusic.mp3"
scene sawyerbackground
show sawyermaingallery at gallerypos01 with moveinleft
call screen gallerysawyer()
screen gallerysawyer():
    text "{font=Gui/Heroes Legend.ttf}Naughty Captain Sawyer{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
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
            action [Hide ("gallerysawyer"), Jump ("SawyerGalleryAnim")]
    
    if renpy.seen_image("sawyerfootcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/sawyergallery01.png" xpos 400 ypos 100
            hover "gallery/sawyergallery01.png"
            action Jump ("SawyerGallery01")
    text "{font=Gui/Heroes Legend.ttf}Footjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("sawyerfootcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("SawyerGallery01hint")

    if renpy.seen_image("sophiaoffice19"):
        imagebutton:
            focus_mask True
            idle "gallery/sawyergallery02.png" xpos 750 ypos 100
            hover "gallery/sawyergallery02.png"
            action Jump ("SawyerGallery02")
    text "{font=Gui/Heroes Legend.ttf}3some w/ Sophia{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("sophiaoffice19") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SawyerGallery")

    if renpy.seen_image("wallsawyercum01"):
        imagebutton:
            focus_mask True
            idle "gallery/sawyergallery03.png" xpos 1100 ypos 100
            hover "gallery/sawyergallery03.png"
            action Jump ("SawyerGallery03")
    text "{font=Gui/Heroes Legend.ttf}Office Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("wallsawyercum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SawyerGallery")


label SawyerGallery01hint:
show sawyermaingallery at gallerypos01
show sawyergallery01 at posgalleryhintpic
show sawyergalleryhint01 at posgalleryhint
pause
hide sawyergalleryhint01
hide sawyergallery01
call screen gallerysawyer()

label SawyerGalleryAnim:
stop channel3
play channel3 "sounds/sexy14.mp3"
call screen screenanimsawyer()
screen screenanimsawyer():
    modal True
    add "gallery/sawyerbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "sawyeranimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "sawyeranimout" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "sawyeranimlin" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "sawyeranimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimsawyer"), SetVariable ("animcount", 1), Jump ("SawyerGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Captain Sawyer{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 39{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft6{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34D-24-34{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Footjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink04
    add "gallery/sawyeranim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimsawyer")]
    add "gallery/sawyeranim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimsawyer")]
    add "gallery/sawyeranim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimsawyer")]
    add "gallery/sawyeranim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimsawyer")]
            
label SawyerGallery01:
scene sawyerstrip01 with fade
play music "sounds/sexy03.mp3"
mc "* Oooh, she's getting undressed behind that curtain. Let's use my Super-Senses to see better..."
scene sawyerstrip02b with dissolve
mc "* That's much better, I can totally see through this ..., it's like it's transparent. I like that Super-Power... *"
scene sawyerstrip03b with dissolve
mc "* Mmh, I'm starting to get a hardon... *"
scene sawyerstrip04b with dissolve
mc "* Ooh yeah, baby, take that bra off while I... adjust my hardening dong... *"
scene sawyerstrip05b with dissolve
mc "* Now we're talking! I'm gonna have a fast wank while she finishes... *"
scene sawyerstrip06b with dissolve
mc "* Just need a few more seco... *"
cs02 "I trust you didn't use your Super-Senses to w..."
stop music
scene sawyerstripendbad with dissolve
cs02 "What the hell! You DID use your Super-Vision you fucking PERVERT!"
scene sawyerprefoot01 with dissolve
mc "Err... Sorry, I couldn't help it... Your body... It's so HOT!"
cs02 "Is that so? Well, we can't go out with your giant cock sticking out like that for all to see. So I'm cancelling the mission for today."
scene sawyerprefoot00 with dissolve
play sound "sounds/dispatch.mp3"
cs02 "Chief Sawyer here. Tell Mrs Porker to come back tomorrow with apologies from the CCPD."
scene sawyerprefoot02 with dissolve
stop sound
cs02 "As for you... you deserve a PUNISHMENT for the crime of \"Misuse of Superpowers\"!"
mc "Uh oh..."
cs02 "Get on your knees and lick my feet!"
play channel1 "sounds/sexy03.mp3"
scene sawyerprefoot03 with dissolve
play sound "sounds/lick01.ogg"
cs02 "A bit higher now. While I tame that hard BEAST of yours..."
scene sawyerprefoot04 with dissolve
play sound "sounds/lick01.ogg"
cs02 "That's good... You like my fishnet stockings, don't you, naughty boy?"
mc "Yes, Captain Sawyer."
if age >= 20:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant young meat!"
if age == 18 or age == 19:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant teeenage meat!"
show sawyerfootslowstart
play channel2 "sounds/wank.mp3"
scene sawyerfootslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
cs02 "Does this feel good on your trembling shaft, [hero]?"
mc "Oh yeah, fuck..."
window hide
pause
cs02 "Remove your hand and let me pump that fat shaft FASTER!"
scene sawyerfootfastvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "God, your feet... These stockings..."
window hide
pause
cs02 "You're gonna cum aren't you? You're gonna unload those bloated balls that are making you lose focus on your duties... Go on, DUMP YOUR YOUNG CREAM!" 
hide sawyerfootslowstart
scene sawyerfootcum01
with dissolve
cs02 "Ooh yeah, you're real close, you're spattering pre-cum all over the pl..."
scene sawyerfootcum02 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAAH!"
window hide
with fastflash
cs02 "That's it, let it all out!"
scene sawyerfootcum03 with dissolve
cs02 "Look at the filthy mess you're making!"
window hide
with fastflash
mc "Ah, it's not my fault, AAAH!"
window hide
with fastflash
cs02 "YES IT IS! This is what happens when you MISUSE YOUR SUPERPOWERS!"
stop channel1
stop channel2
scene sawyerfootcum04 with dissolve
play sound "sounds/panting.mp3"
mc "Aaah... I came too much..."
cs02 "And now you're TIRED and USELESS. So much for that so-called Super-Studliness Captain MILF warned me about. My FEET defeated YOUR superpower!"
scene sawyerfootcum05 with dissolve
cs02 "So let this be a LESSON to you."
mc "Just give me a small break and I'll get another erection in no ti..."
cs02 "GET OUT OF MY OFFICE!"
jump SawyerGallery

label SawyerGallery02:
stop channel3
stop music
scene sophiaoffice10
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
call screen sophiaslowmoxx()
screen sophiaslowmoxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBoobsSlowmoxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBoobsEndxx")    

label SophiaBoobsSlowmoxx:
play sound "v032/wowslow.mp3"
hide slowmoicon
hide nexticon
hide sophiaboobbig
show sophiaboobgrowslowvideo
$ renpy.pause(2.97, hard='True')
hide sophiaboobgrowslowvideo
show sophiaboobbig
label SophiaBoobsEndxx:
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
$ sophiablowslowxx = False

label SophiaBlowSlowxx:
window hide
$ sophiablowfastxx = False
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
if sophiablowslowxx == False:
    $ sophiablowslowxx = True       
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show topicon:
     xpos 50 ypos 500     
call screen sophiablowslowxx()
screen sophiablowslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlowxx")

label SophiaBlowFrontSlowxx:
$ sophiablowfastxx = False
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
if sophiablowslowxx == False:
    $ sophiablowslowxx = True
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiablowtopslowxx()
screen sophiablowtopslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBlowFrontFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlowxx")

label SophiaBlowFastxx:
$ sophiablowslowxx = False
if sophiablowfastxx == False:
    $ sophiablowfastxx = True
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
call screen sophiablowfastxx()
screen sophiablowfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNextxx")

label SophiaBlowFrontFastxx:
window hide
$ sophiablowslowxx = False
if sophiablowfastxx == False:
    $ sophiablowfastxx = True
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
call screen sophiablowtopfastxx()
screen sophiablowtopfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNextxx")

label SophiaBlowNextxx:
hide  nexticon
hide faster
hide slower
hide sceneicon
hide topicon    
cs01 "Let's give her mouth and pussy some respite..."
if age >= 20:
    mc "Let me first see how far she can take my fat pole..."
if age >= 8 and age <= 19:
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
$ sophiadeskslowxx = False

label SophiaDeskSlowxx:
window hide
$ sophiadeskfastxx = False
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
if sophiadeskslowxx == False:
    $ sophiadeskslowxx = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <= 19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophiadeskslowxx()
screen sophiadeskslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlowxx")

label SophiaDeskFrontSlowxx:
$ sophiadeskfastxx = False
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
if sophiadeskslowxx == False:
    $ sophiadeskslowxx = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <= 19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiadeskpovslowxx()
screen sophiadeskpovslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaDeskFrontFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlowxx")

label SophiaDeskFastxx:
$ sophiadeskslowxx = False
if sophiadeskfastxx == False:
    $ sophiadeskfastxx = True
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
call screen sophiadeskfastxx()
screen sophiadeskfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCumxx")

label SophiaDeskFrontFastxx:
window hide
$ sophiadeskslowxx = False
if sophiadeskfastxx == False:
    $ sophiadeskfastxx = True
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
call screen sophiadeskpovfastxx()
screen sophiadeskpovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCumxx")

label SophiaDeskCumxx:
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
$ sophialickslowxx = False

label SophiaLickSlowxx:
window hide
$ sophialickfastxx = False
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
if sophialickslowxx == False:
    $ sophialickslowxx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophialickslowxx()
screen sophialickslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlowxx")

label SophiaLickSceneSlowxx:
$ sophialickfastxx = False
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
if sophialickslowxx == False:
    $ sophialickslowxx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophialicksceneslowxx()
screen sophialicksceneslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaLickSceneFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlowxx")

label SophiaLickFastxx:
$ sophialickslowxx = False
if sophialickfastxx == False:
    $ sophialickfastxx = True
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
call screen sophialickfastxx()
screen sophialickfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCumxx")

label SophiaLickSceneFastxx:
window hide
$ sophialickslowxx = False
if sophialickfastxx == False:
    $ sophialickfastxx = True
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
call screen sophialickpovfastxx()
screen sophialickpovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlowxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCumxx")

label SophiaLickCumxx:
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
jump SawyerGallery

label SawyerGallery03:
stop channel3
stop music
play music "sounds/sexy02.mp3"
scene sawyerprelick01
cs01 "I suppose you want me to help you get a hardon?"
mc "That would help. Sexual intercourse is best with a HARD dick."
scene sawyerprelick02:
    subpixel True
    xpos 0.0 ypos 0.0
    ease 7.0 ypos -1.0 xpos -0.04
with dissolve
$ renpy.pause(2.0, hard='True')
pause
mc "Now turn round, your ass is definitely cock-hardening..."
scene sawyerprelick03:
    subpixel True
    xpos -0.04 ypos -0.0
    ease 7.0 ypos -1.0 xpos 0.0
with dissolve
$ renpy.pause(2.0, hard='True')
pause
cs01 "You talk more like a sex pervert than a Super-Hero, you know that?"
scene sawyerprelick04:
    subpixel True
    xpos 0.0 ypos -1.0
    ease 6.0 ypos -.15 xpos -0.04
with dissolve
$ renpy.pause(2.0, hard='True')
pause
mc "Yeah, I know that."
cs01 "And I see that your cock is now ROCK-HARD."
scene sawyerprelick05 with dissolve
play sound "sounds/moan01.mp3"
cs01 "I can feel it pushing against my back... It's so amazingly HUGE!"
if age >= 20:
    mc "Yep, eighteen inches of SUPER-HERO COCK right there for you, Captain Sawyer..."
if age >= 18 and age <= 19:
    mc "Yep, eighteen inches of SUPER-HERO TEEN COCK right there for you, Captain Sawyer..."
cs01 "Call me Maggie. And go and sit on the sofa so I can take CARE of that giant love muscle..."
scene sawyerprelick06 with dissolve
cs01 "You simply can't concentrate on the job with a hardon THAT MASSIVE, can you?"
mc "It's true, you need to..."
scene sawyerprelick07 with dissolve
cs01 "I'm gonna hold this monster tight while I slowly lick the whole shaft to a mighty explosion!"
$ sawyerlickslowx = False

play channel1 "sounds/lick01.ogg"
label SawyerLickSlowx:
window hide
$ sawyerlickfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickslowvideo behind sawyerlicksceneslowvideo
show sawyerlickslowvideo behind sawyerlickfastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlicksceneslowvideo
hide sawyerlickfastvideo
if sawyerlickslowx == False:
    $ sawyerlickslowx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sawyerlickslowx()
screen sawyerlickslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneSlowx")

label SawyerLickSceneSlowx:
$ sawyerlickfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlicksceneslowvideo behind sawyerlickslowvideo
show sawyerlicksceneslowvideo behind sawyerlickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlickslowvideo
hide sawyerlickscenefastvideo
if sawyerlickslowx == False:
    $ sawyerlickslowx = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sawyerlicksceneslowx()
screen sawyerlicksceneslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SawyerLickSceneFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSlowx")

label SawyerLickFastx:
$ sawyerlickslowx = False
if sawyerlickfastx == False:
    $ sawyerlickfastx = True
    mc "That's it, Maggie, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickfastvideo behind sawyerlickslowvideo
show sawyerlickfastvideo behind sawyerlickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlickslowvideo
hide sawyerlickscenefastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerlickfastx()
screen sawyerlickfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerLickCumx")

label SawyerLickSceneFastx:
$ sawyerlickslowx = False
if sawyerlickfastx == False:
    $ sawyerlickfastx = True
    mc "That's it, Maggie, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickscenefastvideo behind sawyerlicksceneslowvideo
show sawyerlickscenefastvideo behind sawyerlickfastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlicksceneslowvideo
hide sawyerlickfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerlickscenefastx()
screen sawyerlickscenefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerLickCumx")

label SawyerLickCumx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "Oh God, oh..."
scene sawyerlickcum01 with dissolve
play sound "sounds/boymoan03.mp3"
cs01 "You're leaking pre-slime like a faucet! That means you're about to bust your nut!"
scene sawyerlickcum02 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAAH!"
window hide
with hpunch
cs01 "Mmh, yeah, it's FLYING out of your cumslit!"
scene sawyerlickcum03 with dissolve
if age >= 20:
    cs01 "Look at that shot, more manly cum in that single shot than a hundred men combined!"
if age >= 18 and age <= 19:
    cs01 "Look at that shot, more manly teenage cum in that single shot than a hundred men combined!"
window hide
with fastflash
cs01 "As the Captain of the CCPD, I ORDER you to KEEP PUMPING THAT LOAD!"
scene sawyerlickcum04 with dissolve
mc "FFF..FFFFFUUUUCCCKK, RHAAA!"
window hide
with hpunch
cs01 "Keep pumping boy, let it RAIN down upon us!"
window hide
with fastflash
cs01 "Good boy, COVER my body in your red-hot spunk!"
with hpunch
mc "AAAH, AAAAH!"
scene sawyerlickcum05 with dissolve
stop channel1
play sound "sounds/lick03.mp3"
cs01 "Mmmh, it's so thick and chunky. And there's so much of it..."
play sound "sounds/slurp.mp3"
cs01 "I've defeated your mighty cock once ag..."
scene sawyerprefuck01 with dissolve
play sound "sounds/gasp.mp3"
mc "No you haven't! I'm only just STARTING to have fun!"
cs01 "What? You're... LIFTING ME UP WITH YOUR COCK???"
mc "That's right, and I'm going to pound your pussy against the wall now!"
scene sawyerprefuck02 with dissolve
play sound "sounds/moan02.mp3"
mc "So let me help you get these panties down..."
scene sawyerprefuck03 with dissolve
cs01 "You're so... ROUGH. You're gonna fuck my poor pussy while I'm still CAKED in your cum?"
mc "I can't wait Maggie! My cock needs to go down so I can concentrate on the job, remember?"
scene sawyerfuckbackground
show sawyerprefuck04
with dissolve
cs01 "Fine, get on with it, just FUCK M..."
hide sawyerprefuck04
show sawyerprefuck05
with fastdissolve
play sound "sounds/spanking.mp3"
mc "Shut up and let me do the talking!"
hide sawyerprefuck05
show sawyerprefuck04
with fastdissolve
cs01 "Ouch! Why did you do that..."
hide sawyerprefuck04
show sawyerprefuck05
with fastdissolve
play sound "sounds/spanking.mp3"
cs01 "AAAH! I'm at your service!"
scene sawyerprefuck06 with dissolve
mc "Good, now let's start the FUCKING!"
$ sawyerwallslowx = False

label SawyerWallSlowx:
window hide
$ sawyerwallfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallslowvideo behind sawyerwallpovslowvideo
show sawyerwallslowvideo behind sawyerwallfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sawyerwallfastvideo
hide sawyerwallpovslowvideo
show sawyerfuckbackground at sawyerstreetbackground behind sawyerwallslowvideo
if sawyerwallsloxw == False:
    $ sawyerwallslowx = True
    cs01 "You fuck me so good... AAAH!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sawyerwallslowx()
screen sawyerwallslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVSlowx")

label SawyerWallPOVSlowx:
$ sawyerwallfastx = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallpovslowvideo behind sawyerwallslowvideo
show sawyerwallpovslowvideo behind sawyerwallpovfastvideo
show sawyerwallpovslowvideo behind sawyerfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sawyerfuckbackground
hide sawyerwallslowvideo
hide sawyerwallpovfastvideo
if sawyerwallslowx == False:
    $ sawyerwallslowx = True
    cs01 "You fuck me so good... AAAH!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sawyerwallpovslowx()
screen sawyerwallpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SawyerWallPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallSlowx")

label SawyerWallFastx:
$ sawyerwallslowx = False
if sawyerwallfastx == False:
    $ sawyerwallfastx = True
    cs01 "Oh God, fuck me faster, RAM that giant cock in me!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallfastvideo behind sawyerwallpovfastvideo
show sawyerwallfastvideo behind sawyerwallslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sawyerwallslowvideo
hide sawyerwallpovfastvideo
show sawyerfuckbackground at sawyerstreetbackgroundb behind sawyerwallfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerwallfastx()
screen sawyerwallfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerWallCumx")

label SawyerWallPOVFastx:
$ sawyerwallslowx = False
if sawyerwallfastx == False:
    $ sawyerwallfastx = True
    cs01 "Oh God, fuck me faster, RAM that giant cock in me!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallpovfastvideo behind sawyerwallfastvideo
show sawyerwallpovfastvideo behind sawyerwallpovslowvideo
show sawyerwallpovfastvideo behind sawyerfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sawyerfuckbackground
hide sawyerwallfastvideo
hide sawyerwallpovslowvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerwallpovfastx()
screen sawyerwallpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerWallCumx")

label SawyerWallCumx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
cs01 "You're TEARING my pussy apart, please just me give your seed, I WANT IT!"
stop channel1
scene wallsawyercum01 with dissolve
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge02.mp3"
mc "Fuck, OH, here it comes!"
window hide
with fastflash
cs01 "I can take your load, I can tak..."
scene wallsawyercum02 with dissolve
play sound "sounds/moan05.mp3"
cs01 "...AAAAH, I'm cumming!"
window hide
with hpunch
mc "I'm gonna FLOOD your insides Maggie, RHAAA!"
scene wallsawyercum03 with dissolve
play sound "sounds/moan04.ogg"
cs01 "You're pumping so much cum, I can't believe it!"
window hide
with hpunch
play sound "sounds/moan05.mp3"
cs01 "Show me what a STUD you are, pull it out and douse my back with your mighty spunk!"
scene wallsawyercum04 with dissolve
stop channel2
play sound "sounds/boymoan05.mp3"
mc "AAAAH, FUCK!"
window hide
with fastflash
cs01 "That's it, EMPTY YOUR BALLS ON ME, AAAH!" 
scene wallsawyercum05 with dissolve
play sound "sounds/moan06.ogg"
cs01 "Oh my God, you're just a CUM MACHINE!"
window hide
with hpunch
play sound "sounds/splat.ogg"
mc "Y...YES, RHAAA! A little bit more..."
scene wallsawyercum06 with dissolve
play sound "sounds/moan01.mp3"
cs01 "STILL?"
window hide
with fastflash
mc "Fuck yeah, AAAH!"
scene wallsawyercum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Phew..."
cs01 "You've made such a mess... I'm gonna have to call Sergeant Dani to help me clean all this nasty [age]yo spunk..."
mc "Oooh, can I watch?"
cs01 "NO! Go back to your compound and be READY to be be a superhero at last!"
jump SawyerGallery
