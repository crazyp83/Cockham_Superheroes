label CompoundPoolDay:
stop music
play music "sounds/waterrun.mp3"
$ seenpool = True

if d10locday in [3, 4]:
    jump PoolDayMILF
elif d10locday in [5, 6]:
    jump PoolDayWidow
elif all([d10locday in [7, 8], mclevel02]):
    jump PoolPowerLevel02

label PoolEmpty:
if mclevel02 == False:
    scene poolmc01 with fade
if mclevel02:
    scene poolmclevel02a with fade
mc "Ah, it's empty. So I have the whole place to myself then. Let's go for a swim, since I'm here. At the pool. During the day."
if poolmcspeak01 == False:
    mc "Good thing I was provided with an XXXL-sized speedo..."
    $ poolmcspeak01 = True
stop music
play music "sounds/swim.mp3"
if mclevel02 == False:
    scene poolmc02 with dissolve
if mclevel02:
    scene poolmclevel02b with dissolve
mc "* And the Super-hero breaks the world record and the crowd goes wild... *"
if mclevel02 == False:
    scene poolmc03 with dissolve
if mclevel02:
    scene poolmclevel02c with dissolve
mc "Let's swim a bit more... And clearly display my massive bulge in case anyone walks in..."
if mclevel02 == False:
    scene poolmc04 with dissolve
if mclevel02:
    scene poolmclevel02d with dissolve
stop music
mc "Oh well, no one came... I'm guesssing this scene is a place holder at this stage and will repeat indefinitely every time I come here during the day when the pool is empty..."
jump Main

label PoolPowerLevel02:
if period == 0:
    scene compoundpooldaybackground
    show powerpoolnew01
    with fade
if period == 1:
    scene poolbackground
    show powerpoolnew01
    with fade
mc "Oooh, Kara is here. As predicted by the compound roster."
if powerpoolseenbikini == False:
    mc "* And she has a new HOT bikini... *"
    $ powerpoolseenbikini = True
hide powerpoolnew01
show powerpoolnew02
with fastdissolve
pg "I Super-Sensed you behind my back, [name]..."
hide powerpoolnew02
show powerpooleyeblink
with dissolve
mc "Ah, yeah, you're good at that."
pg "I'm the GOAT at that."
label PowerPoolNewDialogues:
menu:
    "I was just going for a swim. You know, to maintain my ROCK-HARD muscles." if unlockedpowergirl == False:
        hide powerpooleyeblink
        show powerpoolnew04 at centerleft
        with fastdissolve        
        pg "Is that so? Then I'll watch you and train with my ultra-heavy dumbbells. Let's see who has the most SOLID muscles after that!"
        jump PowerGirlPoolNewMuscle    
    "That's a HOT bikini you got there, Kara...":
        hide powerpooleyeblink
        show powerpoolnew04 at centerleft
        with fastdissolve        
        pg "You like it? Maybe you deserve a closer look then..."
        jump PowerGirlPoolNewJerk
    "When are we finally going to have SEX?" if helpedwidow and unlockedpowergirl == False:
        hide powerpooleyeblink
        show powerpoolnew05 at centerleft
        with fastdissolve
        pg "SEX with you? And that cunt-wrecking MONSTERCOCK? I don't think so. You're just TOO massive."
        mc "But it's not my fault I was born with such a giant dong!"
        hide powerpoolnew05
        show powerpoolnew04 at centerleft
        with fastdissolve
        pg "Maybe, but my pussy is not a highway for your enormous [age]yo ramrod..."
        hide powerpoolnew04
        show powerpooleyeblink
        with fastdissolve
        jump PowerPoolNewDialogues
    "That bod of yours in that sexy bikini is so HOT, it's giving me an instant BONER!":
        hide powerpooleyeblink
        show powerpoolnew05 at centerleft
        with fastdissolve
        pg "Yuck! You really have to work on your Super-Seduction skills, [name]! That's TOO direct!"
        mc "Ah, sorry, it was a menu option, so I tried it..."
        hide powerpoolnew05
        show powerpooleyeblink
        with fastdissolve
        jump PowerPoolNewDialogues

label PowerGirlPoolNewMuscle:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ unlockedpowergirl = True
scene poolmclevel02a with dissolve
pg "Well go on then, I'll get my set ready..."
mc "Err, okay."
scene poolmclevel02b with dissolve
play sound "sounds/swim.mp3"
pg "Keep going, do as many laps as you can while I pump MY muscles!"
play music "sounds/gymmusic.mp3"
scene powerpoolbellback blurred:
    zoom 1.9 xoffset -400 yoffset -900
show powerpoolbell01:
    xoffset 0 yoffset -1080
show powerpoolbellback blurred at poolbackgroundup
show powerpoolbell01 at poolbackgroundpowerup
with dissolve
$ renpy.pause(7.0, hard='True') 
pg "I'll show how to REALLY train your muscles!"
mc "They don't look so big. How much do they weigh?"
scene powerpoolbellanimback blurred:
    zoom 1.5 xoffset -500 yoffset -100
show powerbellanim01start:
    zoom 1.5 xoffset 100 yoffset -100
with dissolve
pg "Over a TON. EACH!"
mc "Ok, that's a lot then."
pg "First, some heavy wrist curls..."
scene powerpoolbellanimback blurred
show powerbellanim01:
    zoom 1 xoffset 450 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanim01 at powerbellanim
with dissolve
$ renpy.pause(1.0, hard='True')
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbell01()
screen powerbell01():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellFast01")

label PowerBellFast01:
scene powerpoolbellanimback blurred
show powerbellanimfast01:
    zoom 1 xoffset 450 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanimfast01 at powerbellanim
with dissolve
$ renpy.pause(1.0, hard='True')
pg "And now, even FASTER!"
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbellfast01()
screen powerbellfast01():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellEnd01")

label PowerBellEnd01:
scene powerpoolbellback blurred:
    zoom 1.9 xoffset -400 yoffset -900
show powerbellanim02start:
    xoffset 0 yoffset -1080
show powerpoolbellback blurred at poolbackgroundup
show powerbellanim02start at poolbackgroundpowerup02
with dissolve
$ renpy.pause(7.0, hard='True') 
mc "Wow, your muscles have already GROWN some, Kara!"
pg "Gonna continue PUMPING then. Some Arnold press. Apparently some young Austrian bodybuilder came up with that recently."
window hide
scene powerpoolbellanimback blurred
show powerbellanim02:
    zoom 1 xoffset 350 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanim02 at powerbellanim2
with dissolve
$ renpy.pause(2.0, hard='True')
pg "It's a tough exercise, but Powergirl can DO IT!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbell02()
screen powerbell02():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellFast02")

label PowerBellFast02:
play sound "sounds/womangroan.mp3"
scene powerpoolbellanimback blurred
show powerbellanimfast02:
    zoom 1 xoffset 350 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanimfast02 at powerbellanim2
with dissolve
$ renpy.pause(1.0, hard='True')
pg "F...FASTER! I can do it, I have the POWER!"
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbellfast02()
screen powerbellfast02():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellEnd02")

label PowerBellEnd02:
stop music
play sound "sounds/panting.mp3"
scene powerpoolbellanimback blurred:
    zoom 1.2 xoffset -300 yoffset -100
show powerpoolpostbell01:
    zoom 1.2 xoffset 100 yoffset -100
with dissolve
pg "That was...INTENSE.... I..."
mc "Kara, what's happening, you're all flustered!"
hide powerpoolpostbell01
show powerpoolpostbell02
with fastdissolve
pg "Aaah...."
scene powerpoolpostbell03 with dissolve
mc "Damn, she fainted! She must have over-exhausted herself with those super-heavy dumbbells."
scene powerpoolpostbell04 with dissolve
mc "Say something, Kara! Wake up! Oh my God, I have to do something, her skin is SCALDING HOT and her pulse is weak!"
scene powerpoolpostbell05 with dissolve
mc "First, some CPR... Damn, it's not working! I can't do cock-to-pussy resuscitation like you all thought I would, because her pussy would BURN my cock!"
scene powerpoolpostbell06 with dissolve
mc "I'll have to carry her and throw her in the pool so her body temperature can cool down. Without burning myself..."
if mcresistance >= 1:
    call screen usepower("useresistance", "PowerPoolNoResistance", "PowerPoolResistance") with dissolve
