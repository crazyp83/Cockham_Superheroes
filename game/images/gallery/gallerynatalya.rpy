label NatalyaGallery:
stop channel3
play channel3 "v042/russianballet.mp3"
scene natalyabackground
show natalyamaingallery at gallerypos01 with moveinleft
call screen gallerynatalya()
screen gallerynatalya():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Natalya{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerynatalya"), Jump ("MainGallery05")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerynatalya"), Jump ("NatalyaGalleryAnim")]
    
    if renpy.seen_image("embassy10"):
        imagebutton:
            focus_mask True
            idle "gallery/natalyagallery01.png" xpos 400 ypos 100
            hover "gallery/natalyagallery01.png"
            action Jump ("NatalyaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Robot Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("embassy10") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("NatalyaGallery")

    if renpy.seen_image("widownatalya03"):
        imagebutton:
            focus_mask True
            idle "gallery/natalyagallery02.png" xpos 750 ypos 100
            hover "gallery/natalyagallery02.png"
            action Jump ("NatalyaGallery02")
    text "{font=Gui/Heroes Legend.ttf}3some w/Widow{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("widownatalya03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("NatalyaGallery")

label NatalyaGalleryAnim:
stop channel3
play channel3 "sounds/sexy09.mp3"
call screen screenanimnatalya()
screen screenanimnatalya():
    modal True
    add "gallery/natalyabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "natalyaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "natalyaanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "natalyaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimnatalya"), SetVariable ("animcount", 1), Jump ("NatalyaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Agent Natalya{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 35{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34DD-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Slave Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Blowjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/natalyaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimnatalya")]
    add "gallery/natalyaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimnatalya")]
    add "gallery/natalyaanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimnatalya")]
            
label NatalyaGallery01:
stop channel3
stop music
stop channel2
scene embassy08 with dissolve
mc "This place is creepy and I just missed the Black Widow! They took the elevator, I'll check which floor they g..."
scene embassy09 with dissolve
play music "v042/russianballet.mp3"
mc "What the hell...?"
scene embassy10 with dissolve
mc "Where did these two... come from?"
scene embassy11 with dissolve
mc "Hello? Who are you? Just let me through and go and practice ballet somewhere else, ladies!"
scene embassy12 with dissolve
mc "I'm losing patience here, robot-woman! Just GET OUT OF MY WAY!"
scene embassy13 with dissolve
mc "Hey, stop this! These are NOT just dancing robots, they're KILLER-ROBOTS!"
scene embassy14 with dissolve
mc "* Her armhold is... super-strong! I can't... breathe... *"
scene embassy16 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "SUPER-STRENGTH IN ACTION!"
scene embassy17 with dissolve
mc "Oh, you want to fight, hey? Well, I'm prepared to take on BOTH OF YOU METAL FREAKS!"
scene embassy18 with dissolve
play sound "sounds/punch.mp3"
mc "You want some of that? Then eat my shoe!"
scene embassy19 with dissolve
mc "Oh, no you won't hit my soft baby skin face!"
scene embassy20 with dissolve
mc "Now, yield, big-titted ballerina Soviet robot! I have the upper h..."
scene embassy21 with dissolve
play sound "sounds/punch.mp3"
mc "...Yikes!"
scene embassy22 with dissolve
stop music
play music "sounds/sexy02.mp3"
mc "Uh oh... I'm in deep trouble now..."
scene embassy23 with dissolve
mc "Just let me go, I promise I won't come back ever again!"
scene embassy24 with dissolve
mc "Oh God, she even has a realistic pussy, now I'm getting an erection..."
scene embassy25 with dissolve
mc "I see, you girls want to have some fun with my SUPERHERO COCK, hey? Then be my guest, I'll DESTROY your pussies and I'll finally be able to get through!"
scene embassy26 with dissolve
play sound "sounds/kiss.mp3"
mc "* Damn, I'm kissing a mouthless metal robot. Feels pretty good actually... *"
scene embassy27 with dissolve
if age >= 20:
    mc "Yeah, play with my massive balls, I'm gonna cover your tits in an inch-thick layer of my cream!"
