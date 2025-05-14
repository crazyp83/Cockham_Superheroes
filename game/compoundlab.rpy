label Level02lab:
$ mclevel02 = True
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene lab01 with fade
cm "Well, there it is, my Superhero radiation device that I built!"
sg "And what is this machine over there in the corner?"
cm "It's a computer. It has over one KILObyte of memory!"
sg "Wow, that sounds like a LOT!"
mc "Pfff..."
scene lab02 with dissolve
cm "I know, isn't it amazing what recent technological advances have achieved? Who would have thought just a few years ago that we would get a computer with over one KILObyte of memory..."
mc "Computers will never replace Superheroes!"
scene lab03 with dissolve
cm "Before we begin, I need to fix a few things on this machine. It's been slowly falling apart since the last time it was used..."
mc "That doesn't inspire confidence!"
cm "Just get undressed over there in the corner, sweetie pie. You need to be naked before the transformation, remember?"
scene lab04 with dissolve
sg "You're sure you don't need help, Captain MILF? I could just fly up there and fix it for you?"
cm "Thank you for the offer but I'd rather you help me by pressing the right buttons on the computer."
scene lab05 with dissolve
cm "Now lower the plasma generator so I can bang on it with a hammer."
play sound "v031/hammer.mp3"
cm "There, perfect, thank you Linda!"
scene lab06 with dissolve
stop sound
cm "Now you can bring it back up, I'm pretty sure it's fixed."
mc "I'm done getting butt-naked! Where should I stand, Captain MILF?"
scene lab07 with dissolve
cm "Oh dear, I'm getting dizzy from the height and I should also not look at [hero]'s big fat dong..."
mc "Supergirl here thinks it's beautiful, and rightfully so!"
sg "I never said that! It's... an ugly, wrinkly useless piece of dangling flesh!"
scene lab08 with dissolve
cm "Just let me get down and take the ladder away while I DON'T look at you and stand in the middle of the platform, sweetie pie."
mc "Alright, Carol! With my beautiful, big, fat schlong, proudly displayed to the radiations it's going to receive!"
sg "Pfff. I hope it gets SMALLER because of it, that would teach him a lesson!"
scene lab09 with dissolve
cm "Now, are you standing in the middle of the platform, [name]?"
mc "Yes. I am READY. Bring it on! Level 2, here we..."
scene lab11 with dissolve
play channel1 "sounds/radiation02.mp3"
mc "...go! What the?"
scene lab12 with dissolve
mc "Err... It's starting to heat up a little bit here..."
cm "It's normal, don't you remember from the first time?"
scene lab13 with dissolve
play sound "sounds/magic.mp3"
mc "AAAH! It's... BURNING!"
sg "He's GROWING, I can tell!"
scene lab14 with dissolve
stop channel1
play sound "sounds/winning.mp3"
mc "FUCK YEAH!"
call StudPlus from _call_StudPlus
mc "Alright! But wait, there's more!"
show extrapowermenu at extrapowermenupos
if mcsenses <= 1:
    show supersenses at extrapowerpos01
    show textsenses at extrapowertextpos01
if mccombat <= 1:
    show supercombat at extrapowerpos02
    show textcombat at extrapowertextpos02
if mcresistance <= 1:
    show superresistance at extrapowerpos03
    show textresistance at extrapowertextpos03
if mcagility <= 1:
    show superagility at extrapowerpos04
    show textagility at extrapowertextpos04

call screen level02extrapower()
screen level02extrapower():
    modal True
    if mcsenses <= 1:
        button:
            xpos 1600
            ypos 200
            xysize(80, 80)        
            action Jump ("ExtraSenses")
    if mccombat <= 1:
        button:
            xpos 1600
            ypos 400
            xysize(80, 80)        
            action Jump ("ExtraCombat")
    if mcresistance <= 1:
        button:
            xpos 1600
            ypos 600
            xysize(80, 80)        
            action Jump ("ExtraResistance")
    if mcagility <= 1:
        button:
            xpos 1600
            ypos 800
            xysize(80, 80)        
            action Jump ("ExtraAgility")

label ExtraSenses:
scene lab14
call SensesPlus from _call_SensesPlus_1
jump Level02labNext

