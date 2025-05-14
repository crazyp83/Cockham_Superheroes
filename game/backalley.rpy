label PreCatCave:
if preloccatcave and loccatcave == False:
    jump BackAlley
if loccatcave:
   jump CatCave

label BackAlley:
play music "sounds/covertmusic.mp3"
scene backalley01 with fade
mc "This is the address Lois Pane gave me... Let's have a look in that dodgy back alley. I ain't scared of nothing, cos I'm a SUPERHERO!"
scene backalley02 with dissolve
mc "Ah, there she is, hanging from the scaffolding like an acrobat."
scene backalley03 with dissolve
play sound "v05/meow.mp3"
cw "Miaow! Are you looking for me, [name]? Try and catch me if you can!"
scene backalley04 with dissolve
mc "Hey, where are you going? I just want to talk!"
stop music
play music "v042/carchase.mp3"
scene backalley05 with dissolve
mc "Damn it, now I'm going to have to run after her. Or jump more likely."
scene backalley06 with dissolve
mc "You can't escape me now, Catwoman, you're MINE!"
scene backalley07 with dissolve
mc "What is she doing, she must be mad!"
scene backalley08 with dissolve
mc "Oh no, she ain't mad. She's CATWOMAN. And she can jump from one building to the next."
scene backalley09 with dissolve
mc "No other choice than to do the same and prove to the world that I am SUPER-AGILE!"
call screen usepower("useagility", "BackAlleyNoAgility", "BackAlleyAgility") with dissolve

label BackAlleyNoAgility:
scene backalley10
show backalley10b
with dissolve
mc "Uh oh... I think I might fall to my death..."
window hide
play sound "sounds/wilhelmscream.mp3"
show backalley10b at backalleydown
$ renpy.pause(2.0, hard='True')
play sound "sounds/splat.ogg"    
show gameovericon:
    xpos 600 ypos 400
pause
return

label BackAlleyAgility:
scene backalley10c with dissolve
play sound "sounds/mangrunt01.mp3"
mc "GERONIMO!"
$ usedagility += 1
scene backalley11 with dissolve
stop music
play sound "sounds/thud.mp3"
mc "Will you stop jumping around now? I just want to talk to you... About some GOLD we could get our hands on!"
cw "Gold? Well, why didn't you say so earlier! Follow me to my... cat cave."

label CatCave:
play music "sounds/relax.mp3"
scene catwomanlair01
show catwomaneyeblink
with fade
$ loccatcave = True
if mission06end == False:
    cw "This is it. So, about that GOLD?"
label CatwomanLairNewDialogues:
menu:
    "The Stallion has a huge quantity of gold stored in his safe. And I know the code." if mission06end == False:
        hide catwomaneyeblink
        show catwoman03 at centerleft
        with fastdissolve        
        cw "Miaow! You do? What's my cut if I pull this off for you?"
        mc "Err... Like, fifty-fifty?"
        hide catwoman03
        show catwoman02 at centerleft
        with fastdissolve        
        cw "That doesn't sound fair, I take all the risks."
        mc "Not true! We have to get in and face possible violent threats from his gang. You'll need ME to beat them off!"
        hide catwoman02
        show catwoman04 at centerleft
        with fastdissolve        
        cw "I suppose. I agree then, when do we make a move?"
        mc "Tonight. This is a mission and I don't have any more time to waste."                                                                                
        hide catwoman04
        show catwoman02 at centerleft
        with fastdissolve        
        play sound "v05/meow.mp3"
        cw "Miaow! You're a feisty little one, aren't you? Let's go!"
        jump Mission06Stallion
    "Boy, this place is a dump!" if spokecatwoman01 == False:
        $ spokecatwoman01 = True
        hide catwomaneyeblink
        show catwoman02 at centerleft
        with fastdissolve        
        cw "It might not look like much but I LIKE it! This is where I live, and it contain unseen riches beyond your imagination..."
        mc "Sorry, I was just being an asshole."
        hide catwoman02
        show catwomaneyeblink
        with fastdissolve        
        cw "Well stop being one."
        jump CatwomanLairNewDialogues    
    "Well, now that we're here, and I'm feeling SAY-AY-EXY!..." if spokecatwoman02 == False:
        $ spokecatwoman02 = True
        hide catwomaneyeblink
        show catwoman03 at centerleft
        with fastdissolve        
        cw "Sexy? You? With that silly thong?"
        mc "Hey! It ain't silly, it's functional. It can hold my huge package and clearly states I'm a Superhero not to be messed with!"
        hide catwoman03
        show catwoman04 at centerleft
        with fastdissolve
        cw "Well, I like a challenge, and I'm going to MESS WITH YOU!" 
        window hide
        hide catwoman04 with moveoutleft
        jump CatWomanSex
    "I'm feeling SAY-AY-EXY again! That's why I came." if spokecatwoman02:
        hide catwomaneyeblink
        show catwoman04 at centerleft
        with fastdissolve        
        cw "You're very direct. But I like my boys FEISTY. Wait for me. And GET HARD FOR ME!"
        window hide
        hide catwoman04 with moveoutleft
        jump CatWomanSex
    "What are these paintings over there? You stole them?" if spokecatwoman03 == False:
        $ spokecatwoman03 = True
        hide catwomaneyeblink
        show catwoman02 at centerleft
        with fastdissolve        
        cw "What if I did? What are you going to do?"
        mc "Err.. Right now, nothing. Cos it ain't a SEX crime, so it's got nothing to do with me."
        hide catwoman02
        show catwomaneyeblink
        with fastdissolve 
        cw "That's right. Mind your own SEX business."
        jump CatwomanLairNewDialogues

label CatWomanSex:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy03.mp3"
$ renpy.pause(1.0, hard='True')
show catwoman05 with moveinleft
cw "You think you're sexy? How about THIS?"
mc "Damn, yeah, that's definitely SAY-AY-EXY!"
play sound "v05/purring.mp3"
window hide
hide catwoman05
show catwomanlair01 blurred:
    zoom 1.8 xoffset -100 yoffset 0
show catwoman06:
    zoom 1.0 xoffset 200 yoffset -1080    
show catwomanlair01 blurred at widowfullbackzoombackground
show catwoman06 at powerpoolfulldown
with dissolve
$ renpy.pause(4.0, hard='True')
pause        
cw "Would you stroke this pussy?"
mc "That joke's been done and gone, but yeah."
window hide
hide catwoman06
show catwoman07:
    zoom 1.0 xoffset 300 yoffset 0    
show catwomanlair01 blurred at widowbackfullbackzoombackground
show catwoman07 at powerpoolfullup
with dissolve
$ renpy.pause(4.0, hard='True')
pause
cw "Would you mark your territory with your paw back there?"
mc "I would, and right now, I'm hard and ROARING to go!"
scene catwomanlair01
show catwoman07b
with dissolve
cw "Then let me dim the lights, I see better in the dark... And I'll go and sit on my mat. Miaow!"
play sound "v05/meow.mp3"
hide catwoman07b with moveoutleft

