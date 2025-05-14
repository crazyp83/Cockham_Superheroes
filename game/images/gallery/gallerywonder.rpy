label WonderGallery:
stop channel3
play sound "sounds/wwomanmusic01.mp3"
scene wonderbackground
show wondermaingallery at gallerypos01 with moveinleft
call screen gallerywonder()
screen gallerywonder():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Wonder Woman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerywonder"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerywonder"), Jump ("WonderGalleryAnim")]    
    if renpy.seen_image("twister01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery01.png" xpos 400 ypos 100
            hover "gallery/wondergallery01.png"
            action Jump ("WonderGallery01")
    text "{font=Gui/Heroes Legend.ttf}Twister Game{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("twister01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("gymwonderbeastcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery02.png" xpos 750 ypos 100
            hover "gallery/wondergallery02.png"
            action Jump ("WonderGallery02")
    text "{font=Gui/Heroes Legend.ttf}Gym Beast{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("gymwonderbeastcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("wonderblowcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery03.png" xpos 1100 ypos 100
            hover "gallery/wondergallery03.png"
            action Jump ("WonderGallery03")
    text "{font=Gui/Heroes Legend.ttf}Agility Training{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("wonderblowcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("stroheimend01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery04.png" xpos 1450 ypos 100
            hover "gallery/wondergallery04.png"
            action Jump ("WonderGallery04")
    text "{font=Gui/Heroes Legend.ttf}Impregnation{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("stroheimend01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("WonderGallery04hint")

    if renpy.seen_image("wonderfightcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery05.png" xpos 400 ypos 380
            hover "gallery/wondergallery05.png"
            action Jump ("WonderGallery05")
    text "{font=Gui/Heroes Legend.ttf}Anal Combat{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("wonderfightcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("wonderyoga12"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery06.png" xpos 750 ypos 380
            hover "gallery/wondergallery06.png"
            action Jump ("WonderGallery06")
    text "{font=Gui/Heroes Legend.ttf}Senses Training{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06
    if renpy.seen_image("wonderyoga12") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("interrogation04"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery07.png" xpos 1100 ypos 380
            hover "gallery/wondergallery07.png"
            action Jump ("WonderGallery07")
    text "{font=Gui/Heroes Legend.ttf}Nazi Sex (not WW){/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext07
    if renpy.seen_image("interrogation04") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("wonderbedtitcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery08.png" xpos 1450 ypos 380
            hover "gallery/wondergallery08.png"
            action Jump ("WonderGallery08")
    text "{font=Gui/Heroes Legend.ttf}BE scene{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext08
    if renpy.seen_image("wonderbedtitcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

    if renpy.seen_image("wonderroompreass01"):
        imagebutton:
            focus_mask True
            idle "gallery/wondergallery09.png" xpos 400 ypos 660
            hover "gallery/wondergallery09.png"
            action Jump ("WonderGallery09")
    text "{font=Gui/Heroes Legend.ttf}Room Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext09
    if renpy.seen_image("wonderroompreass01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("WonderGallery")

label WonderGallery04hint:
show wondermaingallery at gallerypos01
show wondergallery04 at posgalleryhintpic
show wondergalleryhint04 at posgalleryhint
pause
hide wondergalleryhint04 
hide wondergallery04
call screen gallerywonder()
    
label WonderGalleryAnim:
call screen screenanimwonder()
screen screenanimwonder():
    modal True
    add "gallery/wonderbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "wonderanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "wonderanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "wonderanimgym" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "wonderanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimwonder"), SetVariable ("animcount", 1), Jump ("WonderGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Wonder Woman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: Unknown{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}32DD-22-32{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Submission (when bound){/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Teasing{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Cunnilingus{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/wonderanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimwonder")]
    add "gallery/wonderanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimwonder")]
    add "gallery/wonderanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimwonder")]
    add "gallery/wonderanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimwonder")]
            
label WonderGallery01:
stop sound
stop channel3
scene twister01 with dissolve
mc "So first, you have to stand on a yellow and a blue dot, like so."
voice "wonder/twister01"
ww "That sounds easy enough."
scene twister02 with dissolve
mc "Name a color and a body part and I'll have to put that body part on a dot of the color you picked. And you can pick a body part to remove too if you wish."
voice "wonder/twister02"
ww "I see. What a strange game. Then I pick left arm and yellow. And lift your... left leg."
scene twister03 with dissolve
voice "wonder/twister03"
ww "Oh, you're approaching me?"
mc "I can't beat the shit out of you at this game without getting closer."
voice "wonder/twister04"
ww "Oh ho, then come as close as you like."
mc "My turn to pick. I want to see you on all fours. Arms on yellow and blue dots."
scene twister04 with dissolve
voice "wonder/twister05"
ww "You're not making it even slightly hard. Or fun. I'll rise you up both arms on yellow and blue. But also your right leg..."
mc "But... that would mean..."
voice "wonder/twister06"
ww "That you must stand on your hands. Do you have a problem with that?"
scene twister05 with dissolve
mc "Of course not! There you go. I can't see much though. I don't know what to pick..."
voice "wonder/twister07"
ww "Then you miss your turn. My go AGAIN! Both legs forward now!"
mc "What, hang on... I would have to..."
scene twister05b with dissolve
voice "wonder/twister08"
ww "Do a twisting somersault. The game is called twister right?"
scene twister05c with dissolve
play sound "sounds/panting.mp3"
mc "I can do it..."
if mcagility >= 1:
    call screen usepower("useagility", "TwisterLosex", "TwisterWinx") with dissolve

label TwisterLosex:
scene twister05d with dissolve
mc "AAAh, my agility is not high enough!"
scene twister05e with dissolve
play sound "sounds/thud.mp3"
voice "wonder/twister09"
ww "Really? ZERO super-agility in action right there. You LOSE!"
mc "It's unfair, I got to skip my turn!"
scene twister05f with dissolve
voice "wonder/twister10"
ww "Tsss, don't be a sore loser, that's unbecoming of a superhero."
mc "Fine, I won't be. I admit you won... Now is your time to choose what you want me to do... To ANY part of your body..."
voice "wonder/twister11"
ww "Mmmh, let me think. I think I'll choose to SCISSOR your head between my STRONG thighs!"
mc "Err, and then what?"
voice "wonder/twister11b"
ww "You'll see..."
scene twister11 with dissolve
mc "Indeed I see... Please, don't squash my head too much with your powerful thighs, I can barely breathe!"
voice "wonder/twister12"
ww "Then open your mouth and stick your tongue out to let the fresh air in [hero]..."
scene twister12 with dissolve
voice "wonder/twister13"
ww "And use it to lick my pussy. And relieve me of the stress of the day."
mc "Alright Princess Diana, I'll try my best."
window hide
play channel2 "sounds/lick01.ogg"
show twisterwonderlick with dissolve
pause
voice "wonder/twister14"
ww "Yes, just like that... Just like th..."
scene twister15 with dissolve
stop channel2
play sound "sounds/splooge01.mp3"
voice "wonder/twister15"
ww "Aaah, I'm CUMMING!"
window hide
with fastflash
mc "I made you SQUIRT! Like a true SUPER-STUD! And I didn't even use my super-cock."
scene twister16 with dissolve
play sound "sounds/moan02.mp3"
voice "wonder/twister16"
ww "God! I'm emptying my pussyjuices all over your face!"
window hide
with fastflash
mc "You can say that again..."
stop sound
scene twister19 with dissolve
voice "wonder/twister17"
ww "Now I feel better and I'll sleep VERY WELL. Thank you, [name], you can go."
play sound "sounds/slurp.mp3"
mc " Sure, after I've licked my face clean... *lick*"
jump WonderGallery

label TwisterWinx:
scene twister06 with dissolve
play sound "sounds/thud.mp3"
mc "Perfect landing! Now you get to have to reach out for a green dot with your right arm."
scene twister07 with dissolve
voice "wonder/twister18"
ww "Your leg.... It's in the way."
mc "Nothing I can do about that, Princess Diana. You'll just have to lean closer."
scene twister08 with dissolve
voice "wonder/twister19"
ww "It's... too far. I'll try from above."
mc "Let me help you out a bit then..."
scene twister09 with dissolve
voice "wonder/twister20"
ww "What is this? Your phallus is moving!"
scene twister10 with dissolve
voice "wonder/twister21a"
ww "You're blocking my head movement with that thing! How can a man's phallus be THAT BIG???"
mc "I'm entitled to use ANY part of my body to hinder your movements. Do you give up Wonder Woman?"
scene twister20 with dissolve
voice "wonder/twister22"
ww "I... Yes, I give up. You win. This time."
mc "And now you're WONDERING what I have in mind for you, aren't you?"
scene twister21 with dissolve
voice "wonder/twister23"
ww "I'm warning you, you are not TAKING MY VIRGINITY!"
mc "Fine, if you insist, Princess... But I am taking some jug-milk for you then! Come and SIT on my hard prong and feed me those hard milky nipples..."
scene twister22 with dissolve
voice "wonder/twister24"
ww "You're lucky they produce a WONDERFUL quality milk..."
mc "Oooh, I can't wait to taste it!"
scene twister17 with dissolve
play sound "sounds/lick03.mp3"
voice "wonder/twister25"
ww "You were thirsty, weren't you, naughty boy?"
scene twister18 with dissolve
stop sound
mc "Now rub your super-rump on my hard shaft, Wonder Woman..."
voice "wonder/twister26"
ww "That was not really part of the deal. But if that can make you leave my bedroom fully satisfied, then so be it."
window hide

play channel1 "sounds/wank.mp3"
show twistergrindvideo with dissolve
$ renpy.pause(2.0, hard='True')
voice "wonder/twister27"
ww "Like that? Is that what you wanted?"
mc "Y..yeah, that's great... Grind that ass..."
window hide
$ renpy.pause(2.0, hard='True')
pause
mc "Keep going, you're going to make me cum Diana!"
voice "wonder/twister28"
ww "PRINCESS Diana to you!"
window hide
$ renpy.pause(2.0, hard='True')
stop channel1
scene twistergrindcum01 with dissolve
hide twistergrindvideo
play channel2 "sounds/splooge02.mp3"
mc "Oh fuck, I'm blowing SUPER BIG-TIME!"
window hide
with fastflash
voice "wonder/twister29"
ww "Keep your giant boyload on the mat please!"
window hide
with fastflash
mc "I can't... control myself, RHAAA!"
scene twistergrindcum02 with dissolve
mc "Still CUMMING, AAAH!"
window hide
with fastflash
voice "wonder/twister30"
ww "You're just a FILTHY BOY! Cumming ALL OVER THE PLACE like that!"
window hide
with fastflash
mc "I just NEEDED that release, RHAAA!"
stop channel2
scene twistergrindcum03 with dissolve
play sound "sounds/panting.mp3"
voice "wonder/twister31"
ww "Finally... You made such a BIG mess. Fortunately, most of your spunk landed on the twister mat."
mc "That was... sssoo good."
scene twistergrindcum04 with dissolve
voice "wonder/twister32"
ww "I did what you asked of me. And what you asked was VERY NAUGHTY. So time to leave MY bedroom, [name]... And take that cum-soaked mat with you."
mc "Rhuuu... Okay... Your highness..."
jump WonderGallery

label WonderGallery02:
stop sound
stop channel3
scene gymwonderbackground
show wondergymeyeblink
ww "[hero]. Are you here to train your muscles?"
mc "So you're in beast mode? Well, so am I, in SEXY BEAST MODE!"
hide wondergymeyeblink
show wondergym04 at centerleft
with fastdissolve
ww "My shirt doesn't mean it in THAT way. But let's see if you're really a beast like you pretend..."
mc "Ooh Yeah!"
hide wondergym04
show wondergym03 at centerleft
with fastdissolve
ww "Come over here and let's compare MUSCLES!"
play channel1 "sounds/sexy01.mp3"
scene wondergymbeast01 with dissolve
mc "Alright. Get ready to witness some BEASTLY muscles, Diana!"
ww "Oh oh, come closer then and flex next to MY muscles."
scene wondergymbeast02 with dissolve
ww "Are you ready for MAXIMUM BICEPS FLEX?"
mc "Yeah, I'm ready, Diana!"
play sound "sounds/womangroan.mp3"
scene wondergymbeast03 with dissolve
ww "See how my biceps are BULGING [name]?"
mc "I can see... But mine are bulging EVEN MORE!"
scene wondergymbeast04 with dissolve
ww "But can you MAINTAIN then that way for long?"
mc "Of course, as long as I want."
if period == 0:
    scene wondergymbeast05 with dissolve
if period == 1:
    scene wondergymbeast05night with dissolve
ww "Are you sure about that, [hero]?"
mc "Wh... What are you doing, Wonder Woman?"
scene wondergymbeast06 with dissolve
play sound "sounds/boymoan02.mp3"
ww "All the blood seems to be flowing somewhere else right now..."
mc "That's cheating... You're teasing my cock into a hardon!"
ww "I think you need to take that thong off before you rip it apart, don't you think?"
scene wondergymbeast07 with dissolve
ww "Let's see if that cock is as BEASTLY as your muscles..."
mc "Oh, I'll show you..."
ww "Nudge it between my elbow crack. Right against my HARD bicep!"
scene wondergymbeast08 with dissolve
ww "Oh wow, it IS beastly!"
if age >= 20:
    mc "Fifteen inches of prime boymeat for you, Wonder Woman!"
if age >= 13 and age <= 19:
    mc "Fifteen inches of prime teenage boymeat for you, Wonder Woman!"
if age <= 12:
    mc "Fifteen inches of prime pre-teen boymeat for you, Wonder Woman!"
ww "Wonder Woman's biceps will handle this BEAST!"
play channel2 "sounds/boymoan04.mp3"
window hide

label GymWonderBeastx:
hide nexticon
hide pov
hide sceneicon
show gymbeastvideo behind gymbeastpovvideo
$ renpy.pause(1.0, hard=True)
hide gymbeastpovvideo with dissolve
show nexticon:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500
call screen gymwonderbeastx()
screen gymwonderbeastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("GymWonderBeastPOVx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("GymWonderBeastEndx")

label GymWonderBeastPOVx:
hide nexticon
hide pov
hide sceneicon
show gymbeastpovvideo behind gymbeastvideo
$ renpy.pause(1.0, hard=True)
hide gymbeastvideo with dissolve
show nexticon:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500
call screen gymwonderbeastpovx()
screen gymwonderbeastpovx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("GymWonderBeastx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("GymWonderBeastEndx")

label GymWonderBeastEndx:
hide nexticon
hide pov
hide sceneicon
mc "Your bicep squeezing my shaft... It's..."
ww "...more than you can handle [hero]?"
window hide
$ renpy.pause(1.5, hard=True)
stop channel2
play sound "sounds/boyorgasm01.mp3"
scene gymwonderbeastcum01 with dissolve
hide gymbeastvideo
hide gymbeastpovvideo
ww "Cumming already [hero]?"
window hide
with fastflash
scene gymwonderbeastcum02 with dissolve
ww "Maybe I should release the pressure..."
window hide
with fastflash
mc "AAAH, that's bet..."
scene gymwonderbeastcum03 with dissolve
ww "And then INCREASE it!"
window hide
with fastflash
mc "FFF-UUUU-CCCKKKK!"
scene gymwonderbeastcum04 with dissolve
ww "Poor superhero, his BEAST is getting DRAINED by Wonder Woman..."
scene gymwonderbeastcum03 with dissolve
ww "Every time she FLEXES her muscles!"
window hide
with fastflash
mc "AAAh, NOT AGAIN!!!"
scene gymwonderbeastcum04 with dissolve
ww "Will the poor hero ever be allowed to stop cumming?"
window hide
with fastflash
mc "Yes, please, don't..."
scene gymwonderbeastcum05 with dissolve
ww "Oooh, it looks like you still have a LOT of pent-up sperm pressure to RELEASE!"
window hide
with fastflash
mc "Oh God, I... AAAAH!"
scene gymwonderbeastcum04 with dissolve
mc "I beg you Wonder W..."
scene gymwonderbeastcum05 with dissolve
ww "You want me to stop [name]? Then EMPTY THOSE BALLS FOR WONDER WOMAN!"
window hide
with fastflash
mc "I will, I am, AAAH! TOTALLY! RHAAA!"
window hide
with fastflash
ww "I can feel the final GIANT SPURTS erupting...!"
stop sound
stop channel1
scene gymwonderbeastcum06 with dissolve
play sound "sounds/wwomanmusic02.mp3"
ww "And finally, the BEAST IS DEFEATED BY WONDER WOMAN..."
mc "Oooh... I don't even have the strength to train anymore, which is why I came here in the first place..."
stop sound
jump WonderGallery

label WonderGallery03:
stop sound
stop channel3
stop music
play channel1 "sounds/sexy09.mp3"
scene wonderstretch00 with dissolve
ww "Let me start by concentrating my power into my muscles for MAXIMUM agility..."
mc "Oh, so that's how superpowers work then."
scene wonderstretch01 with dissolve
ww "And now hold my foot..."
mc "Like this?"
ww "Yes. Get on your knees and continue holding it..."
scene wonderstretch02 with dissolve
ww "Like so..."
scene wonderstretch03 with dissolve
mc "I see..."
ww "What do you see?"
mc "Well, it was a figure of speech. But I see now."
scene wonderstretch04 with dissolve
mc " * And I like what I see... Her tits are spilling out of her top as she stretches... * "
scene wonderstretch05 with dissolve
mc " * If only there was a camera underneath her that would allow me to get a better view. Like you guys are enjoying. *"
ww "Keep holding my foot, I'm going to bend it now."
scene wonderstretch06 with dissolve
mc " * I'm getting a better view now... * "
ww "And... Let go."
scene wonderstretch07 with dissolve
play sound "sounds/womangroan.mp3"
mc "I'll stretch a bit too..."
ww "That's a good idea, [name]."
scene wonderstretch08 with dissolve
mc "Yeah, I'm stretching. My eyes mainly, but I'm stretching."
scene wonderstretch09 with dissolve
ww "I think there is something else that is STRETCHING..."
scene wonderstretch10 with dissolve
ww "Now do as I do, first stretch your arms..."
scene wonderstretch11 with dissolve
ww "Then your legs..."
scene wonderstretch12 with dissolve
mc "How about I stretch my BICEPS for you, Princess Diana?"
ww "That's very nice, but not useful to acquire Super-Agility, [name]..."
scene wonderstretch13 with dissolve
ww "But I think you are ready for the next phase. Remove your thong, we need to be unemcumbered by these garments..."
mc "Alright!"
scene wonderstretch14night with dissolve
ww "Are you ready, [name]?"
mc "Oh yeah, ready AND naked!"
ww "First, we will do the Rectangle of Dexterity. You go on top since you're a noob."
scene wonderstretch15 with dissolve
mc "How am I doing?"
ww "Very well so far, [name]. The next exercise requires a lot of agility on your part. You must maintain your equilibrium by placing your hands on my upturned chest..."
mc "Err, you don't mind if I put my hands on your tits, then?"
ww "Not at all, I used to do this fun exercise with lots of boys on my island when I was younger."
scene wonderstretch16 with dissolve
mc "It's... kinda wobbly..."
ww "Stay put. Feel the energy of Super-Equilibrium flow through your vestibular system."
mc "That's too much science for a jock like me."
ww "Now let go of your hands and land on me with the tip of your abdomen..."
mc "Hang on..."
scene wonderstretch17 with dissolve
ww "Yes, you did it! This is absolute proof you are becoming VERY agile!"
scene wonderstretch18 with dissolve
ww "Err... But your cock... Still needs to learn to find another place to settle down than next to my cheek..."
mc "It's too big for it to go anywhere else..."
if age >= 20:
    ww" Your fat BULLBALLS look like they are churning up something..."
if age >= 13 and age <= 19:
    ww" Your fat teen BULLBALLS look like they are churning up something..."
if age <= 12:
    ww" Your fat pre-teen BULLBALLS look like they are churning up something..."
scene wonderstretch19 with dissolve
ww "What, you're getting hard while doing the exercise I assigned you???"
mc "AM I? I can't tell from where I'm standing. Or sitting."
ww "Can't you feel all that blood that RUSHED towards your enormous penis?"
mc "I'll go soft once you get me soft... It's the only way out of this sticky situation, Gal. I mean, Princess Diana."
ww "I've had enough of your childish shenanigans! I'm going to pump the seed right out of that filthy dong of your!"
mc "Alright!"
ww "If I manage to make it fit..."
window hide

label GymWonderStretchSlowx:
hide nexticon
hide faster
hide slower
stop channel2
play channel2 "sounds/blow02.mp3"
show wonderblowslowvideo behind wonderblowfastvideo
$ renpy.pause(1.0, hard=True)
hide wonderblowfastvideo with dissolve
stop channel2
play channel2 "sounds/blow02.mp3"
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen gymwonderstretchslowx()
screen gymwonderstretchslowx():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("GymWonderStretchFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymWonderStretchEndx")

label GymWonderStretchFastx:
hide nexticon
hide faster
hide slower
stop channel2
play channel2 "sounds/blow01.mp3"
show wonderblowfastvideo behind wonderblowslowvideo
$ renpy.pause(1.0, hard=True)
hide wonderblowslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen gymwonderstretchfastx()
screen gymwonderstretchfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("GymWonderStretchSlowx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymWonderStretchEndx")

label GymWonderStretchEndx:
hide nexticon
hide slower
hide faster
mc "Princess Diana, I'm.... gonna nut soon!"
stop channel2
scene wonderblowcum01 with dissolve
hide wonderblowslowvideo
hide wonderblowfastvideo
play channel2 "sounds/splooge02.mp3"
mc "FUCK, RHAAA!"
window hide
with fastflash
mc "BLOWING BIG TIME!"
scene wonderblowcum02 with dissolve
ww "Glllbbbb....!!!"
window hide
with fastflash
mc "Hang on, I'll jump back on my feet, keep your throat on my dong, RHAAA!"
scene wonderblowcum03 with dissolve
mc "Fuck yeah, that's better, now I can pump your stomach full!"
window hide
with fastflash
mc "What was that, Princess Diana of Whatever? How do you like my newfound Super-Agility?"
window hide
with fastflash
ww "Mmmmbbbmmmm!!!!"
scene wonderblowcum04 with dissolve
stop channel2
play sound "sounds/boymoan02.mp3"
mc "You're too full? Then I'll dump the rest of my load on your hot bod, RHAAA!"
window hide
with fastflash
play sound "sounds/moan03.mp3"
ww "You're cumming like a STALLION!"
scene wonderblowcum05 with dissolve
play sound "sounds/panting.mp3"
mc "Damn, that was INTENSE. And I displayed some true HERO Super-Agility!"
ww "That wan NOT meant to happen... You fucked my throat and I'm full of your semen!"
mc "Yeah, sure, but it was tasty, right?"
scene wonderblowcum06 with dissolve
ww "I... suppose it was... Very tasty. Please go back to your room, I need to get cleaned up..."
stop sound
stop channel1
stop music
jump WonderGallery

label WonderGallery04:
stop sound
stop channel3
scene stroheimend03 with dissolve
mc "Man, this is fucked up, even for a silly nazi."
scene stroheimend04 with dissolve
cm "Oh dear me, what are we going to do? Poor Princess Diana..."
mc "There might be a way out of this. I need to drown Hitler's seed with my own superior ALPHA-SPUNK!"
scene stroheimend05 with dissolve
cm "What??? This is just..."
bw "...the only way to stop her from getting pregnant with nazi babies and tearing the timeline of our universe apart! Do it, [hero]!"
scene stroheimend03 with dissolve
ww "I'm just a sperm receptacle, like a good housewife... * sob *"
scene stroheimend06 with dissolve
mc "And SPERM you shall receive. LOTS OF IT!"
cm "I can't believe I'm letting my own son impregnate Wonder Woman..."
scene stroheimend07 with dissolve
pg "I don't think I want to see that. Let's clean up around here and find some clues while [name] does his dirty deed..."
scene stroheimend08 with dissolve
mc "Hey, I'm SAVING the timeline of the universe here!"
ww "Don't listen to your sister. I am ready... and submissively willing to receive your virile offering."
scene wonderstroheimprefuck01 with dissolve
play channel1 "sounds/sexy06.mp3"
mc "Now that's what I like to hear! My cum-missile will ravish your uterus until it swells with my baby-making load!"
cm "Please go slowly at first. She needs to get used to your MASSIVE size. It's even bigger than the nazi dildo they used to rape her..."
scene wonderstroheimprefuck02 with dissolve
play sound "sounds/moan05.mp3"
if age >= 20:
    mc "That's just a few inches of my ALPHA-DONG... Get ready for MANY MORE of them!"
if age >= 13 and age <= 19:
    mc "That's just a few inches of my teenage ALPHA-DONG... Get ready for MANY MORE of them!"
if age <= 12:
    mc "That's just a few inches of my pre-teen ALPHA-DONG... Get ready for MANY MORE of them!"
window hide
$ wonderpoundtalkx = False
label WonderSlowFuckx:
hide cum
hide faster
hide slower
hide harder
hide softer
show wonderstroheimfuckslowvideo behind wonderstroheimfuckfastvideo
show wonderstroheimfuckslowvideo behind wonderstroheimhardslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderstroheimfuckfastvideo
hide wonderstroheimhardslowvideo
with dissolve
stop channel2
play channel2 "sounds/womansex06.mp3"
$ wondertalkfastx = False
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen wonderpovslowx()
screen wonderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderFastFuckx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderPoundSlowx")

label WonderFastFuckx:
hide cum
hide faster
hide slower
hide harder
hide softer
if wondertalkfastx == False:
    ww "I have failed in my duty as a woman, my womb deserves a solid pounding!"
    $ wondertalkfastx = True
show wonderstroheimfuckfastvideo behind wonderstroheimfuckslowvideo
show wonderstroheimfuckfastvideo behind wonderstroheimhardfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderstroheimfuckslowvideo
hide wonderstroheimhardfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex06.mp3"
pause
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen wonderpovfastx()
screen wonderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderSlowFuckx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderPoundFastx")

label WonderPoundSlowx:
hide cum
hide faster
hide slower
hide harder
hide softer
if wonderpoundtalkx == False:
    mc "Now who's going to be your daddy, hey?"
    ww "You're my daddy, [name]. FUCK ME HARDER DADDY!"
    $ wonderpoundtalkx = True
show wonderstroheimhardslowvideo behind wonderstroheimfuckslowvideo
show wonderstroheimhardslowvideo behind wonderstroheimhardfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderstroheimfuckslowvideo
hide wonderstroheimhardfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex03.mp3"
$ wondertalkfastx = False
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen wonderpoundslowx()
screen wonderpoundslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderPoundFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderImpregEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderSlowFuckx")

label WonderPoundFastx:
hide cum
hide faster
hide slower
hide harder
hide softer
if wondertalkfastx == False:
    ww "I have failed in my duty as a woman, my womb deserves a solid pounding!"
    $ wondertalkfastx = True
if wonderpoundtalkx == False:
    mc "Now who's going to be your daddy, hey?"
    ww "You're my daddy, [name]. FUCK ME HARDER DADDY!"
    $ wonderpoundtalkx = True
show wonderstroheimhardfastvideo behind wonderstroheimhardslowvideo
show wonderstroheimhardfastvideo behind wonderstroheimfuckfastvideo
$ renpy.pause(1.0, hard='True') 
hide wonderstroheimhardslowvideo
hide wonderstroheimfuckfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex03.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderpoundfastx()
screen wonderpoundfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderPoundSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderImpregEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderFastFuckx")

label WonderImpregEndx:
hide cum
hide faster
hide slower
hide harder
hide softer
mc "That's it, I can feel my balls churning up a..."
stop channel2
scene wonderstroheimcum01 with dissolve
play channel2 "sounds/splooge02.mp3"
play sound "sounds/boymoan05.mp3"
mc "...MONSTERLOAD! AAAH!"
window hide
with fastflash
ww "AAH, I can feel my womb being WHITEWASHED with your seed!"
play sound "sounds/moan06.ogg"
scene wonderstroheimcum02 with hpunch
mc "Damn right, Adolf's spermies won't stand a chance, RHAAA!"
window hide
with fastflash
cm "I hope this works, give her all you've got, sweetie pie!"
scene wonderstroheimcum03 with dissolve
mc "I am, Captain MILF, I am! FILLING HER UP BIG TIME!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
ww "AAAH, my uterus is SWELLLING!"
scene wonderstroheimcum04 with dissolve
ww "Gggg... I'm just a walking womb... My sole duty as a woman is to carry babies... * sob *"
window hide
with fastflash
cm "Err, okay, I think that's enough [name], she's about to BURST!"
stop channel1
stop channel2
scene wonderstroheimcum05 with dissolve
play sound "sounds/moan03.mp3"
mc "That's it. I'm pretty sure I just saved the timeline of our universe."
cm "Hopefully, not TOO much or you'll end up creating an alternate world filled with horse-hung muscle shota boys..."
mc "Mmmh..."
stop sound
stop channel1
stop music
jump WonderGallery

label WonderGallery05:
stop channel3
stop channel2
stop sound
scene wonderfight01
ww "Not COMPLETELY naked of course, I will use my LASSO OF TRUTH!"
if inventorywhip:
    menu:
        "Use your Super-Whip.":
            mc "Well, in that case, I will use my.... err... Nazi super-whip! Which is no longer nazi cos it's mine."
            pass
        "Don't use your Super-Whip.":
            $ nowhip = True
            pass
if inventorywhip == False:
    $ nowhip = True

if nowhip:
    scene wonderfight02b with dissolve
    mc "Well, that's rather unfair, I don't have a lasso!"
    ww "This is none of Wonder Woman's concern! You have Super-Combat abilities, have you not? So USE THEM!"
if nowhip == False:
    scene wonderfight02a with dissolve
    mc "I am READY, Wonder Woman! Prepare to get TROUNCED!"
    ww "Wonder Woman ALWAYS WINS!"
    
scene wonderfight03 with dissolve
play music "sounds/wwomanmusic02.mp3"
$ renpy.pause(1, hard=True)
mc "What the???"
scene wonderfight04 with dissolve
ww "Amazonian STRIKE!"
if nowhip == False:
    scene wonderfight05 with dissolve
    play sound "v03/whip.mp3"
    ww "Missed! You can't use a whip like Wonder Woman can!"
scene wonderfight06 with dissolve
play sound "v03/whip.mp3"
ww "And now you are already at the mercy of my LASSO OF TRUTH!"
mc "Hey, what the hell, untie me, Wonder Woman!"
scene wonderfight07 with dissolve
stop music
play music "sounds/infiltrate.mp3"
ww "Not before Wonder Woman asks you a few questions... Which you will have to answer TRUTHFULLY!"
mc "Err... I don't like that. I don't like that at all..."
scene wonderfight08 with dissolve
ww "Now tell me, [hero], are you a TRUE Super-hero?"
if evilness <= 9:
    mc "Yes I am! I'm on the good boy path!"
    scene wonderfight09b with dissolve
    ww "Good. Because Wonder Woman doesn't like SUPER-VILLAINS!"
    mc "Then we shall fight them TOGETHER, Princess Diana of... err... Themys... errr..."
    scene wonderfight09a with dissolve
    ww "You're so sweet when you try hard to please Wonder Woman. I have another way for you to PLEASE her..."
if evilness >= 10 and evilness <= 12:
    mc "Err, I'm not quite sure at this stage to be honest. I prefer to remain neutral. A bit like Switzerland."
    scene wonderfight09a with dissolve
    ww "So, you won't fight NAZIS then?"
    mc "Ah, I see your point, what with Switzerland and nazi gold and all that, but I WOULD fight Nazis. I just did! TO save you!"
    scene wonderfight09b with dissolve
    ww "That is correct. Although you did MORE than save me. You also EXPLOITED me!"
    mc "So now we're back to just like Switzerland then."
    ww "You deserve a PUNISHMENT. Lick my pussy, and taste it for the LAST TIME in your life, [name]!"
if evilness >= 13:
    mc "I am... Not. I am becoming quite villainous actually."
    scene wonderfight09b with dissolve
    ww "What? But why? You accepted to be a member of the Cockham League of Justice! You are betraying your oath!"
    mc "Oh well, you know, oaths and Super-Villains, pfff."
    ww "Then you deserve a PUNISHMENT. Lick my pussy, and taste it for the LAST TIME in your life, [name]!"
    
scene wonderfight10 with dissolve
stop music
play music "sounds/sexy04.mp3"
play sound "sounds/lick03.mp3"
ww "Wonder Woman wants a GOOD, CLEAN PUSSY-LICKING TRIM DOWN THERE!"
scene wonderfight11 with dissolve
play sound "sounds/lick02.mp3"
ww "Mmmh, yeah, just like this... Keep going, [name]..."
scene wonderfight12 with dissolve
play sound "sounds/moan05.mp3"
ww "AAAH! You made Wonder Woman cum!... Mmmh,that's a good boy."
mc "Can you untie me now please?"
if evilness >= 13:
    scene wonderfight13 with dissolve
    ww "I will, but I also must warn you, in the spirit of fair-play which I must abide to, that I plan to let Captain MILF know of your villainous intentions..."
    mc "Err, sure, whatever, I ain't scared. * Shit, I'm done for if she grasses on me... *"
    jump WonderFight02x
if evilness <= 12:
    scene wonderfight13 with dissolve
    ww "I will, and since you are not a concealed Super-Villain, despite my suspicions, Wonder Woman will train you in Super-Combat Level 2."
    mc "Alright! Getting closer to that upgrade everyone's been waiting for..."
    jump WonderFight02x
label WonderFight02x:
scene wonderfight14 with dissolve
ww "And now, kiss my hand, like a loyal and inferior male subject in my home island would do... Considering I'm a Princess."
play sound "sounds/kiss.mp3"
scene wonderfight14 with dissolve
if evilness >= 13:
    scene wonderfight18 with dissolve
    ww "You are free to go. After Woman Woman once again PROVED her superiority over mere male mortals."
    scene wonderfight19 with dissolve
    mc "* She's turning her back to me, time to STRIKE! *"
    stop music
    play music "v03/fightmusic.mp3"
    scene wonderfight21 with dissolve
    play sound "sounds/punch.mp3"
    ww "You thought Wonder Woman had not sensed your evil intent?"
    mc "Ouch! Not in my cock!"
    scene wonderfight22 with dissolve
    mc "FUCK ME! That hurts like hell!"
    scene wonderfight20 with dissolve
    ww "I will give you one last chance, a chance to REDEEM yourself. Prepare to FIGHT in pure hand-to-hand Amazonian COMBAT!"    
    jump WonderFight03bx    
if evilness <= 12:
    scene wonderfight18 with dissolve
    ww "After Woman Woman once again PROVED her superiority over mere male mortals, you may rise again and get prepared for your training."
    mc "Gee, thank you, oh Mighty and Gracious Highness Princess Diana..."
    jump WonderFight03x

label WonderFight03x:
stop music
play music "v03/fightmusic.mp3"
scene wonderfight20 with dissolve
ww "We shall train without equipment. In pure hand-to-hand Amazonian COMBAT!"
label WonderFight03bx:
scene wonderfight02b with dissolve
mc "Fine by me! This time, I'll prove my worth! HEEE-YAH!"
scene wonderfight21 with dissolve
play sound "sounds/punch.mp3"
ww "You need to be FASTER and more Super-Agile if you plan to beat Wonder Woman!"
mc "Ouch! Not in my cock!"
label WonderFight04x:
scene wonderfight22 with dissolve
mc "FUCK ME! That hurts like hell!"
ww "You won't be impregnating anyone anytime soon, [hero]!"
scene wonderfight23 with dissolve
mc "That's it, I've had enough of this. You want Super-Fast Combat, I'll give you Super-Fast Combat!"
scene wonderfight24 with dissolve
play sound "sounds/slap.mp3"
mc "Not my dong again!"
ww "Still not fast enough for Wonder Woman! FOCUS, if you want to have any hope of beating me!"
scene wonderfight25 with dissolve
play sound "sounds/thud.mp3"
mc "AAAH!"
ww "Wonder is easily disposing of her opponent!"
mc "* But I sense some weakness in her move... *"
scene wonderfight26 with dissolve
mc "That's it, I'm holding you in a tight armlock now!"
ww "UUURGH, I will not submit, Wonder Woman never subm..."
scene wonderfight27 with dissolve
mc "And now my Super-Strength in action, Princess Diana!"
ww "Let me down!"
stop music
play music "sounds/sexy13.mp3"
scene wonderfight28 with dissolve
mc "I don't think so, I have the upper hand and I intend to KEEP IT! Speaking of upper hand..."
scene wonderfight29 with dissolve
mc "Take THAT hand up your poontang!"
play sound "sounds/moan05.mp3"
ww "WHHHAAAA!!!!"
scene wonderfight28 with dissolve
mc "Sorry, I didn't hear. You were saying?"
scene wonderfight29 with dissolve
play sound "sounds/moan04.ogg"
ww "UUUUH..."
scene wonderfight30 with dissolve
play sound "sounds/moan06.ogg"
mc "I'm enjoying this. And I think your pussy is too..."
window hide
play music [ "sounds/moan04.ogg", "<silence 1.0>"]
scene wonderfightfistfuck
$ renpy.pause(3.0, hard='True')
pause
ww "Please, stop it, you might hurt OUR baby!"
scene wonderfight28 with dissolve
mc "You're right, and I have an even better idea. I'm going to SODOMIZE YOU WONDER WOMAN!"
scene wonderfight31 with dissolve
mc "First, I will BIND you in my muscular arms with a Full Nelson lock..."
ww "No!!! I... I can't fight you anymore... I..."
mc "You will submit and recognize that I am BETTER than you at Super-Combat Wonder Woman?"
ww "No! I... can't... MUST... FIGHT... * sigh *"
scene wonderpreanal01 with dissolve
play sound "sounds/thud.mp3"
if age >= 20:
    mc "Don't fight it! Feel how HEAVY and powerful my fucktool is... THIS is going to enter you backdoor!"
if age >= 18 and age <= 19:
    mc "Don't fight it! Feel how HEAVY and powerful my teenage fucktool is... THIS is going to enter you backdoor!"
ww "* sob * I deserve it, I am just a woman and must satisfy a man's sexual desires to the best of my ability."
scene wonderpreanal02 with dissolve
play sound "sounds/moan04.ogg"
mc "You go that right, Wonder Woman!"
ww "It's so BIG... Tooo big... My poor ass..."
mc "Too late to back down, here we go!"
play channel2 "sounds/womansex01.mp3"

$ wonderanalslowx = False
$ wonderanalfastx = False
$ wonderanalhardx = False

label WonderAnalSlowx:
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalslowvideo behind wonderanalfastvideo
show wonderanalslowvideo behind wonderanalfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalfastvideo
hide wonderanalfrontslowvideo
with dissolve
play channel2 "sounds/womansex01.mp3"
$ wonderanalfastx = False
if wonderanalslowx == False:
    ww "My ass is yours, [hero]! Pound it like the filthy underserving hole it is!"
    $ wonderanalslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500     
call screen wonderanalslowx()
screen wonderanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFrontSlowx")

label WonderAnalFastx:
$ wonderanalslowx = False
if wonderanalfastx == False:
    ww "Thrust faster, please!"
    mc "Damn, you really want that cock, don't you, Servile Wonder Woman!"
    $ wonderanalfastx = True
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalfastvideo behind wonderanalslowvideo
show wonderanalfastvideo behind wonderanalfrontfastvideo
show wonderanalfastvideo behind wonderanalhardvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalslowvideo
hide wonderanalfrontfastvideo
hide wonderanalhardvideo
with dissolve
play channel2 "sounds/womansex04.mp3"
pause
window hide
show harder:
    xpos 1650 ypos 1020    
show slower:
     xpos 50 ypos 500     
show zoomicon:
     xpos 1700 ypos 500     
call screen wonderanalfastx()
screen wonderanalfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalSlowx")
    button:
        xpos 1650
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalHardx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFrontFastx")

label WonderAnalFrontSlowx:
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalfrontslowvideo behind wonderanalslowvideo
show wonderanalfrontslowvideo behind wonderanalfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalslowvideo
hide wonderanalfrontfastvideo
with dissolve
play channel2 "sounds/womansex01.mp3"
$ wonderanalfastx = False
if wonderanalslowx == False:
    ww "My ass is yours, [hero]! Pound it like the filthy underserving hole it is!"
    $ wonderanalslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderanalfrontslowx()
screen wonderanalfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalSlowx")

label WonderAnalFrontFastx:
$ wonderanalslowx = False
if wonderanalfastx == False:
    ww "Thrust faster, please!"
    mc "Damn, you really want that cock, don't you, Servile Wonder Woman!"
    $ wonderanalfastx = True
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalfrontfastvideo behind wonderanalfastvideo
show wonderanalfrontfastvideo behind wonderanalfrontslowvideo
show wonderanalfrontfastvideo behind wonderanalfronthardvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalfastvideo
hide wonderanalfrontslowvideo
hide wonderanalfronthardvideo
with dissolve
play channel2 "sounds/womansex04.mp3"
pause
window hide
show harder:
    xpos 1650 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen wonderanalfrontfastx()
screen wonderanalfrontfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontSlowx")
    button:
        xpos 1650
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalZoomHardx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFastx")

label WonderAnalHardx:
if wonderanalhardx == False:
    mc "Now I'm gonna POUND that ass to OBLIVION until you SUBMIT!"
    $ wonderanalhardx = True
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalhardvideo behind wonderanalfastvideo
show wonderanalhardvideo behind wonderanalfronthardvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalfastvideo
hide wonderanalfronthardvideo
with dissolve
play channel2 "sounds/womansex05.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show zoomicon:
     xpos 1700 ypos 500     
call screen wonderanalhardx()
screen wonderanalhardx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalZoomHardx")

label WonderAnalZoomHardx:
if wonderanalhardx == False:
    mc "Now I'm gonna POUND that ass to OBLIVION until you SUBMIT!"
    $ wonderanalhardx = True
window hide
hide cum
hide harder
hide softer
hide slower
hide faster
hide zoomicon
hide sceneicon
show wonderanalfronthardvideo behind wonderanalfastvideo
show wonderanalfronthardvideo behind wonderanalhardvideo
$ renpy.pause(1.0, hard='True')
hide wonderanalfastvideo
hide wonderanalhardvideo
with dissolve
play channel2 "sounds/womansex05.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen wonderanalfronthardx()
screen wonderanalfronthardx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalHardx")

label WonderAnalEndx:
window hide
hide cum
hide zoomicon
hide harder
hide softer
hide faster
hide slower
hide front
if age >= 20:
    ww "AAAH, your monster cock is DESTROYING MY ANAL HOLE!"
if age >= 18 and age <= 19:
    ww "AAAH, your teenage monster cock is DESTROYING MY ANAL HOLE!"
scene wonderfightcum01 with dissolve
stop channel2
play channel2 "sounds/splooge02.mp3"
play sound "sounds/boyorgasm01.mp3"
mc "Not totally yet, I'll destroy it NOW, WITH MY CUM! RHAAA!"
window hide
with hpunch
ww "Sssoo STRONG! I'm cumming too!"
scene wonderfightcum02 with dissolve
mc "I'm BURSTING, my cock won't stop SPEWING, AAAH!"
window hide
with fastflash
ww "OOOOH!"
scene wonderfightcum03 with dissolve
mc "I need... to..."
window hide
with fastflash
if age >= 20:
    ww "Cover me in your spunk, [hero], I'm just a cum dump for your giant phallus!"
if age >= 18 and age <= 19:
    ww "Cover me in your spunk, [hero], I'm just a cum dump for your giant teenage phallus!"
scene wonderfightcum04 with dissolve
stop channel2
mc "FUCK YEAH!"
window hide
with hpunch
ww "Sssooo much cum! It's flying EVERYWHERE!"
scene wonderfightcum05 with dissolve
play sound "sounds/panting.mp3"
ww "I'm totally soaked in your cum. I belong to you now... * sigh *"
if evilness >= 13:
    mc "Now before you go, you're going to keep quiet and not say ANYTHING to Captain MILF, you hear me? If you disobey, I'll brutally anal-rape you AGAIN!"
    ww "Y...Yes, [name] , I'll do as I'm told by my superior male Master... * sob *"
    mc "That's a good girl. Now we can go back to the gallery and forget about what happened here."
    stop sound
    stop channel1
    stop music
    jump WonderGallery
if evilness <= 12:
    mc "Well, you're the future mother of my offspring, so that's alright."
    ww "Y...Yes, [name] , I'm just your breeding wife now. * sob *"
    mc "Ok, let's not push it, I was only trying to get better at Super-Combat, not humiliate you, Wonder Woman... We'd better go back to the gallery."
stop sound
stop channel1
stop music
jump WonderGallery

label WonderGallery06:
stop channel3
stop channel2
stop sound
scene gymwidowbackground
show level02wondergym01 at centerleft
with dissolve
show level02wondergym01 at centerleft:
    breathe
ww "You need to prep your body. You choose your own method. I'll be doing squats. The important thing is to feel TENSE afterwards."
mc "That's weird, it's totally the opposite of what Powergirl told me."
hide level02wondergym01
show level02wondergym05 at centerleft
with fastdissolve
ww "She was only teaching you Level01 Super-Senses. For Level02, you need to up your game!"
mc "Right, right, totally makes super-sense now. I'll be doing curls then, I'm good at that lately."

window hide
stop music
play music "sounds/gymmusic.mp3"

label WonderSquatx: 
hide mccurlicon
hide wondersquaticon
show wondersquatvideo behind mcupcurlvideo
hide mcupcurlvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show mccurlicon:
     xpos 1700 ypos 500     

call screen wondersquatx()
screen wondersquatx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McUpCurlx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderSensesTrainEndx")

label McUpCurlx:
hide mccurlicon
hide wondersquaticon
show mcupcurlvideo behind wondersquatvideo
hide wondersquatvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show wondersquaticon:
     xpos 50 ypos 500     

call screen mcupcurlx()
screen mcupcurlx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderSquatx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderSensesTrainEndx")

label WonderSensesTrainEndx:
hide mccurlicon
hide wondersquaticon
stop music
scene wondersquatend01 with dissolve
ww "I'm done. Let me check to see if YOUR body is ready..."
scene wondersquatend02 with dissolve
ww "Mine is definitely all PUMPED UP and TENSE!"
scene wondersquatend03 with dissolve
ww "Now keep those curls UP so your body is totally TENSED UP!"
scene wondersquatend04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1, hard=True)
ww "Not bad... Your muscles are indeed ROCK-SOLID... Let's begin FURTHER TRAINING AND TENSING. Get on the floor."
scene wonderyoga09 with dissolve
ww "I see. Some muscles might need a bit more TENSING."
scene wonderyoga10 with dissolve
ww "Like this one for example..."
scene wonderyoga11 with dissolve
play sound "sounds/bonecrack.mp3"
mc "I'm tensing, I'm tensing! You can stop now!"
scene wonderyoga10 with dissolve
ww "Alright, just..."
scene wonderyoga11 with dissolve
play sound "sounds/bonecrack.mp3"
ww"...one MORE time!"
scene wonderyoga12 with dissolve
ww "Now concentrate intensely. InTENSEly, get it?"
mc "No, I don't get it. Was that supposed to be funny?"
scene wonderyoga13 with dissolve
play channel1 "v031/radiation01.mp3"
ww "And RELEASE that stored-up muscle energy around you through the power of your mind."
scene wonderyoga14 with dissolve
ww "Now that the Super-Energy is floating in the ether, you should experience enhanced Super-Senses."
scene wonderyoga15 with dissolve
mc "I can... hear voices... A girl... flying above the compound... It's Powergirl!"
play sound "sounds/nightsounds.mp3"
scene wonderyoga16 with dissolve
pg "* Are you talking to me [name]? Where are you? I can hear you but I can't see you. Are you Super-Sensing me?*"
scene wonderyoga17 with dissolve
stop sound
ww "It worked, but now I need to DE-tense you quickly, or the side effects will be..."
scene wonderyoga18 with dissolve
play sound "sounds/ripping.mp3"
ww "...THIS, what I FEARED!"
stop channel1
scene wonderyoga19 with dissolve
play sound "sounds/thud.mp3"
if age >= 20:
    ww "You've RIPPED your thong to pieces! And now your cock is SUPER-TENSE!"
if age >= 18 and age <= 19:
    ww "You've RIPPED your thong to pieces! And now your teen cock is SUPER-TENSE!"
scene wonderyoga20 with dissolve
play sound "sounds/panting.mp3"
mc "FUCK, I'm SSSOOO HARD! Please do something about it, Princess Diana of...errr. Themys... something!"
ww "THEMYSCIRA! Alright, I suppose I put you in this predicament, so Wonder Woman will come to your RESCUE!"
stop music
play music "sounds/sexy03.mp3"
scene wonderyoga21 with dissolve
play sound "sounds/slurp.mp3"
ww "First, she will use her Super-Mouth to prep your cum-laden MONSTERBALLS for their upcoming release..."
scene wonderyoga22 with dissolve
play sound "sounds/lick01.ogg"
ww "Then the arm-thick root of your shaft..."
scene wonderyoga23 with dissolve
play sound "sounds/lick02.mp3"
mc "Oh God... Keep going!"
scene wonderyoga24 with dissolve
play sound "sounds/lick03.mp3"
if age >= 20:
    ww "Now stand still and let my mouth take care of your aching hardon..."
if age >= 18 and age <= 19:
    ww "Now stand still and let my mouth take care of your aching teenage hardon..."
mc "Y... Yes Princess Diana. Please be quick though, I don't know how long I can survive being that HARD!"
$ wonderblowfuckfastx = False
$ wonderblowfuckslowx = False

label WonderBlowShortSlowx:
window hide
$ wonderblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowshortslowvideo behind wonderblowshortfastvideo
show wonderblowshortslowvideo behind wonderblowshortpovslowvideo
show wonderblowshortslowvideo behind wonderblowhardslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide wonderblowshortfastvideo
hide wonderblowshortpovslowvideo
hide wonderblowhardslowvideo
$ wonderblowfuckfastx = False
if wonderblowfuckslowx == False:
    mc "AAAh, this is so good, Wonder Woman!"
    $ wonderblowfuckslowx = True
window hide
pause
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowshortslowx()
screen wonderblowshortslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVSlowx")

label WonderBlowShortFastx:
$ wonderblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowshortfastvideo behind wonderblowshortslowvideo
show wonderblowshortfastvideo behind wonderblowshortpovfastvideo
show wonderblowshortfastvideo behind wonderblowhardfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide wonderblowshortslowvideo
hide wonderblowshortpovfastvideo
hide wonderblowhardfastvideo
$ wonderblowfuckslowx = False
if wonderblowfuckfastx == False:
    mc "Mmmh, my cock LIKES that!"
    $ wonderblowfuckfastx = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowshortfastx()
screen wonderblowshortfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVFastx")

label WonderBlowShortPOVSlowx:
$ wonderblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowshortpovslowvideo behind wonderblowshortslowvideo
show wonderblowshortpovslowvideo behind wonderblowshortpovfastvideo
show wonderblowshortpovslowvideo behind wonderblowhardpovslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide wonderblowshortslowvideo
hide wonderblowshortpovfastvideo
hide wonderblowhardpovslowvideo
$ wonderblowfuckfastx = False
if wonderblowfuckslowx == False:
    mc "AAAh, this is so good, Wonder Woman!"
    $ wonderblowfuckslowx = True
window hide
pause

show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowshortpovslowx()
screen wonderblowshortpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortSlowx")

label WonderBlowShortPOVFastx:
$ wonderblowharderx = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowshortpovfastvideo behind wonderblowshortpovslowvideo
show wonderblowshortpovfastvideo behind wonderblowshortfastvideo
show wonderblowshortpovfastvideo behind wonderblowhardpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide wonderblowshortpovslowvideo
hide wonderblowshortfastvideo
hide wonderblowhardpovfastvideo
$ wonderblowfuckslowx = False
if wonderblowfuckfastx == False:
    mc "Mmmh, my cock LIKES that!"
    $ wonderblowfuckfastx = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowshortpovfastx()
screen wonderblowshortpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortFastx")

label WonderBlowHardSlowx:
if wonderblowharderx == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharderx = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowhardslowvideo behind wonderblowhardfastvideo
show wonderblowhardslowvideo behind wonderblowhardpovslowvideo
show wonderblowhardslowvideo behind wonderblowshortslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide wonderblowhardfastvideo
hide wonderblowhardpovslowvideo
hide wonderblowshortslowvideo

show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowhardslowx()
screen wonderblowhardslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEndx")

label WonderBlowHardFastx:
if wonderblowharderx == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharderx = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowhardfastvideo behind wonderblowhardslowvideo
show wonderblowhardfastvideo behind wonderblowhardpovfastvideo
show wonderblowhardfastvideo behind wonderblowshortfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide wonderblowhardslowvideo
hide wonderblowhardpovfastvideo
hide wonderblowshortfastvideo

window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowhardfastx()
screen wonderblowhardfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEndx")

label WonderBlowHardPOVSlowx:
if wonderblowharderx == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharderx = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowhardpovslowvideo behind wonderblowhardslowvideo
show wonderblowhardpovslowvideo behind wonderblowhardpovfastvideo
show wonderblowhardpovslowvideo behind wonderblowshortpovslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide wonderblowhardslowvideo
hide wonderblowhardpovfastvideo
hide wonderblowshortpovslowvideo

show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowhardpovslowx()
screen wonderblowhardpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEndx")

label WonderBlowHardPOVFastx:
if wonderblowharderx == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharderx = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
show wonderblowhardpovfastvideo behind wonderblowhardpovslowvideo
show wonderblowhardpovfastvideo behind wonderblowhardfastvideo
show wonderblowhardpovfastvideo behind wonderblowshortpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide wonderblowhardpovslowvideo
hide wonderblowhardfastvideo
hide wonderblowshortpovfastvideo

window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowhardpovfastx()
screen wonderblowhardpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEndx")

label WonderBlowEndx:
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
stop channel1
mc "That's it, I can feel my cum boiling, it's surging through my shaft, sssooo goood..."
play channel1 "sounds/boyorgasm01.mp3"
scene wonderblowhardcum01 with dissolve
mc "...IT'S CO-O-MING!"
play sound "v032/gulp.mp3"
window hide
with fastflash
mc "... BIG TIME, AAAH!"
scene wonderblowhardcum02 with dissolve
play sound "sounds/splooge01.mp3"
ww "Mmmmgggg!"
window hide
with hpunch
mc "Your mouth... It's SUCKING the cum out of my dong!"
scene wonderblowhardcum03 with dissolve
play sound "sounds/panting.mp3"
ww "I need to BREATHE! But you, don't you dare stop SPEWING that nasty load!"
window hide
with fastflash
mc "I won't, I Promise, AAAH!"
scene wonderblowhardcum04 with dissolve
ww "Jizz on me! Jizz on me! JIZZ ON ME!"
window hide
with vpunch
mc "I am! RHAAA!"
scene wonderblowhardcum05 with dissolve
stop channel1
play sound "sounds/boymoan.mp3"
ww "Once again, Wonder Woman has tamed your wild beast. Sort of."
stop channel1
stop channel3
stop music
jump WonderGallery

label WonderGallery07:
stop sound
stop channel3
play music "sounds/underworld.mp3"
scene interrogation01 with fade
mc "Well, well, well. If it isn't my two favorite nazi girls. Tied up like hogs."
scene interrogation02 with dissolve
ig "Vat do you want? I have nothing to say to YOU!"
mc "We'll see about that..."
ig "You can torture me as much as you like, I von't say a vord!"       
scene interrogation03 with dissolve
mc "Who said I was going to torture you? I just want to have a feel of those nice funbags of yours... And play with your uptight German pussy."
ig "You're just a PERVERT!"
scene interrogation04 with dissolve
play sound "sounds/lick01.ogg"
mc "* lick * Yeah, maybe. But I don't think you are as frigid as you make it out to be."
ig "V... Vat are you doing?"
fr "Don't let zis disgusting American Schwein get to you! BE FRIGID, INGRID!"
scene interrogation05 with dissolve
play sound "sounds/moan02.mp3"
ig "N...Nein! I am zo sensitive down there...."
mc "I can see that, you're all wet..."
scene interrogation06 with dissolve
mc "Those big babies must be aching to release their warm milk..."
play sound "sounds/moan01.mp3"
ig "I must... resist!"
scene interrogation07 with dissolve
play sound "sounds/womancum02.mp3"
ig "AAAH! Das ist zo GUT!"
scene interrogation08 with dissolve
mc "Well, that was fast, I must be making you very HORNY..."
ig "NEIN! I vas... just... I needed..."
mc "Say no more and get some rest."
scene interrogation09 with dissolve
mc "Now it's your turn, Frieda. You must be horny too, your nipples are all hard..."
fr "No they're not! It's just...cold in here."
scene interrogation10 with dissolve
mc "Well, allow me to warm them up then. We wouldn't want our guests to catch a nipple cold."
fr "Filthy Schwein! Don't touch me, you are from an inferior race!"
scene interrogation11 with dissolve
mc "Don't say that, it's kind of offensive, and give me a kiss..."
fr "Never! My lips are reserved for Colonel Stroheim! He's a nice man from the SUPERIOR race!"
scene interrogation12 with dissolve
mc "Maybe I asked too nicely... You're going to change your tune, Frieda. Once you meet..."
scene interrogation13 with dissolve
mc "...My giant boyhood..."
fr "Wat is zis thing? It's..."
scene interrogation14 with dissolve
play sound "sounds/gasp.mp3"
mc "...HUGE, right?"
fr "Mein Gott! It's zo much bigger than Colonel Stroheim's bratwurst!"
scene interrogation15 with dissolve
mc "That's right. It's much more POWERFUL too. I'll show you..."
window hide
scene friedatits with fastdissolve
play channel2 [ "sounds/slap.mp3", "<silence .75>" ]
$ renpy.pause(2.0, hard='True')
fr "You are BRUISING mein chest... But it's a gut pain... I like it... I am supposed to be SADISTIC, wat is happening?..."
pause
if age >= 20:
    mc "You're just falling for my SUPER-COCK. It's a perfectly natural reaction."
if age >= 18 and age <= 19:
    mc "You're just falling for my TEEN SUPER-COCK. It's a perfectly natural reaction."
stop channel2
scene interrogation19 with dissolve
mc "Shut up, I'm not done proving my COCK SUPERIORITY to you..."
stop music
play music "sounds/sexy02.mp3"
scene interrogation20 with dissolve
play channel1 "sounds/moan02.mp3"
fr "Wat are you doing????"
mc "Just using my cock as a pussy crank. You'll see..."

label FriedaLiftSlowx:
window hide
show friedaliftslowvideo behind friedaliftfastvideo
pause 1.0
hide friedaliftfastvideo
hide faster
hide slower
with dissolve
fr "I can't believe this is possible!"
mc "You'd better believe it..."
show faster:
     xpos 1700 ypos 500
call screen friedaliftslowx()
screen friedaliftslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaLiftFastx")

label FriedaLiftFastx:
window hide
show friedaliftfastvideo behind friedaliftslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedaliftslowvideo
hide faster
hide slower
with dissolve
mc "See? My tireless [age]yo donkey-dick can do this all day..."
fr "Mein Gott, AAAH!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
call screen friedaliftfastx()
screen friedaliftfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaLiftSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaLiftEndx")

label FriedaLiftEndx:
fr "Mein pussy is getting zo wet..."
scene interrogation21 with dissolve
stop channel1
play sound "sounds/mangrunt01.mp3"
mc "Houston, we have LIFT OFF!"
play sound "sounds/moan04.ogg"
fr "AAAH, you're such a young STALLION!"
scene interrogation22 with dissolve
mc "That's right, so you'd better show your appreciation for this SUPER-COCK!"
scene interrogation21 with dissolve
fr "But you're not Aryan, I can't let y..."
scene interrogation22 with dissolve
mc "What did you say? This SUPERIOR COCK isn't good enough for you?"
fr "Nein, nein! It's gut, I..."
scene interrogation23 with dissolve
play sound "sounds/womancum02.mp3"
mc "No more superior cock for you! Until you tell me EVERYTHING!"
scene interrogation24 with dissolve
fr "Untie me and I will talk. If you prove to me you are from the Superior race..."
mc "Alright, let's see now..."
scene interrogation25 with dissolve
mc "What is Colonel Stroheim up to? Where did he go?"
ig "Don't talk! We vowed allegiance to our Führer! Heil Hitler!"
scene interrogation26 with dissolve
fr "But maybe he's an Aryan, Ingrid. One of ours. If he shows us his Race Papieren..."
mc "I don't have any \"papers\". But I am from the Superior Race. The race of SUPER-HEROES! And I'll PROVE it to you on your little friend!"
scene interrogation27 with dissolve
mc "Your turn to feel the POWER of my mighty pillar!"
ig "W...Wat?"
scene interrogation28 with dissolve
mc "Can you feel the HEAT radiating from its massive girth yet?"
ig "I... Yes, I suppose it is sehr HOT!"
scene interrogation29 with dissolve
mc "Let me place it between your thighs..."
mc "And..."
play channel1 "sounds/moan02.mp3"
play channel2 "sounds/wetmassage.mp3"

label IngridLiftSlowx:
window hide
show ingridliftslowvideo behind ingridliftfastvideo
pause 1.0
hide ingridliftfastvideo
hide faster
hide slower
with dissolve
mc "Does it feel like a SUPERIOR COCK to you yet?"
ig "I... Nein, I must resist!" 
show faster:
     xpos 1700 ypos 500
call screen ingridliftslowx()
screen ingridliftslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridLiftFastx")

label IngridLiftFastx:
window hide
show ingridliftfastvideo behind ingridliftslowvideo
pause 1.0
hide ingridliftslowvideo
hide faster
hide slower
with dissolve
mc "How about if I lift your whole body up even faster? Can you feel its sheer SUPER-POWER now?"
ig "AAAH! You are a sehr big POWERFUL boy, JA!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
call screen ingridliftfastx()
screen ingridliftfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridLiftSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridLiftEndx")

label IngridLiftEndx:
hide nexticon
hide faster
hide slower
mc "Let me emphasize how STRONG it is right now..."
scene interrogation30 with dissolve
stop channel1
stop channel2
play sound "v032/womancum04.mp3"
mc "There! Did you feel that?"
ig "JA, JA, I DID!"
scene interrogation31 with dissolve
fr "He is zo STRONG! Stronger than the Aryan boys I met back in Bavaria vhen I was a horny teenager!"
ig "I know, zis is so embarassing for our superior race..."
scene interrogation32 with dissolve
mc "Next round. My cock versus your Nazi ass!"
ig "NEIN! You are crazy, it vill never fit!"
scene interrogation33 with dissolve
play sound "sounds/moan05.mp3"
mc "I don't see any fitting issues so far..."
ig "AAAH! It feels like I am being IMPALED on your Lieb-Sword!"
play channel1 "sounds/moan03.mp3"
$ ingridanalfuckslowx = False

label IngridAnalFuckSlowx:
$ ingridanalfuckfastx = False
window hide
show ingridanalslowvideo behind ingridanalfastvideo
show ingridanalslowvideo behind ingridanalcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ingridanalfastvideo
hide ingridanalcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckslowx == False:
    $ ingridanalfuckslowx = True
    ig "Your ding-dong... It is zo fucking BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ingridanalfuckslowx()
screen ingridanalfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckPOVSlowx")

label IngridAnalFuckFastx:
$ ingridanalfuckslowx = False
window hide
show ingridanalfastvideo behind ingridanalslowvideo
show ingridanalfastvideo behind ingridanalcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ingridanalcloserfastvideo
hide ingridanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckfastx == False:
    $ ingridanalfuckfastx = True    
    if age >= 20:
        ig "Mein Gott! Zat giant horsedick is stretching mein ass wider than the Siegfried line!"
    if age >= 18 and age <= 19:
        ig "Mein Gott! Zat giant teen horsedick is stretching mein ass wider than the Siegfried line!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ingridanalfuckfastx()
screen ingridanalfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckPOVFastx")

label IngridAnalFuckPOVSlowx:
$ ingridanalfuckfastx = False
window hide
show ingridanalcloserslowvideo behind ingridanalslowvideo
show ingridanalcloserslowvideo behind ingridanalcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ingridanalcloserfastvideo
hide ingridanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckslowx == False:
    $ ingridanalfuckslowx = True
    ig "Your ding-dong... It is zo fucking BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ingridanalcloserfuckslowx()
screen ingridanalcloserfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckSlowx")

label IngridAnalFuckPOVFastx:
$ ingridanalfuckslowx = False
window hide
show ingridanalcloserfastvideo behind ingridanalfastvideo
show ingridanalcloserfastvideo behind ingridanalcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ingridanalfastvideo
hide ingridanalcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
if ingridanalfuckfastx == False:
    $ ingridanalfuckfastx = True    
    if age >= 20:
        ig "Mein Gott! Zat giant horsedick is stretching mein ass wider than the Siegfried line!"
    if age >= 18 and age <= 19:
        ig "Mein Gott! Zat giant teen horsedick is stretching mein ass wider than the Siegfried line!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ingridanalcloserfuckfastx()
screen ingridanalcloserfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckFastx")

label IngridAnalFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
mc "It's time for me to fill up that dirty hole with my SUPERIOR SPUNK!"
fr "If he totally fills you up, then he IS from the Superior Race!"
scene ingridanalcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "v031/boyorgasm02.mp3"
mc "That's it, take THAT, you nazi-whore!"
window hide
with hpunch
ig "AAAH! He's so BRUTAL!"
scene ingridanalcum02 with dissolve
mc "I thought you girls like BRUTAL stuff! You want some more, here's some MOAAAAR!"
window hide
with fastflash
mc "DEEPER INSIDE YOUR BACKDOOR, RHAA!"
scene ingridanalcum03 with dissolve
mc "I'll give you a CUM ENEMA, AAAH!"
window hide
with vpunch
play sound "sounds/womancum02.mp3"
ig "Zo much nutzauce! I'm cumming too!"
scene ingridanalcum04 with dissolve
stop channel1
play sound "sounds/splat.ogg"
mc "Now for the GRAND CUM FINALE!!!!"
window hide
with fastflash
fr "You're LEAKING spunk from dein ass, Ingrid! He IS from the Superior Race!"
scene ingridanalcum05 with dissolve
stop channel2
play sound "sounds/boymoan03.mp3"
mc "There. I totally covered you in my HOT SEED."
play sound "sounds/moan02.mp3"
ig "Uuuhhh, I feel zo dirty... And zo GUT!"
scene ingridanalcum06 with dissolve
fr "I hope you kept some cream for MICH!"
mc "Ooh yeah, a SEX SUPERHERO like me ain't done with just one little load. Come over here and I'll show you..."
scene interrogation40 with dissolve
play sound "sounds/lick01.ogg"
ig "Zo tasty..."
mc "Come closer, Frieda. I want to..."
scene interrogation41 with dissolve
play sound "sounds/kiss.mp3"
mc "...kiss YOU!"
fr "Mmmh... Zuch a good kisser...."
mc "Now get down on your knees...."
scene interrogation42 with dissolve
if age >= 20:
    mc "...And worship my MASSIVE HORSECOCK!"
if age >= 18 and age <= 19:
    mc "...And worship my MASSIVE TEEN HORSECOCK!"
play sound "sounds/kiss.mp3"
fr "I vill, I vill! * kisses *"
mc "And you, Ingrid, clean the tip from my overflowing cum-cannon!"
ig "Ja wohl!"
scene interrogation43 with dissolve
play sound "sounds/slurp.mp3"
mc "That's good, my little nazi cock-sluts. Yeah, sehr good."
scene interrogation44 with dissolve
play sound "sounds/lick02.mp3"
mc "Keep going, suck that dong... Make me COME AGAIN!"

stop channel1
play channel1 "v032/blow03.mp3"
$ ssblowjobslowx = False

label SSBlowjobSlowx:
$ ssblowjobfastx = False
window hide
show ssblowjobslowvideo behind ssblowjobfastvideo
show ssblowjobslowvideo behind ssblowjobcloserslowvideo
pause 1.0
hide ssblowjobfastvideo
hide ssblowjobcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobslowx == False:
    $ ssblowjobslowx = True
    mc "My shaft just LOVES the attention you're giving it, my little nazi cock-whores..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ssblowjobfuckslowx()
screen ssblowjobfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobCloserSlowx")

label SSBlowjobFastx:
$ ssblowjobslowx = False
window hide
show ssblowjobfastvideo behind ssblowjobslowvideo
show ssblowjobfastvideo behind ssblowjobcloserfastvideo
pause 1.0
hide ssblowjobcloserfastvideo
hide ssblowjobslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobfastx == False:
    $ ssblowjobfastx = True
    play sound "sounds/boymoan02.mp3"
    mc "Oh yeah, it's even better like that... Mmmh..."    
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ssblowjobfuckfastx()
screen ssblowjobfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobCloserFastx")

label SSBlowjobCloserSlowx:
$ ssblowjobfastx = False
window hide
show ssblowjobcloserslowvideo behind ssblowjobslowvideo
show ssblowjobcloserslowvideo behind ssblowjobcloserfastvideo
pause 1.0
hide ssblowjobcloserfastvideo
hide ssblowjobslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobslowx == False:
    $ ssblowjobslowx = True
    mc "My shaft just LOVES the attention you're giving it, my little nazi cock-whores..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ssblowjobcloserfuckslowx()
screen ssblowjobcloserfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobCloserFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobSlowx")

label SSBlowjobCloserFastx:
$ ssblowjobslowx = False
window hide
show ssblowjobcloserfastvideo behind ssblowjobfastvideo
show ssblowjobcloserfastvideo behind ssblowjobcloserslowvideo
pause 1.0
hide ssblowjobfastvideo
hide ssblowjobcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
if ssblowjobfastx == False:
    $ ssblowjobfastx = True
    play sound "sounds/boymoan02.mp3"
    mc "Oh yeah, it's even better like that... Mmmh..."    
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ssblowjobcloserfuckfastx()
screen ssblowjobcloserfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobCloserSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobFastx")

label SSBlowjobEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
mc "You want me to come? You want another GIANT LOAD of BOYCREAM?"
fr "Ja, JA! Bitte, give us your young cum!"
scene ssblowjobcum01 with dissolve
stop sound
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "HERE YOU GO, MY LITTLE NAZI CUM-WHORES, AAAH!"
window hide
with fastflash
play sound "sounds/splooge01.mp3"
ig "Mmmggg...."
scene ssblowjobcum02 with dissolve
play sound "sounds/slurp.mp3"
mc "MAJOR CUM RELEASE AHEAD!"
window hide
with hpunch
mc "Fuck yeah! Suck that hot spunk!"
scene ssblowjobcum03 with dissolve
play sound "sounds/lick01.ogg"
fr "You're... * slurp * cumming zzzooo much!"
window hide
with fastflash
mc "Damn right I am, RHAAA!"
scene ssblowjobcum04 with dissolve
play sound "sounds/splat.ogg"
ig "* gargle * He is filling... Mein mouth!"
window hide
with fastflash
if age >= 20:
    mc "...with a MASSIVE dose of my unending supply of jizz!"
if age >= 18 and age <= 19:
    mc "...with a MASSIVE dose of my unending supply of teenage jizz!"
scene ssblowjobcum05 with dissolve
stop channel1
play sound "v031/cough.mp3"
ig "I can't... swallow all zis cream... schnell enough...."
play sound "sounds/lick03.mp3"
fr "Let me lick your mighty cum-cannon clean..."
mc "Yeah, go ahead. Then clean your little friend's face and chest, I made a big cum mess over there..."
scene ssblowjobcum06 with dissolve
play sound "sounds/lick02.mp3"
ig "Oooh, Frieda..."
mc "Yeah, that's hot, keep going..."
scene ssblowjobcum07 with dissolve
play sound "sounds/lick01.ogg"
fr "I just love the taste of that young spunk.... It smells zo VIRILE!"
ig "I know... But... We must not tell him anything..."
scene ssblowjobcum08 with dissolve
mc "I see, you girls need some more CUM PERSUASION! Well, I'm STILL HARD so you'll get what you want!"
ig "Was? How can he still have a hardon after theze zwei MASSIVE RELEASES???"
scene ssblowjobcum09 with dissolve
play sound "sounds/gasp.mp3"
mc "And it's YOUR turn to feel the POWER of my mighty ROD OF PLEASURE, Frieda!"
ig "I...can't fight him anymore. Zorry, Frieda..."
scene ssblowjobcum10 with dissolve
mc "I'm gonna fucking tear your womb apart if you don't talk soon..."
fr "I... Go on, FUCK MICH! I DON'T CARE!"
scene ssblowjobcum11 with dissolve
play sound "sounds/womancum02.mp3"
mc "Cumming already? But that's just the tip..."
ig "There's way over ein foot of MEGACOCK still outzide Frieda!"
mc "That's right, so get ready for a HEAVY POUNDING!"    
$ friedafuckslowx = False

label FriedaFuckSlowx:
$ friedafuckharderx = False
$ friedafucfastx = False
if friedafuckslowx == False:
    $ friedafuckslowx = True
    ig "Just take it like I did! For the glory of our Führer!"
window hide
show friedafuckslowvideo behind friedafuckfastvideo
show friedafuckslowvideo behind friedafuckpovslowvideo
show friedafuckslowvideo behind friedafuckharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide friedafuckfastvideo
hide friedafuckpovslowvideo
hide friedafuckharderslowvideo
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
call screen friedafuckslowx()
screen friedafuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVSlowx")

label FriedaFuckFastx:
$ friedafuckharderx = False
$ friedafuckslowx = False
if friedafucfastx == False:
    $ friedafucfastx = True
    fr "Is that all you have? You'll never get what you what with suck WEAK pounding!"
    mc "Oh, you're taunting me now? I'm gonna fuck you FASTER then!"
window hide
show friedafuckfastvideo behind friedafuckslowvideo
show friedafuckfastvideo behind friedafuckpovfastvideo
show friedafuckfastvideo behind friedafuckharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedafuckslowvideo
hide friedafuckpovfastvideo
hide friedafuckharderfastvideo
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
call screen friedafuckfastx()
screen friedafuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVFastx")

label FriedaFuckPOVSlowx:
$ friedafuckharderx = False
$ friedafucfastx = False
if friedafuckslowx == False:
    $ friedafuckslowx = True
    ig "Just take it like I did! For the glory of our Führer!"
window hide
show friedafuckpovslowvideo behind friedafuckslowvideo
show friedafuckpovslowvideo behind friedafuckpovfastvideo
show friedafuckpovslowvideo behind friedafuckharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide friedafuckslowvideo
hide friedafuckpovfastvideo
hide friedafuckharderpovslowvideo
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
call screen friedafuckpovslowx()
screen friedafuckpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckSlowx")

label FriedaFuckPOVFastx:
$ friedafuckharderx = False
$ friedafuckharderx = False
$ friedafuckslowx = False
if friedafucfastx == False:
    $ friedafucfastx = True
    fr "Is that all you have? You'll never get what you what with suck WEAK pounding!"
    mc "Oh, you're taunting me now? I'm gonna fuck you FASTER then!"
window hide
show friedafuckpovfastvideo behind friedafuckpovslowvideo
show friedafuckpovfastvideo behind friedafuckfastvideo
show friedafuckpovfastvideo behind friedafuckharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedafuckpovslowvideo
hide friedafuckfastvideo
hide friedafuckharderpovfastvideo
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
call screen friedafuckpovfastx()
screen friedafuckpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckFastx")

label FriedaFuckHarderSlowx:
if friedafuckharderx == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharderx = True        
window hide
show friedafuckharderslowvideo behind friedafuckharderfastvideo
show friedafuckharderslowvideo behind friedafuckharderpovslowvideo
show friedafuckharderslowvideo behind friedafuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide friedafuckharderfastvideo
hide friedafuckharderpovslowvideo
hide friedafuckslowvideo
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
call screen friedafuckharderslowx()
screen friedafuckharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEndx")

label FriedaFuckHarderFastx:
if friedafuckharderx == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharderx = True        
window hide
show friedafuckharderfastvideo behind friedafuckharderslowvideo
show friedafuckharderfastvideo behind friedafuckharderpovfastvideo
show friedafuckharderfastvideo behind friedafuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/pounding.ogg"
hide friedafuckharderslowvideo
hide friedafuckharderpovfastvideo
hide friedafuckfastvideo
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
call screen friedafuckharderfastx()
screen friedafuckharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEndx")

label FriedaFuckHarderPOVSlowx:
if friedafuckharderx == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharderx = True        
window hide
show friedafuckharderpovslowvideo behind friedafuckharderslowvideo
show friedafuckharderpovslowvideo behind friedafuckharderpovfastvideo
show friedafuckharderpovslowvideo behind friedafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide friedafuckharderslowvideo
hide friedafuckharderpovfastvideo
hide friedafuckpovslowvideo
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
call screen friedafuckharderpovslowx()
screen friedafuckharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEndx")

label FriedaFuckHarderPOVFastx:
if friedafuckharderx == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharderx = True        
window hide
show friedafuckharderpovfastvideo behind friedafuckharderpovslowvideo
show friedafuckharderpovfastvideo behind friedafuckharderfastvideo
show friedafuckharderpovfastvideo behind friedafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/pounding.ogg"
hide friedafuckharderpovslowvideo
hide friedafuckharderfastvideo
hide friedafuckpovfastvideo
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
call screen friedafuckharderpovfastx()
screen friedafuckharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEndx")

label FriedaFuckEndx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon    
mc "Are you ready to spill the beans? Cos I'm ready to spill MY SEED!"
ig "Hold tight, Frieda!"
scene friedafuckcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/boymoan05.mp3"
fr "Nein! He's cumming..."    
window hide
with fastflash
play sound "sounds/moan05.mp3"
mc "That's right, and that's just the START!"
scene friedafuckcum02 with dissolve
mc "RHAAA! I won't stop until you're BLOATED with my spunk!"
window hide
with hpunch
mc "Talk, or I'll WRECK your womb with a mighty CUMPLOSION!"
scene friedafuckcum03 with dissolve
play sound "sounds/moan04.ogg"
fr "AAAh! I vill talk, I vill talk! Colonel Stroheim vent back in time. To... Berlin, 1945. AAAH!"
window hide
with hpunch
ig "The day after our Führer had a tragic gun-related inzident. Leave her alone now!"
scene friedafuckcum04 with dissolve
play sound "sounds/boymoan03.mp3"
mc "Tell me MORE! Or the next shot will DESTROY your womb! I want to know EVERYTHING!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
fr "UUUH! He is gathering his burnt remains to clone him back to LIFE!"
mc "Then, there is no past time to waste! I must STOP him before it was too late! Tell me how to get there!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
ig "I can take you there, I know how to program ze portal command module! Let her go!"
scene friedafuckcum05 with dissolve
stop channel1
play sound "sounds/moan02.mp3"
play sound "sounds/splooge01.mp3"
mc "Alright, for THIS time, I will spare your womb... And I'll fetch Wonder Woman while you girls clean yourselves up. Of all the Super-heroes, she's the one who deserves to put an END to this neo-nazi madness!"
play sound "sounds/moan02.mp3"
fr "Vat have ve done? Ve have betrayed Colonel Stroheim!"
ig "And our future cloned Führer..."
stop channel1
stop channel3
stop music
jump WonderGallery

label WonderGallery08:
stop sound
stop channel3
stop music
play music "sounds/sexy03.mp3"
scene wonderroomnight02
show wonderworn01 at centerleft
with fade
mc "Oh, where's my dau... I mean our daughter, Princess Diana?" 
hide wonderworn01
show wonderworn02 at centerleft
with fastdissolve
ww "She's being taken care of by Audit Girl. She has sucked so much milk out of me that my tits have just grown painfully LARGE..."
mc "Ah yes, I thought there was something different about you. Bigger boobs, what a tragedy."
hide wonderworn02
show wonderworn03:
    xpos 0.1 zoom 0.5
with fastdissolve
ww "You think they're better like this? But they're too HEAVY! I can't fight properly with these huge udders... And I feel so tired..."
mc "Let me think... And let me do something else too, cos I can multi-task, being a Super-Hero and all that..."
window hide
show wonderworn03:
    subpixel True
    xpos 0.1 ypos 0.0
    linear 4.0 zoom 1.0 xpos -0.3 ypos -0.8
pause
mc "Mmh, yeah, now I'm thinking..."
window hide
show wonderworn04 as wonderworn03:
    xpos -0.3 ypos -0.8 zoom 1.0
with dissolve
pause
mc "...more clearly! And I have an idea."
scene wonderroomnight02 blurred:
    zoom 1.2
show wonderworn05 at centerleft
with dissolve
mc "I think we need to get the milk OUT!"
hide wonderworn05
show wonderworn06 at centerleft
with fastdissolve
ww "But that's what Alpha-Girl was doing!"
mc "Yeah, but I'll do it differently, trust me on this, I'm the boob expert."
scene wonderroomnight03 blurred
show wonderworn07 at centerleft
with fastdissolve
ww "What are you doing? I... I feel weak and helpless."
mc "Just holding you so you don't move too much while I do..."
hide wonderworn07
show wonderworn08 at centerleft
with fastdissolve
mc "...THAT!"
play sound "sounds/moan01.mp3"
ww "Uuuhhh..."
scene wonderroomnight03 blurred:
    zoom 1.2
show wonderworn09 
with fastdissolve
play sound "sounds/moan06.ogg"
mc "It's working, let's get more titty juice flowing..."
hide wonderworn09
show wonderworn10
with fastdissolve
play sound "sounds/moan05.mp3"
ww "My boobs are growing! You're doing it all WRONG!"
hide wonderworn10
show wonderworn11
with fastdissolve
mc "That depends on one's point of view I'd say..."
ww "They're just MASSIVE now! I NEEDED them to get smaller, you idiot!"
hide wonderworn11
show wonderworn12
with fastdissolve
mc "That's it, there's only one way to do this then, a TITTY-FUCK!"
ww "Wh... What? But... That doesn't make any sense!"
mc "It makes perfect sense to me, and that's all that matters."
scene wonderworn13 with dissolve
mc "Let me lay you down on the bed. Just relax, my Super-Cock will do the rest!"
ww "I... Are you sure this will work?"
scene wonderworn14:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
mc "Yes, I mean, the dev can't keep your tits that large for much longer, it looks like this is a BE scene. And BE scenes end back where they started usually."
ww "What are you talking about?"
scene wonderworn15 with dissolve
mc "You'll see, the Super-Studliness of my love sword will vanquish the pain in your boobs. Therefore, they should go back to normal."
ww "Fine, let's try then. It's my last hope anyway..."
scene wonderworn16 with dissolve
mc "First, let me introduce my big friend here..."
ww "I remember him. He's hard-headed and ends up spewing non-stop nonsense."
scene wonderworn17 with dissolve
play sound "sounds/thud.mp3"
mc "You feel that? That's your way out of this predicament..."
play sound "sounds/moan01.mp3"
ww "Uuuh..."
window hide
show wondertitslap
pause
scene wonderworn18 with dissolve
mc "Err. Just let me place my dong right between..."
mc "...those soft tittes, AAAH!"

$ wonderworntalkslowx = False

play channel1 "sounds/wank.mp3"
label WonderWornSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornslowvideo behind wonderwornfastvideo
show wonderwornslowvideo behind wonderwornpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderwornfastvideo
hide wonderwornpovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderworntalkfastx = False
if wonderworntalkslowx == False:
    ww "This doesn't seem to work, I still feel PAIN in my boobs!"
    mc "Don't worry, it will come, let me enjoy this titfuck a while longer first..."
    $ wonderworntalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderwornslowx()
screen wonderwornslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornPOVSlowx")

label WonderWornFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornfastvideo behind wonderwornslowvideo
show wonderwornfastvideo behind wonderwornpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderwornslowvideo
hide wonderwornpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderworntalkslowx = False
if wonderworntalkfastx == False:
    ww "Come on, please, help me get my tits back to normal, [name]!"
    mc "Yeah, okay... * puff * Just a bit more... titfucking..."
    $ wonderworntalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderwornfastx()
screen wonderwornfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderWornEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornPOVFastx")

label WonderWornPOVSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornpovslowvideo behind wonderwornslowvideo
show wonderwornpovslowvideo behind wonderwornpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderwornslowvideo
hide wonderwornpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderworntalkfastx = False
if wonderworntalkslowx == False:
    ww "This doesn't seem to work, I still feel PAIN in my boobs!"
    mc "Don't worry, it will come, let me enjoy this titfuck a while longer first..."
    $ wonderworntalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderwornpovslowx()
screen wonderwornpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornSlowx")

label WonderWornPOVFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornpovfastvideo behind wonderwornfastvideo
show wonderwornpovfastvideo behind wonderwornpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderwornpovslowvideo
hide wonderwornfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderworntalkslowx = False
if wonderworntalkfastx == False:
    ww "Come on, please, help me get my tits back to normal, [name]!"
    mc "Yeah, okay... * puff * Just a bit more... titfucking..."
    $ wonderworntalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderwornpovfastx()
screen wonderwornpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderWornEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornFastx")

label WonderWornEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
ww "They're still MASSIVE!"
mc "Not for long, I'm about to..."
scene wonderbedtitcum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc ".... BLOW MY NUT!"
window hide
with hpunch
mc "AAAH!"
scene wonderbedtitcum02 with dissolve
ww "What are you doing? You were supposed to come on my TITS!"
window hide
with fastflash
mc "AAAAH! Sorry about that, I'll try and..."
scene wonderbedtitcum03 with dissolve
mc "...aim better this time, RHAAA!"
window hide
with vpunch
ww "I've got your red-hot batter all over my face!"
scene wonderbedtitcum04 with dissolve
mc "Don't you worry, I still have enough nutsauce to shower your giant boobs! UUUUH!"
window hide
with fastflash
ww "Keep pumping, if what you say is true, they need to be COVERED in it!"
scene wonderbedtitcum05 with dissolve
stop channel2
play sound "sounds/femalegrunt01.mp3"
ww "This had better work! My breasts are aching so much!"
scene wonderbedtitcum06 with dissolve
ww "AAAAH! Finally, they seem to... get smaller..."
mc "I'd say what a pity, but I kind of knew it was bound to happen."
scene wonderbedtitcum07 with dissolve
ww "Finally!"
mc "See? My Super-Load made your Super-Boobs, errr.... less super."
ww "The pain is withering away... Thank you, but now I need to take a shower. I'm caked in your filthy scum."
mc "Hey! My Super-Scum is anything BUT filthy!"
stop channel3
stop music
jump WonderGallery

label WonderGallery09:
stop sound
stop music
stop channel3
play music "sounds/sexy03.mp3"
scene wonderroomnight02
show wonderlingerie03 at centerleft
ww "I'm in my lingerie, ready to serve you as your harem slave..."
mc "Less time-wasting, that's good, you're learning fast."
hide wonderlingerie03
show wonderlingerie04 at centerleft
with fastdissolve
ww "I suppose I should let you sit on the bed for the formal harem proceedings to begin."
menu:
    "Handcuff her.":
        scene wonderroomnight02 blurred:
            zoom 1.2
        show wonderevil01
        with dissolve
        mc "Hang on a minute, I want to have a closer look at your hot bod first..."
        ww "Err.... Of course..."
        scene wonderroomnight03 blurred
        show wonderevil02
        with fastdissolve
        ww "Hey, why are you handcuffing me, Master?"  
        mc "Just a little sexual kink of mine. Now you'll OBEY me even more..."
        hide wonderevil02
        show wonderevil03
        with fastdissolve
        ww "I was already going to obey you anyway since I'm in your harem..."
        mc "That's true, but it's more fun like this."
        scene wwomanpre00b with dissolve
        mc "I'm ready! And seeing you in handcuffs is making me particularly HORNY!"
        scene wwomanpre01b with dissolve
        ww "I can see that... Your thing... It's MONSTROUS! But how can I service it if I'm in handcuffs?"
        scene wwomanpre02b with dissolve
        mc "I suppose you're right. Come over here, and let's do this the proper way now that I'm ROCK-HARD!"
        mc "Wonderful..."
    "Don't handcuff her.":
        mc "You suppose right."
        scene wwomanpre00 with dissolve
        mc "I'm ready! And I'm getting HARD!"
        scene wwomanpre01 with dissolve
        ww "I can see that... Master's cock is getting MASSIVE for WOnder Woman!"

label WonderRoomPreAssx:
scene wonderroompreass01 with dissolve
mc "Now I want you to show me those WONDERFUL titties of yours..."
scene wonderroompreass02 with dissolve
ww "They're not too small for you then?"
mc "I like 'em big, but I also like' em nice and firm like yours. Variety is the spice of life. And your ass is just sumptuous too, let's see it actually..."
ww "Yes, Harem master..."
scene wonderroompreass03 with dissolve
ww "Should I take my panties off too?"
mc "Not yet, not yet.... Come foward, Princess Diana, approach my Super-Cock!"
scene wonderroompreass04 with dissolve
mc "That's nice, what a sumptuous pair of buns you have there..."
ww "I... Thank you Master for the compliment. My duty is to serve you."
scene wonderroompreass05 with dissolve
mc "Then why don't rub it against my aching dong?"
if evilness >= 13:  
    ww "Your wish is my command, I am bound to obey you. Even if you are truly EVIL."
    mc "Well, let's not exaggerate, I haven't done anything too nasty. YET."
if evilness <= 12:  
    ww "Your wish is my command, I am bound to obey you.."
    mc "You know this for the best, since a SEX Super-Hero like me needs a heavy does of love-making to keep going..."
window hide
$ wonderasstalkslowx = False

play channel1 "sounds/wank.mp3"
label WonderAssSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderassslowvideo behind wonderassfastvideo
show wonderassslowvideo behind wonderasspovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderassfastvideo
hide wonderasspovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderasstalkfastx = False
if wonderasstalkslowx == False:
    ww "Is my ass making your cock SUPER-HARD, [name]?"
    mc "Oh damn, YES!"
    $ wonderasstalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderassslowx()
screen wonderassslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssPOVSlowx")

label WonderAssFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderassfastvideo behind wonderassslowvideo
show wonderassfastvideo behind wonderasspovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderassslowvideo
hide wonderasspovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderasstalkslowx = False
if wonderasstalkfastx == False:
    ww "And what if I slid down your shaft a bit faster... Would that make you EXPLODE?"
    mc "I... OH FUCK!"
    $ wonderasstalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderassfastx()
screen wonderassfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAssEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssPOVFastx")

label WonderAssPOVSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderasspovslowvideo behind wonderassslowvideo
show wonderasspovslowvideo behind wonderasspovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderassslowvideo
hide wonderasspovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderasstalkfastx = False
if wonderasstalkslowx == False:
    ww "Is my ass making your cock SUPER-HARD, [name]?"
    mc "Oh damn, YES!"
    $ wonderasstalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderasspovslowx()
screen wonderasspovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssSlowx")

label WonderAssPOVFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderasspovfastvideo behind wonderassfastvideo
show wonderasspovfastvideo behind wonderasspovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderasspovslowvideo
hide wonderassfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderasstalkslowx = False
if wonderasstalkfastx == False:
    ww "And what if I slid down your shaft a bit faster... Would that make you EXPLODE?"
    mc "I... OH FUCK!"
    $ wonderasstalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderasspovfastx()
screen wonderasspovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAssEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssFastx")

label WonderAssEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "You tried your best, but I resisted... I'm still SUPER-HARD and SUPER-HORNY!"
scene wonderroompretits01 with dissolve
ww "That's disappointing... Please tell me how to make it go down, I beg you!"
mc "Maybe you could let me play with your breasts for a while. I'm more of a breastman than an assman. Although it depends on the player obviously."
scene wonderroompretits02 with dissolve
ww "Fine, go ahead, I'm here to serve you after all..."
mc "That's a good girl."
scene wonderroompretits03 with dissolve
play sound "sounds/slurp.mp3"
mc "Now let's see if there's still some titty-milk left in there for ME!"
ww "Aaaah..."
scene wonderroompretits04 with dissolve
play sound "sounds/moan05.mp3"
mc "Ta-da!"
scene wonderroompretits05 with dissolve
ww "That was embarrassing, it should have been for Alpha-Girl."
mc "She's a pain in the boobs, remember? Pain in the boobs, Get it?"
scene wonderroompretits06 with dissolve
ww "As your harem slave, I am bound to find this funny. Even if I didn't get it. Let me get you off with my tits, and this time, Wonder Woman will succeed!"
mc "Alright! Let's see what you've got in store for me then!"
scene wonderroompretits07 with dissolve
play sound "sounds/lick01.ogg"
scene wonderroompretits08 with dissolve
play sound "sounds/lick02.mp3"
ww "Too much for you, [name]?"
play sound "sounds/boymoan.mp3"
mc "Uuuh.... It's just a small plume of premature cum, not to worry..."
scene wonderroompretits09 with dissolve
play sound "v032/gulp.mp3"
ww "Is that so? Then let's make this cock REALLY EXPLODE!"
window hide
play channel1 "sounds/wank.mp3"
$ wondertittalkslowx = False

label WonderTitSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitslowvideo behind wondertitfastvideo
show wondertitslowvideo behind wondertitpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wondertitfastvideo
hide wondertitpovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wondertittalkfastx = False
if wondertittalkslowx == False:
    ww "This time, don't even try and resist."
    $ wondertittalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wondertitslowx()
screen wondertitslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitPOVSlowx")

label WonderTitFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitfastvideo behind wondertitslowvideo
show wondertitfastvideo behind wondertitpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wondertitslowvideo
hide wondertitpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wondertittalkslowx = False
if wondertittalkfastx == False:
    if age >= 20:
        ww "If I do it faster like this, your great big whopper is going to explode, isn't it?"
    if age >= 18 and age <= 19:
        ww "If I do it faster like this, your great big teenage whopper is going to explode, isn't it?"
    mc "Oh... Fuck, yeah... Just a bit more..."
    $ wondertittalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wondertitfastx()
screen wondertitfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderTitEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitPOVFastx")

label WonderTitPOVSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitpovslowvideo behind wondertitslowvideo
show wondertitpovslowvideo behind wondertitpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wondertitslowvideo
hide wondertitpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wondertittalkfastx = False
if wondertittalkslowx == False:
    ww "This time, don't even try and resist."
    $ wondertittalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wondertitpovslowx()
screen wondertitpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitSlowx")

label WonderTitPOVFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitpovfastvideo behind wondertitfastvideo
show wondertitpovfastvideo behind wondertitpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wondertitpovslowvideo
hide wondertitfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wondertittalkslowx = False
if wondertittalkfastx == False:
    if age >= 20:
        ww "If I do it faster like this, your great big whopper is going to explode, isn't it?"
    if age >= 18 and age <= 19:
        ww "If I do it faster like this, your great big teenage whopper is going to explode, isn't it?"
    mc "Oh... Fuck, yeah... Just a bit more..."
    $ wondertittalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wondertitpovfastx()
screen wondertitpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderTitEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitFastx")

label WonderTitEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
ww "Come on, come for me, come for WONDER WOMAN!"
scene wwomantitcum01 with dissolve
stop channel2
play sound "sounds/boymoan03.mp3"
mc "Alrigh,t here it comes, AAAH!"
window hide
with fastflash
play channel2 "v031/boyorgasm02.mp3"
ww "Yes, YES!"
scene wwomantitcum02 with dissolve
play sound "sounds/wow.mp3"
ww "I did it, I made you come!"
window hide
with hpunch
mc "And I'm only getting started, AAAH!"
scene wwomantitcum03 with dissolve
ww "By Zeus, let your baby-batter rain down upon us!"
window hide
with fastflash
mc "RHOOOOO!"
scene wwomantitcum04 with dissolve
stop channel1
stop channel2
play sound "sounds/panting.mp3"
ww "Once again, Wonder Woman defeats her beastly opponent."
play sound "sounds/slurp.mp3"
mc "Gggg...."
scene wwomantitcum05:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
play sound "sounds/lick02.mp3"
ww "Mmh, it's wonderfully tasty..."
mc "I agree, I tasted it myself when, err... the Black Widow forced me to."
scene wwomantitcum06 with dissolve
ww "But that wasn't enough for you, was it?"
mc "What? I mean, yeah, one is NEVER enough!"
scene wwomantitcum07 with dissolve
play sound "sounds/lick01.ogg"
ww "So I NEED to make you explode AGAIN, right?"
scene wwomantitcum08 with dissolve
play sound "sounds/lick03.mp3"
mc "Indeed, you have your need, I have my needs too!"
scene wwomantitcum09 with dissolve
if age >= 20:
    ww "You've made me so horny coming like a true STALLION that I'm ready to take your MASSIVE cock..."
if age >= 18 and age <= 19:
    ww "You've made me so horny coming like a true STALLION that I'm ready to take your MASSIVE teen cock..."
mc "Now we're talking!"
scene wwomantitcum10 with dissolve
ww "But I can't get pregnant again. Not until I find my home portal..."
mc "So I guess ANAL it is then!"
scene wwomantitcum11 with dissolve
ww "You guessed right..."
mc "Bingo!"
scene wwomantitcum12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
ww "But be careful with that thing. I still need to be able to FIGHT."
if age >= 20:
    mc "I'll be as gentle as a man equipped with an eighteen-inch cum-cannon can be."
if age >= 18 and age <= 19:
    mc "I'll be as gentle as a teenage boy equipped with an eighteen-inch cum-cannon can be."
scene wwomantitcum13 with dissolve
ww "You promise you'll be gentle?"
mc "Of course, Pricness Diana."
scene wwomantitcum14 with dissolve
play sound "sounds/gasp.mp3"
mc "What harm could THIS weapon possibly do?"
play sound "sounds/moan01.mp3"
ww "It's so BIG..."
scene wwomantitcum15 with dissolve
mc "Get on top of me and let me gently pleasure... your backdoor."
scene wwomantitcum16 with dissolve
play sound "sounds/womangroan.mp3"
ww "My ass! It's distending so much!"
scene wwomantitcum17 with dissolve
mc "NOT ENOUGH FOR MY DONG!"
play channel1 "sounds/wank.mp3"
$ wonderbedanaltalkslowx = False

label WonderBedAnalSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalslowvideo behind wonderbedanalfastvideo
show wonderbedanalslowvideo behind wonderbedanalfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderbedanalfastvideo
hide wonderbedanalfrontslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderbedanaltalkfastx = False
if wonderbedanaltalkslowx == False:
    ww "Oh God, it's so BIG in my ass!"
    $ wonderbedanaltalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen wonderbedanalslowx()
screen wonderbedanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalFrontSlowx")

label WonderBedAnalFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfastvideo behind wonderbedanalslowvideo
show wonderbedanalfastvideo behind wonderbedanalfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderbedanalslowvideo
hide wonderbedanalfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderbedanaltalkslowx = False
if wonderbedanaltalkfastx == False:
    mc "Yeah, that's it, ride my fat dong faster, you know you want to!"
    ww "I want to make you come!"
    $ wonderbedanaltalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen wonderbedanalfastx()
screen wonderbedanalfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBedAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFrontFastx")

label WonderBedAnalFrontSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfrontslowvideo behind wonderbedanalslowvideo
show wonderbedanalfrontslowvideo behind wonderbedanalfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderbedanalslowvideo
hide wonderbedanalfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderbedanaltalkfastx = False
if wonderbedanaltalkslowx == False:
    ww "Oh God, it's so BIG in my ass!"
    $ wonderbedanaltalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderbedanalfrontslowx()
screen wonderbedanalfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalSlowx")

label WonderBedAnalFrontFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfrontfastvideo behind wonderbedanalfastvideo
show wonderbedanalfrontfastvideo behind wonderbedanalfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderbedanalfrontslowvideo
hide wonderbedanalfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderbedanaltalkslowx = False
if wonderbedanaltalkfastx == False:
    mc "Yeah, that's it, ride my fat dong faster, you know you want to!"
    ww "I want to make you come!"
    $ wonderbedanaltalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderbedanalfrontfastx()
screen wonderbedanalfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBedAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFastx")

label WonderBedAnalEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
ww "Are you ready to explode your cream inside Wonder Woman's ass?"
mc "Is that what you want? Go on, say it, my harem slave!"
scene wwomananalcum01 with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge01.mp3"
mc "AAAH! FU-UUUUCK!!!"
window hide
with fastflash
ww "I can FEEL your shots! They're so PLENTIFUL!"
scene wwomananalcum02 with dissolve
mc "Those were just an appetizer, THESE are the REALLY MONSTER ONES! UUUH!"
window hide
with hpunch
ww "SSSSOOO MUCH WARM BABY-BATTER!!!"
scene wwomananalcum03 with dissolve
mc "I've got more in store for you, Wonder Woman! RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
ww "AAAAAH, By Zeus, you're coming so DEEP inside me!"
scene wwomananalcum04 with dissolve
ww "I'm just ass-blowing your cum now, there's just too much of it!"
window hide
with vpunch
mc "I filled you up, now it's time to COVER you with my Alpha-Spunk then!"
scene wwomananalcum05 with dissolve
stop channel1
if age >= 20:
    ww "You're STILL cumming? You have such a HUGE reservoir of potent seed!"
if age >= 18 and age <= 19:
    ww "You're STILL cumming? You have such a HUGE reservoir of potent teenage seed!"
window hide
with fastflash
mc "Damn right, AAAH!"
scene wwomananalcum06 with dissolve
stop channel2
play sound "sounds/panting.mp3"
ww "You came so much..."
mc "Phew, thanks to your HOT BOD, Princess Diana!"
scene wwomananalcum07 with dissolve
play sound "sounds/kiss.mp3"
ww "That's such a sweet thing to say. Kiss me, my beloved BREEDING STUD!"
stop channel3
stop music
jump WonderGallery