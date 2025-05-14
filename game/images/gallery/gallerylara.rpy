label LaraGallery:
stop channel3
play channel3 "sounds/croftintro.mp3"
scene larabackground
show laramaingallery at gallerypos01 with moveinleft
call screen gallerylara()
screen gallerylara():
    text "{font=Gui/Heroes Legend.ttf}Naughty Lara Crotch{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerylara"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerylara"), Jump ("LaraGalleryAnim")]
    
    if renpy.seen_image("laratemple22"):
        imagebutton:
            focus_mask True
            idle "gallery/laragallery01.png" xpos 400 ypos 100
            hover "gallery/laragallery01.png"
            action Jump ("LaraGallery01")
    text "{font=Gui/Heroes Legend.ttf}Temple of Lust{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("laratemple22") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LaraGallery")

    if renpy.seen_image("larapoolcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/laragallery02.png" xpos 750 ypos 100
            hover "gallery/laragallery02.png"
            action Jump ("LaraGallery02")
    text "{font=Gui/Heroes Legend.ttf}Pool Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("larapoolcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LaraGallery")

    if renpy.seen_image("larawidowpool01"):
        imagebutton:
            focus_mask True
            idle "gallery/laragallery03.png" xpos 1100 ypos 100
            hover "gallery/laragallery03.png"
            action Jump ("LaraGallery03")
    text "{font=Gui/Heroes Legend.ttf}Lesbian w/Widow{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("larawidowpool01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LaraGallery")

label LaraGalleryAnim:
call screen screenanimlara()
screen screenanimlara():
    modal True
    add "gallery/larabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "laraanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "laraanimbik" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "laraanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimlara"), SetVariable ("animcount", 1), Jump ("LaraGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Lara Crotch{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 28{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34EE-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Teasing{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Dangerous Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/laraanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimlara")]
    add "gallery/laraanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimlara")]
    add "gallery/laraanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimlara")]
    
label LaraGallery01:
stop channel3
play channel2 "sounds/waterrun.mp3"
stop music
play music "sounds/croft02.mp3"
scene laratemple20 with dissolve   
voice "lara/temple18"
lc "Finally, we reach the heart of the Temple. This is where the biggest dangers lie. Usually."
mc "Looks pretty peaceful to me."
voice "lara/temple19"
lc "Now, to find out how to obtain that Cockring of Lust...."
mc "What does your notebook say?"
scene laratemple21 with dissolve   
voice "lara/temple20"
lc "That we must enter the pool to retrieve the Sacred Bowl and be wary of snares."
mc "What snares?"
scene laratemple22 with dissolve   
voice "lara/temple21"
lc "There is no mention of that in the text. Well, I'm up to the challenge, I will change into my two-piece swimsuit. It doesn't look like you need to change into any swimming gear by the looks of it."
mc "I still need to take my shoes off. I'm gonna feel naked without them."
scene laratemple23 with dissolve
mc "Is the water temperature nice? Like, my huge nuts won't shrivel up?"
voice "lara/temple22"
lc "Just get in the water, will you? We must find these artefacts as fast as we can, before..."
scene laratemple26 with dissolve 
play sound "sounds/diving.mp3"
voice "lara/temple23"
lc "What is this dreadful creature?"
scene laratemple27 with dissolve   
mc "Looks like a giant octopus with cock-tentacles to me."
voice "lara/temple24"
lc "AAAH, it is trying to find its way into MY inner sanctum! I need... to reach... for my blade!"
scene laratemple28 with dissolve   
play sound "sounds/lick01.ogg"
mc "I think it found it..."
voice "lara/temple25"
lc "Damn you, vile creature!"
scene laratemple29 with dissolve   
play sound "sounds/moan06.ogg"
voice "lara/temple26"
lc "Get in there and stop that sperm-tacle from going any deeper, [name]!"
scene laratemple30 with dissolve   
mc "Alright, muscle-hero is GO!"
if mccombat >= 1:
    call screen usepower("usecombat", "LaraTempleNoCombatx", "LaraTempleCombatx") with dissolve