if age >= 18 and age <= 19:
    mc "Yeah, play with my massive balls, I'm gonna cover your tits in an inch-thick layer of my teenage cream!"
scene embassy28 with dissolve
mc "Now hang on ladies, this is getting a bit TOO femdom-y to my lik..."
scene embassy29 with dissolve
mc "* She's pinning my throat with her metal arse! *"
scene embassy30 with dissolve
mc "* While the other sex-crazed ballerina is about to ride my dong mercilessly! *"
mc "* I think they're not just killer robots, they're SEX KILLER ROBOTS! * Gonna have to... survive this! *"
play channel2 "sounds/boymoan02.mp3"

label RobotAssFuckSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckslowvideo behind robotassfuckfastvideo
show robotassfuckslowvideo behind robotassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckfastvideo
hide robotassfuckfrontslowvideo
with dissolve
play channel1 "sounds/wank.mp3"
mc "* Oh Fuck, she can take ssso many inches of my shaft inside her arse, it's amazing! *"
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen robotassfuckslowx()
screen robotassfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("RobotAssFuckFrontSlowx")

label RobotAssFuckFastx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfastvideo behind robotassfuckslowvideo
show robotassfuckfastvideo behind robotassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckslowvideo
hide robotassfuckfrontfastvideo
with dissolve
play channel1 "sounds/wetmassage.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen robotassfuckfastx()
screen robotassfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("RobotAssFuckFrontFastx")

label RobotAssFuckFrontSlowx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfrontslowvideo behind robotassfuckslowvideo
show robotassfuckfrontslowvideo behind robotassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckslowvideo
hide robotassfuckfrontfastvideo
with dissolve
play channel1 "sounds/wank.mp3"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen robotassfuckfrontslowx()
screen robotassfuckfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckSlowx")

label RobotAssFuckFrontFastx:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfrontfastvideo behind robotassfuckfastvideo
show robotassfuckfrontfastvideo behind robotassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckfastvideo
hide robotassfuckfrontslowvideo
with dissolve
play channel1 "sounds/wetmassage.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen robotassfuckfrontfastx()
screen robotassfuckfrontfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFastx")

label RobotAssFuckEndx:
hide cum
hide assview
hide faster
hide slower
hide front
mc "* I'm starting to get dizzy... And my balls DEMAND release at the same time! *"
scene robotcum01 with dissolve
stop channel2
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "FU-UUUUCK!"
window hide
with fastflash
mc "I'm CUMMMING, AAAAH!"
scene robotcum02 with dissolve
mc "* Nooo! She's CRUSHING my pelvis! *"
window hide
with hpunch
mc "* Must... FIGHT IT! *"
scene robotcum03a with dissolve
play channel2 "sounds/splooge02.mp3"
mc "By FLOODING her insides, RHAAA!"
window hide
with fastflash
play sound "sounds/boymoan03.mp3"
mc "Take that!"
scene robotcum04 with dissolve
play sound "sounds/effort01.mp3"
mc "GGGG... Gotta cum some MORE!"
window hide 
with hpunch
mc "Gotta BLAST it out... And keep that other robot from choking me!"
scene robotcum05 with dissolve
stop channel2
stop channel1
play channel4 "sounds/boymoan05.mp3"
play sound "sounds/splooge03.mp3"
mc "...NOW! RHAAAA!"
window hide
with vpunch
mc "FUCK, YEAH, AAAAH!"
scene robotcum06 with dissolve
stop channel4
play sound "sounds/glitch.mp3"
mc "That's it, next robot to SUBDUE with my mighty PILLAR!"
scene robotcum07 with dissolve
mc "And my mighty MUSCLES! What are you gonna do? Who's your daddy now?"
scene robotcum08 with dissolve
play sound "sounds/bonecrack.mp3"
mc "Since you don't seem to get the message and I don't have all day, I'm gonna get rid of you ONCE and FOR ALL!"
scene robotcum09 with dissolve
stop music
play sound "sounds/glitch.mp3"
mc "Finally, the coast is clear. I'm not even gonna bother putting my thong back on before going back to the gallery."
stop sound
stop channel3
stop channel1
stop music
jump NatalyaGallery