label CatwomanSexDialogues:
if fuckedcatwoman == False:
    scene catwoman08 with dissolve
if fuckedcatwoman:    
    scene catwoman08b with dissolve
cw "So, tiger, what do you plan to do with Catwoman?"
menu:
    "I plan to grab her by the pussy!":
        if fuckedcatwoman == False:
            scene catwoman11 with dissolve
        if fuckedcatwoman:    
            scene catwoman11b with dissolve
        play sound "v05/meow.mp3"
        cw "Which pussy? THIS pussy or THAT pussy?..."
        mc "Err... Thas pussy?"
        jump CatWomanPussySex
    "The tiger is the Alpha in the feline rank. So ANAL SUBDUCTION it is!":
        if fuckedcatwoman == False:
            scene catwoman09 with dissolve
        if fuckedcatwoman:    
            scene catwoman09b with dissolve
        cw "Fucking a pussy up the ass, is that even a thing?"
        mc "It will be now!"
        if fuckedcatwoman == False:
            scene catwoman10 with dissolve
        if fuckedcatwoman:    
            scene catwoman10b with dissolve 
        cw "Then let me raise my tail and show you my puckered hole..."
        play sound "v05/purring.mp3"
        mc "Yeah, that's what happy pussies do."
        jump CatWomanAnalSex
    "Are you a thirsty pussy? Cos I have a HUGE supply of spunk-milk for you to blow out of my rod!" if mission06end and fuckedcatwoman:
        scene catwoman09b with dissolve
        cw "You want a blowjob?"
        mc "That was the idea."
        scene catwoman08b with dissolve
        play sound "v05/purring.mp3"
        cw "I LIKE that idea..."
        jump CatWomanBlowJob
    "We're done here.":
        if fuckedcatwoman == False:
            scene catwoman09 with dissolve
        if fuckedcatwoman:    
            scene catwoman09b with dissolve
        cw "So soon already? It's only midnight, I'm going out then!"
        mc "Where's the door by the way?"
        cw "Door? You need to use that cat flap behind you."
        $ fuckedcatwoman = False
        stop music
        show screen calendar
        show screen statscreenicon
        show screen questscreenicon
        jump Main

label CatWomanBlowJob:
scene catpreblow01 with dissolve
play sound "v05/meow.mp3"
cw "Let me stretch my body so I can be as supple as I need for this mighty blowjob!"
mc "There will be a lot of stretching involved indeed."
scene catpreblow02 with dissolve
cw "Really? You want to stretch this little pussy's mouth?"
mc "I sure do."
cw "How BIG will you stretch it?"
scene catpreblow03 with dissolve
play sound "v05/purring.mp3"
mc "THIS big. Hope you can manage. I imagine you can."
cw "Ooh, that is a very BIG stretch of the imagination."
scene catpreblow04 with dissolve
play sound "sounds/lick01.ogg"
cw "Let me lick the tip and impregnate my snout with its virile smell!"
scene catpreblow05 with dissolve
play sound "sounds/lick02.mp3"
mc "Ooh yeah, that's going to be a SWEE-EE-EET blowjob!"

label CatBlowSlow:
$ catharder = False
$ catblowfaster = False
window hide
show catblowslowvideo behind catblowfastvideo
show catblowslowvideo behind catblowpovslowvideo
show catblowslowvideo behind catblowharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowfastvideo
hide catblowpovslowvideo
hide catblowharderslowvideo
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
call screen catblowslow()
screen catblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowPOVSlow")

label CatBlowFast:
$ catharder = False
if catblowfaster == False:
    $ catblowfaster = True
    mc "That's nice, but go faster now... Just the tip, like before..."
window hide
show catblowfastvideo behind catblowslowvideo
show catblowfastvideo behind catblowpovfastvideo
show catblowfastvideo behind catblowharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowslowvideo
hide catblowpovfastvideo
hide catblowharderfastvideo
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
call screen catblowfast()
screen catblowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowPOVFast")

label CatBlowPOVSlow:
$ catharder = False
$ catblowfaster = False
window hide
show catblowpovslowvideo behind catblowslowvideo
show catblowpovslowvideo behind catblowpovfastvideo
show catblowpovslowvideo behind catblowharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowslowvideo
hide catblowpovfastvideo
hide catblowharderpovslowvideo
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
call screen catblowpovslow()
screen catblowpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowSlow")

label CatBlowPOVFast:
$ catharder = False
if catblowfaster == False:
    $ catblowfaster = True
    mc "That's nice, but go faster now... Just the tip, like before..."
window hide
show catblowpovfastvideo behind catblowpovslowvideo
show catblowpovfastvideo behind catblowfastvideo
show catblowpovfastvideo behind catblowharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowpovslowvideo
hide catblowfastvideo
hide catblowharderpovfastvideo
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
call screen catblowpovfast()
screen catblowpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowFast")

label CatBlowHarderSlow:
$ catdeeper = False
$ catblowfaster = False
if catharder == False:
    mc "Time to take it up a notch. Get more of my monster meat down your throat!"
    $ catharder = True        
window hide
show catblowharderslowvideo behind catblowharderfastvideo
show catblowharderslowvideo behind catblowharderpovslowvideo
show catblowharderslowvideo behind catblowslowvideo
show catblowharderslowvideo behind catblowdeeperslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowharderfastvideo
hide catblowharderpovslowvideo
hide catblowslowvideo
hide catblowdeeperslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
show harder:
    xpos 1700 ypos 700    
call screen catblowharderslow()
screen catblowharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatBlowSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowDeeperSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVSlow")

label CatBlowHarderFast:
$ catdeeper = False
$ catblowfaster = False
if catharder == False:
    mc "Time to take it up a notch. Get more of my monster meat down your throat!"
    $ catharder = True        
window hide
show catblowharderfastvideo behind catblowharderslowvideo
show catblowharderfastvideo behind catblowharderpovfastvideo
show catblowharderfastvideo behind catblowfastvideo
show catblowharderfastvideo behind catblowdeeperfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowharderslowvideo
hide catblowharderpovfastvideo
hide catblowfastvideo
hide catblowdeeperfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
show harder:
    xpos 1700 ypos 700    
call screen catblowharderfast()
screen catblowharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatBlowFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowDeeperFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVFast")

label CatBlowHarderPOVSlow:
$ catdeeper = False
$ catblowfaster = False
if catharder == False:
    mc "Time to take it up a notch. Get more of my monster meat down your throat!"
    $ catharder = True        
window hide
show catblowharderpovslowvideo behind catblowharderslowvideo
show catblowharderpovslowvideo behind catblowharderpovfastvideo
show catblowharderpovslowvideo behind catblowpovslowvideo
show catblowharderpovslowvideo behind catblowdeeperpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowharderslowvideo
hide catblowharderpovfastvideo
hide catblowpovslowvideo
hide catblowdeeperpovslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
show harder:
    xpos 1700 ypos 700    