label PowerPoolNoResistance:
scene powerpoolpostbell06b with dissolve
play sound "v05/burn.mp3"
mc "AAAAH! It's BURNING MY SKIN! Why didn't I choose Super-Resistance as a superpower! I'm gonna DIE now!"
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label PowerPoolResistance:
$ savedkarapool = True
scene powerpoolpostbell07 with dissolve
mc "Just in the nick of time, it was starting to HEAT UP a LOT!"
scene powerpoolpostbell08 with dissolve
mc "And now I'll jump in and make sure she doesn't drown!"
play sound "sounds/diving.mp3"
mc "I need to be quick!"
scene powerpoolpostbell09 with dissolve
play music "sounds/underwater.mp3"
mc "There she is, her skin doesn't look scalding HOT anymore, thanks God!"
scene powerpoolpostbell10 with dissolve
play music "sounds/waterrun.mp3"
mc "Let's get you out of the water now, your body temperature is back to normal..."
pg "What... What happened?..."
scene powerpoolpostbell11 with dissolve
pg "You were overheating. But I saved you... Kara..."
scene powerpoolpostbell12 with dissolve
play sound "sounds/kiss.mp3"
pg "You did? You saved ME? Let me kiss you..."
mc "Mmh, your tongue is still super-HOT!"
pg "It ALWAYS is... * wink *"
pg "I need to get back to my room and stick some ice inside my... girly bits."
mc "Right, right..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label PowerGirlPoolNewJerk:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy06.mp3"
window hide
if period == 0:
    scene compoundpooldaybackground blurred:
        zoom 1.9 xoffset -400 yoffset 0
    show powergirlpoolnew01:
        xoffset 0 yoffset 0
    show compoundpooldaybackground blurred at powerfulldownbackground
    show powergirlpoolnew01 at harleyfulldown
    with dissolve
    $ renpy.pause(4.0, hard='True')
    pg "A closer look at how it hugs my shapely rump like a second skin..."
    mc "Ooh, mamma mia!"
    scene compoundpooldaybackground blurred:
        zoom 1.9 xoffset -400 yoffset -900
    show powergirlpoolnew02:
        xoffset 0 yoffset -1080
    show compoundpooldaybackground blurred at poolbackgroundup
    show powergirlpoolnew02 at poolbackgroundpowerup
    with dissolve
    $ renpy.pause(4.0, hard='True') 
    pg "And how it maintains my large breasts in a tight confine..."
    mc "They need to get OUT of that tight confine!"
    pg "Not yet, don't hurry things..."
    scene compoundpooldaybackground blurred:
        zoom 1.9 xoffset -400 yoffset 0
    show powergirlpoolnew03:
        xoffset 0 yoffset 0
    show compoundpooldaybackground blurred at powerfulldownbackground
    show powergirlpoolnew03 at harleyfulldown
    with dissolve
    $ renpy.pause(4.0, hard='True')
    pg "But I'll give you a sneak peek of what's hiding under my teenie thong..."
    mc "Oh God..."
if period == 1:
    scene compoundpoolnight blurred:
        zoom 1.9 xoffset -400 yoffset 0
    show powergirlpoolnew01:
        xoffset 0 yoffset 0
    show compoundpoolnight blurred at powerfulldownbackground
    show powergirlpoolnew01 at harleyfulldown
    with dissolve
    $ renpy.pause(4.0, hard='True')
    pg "A closer look at how it hugs my shapely rump like a second skin..."
    mc "Ooh, mamma mia!"
    scene compoundpoolnight blurred:
        zoom 1.9 xoffset -400 yoffset -900
    show powergirlpoolnew02:
        xoffset 0 yoffset -1080
    show compoundpoolnight blurred at poolbackgroundup
    show powergirlpoolnew02 at poolbackgroundpowerup
    with dissolve
    $ renpy.pause(4.0, hard='True') 
    pg "And how it maintains my large breasts in a tight confine..."
    mc "They need to get OUT of that tight confine!"
    pg "Not yet, don't hurry things..."
    scene compoundpoolnight blurred:
        zoom 1.9 xoffset -400 yoffset 0
    show powergirlpoolnew03:
        xoffset 0 yoffset 0
    show compoundpoolnight blurred at powerfulldownbackground
    show powergirlpoolnew03 at harleyfulldown
    with dissolve
    $ renpy.pause(4.0, hard='True')
    pg "But I'll give you a sneak peek of what's hiding under my teenie thong..."
    mc "Oh God..."
stop music
play music "sounds/waterrun.mp3"
scene powergirlpoolnew07 with dissolve
pg "It's getting hot, isn't it? I need to cool down in the pool..."
if period == 0:
    scene powergirlpoolnew08b with dissolve
if period == 1:
    scene powergirlpoolnew08 with dissolve
play sound "sounds/diving.mp3"
mc "Hey, wait for me, Kara!"
pg "Well, dive in, what are you waiting for?"
if period == 0:
    scene powergirlpoolnew09 with dissolve
if period == 1:
    scene powergirlpoolnew09
    show powergirlpoolnew09b
    with dissolve
mc "Alright, I'll catch you in no time!"
scene powergirlpoolnew10 with dissolve
stop music
play music "sounds/underwater.mp3"
mc "Here I come!"
scene powergirlpoolnew11 with dissolve
mc "* Where did she disappear??? *"
scene powergirlpoolnew12 with dissolve
play sound "sounds/thud.mp3"
mc "* Hey! She's kicking me, better get back to the surface soon!* "
scene powergirlpoolnew13 with dissolve
pg "* Where do you think you're going, [name]? *"
mc "* Quick, before she pulls my... *"
scene powergirlpoolnew14 with dissolve
stop music
play music "sounds/waterrun.mp3"
mc "* ... Too late... *"
pg "I think you lost these, [name]..."
mc "That's not fair. Now I'm naked and you're not!"
scene powergirlpoolnew15 with dissolve
pg "Maybe we should level things a bit then? Just for you, I'll take my top off..."
scene powergirlpoolnew16 with dissolve
pg "Is that more fair?"
scene powergirlpoolnew17 with dissolve
pg "Are you... jerking off underwater? Watching your landlady's daughter half-naked in the pool? Eew, that's kinda gross..."
mc "It's... your hot bod. I can't help it!"
scene powergirlpoolnew18 with dissolve
pg "I think I'd better get out of the pool now before you start sexually assaulting me..."
mc "I wouldn't do that! I just want to get my rocks off, please help me Kara!"
stop music
play music "sounds/sexy06.mp3"
window hide    
scene powergirlpoolnew19:
    zoom 1.0 xoffset -80 yoffset 0    
show powergirlpoolnew19 at powerpoolfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
pg "Now I feel safer. Away from that horny dong of yours..."
scene powergirlpoolnew20:
    zoom 1.0 xoffset -40 yoffset -1500    
show powergirlpoolnew20 at powerpoolfulldown02
with dissolve
$ renpy.pause(6.0, hard='True')    
pg "You're going to be a good boy and stay put in the pool?"
mc "Depends, what do I get in exchange?"
scene powergirlpoolnew21 with dissolve
pg "Something to get your \"rocks off\" as you put it..."
mc "Then I stay put. And get my rocks off."
scene powergirlpoolnew22 with dissolve
pg "Good. You've got to learn to keep that overshooting libido of yours under control. Fortunately, your landlady's daughter's pussy is here to help..."
mc "I don't think it's helping much, I'm getting HARDER and HARDER!"
scene powergirlpoolnew23 with dissolve
if age >= 20:
    pg "Just watch me play with my little pussy and imagine it's your giant piledriver that's plowing it..."
if age >= 18 and age <= 19:
    pg "Just watch me play with my little pussy and imagine it's your giant teenage piledriver that's plowing it..."
window hide
play channel2 "sounds/wetmassage.mp3"

label PowerPoolPussySlow:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussyslowvideo behind powerpoolpussyfastvideo
show powerpoolpussyslowvideo behind powerpoolpussycloserslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyfastvideo
hide powerpoolpussycloserslowvideo
with dissolve
play channel1 "sounds/moan02.mp3"
$ powerpoolpussyfast = False
if powerpoolpussyslow == False:
    pg "That's it, jerk that fat cock of yours while you watch me stroke my pussy..."
    $ powerpoolpussyslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show closer:
     xpos 50 ypos 500     
call screen powerpoolpussyslow()
screen powerpoolpussyslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolPussyFrontSlow")

label PowerPoolPussyFast:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussyfastvideo behind powerpoolpussyslowvideo
show powerpoolpussyfastvideo behind powerpoolpussycloserfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyslowvideo
hide powerpoolpussycloserfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ powerpoolpussyslow = False
if powerpoolpussyfast == False:
    pg "Go on, keep PUMPING that shaft, Do it as FAST as I frig myself!"
    $ powerpoolpussyfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show closer:
     xpos 1700 ypos 500     