label NatalyaGallery02:
stop channel3
stop music
play music "sounds/sexy09.mp3"
scene widownatalya01:
    zoom 0.5
with fade
mc "* What's going on here? I bet that Soviet agent is trying to manipulate the Black Widow again! Let me zoom in and try and listen to what they are talking about... *"
show widownatalya01:
    subpixel True
    linear 4.0 zoom 1.0 xpos -0.5 ypos -0.3
nt "You know this is for the best. For the best of Mother Russia!"
scene widownatalya02 with dissolve
bw "I understand my mission, I will obey, Major Natalya."
nt "Good, then maybe I can finally UNLEASH you..."
scene widownatalya03 with dissolve
nt "There. What are you going to do now to thank me for showing you the right path?"
scene widownatalya04 with dissolve
bw "I..."
scene widownatalya05 with dissolve
play sound "sounds/kiss.mp3"
nt "Don't say a word. Just kiss me, Natasha..."
scene widownatalya06 with dissolve
nt "Now I will implant the bugging device you know where."
bw "I'm very... sensitive down there."
nt "I bet you are. You have been DEPRAVED by Western decadence!"
scene widownatalya07 with dissolve
nt "But I will show you the way of Soviet PURITY!"
scene widownatalya08 with dissolve
play sound "sounds/moan02.mp3"
nt "With a iron FIST if need be!"
scene widownatalya09 with dissolve
nt "Normally, you shouldn't be enjoying this AT ALL... We'll see if you have been well-trained..."
play channel1 "sounds/wetmassage.mp3"
play channel2 "sounds/moan02.mp3"
window hide

label NatalyaFistSlowxx: 
hide faster
hide slower
hide nexticon
show natalyafistslowvideo behind natalyafistfastvideo
pause 1.0
hide natalyafistfastvideo with dissolve
show faster:
     xpos 1700 ypos 500     
show nexticon:
    xpos 1750 ypos 1020       
call screen natalyafistslowxx()
screen natalyafistslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEndxx")

label NatalyaFistFastxx:
hide slower
hide faster
hide nexticon
show natalyafistfastvideo behind natalyafistslowvideo
nt "What if I fisted you a bit faster? I wonder what would happen then..."
window hide
hide natalyafistslowvideo with dissolve
show slower:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen natalyafistfastxx()
screen natalyafistfastxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEndxx")

label NatalyaFistEndxx:
hide nexticon
hide slower
hide faster
nt "You're enjoying this, aren't you? All that Western decadence CORRUPTION is showing!"
bw "No, I ... It just reminds me of someone's c..."
nt "Oh, I see. That stupid Super-Hero with the stupid thong? Did he go as deep as THIS though?"

label NatalyaFistHarderSlowxx:  
hide faster
hide slower
hide nexticon
show natalyafistharderslowvideo behind natalyafistharderfastvideo
pause 1.0
hide natalyafistharderfastvideo with dissolve
play sound "sounds/womangroan.mp3"
bw "AAAH, it's so DEEP!"
show faster:
     xpos 1700 ypos 500     
show nexticon:
    xpos 1750 ypos 1020       
call screen natalyafistharderslowxx()
screen natalyafistharderslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEndxx")

label NatalyaFistHarderFastxx:
hide slower
hide faster
hide nexticon
show natalyafistharderfastvideo behind natalyafistharderslowvideo
play sound "sounds/moan04.ogg"
nt "You want it even FASTER, don't you, Natasha?"
bw "No... I..."
window hide
hide natalyafistharderslowvideo with dissolve
show slower:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen natalyafistharderfastxx()
screen natalyafistharderfastxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEndxx")

