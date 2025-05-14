label SirensClub:
play music "sounds/barmusic.mp3"
jump SirensDay
#if period == 1:
#    jump SirensNight
    
label SirensDay:
if seenbarbarastrip:
    scene sirensbaranim with fade
    if seentabitha == False:
        mc "I guess I'll go and talk to the barmaid, since no one else is around..."
        jump TabithaBar
    if seentabitha and seentabithastrip == False:
        mc "I guess I'll go and talk to Tabitha again, since no one else is around..."    
        jump TabithaBar
    if seentabitha and seentabithastrip:
        pass
scene sirensbaranim with fade
show keensirens01
with dissolve
if period == 0:
    bk "[hero]... What brings you here? To MY PRIVATE club?"
if period == 1:
    bk "[hero]... What brings you here? To MY PRIVATE club? In the only evening during the week when we are closed?"
label SirensBarbaraDialogues:
menu:
    "You are a prime suspect in a...err... forced chastity case." if mission03 and mission03end == False and spokebarbaramission03 == False:
        hide keensirens01
        show keensirens02
        with fastdissolve
        bk "Who was \"forced into chastity\"? A man or a woman?"
        mc "Well, a woman obviou..."
        hide keensirens02
        show keensirens06
        with fastdissolve
        bk "Then I have nothing to do with that. No further comment."
        mc "Hang on hang on, you're still a prime suspect! As Mayor Krass's ex-lover!"
        hide keensirens06
        show keensirens03
        with fastdissolve
        bk "How dare you utter this... man's name here! And you said a woman anyway! What does this have to do with HIM?"
        mc "His daughter. You put that chastity belt on her to punish him didn't you? Come on, admit it, Barbara Keen!"
        hide keensirens03
        show keensirens01
        with fastdissolve
        bk "I admit I am a Super-Villainess. And I also admit I am THIS CLOSE to summoning my legion of sex assassins and UNLEASHING them on you if you continue that ridiculous line of inquiry!"
        mc" Ah, Ok. Maybe you're innocent after all then. Sorry for the bother."
        hide keensirens01
        show keensirens05
        with fastdissolve
        bk "GET OUT OF HERE!"
        $ spokebarbaramission03 = True
        mc "Damn, if it's not her, who might it be then? Maybe I should check the hints on the quest screen... *"
        jump Main
    "I'd like to become a member of your PRIVATE club.":
        hide keensirens01
        show keensirens04
        with fastdissolve
        bk "Well, you can't. It's reserved for my RICH clientele. Last time I checked, you have NO MONEY."
        mc "Is Bruce Vayne a member of your club?"
        hide keensirens04
        show keensirens06
        with fastdissolve
        bk "I don't divulge the list of my PRIVATE members, [hero]."
        mc "Gee, conversation is really tough with you."
        hide keensirens06
        show keensirens01
        with fastdissolve
        jump SirensBarbaraDialogues        
    "What exactly goes on around here? I bet it's SEX CRIME, isn't it? You're DONE FOR Barbara Keen!" if seenbarbarastrip == False:
        hide keensirens01
        show keensirens02
        with fastdissolve
        bk "Are fancy stripclubs illegal?"
        mc "Err, no, but I don't see any strippers here. Is this place REALLY a stripclub? I wonder..."
        bk "Allow me to demonstrate to you, [hero]. So you will be CONVINCED that this place is nothing more than a very upscale adult entertainment private club..."
        mc "OK, how are you going to do that?"
        bk "Just sit here and WATCH."
        jump BarbaraStrip
    "This place looks dead. Business must be real BAD for you.":
        hide keensirens01
        show keensirens04
        with fastdissolve
        bk "It's the middle of the day. We open in the EVENINGS, [hero]."
        mc "Ah, that explains it then... Can I come in the evening?"
        hide keensirens04
        show keensirens06
        with fastdissolve
        bk "Only PRIVATE members can come when I'm open for business. So the answer is NO!"
        mc "Damn it."
        hide keensirens06
        show keensirens01
        with fastdissolve
        jump SirensBarbaraDialogues        
    "What's in the back room over there?":
        bk "Do you have a warrant?"
        mc "Err, no."
        hide keensirens01
        show keensirens06
        with fastdissolve
        bk "Then I'm not showing you. No further comment."
        mc "Gee, it was just an innocent question, really."
        hide keensirens06
        show keensirens01
        with fastdissolve
        jump SirensBarbaraDialogues
    "I heard you're having a big party here soon. I'd like a job as a waiter." if seentabithastrip and waitertrained == False:
        bk "Why? Is this a trick?"
        mc "Err, no. I just need the money is all."
        hide keensirens01
        show keensirens05
        with fastdissolve
        bk "You do realize that my rich clientele is VERY demanding. Especially my rich FEMALE clientele..."
        mc "What do you mean exactly?"
        hide keensirens05
        show keensirens02
        with fastdissolve
        bk "I think you know EXACTLY what I mean. And if you're not up to it, I won't hire you!"
        mc "* Prostitution is illegal, but... *"
        menu:
            "I get it and I'm willing to service your rich FEMALE clientele (+1 Super-VIllain)":
                call Evil from _call_Evil_11
                hide keensirens02
                show keensirens04
                with fastdissolve                
                bk "Let's see if you have what it takes to be a upscale waiter first... Tabitha, vive him his outfit to change into. And we'll get OUR outfits..."
                ta "Follow us to the back room, [hero]. And no sudden moves, or you KNOW what will happen..."
                jump WaiterTraining
            "No way! I won't mover myself to illegal gigolo status (no change)":
                hide keensirens02
                show keensirens06
                with fastdissolve                
                bk "Then goodbye, the party will be WITHOUT YOU!"
                jump Main
    "I'm done here.":
        bk "Good. DOn't bother coming back."
        jump Main

label BarbaraStrip:
$ seenbarbarastrip = True
stop music
play music "sounds/sexy07.mp3"
scene barbarastrip01 with dissolve
mc "* Damn... Hot strip just for ME! *"
scene barbarastrip02 with dissolve
$ renpy.pause(1.0, hard='True')
bk "My club is all about ELEGANCE and CLASS."
scene barbarastrip03 with dissolve
mc "I see..."
scene barbarastrip04 with dissolve
$ renpy.pause(2.0, hard='True')
bk "Nothing you will see here is ILLEGAL..."
scene barbarastrip05 with dissolve
mc "Let me be the judge of that. Carry on."
scene barbarastrip06:
    subpixel True
    ease 6.0 xoffset 0 yoffset -1320
with dissolve
$ renpy.pause(5.0, hard='True')
bk "This part of my strip routine is usually when heads start to turn..."
scene barbarastrip07 with dissolve
$ renpy.pause(2.0, hard='True')
mc "I can see why..."
scene barbarastrip08 with dissolve
$ renpy.pause(1.0, hard='True')
bk "So, are you convinced that there nothing but CLASSY, SEXY stripping going on in my establishment, [hero]?"
stop music
mc "I suppose. But I'll come back one day when you're least expecting me, just to check. And possibly see another routine."
jump Main

label TabithaBar:
if seentabitha and seentabithastrip == False:    
    scene tabithabar01 with dissolve
    ta "Ah, you're back. Still on the job and desperately trying to get valuable intel from me?"
    if mission03 and mission03end == False:
        mc "Yes, but my job is now a MISSION. And it's all very hush-hush. Can't say anything more."
        jump TabithaMission03
    mc "Yeah? That or seeing you doing a classy and elegant stripshow for me. You know, to practice for tonight."
    scene tabithabar02 with dissolve
    ta "And what makes you think I might be a stripper?"
    mc "You've got the smoking hot body for it, Tabitha..."
    ta "You really think so?"
    mc "Yes I do. Although you could offer me definitive PROOF."
    scene tabithabar04 with dissolve
    ta "Oh, you want PROOF? I'll give you PROOF!"
    mc "* Bingo! *"
    jump TabithaStrip
    
if seentabitha == False:    
    $ seentabitha = True
    scene tabithabar01 with dissolve
    ta "Welcome to the Sirens Club. [hero]."
    mc "Where's Barbara Keen? And who are you?"
    scene tabithabar04 with dissolve
    ta "Barbara Keen is not here. Clearly. And I'm Tabitha Gala-Vag. The barmaid. And assassin."
    mc "I see. That's an interesting mix."
    scene tabithabar02 with dissolve
    ta "I know, right? I named a drink after it. The \"Barman Murder\". Would you like to try it?"
    mc "No thanks, I don't drink on the job."
    scene tabithabar03 with fastdissolve
    ta "Oh, you're on the job, are you? And what \"job\" is that exactly?"

label TabithaBar02:

if mission03 and mission03end == False:
    mc "Right now, a secret job. It's all very hush-hush. Can't say anything more."
    if spokebarbaramission03:
        label TabithaMission03:
        scene tabithabar02 with dissolve
        ta "But it involves the Mayor's daughter, right?"
        mc "Err, yeah, possibly. Why? What do YOU know?"
        scene tabithabar03 with dissolve
        ta "I know you're wasting your time digging for answers HERE. You should look towards the Chinese Triad. They've been trying to infiltrate their agents all around town."
        scene tabithabar01 with dissolve
        ta "Including HERE. Do you know what happened to that agent?"
        mc "No. What happened?"
        scene tabithabar04 with dissolve
        ta "I killed her."
        mc "Err, alright. I guess that is a legitimate assassination in this case... Considering they are ALSO the bad guys. So I won't arrest you. This time."
        scene tabithabar02 with dissolve
        ta "How magnanimous of you. I was sssoooo scared for a moment."
        mc "Yeah, I'm... err... that kind of guy. Thank you for your time, I must go, busy busy. I'll walk softly towards the entrance. Without turning my back on you if you don't mind...."
        ta "I think that's a good idea indeed."
        jump Main