label LaraTempleNoCombatx:
scene laratemple31b with dissolve
play sound "sounds/punch.mp3"
mc "Uh..."
voice "lara/temple27"
lc "That was kinda useless, now I have to deal with this monster on MY OWN! First, I need to cut off the constraining tentacle..."
play sound "sounds/knifecut.mp3"
voice "lara/temple28"
lc "There!"
scene laratemple32b with dissolve
play sound "sounds/femalegrunt01.mp3"
voice "lara/temple29"
lc "And now for the sperm-tacle! HIYAAH!"
scene laratemple33
show laratemple33b
with dissolve
play sound "sounds/knifecut.mp3"
voice "lara/temple30"
lc "My trusted blade will bleed this thing to death!"
jump LaraTempleEndCombatx

label LaraTempleCombatx:
scene laratemple31 with dissolve 
play sound "sounds/knifecut.mp3"
voice "lara/temple31"
lc "Hold it still while I cut off the constraining tentacle! There, got you!"
play sound "sounds/mangrunt01.mp3"
mc "Stop moving, you damn sperm-tacle!"
scene laratemple32 with dissolve 
play sound "sounds/splooge01.mp3"
mc "Hey, this fucking thing is spewing all over me!"
play sound "sounds/femalegrunt01.mp3"
voice "lara/temple32"
lc "Hang tight, I'm free from the grip of its other tentacle now!"
scene laratemple33 with dissolve 
mc "YUCK! I've got slimy squid-sperm on my face!"
play sound "sounds/knifecut.mp3"
voice "lara/temple33"
lc "I'm going to cut this bloody sperm-tacle in half with my trusted blade!"

label LaraTempleEndCombatx:
scene laratemple34 with dissolve 
voice "lara/temple34"
lc "Finally, this horrible creature has perished... We can now dive into the pool and retrieve the Sacred Bowl."
mc "Err, maybe I'll let you do that. That way, I can keep an eye out for any FURTHER snares. And wipe my face clean of that filthy spunk."
scene laratemple35 with dissolve 
play sound "sounds/diving.mp3"
voice "lara/temple35"
lc "Fine, I'll get it. ON MY OWN."                               
scene laratemple36 with dissolve 
stop channel2
play channel2 "sounds/underwater.mp3"
mc "* Hopefully, she finds it, this place is super-creepy... I mean, sperm-tacles, really? Who came up with this shit? *"
scene laratemple37 with dissolve 
stop channel2
play channel2 "sounds/waterrun.mp3"
voice "lara/temple36"
lc "Here, I got it, innit?"
mc "Oh cool, let's get out of this dark pool pronto before more tentacles emerge."
scene laratemple38 with dissolve
voice "lara/temple37"
lc "First, I will place the Sacred Bowl in front of the statue of the God of Lust."
mc "Ok. When do I get that cock ring?"
scene laratemple39 with dissolve
voice "lara/temple38"
lc "According to the legend, once you've filled it up with your seed."
mc "WTF???"
voice "lara/temple39"
lc "What did you expect? You think the God of Lust just gives out cockrings willy-nilly?"
mc "Err, that's a pretty BIG bowl."
scene laratemple40 with dissolve
voice "lara/temple40"
lc "I'm sure a strapping young lad like you won't have any problems filling it up. I estimate a quart of sperm will suffice."
mc "I'm gonna need... some help. You know, like something stimulating. Or I'll never be able to come THAT MUCH."
voice "lara/temple41"
lc "And you expect me to provide that `\"stimulation\" I assume?"
mc "I don't see any other sexy girl around here..."

voice "lara/temple42"
lc "Fine, I'll will undress for you then..."
stop channel2
stop music
play channel2 "sounds/sexy07.mp3"
scene laratemplestrip01:
    subpixel True
    ypos 0.0
    linear 6.0 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
voice "lara/temple43"
lc "Are you getting hard, [name]?"
scene laratemplestrip02:
    subpixel True
    ypos -1.0
    linear 6.0 ypos 0.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "I'm certainly getting there..."
scene laratemple41 with dissolve
voice "lara/temple44"
lc "I can see that... You have a MASSIVE hardon..."
mc "All thanks to you, Lara..."
scene laratemple42 with dissolve
mc "And a MASSIVE desire to FUCK you..."
if age >= 20:
    voice "lara/temple45a"
    lc "Hey, hold your horses, young man... This is purely professional to get your monstercock to unleash a great big fat load."