call screen catblowharderpovslow()
screen catblowharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatBlowPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowDeeperPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowHarderSlow")

label CatBlowHarderPOVFast:
$ catdeeper = False
$ catblowfaster = False
if catharder == False:
    mc "Time to take it up a notch. Get more of my monster meat down your throat!"
    $ catharder = True        
window hide
show catblowharderpovfastvideo behind catblowharderpovslowvideo
show catblowharderpovfastvideo behind catblowharderfastvideo
show catblowharderpovfastvideo behind catblowpovfastvideo
show catblowharderpovfastvideo behind catblowdeeperpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowharderpovslowvideo
hide catblowharderfastvideo
hide catblowpovfastvideo
hide catblowdeeperpovfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show harder:
    xpos 1700 ypos 700    
show sceneicon:
     xpos 50 ypos 500     
call screen catblowharderpovfast()
screen catblowharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatBlowPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowHarderFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowDeeperPOVFast")

label CatBlowDeeperSlow:
if catdeeper == False:
    mc "Come on, you can do better than this, really open your throat this time!"
    $ catdeeper = True        
window hide
show catblowdeeperslowvideo behind catblowdeeperfastvideo
show catblowdeeperslowvideo behind catblowdeeperpovslowvideo
show catblowdeeperslowvideo behind catblowharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowdeeperfastvideo
hide catblowdeeperpovslowvideo
hide catblowharderslowvideo
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
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen catblowdeeperslow()
screen catblowdeeperslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowDeeperFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowDeeperPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatBlowEnd")

label CatBlowDeeperFast:
if catdeeper == False:
    mc "Come on, you can do better than this, really open your throat this time!"
    $ catdeeper = True 
window hide
show catblowdeeperfastvideo behind catblowdeeperslowvideo
show catblowdeeperfastvideo behind catblowdeeperpovfastvideo
show catblowdeeperfastvideo behind catblowharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowdeeperslowvideo
hide catblowdeeperpovfastvideo
hide catblowharderfastvideo
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
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen catblowdeeperfast()
screen catblowdeeperfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowDeeperSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowDeeperPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatBlowEnd")

label CatBlowDeeperPOVSlow:
if catdeeper == False:
    mc "Come on, you can do better than this, really open your throat this time!"
    $ catdeeper = True 
window hide
show catblowdeeperpovslowvideo behind catblowdeeperslowvideo
show catblowdeeperpovslowvideo behind catblowdeeperpovfastvideo
show catblowdeeperpovslowvideo behind catblowharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide catblowdeeperslowvideo
hide catblowdeeperpovfastvideo
hide catblowharderpovslowvideo
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
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen catblowdeeperpovslow()
screen catblowdeeperpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowDeeperPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowDeeperSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatBlowEnd")

label CatBlowDeeperPOVFast:
if catdeeper == False:
    mc "Come on, you can do better than this, really open your throat this time!"
    $ catdeeper = True 
window hide
show catblowdeeperpovfastvideo behind catblowdeeperpovslowvideo
show catblowdeeperpovfastvideo behind catblowdeeperfastvideo
show catblowdeeperpovfastvideo behind catblowharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow02.mp3"
hide catblowdeeperpovslowvideo
hide catblowdeeperfastvideo
hide catblowharderpovfastvideo
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
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen catblowdeeperpovfast()
screen catblowdeeperpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatBlowDeeperPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatBlowHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatBlowDeeperFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatBlowEnd")

label CatBlowEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
mc "Oh fuck, you're blowing me so good.... I'm gonna..."
scene catblowcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play sound "sounds/slurp.mp3"
mc "....CUM!"
window hide 
with hpunch
cw "Mmmmgggg..."
scene catblowcum02 with dissolve
mc "Take that [age]-yo spunk DEEPER down your throat, RHAAA!"
window hide 
with fastflash
mc "Oh my God, that TONGUE of yours!"
scene catblowcum03 with dissolve
play sound "sounds/slurp.mp3"
mc "This is sssooo GOOD, AAAH!"
window hide
with fastflash
mc "Damn it, your mouth is like a vacuum cleaner!"
scene catblowcum04 with dissolve
play sound "sounds/splooge02.mp3"
mc "AAAH! You're taking me EVEN DEEPER???"
window hide
with hpunch
mc "While I'm still NUTTING, RHAAA!"
scene catblowcum05 with dissolve
play sound "sounds/slurp.mp3"
mc "UUUH!!!... You're sucking the cum out of my spunk-factories!!!"
window hide
with fastflash
play sound "sounds/lick01.ogg"
mc "I need to... I can't..."
scene catblowcum06 with dissolve
mc "RHAAA! Let me fill up your hungry mouth!"
window hide
with vpunch
cw "Gimme, gimme, give to the little kitty!"
scene catblowcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "FUCK ME! That was..."
play sound "sounds/lick02.mp3"
cw "Did I do good?"
mc "Oooh yeah, you did REAL good... Now get cleaned up, you made me SUPER-HORNY!"
$ fuckedcatwoman = True
jump CatwomanSexDialogues

label CatWomanPussySex: 
if fuckedcatwoman == False:
    scene catwomanpre01 with dissolve
    cw "That's the pussy you want to fuck?"
    mc "Yep, right there."
    scene catwomanpre02 with dissolve    
    play sound "v05/purring.mp3"
    cw "Then maybe I should make it wet for your giant hog..."
    mc "It would be advisable indeed."
scene catwomanpre03 with dissolve 
play sound "v05/meow.mp3"
cw "I'm ready tiger! Give me your hot MEAT!"
scene catwomanprepussy01 with dissolve    
mc "Then open up real wide for this [age]-yo PUSSY-WRECKER!"
cw "Oh my God, it's so BIG!"
scene catwomanprepussy02 with dissolve    
play sound "sounds/moan06.ogg"
mc "It went in nice and easy, your snatch is like butter!"
cw "I hate water but my pussy loves to be wet! FUCK ME TIGER!"

label CatWomanPussySlow:
hide cum
hide faster
hide slower
hide softer
hide harder
show catwomanpussyslowvideo behind catwomanpussyfastvideo
show catwomanpussyslowvideo behind catwomanpussyharderslowvideo
$ renpy.pause(1.0, hard=True)
hide catwomanpussyfastvideo with dissolve
hide catwomanpussyharderslowvideo
play channel1 "sounds/womansex03.mp3"
$ catpussyfast = False
if catpussyslow == False:
    $ catpussyslow = True
    mc "Who's pussy is it, hey? Who's pussy is it?"
    cw "Meow! It's YOUR pussy, tiger!"
show faster:
     xpos 1700 ypos 500
show harder:
     xpos 50 ypos 500
call screen catwomanpussyslow()
screen catwomanpussyslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(110, 60)        
        action Jump ("CatWomanPussyFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatWomanPussyHarderSlow")

label CatWomanPussyFast:
hide cum
hide faster
hide slower
hide softer
hide harder
$ catpussyslow = False
if catpussyfast == False:
    $ catpussyfast = True
    cw "Give it to me, faster, FASTER!"
show catwomanpussyfastvideo behind catwomanpussyslowvideo
show catwomanpussyfastvideo behind catwomanpussyharderfastvideo
$ renpy.pause(1.0, hard=True)
play channel1 "sounds/womansex04.mp3"
hide catwomanpussyslowvideo with dissolve
hide catwomanpussyharderfastvideo with dissolve
show slower:
     xpos 50 ypos 500
show harder:
     xpos 1700 ypos 500
call screen catwomanpussyfast()
screen catwomanpussyfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("CatWomanPussySlow")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("CatWomanPussyHarderFast")

label CatWomanPussyHarderSlow:
hide cum
hide faster
hide slower
hide softer
hide harder
if catpussyhard == False:
    $ catpussyhard = True
    cw "My pussy has been very naughty, you need to pound it HARDER!"
show catwomanpussyharderslowvideo behind catwomanpussyslowvideo
show catwomanpussyharderslowvideo behind catwomanpussyharderfastvideo
$ renpy.pause(1.0, hard=True)
hide catwomanpussyslowvideo with dissolve
hide catwomanpussyharderfastvideo
play channel1 "sounds/womansex03.mp3"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500
show softer:
     xpos 50 ypos 500
call screen catwomanpussyharderslow()
screen catwomanpussyharderslow():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("CatWomanPussySlow")
    button:
        xpos 1700
        ypos 500
        xysize(110, 60)        
        action Jump ("CatWomanPussyHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatWomanPussyEnd")

label CatWomanPussyHarderFast:
hide cum
hide faster
hide slower
hide softer
hide harder
if catpussyhard == False:
    $ catpussyhard = True
    cw "My pussy has been very naughty, you need to pound it HARDER!"
show catwomanpussyharderfastvideo behind catwomanpussyfastvideo
show catwomanpussyharderfastvideo behind catwomanpussyharderslowvideo
$ renpy.pause(1.0, hard=True)
play channel1 "sounds/womansex04.mp3"
hide catwomanpussyfastvideo with dissolve
hide catwomanpussyharderslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020   
show slower:
     xpos 50 ypos 500
show softer:
     xpos 1700 ypos 500
call screen catwomanpussyharderfast()
screen catwomanpussyharderfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("CatWomanPussyHarderSlow")
    button:
        xpos 1700
        ypos 500
        xysize(110, 60)        
        action Jump ("CatWomanPussyFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatWomanPussyEnd")
        
label CatWomanPussyEnd:
hide cum
hide slower
hide faster
hide softer
hide harder
cw "Are you ready to give this pussy some cream? I LOVE milky semen!"
mc "I am... I am..."
scene catfuckpussycum01 with dissolve    
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "NOW! RHAAA!"
window hide
with fastflash
play sound "v05/meow.mp3"
cw "Meow! You're making this pussy very happy!"
scene catfuckpussycum02 with dissolve    
mc "That pussy is so damn tight and warm, I can't stop nutting my cream!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
cw "Keep going, I can hold it, I WANT IT ALL!"
scene catfuckpussycum03 with dissolve    
mc "It's overflowing but I don't care, AAAH!"
window hide
with hpunch
play sound "sounds/moan04.ogg"
cw "AAAAH, it's so good, it's so MUCH!"
scene catfuckpussycum04 with dissolve 
mc "Need to mark my territory on your bed now, RHAAA!"
window hide
with fastflash
if age >= 20:
    cw "Look at those jets of young spunk flying everywhere!"
if age >= 18 and age <= 19:
    cw "Look at those jets of young tenage spunk flying everywhere!"
scene catfuckpussycum05 with dissolve    
stop channel1
play sound "sounds/panting.mp3"
mc "Phew, I think I did a right mess on your bed... and in your fuckhole."
play sound "v05/meow.mp3"
cw "There's a HUGE puddle of milky semen right in front of me. I NEED to slurp it up!"
scene catfuckpussycum06 with dissolve    
play sound "sounds/lick01.ogg"
mc "Be my guest. Lick it all up, it's your reward."
play sound "v05/purring.mp3"
cw "I would call you Master but a cat only has servants. Let me finish cleaning myself up and I'll be ready for some MORE."
$ fuckedcatwoman = True
jump CatwomanSexDialogues

label CatWomanAnalSex:
if fuckedcatwoman == False:
    scene catwomanpre01 with dissolve
    cw "That's the little hole you want to fuck down there?"
    mc "Yep, right there."
    scene catwomanpre02 with dissolve    
    play sound "v05/purring.mp3"
    cw "I don't know if your huge LOG will fit in my small backdoor..."
    mc "We can only know by trying."
scene catwomanpreanal01 with dissolve 
play sound "v05/meow.mp3"
if age >= 20:
    cw "Alright then, I'm ready tiger! Stick that fucking monster pole in my ass!"
if age >= 18 and age <= 19:
    cw "Alright then, I'm ready tiger! Stick that fucking teenage monster pole in my ass!"
scene catwomanpreanal02 with dissolve    
mc "You ask for it and [hero] will deliver!"
cw "But try and be caref..."
scene catwomanpreanal03 with dissolve    
play sound "sounds/moan04.ogg"
cw "...FUL! AAAH!"
mc "I'll go easy on you. AT FIRST."

label CatwomanAnalShortFuckSlow:
$ catanalharder = False
$ catanalfaster = False
if catanalslower == False:
    $ catanalslower = True
    cw "I've never taken something this BIG up my ass before... It's sssooo BIG!"
window hide
show catanalshortslowvideo behind catanalshortfastvideo
show catanalshortslowvideo behind catanalshortpovslowvideo
show catanalshortslowvideo behind catanalslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide catanalshortfastvideo
hide catanalshortpovslowvideo
hide catanalslowvideo
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
call screen catanalshortslow()
screen catanalshortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalShortFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckPOVSlow")

label CatwomanAnalShortFuckFast:
$ catanalharder = False
$ catanalslower = False
if catanalfaster == False:
    $ catanalfaster = True
    cw "Go on, you can move those hips faster now!"
window hide
show catanalshortfastvideo behind catanalshortslowvideo
show catanalshortfastvideo behind catanalshortpovfastvideo
show catanalshortfastvideo behind catanalfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide catanalshortslowvideo
hide catanalshortpovfastvideo
hide catanalfastvideo
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
call screen catanalshortfast()
screen catanalshortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalShortFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckPOVFast")

label CatwomanAnalShortFuckPOVSlow:
$ catanalharder = False
$ catanalfaster = False
if catanalslower == False:
    $ catanalslower = True
    cw "I've never taken something this BIG up my ass before... It's sssooo BIG!"