label ExtraCombat:
scene lab14
call CombatPlus from _call_CombatPlus
jump Level02labNext

label ExtraResistance:
scene lab14
call ResistancePlus from _call_ResistancePlus_3
jump Level02labNext

label ExtraAgility:
scene lab14
call AgilityPlus from _call_AgilityPlus

label Level02labNext:
scene lab15 with dissolve
mc "Behold, my slightly enhanced NEW body!"
sg "Noticeably bigger and taller, but you were very muscular to begin with. But the fact that you're sporting a MASSIVE hardon is just DISGUSTING, [name]!"
cm "Oh my God, he's so...BIG... I shouldn't look but I can't stare away..."
scene lab16 with dissolve
sg "Captain MILF, what's going on, are you feeling alright?"
cm "His... HUGE... HARD... cock! It's making me lose all my Superpowers..."
sg "[name], do something about it! Hide that... thing away!"
scene lab17 with dissolve
mc "I'll try, but that extra power is making me so fucking HORNY! I can hide behind her so she doesn't see me is all at this stage..."
sg "Well, do that at least!"
cm "The compound... I can't defend it... Without my Superpowers..."
scene lab18 with dissolve
mc "Okay, I'll hold her up from behind, trying to make sure my monstercock doesn't get in the way... Ooops, sorry about that Carol..."
sg "Now, what was the sequence she entered... Yes, I think I remember!"
scene lab19 with dissolve
mc "Hey, where are you going? And why are you getting naked?"
sg "If I get STRONGER, I could defend the compound like TWO Superheroes!"
mc "I can defend the compound on my own, but that's not the point! We need to help Captain MILF recover her superpowers!"
scene lab20 with dissolve
sg "I want to get bigger, I NEED to get bigger! So I can compete with Powergirl!"
play channel1 "v031/radiation01.mp3"
play channel2 "sounds/coldwind.mp3"
scene lab21:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with dissolve
sg "Come to me, body-enhancing radiations!"
scene lab22 with dissolve
play sound "v031/spark.mp3"
mc "Uh oh, that doesn't sound good, come back down Supergirl!"
sg "NO! I don't care, I can feel.... My body... burning and... GROWING!"
scene lab23 with dissolve
play sound "sounds/thunder.mp3"
sg "AAAAH!"
mc "You're gonna get electrocuted!"
play sound "sounds/moan05.mp3"
sg "No, I'm... FINE... I FEEL STRONGER ALREADY!"
scene lab24 with dissolve
mc "Damn, Linda, you're growing... pretty damn BIG!"
play sound "sounds/thunder.mp3"
sg "AAAH!"
scene lab25 with dissolve
stop channel2
sg "YES!!! Now, I'm even BIGGER than Powergirl, even MORE MUSCULAR than Captain MILF!"
mc "And that's not gonna make me lose my hardon, that's for sure..."
scene lab26 with dissolve
stop channel1
sg "Look at those BIG, STRONG tits! I could SMOTHER my enemies with them now!"
mc "Let's go back to my room, I need to...err...find new clothes and revive Captain MILF."