if age >= 18 and age <= 19:
    voice "lara/temple45b"
    lc "Hey, hold your horses, young man... This is purely professional to get your teenage monstercock to unleash a great big fat load."
mc "Err... Can I at least use your body to achieve this..."
voice "lara/temple46"
lc "I suppose. I'll turn round and you can pretend to fuck me."
scene laratemple43 with dissolve
mc "Fuck yeah, just the rubbing from your thighs as my shaft pummels between your legs will be enough to make me cum."
voice "lara/temple47"
lc "Use my thighs as your personal wanksheath then, [name]!"
play music "sounds/wank.mp3"
stop channel1
window hide

label LaraTempleSlowFuckx:
window hide
show laratemplewankslowvideo behind laratemplewankfastvideo
show laratemplewankslowvideo behind laratemplesideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple48"
lc "Mmmh, just like that. And play with my big boobs..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen laratemplefuckslowx()
screen laratemplefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleFastFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSideSlowx")

label LaraTempleFastFuckx:
window hide
show laratemplewankfastvideo behind laratemplewankslowvideo
show laratemplewankfastvideo behind laratemplesidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide laratemplesidefastvideo
hide laratemplewankslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple49"
lc "Yes, go on, pound that great big whopper between my thighs..."
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen laratemplefuckfastx()
screen laratemplefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSideFastx")


label LaraTempleSideSlowx:
window hide
show laratemplesideslowvideo behind laratemplewankslowvideo
show laratemplesideslowvideo behind laratemplesidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide laratemplesidefastvideo
hide laratemplewankslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple50"
lc "I love how your fuckstick reaches so far in front of me..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratemplesidefuckslowx()
screen laratemplesidefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSideFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSlowFuckx")

label LaraTempleSideFastx:
window hide
show laratemplesidefastvideo behind laratemplewankfastvideo
show laratemplesidefastvideo behind laratemplesideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide laratemplewankslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
show laratemplesidefastvideo
with dissolve
voice "lara/temple51"
lc "I can feel your strong abs pounding against my ass, mmhh..."
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratemplesidefuckfastx()
screen laratemplesidefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSideSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleFastFuckx")

label LaraTempleFuckEndx:
hide sceneicon
hide faster
hide slower
hide sideicon
mc "I'm gonna cum, Lara!"
voice "lara/temple52"
lc "Not yet, I need to get the bowl!"
scene laratemplecum01 with dissolve
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide laratemplesidefastvideo
hide laratemplewankslowvideo
stop music
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
mc "Too late, RHAAA!"
window hide
with fastflash
voice "lara/temple53"
lc "Aim for the bowl!"
scene laratemplecum02a with dissolve
play sound "sounds/boymoan05.mp3"
mc "I can't aim, I'm CUUUU-UUU-MMMIIING!"
window hide
with fastflash
voice "lara/temple54"
lc "Then I'll take charge of your disgorging cum-cannon!"
show laratemplecum02b with fastdissolve
voice "lara/temple55"
lc "We're not even CLOSE to filling it up!"
window hide
with fastflash
play sound "sounds/boymoan03.mp3"
mc "That's the last of it, AAAH!"
stop channel1
scene laratemplecum03 with dissolve
play sound "sounds/panting.mp3"
voice "lara/temple56"
lc "That was a BAD idea, there's more cum OUTSIDE the bowl than INSIDE and it's only HALF-FULL!"
mc "Who says I can't keep on going?"
scene laratemplecum04 with dissolve
voice "lara/temple57"
lc "What? You're STILL hard?"
mc "Hey, I'm a Super-Hero, remember?"
scene laratemplecum05 with dissolve
voice "lara/temple58"
lc "You ARE indeed... Seeing your rock-hard leaking shaft makes me want to SLURP on your fat bullballs!"
mc "Be my guest, Lara... That'll help me churn up another HUGE load."
scene laratemplecum06 with dissolve
play sound "sounds/slurp.mp3"
mc "Yeah, try and get one massive testicle in your mouth, you can do it..."
lc "Mmmgggbbb..."
mc "That's enough, I'm fucking horny for your PUSSY now!"
scene laratemplecum07 with dissolve
play sound "sounds/moan02.mp3"
mc "Are you ready to get impaled on my Superhero cock, Lara?"
voice "lara/temple59"
lc "Y...Yes, I am. Fuck me, fuck me HARD like the Super-Stud that you are!"
window hide