if mission03 == False or mission03end:
    mc "Right now, just getting to know the various neighborhoods. Where do Super-Villains hang out, what they're up to, and so forth, you know."
    scene tabithabar02 with dissolve
    ta "Are you trying to get me to reveal private stuff about Barbara Keen?"
    mc "Err, well, that would be helpful, yes. Yes, why not, thanks for offering, I'm listening."
    scene tabithabar03 with dissolve
    ta "You think you're funny?"
    mc "Ah, you're not falling for it, then?"
    scene tabithabar04 with dissolve
    ta "No I'm not. Now get out of here, I have to prepare cocktails for tonight's party. To which you're NOT invited."
    mc "I'll be back."
    jump Main

label TabithaStrip:
stop music
play music "sounds/bellydance.mp3"
$ seentabithastrip = True
scene tabithadance01 with dissolve
ta "In that case, I'll show you my belly-dancing routine... Even though I'm not wearing my proper costume for that..."
mc "Fine by me."
scene tabithadance02 with dissolve
ta "It's meant to be highly SENSUAL and EROTIC."
mc "So far so good, I must admit."
scene tabithadance03 with dissolve
ta "Really? You're not saying that just to please me?"
scene tabithadance04 with dissolve
mc "It comes from the bottom of my co... I mean, heart."
scene tabithadance05 with dissolve
ta "I'm glad you're enjoying, I have something SPECIAL for you at the end..."
mc "Ooh, I can't wait!"
scene tabithadance06 with dissolve
ta "It will TAKE YOUR BREATH AWAY..."
mc "Now we're talking!"
scene tabithadance07 with dissolve
ta "You won't soon forget what will happen to you..." 
scene tabithadance08 with dissolve
ta "So come closer, [hero], come and get your REWARD."
mc "I'm READY! Fuck YEAH!"
scene tabithadance09 with dissolve
mc "What the...?"
ta "Here's your REWARD, you dirty boy! You think you can Super-Seduce a trained assassin?"
mc "Well, err, I thought..."
scene tabithadance10 with dissolve
ta "Do you know what dagger this is?"
mc "A very sharp one, please stop pushing it against my beautiful baby-skin!"
ta "It's the dagger that killed Ra's Al-Ghul. It can cut through steel-plated armor like butter..."
mc "I'm not Ra's Al-Ghul! Please spare me, I have nothing to do with that dude, whoever he is!"
scene tabithadance09 with dissolve
ta "Don't fucking come back again to try and stir trouble in Barbara Keen's establishment, [hero]...."
mc "I won't, I won't, I promise!"
ta "Good. You may go...safely."
mc "* Damn, she's beautiful, nuts AND dangerous! *"
jump Main

label WaiterTraining:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
$ waitertrained = True
scene sirensbackroombackground
show tabithalingerie01 at midright
with fade
show keenlingerie01 at midleft with moveinleft
bk "Now let's see if that outfit fits you..."
hide tabithalingerie01
show tabithalingerie02 at midright
with fastdissolve
ta "It clearly doesn't, even though I gave him the one with the LARGEST pouch size available..."
hide keenlingerie01
show keenlingerie02 at midleft 
with fastdissolve
bk "Ooh, INTERESTING. Our clientele are going to LIKE this a LOT..."
hide keenlingerie02
show keenlingerie03 at midleft 
hide tabithalingerie02
show tabithalingerie01 at midright
with fastdissolve
bk "Now step on the stage and show us the goods, [hero]..."
play music "sounds/sexy06.mp3"
scene sirensbackroom01 with dissolve
mc "This is super-embarrassing. My cock is literally hanging out..."
bk "Never mind that. Take a bow, we're your audience."
scene sirensbackroom02 with dissolve
ta "He's a natural."
mc "And next?"
bk "Improvise. We need to get aroused by your routine..."
scene sirensbackroom03 with dissolve
ta "Keep smiling. Our female clientele want to feel appreciated."
bk "And use that pole. It's there for a reason."
scene sirensbackroom04 with dissolve
mc "Err, hi ladies, welcome to my SEXY show!"
ta "Now we're talking."
scene sirensbackroom05 with dissolve
ta "His cock is flying everywhere! * giggles *"
scene sirensbackroom06 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And look at it hanging all the way to the ground... It does look YUMMY!"
scene sirensbackroom07 with dissolve
ta "Maybe we should test-ride it first then? What do you think, Barbara?"
bk "I think I haven't had a cock in a long time... TOO LONG!"
ta "That's cos you've been too busy with my PUSSY! * giggles *"
bk "GET HARD FOR US, BOY!"
scene sirensbackroom08 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I'm definitely test-riding THAT THING!"
scene sirensbackroom09 with dissolve
mc "I feel like a cheap piece of meat."
bk "That's what you are. At our clientele's disposal. And therefore at OUR disposal too."
mc "I get it. I want the job badly so I'll do as I'm told. Plus, I'm just too horny right now."
stop music fadeout 2.0
bk "Your routine was quite good. But it could be better. Why don't you stand next to me while Tabitha shows you how to perform a PROPER pole dance routine?..."
play music "sounds/sexy11.mp3"
scene sirensbackroom10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
bk "Watch her. And learn from her. Then, you'll be ready to be a gigolo waiter at my big party..."
mc "Su.. Sure..."
scene sirensbackroom11 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I feel a HORNY audience tonight..."
scene sirensbackroom12 with dissolve
$ renpy.pause(1.0, hard='True')
ta "HORNY for a HOT, SENSUAL, show..."
bk "See how she engages with her audience?"
scene sirensbackroom13 with dissolve
$ renpy.pause(1.0, hard='True')
mc "Damn, look at that backside!"
bk "She's making you even HARDER, isn't she? I can feel your dong GROWING, [hero]..."
scene sirensbackroom14 with dissolve
$ renpy.pause(1.0, hard='True')
ta "I'm HORNY too..."
scene sirensbackroom15 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And look at how agile she is..."
scene sirensbackroom16 with dissolve
mc "Oh fuck..."
scene sirensbackroom17 with dissolve
bk "Yeah, watch her slide down that pole while my hand slides up YOURS!"
scene sirensbackroom18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
bk "Watch what she's about to do..."
scene sirensbackroom19 with dissolve
$ renpy.pause(1.0, hard='True')
ta "...for the final touch!"
mc "Oh!!!"
scene sirensbackroom20 with dissolve
$ renpy.pause(1.0, hard='True')
bk "And now the Grand Finale! What did you think?"
mc "Spectacular!"
stop music
ta "You ain't seen nothing yet, [hero]... Barbara, why don't you join me on stage?"
scene sirensbackroom21 with dissolve
play music "sounds/sexy13.mp3"
bk "I thought you'd never ask. Let me take my top off..."
scene sirensbackroom22 with dissolve
ta "Your breast are so soft... I never tire of playing with them!"
scene sirensbackroom23 with dissolve
play sound "sounds/moan02.mp3"
bk "And I LOVE how you play so delicately with them too..."
scene sirensbackroom24 with dissolve
ta "There's something else soft and tender that I'd like to play with..."
scene sirensbackroom25 with dissolve
play sound "sounds/moan02.mp3"
bk "Mmmh... In front of this... young muscle stud... You're going to make him so jealous..."
scene sirensbackroom26 with dissolve
mc "You girls are making me so FUCKING HORNY!"
scene sirensbackroom27 with dissolve
bk "Then come and join us..."
mc "FUCK YEAH!"
scene sirensbackroom28 with dissolve
ta "I'm going to lick that sumptuous pussy."
scene sirensbackroom29 with dissolve
mc "While I finger your sumptuous PUSSY!"
play sound "sounds/moan01.mp3"
ta "Oooh, that's so NAUGHTY!"
scene sirensbackroom30 with dissolve
play channel2 "sounds/lick01.ogg"
bk "Oooh... That's so..."
scene sirensbackroom31 with dissolve
play sound "sounds/moan03.mp3"
bk "...GOOOD!"
scene sirensbackroom30 with fastdissolve
play channel1 "sounds/moan02.mp3"
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
scene sirensbackroom30 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
scene sirensbackroom30 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sirensbackroom31 with fastdissolve
$ renpy.pause(1.0, hard='True')
stop channel1
stop channel2
ta "That was real Tasty, Barbara..."
bk "I... NEED A COCK! Carry us to the fuck area, [hero]..."
stop music
scene sirensbackroom32 with fastdissolve
bk "Oh my, you really are STRONG!"
if mcstrength == 1:
    mc "Super-Strength Level 1 right there, ladies!"
if mcstrength == 2:
    mc "Super-Strength Level 2 right there, ladies!"
    ta "Level 2? Wow, almost as strong as SUPERMAN!"

scene sirensbackroom33 with fastdissolve
bk "So what are you going to do, Super-Strong Boy?"
mc "I'm going to stick my giant pud up your twat so far, you'll be able to TASTE IT!"
bk "Let' see if you can keep promises then..."
scene sirensbackroom34 with dissolve
play sound "sounds/moan05.mp3"
bk "OOOOH! It's... * panting * ...already QUITE deep... Just go slow at first..."