call screen powerpoolpussyfast()
screen powerpoolpussyfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussySlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolPussyFrontFast")

label PowerPoolPussyFrontSlow:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussycloserslowvideo behind powerpoolpussyslowvideo
show powerpoolpussycloserslowvideo behind powerpoolpussycloserfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyslowvideo
hide powerpoolpussycloserfastvideo
with dissolve
play channel1 "sounds/moan02.mp3"
$ powerpoolpussyfast = False
if powerpoolpussyslow == False:
    pg "That's it, jerk that fat cock of yours while you watch me stroke my pussy..."
    $ powerpoolpussyslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerpoolpussycloserslow()
screen powerpoolpussycloserslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussySlow")

label PowerPoolPussyFrontFast:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussycloserfastvideo behind powerpoolpussyfastvideo
show powerpoolpussycloserfastvideo behind powerpoolpussycloserslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyfastvideo
hide powerpoolpussycloserslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ powerpoolpussyslow = False
if powerpoolpussyfast == False:
    pg "Go on, keep PUMPING that shaft, Do it as FAST as I frig myself!"
    $ powerpoolpussyfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen powerpoolpussycloserfast()
screen powerpoolpussycloserfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFast")

label PowerPoolPussyEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
pg "Are you gonna cum for me, [name]? Are you going to unload a MASSIVE explosion of SPUNK for your landlady's daughter?"
mc "Y...Yeah, I'm getting close!"
scene powerpoolwankcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
pg "Then cum for me, BLAST that sweet baby-batter!!!"
window hide
with fastflash
mc "I'm NUTTING FOR YOU, KARA!!! AAAHHH!"
scene powerpoolwankcum02 with dissolve
play sound "sounds/moan06.ogg"
pg "Watching you is making me cum too! OOOH!"
window hide 
with fastflash
pg "Look at me squirting, AAAH, it's sooo HOT!"
scene powerpoolwankcum03 with dissolve
mc "Oh God, it's making me BLAST even STRONGER! RHAAA!"
window hide
with hpunch
pg "I can see that, CUM SOME MORE FOR ME!"
scene powerpoolwankcum04 with dissolve
pg "Make it the BIGGEST load ever! Your shots are getting so HUGE, make them COVER me in your warm spunk!"
scene powerpoolwankcum03 with dissolve
mc "Here you GO, MORE FOR YOUUUUU!"
scene powerpoolwankcum05 with dissolve
play sound "sounds/moan02.mp3"
pg "You're a CUM-MACHINE! Look at poor little me, you've CAKED MY TITS in your MONSTER LOAD!"
mc "Just a few last shots, AAAAH!"
stop channel1
play sound "sounds/panting.mp3"
scene powerpoolwankcum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1        
with dissolve
pg "You've made GIANT puddles of cum on the pool surface... I wonder what it tastes like, I just need to grab some..."
scene powerpoolwankcum07 with dissolve
play sound "sounds/lick01.ogg"
pg "Mmh, it tastes GREAT! Chlorine enhances the flavor..."
scene powerpoolwankcum08 with dissolve
play sound "sounds/slurp.mp3"
mc "You learn something new every day."
pg "Thank you for this wonderful CUM-MEAL. But you need to go before the cleaning lady sees the mess you made...."
stop music
stop sound
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label PoolDayWidow:
stop music
play channel1 "sounds/shower.mp3"
scene widowpoolshower00 with fade
mc "I can hear the shower running. Which means that the Black Widow must be in there..."
if mclevel02 == False:
    scene widowpoolshower01 with dissolve
if mclevel02:
    scene widowpoolshowerlevel02a with dissolve
mc "And bingo! Topless no less..."
scene widowpoolshower02 with dissolve
mc " * Look at that fine ass, just LOOK AT IT! *"
scene widowpoolshower03 with dissolve
bw "I might not have any Super-Senses but I could still tell you were around. Lurking."
mc "I am NOT lurking! I was coming for a... fresh shower before heading for the pool."
scene widowpoolshower04 with fastdissolve
bw "Are you SURE about that? I feel like, maybe, you were ogling my backside."
mc "Err... No... Yes... I mean, damn, what an ASS!"
if sawbmasturbation == False:
    scene widowpoolshower03 with dissolve
    bw "Too bad for you, I'm not interested. You haven't been TEASED enough yet. Go and cool off in the pool while I finish my shower."
    mc "But..."
    bw "It's over, [name]!"
    stop channel1
    stop music
    play music "sounds/swim.mp3"
    scene poolmc02 with dissolve
    mc "* Damn it, I need to swim and forget about THAT ass... *"
    scene poolmc03 with dissolve
    mc "* God, THAT ASS! That godamn PERFECT BOOTY! * "
    scene poolmc04 with dissolve
    stop music
    mc "And now she's gone and I'm all alone... She said I haven't been TEASED enough. Maybe I should let her TEASE me some more by visiting her in her room at nights..."
    jump Main
if mclevel02:
    scene widowpoolshower03 with dissolve
    bw "Pity you won't get to fuck it this time. Your cock is simply too big. I would need to... find a bigger dildo and train on it."
    mc "But..."
    bw "It's over, [name]!"
    stop channel1
    stop music
    play music "sounds/swim.mp3"
    scene poolmclevel02b with dissolve
    mc "* Damn it, I need to swim and forget about THAT ass... *"
    scene poolmclevel02c with dissolve
    mc "* God, THAT ASS! That godamn PERFECT BOOTY! * "
    scene poolmclevel02d with dissolve
    stop music
    mc "And now she's gone and I'm all alone... She said I haven't been TEASED enough. Maybe I should let her TEASE me some more by visiting her in her room at nights..."
    jump Main

scene widowpoolshower05 with dissolve
bw "Why don't you drop that that ridiculously bulging swimtrunk and come inside then..."
mc "Alright!"
scene widowpoolshower06 with dissolve
stop channel1
play channel2 "sounds/sexy02.mp3"
bw "Even soft, it's still sssooo GIGANTIC!"
mc "And it's gonna get HARD real fast for you, Natasha!"
if usedseduction == 0:
    bw "I don't know if you... DESERVE any of this... You're not being very seductive..."
    call screen usepower("useseduction", "WidowPoolNoSeduction", "WidowPoolSeduction") with dissolve
if usedseduction >= 1:
    scene widowpoolshower07 with dissolve
    mc "Especially if I start playing with these big funbags of yours..."
    jump WidowPoolDoneSeduction

label WidowPoolNoSeduction:
mc "What? So, you're NOT going to let me fuck you?"
scene widowpoolshower03 with dissolve
bw "I was just SHOWERING until you barged in here with that great big erection of yours! So no, another time maybe. When you're ready!"
stop music
stop channel1
stop music
play music "sounds/swim.mp3"
scene poolmc02 with dissolve
mc "* Damn it, I need to swim and forget about THAT ass... *"
scene poolmc03 with dissolve
mc "* God, THAT ASS! That godamn PERFECT BOOTY! * "
scene poolmc04 with dissolve
stop music
mc "And now she's gone and I'm all alone... She said I should SEDUCE her. Maybe next time, I should be less \"woke\" and press that fucking seduction button."
jump Main

label WidowPoolSeduction:
$ usedseduction += 1
scene widowpoolshower07 with dissolve
mc "Then maybe I should start playing with these big funbags of yours... To SEDUCE you."
label WidowPoolDoneSeduction:
bw "Oooh, what do you have in mind for a FUN game with FUNBAGS?"
scene widowpoolshower08 with dissolve
play sound "sounds/lick01.ogg"
mc "This..."
scene widowpoolshower09 with dissolve
play sound "sounds/moan01.mp3"
bw "Mmmh, yeah, lick it clean... You naughty boy."
scene widowpoolshower10 with dissolve
play sound "sounds/kiss.mp3"
bw "Come and kiss me."
scene widowpoolshower11 with dissolve
mc "Are we finally going to fuck, Natasha?"
if age >= 20:
    bw "I hesitate. Let's start with you rubbing that fat donkey-dick against my asscheeks. Until you EXPLODE!"
if age >= 18 and age <= 19:
    bw "I hesitate. Let's start with you rubbing that fat teenage donkey-dick against my asscheeks. Until you EXPLODE!"