window hide
show catanalshortpovslowvideo behind catanalshortslowvideo
show catanalshortpovslowvideo behind catanalshortpovfastvideo
show catanalshortpovslowvideo behind catanalpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide catanalshortslowvideo
hide catanalshortpovfastvideo
hide catanalpovslowvideo
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
call screen catanalshortpovslow()
screen catanalshortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalShortFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckSlow")

label CatwomanAnalShortFuckPOVFast:
$ catanalharder = False
$ catanalharder = False
$ catanalslower = False
if catanalfaster == False:
    $ catanalfaster = True
    cw "Go on, you can move those hips faster now!"
window hide
show catanalshortpovfastvideo behind catanalshortpovslowvideo
show catanalshortpovfastvideo behind catanalshortfastvideo
show catanalshortpovfastvideo behind catanalpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide catanalshortpovslowvideo
hide catanalshortfastvideo
hide catanalpovfastvideo
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
call screen catanalshortpovfast()
screen catanalshortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalShortFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckFast")

label CatwomanAnalFuckSlow:
if catanalharder == False:
    if age >= 20:
        cw "My ass is getting so STRETCHED out by your ENORMOUS DONG!"
    if age >= 18 and age <= 19:
        cw "My ass is getting so STRETCHED out by your ENORMOUS TEEN DONG!"
    mc "Then it's time to DESTROY IT!"
    cw "What? You're gonna POUND ME EVEN HARDER???!"
    mc "Damn right I am, here we go!!!"
    $ catanalharder = True        
window hide
show catanalslowvideo behind catanalfastvideo
show catanalslowvideo behind catanalpovslowvideo
show catanalslowvideo behind catanalshortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide catanalfastvideo
hide catanalpovslowvideo
hide catanalshortslowvideo
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
call screen catanalslow()
screen catanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalFuckFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatwomanAnalCumEnd")

label CatwomanAnalFuckFast:
if catanalharder == False:
    if age >= 20:
        cw "My ass is getting so STRETCHED out by your ENORMOUS DONG!"
    if age >= 18 and age <= 19:
        cw "My ass is getting so STRETCHED out by your ENORMOUS TEEN DONG!"
    mc "Then it's time to DESTROY IT!"
    cw "What? You're gonna POUND ME EVEN HARDER???!"
    mc "Damn right I am, here we go!!!"
    $ catanalharder = True        
window hide
show catanalfastvideo behind catanalslowvideo
show catanalfastvideo behind catanalpovfastvideo
show catanalfastvideo behind catanalshortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide catanalslowvideo
hide catanalpovfastvideo
hide catanalshortfastvideo
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
call screen catanalfast()
screen catanalfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalFuckSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatwomanAnalCumEnd")

label CatwomanAnalFuckPOVSlow:
if catanalharder == False:
    if age >= 20:
        cw "My ass is getting so STRETCHED out by your ENORMOUS DONG!"
    if age >= 18 and age <= 19:
        cw "My ass is getting so STRETCHED out by your ENORMOUS TEEN DONG!"
    mc "Then it's time to DESTROY IT!"
    cw "What? You're gonna POUND ME EVEN HARDER???!"
    mc "Damn right I am, here we go!!!"
    $ catanalharder = True        
window hide
show catanalpovslowvideo behind catanalslowvideo
show catanalpovslowvideo behind catanalpovfastvideo
show catanalpovslowvideo behind catanalshortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide catanalslowvideo
hide catanalpovfastvideo
hide catanalshortpovslowvideo
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
call screen catanalpovslow()
screen catanalpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalFuckPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatwomanAnalCumEnd")

label CatwomanAnalFuckPOVFast:
if catanalharder == False:
    if age >= 20:
        cw "My ass is getting so STRETCHED out by your ENORMOUS DONG!"
    if age >= 18 and age <= 19:
        cw "My ass is getting so STRETCHED out by your ENORMOUS TEEN DONG!"
    mc "Then it's time to DESTROY IT!"
    cw "What? You're gonna POUND ME EVEN HARDER???!"
    mc "Damn right I am, here we go!!!"
    $ catanalharder = True        
window hide
show catanalpovfastvideo behind catanalpovslowvideo
show catanalpovfastvideo behind catanalfastvideo
show catanalpovfastvideo behind catanalshortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide catanalpovslowvideo
hide catanalfastvideo
hide catanalshortpovfastvideo
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
call screen catanalpovfast()
screen catanalpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatwomanAnalFuckPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("CatwomanAnalShortFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CatwomanAnalFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatwomanAnalCumEnd")

label CatwomanAnalCumEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
cw "You've totally ruined by poor little backdoor! Now FLOOD IT with your cum, you HORSE-HUNG TIGER!"
mc "I'm going to, I'm going t..."
scene catanalcum01 with dissolve    
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play sound "sounds/splooge02.mp3"
mc "..TO COME, GODAMN RHAAA!"
window hide
with hpunch
cw "Meow! You're PUMPING my rosebud full of young spunk!"
scene catanalcum02 with dissolve    
play sound "sounds/splooge01.mp3"
if age >= 20:
    cw "AAAH, you're so BRUTAL when you dump your MASSIVE LOAD!"
if age >= 18 and age <= 19:
    cw "AAAH, you're so BRUTAL when you dump your MASSIVE TEENAGE LOAD!"
window hide
with hpunch
mc "That's cos I NEEEEDDD TO BURST!"
scene catanalcum03 with dissolve    
play sound "sounds/splooge02.mp3"
mc "FILLING YOUR PUSSY-ASS WITH CUM!"
window hide
with fastflash
cw "I'm so FULL already, AAAH I'm cumming too!"
scene catanalcum04 with dissolve    
play sound "sounds/boymoan05.mp3"
mc "I've got MOAR for YOU!"
window hide
with fastflash
mc "Gonna COVER you in my seed and MARK my territory, RHAAA!"
scene catanalcum05 with dissolve    
play sound "v05/meow.mp3"
cw "You're such a NAUGHTY tiger! My ass BELONGS to you now, you've stretched it out so MUCH!"
window hide
with hpunch
cw "You're STILL spewing those fat nut ropes! Oh my GOD, you're a SPUNK-MACHINE!"
window hide
with fastflash
mc "STILL... AAAH! A FEW MORE..."
scene catanalcum06 with dissolve    
stop channel1
play sound "sounds/panting.mp3"
mc "Damn it, that was a breeding worthy of the Discovery Channel."
play sound "v05/purring.mp3"
cw "I need to clean myself of all this cum. You CAKED me in it... Mmmh..."
$ fuckedcatwoman = True
jump CatwomanSexDialogues