label LaraTempleSlowUpx:
window hide
show laratemplefuckslowvideo behind laratemplefuckfastvideo
show laratemplefuckslowvideo behind laratempledownslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen laratempleupslowx()
screen laratempleupslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleFastUpx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleDownSlowx")

label LaraTempleFastUpx:
window hide
show laratemplefuckfastvideo behind laratemplefuckslowvideo
show laratemplefuckfastvideo behind laratempledownfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide laratemplefuckslowvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen laratempleupfastx()
screen laratempleupfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSlowUpx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleDownFastx")


label LaraTempleDownSlowx:
window hide
show laratempledownslowvideo behind laratemplefuckslowvideo
show laratempledownslowvideo behind laratempledownfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratempledownfuckslowx()
screen laratempledownfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleDownFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSlowUpx")

label LaraTempleDownFastx:
window hide
show laratempledownfastvideo behind laratemplefuckfastvideo
show laratempledownfastvideo behind laratempledownslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratempledownfuckfastx()
screen laratempledownfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleDownSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleFastUpx")

label LaraTempleUpEndx:
hide cum
hide faster
hide slower
hide assview
hide sceneicon
voice "lara/temple60"
lc "Please hurry up, my cunt is getting DESTROYED by the ungodly width of your love muscle!"
mc "I'm almost there, Lara. I'm about to..."
window hide
scene laratemplefuckcum01 with dissolve
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
stop channel1
play channel1 "sounds/splooge01.mp3"
play music "sounds/boyorgasm01.mp3"
mc "BLOW.... RHAAAA!"
window hide
with fastflash
voice "lara/temple61"
lc "Godammit boy, you're doing it again, you're NOT pumping your seed into the bowl!"
with hpunch
window hide
with fastflash
play sound "sounds/womancum02.mp3"
voice "lara/temple62"
lc "You're pumping DIRECTLY into my womb, aaah!"
scene laratemplefuckcum02 with dissolve
mc "AAAH! I'm gonna fill you up till it's cascading out of your fuckhole!"
with hpunch
window hide
with fastflash
voice "lara/temple63"
lc "I can feel every POWERFUL blast, keep PUMPING!"
window hide
with fastflash
voice "lara/temple64"
lc "Pull me up, I'm getting bloated with your cream!"
scene laratemplefuckcum03 with dissolve
stop music
stop channel1
play sound "sounds/panting.mp3"
mc "Fuck yeah, that was another SPUNKY load..."
voice "lara/temple65"
lc "Now put me down, I need to check whether the Sacred Bowl is finally full... And whether we need ANOTHER load from you or not..."
scene laratemplefuckcum04 with dissolve
stop channel2
play music "sounds/waterrun.mp3"
voice "lara/temple66"
lc "This time, you managed to fill up the Sacred Bowl to the brim... Thanks God, I don't think my poor pussy could have taken another pounding like that..."
mc "Too bad, I could go ON and ON if I wanted to... * wink *"
voice "lara/temple67"
lc "Keep your strength, you must remain hard for the next phase. The magical transfer of the Prince Albert Cockring of Lust to your giant phallus!"
scene laratemplefuckcum05 with dissolve
play sound "sounds/coldwind.mp3"
mc "That sound is ominous..."
voice "lara/temple68"
lc "Do not fear, we have followed what my notebook says, it should be fi..."
scene laratemplefuckcum06 with dissolve
with hpunch
play sound "sounds/magic.mp3"
mc "What the?..."
scene laratemplefuckcum07 with dissolve
voice "lara/temple69"
lc "The Cockring of Lust has been transferred to your phallus!"
$ inventorylustring = True
play sound "sounds/achievement.mp3"
show acquiredcockring at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Fuck yeah!"
scene laratemplefuckcum08 with dissolve
play sound "sounds/splooge02.mp3"
mc "AAAHHHH!!!!!"
with hpunch
window hide
with fastflash
voice "lara/temple70"
lc "What the? Why are you cumming like that?"
play sound "sounds/splooge01.mp3"
with hpunch
window hide
with fastflash
play sound "sounds/boymoan04.mp3"
mc "I can't help myself, it just came out like that, RHAAAA!"
scene laratemplefuckcum09 with dissolve
stop sound
voice "lara/temple71"
lc "Finally, your MEGA-ORGASM is over..."
mc "And my cock ring is disappearing... Why is this happening?"
scene laratemplefuckcum10 with dissolve
play sound "sounds/slurp.mp3"
voice "lara/temple72"
lc "Don't you worry, this was to be expected. It is an invisible ring. But it is there, and you should see it in your inventory..."
mc "Oh cool, we didn't do all this for nothing then."
voice "lara/temple73"
lc "Just make sure nobody ever steals it. Especially Super-Villains. Let's get dressed and go back to Cockham City now..."
stop music
stop channel1
stop channel2
jump LaraGallery