label SirensBarbShortFuckSlow:
$ barbharder = False
window hide
show sirensbarbshortslowvideo behind sirensbarbshortfastvideo
show sirensbarbshortslowvideo behind sirensbarbshortpovslowvideo
show sirensbarbshortslowvideo behind sirensbarbslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbshortfastvideo
hide sirensbarbshortpovslowvideo
hide sirensbarbslowvideo
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
call screen sirensbarbshortslow()
screen sirensbarbshortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVSlow")

label SirensBarbShortFuckFast:
$ barbharder = False
window hide
show sirensbarbshortfastvideo behind sirensbarbshortslowvideo
show sirensbarbshortfastvideo behind sirensbarbshortpovfastvideo
show sirensbarbshortfastvideo behind sirensbarbfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbshortslowvideo
hide sirensbarbshortpovfastvideo
hide sirensbarbfastvideo
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
call screen sirensbarbshortfast()
screen sirensbarbshortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVFast")

label SirensBarbShortFuckPOVSlow:
$ barbharder = False
window hide
show sirensbarbshortpovslowvideo behind sirensbarbshortslowvideo
show sirensbarbshortpovslowvideo behind sirensbarbshortpovfastvideo
show sirensbarbshortpovslowvideo behind sirensbarbpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbshortslowvideo
hide sirensbarbshortpovfastvideo
hide sirensbarbpovslowvideo
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
call screen sirensbarbshortpovslow()
screen sirensbarbshortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckSlow")

label SirensBarbShortFuckPOVFast:
$ barbharder = False
window hide
show sirensbarbshortpovfastvideo behind sirensbarbshortpovslowvideo
show sirensbarbshortpovfastvideo behind sirensbarbshortfastvideo
show sirensbarbshortpovfastvideo behind sirensbarbpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbshortpovslowvideo
hide sirensbarbshortfastvideo
hide sirensbarbpovfastvideo
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
call screen sirensbarbshortpovfast()
screen sirensbarbshortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbShortFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckFast")

label SirensBarbFuckSlow:
if barbharder == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharder = True        
window hide
show sirensbarbslowvideo behind sirensbarbfastvideo
show sirensbarbslowvideo behind sirensbarbpovslowvideo
show sirensbarbslowvideo behind sirensbarbshortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbfastvideo
hide sirensbarbpovslowvideo
hide sirensbarbshortslowvideo
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
call screen sirensbarbslow()
screen sirensbarbslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEnd")

label SirensBarbFuckFast:
if barbharder == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharder = True        
window hide
show sirensbarbfastvideo behind sirensbarbslowvideo
show sirensbarbfastvideo behind sirensbarbpovfastvideo
show sirensbarbfastvideo behind sirensbarbshortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbslowvideo
hide sirensbarbpovfastvideo
hide sirensbarbshortfastvideo
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
call screen sirensbarbfast()
screen sirensbarbfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEnd")

label SirensBarbFuckPOVSlow:
if barbharder == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharder = True        
window hide
show sirensbarbpovslowvideo behind sirensbarbslowvideo
show sirensbarbpovslowvideo behind sirensbarbpovfastvideo
show sirensbarbpovslowvideo behind sirensbarbshortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide sirensbarbslowvideo
hide sirensbarbpovfastvideo
hide sirensbarbshortpovslowvideo
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
call screen sirensbarbpovslow()
screen sirensbarbpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEnd")

label SirensBarbFuckPOVFast:
if barbharder == False:
    bk "I'm ready to take that fuckstick HARDER!"
    mc "You want me to POUND YOU HARDER?"
    bk "YES! JUST DO IT, YOU GODAM MONSTERSTUD!"
    $ barbharder = True        
window hide
show sirensbarbpovfastvideo behind sirensbarbpovslowvideo
show sirensbarbpovfastvideo behind sirensbarbfastvideo
show sirensbarbpovfastvideo behind sirensbarbshortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbpovslowvideo
hide sirensbarbfastvideo
hide sirensbarbshortpovfastvideo
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
call screen sirensbarbpovfast()
screen sirensbarbpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensBarbFuckPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("SirensBarbShortFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensBarbFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensBarbCumEnd")

label SirensBarbCumEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
if age >= 20:
    bk "Please cum, [hero], I want to get FILLED UP with your YOUNG CREAM!"
if age >= 18 and age <= 19:
    bk "Please cum, [hero], I want to get FILLED UP with your YOUNG TEENAGE CREAM!"
window hide
show sirensbarbpovfastvideo behind sirensbarbpovslowvideo
show sirensbarbpovfastvideo behind sirensbarbfastvideo
show sirensbarbpovfastvideo behind sirensbarbshortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide sirensbarbpovslowvideo
hide sirensbarbfastvideo
hide sirensbarbshortpovfastvideo
mc "Alright, I'll show you how a SUPERSTUD COMES!"
window hide
pause 1.0
stop channel1
play channel1 "sounds/splooge02.mp3"
show sirenscum01 at truecenter:
    subpixel True
    linear 3.0 zoom 1.2 xoffset 0 yoffset 0 
with dissolve
mc "I'M BLOWING NOOOOWWWW!"
window hide
with fastflash
scene sirenscum02 with dissolve
mc "AND MORE! RHAAA!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
bk "AAAAH!"
window hide
with fastflash
ta "Pull out, she loves to be DOUSED in warm ball-batter!"
scene sirenscum03 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "HERE YOU ARE, WARM CUM COMING YOUR WAY!!!"
window hide
with fastflash
if age >= 20:
    bk "He's CAKING me in red-hot SPUNK!"
if age >= 18 and age <= 19:
    bk "He's CAKING me in red-hot TEEN SPUNK!"
scene sirenscum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Damn it... I'm still HARD. I'm gonna fuck ANOTHER PUSSY!"
bk "I guess it's your turn, Tabitha..."
ta "Is he really STILL HARD?"
scene sirenscum04 with dissolve
play sound "sounds/thud.mp3"
mc "Does this sound answer your question?"
ta "Oh fuck... This is UNREAL..."

scene sirenscum06 with dissolve
play sound "sounds/moan02.mp3"
ta "I can feel his HUGE HELMET... Already distending my pussylips..."

label SirensTabFuckSlow:
$ tabharder = False
window hide
show sirenstabslowvideo behind sirenstabfastvideo
show sirenstabslowvideo behind sirenstabpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sirenstabfastvideo
hide sirenstabpovslowvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen sirenstabslow()
screen sirenstabslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEnd")

label SirensTabFuckFast:
if tabharder == False:
    ta "I need to come, fuck me FASTER, STUD!"
    $ tabharder = True        
window hide
show sirenstabfastvideo behind sirenstabslowvideo
show sirenstabfastvideo behind sirenstabpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sirenstabslowvideo
hide sirenstabpovfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen sirenstabfast()
screen sirenstabfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEnd")

label SirensTabFuckPOVSlow:
$ tabharder = False
window hide
show sirenstabpovslowvideo behind sirenstabslowvideo
show sirenstabpovslowvideo behind sirenstabpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sirenstabslowvideo
hide sirenstabpovfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen sirenstabpovslow()
screen sirenstabpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEnd")

label SirensTabFuckPOVFast:
if tabharder == False:
    ta "I need to come, fuck me FASTER, STUD!"
    $ tabharder = True        
window hide
show sirenstabpovfastvideo behind sirenstabpovslowvideo
show sirenstabpovfastvideo behind sirenstabfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sirenstabpovslowvideo
hide sirenstabfastvideo
hide cum
hide faster
hide slower
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen sirenstabpovfast()
screen sirenstabpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SirensTabFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SirensTabFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SirensTabCumEnd")

label SirensTabCumEnd:
ta "You're gonna cum again, aren't you?"
mc "Fuck yeah..."
bk "He's gonna pump you FULL of his seed, Tabitha. You'd better get prepared!"
ta "Oh, I AM READY!"
scene sirenstabcum01 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
mc "Fuck, AAAAAHHH!"
window hide
with fastflash
ta "YES, YES, I'M CUMMING TOO!"
scene sirenstabcum02 with dissolve
play sound "sounds/moan06.ogg"
mc "ALL THE WAY IN!"
window hide
with hpunch
ta "AAAAH, IT'S SO DEEP!!!"
scene sirenstabcum03 with dissolve
play sound "sounds/boymoan03.mp3"
mc "OH GOD, I still NEED TO CUM SO MUCH, AAAH!"
window hide
with fastflash
bk "EMPTY THOSE BALLS, COME ON, COVER ME AGAIN IN YOUR SPUNK!"
scene sirenstabcum04 with dissolve
play sound "sounds/boymoan05.mp3"
mc "I'm CUMMING, BIG TIIIIMMME!"
window hide
with fastflash
ta "I can even HEAR his MASSIVE cumblasts!"
window hide 
with hpunch
play sound "sounds/boymoan03.mp3"
mc "Take those last few shots, my little cum-sluts! RHAAA!"
scene sirenstabcum05 with dissolve
bk "He did it again... I'm absolutely DRENCHED in his [age]yo scum..."
ta "I can feel his goo sliding down my poor ass... And he called us \"cum-sluts\", you heard that?"
bk "Yes, that was highly inappropriate, even though some of our clientele DO like to be domin..."
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "Ouch! What.. what are you doing?"
mc "You deserve a punishment for being my little cock-sluts today..."
scene sirenstabcum05 with dissolve
bk "He's so MANLY, even though he's just a BOY!"
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "AAAH, yes, slap me Daddy!"
scene sirenstabcum05 with dissolve
bk "Daddy? Why are you calling him that???"
play sound "sounds/spanking.mp3"
scene sirenstabcum06 with dissolve
ta "Ow! Err... I don't know, I just blurted it out..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
scene sirensbackroombackground
show tabithacum01 at midright
show keencum02 at midleft
with fade
ta "So, do you reckon he passed the test, Barbara?"
hide keencum02
show keencum01 at midleft
with fastdissolve
bk "I suppose we could hire him for ONE night at least and see how he BEHAVES!"
hide tabithacum01
show tabithacum02 at midright
with fastdissolve
ta "I'll keep an eye on him. And I'll SLIT HIS THROAT if he does!"
mc "Wow. Is there an union I can join to fight these violent corporate threats?"
bk "No."
hide tabithacum02
show tabithacum01 at midright
with fastdissolve
ta "We'll let you know when we need you. Now GO."
jump Main