scene widowpoolshower12 with dissolve
mc "Can't I just stick it in your ass please?"
bw "No, you may NOT! Just rub it against my ass... You'll enjoy it, I promise."
play music "sounds/moan02.mp3"
label WidowShowerSlow:
window hide
hide slower
hide cum
show widowshowerslowvideo behind widowshowerfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfastvideo
with dissolve
$ renpy.pause(2.0, hard='True')
bw "Yeah, just like that. Mmmh, it feels so HEAVY!"
window hide
show faster:
     xpos 1700 ypos 500
play channel1 "sounds/boymoan04.mp3"
call screen screenwidowshowerslow()
screen screenwidowshowerslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowShowerFast")

label WidowShowerFast:
hide faster
mc "I need to do it FASTER!"
bw "If that can help you spew your load faster, be my guest..."
window hide
show widowshowerfastvideo behind widowshowerslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerslowvideo
with dissolve
stop channel1
play channel1 "sounds/boymoan02.mp3"
show slower:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen screenwidowshowerfast()
screen screenwidowshowerfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowShowerSlow")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("WidowShowerCum")

label WidowShowerCum:
hide slower
hide cum
mc "I'm gonna cum, Natasha. I'm..."
scene widowpoolshowercum01 with dissolve
hide widowshowerslowvideo
hide widowshowerfastvideo
stop music
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAh, fuck!"
window hide
with fastflash
bw "Mmh, dump that seed all over my backside!"
scene widowpoolshowercum02 with dissolve
bw "Ooh, your shots are getting even BIGGER!"
window hide
with fastflash
mc "AAAH!"
scene widowpoolshowercum03 with dissolve
bw "Keep going [name], I don't want you to stop!"
window hide
with fastflash
mc "I... Oooh FUCK, here's MORE!!!!"
if age >= 20:
    bw "I want you to PLASTER the shower wall. NOW. PROVE to me you're a fucking BULLSTUD, DO IT!"
if age >= 18 and age <= 19:
    bw "I want you to PLASTER the shower wall. NOW. PROVE to me you're a fucking TEEN BULLSTUD, DO IT!"
scene widowpoolshowercum04 with dissolve
play sound "sounds/splat.ogg"
mc "RHAAAA!"
window hide
with fastflash
play sound "sounds/splat.ogg"
bw "Mmmh,that's it, your MONSTERSHOTS are fucking HITTING the wall with such BRUTAL FORCE!"
stop channel1
scene widowpoolshowercum05 with dissolve
play channel1 "sounds/boymoan02.mp3"
play sound "sounds/lick02.mp3"
bw "Mmmh, I just want to FEED on this warm tasty spunk..."
scene widowpoolshowercum06 with dissolve
mc "Damn, I came so MUCH. And I'm STILL ROCKHARD!"
scene widowpoolshowercum07 with dissolve
bw "What??? Oh my God, it's true! I want to suck on your fat bloated balls then..."
scene widowpoolshowercum08 with dissolve
play sound "sounds/lick03.mp3"
mc "Yeah, get them to churn another HUGE load for you!"
scene widowpoolshowercum09 with dissolve
play sound "sounds/lick02.mp3"
bw "I would like THAT! * suck * "
scene widowpoolshowercum10 with dissolve
bw "Maybe I should switch to the other BLOATED ball?"
scene widowpoolshowercum11 with dissolve
play sound "sounds/lick03.mp3"
mc "Og God... You're suckling on it like a starved calf!"
scene widowpoolshowercum12 with dissolve
play sound "sounds/lick02.mp3"
bw "Mmmh, there's so much cummy afterdreg to lick still..."
scene widowpoolshowercum13 with dissolve
mc "I can't..."
scene widowpoolshowercum14 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "...HOLD OFF, AAAH!!!"
window hide
with fastflash
if age >= 20:
    bw "Ooh, I coaxed ANOTHER load out of your behemoth? I'm so NAUGHTY!"
if age >= 18 and age <= 19:
    bw "Ooh, I coaxed ANOTHER load out of your teenage behemoth? I'm so NAUGHTY!"
scene widowpoolshowercum15 with dissolve
play sound "sounds/moan01.mp3"
bw "Mmmh, I LOVE how your shaft CONTORTS and SPASMS with each POWERFUL SHOT OF SPUNK!"
window hide
with fastflash
mc "I can feel that..."

if inventorylustring == False:
    scene widowpoolshowercum16a
    show widowpoolshowercum16b
    with dissolve
    mc "... I... don't think I...can cum anymore! AAAH!"
    window hide
    with fastflash
    bw "Blast the last of it then, [name]!"
    scene widowpoolshowercum17 with dissolve
    play sound "sounds/slurp.mp3"
    bw "That's a decent amount of spunk... I won't let it go down the drain... * slurp *"
    scene widowpoolshowercum19 with dissolve
    play sound "sounds/panting.mp3"
    bw "But now your cock is totally spent. Defeated by the Black Widow's expert hands!"
    mc "Oh God... Yeah... I'd better..."
    bw "Go back to your room? Yes, you'd BETTER!"
    mc "* If only I had a cockring that would allow me to keep on going after these mighty cumshots... Maybe this scene would be longer. *"
    jump Main
if inventorylustring:
    scene widowpoolshowercum16a
    show widowpoolshowercum16c
    with dissolve
    mc "... I still have MORE, RHAAAA!"
    play sound "sounds/magic.mp3"
    hide widowpoolshowercum16c
    show widowpoolshowercum16d
    with fastdissolve
    $ renpy.pause(0.5, hard='True')
    hide widowpoolshowercum16d
    show widowpoolshowercum16e
    with fastdissolve
    $ renpy.pause(0.5, hard='True')
    play sound "sounds/boymoan05.mp3"
    window hide
    with fastflash
    bw "MUCH more by the looks of it! Wow!"

scene widowpoolshowercum17 with dissolve
play sound "sounds/slurp.mp3"
bw "Look at all that spunk... I won't let it go down the drain... * slurp *"
scene widowpoolshowercum18 with dissolve
mc "That's all very well, but my cock needs a tight hole this TIME!"
bw "What are you going to do???"
mc "I'm gonna ASSFUCK YOU, that's what I'm going to do!"
bw "But..."
window hide

label WidowPoolSlowFuck:
hide cum
hide slower
hide faster
hide assview
hide front
$ widowpoolassharder = False
show widowshowerfaceslowvideo behind widowshowerfacefastvideo
show widowshowerfaceslowvideo behind widowshowerassslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerassslowvideo
hide widowshowerfacefastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen widowpoolassfacefuckslow()
screen widowpoolassfacefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFastFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolFaceSlow")

label WidowPoolFastFuck:
hide cum
hide slower
hide faster
hide assview
hide front
if widowpoolassharder == False:
    bw "Are you going to pound me harder?"
    mc "Is that what you want, Natasha?"
    bw "YES! I want your giant cock ripping my ass apart!"
    $ widowpoolassharder = True    
show widowshowerfacefastvideo behind widowshowerfaceslowvideo
show widowshowerfacefastvideo behind widowshowerasssfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfaceslowvideo
hide widowshowerassfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen widowpoolassfacefuckfast()
screen widowpoolassfacefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFaceFast")


label WidowPoolFaceSlow:
$ widowpoolassharder = False
hide cum
hide slower
hide faster
hide assview
hide front
show widowshowerassslowvideo behind widowshowerfaceslowvideo
show widowshowerassslowvideo behind widowshowerasssfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfaceslowvideo
hide widowshowerassfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen widowpoolassfuckslow()
screen widowpoolassfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFaceFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolSlowFuck")

label WidowPoolFaceFast:
hide cum
hide slower
hide faster
hide assview
hide front
if widowpoolassharder == False:
    bw "Go on, stick your monster shaft harder into my booty! ANAL-DESTROY ME!"
    mc "Since you ask so politely..."
    $ widowpoolassharder = True
show widowshowerassfastvideo behind widowshowerfacefastvideo
show widowshowerassfastvideo behind widowshowerassslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerassslowvideo
hide widowshowerfacefastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show front:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen widowpoolassfuckfast()
screen widowpoolassfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolFaceSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFastFuck")

label WidowPoolFuckEnd:
bw "You've got another big load for my ass, STUD?"
mc "Fuck yeah, you want it?"
bw "Yes, BLAST that young spunk inside me [name], go on, FILL ME UP TO THE BRIM!"
scene widowpoolasscum01 with dissolve
hide widowshowerassfastvideo
hide widowshowerfacefastvideo
hide widowshowerassslowvideo
hide widowshowerfaceslowvideo
stop channel1
play channel1 "sounds/splooge02.mp3"
mc "Alright, here it comes, AAAH!"
window hide
with fastflash
bw "Mmh, I can FEEL every shot, they are so POWERFUL!"
scene widowpoolasscum02 with dissolve
play sound "sounds/womancum01.mp3"
mc "Fuck, I'm just coming NON-STOP! RHAAA!"
window hide
with fastflash
if age >= 20:
    bw "Your warm spunk is overflowing down my back!"