scene mcroomsex01 with fade
stop music
play music "sounds/sexy04.mp3"
cm "Oh... Where am I? It's you, sweetie pie?"
mc "Yes Carol, you fainted when...err... I came out of your radiation machine."
scene mcroomsex02 with dissolve
cm "And why is Supergirl so... BIG???"
mc "She also entered the machine. I told her not to but..."
play sound "sounds/moan02.mp3"
sg "Look, I can flex my biceps into BOULDERS OF MUSCLE!"
scene mcroomsex03 with dissolve
sg "And I just can't keep my eyes off my new enhanced SUPER-BOOBS!"
mc "Neither can I... I still have a massive aching hardon..."
scene mcroomsex04 with dissolve
cm "I need to take my top off, I'm still all flushed..."
mc "I can give you a nice massage to help you recover your superpowers."
scene mcroomsex05 with dissolve
cm "That would be lovely, sweetie pie! Let me get some nice cushion so I can lie down comfortably on the bed."
scene mcroomsex06 with dissolve
cm "I'm ready! And looking the other way so I don't see your huge... thingie."
mc "I'll try and keep it out of the way but damn! It's at least three inches bigger than it used to be!"
play sound "sounds/moan03.mp3"
cm "THREE INCHES? Ooohhh...."
scene mcroomsex07 with dissolve
cm "Mmh, that's nice, sweetie pie..."
scene mcroomsex08 with dissolve
mc "Your buns are just so... amazingly tight, Captain MILF!"
cm "I can crush a walnut between my cheeks."
mc "Right, err... You'll have to show me that one day."
scene mcroomsex09 with dissolve
mc "In the meantime..."
play sound "sounds/moan02.mp3"
cm "Oooh, what are you doing, naughty boy?"
mc "Massaging the INSIDE of your snatch. It needs to dilate quite a bit, considering my NEW size."
cm "Are you planning on... fucking your landlady with your monster cock?"
mc "I can't say it didn't cross my mind."
scene mcroomsex10 with dissolve
play sound "sounds/moan01.mp3"
cm "That was VERY good, my lovely tenant... Now it is MY turn to show my appreciation."
scene mcroomsex11a with dissolve
play sound "sounds/gasp.mp3"
cm "Oh my dear Lord! You HAVE grown quite a bit, haven't you, sweetie pie?"
mc "Yes, and I'm so hard, it's literally aching!"
sg "It's...even more beautiful that before..."
scene mcroomsex12 with dissolve
cm "I think I should test your level 2 Super-Studliness power before... you use it badly on someone."
mc "Why would I use it badly?"
cm "I sense that you are... still hesitant about where you stand..."
if evilness >= 13:
    mc "Has Wonder Woman said anything?"
    cm "About what?"
    mc "Err... nothing. Let's do it, Carol, I'm still sporting a giant hardon for you!"
if evilness <= 12:
    mc "I'm a Superhero and I'll prove it to you. With my Super-Cock!"
    call Good from _call_Good_9
scene mcroomsex13 with dissolve
cm "I can see that, sweetie pie... Show me how you please a woman with that giant pecker!"
mc "Oh God, this is about to get real HOT!"
scene mcroomsex18 with dissolve
mc "Fuck, I'm just so fucking HUGE for you, Captain MILF!"
cm "I can't even watch, I fear I might faint again seeing your behemoth plowing through my love canal..."
scene mcroomsex19a with dissolve
play sound "sounds/thud.mp3"
mc "Can you feel how HEAVY it is Carol?"
play channel2 "sounds/moan02.mp3"
window hide
scene mcroomsex19b with dissolve
$ renpy.pause(.8, hard='True')
play channel1 [ "sounds/thud.mp3", "<silence .9>"]
scene milfcockslap
pause
cm "Oh God... It's the BIGGEST piece of [age]-yo boymeat on Earth, sweetie pie! Just Give it to me, I WANT IT!"
stop channel1
stop channel2
scene mcroomsex20 with dissolve
play sound "sounds/moan06.ogg"
mc "I'll make you recover your superpowers by giving you my Super-Cock!"
$ milfmassagetalkslow = True

label MILFMassageSlow:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfast = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslow == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslow = True
window hide
show milfmassageslowvideo behind milfmassagepovslowvideo
show milfmassageslowvideo behind milfmassagefastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovslowvideo
hide milfmassagefastvideo
with dissolve

show faster:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milfmassageslow()
screen milfmassageslow():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageFast")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVSlow")

label MILFMassageFast:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfast == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfast = True
window hide
show milfmassagefastvideo behind milfmassagepovfastvideo
show milfmassagefastvideo behind milfmassageslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagepovfastvideo
hide milfmassageslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 800     
show pov:
     xpos 50 ypos 800     
call screen milfmassagefast()
screen milfmassagefast():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEnd")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVFast")

label MILFMassagePOVSlow:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfast = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslow == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslow = True
window hide
show milfmassagepovslowvideo behind milfmassageslowvideo
show milfmassagepovslowvideo behind milfmassagepovfastvideo
$ renpy.pause(1.0, hard='True')
hide milfmassageslowvideo
hide milfmassagepovfastvideo
with dissolve
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfmassagepovslow()
screen milfmassagepovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageSlow")