label SirensParty:
if period == 0:
    $ period += 1
stop channel1
stop music
play music "sounds/barmusic.mp3"
scene sirens01
show tabithaclub01 at centerleft
with fade
ta "Ah, there you are, about time, our eminent guests are arriving in a short while."
mc "I came as fast as I could considering I don't have a cape and therefore I can't fly. Anyway, where is Barbara Keen? I don't see her around, that's weird."
hide tabithaclub01
show tabithaclub02 at centerleft
with fastdissolve
ta "That's NONE of your concern! You are here to WORK, remember?"
mc "Ah yeah, as a cheap male stripper who doesn't even get paid."
hide tabithaclub02
show tabithaclub03 at centerleft
with fastdissolve
ta "That's right, so just get dressed and ready for the party. I'll meet you backstage..."
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
scene backstage01 with dissolve
ta "Looks like you've grown some since last time... This outfit is really... HUGGING your muscles... * wink *"
mc "Err, yeah, I'm up to Level 2 now so I'm bigger."
scene backstage02 with dissolve
ta "Ah, here's Dani, the stripper we recruited at the last minute because the previous one dropped out."
mc "Sergeant D...? I mean, Sir. Gent-leman. This is how you should call the customers Dani, a piece of advice from a pro."
scene backstage03 with dissolve
ta "Yeah, whatever, she's not here to strike a conversation with the guests, so just shut up, BOTH OF YOU. She'll go first, then you, [hero]. I'll go and greet the first guests, so get ready."
scene backstage04 with dissolve
mc "What are you doing here, Sergeant Dani?"
da "I'm on a CCPD mission. Something's coming down tonight and Captain Sawyer wants me to find out what."
mc "Yeah, that's what everyone's saying but we're still totally in the dark."
scene backstage05 with dissolve
da "Aren't you going to wear a mask so you don't get recognized?"
mc "Na, I'll be fine. Without my thong and the super-hero sign on it, there's no way for people to know it's me. Just like with Clark Kunt."
da "What? Who's Clark Kunt?"
mc "Err... Nobody. He's a nobody. Without a dick."
scene backstage06 with dissolve
da "I'd better get going so as not to rouse suspicion. I'll see you later [hero] and we can... exchange information."
mc "Sure, I'll see how you're doing and get ready for my... err... stripshow."
play music "sounds/sexy06.mp3" volume 0.75
scene danistrip01 with dissolve
mc "* The room is packed. I hope she makes a good impression... *"
play sound "v061/applause.mp3"
scene danistrip02:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "* Well, she got some applause at least. Must be the big tits. *"
scene danistrip03 with dissolve
mc "* Nice. She's really taking this seriously. *"
scene danistrip04 with dissolve
mc "* I wonder if I'll get any applause... *"
scene danistrip05 with dissolve
mc "* Stripping is so stressful. *"
scene danistrip06 with dissolve
mc "* But she's such a natural... *"
scene danistrip07:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
"(guest) Show us some MOAR!"
"(other guest) YES, SHOW US YER PUSSY!"
scene danistrip08 with dissolve
mc "* I thought this was a high-class joint, but I see they still let the riffraff in! *"
scene danistrip09:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "* Ooh, I think she's doing what they asked for. Not that I can see anything, since I'm behind the curtain.*"
scene danistrip10 with dissolve
mc "* She's really giving them quite a show! *"
scene danistrip11 with dissolve
mc "* ...And putting the pressure on me... *"
scene danistrip12 with dissolve
"(guest) YEAH! WOO-HOO!"
scene danistrip13:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan01.mp3"
mc "* Now she's even playing with her pussy. *"
scene danistrip14 with dissolve
"(guest) Great pussy and nice tits!"
play sound "v061/applause.mp3"
scene danistrip15:
    zoom 1.0 xoffset -80 yoffset 0    
show danistrip15 at powerpoolfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
mc "* Ah, it looks like it's going to be my turn soon. *"
scene backstage07 with dissolve
ta "Your turn. Get on the stage and make sure to display that boymeat of yours for the ladies!"
mc "I feel just so cheap..."
ta "You ARE cheap. You work for free, remember?"
stop music
play music "sounds/sexy11.mp3" volume 0.5
scene mcstrip01 with dissolve
mc "* Now I'm super-stressed... *"
scene mcstrip02 with dissolve
mc "* Hope they don't laugh at my routine... *"
scene mcstrip03 with dissolve
mc "* Smile for the ladies... *"
scene mcstrip04 with dissolve
mc "* And now the helicopter cock... *"
window hide
scene mcstrip05 with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip06a with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip06b with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip03 with dissolve
play sound "sounds/wow.mp3"
mc "* Someone likes it at least... *"
show helicock
pause
play sound "v061/applause.mp3"
mc "* I got my first applause... *"
scene mcstrip07 with dissolve
mc "* Now I need to concentrate for my next acrobatic move... *"
scene mcstrip08:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "* Come on, I can do it... *"

scene mcstrip09 with dissolve
play sound "v061/applause.mp3"
mc "* I'm getting some more applause! *"
scene mcstrip10 with dissolve
"(female guest) GET THAT THING HARD FOR US!"
scene mcstrip11 with dissolve
mc "* Jesus... These people feel so entitled... I guess they're high-society. Or freeloading pirates on f95zone. *"
scene mcstrip12:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
play sound "sounds/audiencegasp.mp3"
mc "* Yeah, that shut them up alright! *"
scene mcstrip13 with dissolve
mc "* Check this mammoth rock-hard boymeat, you filthy perverts! *"
scene mcstrip14:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
play sound "sounds/boymoan.mp3"
mc "* Yeah... Fondling my balls and twisting my nipple... *"
stop music
play music "sounds/sexy14.mp3" volume 0.5
scene mcstrip15 with dissolve
mc "Sergeant Dani??? What are you doing?"
da "They want us to put on a show, so we'd better do as we're told, I don't want to blow my cover..."
scene mcstrip16 with dissolve
da "So I'll blow YOU instead! Just play along..."
mc "ALRIGHT!"
scene mcstrip17 with dissolve
play sound "sounds/slurp.mp3"
if age >= 20:
    da "It looks like it's getting you very EXCITED to know that I'm about to suck on your giant dong in front of all these people..."
if age >= 18 and age <= 19:
    da "It looks like it's getting you very EXCITED to know that I'm about to suck on your giant teenage dong in front of all these people..."
mc "Ohhh.... Fuck..."
scene mcstrip18 with dissolve
mc "AAAH..."
play channel1 "sounds/blow01.mp3"

label DaniBlowSlow:
$ daniblowfast = False
window hide
show daniblowslowvideo behind daniblowfastvideo
show daniblowslowvideo behind daniblowsceneslowvideo
pause 1.0
hide daniblowfastvideo
hide daniblowsceneslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowslow == False:
    $ daniblowslow = True
    mc "Yeah, gobble this cock for the audience, they like it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowslow()
screen daniblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowPOVSlow")

label DaniBlowFast:
$ daniblowslow = False
window hide
show daniblowfastvideo behind daniblowslowvideo
show daniblowfastvideo behind daniblowscenefastvideo
pause 1.0
hide daniblowscenefastvideo
hide daniblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowfast == False:
    $ daniblowfast = True    
    mc "You want to go a bit faster, hey, Yeah, that's right, we need to put on a SHOW tonight!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowfast()
screen daniblowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowPOVFast")

label DaniBlowPOVSlow:
$ daniblowfast = False
window hide
show daniblowsceneslowvideo behind daniblowslowvideo
show daniblowsceneslowvideo behind daniblowscenefastvideo
pause 1.0
hide daniblowscenefastvideo
hide daniblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowslow == False:
    $ daniblowslow = True
    mc "Yeah, gobble this cock for the audience, they like it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowscenefuckslow()
screen daniblowscenefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowSlow")

label DaniBlowPOVFast:
$ daniblowslow = False
window hide
show daniblowscenefastvideo behind daniblowfastvideo
show daniblowscenefastvideo behind daniblowsceneslowvideo
pause 1.0
hide daniblowfastvideo
hide daniblowsceneslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if daniblowfast == False:
    $ daniblowfast = True    
    mc "You want to go a bit faster, hey, Yeah, that's right, we need to put on a SHOW tonight!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowscenefuckfast()
screen daniblowscenefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowFast")

label DaniBlowEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Fuck yeah... Now hold it still..."
scene mcstrip19 with dissolve
play sound "sounds/blow02.mp3"
mc "Hold it..."
scene mcstrip20 with dissolve
play sound "v032/blow03.mp3"
mc "Let me help you get my shaft DEEPER down your hungry throat..."
scene mcstrip21 with dissolve
mc "Yeah, that's nice... Now keep going on your own, you can do it..."
play channel1 "sounds/blow02.mp3"