if age >= 18 and age <= 19:
    bw "Your warm teenage spunk is overflowing down my back!"
scene widowpoolasscum03 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "And here's more baby-batter for your back, DAMN IT, FU-UU-UUCK!"
window hide
with fastflash
bw "Keep going, more, MORE!"
scene widowpoolasscum04 with dissolve
play sound "sounds/boymoan05.mp3"
mc "RHAAA!"
window hide
with fastflash
bw "You could DROWN a woman in your virile load!..."
scene widowpoolasscum05 with dissolve
play sound "sounds/panting.mp3"
bw "...But not the Black Widow... Looks like I finally managed to tame that BEAST..."
mc "My balls hurt ssooo much..."
scene widowpoolasscum06 with dissolve
play sound "sounds/slap.mp3"
bw "That's what happens when you try to outfuck ME! Now let me finish my shower... I need to clean off all that SPUNK!"
$ widowpoolassfuck = True
jump Main

label PoolDayMILF:
play music "sounds/waterrun.mp3"
scene compoundpooldaybackground with fade
show milfpool01 at centerleft with dissolve
cm "Oh, hello sweetie, coming for a day swim?"
hide milfpool01
show milfpooleyeblink
with fastdissolve
label MILFpoolDialoguesDay:
menu:
    "I was wondering where one could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide milfpooleyeblink
        show milfpool04 at centerleft
        with fastdissolve
        cm "But, she's just an intern. Why would she need a costume?"
        mc "She's still a SUPER-HERO! And superheroes have a costume, otherwise, they don't look like superheroes. And it gets confusing."
        hide milfpool04
        show milfpool02 at centerleft
        with fastdissolve
        cm "I suppose so... Well, there is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide milfpool02
        show milfpool03 at centerleft
        with fastdissolve
        hide auditquestcostumeprogress01
        cm "Just don't spend too much money on her. She's JUST an intern, sweetie."
        mc "Sure, Carol."
        hide milfpool03
        show milfpooleyeblink
        with fastdissolve        
        jump MILFpoolDialoguesDay
    "I'll go for a swim now.":
        hide milfpooleyeblink
        show milfpool03 at centerleft
        with fastdissolve        
        cm "And I'll head to the sauna..."
        if mclevel02 == False:
            scene poolmilfsauna00
        mc "* Damn... Her fine ass is making me hard... I'm gonna need to go for a swim to keep my hardening dong down."
        play music "sounds/swim.mp3"
        if mclevel02 == False:
            scene poolmc03 with fade
        if mclevel02:
            scene poolmclevel02c with fade
        mc "There. That's better... Now I can leave the pool without an aching hardon..."
        stop music
        jump Main    
    "I'll join you, that's where I was heading too." if mclevel02 == False:
        jump PoolSaunaMILF
    "I need to get my Super-Resistance up a notch. I feel too...unresistant." if mclevel02 and seenmilfpoolresistance == False:
        hide milfpooleyeblink
        show milfpool03 at centerleft
        with fastdissolve 
        cm "Then follow me to the sauna, I have an idea..."
        if mcresistance >= 2:
            cm "Although since you're already level 2 in Super-Resistance, I doubt it will achieve anything..."
        if mcresistance >= 1 and evilness >= 13:
            cm "Although since you're already level 1 in Super-Resistance, I doubt it will achieve anything..."
        jump MilfPoolResistance

label CompoundPoolNight:
stop music
play music "sounds/waterrun.mp3"

if d10locnight == 1 or d10locnight == 10:
    jump PoolNightMILF
if (d10locnight == 2 or d10locnight == 8) and mclevel02 == False:
    jump PoolNightWidow
if (d10locnight == 3 or d10locnight == 4) and seenpowerpool and powerlingerie and mclevel02 == False:
    jump PoolNightPowerScene
if d10locnight == 3 or d10locnight == 4:
    jump PoolNightPower
#if d10locnight == 6:
#    jump PoolNightWonder

jump PoolEmpty

label PoolNightMILF:
scene poolmilf01 with fade
if d10locnightpoolmilf == 1:
    jump PoolNightMILF01
if d10locnightpoolmilf == 2 and mclevel02 == False:
    jump PoolNightMILF02
if d10locnightpoolmilf == 2 and mclevel02:
    jump PoolNightMILF01
    
label PoolNightMILF01:
mc "Oooh, Captain MILF is coming out of the water... In a very WET bikni..."
scene poolmilf02 with dissolve
cm "It's you. I thought it might be..."
scene poolmilf06 with dissolve
cm "Let me dry myself up a bit..."
scene poolmilf07 with dissolve
cm "I'll be with you in a moment..."
scene poolbackground:
    zoom 1.9 xoffset -400 yoffset -980
show milfpoollarge:
    xoffset 0 yoffset -1080
show poolbackground at poolbackgroundup
show milfpoollarge at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True')     
mc "* Damn, her bikini is so wet,it's almost SEE-THROUGH! *"
scene poolbackground
show milfpool01 at centerleft with dissolve
cm "Why don't you go for a swim [name]? I'm done. I was heading for the sauna."
hide milfpool01
show milfpooleyeblink
with fastdissolve
label MILFpoolDialogues:
menu:
    "I was wondering where one could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide milfpooleyeblink
        show milfpool04 at centerleft
        with fastdissolve
        cm "But, she's just an intern. Why would she need a costume?"
        mc "She's still a SUPER-HERO! And superheroes have a costume, otherwise, they don't look like superheroes. And it gets confusing."
        hide milfpool04
        show milfpool02 at centerleft
        with fastdissolve
        cm "I suppose so... Well, there is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide milfpool02
        show milfpool03 at centerleft
        with fastdissolve
        hide auditquestcostumeprogress01
        cm "Just don't spend too much money on her. She's JUST an intern, sweetie."
        mc "Sure, Carol."
        hide milfpool03
        show milfpooleyeblink
        with fastdissolve        
        jump MILFpoolDialogues
    "I'll go for a swim now.":
        hide milfpooleyeblink
        show milfpool03 at centerleft
        with fastdissolve        
        cm "And I'll head to the sauna..."
        if mclevel02 == False:
            scene poolmilfsauna00
        mc "* Damn... Her fine ass is making me hard... I'm gonna need to go for a swim to keep my hardening dong down."
        play music "sounds/swim.mp3"
        if mclevel02 == False:
            scene poolmc03 with fade
        if mclevel02:
            scene poolmclevel02c with fade
        mc "There. That's better... Now I can go to bed without an aching hardon..."
        stop music
        jump Main
    "I'll join you, that's where I was heading too." if mclevel02 == False:
        jump PoolSaunaMILF
    "I need to get my Super-Resistance up a notch. I feel too...unresistant." if mclevel02:
        hide milfpooleyeblink
        show milfpool03 at centerleft
        with fastdissolve 
        cm "Then follow me to the sauna, I have an idea..."
        if mcresistance >= 2:
            cm "Although since you're already level 2 in Super-Resistance, I doubt it will achieve anything..."
        if mcresistance >= 1 and evilness >= 13:
            cm "Although since you're already level 1 in Super-Resistance, I doubt it will achieve anything..."
        jump MilfPoolResistance

label PoolNightMILF02:
mc "Oooh, Captain MILF is going into the water... Let's join her then So I can admire her FIT big-titted body from UP CLOSE..."
stop music
play music "sounds/swim.mp3"
scene poolmilf03 with dissolve
cm "Are you enjoying the swimming pool, [name]?"
mc "Ooh yeah."
scene poolmilf04 with dissolve
cm "I've been in here long enough now..."
stop music
scene poolmilf08 with dissolve
cm "Are you staying or are you coming out of the pool too?"
mc " * Shit, I have a monster hardon right now... *"
scene poolmilf05 with dissolve
mc "Err, I'll be staying for a while longer, Carol."
cm "Alright, sweetie!"
if mclevel02 == False:
    scene poolmc04 with dissolve
if mclevel02:
    scene poolmclevel02d with dissolve
mc "Now that she's gone, I can finally come out of the pool."
jump Main
    