label MILFMassagePOVFast:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfast == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfast = True
window hide
show milfmassagepovfastvideo behind milfmassagefastvideo
show milfmassagepovfastvideo behind milfmassagepovslowvideo
$ renpy.pause(1.0, hard='True')
hide milfmassagefastvideo
hide milfmassagepovslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfmassagepovfast()
screen milfmassagepovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageFast")

label MILFMassageEnd:
hide cum
hide faster
hide slower
hide pov
hide sceneicon
play sound "sounds/moan05.mp3"
cm "Sweetie, I... PLEASE CUM INSIDE ME, YOU STALLION!"
mc "I wonder if my loads have also increased in..."
stop channel2
scene mcroomsex21 with dissolve
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boyorgasm01.mp3"
mc "...size. AAAAH! Here it comes!"
window hide
with fastflash
mc "And it feels so fucking good!"
scene mcroomsex22 with dissolve
cm "Oh dear me, is that still the same shot? You've been pumping your seed for so long already, sweetie pie!"
window hide
with hpunch
mc "Oh Fuck, can't stop NU-UU-TTING!!"
scene mcroomsex23 with dissolve
cm "Maybe you should dump the rest on me, I'm starting to feel a bit... bloated with your young spunk!"
window hide
with fastflash
mc "Oh damn, alright, gonna try and pull it out while I'm still spewing my sauce, RHAAAA!"
scene mcroomsex24 with dissolve
stop channel2
if age >= 20:
    cm "Oh my goodness, you're splattering your potent goo all over my body!"
if age >= 18 and age <= 19:
    cm "Oh my goodness, you're splattering your potent teenage goo all over my body!"
window hide
with fastflash
cm "Give me more [name], DROWN ME IN YOUR SWEET CUM!"
scene mcroomsex25 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE YOU GO CAROL, AAAHHH!"
window hide
with fastflash
sg "This is crazy! He's coming like a FIREHOSE!"
scene mcroomsex26 with dissolve
play sound "sounds/panting.mp3"
play channel2 "sounds/splooge02.mp3"
cm "You came so much inside me, sweetie pie... Oooh..."
mc "Damn, I can see that..."
scene mcroomsex27 with dissolve
play sound "sounds/lick02.mp3"
cm "Why don't you come and help me clean up this cummy mess, Linda?"
scene mcroomsex28 with dissolve
stop channel2
sg "But... This is so lewd! He's my distant cousin!"
cm "So? It's not incest, you're way TOO distant. And you've been a NAUGHTY girl testing my machine without my authorization!"
sg "Uh... Alright, Captain MILF."
scene mcroomsex30 with dissolve
play sound "sounds/lick01.ogg"
cm "There you go, slurp his cum slowly... And lick my giant MILF funbags..."
scene mcroomsex31 with dissolve
play sound "sounds/lick02.mp3"
sg "*slurp *  He's made such a MESS!"
cm "That's why you have to be thorough... My pussy is DRIPPING with his spunk."
scene mcroomsex32 with dissolve
play channel2 "sounds/lick03.mp3"
play sound "sounds/moan03.mp3"
cm "Yes, just like that! AAAH!"
mc "Damn, I'm getting HARD again! Actually, I didn't even lose my MONSTER erection, but now I feel like I NEED to FUCK some MORE!"
scene mcroomsex33 with dissolve
stop channel2
cm "Lick my fingers clean Linda, I think [name] is about to give you something BIG to eat!"
play sound "sounds/lick03.mp3"
scene mcroomsex34 with dissolve
sg "What? Gggllll...."
mc "You'd better open up REAL WIDE distant cuz, show me that you DESERVE this dick!"
scene mcroomsex35 with dissolve
mc "Yeah, that's better... My knobhead just fits PERFECTLY inside your tiny cock-hungry mouth, doesn't it?"
sg "* Gllbbbb.... *"
cm "Now sweetie, be gentle when you POUND her face with your giant HORSEDICK!"
play channel1 "sounds/blow01.mp3"

label LindaDeepThroatSlow:
hide slower
hide faster
hide cum
show lindasuckslowvideo behind lindasuckfastvideo
$ renpy.pause(1.0, hard='True')
hide lindasuckfastvideo
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen lindasuckslow()
screen lindasuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEnd")