label NatalyaFistHarderEndxx:
hide nexticon
hide slower
hide faster
scene widownatalya10 with dissolve
nt "I think... I placed it in the right spot..."
stop channel1
stop channel2
scene natalyafistcum01 with dissolve
play sound "sounds/moan06.ogg"
nt "Oh yeah, most definitely!"
scene natalyafistcum02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1        
with dissolve
play sound "sounds/moan03.mp3"
pause
nt "Look at all that filthy anal cream. We should invent a word for it. Like santorum or something."
mc "* I think it's time to intervene... *"
scene widownatalya11 with dissolve
mc "Stop this right there! I kind of enjoyed this, but it's going too far! And too deep."
nt "You again! Always at the wrong place at the wrong time..."
mc "What are you up to, Agent Natalya? SPEAK!"
scene widownatalya12 with dissolve
nt "We were discussing how DEPRAVED this country is. And how superior the PURITY of the Soviet Way of Life is!"
mc "Says the commie fister!"
scene widownatalya13 with dissolve
nt "Why are you so angry? People in the Soviet Union are never angry. You could be their hero. If you wanted..."
bw "Yes. And MY hero..."
mc "Pure propaganda! I'm not as easily manipulated as an Iowa country bumpkin during a Republican primary!"
scene widownatalya14 with dissolve
nt "You're walking around in a thong, that's just disgusting! If you were a Soviet Super-Hero, you would have a PROPER costume... With a CAPE."
mc "I would?"
    
scene widownatalya15:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/dream.mp3"
show mcsoviethero01:
    xpos 0.02 ypos 0.02
with dissolve
nt "And the Black Widow could be your PERSONAL side-kick to bring Soviet Peace and Justice to this country..."
mc "I..."
hide mcsoviethero01
show mcsoviethero02:
    xpos 0.02 ypos 0.02
with fastdissolve
nt "Imagine how the people of Cockham would worship you once you give them back what was STOLEN from them by the evil capitalists! Such as Bruce Vayne... Or Batman if you prefer..."
scene widownatalya16:
    subpixel True
    zoom 1 xpos 0 ypos -0.02
    ease 10 xpos -0.05 ypos 0.0 zoom 1.05
show mcsoviethero03:
    xpos 0.52 ypos 0.02
with dissolve
mc "Ah yeah, that billionaire dude, he's not even a REAL Super-Hero!"
nt "No he's not. But YOU ARE. A Super-Hero of the PEOPLE... With my help... And the Black Widow, she's just ACHING to be your side-kick, aren't you, Natasha?"
scene widownatalya17 with dissolve
bw "Yes. Join us [name], the Soviets are destined to rule the world. The Soviet Union will NEVER fall."
nt "We are ONE people, Russian and Ukrainian brothers who would never fight each other like the Americans do all the time. We are the country of Peace, and your country NEEDS us!"
bw "Join us..."
nt "Yes, JOIN US!"
if evilness <= 12:
    scene widownatalya18a with dissolve
    mc "Not a chance, I'm an ALL-AMERICAN SUPER-HERO!"
    nt "So be it, then I will have to SUBDUE you!"
if evilness >= 13:
    scene widownatalya18b with dissolve
    mc "Maybe... It sounds like it could fit my plan for Super-Domination of Cockham pretty well, it's a deal. BUT..."
    nt "But WHAT?"
    scene widownatalya18c with dissolve
    mc "You'll be the ones under MY COMMAND!"
    nt "Mother Russia has no Master but Mother Russia! And whoever is the First Secretary of the Communist Party obviously."
    scene widownatalya18a with dissolve
    mc "Then we are at an impasse, Agent Natalya..."
    nt "I think not!"