label PoolNightWidow:
scene poolbackground with fade
if widowpoolsaid == False:
    mc "Hang on, where's the Black Widow? It clearly said she would be here, this is a dev scam!"
    $ widowpoolsaid = True
    jump PoolNightWidowb
mc "Once again, it appears that the Black Widow will only show up AFTER I've gone for a swim..."
label PoolNightWidowb:
scene poolmc01 with dissolve
mc "So I guess I have no choice but to swim... Alone."
stop music
play music "sounds/swim.mp3"
scene poolmc02 with dissolve
mc "* Surely the black widow will come anytime now... *"

scene poolmc03 with dissolve
if age >= 20:
    mc "* Ah, maybe she'll come as I do a back-crawl and my monster cock is clearly visible above the water surface... *"
if age == 18 or age == 19:
    mc "* Ah, maybe she'll come as I do a back-crawl and my monster teenage cock is clearly visible above the water surface... *"
stop music
scene widowpool01 with dissolve
bw "Well, well, well, if it isn't [hero] swimming in a super-tight speedo..."
mc "* bingo *"
scene widowpoolbackground02 blurred
show widowpool03
with dissolve
play music "sounds/sexy06.mp3"
bw "What do you think of MY super-tight bikini?"
window hide
show widowpoolbackground01 blurred:
    zoom 1.1 xoffset -100 yoffset 0
show widowpool02:
    zoom 1.0 xoffset -50 yoffset 0    
show widowpoolbackground01 blurred at widowpoolbackzoombackground
show widowpool02 at widowpoolfullup
with dissolve
$ renpy.pause(4.0, hard='True')     
bw "Have a good look at the back... How it fits snugly between my TIGHT asscheeks..."
mc "I am... having a good look."
scene widowpoolbackground02 blurred
show widowpool03
with dissolve
bw "Now don't get any funny ideas. After all, I came here to SWIM."
scene widowpoolbackground02 blurred:
    zoom 1.1
show widowpool04
with dissolve
bw "So let me do a bit of stretching first..."
mc "Damn, you're supple..."
hide widowpool04
show widowpool05
with dissolve
bw "As an expert COMBAT Super-Heroine, I NEED to be..."
scene widowpoolbackground02 blurred:
    zoom 1.2 yoffset -200
show widowpool06a
with dissolve
bw "...And to stay FIT!"
hide widowpool06a
show widowpool06b
with fastdissolve
bw "A few one-armed press-ups..."
window hide
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool07
with dissolve
bw "And a bit more teasing..."
mc "Ggg...ggg..."
hide widowpool07
show widowpool09
with dissolve
bw "Now you seem to be ready for some UNDERWATER combat training... Try and catch me if you can, [name]..."
stop music
scene widowpool10 with dissolve
mc "Wh...What???"
scene widowpool11 with dissolve
play sound "sounds/diving.mp3"
bw "You'd better hurry up, I already have a head-start!"
scene widowpool12 with dissolve
stop sound
play music "sounds/underwater.mp3"
mc "* She's taunting me... *"
scene widowpool13 with dissolve
mc "* Let's make a move... Not too sudden... So I can surprise her... *"
scene widowpool14 with dissolve
play sound "sounds/whoosh.mp3"
mc "What the??? Damn, she's fast!"
scene widowpool15 with dissolve
stop sound
mc "* Where did she go??? *"
scene widowpool16 with dissolve
bw "* I'm here, silly... SURPRISE! *"
play sound "sounds/kiss.mp3"
mc "* Ok, you win, Natasha... *"
scene widowpool17 with dissolve
stop sound
mc "* Let's grab her ass and see where that goes... *"
scene widowpool18 with dissolve
bw "* No, no, you naughty boy. Not yet... *"
mc "* Ah. Nowhere apparently... *"
stop music
scene widowpool19:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with fade
bw "Now you stay and cool down, [name]. I think you had enough emotions for the night..."
mc "No I didn't, no I didn't!"
bw "Goodnight and sweet dreams!"
jump Main

label PoolNightPower:
$ seenpowerpool = True
scene poolpower01 with fade
pg "Hello [name]... I super-heard you coming..."
scene poolbackground:
    zoom 1.9 xoffset -400 yoffset -980
show powerpoollarge:
    xoffset 0 yoffset -1080
show poolbackground at poolbackgroundup
show powerpoollarge at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True')     
pg "Stop staring at me like that and pass me the towel will you? I'm all wet..."
mc "Err, yeah, sure..."
scene poolbackground
show powerpool02
with dissolve
pg "Thank you, [name]. Are you going in the pool now or are you going to continue to stare?"
mc "Ah, yeah, the pool. Swimming. That's why I came here, right?"
hide powerpool02
show powerpool03
with dissolve
pg "Maybe in a later version, there will be MORE to this scene... * wink *"
mc "I bloody well hope so... Goodnight, Kara."
hide powerpool03
show powerpool04
with dissolve
pg "That would be nice, wouldn't it? Goodbye, [name]!"
scene poolmc03 with dissolve
mc "I didn't *actually* come here to swim but never mind..."
jump Main

label PoolNightPowerScene:
scene compoundpowermc00 with fade
play music "sounds/waterrun.mp3"
mc "Oh, Kara is relaxing in the pool."
scene compoundpowermc01 with dissolve
mc "She looks so peaceful, with her big gazoongas sticking out of the water like that..."
scene compoundpowermc02 with dissolve
mc "Therefore, it's the perfect opportunity to play a trick on her. GERONIMO!"
scene compoundpowermc03 with dissolve
play sound "sounds/diving.mp3"
mc "Shit, she plunged under the surface just in the nick of time!"
scene compoundpowermc04 with dissolve
stop music
play music "sounds/underwater.mp3"
mc " * But I see her, she won't escape me! *"
scene compoundpowermc05 with dissolve
if mcagility >= 1:
    mc " * Come on, my Super-Agility should be enough... *"
if mcagility == 0:
    mc " * She's trying to use her Super-Agility to evade me... *"
scene compoundpowermc06 with dissolve
mc "* Almost, just a few inches... *"
scene compoundpowermc07 with dissolve
play music "sounds/waterrun.mp3"
pg "Not fast enough, [name]!"
scene compoundpowermc08 with dissolve
play sound "sounds/diving.mp3"
play music "sounds/underwater.mp3"
mc "* Damn, where did she go? * "
scene compoundpowermc09 with dissolve
pg "* Got you, [name]! *"
mc "* AAARGH! She's holding me in a tight armlock! And my Super-Strength is... Gotta tense all my MUSCLES... *"
scene compoundpowermc10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "* My Super-Cock is also getting tense, her armlock is making all the blood RUSH to it! *"
play sound "sounds/ripping.mp3"
mc "* Uh oh... My speedo is about to get ripped apart... *"
scene compoundpowermc11 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "I need to get out of that armlock, I can't breathe!"
scene compoundpowermc12 with dissolve
play music "sounds/waterrun.mp3"
if mcstrength >= 2:
    pg "Do you give up yet [name]? You might be Super-Stronger than me, but I have the advantage and you're out of breath!"
if mcstrength == 1:
    pg "Do you give up yet [name]? My Super-Strength is a perfect match to yours but I have the advantage!"
    jump PowerPoolNoStrength
if mcstrength >= 2:
    call screen usepower("usestrength", "PowerPoolNoStrength", "PowerPoolStrength") with dissolve
label PowerPoolNoStrength:
mc "I... Fine, I give up! Please let go of me, Kara!"
scene compoundpowermc13 with dissolve
play channel2 "sounds/sexy09.mp3"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
pg "Oh, but what about this great big hardon you're sporting? I can't leave you all flustered like this..."
if helpedpowergirl:
    pg "After all, you did try to help me when I was fighting that evil nazi Valkyrie... Even if you did it CLUMSILY."
scene compoundpowermc14 with dissolve
play sound "sounds/boymoan.mp3"
mc "Well, err..."
play music "sounds/underwater.mp3"
play channel1 "sounds/wank.mp3"

label PowerPoolSlow:
hide cum
hide faster
hide slower
hide harder
hide softer
show powerpoolhjslowvideo behind powerpoolhjfastvideo
show powerpoolhjslowvideo behind powerpoolhardhjslowvideo
$ powerpooltalkfast = False
$ powerpoolpoundtalk = False
pg "I'll just jerk you off... Nice and slow..."
window hide
$ renpy.pause(1.0, hard='True') 
hide powerpoolhjfastvideo
hide powerpoolhardhjslowvideo
with dissolve
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen powerpoolpovslow()
screen powerpoolpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolHardSlow")