label LindaDeepThroatFast:
show lindasuckfastvideo behind lindasuckslowvideo
hide cum
hide faster
hide slower
mc "That throat is so warm, I think I'm going to face-fuck you FASTER, whether you're ready or not!"
sg "* gllur *"
hide lindasuckslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500

call screen lindasuckfast()
screen lindasuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEnd")

label LindaDeepThroatEnd:
hide nexticon
hide slower
hide faster
cm "Sweetie, I think she's struggling a bit, you'd better give it a rest. We'll lick your dong for you. BOTH OF US."
mc "Alright, that sounds like a good deal!"
stop channel1
scene supthroatpost01 with dissolve
play sound "v031/cough.mp3"
cm "Are you alright, Linda?"
sg "I can't... feeel my jaw...."
mc "Well, use your tongue instead then. On my knob."
scene supthroatpost02 with dissolve
play sound "sounds/kiss.mp3"
sg "Mmmh, it's so BEAUTIFUL! I want to lick it all over!"
cm "Me too, I'm totally under its spell right now..."
play channel1 "sounds/lick01.ogg"
scene massagelickthreesomevideo with dissolve
$ renpy.pause(1.0, hard='True')
mc "Mmh, two warm tongues... I'm in heavens!"
pause
cm "Just wait till you start FUCKING our pussies in unison, that will be TRUE heavens!"
scene supthroatpost03 with dissolve
stop channel1
mc "Oooh, wow, where do I sign up?"
cm "You can sign up very soon, sweetie pie. Let us worship that HUMONGOUS dong a bit more first... Especially Linda, she seems ENTRANCED by it!"
scene doublethroatsup with dissolve
play channel1 [ "sounds/blow02.mp3", "<silence .9>"]
pause
scene supthroatpost02 with dissolve
stop channel1
play sound "sounds/kiss.mp3"
cm "I think we're ready. Let us lign up our fuckholes for your great big whopper!"
scene dpprefuck01 with dissolve
mc "Are you ready to receive my mighty love muscle, Captain MILF?"
cm "Yes, sweetie pie. We're going to make you cum so many times that it will finally go down and I won't be under its gorgeous spell..."
scene dpprefuck02 with dissolve
play sound "sounds/moan05.mp3"
cm "OOOH! I can already feel your apple-sized helmet STRETCHING my pussylips... Be careful with that thing, [name]!"
$ milfdptalk01slow = True
$ supdptalk01slow = True

label DoubleFuckNoMilfSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slow == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slow = True
window hide
show doublefuckslowvideo behind doublefuckfastvideo
show doublefuckslowvideo behind doublefuckslowpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckslowpovvideo
hide doublefuckfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkfirst == False:
    if age >= 20:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milfdptalkfirst = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknomilfslow()
screen doublefucknomilfslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlow") 

label DoubleFuckNoMilfFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fast == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fast = True
window hide
show doublefuckfastvideo behind doublefuckslowvideo
show doublefuckfastvideo behind doublefuckfastpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckfastpovvideo
hide doublefuckslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknomilffast()
screen doublefucknomilffast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfPOVFast") 

label DoubleFuckNoMilfPOVSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slow == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slow = True
window hide
show doublefuckslowpovvideo behind doublefuckfastpovvideo
show doublefuckslowpovvideo behind doublefuckslowvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckfastpovvideo
hide doublefuckslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknomilfpovslow()
screen doublefucknomilfpovslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSlow") 

label DoubleFuckNoMilfPOVFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fast == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fast = True
window hide
show doublefuckfastpovvideo behind doublefuckslowpovvideo
show doublefuckfastpovvideo behind doublefuckfastvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckslowpovvideo
hide doublefuckfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknomilfpovfast()
screen doublefucknomilfpovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfFast") 

label DoubleFuckNoSupSwitch:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupslowvideo
if talkedswitchsup == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    cm "As long as you come back to cum inside me, sweetie pie!"
    $ talkedswitchsup = True
window hide
show doublefuckmilfswitchvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupslowvideo behind doublefuckmilfswitchvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchvideo
hide doublefuckmilfswitchvideo
if supdptalkfirst == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirst = True
window hide
$ supdptalk01slow = True
jump DoubleFuckNoSupSlow