play music "sounds/radiation02.mp3"
show spiral:
    subpixel True
    rotate 0 xanchor 0.285 yanchor 0.375    
    linear 10.0 rotate 360
    repeat
show natalyahypno:   
    subpixel True
    zoom 0.9 xpos -0.05 ypos 0.0
    linear 5.0 zoom 1.0 xpos -0.1 ypos -0.05
    linear 5.0 zoom 0.9 xpos -0.05 ypos 0.0
    repeat
nt "Submit to my will, [name]."
mc "She's trying to hypnotize me! I must... RESIST..."
call screen usepower("useresistance", "HypnoNoResistancexx", "HypnoResistancexx") with dissolve

label HypnoNoResistancexx:
"You are slowly being turned into a Soviet zombie sleeper agent..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
jump NatalyaGallery    

label HypnoResistancexx:
stop music
scene widownatalya18a with dissolve
mc "Now, it's MY turn!"
$ img_l = []
$ l2_l = []
if mccombat >= 0:
    $ img_l.append("usecombat")
    $ l2_l.append("HypnoCombatxx")
if mcmind >= 0:
    $ img_l.append("usemind")
    $ l2_l.append("HypnoCombatxx")
if img_l:
    call screen usepower(img_l, "HypnoNoCombatxx", l2_l) with dissolve

label HypnoNoCombatxx:
mc "* You're too slow, player! Let's try this again..."
jump HypnoResistancexx

label HypnoCombatxx:
if selected_power == "usemind":
    play music "sounds/radiation02.mp3"    
    scene widownatalya20 with dissolve
    mc "YOU submit to my will!"
    stop music

if selected_power == "usecombat":
    scene widownatalya21 with dissolve
    play sound "sounds/punch.mp3"
    mc "Take THAT, filthy commie spy!"
    scene widownatalya22 with dissolve
    play sound "sounds/femalegrunt01.mp3"
    mc "Are you going to be a good little girl and SUBMIT, Natalya?"
    nt "I... Fine, I SUBMIT, please let me go, you're hurting me!"

scene widownatalya23:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
if evilness <= 12:
    mc "The tables have turned... And to make sure you understand what I mean when I say I'm an All-American Super-Hero, I'll show you what makes me such a SUPER-HERO!" 
if evilness >= 13:
    mc "The tables have turned... And to make sure you understand what our agreement is all about, I'll show you what makes me such a powerful secret SUPER-VILLAIN!" 
play music "sounds/sexy09.mp3"
scene natalyapreblow01 with dissolve
play sound "sounds/wow.mp3"
nt "I've never seen a Soviet cock THIS big!"
mc "That's right. THIS is a REAL SUPERHERO COCK!"
scene natalyapreblow02 with dissolve
play sound "sounds/slap.mp3"
mc "One that carries a heavy punch!"
scene natalyapreblow03 with dissolve
play sound "sounds/slap.mp3"
mc "For those who DISOBEY me!"
scene natalyapreblow04 with dissolve
mc "So get going and get SUCKING!"
bw "Yes MASTER!"
play channel2 "sounds/wank.mp3"
$ natalyablowslowx = False

label NatalyaBlowSlowxx:
$ natalyablowfastx = False
window hide
show natalyablowslowvideo behind natalyablowfastvideo
show natalyablowslowvideo behind natalyablowpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyablowfastvideo
hide natalyablowpovslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowslowx == False:
    $ natalyablowslowx = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowslowxx()
screen natalyablowslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVSlowxx")

label NatalyaBlowFastxx:
$ natalyablowslowx = False
window hide
show natalyablowfastvideo behind natalyablowslowvideo
show natalyablowfastvideo behind natalyablowpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyablowpovfastvideo
hide natalyablowslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowfastx == False:
    $ natalyablowfastx = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowfastxx()
screen natalyablowfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVFastxx")