label LaraGallery02:
stop channel3
play music "sounds/croftintro.mp3"
scene larapool01 with fade
lc "You remember my private pool? We've been here before..."
mc "Damn, I sure remember Lara!"
scene larapool02 with dissolve
lc "Last one in is a chicken-shit superhero adventurer!"
play sound "sounds/diving.mp3"
mc "Hey!"
scene larapool03 with dissolve
lc "Come on, are you scared or something?"
mc "No I'm not... I just... don't like cold water. My cock doesn't at least."
scene larapool04 with dissolve
lc "The water is warmed to a perfect temperature all year round... Your cock shouldn't have anything to fear."
mc "* Damn, look at those tits... *"
scene larapool05 with dissolve
lc "I could check if you want..."
mc "Check what?"
scene larapool06 with dissolve
play sound "sounds/underwater.mp3"
mc "* Ah, now I get it... Maybe I should get HARD for her then... *"
scene larapool07 with dissolve
mc "* Yeah... That's it, get hard, cock!"
scene larapool08 with dissolve
stop sound
mc "She's fondling my shaft... This is about to get STEAMY!"
scene larapool09 with dissolve
play sound "sounds/underwater.mp3"
mc "* Oooh, fuck, she's pulling my speedoes down... Just in time as I'm getting... *"
scene larapool10 with dissolve
mc "* ... ROCK-HARD! *"
scene larapool11 with dissolve
stop sound
mc "Fuck yeah, my cock is so fucking BIG now, need to hold it steady before I blow my load!"
scene larapool12 with dissolve
play sound "sounds/underwater.mp3"
mc "* Oh God, she's sucking my balls... underwater. *"
window hide
stop sound
play channel1 "sounds/lick02.mp3"
show larapoollickvideo with dissolve
pause 1.0
play channel2 "sounds/boymoan04.mp3"
mc "* And now she's licking all the way up my shaft.... *"
window hide
pause
stop channel1
stop channel2
scene larapool13 with dissolve
lc "Now I bet you want you to FUCK ME again with this enormous dong of yours, don't you? You're already drooling so much pre-cum..."
mc "I'm so hard, I simply NEED to, Lara!"
scene larapool14 with dissolve
if age >= 20:
    lc "Then let's switch places. Get in the water and prep your giant tool while I remove my bikini bottom..."
if age >= 18 and age <= 19:
    lc "Then let's switch places. Get in the water and prep your giant teenage tool while I remove my bikini bottom..."

scene larapool20 with dissolve
play sound "sounds/moan02.mp3"
lc "Pound me real good with it please, [name]!"
mc "My SUPER-STUD powers will be on full display, don't you worry about that!"
scene larapool21 with dissolve
lc "Then, I think I'm ready... Even though your cock is truly IMMENSE."
stop sound

$ larapoolfuckslowx = False
$ larapoolfuckfastx = False

label LaraPoolFuckSlowx:
$ larapoolfuckfastx = False
window hide
show larapoolslowvideo behind larapoolfastvideo
show larapoolslowvideo behind larapoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide larapoolfastvideo
hide larapoolpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckslowx == False:
    $ larapoolfuckslowx = True
    lc "Your [age]yo dick is so fucking big... I love it when you fuck me slowly like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen larapoolfuckslowx()