label DaniBlowHarderSlow:
$ daniblowharderfast = False
window hide
show daniblowharderslowvideo behind daniblowharderfastvideo
show daniblowharderslowvideo behind daniblowharderpovslowvideo
pause 1.0
hide daniblowharderfastvideo
hide daniblowharderpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderslow == False:
    $ daniblowharderslow = True
    mc "Oh God, I don't know where my cock is going, but it's going somewhere NICE and WARM!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowharderslow()
screen daniblowharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCum")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderPOVSlow")

label DaniBlowHarderFast:
$ daniblowharderslow = False
window hide
show daniblowharderfastvideo behind daniblowharderslowvideo
show daniblowharderfastvideo behind daniblowharderpovfastvideo
pause 1.0
hide daniblowharderpovfastvideo
hide daniblowharderslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderfast == False:
    $ daniblowharderfast = True    
    mc "Look at all those perverts watching us... It's making me so fucking HARD!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowharderfast()
screen daniblowharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCum")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderPOVFast")

label DaniBlowHarderPOVSlow:
$ daniblowharderfast = False
window hide
show daniblowharderpovslowvideo behind daniblowharderslowvideo
show daniblowharderpovslowvideo behind daniblowharderpovfastvideo
pause 1.0
hide daniblowharderpovfastvideo
hide daniblowharderslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderslow == False:
    $ daniblowharderslow = True
    mc "Oh God, I don't know where my cock is going, but it's going somewhere NICE and WARM!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowharderpovfuckslow()
screen daniblowharderpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCum")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderSlow")

label DaniBlowHarderPOVFast:
$ daniblowharderslow = False
window hide
show daniblowharderpovfastvideo behind daniblowharderfastvideo
show daniblowharderpovfastvideo behind daniblowharderpovslowvideo
pause 1.0
hide daniblowharderfastvideo
hide daniblowharderpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if daniblowharderfast == False:
    $ daniblowharderfast = True    
    mc "Look at all those perverts watching us... It's making me so fucking HARD!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowharderpovfuckfast()
screen daniblowharderpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCum")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderFast")

label DaniBlowHarderCum:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Oh fuck, I'm gonna blow..."
play sound "sounds/splooge02.mp3"
scene mcstripcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "Ohhhh!"
window hide
with hpunch
mc "COMING!!!!"
scene mcstripcum02 with dissolve
da "Mmmgggbb...."
window hide
with fastflash
mc "SO GOOD, AAAH!"
scene mcstripcum03 with dissolve
mc "Keep swallowing that boyload, I have more for you, RHAAA!"
window hide
with hpunch
mc "Goddam... UUUH!"
scene mcstripcum04:
    zoom 0.5
with dissolve
show mcstripcum04:
    subpixel True
    linear 8.0 zoom 1.0 xpos -0.5 ypos -0.5
play sound "sounds/splooge03.mp3"
if age >= 20:
    da "Looks like your erupting MEGA-DONG needed some fresh air! Look at that MONSTER SHOT!!!"
if age >= 18 and age <= 19:
    da "Looks like your erupting teen MEGA-DONG needed some fresh air! Look at that MONSTER SHOT!!!"
window hide
with fastflash
mc "AAAH! Oh God!!!"
scene mcstripcum05 with dissolve
play sound "sounds/moan02.mp3"
da "Keep going, cover me in your red-hot ball-batter!!!!"
window hide
with fastflash
mc "That's... AAAAH..."
window hide
with fastflash
mc ".... The last of it... Phew..."
stop channel1
scene mcstripcum06 with dissolve
play sound "sounds/lick02.mp3"
da "There's so much warm cum... We really gave them quite a show..."
mc "And yet, they didn't even give us a tip. Ungrateful high-society pirates..."
stop music
    
scene backstage08 with dissolve
ta "I'm forced to admit you did a pretty good job. Now I want you to wait on our distinguished guests."
ta "Dani, you take the backroom, [name], you take the front bar. And please wipe that cum off your face Dani, it's unbecoming of our high-class club."
scene backstage09 with dissolve
da "Now that she's gone, I need to tell you that I overheard a guest talk about some password that they needed to use later on."
mc "Oooh? And what was the password?"
scene backstage10 with dissolve
da "Something like... Constantinople. Or maybe Byzantium, I didn't hear very well."
mc "They're like totally different, how could you mistake the two????"
scene backstage09 with dissolve
da "No they're not! They're the same town!"
mc "Maybe it was Istanbul then... * snickers *"
scene backstage10 with dissolve
da "You can laugh all you want, at least I'm getting somewhere. I'd better get back to work, Tabitha has been looking at me strangely..."
mc "Fine, I'll try and find out what's going on and I'll keep an eye on you also, Dani."

play music "sounds/barmusic.mp3"
scene frontbar01:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with fade
mc "* How low have I sunk?... Serving champagne glasses to chrome-textured, and therefore unimportant, rich people while wearing a humiliating waiter costume... *"
scene frontbar02 with dissolve
mc "Hang on, isn't that the Mayor over there? And what is Emma Frost doing here too???"
label FrontBarMenu:
scene frontbar02
menu:
    "Approach the Mayor":
        jump FrontBarMayor
    "Approach Emma Frost":
        jump FrontBarFrost
    "Do your job and bring drinks to thirsty guests" if seenmayorbar and seenemmabar:
        jump FrontBarNext

label FrontBarMayor:
$ seenmayorbar = True
scene frontbar03 with dissolve
mc "Hey, Mister Mayor, it's me, [hero]!"
mk "Sorry young man, but I fear you are mistaken. I have no idea who you are..."
scene frontbar04 with dissolve
mk "And let it be known that THIS mayor doesn't frequent gay bars!"
" (male guest) Ha ha, nice one Mr Mayor! That boy certainly looks totally gay indeed!"
mc "* Damn it! Without my thong on and the superhero sign on it, he simply won't recognize me... (sigh)*"
jump FrontBarMenu

label FrontBarFrost:
$ seenemmabar = True
scene frontbar05 with dissolve
ef "Well, look here who comes... [hero], in a VERY gay waiter costume!"
mc "How did you recognize me????"
scene frontbar06 with dissolve
ef "I've seen your cock, remember? And right now, it's hanging out for all to see!"
ta "I like to make sure our waiters look like good little slave boys. HA HA! Speaking of which, GO BACK TO WORK!"
mc "* Damn it! Now they're making fun of me, this is so humiliating... *"
jump FrontBarMenu

label FrontBarNext:
scene frontbar07 with dissolve
"(male guest) Hey, waiter! Bring us some drinks over here!"
scene frontbar08 with dissolve
"(male guest) I hope it's not a GAY beer... * chuckles *"
mc "* Tabitha is talking to the Mayor. I wonder what she's saying... *"
call screen usepower("usesenses", "BarNoSenses", "BarSenses") with dissolve
label BarSenses:
if usedsenses <= 2:
    jump BarNoSenses
$ usedsenses += 1 
ta "The...ord...is...tanti..."
mc "* This room is too noisy, I only caught glimpses of what she said... *"
jump FrontBarNext02

label BarNoSenses:
ta "....an....."
if usedsenses <= 2:
    mc "Can't hear a damn thing! I haven't been using my Super-Senses enough times so far..."
    jump FrontBarNext02
mc "Can't hear a damn thing!"

label FrontBarNext02:
scene frontbar09 with dissolve
mc "* Uh oh. And now the Mayor is being whisked away by this devious assassin Tabitha. I'd better follow him."
label MoonStart:
stop music
play music "sounds/suspense.mp3"        
scene backstage11 with dissolve
mc "* Why did he go backstage? It looks like he's about to pick a gown... *"
scene backstage12 with dissolve
mc "* And he's put on a weird mask. What is he doing??? I'd better put on a similar costume and see where he's heading... *"
scene moonentrance01 with fade
ta "What is the password?"
menu:
    "Byzantium.":
        scene moonentrance02 with dissolve
        ta "WRONG ANSWER!"
        play sound "sounds/knifecut.mp3"
        ta "And now, you DIE, just like Ra's Al-Ghul did..."
        show gameovericon:
            xpos 600 ypos 400
        pause
        return
    "Constantinople.":
        ta "You may go through."
        jump SacrificeCeremony
    "Password? What password?":
        scene moonentrance02 with dissolve
        ta "WRONG ANSWER!"
        play sound "sounds/knifecut.mp3"
        ta "And now, you DIE, just like Ra's Al-Ghul did..."
        show gameovericon:
            xpos 600 ypos 400
        pause
        return