label DoubleFuckNoMilfSwitch:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckslowvideo
if talkedswitchmilf == False:
    mc "I'm gonna switch for a while and ram my shaft inside Captain MILF's pussy again!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilf = True
window hide
show doublefucksupswitchvideo
$ renpy.pause(0.6, hard='True')
show doublefuckslowvideo behind doublefucksupswitchvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchvideo
hide doublefucksupswitchvideo
$ milfdptalk01slow = True
jump DoubleFuckNoMilfSlow

label DoubleFuckNoSupSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slow == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slow = True
window hide
show doublefucksupslowvideo behind doublefucksupfastvideo
show doublefucksupslowvideo behind doublefucksupslowpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupslowpovvideo
hide doublefucksupfastvideo
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknosupslow()
screen doublefucknosupslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlow") 

label DoubleFuckNoSupFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fast == False:
    sg "You want to really pound my new Super-Pussy with your [age]-yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fast = True
window hide
show doublefucksupfastvideo behind doublefucksupslowvideo
show doublefucksupfastvideo behind doublefucksupfastpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupfastpovvideo
hide doublefucksupslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknosupfast()
screen doublefucknosupfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupPOVFast") 

label DoubleFuckNoSupPOVSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slow == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slow = True
window hide
show doublefucksupslowpovvideo behind doublefucksupfastpovvideo
show doublefucksupslowpovvideo behind doublefucksupslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupfastpovvideo
hide doublefucksupslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknosuppovslow()
screen doublefucknosuppovslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSlow") 

label DoubleFuckNoSupPOVFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fast == False:
    sg "You want to really pound my new Super-Pussy with your [age]-yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fast = True
window hide
show doublefucksupfastpovvideo behind doublefucksupslowpovvideo
show doublefucksupfastpovvideo behind doublefucksupfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupslowpovvideo
hide doublefucksupfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucknosuppovfast()
screen doublefucknosuppovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupFast") 

label DoubleFuckNoMilfCum:
$ milfdptalk01slow = True
$ dpmilfcame += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "I feel like I'm ready to blow a load, Captain MILF!"
cm "Then pump your seed inside me [name]!"
scene dpmilfnocum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene dpmilfnocum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene dpmilfnocum03 with dissolve
stop channel1
mc "There you go, Captain MILF, RHOOO!"
window hide
with fastflash
sg "He's really cumming like a STALLION!"
scene dpmilfnocum04 with dissolve
mc "Still more shots BLASTING, RHAAA!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
scene dpmilfcum05 with dissolve
mc "Getting back in that tight snatch of yours, Captain MILF!"
cm "Damn, you're still raring to go! How are we going to TAME your BEAST?"
stop channel2
jump DoubleFuckMilfSlow

label DoubleFuckNoSupCum:
$ supdptalk01slow = True
$ dpsupcame += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
sg "Your cock... It's becoming even BIGGER inside my pussy!"
mc "That's cos I'm about to blow another load!"
scene dpsupnocum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boymoan05.mp3" 
mc "AAAAH!"
window hide
with hpunch
sg "You're pumping so much spunk inside me, aaah!"
scene dpsupnocum02 with dissolve
play sound "sounds/boymoan04.mp3" 
mc "There's more where that came from, RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
if dpsupcame == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcame >= 1:
    sg "I'm getting BLOATED again by your MONSTER LOAD, you just cum like a FIREHOSE!"
scene dpsupnocum03 with dissolve
play sound "sounds/boymoan03.mp3" 
mc "Endless supplies of young, virile cum from THIS Super-Stud!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
sg "Don't stop, keep cumming, AAAH, I'm gonna squirt!"
window hide
with fastflash
mc "There you go, the last few shots just for you, Supergirl!"
window hide
with fastflash
stop channel2
if dpmilfcame >= 2 and dpsupcame >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEnd
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcame == 0:
    jump DoubleFuckNoSupSlow
jump DoubleFuckSupSlow

label DoubleFuckMilfSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slow == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slow = True
window hide
show doublefuckcumslowvideo behind doublefuckcumfastvideo
show doublefuckcumslowvideo behind doublefucksupcumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovslowvideo
hide doublefuckcumfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkcumfirst == False:
    if age >= 20:
        cm "You just came and you're STILL hard? My tenant is such a STALLION!"
    if age >= 18 and age <= 19:
        cm "You just came and you're STILL hard? My tenant is such a TEENAGE STALLION!"
        $ milfdptalkcumfirst = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefuckmilfslow()