label NatalyaBlowPOVSlowxx:
$ natalyablowfastx = False
window hide
show natalyablowpovslowvideo behind natalyablowslowvideo
show natalyablowpovslowvideo behind natalyablowpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyablowpovfastvideo
hide natalyablowslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowslowx == False:
    $ natalyablowslowx = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckslowxx()
screen natalyablowpovfuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowSlowxx")

label NatalyaBlowPOVFastxx:
$ natalyablowslowx = False
window hide
show natalyablowpovfastvideo behind natalyablowfastvideo
show natalyablowpovfastvideo behind natalyablowpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyablowfastvideo
hide natalyablowpovslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
if natalyablowfastx == False:
    $ natalyablowfastx = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckfastxx()
screen natalyablowpovfuckfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowFastxx")

label NatalyaBlowEndxx:
hide nexticon
hide closer
hide faster
hide slower
hide pov
mc "I think your jaws need some more stretching, don't you think?"
if evilness <= 12:
    nt "I... Yes, Good Master."
if evilness >= 13:
    nt "I... Yes, Evil Master."
stop channel1
stop channel2
scene natalyapostblow01:
    subpixel True
    zoom 1 xpos 0 ypos -0.02
    ease 10 xpos -0.05 ypos 0.0 zoom 1.05
with dissolve
mc "So time for your big mouths to OPEN WIDE!"
play channel2 "sounds/wank.mp3"
$ natalyaswitchslowx = False

label NatalyaSwitchBlowSlowxx:
$ natalyaswitchfastx = False
window hide
show natalyaswitchslowvideo behind natalyaswitchfastvideo
show natalyaswitchslowvideo behind natalyaswitchcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyaswitchfastvideo
hide natalyaswitchcloserslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchslowx == False:
    $ natalyaswitchslowx = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchslowxx()
screen natalyaswitchslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlowxx")

label NatalyaSwitchBlowFastxx:
$ natalyaswitchslowx = False
window hide
show natalyaswitchfastvideo behind natalyaswitchslowvideo
show natalyaswitchfastvideo behind natalyaswitchcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyaswitchcloserfastvideo
hide natalyaswitchslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchfastx == False:
    $ natalyaswitchfastx = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchfastxx()
screen natalyaswitchfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVFastxx")

label NatalyaSwitchBlowPOVSlowxx:
$ natalyaswitchfastx = False
window hide
show natalyaswitchcloserslowvideo behind natalyaswitchslowvideo
show natalyaswitchcloserslowvideo behind natalyaswitchcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyaswitchcloserfastvideo
hide natalyaswitchslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchslowx == False:
    $ natalyaswitchslowx = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckslowxx()
screen natalyaswitchcloserfuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowSlowxx")

label NatalyaSwitchBlowPOVFastxx:
$ natalyaswitchslowx = False
window hide
show natalyaswitchcloserfastvideo behind natalyaswitchfastvideo
show natalyaswitchcloserfastvideo behind natalyaswitchcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyaswitchfastvideo
hide natalyaswitchcloserslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
if natalyaswitchfastx == False:
    $ natalyaswitchfastx = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckfastxx()
screen natalyaswitchcloserfuckfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowFastxx")

label NatalyaSwitchBlowEndxx:
stop channel1
stop channel2
scene natalyapostblow02 with dissolve
mc "Nice, you did a good enough job. Now turn round and offer your womanhoods to my CUNT-DESTROYER!"
bw "Who should go first?"
mc "Agent Natalya. She needs to be PUNISHED what what she's done!"
scene natalyaprefuck01 with dissolve
mc "And PUNISHED she will be!"
scene natalyaprefuck02 with dissolve
if age >= 20:
    nt "Your Western monstercock... It's just TOO BIG!"
if age >= 18 and age <= 19:
    nt "Your Western teenage monstercock... It's just TOO BIG!"