label Mission06Stallion:
stop music
play music "sounds/covertmusic.mp3"
scene heist01 with fade
mc "Oh good, they seem to be all asleep after a heavy fuck session with the Stallion's cock..."
scene heist02 with dissolve
mc "Let's quietly move past them and look around for that safe..."
cw "That cock... It's coated with GOLD!"
mc "Yeah, and when we steal his gold, his cock will become useless."
cw "But it looks so yummy like that. I mean, it's coated with GOLD!"
mc "Yeah, err, okay, let's move on."
scene heist03 with dissolve
mc "Ah, there's the safe. You have the code, open it while I stand watch over them in case they wake up."
scene heist04 with dissolve
cw "That should be easy and quick."
play sound "v05/safelock.mp3"
cw "Uh oh..."
mc "What?"
scene heist05 with dissolve
if mission06day >= 4:
    cw "The code you gave me doesn't work! There's no way I can open this safe without it!"
    mc "Ah, shit, that might be because I piss-farted around for too many days and the Stallion changed the code. My bad, ABORT, ABORT!"
    jump EndMission06Fail
cw "The code only unlocked the FIRST safety level! This safe is more secure than I thought. I can do the rest, I'm just going to need more time."
mc "Time is something we don't have. Hurry up, Catwoman!"
scene heist06 with dissolve
play sound "sounds/yawn.mp3"
mc "Not good, one of them just woke up! Hurry up!"
scene heist07 with dissolve
cw "You need to buy me more time, I can't work under such pressure! That's why I like to work ALONE!"
mc "Alright, I'll..."
scene heist08 with dissolve
play sound "sounds/gasp.mp3"
mc "...grab her and make sure she doesn't make a sound!"
scene heist09 with dissolve
play sound "sounds/punch.mp3"
mc "Ouch! She's kicking me in the nuts! I HATE that!"
scene heist10 with dissolve
mc "That's it, if you won't stop this, I've got another way to SHUT YOU UP! I'm going to destroy your PUSSY into OBLIVION with my SUPERCOCK!"
cw "Do we really have time for your sexual shenanigans?"
mc "I'm a SEX Superhero, trust me, this is what I do BEST!"
scene heist11 with dissolve
mc "See this dong? You think the Stallion's cock is big but mine is SUPER-HARD I'll be plowing it into your pussy FIFTEEN INCHES DEEP!"
af "Mm-uuummmm-hhhmmmm..."
scene heist12 with dissolve
mc "You'd better stay real quiet if you don't want me to pound it EVEN DEEPER, you hear me? Cos I've got inches to spare!"
af "Fine, go ahead, I can take it! Samson Goldcock's dong is even bi..."
scene heist13 with dissolve
play sound "sounds/whoosh.mp3"
mc "Too much information! Too much information! This is almost NTR!"
af "* (...) *"
scene heist14 with dissolve
mc "Not so talkative anymore are we? Good, that means you're ready for a SUPERHERO POUNDING!"
play channel1 "sounds/wetmassage.mp3"

label AfricaShortFuckSlow:
$ africaharder = False
$ africafaster = False
window hide
show africashortslowvideo behind africashortfastvideo
show africashortslowvideo behind africashortfrontslowvideo
show africashortslowvideo behind africaslowvideo
pause 1.0
stop channel1
hide africashortfastvideo
hide africashortfrontslowvideo
hide africaslowvideo
if africaslower == False:
    $ africaslower = True
    mc "Do you feel how SUPER-HARD I am?"
    af "Y...yes... Ooh..."
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen africashortslow()
screen africashortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaShortFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("AfricaFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFrontSlow")

label AfricaShortFuckFast:
$ africaharder = False
$ africaslower = False
if africafaster == False:
    $ africafaster = True
    mc "Can the Stallion fuck you like that, hey? I bet he can't fuck you that FAST!"
window hide
show africashortfastvideo behind africashortslowvideo
show africashortfastvideo behind africashortfrontfastvideo
show africashortfastvideo behind africafastvideo
pause 1.0
play channel2 "sounds/moan02.mp3"
hide africashortslowvideo
hide africashortfrontfastvideo
hide africafastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen africashortfast()
screen africashortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaShortFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("AfricaFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFrontFast")

label AfricaShortFuckFrontSlow:
$ africaharder = False
$ africafaster = False
if africaslower == False:
    $ africaslower = True
    mc "Do you feel how SUPER-HARD I am?"
    af "Y...yes... Ooh..."
window hide
show africashortfrontslowvideo behind africashortslowvideo
show africashortfrontslowvideo behind africashortfrontfastvideo
show africashortfrontslowvideo behind africafrontslowvideo
pause 1.0
hide africashortslowvideo
hide africashortfrontfastvideo
hide africafrontslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen africashortfrontslow()
screen africashortfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaShortFuckFrontFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("AfricaFuckFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaShortFuckSlow")

label AfricaShortFuckFrontFast:
$ africaharder = False
$ africaharder = False
$ africaslower = False
if africafaster == False:
    $ africafaster = True
    mc "Can the Stallion fuck you like that, hey? I bet he can't fuck you that FAST!"
window hide
show africashortfrontfastvideo behind africashortfrontslowvideo
show africashortfrontfastvideo behind africashortfastvideo
show africashortfrontfastvideo behind africafrontfastvideo
pause 1.0
play channel2 "sounds/moan02.mp3"
hide africashortfrontslowvideo
hide africashortfastvideo
hide africafrontfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen africashortfrontfast()
screen africashortfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaShortFuckFrontSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("AfricaFuckFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFast")

label AfricaFuckSlow:
if africaharder == False:
    cw "Hurry up, and get it over with [hero]!"
    mc "Alright, I'll give her ALL EIGHTEEN INCHES THEN!"
    af "I can resist, I'll res..."
    $ africaharder = True        
window hide
show africaslowvideo behind africafastvideo
show africaslowvideo behind africafrontslowvideo
show africaslowvideo behind africashortslowvideo
pause 1.0
stop channel1
stop channel2
play channel2 "sounds/pounding.ogg"
hide africafastvideo
hide africafrontslowvideo
hide africashortslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen africaslow()
screen africaslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaFuckFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("AfricaShortFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AfricaFuckEnd")

label AfricaFuckFast:
if africaharder == False:
    cw "Hurry up, and get it over with [hero]!"
    mc "Alright, I'll give her ALL EIGHTEEN INCHES THEN!"
    af "I can resist, I'll res..."
    $ africaharder = True        
window hide
show africafastvideo behind africaslowvideo
show africafastvideo behind africafrontfastvideo
show africafastvideo behind africashortfastvideo
pause 1.0
stop channel1
stop channel2
play channel2 "sounds/pounding.ogg"
hide africaslowvideo
hide africafrontfastvideo
hide africashortfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen africafast()
screen africafast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaFuckSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AfricaFuckEnd")

label AfricaFuckFrontSlow:
if africaharder == False:
    cw "Hurry up, and get it over with [hero]!"
    mc "Alright, I'll give her ALL EIGHTEEN INCHES THEN!"
    af "I can resist, I'll res..."
    $ africaharder = True        
window hide
show africafrontslowvideo behind africaslowvideo
show africafrontslowvideo behind africafrontfastvideo
show africafrontslowvideo behind africashortfrontslowvideo
pause 1.0
stop channel1
stop channel2
play channel2 "sounds/pounding.ogg"
hide africaslowvideo
hide africafrontfastvideo
hide africashortfrontslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
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
call screen africafrontslow()
screen africafrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaFuckFrontFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AfricaFuckEnd")