screen doublefuckmilfslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlow") 

label DoubleFuckMilfFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fast == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fast = True
window hide
show doublefuckcumfastvideo behind doublefuckcumslowvideo
show doublefuckcumfastvideo behind doublefucksupcumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovfastvideo
hide doublefuckcumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefuckmilffast()
screen doublefuckmilffast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfPOVFast") 

label DoubleFuckMilfPOVSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slow == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slow = True
window hide
show doublefuckcumpovslowvideo behind doublefuckcumpovfastvideo
show doublefuckcumpovslowvideo behind doublefuckcumslowvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckcumpovfastvideo
hide doublefuckcumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefuckmilfpovslow()
screen doublefuckmilfpovslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSlow") 

label DoubleFuckMilfPOVFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fast == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fast = True
window hide
show doublefuckcumpovfastvideo behind doublefuckcumpovslowvideo
show doublefuckcumpovfastvideo behind doublefuckcumfastvideo
$ renpy.pause(1.0, hard='True')    
hide doublefuckcumpovslowvideo
hide doublefuckcumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefuckmilfpovfast()
screen doublefuckmilfpovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfFast")

label DoubleFuckSupSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slow == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slow = True
if supdptalkcumfirst == False and dpsupcame >= 1:
    sg "You're fucking me again! In my already cum-filled pussy... Mmmh, this is so good!"
    mc "It's so slippery with my spunk now, I can pound away even deeper!"
    $ supdptalkcumfirst = True
window hide
show doublefucksupcumslowvideo behind doublefucksupcumfastvideo
show doublefucksupcumslowvideo behind doublefucksupcumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovslowvideo
hide doublefucksupcumfastvideo
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucksupslow()
screen doublefucksupslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlow") 

label DoubleFuckSupFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fast == False:
    sg "You want to really pound my new Super-Pussy with your [age]-yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fast = True
window hide
show doublefucksupcumfastvideo behind doublefucksupcumslowvideo
show doublefucksupcumfastvideo behind doublefucksupcumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovfastvideo
hide doublefucksupcumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucksupfast()
screen doublefucksupfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupPOVFast") 

label DoubleFuckSupPOVSlow:
$ milfdptalk01fast = False
$ supdptalk01fast = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slow == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slow = True
window hide
show doublefucksupcumpovslowvideo behind doublefucksupcumpovfastvideo
show doublefucksupcumpovslowvideo behind doublefucksupcumslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovfastvideo
hide doublefucksupcumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucksuppovslow()
screen doublefucksuppovslow():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSwitch")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSlow") 

label DoubleFuckSupPOVFast:
$ milfdptalk01slow = False
$ supdptalk01slow = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fast == False:
    sg "You want to really pound my new Super-Pussy with your [age]-yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fast = True
window hide
show doublefucksupcumpovfastvideo behind doublefucksupcumpovslowvideo
show doublefucksupcumpovfastvideo behind doublefucksupcumfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefucksupcumpovslowvideo
hide doublefucksupcumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefucksuppovfast()
screen doublefucksuppovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupFast")

label DoubleFuckSupSwitch:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupcumslowvideo
if talkedswitchsupcum == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    if dpmilfcame <= 1:
        cm "As long as you give me another BIG load, sweetie pie!"
    if dpmilfcame >= 2:
        cm "Alright-ee, sweetie pie. You already gave your landlady so many MASSIVE cumloads!"
    $ talkedswitchsupcum = True
window hide
show doublefuckmilfswitchcumvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupcumslowvideo behind doublefuckmilfswitchcumvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchcumvideo
hide doublefuckmilfswitchcumvideo
if supdptalkfirst == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirst = True
window hide
$ supdptalk01slow = True
jump DoubleFuckSupSlow

label DoubleFuckMilfSwitch:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckcumslowvideo
if talkedswitchmilfcum == False:
    mc "I'm gonna switch for a while and dip my dong inside Captain MILF's snatch!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilfcum = True