mc "Or maybe it's your tiny Commie pussy that's TOO TIGHT! Let's find out..."
scene natalyaprefuck03 with dissolve
play sound "sounds/womancum01.mp3"
nt "AAAH!"
mc "I guess you're right. It's my American cock that's just HUMONGOUS. Your pussy is just fine."
bw "He's going to DESTROY you, Natalya, get ready for it... I'm sorry, but I can't help you, he's just too... MANLY!"
$ natalyafuckslowx = False

label NatalyaFuckSlowxx:
$ natalyafuckfastx = False
window hide
show natalyafuckslowvideo behind natalyafuckfastvideo
show natalyafuckslowvideo behind natalyafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyafuckfastvideo
hide natalyafuckpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckslowx == False:
    $ natalyafuckslowx = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckslowxx()
screen natalyafuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVSlowxx")

label NatalyaFuckFastxx:
$ natalyafuckslowx = False
window hide
show natalyafuckfastvideo behind natalyafuckslowvideo
show natalyafuckfastvideo behind natalyafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "v031/womansex07.mp3"
hide natalyafuckpovfastvideo
hide natalyafuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckfastx == False:
    $ natalyafuckfastx = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckfastxx()
screen natalyafuckfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVFastxx")

label NatalyaFuckPOVSlowxx:
$ natalyafuckfastx = False
window hide
show natalyafuckpovslowvideo behind natalyafuckslowvideo
show natalyafuckpovslowvideo behind natalyafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyafuckpovfastvideo
hide natalyafuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckslowx == False:
    $ natalyafuckslowx = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckslowxx()
screen natalyafuckpovfuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckSlowxx")

label NatalyaFuckPOVFastxx:
$ natalyafuckslowx = False
window hide
show natalyafuckpovfastvideo behind natalyafuckfastvideo
show natalyafuckpovfastvideo behind natalyafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "v031/womansex07.mp3"
hide natalyafuckfastvideo
hide natalyafuckpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if natalyafuckfastx == False:
    $ natalyafuckfastx = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckfastxx()
screen natalyafuckpovfuckfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckFastxx")

label NatalyaFuckEndxx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
bw "Are you about to give her your nutload, [hero]?"
play sound "sounds/panting.mp3"
mc "Fuck yeah, close..."
scene natalyafuckcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "CLOSER, RHAAA!"
window hide
with fastflash
nt "I'm being stuffed by a giant Western cock! AAAH!"
scene natalyafuckcum02 with dissolve
play sound "sounds/splooge02.mp3"
mc "That's right, and now I'm going to fill you up like an AMERICAN GAS-GUZZLER!"
window hide
with vpunch
mc "FUCK YEAH!!!!"
scene natalyafuckcum03 with dissolve
play sound "sounds/splooge03.mp3"
bw "Go on, [hero], fill her tight Russian fuckhole with your super-hero cream, show her what she's been missing!"
window hide
with fastflash
nt "TOO MUCH! AAAH!!!"
scene natalyafuckcum04 with dissolve
mc "Never ENOUGH for a All-American SUPER-STUD!!!"
window hide
with hpunch
bw "COVER HER WITH YOUR CREAM!"
scene natalyafuckcum05 with dissolve
mc "YAAAH!"
window hide
with fastflash
nt "I Submit, I submit! I'll leave the Black Widow alone and help you in any way I can..."
scene natalyafuckcum06 with dissolve
stop channel1
mc "Phew... I knew you would... Eventually..."
bw "But what about me, [hero]? I never said I would submit... * wink *"
scene natalyafuckcum07:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "Oh, I see. You want me to make you SUBMIT, hey?"
bw "Yes, Daddy! Then I'll become your harem slave... You want that, don't you?"
mc "Oh fuck, that's it, I'm STILL HARD because of your naughty talk!"
scene natalyafuckcum08 with dissolve
mc "SO HARD in fact that I'm just going to need to POUND that nice pussy of yours HARD and FAST!"
bw "Oooh, I'm going to get punished too for being such a naughty commie spy then?"
scene natalyafuckcum09 with dissolve
play sound "sounds/moan05.mp3"
mc "Yes! And I'll turn you into my personal obedient harem cock-slut!"
bw "AAAH, I can't wait Daddy!"