label SacrificeCeremony:
stop music
play music "v061/ominous.mp3" volume 0.5
scene moontemple01:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "* Err, okay, I'll guess I'll just go and stand in that empty spot over there then... *"
scene moontemple02 with dissolve
bk "Bring the sacrificial lamb to be offered to the dark Soul of Ra's Al-Ghul!"
mc "What the hell is going on? I'd better stay put for the moment and find out some more. *"
scene moontemple03 with dissolve
mc "* Sergeant Dani is the sacrificial lamb? *"
scene moontemple04 with dissolve
mc "* She looks totally drugged out. Probably on Chromium. So I doubt she's playing along. *"
scene moontemple05 with dissolve
play sound "sounds/coldwind.mp3"
bk "BEHOLD the mighty power of Ra's Al-Ghul's shadow as it enters into this temple!"
scene moontemple06 with dissolve
ta "Here is the Dagger that killed Ra's Al-Ghul! Watch it GLOW with the anticipation of this unholy sacrifice!"
play sound "sounds/audiencegasp.mp3"
bk "Hand it over. I alone can summon the Shadow Army of Ra's-Al-Ghul!!"
scene moontemple07:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
bk "Bow down before this dagger, slave! The dagger that will give ME the power to rule over Cockham once I plunge it into your heart!"
scene moontemple08 with dissolve
mk "Err, hang on a minute... I thought you said that I would be re-elected Mayor if..."
bk "Yes, you'll still be Mayor... But I'll stand besides you and you will do what I say! You remember when you used to do what I said, don't you? When you TRULY LOVED ME."
scene moontemple09 with dissolve
mk "I... I can't condone the killing of an innocent woman for re-election purposes!"
bk "Tell me you don't love me and you don't want to be Mayor anymore then! Dare say that and I won't plunge this dagger into her heart!"
scene moontemple10 with dissolve
hq "Boo-hoo! You guys are CRIMINALLY INSANE! I LOVE it!"
bm "I knew it was you, you filthy whore!"
scene moontemple11 with dissolve
bk "Why is Batman here? He was NOT invited!"
ta "He... He must have taken Bruce Vayne's spot, I'm sorry, I was sure it was him!"
scene moontemple12 with dissolve
hq "Batman, you really put the \"FUN\" in funeral! But anyway, I'll just have to smash your head in... AGAIN!"
bm "You won't get away this time, Harley!"
scene moontemple13:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
lu "Just KILL her godammit! You have a mole in here, I recognize her, she works for the CCPD! So just KILL HER ALREADY!"
ta "And I'll kill Mayor Krass and rid this city of him once and for all!"
mc " *Damn it, now I need to reveal myself and do something, this is turning into total mayhem! *"
stop music
play music "sounds/battlemusic.mp3"
menu:
    "Attempt to seize the dagger (Super-Agility)":
        jump MoonDagger
    "Try and protect the Mayor (Super-Combat)":
        jump MoonMayor

label MoonDagger:
scene moontemple14 with dissolve
call screen usepower("useagility", "DaggerNoAgility", "DaggerAgility") with dissolve

label DaggerAgility:
if usedagility <= 2:
    jump DaggerNoAgility
$ usedagility += 1 
scene moontemple15 with dissolve
$ saveddani = True
mc "OUCH, THIS BURNS! But I managed to grab it just in time!"
scene moontemple16 with dissolve
mc "Now I have your dagger, Barbara!"
bk "NO!!!! Tabitha, forget about the Mayor, get me my dagger back!"
scene moontemple17 with dissolve
lc "Throw it to me [name], I'll take it back to the compound and destroy it!"
mc "Lara???"
scene moontemple18 with dissolve
ef "Don't listen to her! Throw ME the dagger! I need it to RULE COCKHAM! With you!"
mc "Emma Frost???"
menu:
    "Throw the dagger to Lara Crotch (+1 Hero)" if evilness <= 12:
        $ laradagger = True
        scene moontemple19:
            subpixel True
            xpos 0.0
            linear 4.0 xpos -0.1        
        with dissolve
        play sound "sounds/whoosh.mp3"
        bk "My dagger, My PRECIOUS Dagger!!"
        call Good
        scene moontemple21 with dissolve
        ef "Damn you, [hero], I will not forget your TREACHERY!"
        lu "I'm outta here too, there are too many pesky super-heroes around to my liking!"
        hq "Missed again Batman! Hee hee!!!"
        scene moontemple28:
            subpixel True
            xpos 0.0
            linear 4.0 xpos -0.1        
        with dissolve
        play sound "sounds/knifecut.mp3"
        mc "You want some of me, Tabitha? I want some of you too, I'm gonna take a bite off your arm!"
        ta "AAAH!"
        scene moontemple29 with dissolve
        mc "Here, Mister Mayor, let me help you get up..."
        mk "Thank you young man, I don't know who you are but I will do everything I can for the LGBTQ community from now on..."
        mc "I'm [hero], Godammit, not a gay waiter!!!"        
        jump MoonEnd
        
    "Throw the dagger to Emma Frost (+1 Villain)" if evilness >= 13:
        $ emmadagger = True
        scene moontemple20 with dissolve
        play sound "sounds/whoosh.mp3"
        bk "My dagger, My PRECIOUS Dagger!!"
        call Evil
        play sound "sounds/punch.mp3"
        hq "Take THAT, you BORE!"
        scene moontemple21 with dissolve
        ef "I have it! Now I can escape and leave you all to FIGHT, HA HA HA!"
        lu "I'm outta here too, there are too many pesky super-heroes around to my liking!"
        hq "Missed again Batman! Hee hee!!!"
        scene moontemple28:
            subpixel True
            xpos 0.0
            linear 4.0 xpos -0.1        
        with dissolve
        play sound "sounds/knifecut.mp3"
        mc "You want some of me, Tabitha? I want some of you too, I'm gonna take a bite off your arm!"
        ta "AAAH!"
        scene moontemple29 with dissolve
        mc "Here, Mister Mayor, let me help you get up..."
        mk "Thank you young man, I don't know who you are but I will do everything I can for the LGBTQ community from now on..."
        mc "I'm [hero], Godammit, not a gay waiter!!!"        
        jump MoonEnd
        
    "Keep the dagger":
        scene moontemple22 with dissolve
        play sound "sounds/knifecut.mp3"
        ta "And now, you DIE, just like Ra's Al-Ghul did..."
        mc "AAAH! I was too greedy and selfish..."
        window hide
        show gameovericon:
            xpos 600 ypos 400
        pause
        return

label DaggerNoAgility:
scene moontemple23 with dissolve
mc "I missed entirely! What a loser!"
scene moontemple22 with dissolve
play sound "sounds/knifecut.mp3"
ta "And now, take THIS!"
mc "AAAH! That fucking hurts! Like I'm about to DIE..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label MoonMayor:
scene moontemple25 with dissolve
call screen usepower("usecombat", "TabithaNoCombat", "TabithaCombat") with dissolve

label TabithaCombat:
if mccombat <= 1 or usedcombat <= 2:
    jump TabithaNoCombat
$ usedcombat += 1
scene moontemple26 with dissolve
play sound "sounds/punch.mp3"
mc "Ouch! That is LITERALLY below the belt!"
ta "SuperVillains don't play by any RULES!"
mk "Please, somebody help me, she's going to kill me!"
scene moontemple27 with dissolve
play sound "sounds/whoosh.mp3"
lc "Super-Heroes can also bend the rules! I'll take this dagger, thank you very much!"
bk "What? Where did she come from???"
scene moontemple28:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
play sound "sounds/knifecut.mp3"
mc "You don't play by the rules? Then neither do I, I'm gonna take a bite off your arm!"
ta "AAAH!"
bk "Tabitha, the Dagger! They've taken THE DAGGER!!!"
scene moontemple29 with dissolve
mc "Here, Mister Mayor, let me help you get up..."
mk "Thank you young man, I don't know who you are but I will do everything I can for the LGBTQ community from now on..."
mc "I'm [hero], Godammit, not a gay waiter!!!"
scene moontemple21 with dissolve
ef "Damn this Lara Crotch for foiling my plan! Now I need to escape!"
lu "I'm outta here too, there are too many pesky super-heroes around to my liking!"
hq "Missed again Batman! Hee hee!!!"
$ laradagger = True
jump MoonEnd

label TabithaNoCombat:
scene moontemple22 with dissolve
play sound "sounds/knifecut.mp3"
ta "You can't FIGHT FOR SHIT! Not against ME!"
mc "AAAH! That fucking hurts! Like I'm about to DIE..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label MoonEnd:
stop music
play sound "sounds/policemusic.mp3"
scene moontemple30 with dissolve
cs02 "Everyone, FREEZE!"
scene moontemple31 with dissolve
ta "Time to leave quickly, sorry Barbara..."
bk " * sob * It's all over... I've been NEUTRALIZED..."
scene moontemple32 with dissolve
hq "I'm innocent, Mrs Policer Officer! I was assaulted by this nasty man with the mask!"
bm "I'm Batman! Arrest HER, she's the Super-Villain RAPIST!"
cs02 "Presumed rapist, Batman. And innocent until proven guilty. As per the judge's order. But I'll sort this all out at the station, I'm taking EVERYONE!"
scene moontemple33 with dissolve
stop sound
mk "You can let this young man go. He saved my life, despite being totally gay."
cs02 "It's [hero] Mister Mayor, from the Cockham League of Justice."
mc "I've been trying to tell him that for ages, but he simply doesn't get it!"

label Mission07Debrief:
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop music
play music "sounds/ccpdoffice.mp3"
scene ccpd01
show ccpd01back
with fade
show sawyereyeblink at centerleft with dissolve
cs01 "Thanks to you, we've arrested both Barbara Keen AND Harley Quiff. This is a glorious day for the CCPD!"
window hide
play sound "sounds/winning.mp3"
show mission07icon at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
$ mission07win = True
pause
hide mission07icon
hide winicon
if emmadagger:
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "It does appear however that we have not recovered the Dagger of Ra's-Al-Ghul... Would you happen to know where it vanished?"
    mc "Err... I was too busy fighting the bad guys to notice Captain Sawyer, sorry."
    hide sawyer04
    show sawyereyeblink at centerleft
    with fastdissolve
    cs01 "I see... Strange. You're supposed to have Super-Senses..."