window hide
show doublefucksupswitchcumvideo
$ renpy.pause(0.6, hard='True')
show doublefuckcumslowvideo behind doublefucksupswitchcumvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchcumvideo
hide doublefucksupswitchcumvideo
$ milfdptalk01slow = True
jump DoubleFuckMilfSlow

label DoubleFuckMilfCum:
$ milfdptalk01slow = True
$ dpmilfcame += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "Gonna cum again, Captain MILF, I can feel it!"
cm "Then pump your seed inside me and all over my back [name]!"
scene dpmilfcum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene dpmilfcum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene dpmilfcum03 with dissolve
stop channel1
mc "There you go, Captain MILF, RHOOO!"
window hide
with fastflash
sg "He's really cumming like a STALLION!"
scene dpmilfcum04 with dissolve
mc "Still more shots BLASTING, RHAAA!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
if dpmilfcame >= 2 and dpsupcame >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEnd
scene dpmilfcum05 with dissolve
mc "Getting back in that tight snatch of yours, Captain MILF!"
cm "Damn, you're STILL raring to go? How are we going to TAME your BEAST?"
stop channel2
jump DoubleFuckMilfSlow

label DoubleFuckSupCum:
$ supdptalk01slow = True
$ dpsupcame += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
sg "Your cock... It's becoming even BIGGER inside my pussy!"
mc "That's cos I'm about to blow another load!"
scene dpsupcum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boymoan05.mp3" 
mc "AAAAH!"
window hide
with hpunch
sg "You're pumping so much spunk inside me, aaah!"
scene dpsupcum02 with dissolve
play sound "sounds/boymoan04.mp3" 
mc "There's more where that came from, RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
if dpsupcame == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcame >= 1:
    sg "I'm getting BLOATED again by your MONSTER LOAD, you just cum like a FIREHOSE!"
scene dpsupcum03 with dissolve
play sound "sounds/boymoan03.mp3" 
mc "Endless supplies of young, virile cum from THIS Super-Stud!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
sg "Don't stop, keep cumming, AAAH, I'm gonna squirt!"
window hide
with fastflash
mc "There you go, the last few shots just for you, Supergirl!"
window hide
with fastflash
stop channel2
if dpmilfcame >= 2 and dpsupcame >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEnd
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcame == 0:
    jump DoubleFuckNoSupSlow
jump DoubleFuckSupSlow

label DoubleFuckEnd:
stop channel2
play sound "sounds/panting.mp3"
scene doublefuckend01 with dissolve
mc "That's it, I think you girls finally drained me... After I came over 5 MEGA-LOADS..."
if age >= 18:
    sg "I still can't believe a man can cum so many times in a row and never lose his hardon... Uuuhhhh...."
scene doublefuckend02 with dissolve
cm "Your landlady is very proud of you, [name]. You've definitely MASTERED Level02 Super-Studliness! * slurp *"
scene doublefuckend03 with dissolve
play sound "sounds/moan03.mp3"
sg "My pussy is so full of warm cream... Mmhhh..."
scene doublefuckend02 with dissolve
cm "Now I'd better go back to my room and clean up before some Super-Villains attack the compound."
scene doublefuckend04 with dissolve
mc "With my new BIGGER muscles, I could defeat anyone that dares set foot in our compound, Captain MILF!"
cm "Yeah, I know, you're VERY muscular my young tenant... But you're still only Super-Strength level 02. Superman is less muscular than you but he's STRONGER..."
mc "Pff! I'll become STRONGER than this wimp in no time, mark my words!"
scene doublefuckend05 with dissolve
sg "What's going on? My body... It's getting smaller! NOOOOOO!"
scene doublefuckend06 with dissolve
cm "Did you press ctrl+alt+Shift+F8 before hitting Enter?"
sg "Ctrl+alt+WHAT???"
cm "Ctrl+alt+Shift+F8. It's required to make the radiation-induced body enhancements permanent. You must have forgotten to press it, thanks God."
cm "Now you'll become the sweet little girl I've always known you as again."
scene doublefuckend07 with dissolve
sg "But I DON'T WANT TO! * sob *"
mc "Look on the bright side. Your costume will fit you again and you can fly back to Smallville without the hassle of finding a new one."
sg "I HATE YOU!"
$ usedstudliness += 1
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main