label PowerPoolFast:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpooltalkfast == False:
    pg "I think I need to go a little FASTER on that shaft, it's just BEGGING for it!"
    $ powerpooltalkfast = True
show powerpoolhjfastvideo behind powerpoolhjslowvideo
show powerpoolhjfastvideo behind powerpoolhardhjfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerpoolhjslowvideo
hide powerpoolhardhjfastvideo
with dissolve
$ powerpoolpoundtalk = False
pause
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen powerpoolpovfast()
screen powerpoolpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolSlow")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolHardFast")

label PowerPoolHardSlow:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpoolpoundtalk == False:
    mc "Please Kara... I need some release soon!"
    if age >= 20:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT monster schlong?"
    if age >= 18 and age <= 19:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT teenage monster schlong?"
    window hide
    $ powerpoolpoundtalk = True
show powerpoolhardhjslowvideo behind powerpoolhjslowvideo
show powerpoolhardhjslowvideo behind powerpoolhardhjfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerpoolhjslowvideo
hide powerpoolhardhjfastvideo
with dissolve
$ powerpooltalkfast = False
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen powerpoolpoundslow()
screen powerpoolpoundslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolCum")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolSlow")

label PowerPoolHardFast:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpooltalkfast == False:
    pg "I think I need to go a little FASTER on that shaft, it's just BEGGING for it!"
    $ powerpooltalkfast = True
if powerpoolpoundtalk == False:
    mc "Please Kara... I need some release soon!"
    if age >= 20:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT monster schlong?"
    if age >= 18 and age <= 19:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT teenage monster schlong?"
    window hide
    $ powerpoolpoundtalk = True
show powerpoolhardhjfastvideo behind powerpoolhardhjslowvideo
show powerpoolhardhjfastvideo behind powerpoolhjfastvideo
$ renpy.pause(1.0, hard='True') 
hide powerpoolhardhjslowvideo
hide powerpoolhjfastvideo
with dissolve
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerpoolpoundfast()
screen powerpoolpoundfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolHardSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolCum")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolFast")

label PowerPoolCum:
window hide
hide cum
hide slower
hide faster
mc "Kara, I'm... about to..."
scene powerpoolhandjobcum01 with dissolve
stop channel1
play sound "sounds/boymoan04.mp3"
mc "... BLOW! AAAH!"
window hide
with hpunch
pg "That's it, release all that pent-up scum for your landlady's daughter!"
scene powerpoolhandjobcum02 with dissolve
stop music
play music "sounds/waterrun.mp3"
play sound "sounds/boymoan05.mp3"
pg "Ooh, you're cumming so HARD, your plumes of SPUNK are erupting right through the water!"
window hide
with fastflash
mc "RHAAAA! Blasting at FULL ALPHA-POWER!"
scene powerpoolhandjobcum03 with dissolve
play sound "sounds/boyorgasm01.mp3"
pg "Keep PUMPING all that nasty spunk, [name]! I LOVE IT when you cum like a STALLION!"
window hide
with fastflash
mc "Oh God, Kara, I'm..."
scene powerpoolhandjobcum03 with dissolve
play sound "sounds/boymoan05.mp3"
pg "...BLASTING at FULL STRENGTH? Yeah, I can see that..."
window hide
with fastflash
mc "AAAAH, it's so GOOD!!!!"
scene powerpoolhandjobcum04 with dissolve
pg "Oh my God, look at THAT SHOT! It's just GIGANTIC!"
window hide
with hpunch
pg "My expert POWER hand is just EMPTYING your balls, isn't it?"
scene powerpoolhandjobcum05 with dissolve
play sound "sounds/boymoan03.mp3"
pg "Still spewing that FAT load, [name]? Spewing that MONSTER LOAD for little me?"
window hide
with fastflash
pg "Look at you, you're COVERED in your own slime! That's just so FILTHY!"
scene powerpoolhandjobcum06 with dissolve
stop channel1
stop sound
pg "You're swimming in a puddle of your own cum. You're gonna have to clean the pool after this MIGHTY ORGASM, [name]!"
mc "Rrrrhoo..."
mc "Is that all you can say? After your landlady's daughter gave you such a POWERFUL handjob?"
scene powerpoolhandjobcum07 with dissolve
pg "I'll help you clean up just a bit before I go..."
play sound "sounds/slurp.mp3"
pg "Mmmh, [hero]'s spunk certainly has an ALPHA-TASTE! Goodnight, [name]!"
mc "Gggg..."
stop channel2
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label PowerPoolStrength:
$ usedstrength += 1
scene compoundpowermc20 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "RHAAA! No, I WON'T GIVE UP!"
pg "Oh my God, you're so POWERFUL!"
scene compoundpowermc21 with dissolve
mc "Now [hero] has the UPPER HAND!"
pg " * cough * You're choking me [name], please be careful!"
mc "I will, I don't want to damage my SEXUAL GOODS!"
scene compoundpowermc22 with dissolve
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play channel1 "sounds/sexy06.mp3"
pg "I'm totally at the mercy of your HUGE muscles now! What are you going to do to poor little me after I teased you so much?"
mc "You're a NAUGHTY girl, Kara! And a naughty girl needs to be PUNISHED!"
scene compoundpowermc23 with dissolve
play sound "sounds/ripping.mp3"
pg "Hey, you're RIPPING my bikini top!"
mc "That's right, I want access to those sumptuous FUNBAGS!"
scene compoundpowermc24:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "I need some superhero tiddy milk!"
pg "Why would I be making breast milk?"
mc "Cos you're a SUPERHEROINE and I WANT tiddy milk! So GIVE ME TIDDY MILK!"
label PowerPoolBreastSlow:
hide nexticon
hide faster
hide slower
pg "If you're prepared to work for it..."
play channel2 "sounds/moan02.mp3"
window hide
show powerpoolbreastslowvideo behind powerpoolbreastfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolbreastfastvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen powerpoolbreastslowb()
screen powerpoolbreastslowb():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("PowerPoolBreastFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolBreastEnd")

label PowerPoolBreastFast:
hide faster
hide slower
hide nexticon
play sound "sounds/moan03.mp3"
pg "Mmmh, do it faster, [name], I think it might be coming..."
window hide
show powerpoolbreastfastvideo behind powerpoolbreastslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolbreastslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen powerpoolbreastfastb()
screen powerpoolbreastfastb():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PowerPoolBreastSlow")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolBreastEnd")

label PowerPoolBreastEnd:
hide nexticon
hide slower
hide faster
mc "Gimme gimme gimme!"
stop channel2
scene powerpoolbreastmilk01 with dissolve
play sound "sounds/moan03.mp3"
pg "AAAH, I'm lactating!"
window hide
with fastflash
mc "Mmmh, fill up my mouth, Kara!"
scene powerpoolbreastmilk02 with dissolve
play sound "sounds/slurp.mp3"
pg "You're so... NAUGHTY! Licking my breast like that, I..."
window hide
with hpunch
play sound "sounds/moan06.ogg"
pg "... I'm CUMMMING! AAAH!"
scene powerpoolbreastmilk03 with dissolve
mc "That was really... * swallow* tasty..."
pg "Can I go now, please?"
scene powerpoolbreastmilk04 with dissolve
mc "Yeah, OK, let me just admire the view as you leave the pool, Kara..."
scene powerpoolbreastmilk05:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "I'm sorry to be leaving you with such a great big HARDON, [name]! I guess you'll have to take care of it yourself this time..."
scene powerpoolbreastmilk06 with dissolve
mc "Yeah, I'm so fucking hard. Hopefully, this scene will be expanded in the future when I feel BAD enough to force her into giving me a BJ..."
stop channel2
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
    