hide sawyereyeblink
show sawyer05 at centerleft
with fastdissolve
cs01 "And Sergeant Dani has recovered from her Chromium overdose. Ah, here she comes."
show sawyer05 at midright with move
window hide
show dani03 at farleft with moveinleft
if saveddani:
    da "Thanks for saving my life [hero]! You are a CCPD HERO now! And you will always be MY hero in my heart..."
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirldani at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ daniharem = True
    mc "* Alright! A new chick in my HAREM! *"
    hide sawyer05
    show sawyer02 at midright
    with fastdissolve
    cs01 "Right, thank you for that...very personal note, Sergeant, go back to your duties."
    hide haremgirltext
    hide haremgirldani
    window hide
    hide dani03 with moveoutleft
if saveddani == False:
    da "Thanks to the Cockham League of Justice! And especially Lara Croft."
    mc "Well, I was going to save you, I was just saving the Mayor first..."
    hide sawyer05
    show sawyer02 at midright
    with fastdissolve
    cs01 "And Sergeant Dani appreciates your cooperation in the whole case, right Sergeant?"    
    hide dani03
    show dani02 at farleft
    with fastdissolve
    da "Sure! But still, Lara Croft is the ONE who truly saved my life. Goodbye, [hero]!"
    hide dani02 with moveoutleft
show sawyer02 at center with move
hide sawyer02
show sawyer05
with fastdissolve
cs01 "We unfortunately don't have yet any criminal motive to charge Harley Quiff who claims to have been assaulted by Batman. So your testimony will be essential in this case..."
hide sawyer05
show sawyer03 at center
with fastdissolve
cs01 "Also, she has requested to speak with YOU in private, and it was granted by the judge. So go and meet her in her cell and we'll record your damning testimony once you're done..."
stop music

hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene harleycell01 with fade
voice "harley/jail01"
hq "I've just been released from the NUT house and now they try and put me in the BIG house! Ain't that just CRAZY, my sweet puddin'?"
mc "I'm not your \"sweet pudding\". What do you want from me, Harley Quiff?"
scene harleycell02 with dissolve
voice "harley/jail02"
hq "Oops! Sorry, maybe you prefer if I call you an ANAL RAPIST? Does that ring a \"click\" better?"
mc "What? I didn't rape anyone!"
scene harleycell03 with dissolve
voice "harley/jail03"
hq "Oh but I have some photographs that say otherwise. What's this? I should tell him you think?"
mc "Who are you talking to?"    
scene harleycell04 with dissolve
voice "harley/jail04"
hq "The Joker! He's such a joke, he's even in my head! He says he's ready to mail those photos to Lois Pane at the Cockham Planet... OOPSIE!"
mc "Err, hang on, can we..."
scene harleycell02 with dissolve
voice "harley/jail05"
hq "...Talk? Sure, I LOVE to hear your voices! Can you imagine the face on Lois when she finds out her favorite Super-Hero is an ANAL RAPIST? She can be so NOSY!"
mc "Well, actually, she's kind of into BDSM and stuff, so..."
scene harleycell03 with dissolve
voice "harley/jail06"
hq "Ooh, she's NAUGHTY is she? Just as NAUGHTY as you? So naughty, you're about to RAPE a poor little innocent girl wrongly imprisoned for a crime she didn't commit?"
mc "What? I..."
scene harleycell05 with dissolve
voice "harley/jail07"
hq "Help, help! [hero] is about to rape me! Like he's done to so many INNOCENT women before!"
mc "Keep it down! I don't want the guards to hear about this nonsense!"
scene harleycell04 with dissolve
voice "harley/jail08"
hq "Oh well, I guess you'll just have to make sure I get out of here soon, won't ya puddin'?"
mc "What do you mean?"
play music "sounds/sexy08.mp3" volume 0.25
scene harleycell06 with dissolve
voice "harley/jail09"
hq "I heard that you saw EVERYTHING at that crazy cult party! You definitely saw that nasty Batman assault me with a baseball bat didn't ya? * wink *"
mc "Okay, I get it, I'll say that you were wrongly assaulted by this dickhead then."
voice "harley/jail10"
hq "AND you'll rape me, don't forget that bit, puddin'!"
scene harleycell07:
    zoom 1.0 xoffset -80 yoffset 0    
show harleycell07 at powerpoolfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
voice "harley/jail11"
hq "Good thing they let me wear some SEXY lingerie underneath that AWFUL prison uniform!"
scene harleycell08:
    zoom 1.0 xoffset -40 yoffset -1400    
show harleycell08 at powerpoolfulldown02
with dissolve
$ renpy.pause(6.0, hard='True')    
voice "harley/jail12"
hq "I mean, how the hell are you supposed to RAPE me if I can't even get you HARD?"
mc "I..."
voice "harley/jail13"
hq "Shush, puddin'! Don't say a word and grab me from behind the bars like you MEAN IT..."
scene harleycell09 with dissolve
voice "harley/jail14"
hq "Mmmh, yeah, just like that... You like my big tits, dontcha?"
scene harleycell10 with dissolve
voice "harley/jail15"
hq "And I like that HUGE thing you're trying to hide down that ridiculous thong, hee hee!"
scene harleycell11:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
voice "harley/jail16"
hq "Oh, lookee! You're SUPER-HARD for me! This is going to be a GREAT RAPE!"
mc "I don't know if we should be doing th..."
scene harleycell12 with dissolve
voice "harley/jail17"
hq "What does it say right HERE? Can't you READ?"
mc "It's just that... I'M NOT A RAPIST!"
voice "harley/jail18"
hq "Alright, I see, I'm the one who's going to have to do all the work. AS USUAL, PFFF!"
scene harleycell13:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
play sound "sounds/wow.mp3"
if age >= 20:
    voice "harley/jail19a"
    hq "My! You have such a MASSIVE manmeat for me, Mr Rapist!"
if age >= 18 and age <= 19:
    voice "harley/jail19b"
    hq "My! You have such a MASSIVE teen boymeat for me, Mr Rapist!"
mc "Stop calling me that and start sucking, you nutcase!"
scene harleycell14 with dissolve
voice "harley/jail20"
hq "Every woman has a crazy side that only the right man can bring out."
scene harleycell15 with dissolve
mc "I may not be the right man, but I have the right dong, so get working!"
voice "harley/jail21"
hq "Now you're getting the hang of it, Mr Rapist!"
scene harleycell16 with dissolve
play sound "sounds/lick03.mp3"
mc "AAAH..."
voice "harley/jail22"
hq "I'll start from that end and make my way to the other side!"

play channel1 "sounds/blow01.mp3" volume 0.75
play channel2 "sounds/wank.mp3" volume 0.5

label HarleyBlowSlow:
$ harleyblowfast = False
window hide
show harleyblowslowvideo behind harleyblowfastvideo
show harleyblowslowvideo behind harleyblowpovslowvideo
pause 1.0
hide harleyblowfastvideo
hide harleyblowpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if harleyblowslow == False:
    $ harleyblowslow = True
    mc "It's crazy how big your mouth is when you think about it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen harleyblowslow()
screen harleyblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowPOVSlow")

label HarleyBlowFast:
$ harleyblowslow = False
window hide
show harleyblowfastvideo behind harleyblowslowvideo
show harleyblowfastvideo behind harleyblowpovfastvideo
pause 1.0
hide harleyblowpovfastvideo
hide harleyblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if harleyblowfast == False:
    $ harleyblowfast = True    
    mc "Yeah, do it faster. But don't bite!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen harleyblowfast()
screen harleyblowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowPOVFast")

label HarleyBlowPOVSlow:
$ harleyblowfast = False
window hide
show harleyblowpovslowvideo behind harleyblowslowvideo
show harleyblowpovslowvideo behind harleyblowpovfastvideo
pause 1.0
hide harleyblowpovfastvideo
hide harleyblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if harleyblowslow == False:
    $ harleyblowslow = True
    mc "It's crazy how big your mouth is when you think about it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleyblowpovfuckslow()
screen harleyblowpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowSlow")

label HarleyBlowPOVFast:
$ harleyblowslow = False
window hide
show harleyblowpovfastvideo behind harleyblowfastvideo
show harleyblowpovfastvideo behind harleyblowpovslowvideo
pause 1.0
hide harleyblowfastvideo
hide harleyblowpovslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide pov
if harleyblowfast == False:
    $ harleyblowfast = True    
    mc "Yeah, do it faster. But don't bite!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleyblowpovfuckfast()
screen harleyblowpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowFast")

label HarleyBlowEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if age >= 20:
    mc "I bet you want to go DEEPER don't you? Cos you're nuts and it would be mad to try and DEEP-THROAT MY EIGHTEEN INCH MEGA-COCK!"
if age >= 18 and age <= 19:
    mc "I bet you want to go DEEPER don't you? Cos you're nuts and it would be mad to try and DEEP-THROAT MY EIGHTEEN INCH TEENAGE MEGA-COCK!"
stop channel1
stop channel2
scene harleychoke01 with dissolve
play sound "v061/blowgulp.mp3"
hq "Mmmmgggbb...I...gg-can...mm-do...IT!"
mc "Not bad, but I think you need a little bit of help..."
play channel2 "sounds/blow02.mp3"
scene harleychoke02:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "Like so! AAAH!"
scene harleychoke03 with dissolve
mc "Deeper still, come on, open that big mouth of yours wider, Harley!"
hq "Mmmgggg!!!"
scene harleychoke04 with dissolve
mc "There you go, take a short breather. If you can..."
hq " *puff *"
scene harleychoke05 with dissolve
mc "And come back closer to daddy! RHAAA!"
window hide
show harleychoke
pause
stop channel2
play sound "v061/blowend.mp3"
    