screen larapoolfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckPOVSlowx")

label LaraPoolFuckFastx:
$ larapoolfuckslowx = False
window hide
show larapoolfastvideo behind larapoolslowvideo
show larapoolfastvideo behind larapoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide larapoolpovfastvideo
hide larapoolslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckfastx == False:
    $ larapoolfuckfastx = True    
    if age >= 20:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant horsecock!"
    if age >= 18 and age <= 19:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant teen horsecock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen larapoolfuckfastx()
screen larapoolfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckPOVFastx")


label LaraPoolFuckPOVSlowx:
$ larapoolfuckfastx = False
window hide
show larapoolpovslowvideo behind larapoolslowvideo
show larapoolpovslowvideo behind larapoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide larapoolpovfastvideo
hide larapoolslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckslowx == False:
    $ larapoolfuckslowx = True
    lc "Your [age]yo dick is so fucking big... I love it when you fuck me slowly like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen larapoolpovfuckslowx()
screen larapoolpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckSlowx")

label LaraPoolFuckPOVFastx:
$ larapoolfuckslowx = False
window hide
show larapoolpovfastvideo behind larapoolfastvideo
show larapoolpovfastvideo behind larapoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide larapoolfastvideo
hide larapoolpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if larapoolfuckfastx == False:
    $ larapoolfuckfastx = True    
    if age >= 20:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant horsecock!"
    if age >= 18 and age <= 19:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant teen horsecock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen larapoolpovfuckfastx()
screen larapoolpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckFastx")

label LaraPoolFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
lc "You're gonna pump a fat load inside my pussy aren't you?"
mc "Y... Yes, I'm..."
scene larapoolcum01 with dissolve
stop channel1
play sound "sounds/boymoan05.mp3"
mc "... BLOWING, AAAH!"
window hide
with hpunch
play channel2 "sounds/moan04.ogg"
lc "I can feel it, I'm coming too!"
scene larapoolcum02 with dissolve
stop channel2
play channel2 "sounds/splooge02.mp3"
lc "You're filling me up with so much spunk!"
window hide
with fastflash
play sound "sounds/kiss.mp3"
lc "Mmmh, kiss me while you cum DEEP inside me, STUD!"
scene larapoolcum03 with dissolve
lc "Mmmhh, you're a good kisser."
window hide
with fastflash
play sound "sounds/moan05.mp3"
lc "And a good CUMMER!"
scene larapoolcum04 with dissolve
play sound "sounds/moan02.mp3"
lc "I want you to pull out your disgorging dong and COVER MY TITS in your thick scum. Can you do that for me, [name]?"
scene larapoolcum05 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "I'm... STILL BLOWING BIG TIME!"
window hide
with fastflash
lc "I can see THAT! It's FLYING everywhere!"
scene larapoolcum06 with dissolve
play sound "sounds/splooge03.mp3"
lc "For Queen's sake, try and aim your giant spurts better! You've pumping half of it all over my face!"
window hide
with fastflash
mc "AAAAH, sorry, can't control myself when I'm NU-UUU-TTTING!"
scene larapoolcum07 with dissolve
stop channel2
play sound "sounds/panting.mp3"
lc "Finally, your cum-cannon is done spewing its GIGANTIC load all over the place..."
scene larapoolcum08 with dissolve
play sound "sounds/lick02.mp3"
lc "Mmh, it's very tasty actually. I think I might... * slurp * stick around a bit longer..."
play sound "sounds/panting.mp3"
mc "Rhuuu...."
play sound "sounds/lick03.mp3"
lc "But you seem to be rather drained, so you'd better go back and get some rest, [name]...."
stop music
stop channel1
stop channel2
jump LaraGallery