label PoolSaunaMILF:
$ seenmilfsauna = True
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
scene poolmilfsauna00 with dissolve
cm "Then I'll be waiting for you inside, sweetie! Get yourself a towel to cover... your bulge please."
scene poolmilfsauna01 with dissolve
mc "Right, I'll get a towel, but I'll get out of my speedo too. Don't want it to cling to my sweaty body while we're in there..."
scene poolmilfsauna02 with fade
play music "sounds/sexy05.mp3"
cm "This will rid your body of toxins, you just need to sweat them out..."
mc "Aaahh, this is nice and relaxing..."
scene poolmilfsauna03 with dissolve
cm "* It's getting so hot in here, I'll sneakily get rid of my towel while he's slowly drifting away... *"
scene poolmilfsauna04 with dissolve
cm "* And now I can relax. Although I don't need to get rid of toxins myself since I'm super-resistant to them... *"
scene poolmilfsauna05 with dissolve
mc "* Damn, she went topless while I was drifting away... What a HUGE pair of MILF funbags... I think I'm getting a...* "
scene poolmilfsauna06 with dissolve
mc "* Oh shit... *"
cm "I thought you weren't looking!"
scene poolmilfsauna07 with dissolve
mc "I WAS looking and now I can't stop my cock from hardening!"
scene poolmilfsauna08 with dissolve
cm "Oh dear me, you dropped your towel and now I can see your... HUGE COCK!"
scene poolmilfsauna09 with dissolve
play sound "sounds/thud.mp3"
mc "I can't hide it anymore, Carol, sorry..."
cm "I'm getting weak in the knees..."
scene poolmilfsauna10 with dissolve
cm "We have to do SOMETHING about it, I can sense I've lost my superpowers and if the compound gets attacked, I'll be useless!"
mc "Well, there's only one way to get it down..."
scene poolmilfsauna11 with dissolve
cm "You mean... You want me to blow you?"
mc "It's the only way, Captain MILF..."
scene poolmilfsaunapreblow01 with dissolve
if age >= 20:
    cm "I... can't resist. That HUGE schlong is... mesmerizing."
if age == 18 or age == 19:
    cm "I... can't resist. That HUGE teenage schlong is... mesmerizing."
mc "Go right ahead, it's all yours!"
cm "My hand can't even get halfway around its GIRTH... I want to feel its POWER!"
window hide
show poolmilftonguevideo with dissolve
play channel2 [ "<silence .75>", "sounds/thud.mp3" ]
pause
cm "It's so HEAVY! Like a battering ram!"
window hide
pause
stop channel2
scene poolmilfsaunapreblow02 with dissolve
hide poolmilftonguevideo
play sound "sounds/lick01.ogg"
cm "And now, let me DRAIN your fat balls with my MOUTH!"
mc "Yeah... I'm ready for it, Carol!"
play channel2 "sounds/wank.mp3"
window hide

label SaunaMILFSlow:
hide cum
hide faster
hide slower
window hide
show milfsaunablowslowvideo behind milfsaunablowfastvideo
$ renpy.pause(2.0, hard='True')
hide milfsaunablowfastvideo
with dissolve
mc "Damn that's good... Nice and slow..."
window hide
show faster:
     xpos 1700 ypos 500
play channel1 "sounds/blow01.mp3"
call screen screensaunaMILFslow()
screen screensaunaMILFslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SaunaMILFFast")

label SaunaMILFFast:
hide cum
hide slower
hide faster
mc "Please... DO it faster!"
window hide
show milfsaunablowfastvideo behind milfsaunablowslowvideo
$ renpy.pause(1.0, hard='True')
hide milfsaunablowslowvideo
with dissolve
stop channel1
play channel1 "sounds/blow02.mp3"
show slower:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen screensaunaMILFfast()
screen screensaunaMILFfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("SaunaMILFSlow")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("SaunaMILFCum")

label SaunaMILFCum:
hide cum
hide faster
hide slower
mc "I'm about to bust my nut, Carol..."
window hide
$ renpy.pause(2.0, hard='True')
stop channel2
stop channel1
scene poolmilfsaunacum01 with dissolve
hide milfsaunablowslowvideo
hide milfsaunablowfastvideo
play sound "sounds/boymoan03.mp3"
mc "AAAH! Directly into your mouth!"
window hide
with fastflash
cm "Gllluub..."
play sound "sounds/boyorgasm01.mp3"
scene poolmilfsaunacum02 with dissolve
mc "Fuck! AAAH, my cream is flowing out of your mouth!"
window hide
with fastflash
mc "STIIIILLL... BLLAAA-AAA-STING!"
play sound "sounds/boymoan02.mp3"
scene poolmilfsaunacum03:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "Oh God..."
play sound "sounds/panting.mp3"
stop music
scene poolmilfsaunacum04 with dissolve
cm "Is it.... finally going to go down now?"
mc "Not if you're ready for some mo..."
cm "No [name], you must get this thing DOWN now! The security of the compound is at stakes!"
mc "Alright, Captain MILF, I'll... go back to my room then. Thanks for the blowjob."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label MilfPoolResistance:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ seenmilfpoolresistance = True
stop music
play music "sounds/sexy01.mp3"
scene milfpoolresistance01 with dissolve
cm "You'll have to get totally NAKED for this resistance test. And please try not to get a hardon in front of your League Captain..."
mc "Not a problem. I'm good at getting naked."
scene milfpoolresistance02 with dissolve
cm "I will of course wear a towel so you don't get all excited from watching my Super-MILF figure..."
mc "* Damn it! *"
cm "Now I'm going to turn the sauna heat to MAXIMUM LEVEL."
scene milfpoolresistance03 with dissolve
cm "Just relax. And make sure that dong of yours is also totally RELAXED, understood?"
mc "Yes, Captain MILF..."
scene milfpoolresistance04 with dissolve
cm "How are you feeling?"
mc "Its getting...  HOT! Like. SUPER-HOT!"
cm "You're sweating, that's good. Super-Resistance is about controlling your BODY to withstand extreme temperatures."
scene milfpoolresistance05 with dissolve
cm "So focus on that. Focus on using your skin surface to let the heat OUT of your..."
scene milfpoolresistance06 with dissolve
cm "* Oh no, I think my tenant is getting hard... He's so SEXY looking like this with his massive... *"
scene milfpoolresistance07 with dissolve
cm "* ... YOUNG HORSECOCK and HUGE MUSCLES! *"
scene milfpoolresistance08 with dissolve
mc "Uh oh! The extreme heat made me SUPER-HARD! I didn't mean to, I swear Captain MILF!"
scene milfpoolresistance09 with dissolve
cm "Your cock... Your GIANT [age]yo MONSTERDICK!..."
mc "Are you alright, Carol?"
scene milfpoolresistance10 with dissolve
cm "No! My Super-Resistance is... failing me because of your MASSIVE erection!"
mc "It's getting ... so HOT!"
scene milfpoolresistance11 with dissolve
mc "Must... RESIST!"
scene milfpoolresistance12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
mc "AAAH! The extreme HEAT is lifting my body in the air and tearing at my skin!"
cm "My skin is... BURNING!"
mc "I need to use my cock skin surface to let the HEAT out and save Captain MILF before it's too late!"
scene milfpoolresistance13 with dissolve
mc "Focus, FOCUS!"
if mcresistance == 1:
    call ResistancePlus from _call_ResistancePlus_1
    mc "Finally, I've acquired Super-Resistance Level 02! Now I need to USE IT!"
if mcresistance == 0:
    call ResistancePlus from _call_ResistancePlus_2
    mc "Finally, I've acquired Super-Resistance! Now I need to USE IT!"
call screen usepower("useresistance", "MilfSaunaNoResistance", "MilfSaunaResistance") with dissolve

label MilfSaunaNoResistance:
scene milfpoolresistance13b with dissolve
play sound "sounds/radiation02.mp3"
mc "Oh no, my player wants me to DIE for some sadistic reasons!"
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label MilfSaunaResistance:
$ usedresistance += 1
play sound "sounds/mangrunt01.mp3"
mc "It's working! I can feel the heat escaping through my dong!"
scene milfpoolresistance14 with dissolve
cm "Hurry up, my skin..."
mc "I'll turn the heat down now, Captain MILF, hang in there!"
scene milfpoolresistance15 with dissolve
mc "Damn, it's not enough, there's too much steam inside the sauna cabin. I need to break this strong glass window!"
scene milfpoolresistance16 with dissolve
play sound "sounds/brokenglass.mp3"
mc "Fortunately, I'm SUPER-STRONG!" 
scene milfpoolresistance17 with dissolve
mc "I'll get you out of this steaming sauna, Captain MILF!"
scene milfpoolresistance18 with dissolve
cm "I'm feeling... BETTER. My Super-Resistance is back up and running! I hope my breasts weren't too damaged..."
scene milfpoolresistance19 with dissolve
mc "Let me check that for you..."
play sound "sounds/kiss.mp3"
cm "Oooh, what are you doing, naughty boy?"
scene milfpoolresistance20 with dissolve
play sound "sounds/moan04.ogg"
mc "Just checking that everything is functional..."
scene milfpoolresistance21 with dissolve
play sound "sounds/kiss.mp3"
cm "And?..."
mc "It all seems to be, Captain MILF..."
cm "You're making me so horny, I need to go back to my bedroom and REALLY cool down..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main