scene harleychoke06 with dissolve
mc "And... Release."
scene harleychoke07 with dissolve
play sound "v031/cough.mp3"
mc "Ah, that was good. For me. How was it for you? Not that I care."
voice "harley/jail23"
hq "* cough * Usually, I'm the one who fucks with people's heads!"
scene harleychoke08 with dissolve
voice "harley/jail24"
hq "But you didn't come yet. That doesn't count as a PROPER rape if you don't unload a CRAZY NUT!"
mc "You wanna get raped real MAD, don't you?"
scene harleycell22 with dissolve
voice "harley/jail25"
hq "I'm feeling an emptiness in my coochee right now. And when my coochee is empty, I can get HYSTERICAL! \n I might end up calling the guards on you. OOP-SIE!"
mc "Don't you dare! Or I'll..."
scene harleycell23 with dissolve
voice "harley/jail26"
hq "...Rape me real good? But you'll have to open the door to catch me, Mr Rapist!"
mc "I will, and you'd better play the innocent helpless rape victim, I'm warning you!"
voice "harley/jail27"
hq "Ooh, I've always wanted a REAL rapeplay buddy!"
scene harleycell24:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
if age >= 20:
    voice "harley/jail28a"
    hq "Help! I'm about to have my fuckhole torn apart by a nasty man with a YUMMY MONSTERCOCK!"
if age >= 18 and age <= 19:
    voice "harley/jail28b"
    hq "Help! I'm about to have my fuckhole torn apart by a nasty teenage boy with a YUMMY MONSTERCOCK!"
scene harleycell25 with dissolve
mc "You won't need that, Harley Quiff!"
scene harleycell26 with dissolve
play sound "sounds/ripping.mp3"
voice "harley/jail29"
hq "That was my only pair! Are you CRAZY?"
scene harleycell27 with dissolve
mc "Now turn round, you little harlot! Time for some good spanking!"
voice "harley/jail30"
hq "What have I done to deserve this, Mr Rapist?"
scene harleycell28 with dissolve
mc "You've been a very NAUGHTY girl and I'm going to slap some SENSE into you..."
scene harleycell29 with dissolve
play sound "sounds/thud.mp3"
mc "... With THIS!"
scene harleycell28 with dissolve
voice "harley/jail31"
hq "Oooh! Slap me again! I've been such a BAD girl!"
show harleyslap
window hide
play channel1 [ "sounds/thud.mp3", "<silence .72>" ]
show harleyslap
pause
stop channel1
mc "That's enough. I think you've learnt your lesson."
scene harleycell30 with dissolve
voice "harley/jail32"
hq "I'm a slow learner, I might need some more IN-DEPTH private tuition!"
mc "I see. I'm going to have to DRILL that lesson into you then!"
scene harleycell31 with dissolve
voice "harley/jail33"
hq "Ooh, no Mr Rapist! Don't stick your massive wang inside my poor little innocent hole, please!"
mc "Err... I'm going to say you're playing along and this isn't really rape. For Patreon rules purposes that is."
scene harleycell32 with dissolve
play sound "sounds/womancum01.mp3"
voice "harley/jail34"
hq "UUUH, AAAH! That wasn't simulated, I can assure you, you're in SO DEEP already!"
stop sound
play channel2 "sounds/womansex05.mp3"
label HarleyPoundSlow:
$ harleypoundfast = False
window hide
show harleypoundslowvideo behind harleypoundfastvideo
show harleypoundslowvideo behind harleypoundfrontslowvideo
pause 1.0
hide harleypoundfastvideo
hide harleypoundfrontslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
with dissolve
play channel2 "sounds/womansex02.mp3"
if harleypoundslow == False:
    $ harleypoundslow = True
    mc "Damn you... * puff * I'm going to fuck you silly!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen harleypoundslow()
screen harleypoundslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundPOVSlow")

label HarleyPoundFast:
$ harleypoundslow = False
window hide
show harleypoundfastvideo behind harleypoundslowvideo
show harleypoundfastvideo behind harleypoundfrontfastvideo
pause 1.0
hide harleypoundfrontfastvideo
hide harleypoundslowvideo
hide nexticon
hide front
hide faster
hide slower
hide front
with dissolve
play channel2 "v031/womansex08.mp3"
if harleypoundfast == False:
    $ harleypoundfast = True    
    voice "harley/jail35"
    hq "Come on, bang me harder, give it all you've got, Mr Rapist!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen harleypoundfast()
screen harleypoundfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundPOVFast")

label HarleyPoundPOVSlow:
$ harleypoundfast = False
window hide
show harleypoundfrontslowvideo behind harleypoundslowvideo
show harleypoundfrontslowvideo behind harleypoundfrontfastvideo
pause 1.0
hide harleypoundfrontfastvideo
hide harleypoundslowvideo
hide nexticon
hide front
hide faster
hide slower
hide front
with dissolve
play channel2 "sounds/womansex02.mp3"
if harleypoundslow == False:
    $ harleypoundslow = True
    hq "Do you like my little innocent sex-crazed hole, Mr Rapist?"
    mc "Damn you... * puff * I'm going to fuck you silly!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleypoundfrontfuckslow()
screen harleypoundfrontfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundSlow")

label HarleyPoundPOVFast:
$ harleypoundslow = False
window hide
show harleypoundfrontfastvideo behind harleypoundfastvideo
show harleypoundfrontfastvideo behind harleypoundfrontslowvideo
pause 1.0
hide harleypoundfastvideo
hide harleypoundfrontslowvideo
hide nexticon
hide front
hide faster
hide slower
hide front
play channel2 "v031/womansex08.mp3"
if harleypoundfast == False:
    $ harleypoundfast = True    
    voice "harley/jail35"
    hq "Come on, bang me harder, give it all you've got, Mr Rapist!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleypoundfrontfuckfast()
screen harleypoundfrontfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundFast")

label HarleyPoundEnd:
hide nexticon
hide front
hide faster
hide slower
hide front
voice "harley/jail36"
hq "Now is the perfect time to DUMP that load in my fertile womb, Mr Rapist!"
mc "What? I..."
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
scene harleyfuckcum01:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
play channel3 "sounds/splooge02.mp3"
mc "......COMING! AAAH!"
window hide 
with fastflash
voice "harley/jail37"
hq "That's it, but it's not ENOUGH!"
scene harleyfuckcum02 with dissolve
play sound "sounds/womancum02.mp3"
voice "harley/jail38"
hq "Just KEEP PUMPING PUDDIN'! I WANT YOUR BABY YOU HEAR ME!"
window hide
with fastflash
mc "Godamn, RHAAA!!!"
scene harleyfuckcum03 with dissolve
mc "You're gripping my dong so tight, AAAH!"
window hide
with hpunch
voice "harley/jail39"
hq "I just want to make sure I'll get PREGNANT from your nutsauce!"
scene harleyfuckcum04 with dissolve
play sound "v032/womancum04.mp3"
voice "harley/jail40"
hq "So just REALLY POUND my uterus with your baby-making ball-batter, Mr Rapist!"
window hide
with vpunch
mc "You filthy harlot! You want a RAPE-BABY? You'll GET ONE!"
scene harleyfuckcum05 with dissolve
voice "harley/jail41"
hq "Have you dumped ENOUGH nutsauce in my belly you reckon? It sure seems to have SWELLED UP A LOT!"
mc "I've dumped the biggest load you'll ever h..."
scene harleyfuckcum06 with dissolve
stop channel3
play sound "sounds/splooge03.mp3"
voice "harley/jail42"
hq "Back to the sender! Hee hee!"
mc "What the?..."
scene harleyfuckcum07 with dissolve
stop channel2
play sound "sounds/punch.mp3"
voice "harley/jail43"
hq "Get off me, Mr Rapist! Here, let me HELP YOU!"
play sound "sounds/splooge01.mp3"
mc "UUUH!"
scene harleyfuckcum08 with dissolve
voice "harley/jail44"
hq "You didn't HONESTLY believe I would want a baby from YOU? Eew! Like I would ever want to raise YOUR stupid SPAWN!"
mc "You are so cruel, Harley..."
scene harleyfuckcum09:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
voice "harley/jail45"
hq "Yep, that's ME-EE! Now, you know what to testify, Mr Rapist. Or I'll be forced to say you knocked me up against my OWN FREE WILL!"
mc "Damn you, Harley. DAMN YOU!"
voice "harley/jail46"
hq "BOO-HOO! I heard that kind of WHINING so many times before! BORING!"
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
play music "sounds/ccpdoffice.mp3"
scene ccpd01
show ccpd01back
with fade
show sawyereyeblink with dissolve
cs01 "How did it go? You took your pretty time..."
mc "Err... We were involved in a lengthy argument."
hide sawyereyeblink
show sawyer02
with fastdissolve
cs01 "I see... I hope you testimony will be much shorter and put her behind bars for GOOD then."
mc "About that. I testify that Batman assaulted her first. She was just an innocent bystander in that murderous cult meeting."
hide sawyer02
show sawyer04
with fastdissolve
cs01 "What??? This is NOT what I expected! The judge will force me to release her!"
mc "As I said, she's innocent, so setting her free would be the proper thing to do. If she was guilty, she'd be appealing everything under the sun to stay out of jail until she gets elected to some office with immunity."
hide sawyer04
show sawyer03
with fastdissolve
cs01 "* sigh * I suppose I'll have to take your word for it and let her go then. This day turned from glorious to disastrous in a single affidavit. Get out of here!"
jump Main