label AfricaFuckFrontFast:
if africaharder == False:
    cw "Hurry up, and get it over with [hero]!"
    mc "Alright, I'll give her ALL EIGHTEEN INCHES THEN!"
    af "I can resist, I'll res..."
    $ africaharder = True        
window hide
show africafrontfastvideo behind africafrontslowvideo
show africafrontfastvideo behind africafastvideo
show africafrontfastvideo behind africashortfrontfastvideo
pause 1.0
stop channel1
stop channel2
play channel2 "sounds/pounding.ogg"
hide africafrontslowvideo
hide africafastvideo
hide africashortfrontfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
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
call screen africafrontfast()
screen africafrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AfricaFuckFrontSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("AfricaShortFuckFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AfricaFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AfricaFuckEnd")

label AfricaFuckEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide front
hide sceneicon
mc "You want some cum, don't you? Don't answer, I wouldn't want you to raise the alarm. But take..."
scene africacum01 with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
play sound "sounds/splooge03.mp3"
mc "..THIS!"
window hide 
with fastflash
af "Mmmmgggg..."
scene africacum02 with dissolve
play sound "sounds/splooge02.mp3"
mc "And THAT!"
window hide 
with hpunch
mc "I bet that's MORE cum that the Stallion ever gave you!"
scene africacum03 with dissolve
play sound "sounds/splat.ogg"
mc "I'll show you better how MASSIVE my cum ropes are!"
window hide 
with fastflash
cw "Your cumshots are making too much noise, try and keep it down, I need to concentrate!"
scene africacum04 with dissolve
mc "Oh, sorry, let me aim my spunk-cannon better then. At her TITS!"
window hide 
with fastflash
af "Noooo!!! I'm only allowed to taste Samson's seed!!!"
scene africacum05 with dissolve
mc "Too fucking late, I'm PLASTERING you in MY SUPER-VIRILE SPERM now!"
window hide 
with fastflash
mc "His gunk will DISINTEGRATE under MY layers of cum!"
scene africacum06 with dissolve
play sound "sounds/splooge02.mp3"
mc "And here's some more inside your snatch for good measure!"
window hide 
with hpunch
cw "How can I work when you're dumping your load right besides me? I mean, really!"
scene africacum07 with dissolve
play sound "sounds/splooge01.mp3"
mc "Almost done, Catwoman, here's the last of it to knock her CUM-UNCONSCIOUS!"
window hide 
with hpunch
mc "Godammit, nutting so much!!!! But she's fainting now..."
scene africacum08 with dissolve
stop channel2
stop sound
mc "That's it. Another villainous henchwoman neutralized... With my SUPER-DONG and MONSTER CUMLOADS!"
cw "Can I finally have some piece and quiet to finish opening this safe then?"
scene africacum09 with dissolve
mc "Sure, let me lay her down on the floor and I'll go back to my sentinel post."
cw "You've probably woken up the entire neighborhood!"
mc "Hey, I was being as quiet as a non-stop cumming SEX Super-Hero can get!"
scene heist15 with dissolve
mc "Having said that, it appears you were half-right. The other chick woke up..."
cw "Do what you have to do. IN SILENCE!"
scene heist16 with dissolve
mc "Where do you think you're going?"
ja "What the???..."
scene heist17 with dissolve
mc "Surprise! You're going to get the same treatment as your friend. But ANALLY!"
ja "Mmmmmuuuuuuhhhh!!!"
scene heist18 with dissolve
mc "That's right, shut up and take it like the cock-whore that you are!"
cw "That's a pretty rude thing to say to a girl, but I guess she deserves it. The slut."
scene heist19 with dissolve
mc "Let's see if you can take my monsterdick up your slutty backdoor, shall we?"
scene heist20 with dissolve
mc "Looks like it fits so far. But that's just the tip..."
scene heist21 with dissolve
play sound "sounds/moan02.mp3"
mc "Well, look at you, you seem to be enjoying getting butt-fucked by an arm-thick piece of boymeat..."
cw "What a total slut. Do shut her up for good will you?"
mc "I will, don't worry Catwoman!"

label JasmineAssFuckSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show jasmineassfuckslowvideo behind jasmineassfuckfastvideo
show jasmineassfuckslowvideo behind jasmineassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide jasmineassfuckfastvideo
hide jasmineassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex06.mp3"
$ jasmineassfuckfast = False
if jasmineassfuckslow == False:
    if age >= 20:
        mc "Much better than you thought, isn't it? That's what a SUPERCOCK does!"
    if age >= 18 and age <= 19:
        mc "Much better than you thought, isn't it? That's what a TEEN SUPERCOCK does!"
    $ jasmineassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen jasmineassfuckslow()