label LaraGallery03:
stop channel3
play channel2 "sounds/waterrun.mp3"
scene larawidowpool01 with dissolve
lc "I'm so glad you came. I heard you were... rather busy lately."
bw "Yeah, I am. But I thought it would be a nice change from my NEW routine."
scene larawidowpool02 with dissolve
lc "So, what new routine is that? Would you like to talk about it?"
bw "I'm fighting Western DECADENCE. Greed is the root of all evil. Speaking of which, your GOLDEN swimsuit is... rather tasteless."
scene larawidowpool03 with dissolve
lc "Ah, err... I can take it off if you want. I wanted to get a new one. A more modest one anyway."
scene larawidowpool04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
bw "That's better... I see you are ready to abandon your depraved ways."
stop music
play music "sounds/sexy03.mp3"
scene larawidowpool05 with dissolve
bw "Now there's ONE thing that needs sharing more than money..."
lc "And what is that?"
scene larawidowpool06 with dissolve
bw "LOVE..."
lc "Oooh... I ssooo agree..."
scene larawidowpool07 with dissolve
play sound "sounds/slurp.mp3"
lc "Mmmh..."
scene larawidowpool08 with dissolve
play sound "sounds/lick02.mp3"
lc "Aaah... You know my weak spots, Natasha..."
scene larawidowpool09 with dissolve
play sound "sounds/kiss.mp3"
bw "And you know mine..."
scene larawidowpool10 with dissolve
mc "Mmmh, I wonder whether now is a good time? My Super-Libido tells me to wait a bit longer for this lesbian show to escalate..."
lc "Now it's my turn to return the favor. I'm gonna hold you up in the water so you can play with your pussy in zero gravity..."
scene larawidowpool11a with dissolve
bw "Oh yeah, I like that..."
play channel1 "sounds/wank.mp3"
window hide
show widowlarapoolwank with fastdissolve
pause
bw "Gonna..."
scene larawidowpool12 with dissolve
stop channel1
play sound "sounds/moan05.mp3"
bw "... CUM, AAAHH!"
scene larawidowpool13 with dissolve
play sound "sounds/kiss.mp3"
bw "That was wonderful... Now your pussy needs some tender loving too... From my fingers!"
scene larawidowprewank01 with dissolve
lc "Ooooh..."
play channel1 "sounds/wetmassage.mp3"
window hide

label LaraPoolWankSlowx: 
hide nexticon
hide faster
hide slower
show larawidowpoolwankslowvideo behind larawidowpoolwankfastvideo
pause 1.0
hide larawidowpoolwankfastvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen larawidowpoolwankslowx()
screen larawidowpoolwankslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolWankEndx")

label LaraPoolWankFastx:
show larawidowpoolwankfastvideo behind larawidowpoolwankslowvideo
hide nexticon
hide faster
hide slower
hide larawidowpoolwankslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen larawidowpoolwankfastx()
screen larawidowpoolwankfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolWankEndx")

label LaraPoolWankEndx:
hide nexticon
hide slower
hide faster
lc "Just like that, just like that...You're going to make me..."
scene larawidowpostwank01 with dissolve
stop channel1
play sound "sounds/moan06.ogg"
lc "...SQUIRT! AAAH!"
scene larawidowpool14 with dissolve
bw "Now I NEED to taste those yummy juices of yours..."
scene larawidowpool15 with dissolve
play channel1 "sounds/moan02.mp3"
lc "Oh God... Your tongue..."
play sound "sounds/lick02.mp3"
bw " * lick *"
scene larawidowpool16 with dissolve
lc "Yes, just keep going Natasha... "
mc "* Why is she holding her hand like that? *"
scene larawidowpool17 with dissolve
mc "* Oh, I got it. NOW is the time! Here's the gem, Lara! *"
scene larawidowpool18 with dissolve
play sound "sounds/magic.mp3"
lc "Patra-Khok-..."
scene larawidowpool19 with dissolve
lc "...Mindh-Khon-Troll!"
scene larawidowpool20 with dissolve
lc "Let go of your mind, Natasha! Remove the lock and escape from the grip of your enslaver! You are not working for the Soviets!"
scene larawidowpool21 with dissolve
play sound "sounds/magic.mp3"
lc "I FREE YOU, by the Power of the Queen Jewel!"
scene larawidowpool22 with dissolve
mc "Did it work?"
lc "Of course it did. I said the correct incantation which were left in a notebook by my late explorer father!"
mc "So she's no longer a radical leftist lunatic then? She's a normal decadent American capitalist right?"
lc "She needs to recover from the exhaustion. Let me take her back to the gallery and make sure she sleeps well."
stop music
stop channel1
stop channel2
jump LaraGallery