label NatalyaWidowFuckSlowxx:
window hide
show natalyawidowfuckslowvideo behind natalyawidowfuckfastvideo
show natalyawidowfuckslowvideo behind natalyawidowfuckfastervideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyawidowfuckfastvideo
hide natalyawidowfuckfastervideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
mc "So you want to become my harem slave, Natasha?"
bw "Ooh, yes daddy! But fuck me some more first... Aaah..."
show faster:
     xpos 1700 ypos 500    
call screen natalyawidowfuckslowxx()
screen natalyawidowfuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFastxx")

label NatalyaWidowFuckFastxx:
window hide
show natalyawidowfuckfastvideo behind natalyawidowfuckslowvideo
show natalyawidowfuckfastvideo behind natalyawidowfuckfastervideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide natalyawidowfuckfastervideo
hide natalyawidowfuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
bw "Ooh... God... Daddy, you fuck me so POWERFULLY!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show slower:
     xpos 50 ypos 500    
call screen natalyawidowfuckfastxx()
screen natalyawidowfuckfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFasterxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckSlowxx")

label NatalyaWidowFuckFasterxx:
window hide
show natalyawidowfuckfastervideo behind natalyawidowfuckfastvideo
show natalyawidowfuckfastervideo behind natalyawidowfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide natalyawidowfuckfastvideo
hide natalyawidowfuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov  
bw "Yes, Yes, fuck me HARD and FAST DADDY!!!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
call screen natalyawidowfuckfasterxx()
screen natalyawidowfuckfasterxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEndxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckFastxx")

label NatalyaWidowFuckEndxx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
bw "Am I going to get impregnated by your fat load, daddy?"
mc "Is that what you want?"
bw "Yes daddy, give your little Russian cock-whore a baby!"
scene widownatalyafuckcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "THERE YOU GO THEN!!!"
window hide
with fastflash
bw "I can feel it Daddy, I can feel your fertile seed inside my poor little slut pussy!!!"
scene widownatalyafuckcum02 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE, YOU'LL FEEL IT EVEN BETTER, RHAAA!"
window hide
with vpunch
play sound "sounds/womancum02.mp3"
bw "AAAAH!"
scene widownatalyafuckcum03 with dissolve
mc "COMING SO MUCH, RHAAA!"
window hide
with fastflash
nt "Her... stomach is distending from the super-heroic amount of come you're dumping inside her!"
scene widownatalyafuckcum04:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
nt "Are you alright, Natasha? Say something!"
window hide
with fastflash
bw "Uuuh.... HE'S STILL PUMPING ME FULL!"
nt "Pull out, I beg you [hero], I'll do anything you want but don't destroy her womb like that!"
scene widownatalyafuckcum05 with dissolve
stop channel2
play sound "sounds/femalegrunt01.mp3"
bw "I can do it myself, AAAAH!"
window hide
with vpunch
nt "Well done, you're plastering him with his own cum, that will teach him a lesson!"
scene widownatalyafuckcum06 with dissolve
play sound "sounds/splooge01.mp3"
mc "I'm not done yet, I'll keep showering you with even MORE scum than you pump out, Natasha!"
window hide
with fastflash
play sound "sounds/splat.ogg"
bw "UUUUH! NEED... TO.... BEAT... HIM!"
scene widownatalyafuckcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Came... so much... Did I win?..."
scene widownatalyafuckcum08 with dissolve
nt "I have to admit you... caked her in GALLONS of cum. We are defeated. And the Black Widow is now yours to dispose of as you wish..."
stop sound
stop channel3
stop channel1
stop music
jump NatalyaGallery