screen jasmineassfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("JasmineAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("JasmineAssFuckFrontSlow")

label JasmineAssFuckFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show jasmineassfuckfastvideo behind jasmineassfuckslowvideo
show jasmineassfuckfastvideo behind jasmineassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide jasmineassfuckslowvideo
hide jasmineassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex03.mp3"
$ jasmineassfuckslow = False
if jasmineassfuckfast == False:
    cw "I STILL need to CONCENTRATE you know!"
    mc "Alright, alright! I'll fuck her till she passes out from my mighty pillar of anal lust!"
    $ jasmineassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen jasmineassfuckfast()
screen jasmineassfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("JasmineAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("JasmineAssFuckFrontFast")

label JasmineAssFuckFrontSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show jasmineassfuckfrontslowvideo behind jasmineassfuckslowvideo
show jasmineassfuckfrontslowvideo behind jasmineassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide jasmineassfuckslowvideo
hide jasmineassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex06.mp3"
$ jasmineassfuckfast = False
if jasmineassfuckslow == False:
    if age >= 20:
        mc "Much better than you thought, isn't it? That's what a SUPERCOCK does!"
    if age >= 18 and age <= 19:
        mc "Much better than you thought, isn't it? That's what a TEEN SUPERCOCK does!"
    $ jasmineassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen jasmineassfuckfrontslow()
screen jasmineassfuckfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("JasmineAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckSlow")

label JasmineAssFuckFrontFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show jasmineassfuckfrontfastvideo behind jasmineassfuckfastvideo
show jasmineassfuckfrontfastvideo behind jasmineassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide jasmineassfuckfastvideo
hide jasmineassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex03.mp3"
$ jasmineassfuckslow = False
if jasmineassfuckfast == False:
    cw "I STILL need to CONCENTRATE you know!"
    mc "Alright, alright! I'll fuck her till she passes out from my mighty pillar of anal lust!"
    $ jasmineassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen jasmineassfuckfrontfast()
screen jasmineassfuckfrontfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("JasmineAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("JasmineAssFuckFast")

label JasmineAssFuckEnd:
hide cum
hide assview
hide faster
hide slower
hide front
mc "You're going to submit and pass out?"
ja "Fuck you...ggg...muthafucka!"
scene jasminecum01 with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
play sound "sounds/splooge03.mp3"
mc "THIS should shut you up!"
window hide 
with fastflash
ja "Ain't nothing to...aaah...me!"
scene jasminecum02 with dissolve
play sound "sounds/splooge02.mp3"
mc "And DEEPER?"
window hide 
with hpunch
ja "I..."
scene jasminecum03 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
mc "That's right, don't talk and get creamed up with my cum enema!"
window hide 
with fastflash
cw "You're again making too much filthy squishy noise with your disgorging rod, just get it over with!"
scene jasminecum04 with dissolve
play sound "sounds/splat.ogg"
mc "But my cumloads are so STRONG and last so LONG, I can't stop now, need to NUU-UUUU-TTT!"
window hide 
with fastflash
mc "She's getting the message, a few more..."
scene jasminecum05 with dissolve
play sound "sounds/splooge02.mp3"
mc "...SHOTS IN HER ASS!!!"
window hide 
with fastflash
play sound "sounds/boymoan03.mp3"
mc "I'm almost done, but here's some MORE!"
scene jasminecum06 with dissolve
stop channel2
stop sound
play sound "sounds/panting.mp3"
mc "At last, she's passed out, just in time, as I was running out of nutsauce."
cw "So I can finally work without you disturbing me now?"
scene jasminecum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1 
with dissolve
stop sound
mc "Yeah, the coast is clear. For now."
scene heist22 with dissolve
play sound "v05/safelock.mp3"
cw "I've finally managed to open the safe!"
scene heist23 with dissolve
play sound "sounds/winning.mp3"
show missionicon06 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
show textmission06 at posmissiontext
$ mission06win = True
$ mission06end = True
cw "So much GOLD! There must  at least a TON of it! How will we carry it?"
mc "No worries, a ton is NOTHING to a SUPER-STRONG hero like me!"
cw "Good, bring it to my lair, it's safest there..."
mc "Err, I suppose so, let's just get out as fast as possible in any case."
scene heist24 with dissolve
cw "There's some gold we forgot..."
mc "What do you mean?"
scene heist25 with dissolve
cw "On his cock. His big dangling cock. I could lick it off without waking him up, he seems to be a very DEEP sleeper."
menu:
    "Fine, but be quick about it! (watch scene)":
        jump CatwomanDongLick
    "Eew, that's gross, and totally NTRish! (don't watch scene)":
        cw "I suppose you're right. We can't alienate all the pathetically-squeamish anti-NTR brigade players out there."
        jump CatwomanMissionEnd

label CatwomanDongLick:
scene heist26 with dissolve
play sound "sounds/lick01.ogg"
cw "I'll just start by licking the tip..."
mc "There's no gold on the tip, you're just wasting time."
scene heist27 with dissolve
play sound "sounds/lick03.mp3"
cw "Oooh, it looks like he likes it..."
mc "Okay, so he can get hard. Big deal. I can get SUPER-HARD!"
scene heist28 with dissolve
play sound "sounds/lick02.mp3"
cw "He's so MASSIVE. Definitely the BIGGEST cock in town already and he's still growing!"
mc "I'm still growing too, I'll beat him one day, you'll see!"
scene heist29 with dissolve
play sound "sounds/slurp.mp3"
mc "You're supposed to LICK THE GOLD off it, remember? Not STUFF IT down your throat like you're starving for it!"
scene heist30 with dissolve
play sound "sounds/lick01.ogg"
mc "Ah, I see, you have an elasti-tongue. I didn't know that."
scene heist31 with dissolve
play sound "sounds/lick03.mp3"
mc "I must admit, it is quite an efficient way of licking the gold off his cock."
scene heist32 with dissolve
play sound "sounds/slurp.mp3"
mc "You'll have to do that to me one day, I want to know how it feels to have that tongue wrapped around my hard shaft..."
scene heist33 with dissolve
play sound "sounds/blow01.mp3"
mc "Come on, if you're going to blow him, blow him PROPERLY! And FINISH THE JOB!"
cw "Mmggg...."
scene heist34 with dissolve
play sound "sounds/blow02.mp3"
mc "There you go, you gold-licker... Dig in there."
scene heist35 with dissolve
play sound "sounds/lick03.mp3"
mc "Don't forget the balls..."
scene heist36 with dissolve
play sound "sounds/moan02.mp3"
mc "Good cleaning, Catwoman, you got it all!"
cw "And I made him ROCK-HARD too!"
scene heist37 with dissolve
cw "Wh...What's happening???"
mc "He can't keep it up, that's what's happening! Unlike me and my SUPER-C..."
scene heist38 with dissolve
cw "No!!! This is not what I wanted! He's becoming TINY!"
mc "You stole his gold, you stole his mojo... It was to be expected."
scene heist39 with dissolve
mc "Will you look at this tiny stub, HA HA! I can't stop quietly laughing! I'm embarrassed for him to be honest."
cw "Stop it, you're just being mean!"
mc "Let's get out of here before he wakes up and realizes his todger has become a useless limp noodle..."

label CatwomanMissionEnd:
stop music
play music "sounds/relax.mp3"
scene catwomanlair01
show catwomaneyeblink
with fade
mc "Where should I put the gold?"
cw "In MY safe over there in the corner."
mc "Ok, done. Now how do I get my half of it? The safe locked itself automatically."
hide catwomaneyeblink
show catwoman02 at centerleft
with dissolve
cw "Your half of what?"
mc "My half of the GOLD!"
hide catwoman02
show catwoman04 at centerleft
with dissolve
cw "I don't know anything about gold. Are you suggesting you participated in an illegal gold heist and that I was your accomplice?"
mc "Err, yes."
hide catwoman04
show catwomaneyeblink
with dissolve
cw "I will deny everything and throw YOU under the bus!"
mc "Hey!, You're STEALING my HALF of the GOLD!"
hide catwomaneyeblink
show catwoman03 at centerleft
with dissolve
cw "What gold?"
mc "* sigh * I've been had. Since there isn't any money in this game anyway, I don't care at this point, I'm not fighting with you Catwoman..."
hide catwoman03
show catwoman04 at centerleft
with dissolve
cw "That's a good boy. Now, if you'll excuse me, I have some accounting business to do..."
window hide
hide catwoman04 with moveoutleft
mc "* sigh *"
jump Main

label EndMission06Fail:
stop music
scene catwomanlair01 with fade
show catwoman04 at centerleft
cw "Because of your abject failure, I don't have any gold!"
if mission06good:
    mc "And I haven't even told Captain sawyer about it yet. She's going to be MAD..."
if mission06evil:
    mc "And I haven't even told Emma Frost about it yet. She's going to be MAD..."
hide catwoman04
show catwoman02 at centerleft
with dissolve
cw "Get out of my cat cave, you're USELESS!"
jump Main