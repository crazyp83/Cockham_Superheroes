label CMRoomDay:
stop music
scene compoundmilfbedroomday with fade
mc "Well, look at this place. Windows wide open, any Super-Villain could just fly straight in! I'll guess I stand guard here until the evening then..."
jump Main

label CMRoomNight:
if (d10locnight == 3 or d10locnight == 4) or ((d10locnight == 2 or d10locnight == 8) and seenmilfnight == False):
    jump CMRoomNightMILF
if (d10locnight == 2 or d10locnight == 8) and seenmilfnight:
    jump CMRoomNightYoga

scene compoundmilfbedroomnight with fade
mc "Well, look at this place. Windows wide open, any Super-Villain could just fly straight in! I'll guess I stand guard here until Captain MILF goes to bed then..."
scene compoundmilfbedroomnight with fade
show librarymilf04 with moveinright
cm "What are you doing here, [name]?"
mc "I was standing GUARD against our Super-Villain ENEMIES. Especially the flying ones who could have easily flown into your bedroom since the windows were wide open!"
hide librarymilf04
show librarymilf03 with fastdissolve
cm "Well, thank you for your... vigilance. Although you could have just closed the windows..."
mc "Ah yes, but then, they wouldn't have been tempted to come and I wouldn't have been able to CAPTURE THEM!"
hide librarymilf03
show librarymilf04 with fastdissolve
cm "Right... Well, now I'm here so you can go back to your bedroom. I will close the windows and no flying Super-Villain will dare come into our compound."
mc "I will sleep with one eye open to protect the compound!"
hide librarymilf04
show librarymilf02 with fastdissolve
cm "Sure. Goodnight, sweetie."
jump Main

label CMRoomNightMILF:
if seenmilfpoolresistance and (chosemilftitjob == False or chosemilffootjob == False or chosemilfanal == False):
    jump MilfSaunaReward
if seenmilfpoolresistance and chosemilftitjob and chosemilffootjob and chosemilfanal and mission07win and evilness <= 5:
    jump MilfSaunaRewardHarem

stop music
play channel1 "sounds/sexy06.mp3"
scene compoundmilfbedroomnight with fade
show milfnight01 at centerleft with moveinright
show milfnight01 at centerleft:
    breathe
voice "milf/room01"
cm "Hello sweetie, what are you doing visiting me in my room that late?"
label CMNightDialogue:
menu:
    "Oh, I didn't realize it was that late.":
        $ seenmilfnight = True
        hide milfnight01
        show milfnight02 at centerleft
        with fastdissolve
        voice "milf/room02"
        cm "I was about to go to bed actually..."
        mc "Fine, err... I'll go to bed too then. Just making sure you were safe and all..."
        hide milfnight02
        show milfnight06 at centerleft
        with fastdissolve
        voice "milf/room03"
        cm "I'm pretty sure I'll be fine... But I'll let you watch just in case. So you can go back to your room completely reassured."
        hide milfnight06
        show milfnight03 at centerleft
        with fastdissolve
        voice "milf/room04"
        cm "That's really why you came, isn't it?"
        mc "Err..."
        hide milfnight03
        show milfnight04 at centerleft
        with fastdissolve
        voice "milf/room05"
        cm "To watch me take off my night robe and expose my muscular body in sexy lingerie..."
        mc "Well, now that you mention it..."
        hide milfnight04
        show milfnight05 at centerleft
        with fastdissolve
        voice "milf/room06"
        cm "And admire my tight glutes as I head off to bed..."
        mc "Damn, they sure are TIGHT!"
        window hide
        show compoundmilfbedroomnight blurred:
            subpixel True
            zoom 2.0
            xpos 0.4 ypos 1.2
            ease 3.5 xpos 0.42 ypos 1.3           
        show milfnight05b:
            subpixel True
            ypos 0.0
            linear 3.0 ypos -0.1
        $ renpy.pause(3.0, hard='True')
        voice "milf/room07"
        cm "So, are you reassured that nothing will happen to me?"
        window hide
        mc "I think I am..."
        voice "milf/room08"
        cm "Then go back to your room and go to sleep..."
        stop channel1
        jump Main
    "I wanted to know where I could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide milfnight01
        show milfnight02 at centerleft
        with fastdissolve
        voice "milf/room09"
        cm "But, she's just an intern. She doesn't need a costume."
        mc "How is she going to audit the books of super-villains if she's stuck in the compound?"
        hide milfnight02
        show milfnight06 at centerleft
        with fastdissolve
        voice "milf/room10"
        cm "I suppose you're right. There is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide auditquestcostumeprogress01
        hide milfnight06
        show milfnight03 at centerleft
        with fastdissolve
        voice "milf/room11"
        cm "Are you interested in her? Your landlady's puppies aren't big enough for you? * wink *"
        mc "Well, err... No, it's just..."
        voice "milf/room12"
        cm "You're trying to help me manage the compound? You think I can't handle it by myself?"
        mc "Well, you must be busy all the time, so I thought..."
        hide milfnight03
        show milfnight02 at centerleft
        with fastdissolve
        voice "milf/room13"
        cm "Just don't spend too much money on her. She's JUST an intern. And I'm the League's CAPTAIN."
        mc "Roger that, Captain MILF!"
        stop channel1
        jump Main
    "I was raped by Harley Quiff. Anally raped." if sawharley and toldmilfharley == False and period == 1:
        $ toldmilfharley = True
        hide milfnight01
        show milfnight06 at centerleft
        with fastdissolve
        cm "What? You mean... You took it up the ass?"
        mc "No! She forced my dick up HER ass! And drained my nuts. I must have come a gallon."
        hide milfnight06
        show milfnight03 at centerleft
        with fastdissolve
        cm "Oh, that's terrible, my sweet little pumpkin. Did you arrest her then?"
        mc "No... I failed miserably..."
        hide milfnight03
        show milfnight02 at centerleft
        with fastdissolve
        cm "That's not very impressive any longer. You're a disappointing tenant, [name]. I gave you these huge muscles to be able to ARREST Super-Villains!"
        mc "Her Super-Seduction powers are just too strong for me at this stage. I need MORE superpower!"
        cm "Therefore, you need to train and reach level 2 SUPERHERO!"
        mc "But I can't yet."
        hide milfnight02
        show milfnight01 at centerleft
        with fastdissolve
        cm "The time will come, the time will come, sweetie. Goodnight, [name]."
        jump Main
    "Do you need a nice relaxing massage before going to bed, Carol?" if mclevel02:
        voice "milf/room14"
        cm "You're offering to give your landlady a massage? How sweet of you!"
        mc "We can go to my room for it, it has a nice soothing atmosphere..."
        hide milfnight01
        show milfnight03 at centerleft
        with fastdissolve
        voice "milf/room15"
        cm "I do feel a bit tense... Alright, sweetie pie, lead the way! But don't expect any discount on your rent. Which is due next week, I remind you."
        jump MILFMassage
    "Can you teach me Super-Seduction level 2, Captain MILF?" if usedseduction >= 1 and seenmilfyoga and mcseduction == 1 and mission03end:
        hide milfnight01
        show milfnight06 at centerleft
        with fastdissolve
        cm "Super-Seduction? You think you might need it?"
        mc "Yes, definitely. Especially if I am to reach Superhero level 2. You want me to reach it, right? My muscles and... my cock would GROW even BIGGER..."
        hide milfnight06
        show milfnight03 at centerleft
        with fastdissolve
        cm "Please don't say that... You make me sound like a cockhound. But fine, I'll teach you. Let's move closer to the bed, it will be required..."
        jump MILFSeduction
    "Are you in the mood for some HOT seducing? By ME!" if mcseduction >= 2 and mclevel02 == False:
        hide milfnight01
        show milfnight06 at centerleft
        with fastdissolve
        cm "Are you planning on Super-Seducing your landlady, you naughty boy?"
        mc "Damn right, I am!"
        hide milfnight06
        show milfnight03 at centerleft
        with fastdissolve
        cm "Well, I do feel... kinda KINKY tonight. Why don't we head closer to the bed honeypot?"
        mc "Oooh yeah!"
        jump MILFSeduction
    "Carol, I want to show you something. (show your cock, MALEDOM SEX SCENE)" if (evilness >= 13 or evilness <= 5) and seenmilfseduction and seenmilfmaledom == False and mclevel02 == False:
        hide milfnight01
        show milfnight02 at centerleft
        with fastdissolve
        cm "What is is, [name]?"
        play sound "sounds/thud.mp3"
        mc "THIS! My MIGHTY ALPHA-COCK!"
        hide milfnight02
        show milfnight07 at centerleft
        with fastdissolve
        play sound "sounds/gasp.mp3"
        hide milfnight07
        show milfpremaledom01
        with fastdissolve
        play music "sounds/sexy06.mp3"
        cm "Oh my God... I... can't fight it... Your cock, it's so MASSIVE!"
        mc "Yeah, and I'm going to fuck you senseless with it, Captain MILF! So take that gown off NOW!"
        hide milfnight07
        show milfpremaledom01
        with fastdissolve
        if age >= 20:
            cm "You're just so MANLY when you talk to me like that... With your GIANT menacing pussy-wrecker staring at me..."
        if age >= 18 and age <= 19:
            cm "You're just so MANLY when you talk to me like that... With your GIANT menacing teenage pussy-wrecker staring at me..."
        hide milfpremaledom01
        show milfpremaledom02
        with fastdissolve
        mc "Walk towards the bed, Carol..."
        jump MILFMaledom
    "You know why I'm here. LANDLADY-LANDBOY SEX! (show your cock, MALEDOM SEX SCENE)" if (evilness >= 13 or evilness <= 5) and seenmilfseduction and seenmilfmaledom and mclevel02 == False:
        hide milfnight01
        show milfnight02 at centerleft
        with fastdissolve
        cm "Oh no, you're going to FUCK MY ASS AGAIN???"
        play sound "sounds/thud.mp3"
        mc "That's right. With my MIGHTY ALPHA-COCK!"
        hide milfnight02
        show milfnight07 at centerleft
        with fastdissolve
        play sound "sounds/gasp.mp3"
        cm "Oh my God... I... can't fight it... Your cock, it's so MASSIVE!"
        mc "Yeah, and I'm going to fuck you senseless with it again, Captain MILF! So take that gown off NOW!"
        hide milfnight07
        show milfpremaledom01
        with fastdissolve
        if age >= 20:
            cm "You're just so MANLY when you talk to me like that... With your GIANT menacing pussy-wrecker staring at me..."
        if age >= 18 and age <= 19:
            cm "You're just so MANLY when you talk to me like that... With your GIANT menacing teenage pussy-wrecker staring at me..."
        hide milfpremaledom01
        show milfpremaledom02
        with fastdissolve
        mc "You know the drill, Captain MILF. Get on the bed! NOW!"
        jump MILFMaledom    
    "I'm off to bed, Captain MILF.":
        hide milfnight01
        show milfnight06 at centerleft
        with fastdissolve
        cm "Sincerity dictates that I do not enjoy this state of idleness."
        stop channel1
        jump Main

label CMRoomNightYoga:
$ seenmilfyoga = True
stop channel1
scene milfroomnightyoga01 with fade
play channel1 "sounds/relax.mp3"
call screen milfyoganight()
screen milfyoganight():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Jump ("MainTime")]        
    imagebutton:
        focus_mask True
        idle "v02/milfroomnightyoga01idle.png"
        hover "v02/milfroomnightyoga01hover.png"
        action Jump ("CMRoomNightYogaB")
        
label CMRoomNightYogaB:
scene milfroomnightyoga02 with dissolve
cm "Oh, hello sweetie. I was just doing a bit of yoga stretching before heading to bed..."
mc "And I was just passing by in the hope you were..."
scene milfroomnightyoga03 with dissolve
cm "You can watch, but don't disturb me. I need to concentrate on all my MUSCLES."
scene milfroomnightyoga04 with dissolve
cm "It's important that I stay in shape, don't you agree?"
mc "Oh yeah, totally."
scene milfroomnightyoga05 with dissolve
cm "If our enemies were to attack us, I would be READY to REPEAL them."
mc "So would I! Although maybe not quite right now."
scene milfroomnightyoga06 with dissolve
cm "And why is that, [name]?"
mc "Well, I'm, like, too focused on something else right now..."
scene milfroomnightyoga07 with dissolve
cm "Ooh? And what would that be?"
scene milfroomnightyoga08 with dissolve
mc "...Gllrr..."
cm "Why don't you help me stretch my leg muscles instead of mumbling to yourself? Hold my left foot for me while I stretch them."
scene milfroomnightyoga09 with dissolve
cm "[name]! Your... thing... it's getting awfully BIG! What is happening?"
scene milfroomnightyoga10 with dissolve
mc "It's not my fault, I..."
scene milfroomnightyoga11 with dissolve
mc "...can't help it!"
if seenmilfsauna or seenmilfyoga:
    cm "Oh dear, you're getting a HARDON! In front of your landlady! AGAIN!"
else:
    cm "Oh dear, you're getting a HARDON! In front of your landlady!"
scene milfroomnightyoga12 with dissolve
cm "This can't be happening! I need to..."
scene milfroomnightyoga13 with dissolve
if seenmilfsauna or seenmilfyoga:
    cm "...look away NOW! Please leave [name], I can't afford to lose my superpowers! Yet AGAIN!"
else:
    cm "...look away NOW! Please leave [name], I can't afford to lose my superpowers!"
mc "I'm sorry Carol! I'll... leave now. And take care of that hardon myself..."
scene milfroomnightyoga14 with dissolve
if age >= 20:
    cm "Don't say that, I'm imagining you jerking off that fat donkey-dick of yours! Please go away, I'm having terrible landlady-tenant thoughts! "
if age >= 18 and age <= 19:
    cm "Don't say that, I'm imagining you jerking off that fat teenage donkey-dick of yours! Please go away, I'm having terrible landlady-tenant thoughts! "
jump Main
            
label MILFSeduction:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ seenmilfseduction = True
stop channel1
play music "sounds/sexy05.mp3"
scene compoundmilfnightseduction01
show milfseduction01
with dissolve
if mcseduction == 1:
    cm "First, the rules. You need to seduce me WITHOUT using your cock. Because that would be cheating. In my case."
    mc "Fine. So, what do I have to do?"
    cm "You have to show the woman you are trying to seduce how special she is."
    mc "Well, you're SUPER-special to me. I mean, you're my landlady and..."
if mcseduction >= 2:
    cm "This is why you came, isn't it. To SEDUCE your landlady again. Without your cock again." 
    mc "I was hoping you weren't going to say that second part. * sigh *"
hide milfseduction01
show milfseduction02
with dissolve
if mcseduction == 1:
    cm "Not like that. Not all women you want to seduce are going to be your landladies!"
    cm "Let's move to more practical exercises. Seduce me with your hands, play with my body, do it softly, like women yearn for..."
    mc "I can do that, I'm an expert I'll show you!"
if mcseduction >= 2:
    cm "I will enjoy it. You playing softly with my body." 
    mc "Alright, I'll do it."
hide milfseduction02
show milfseduction03
with dissolve
if mcseduction == 1:
    cm "I will slightly open my gown to make it easier for you. Come forward, [name] and show me..."
if mcseduction >= 2:
    cm "Come forward, [name], your landlady is ready for some SENSUAL loving..."        
scene compoundmilfnightseduction02
show milfseduction04
with dissolve
play sound "sounds/moan02.mp3"
if mcseduction == 1:
    cm "Mmmh, go slowly, [name]. Show a woman that you have plenty of time for her..."        
if mcseduction >= 2:
    cm "Mmmh, go slowly, [name]. We have plenty of time..."        
hide milfseduction04
show milfseduction05
with dissolve
play sound "sounds/moan01.mp3"
cm "That's better, [name]..."
mc "Let me slowly slide your gown off before I..."
hide milfseduction05
show milfseduction06
with dissolve
play sound "sounds/moan03.mp3"
mc "...play with your belly button..."
cm "Oooh, I didn't expect that..."
scene milfseduction07 with dissolve
play sound "sounds/moan01.mp3"
cm "Oooh, what are you doing, naughty boy?"
scene milfseduction08 with dissolve
play sound "sounds/lick01.ogg"
mc "Just making sure your pussy is nice and wet..."
scene milfseduction09 with dissolve
play sound "sounds/moan02.mp3"
if mcseduction == 1:
    cm "Push my panties aside slowly, you're doing VERY good so far, [name]..."
if mcseduction >= 2:
    cm "Push my panties aside slowly, [name]..."        
scene milfseduction10 with dissolve
cm "Mmh, just like that, gently pull them down now..."
scene milfseduction11 with dissolve
mc "And now I can lick your sweet nectar direct from the source..."
cm "Please hurry up, I'm so wet..."
scene milfseduction12 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH!"
window hide
with hpunch
mc "Did I just make you cum, Captain MILF?"
cm "Yes, a little bit... I need to play with my big titties..." 
mc "Allow me... As a landboy, it is my duty to pleasure my landlady..."
scene milfseduction13 with dissolve
play channel1 "sounds/moan02.mp3"
cm "Mmmh, knead them for me, make them all YOURS!"
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
stop music
mc "They feel so fucking big, Carol... You are the epitome of the SUPER-heroine! And SUPER-LANDLADY."
if age >= 20:
    cm "Oh, I'm gonna cum again, my dear hunk of a tenant!"
if age >= 18 and age <= 19:
    cm "Oh, I'm gonna cum again, my dear teenage hunk of a tenant!"
stop channel1
window hide
play sound "sounds/womancum01.mp3"
with hpunch
scene milfseduction13 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction14 with dissolve
$ renpy.pause(1.0, hard='True')
cm "Now play with my pussy and make me EXPLODE with pleasure, sweetie pie!"
scene milfseduction15 with dissolve
play sound "sounds/moan01.mp3"
cm "Mmh, yes, just like that..."
scene milfseduction16 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH, it's so good!"
play channel1 "sounds/moan03.mp3"
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction15 with dissolve
$ renpy.pause(0.5, hard='True')
scene milfseduction16 with dissolve
$ renpy.pause(0.5, hard='True')
mc "And now for the Grand Finale..."
stop channel1
scene milfseduction17 with dissolve
play sound "sounds/womancum02.mp3"
cm "OOOOOHHHH!"
window hide
with hpunch
mc "Yeah, squirt for me, Carol!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
cm "AAAAH!"
mc "I did, I made you squirt!"
cm "So you did, and you deserve a reward. A MILKY REWARD!"
scene milfseduction18 with dissolve
cm "So come and get it, your landlady still has breast milk from when, err... whatever."
scene milfseduction19 with dissolve
play sound "sounds/slurp.mp3"
cm "Oooh, yes, pinch my right nipple while you suckled on my left tit..."
play sound "sounds/moan01.mp3"
mc "I love your landlady milk, I want more!"
scene milfseduction18 with dissolve
cm "It's all for you, my sweet boy."
scene milfseduction19 with dissolve
play sound "sounds/slurp.mp3"
cm "That's it, slurp it all up, you deserve it, you've been  such a GOOD boy!"
scene milfseduction20 with dissolve
cm "Was it good, my sweet landboy?"
mc "Super-Tasty, Carol!"
cm "Then let ME taste it too..."
stop music
scene milfseduction21:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
if mcseduction == 1:
    play sound "sounds/kiss.mp3"
    cm "That was perfect, [name]. You've definitely reached level 2 in Super-Seduction! Kiss me tenderly..."
    call SeductionPlus from _call_SeductionPlus
    mc "Fuck yeah, Level 2 in Super-Seduction, DAMN!"
    cm "Now remember, use this super-power only when you NEED to... Like just now because I NEEDED this... Bye bye, sweetie!"
    jump Main
if mcseduction == 2:
    cm "That was perfect, [name]. Kiss me tenderly..."
    play sound "sounds/kiss.mp3"
    cm "And go back to your room, my dear young landboy."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
        
label MILFMaledom:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ seenmilfmaledom = True
stop channel1
play music "sounds/sexy12.mp3"
scene compoundmilfnightseduction02
show milfmaledom01
with dissolve
if evilness <= 5:
    cm "My sweet landboy, I'll do whatever you want cos you've been such a GOOD boy, but we must be quick about it."
    mc "Let's see how it goes. I might need multiple releases, Carol."
if evilness >= 13:
    cm "The compound is at our enemies' mercy without my Super-powers. Don't you care?"
    mc "Nope. I care about only one thing right now... Fucking you on your bed. And you only care about that too, admit it, Captain MILF!"
hide milfmaledom01
show milfmaledom02
with dissolve
if evilness <= 5:
    cm "Alright, I can't say no to you, you're such an ASSET to the compound... And your cock... Is making me weak in the knees..."
    mc "I know but I chose you because you're the hottest MILF here! And you're my landlady too..."
    hide milfmaledom02
    show milfmaledom01
    with fastdissolve
    cm "Really?? You think that? I'm not too old for such a strapping young SUPERSTUD like you?"
    mc "Of course not, Carol! Now please show me that sumptuous ass of yours..."
if evilness >= 13:
    cm "I... Yes, I admit it. I am just a filthy landlady who can't help but lust after her horse-hung tenant's [age]year-old MONSTER COCK..."
    mc "Turn round Carol, I want to see that sumptuous ass of yours again..."
window hide
hide milfmaledom01
hide milfmaledom02
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 1.8
    xpos 0.4 ypos 1.6
    ease 7.5 xpos 0.42 ypos 1.0           
show milfmaledom03:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
if evilness <= 5:
    mc "Fuck yeah! I'm going to ENJOY working that hot landlady ass tonight!"
    cm "You're being VERY naughty. But you're just so horny, aren't you? My poor sweet tenant..."
    mc "Yeah, you're just so hot I'm getting a MASSIVE hardon... You need to do something about it, Carol."    
if evilness >= 13:
    mc "Fuck yeah! I'm going to DESTROY that ass tonight!"
    cm "You want to destroy's your landlady's ass? That's so... filthy, [name]!"
    mc "It's not filthy, it's the natural stage of landboy superhero evolution. Now worship my cock!"
scene milfmaledom04 with dissolve
cm "[name], your cock! It's just so ENORMOUS!"
mc "That's right, and YOU'RE the one who rents a room to this SUPER-STUD."
scene milfmaledom05 with dissolve
play sound "sounds/kiss.mp3"
cm "I'm such a proud landlady. * kisses *"
play sound "sounds/kiss.mp3"
cm "Having such a HORSE-HUNG landboy... * kiss *"
scene milfmaledom06 with dissolve
play sound "sounds/lick02.mp3"
if age >= 20:
    cm "And your balls... They're just so MANLY. So full of hot, young VIRILE CUM!"
if age >= 18 and age <= 19:
    cm "And your balls... They're just so MANLY. So full of hot, young VIRILE TEENAGE CUM!"
mc "AAAH..."
scene milfmaledom07 with dissolve
play sound "sounds/lick03.mp3"
cm "You like it when I worship your HUGE BULL-BALLS?"
mc "FUCK!!! Yes, I do, you're doing a great job, Carol!"
scene milfmaledom08 with dissolve
cm "You're making me so horny, [name]! I need to take this bra off..."
mc "Yeah, you do... And your panties too... SO I can POUND THAT ASS!"
scene milfmaledom09 with dissolve
cm" But... Your love muscle is just so BIG! DO you think it will fit inside my tight little butthole?"
mc "I'll make it fit. Even if it means I have to DESTROY YOUR HOLE!"
scene milfmaledom10 with dissolve
cm "Maybe you should lubricate my rosebud with your abundant precum, [name]."
mc "Damn, Captain MILF, you're making me LEAK so damn much!"
scene milfmaledom11 with dissolve
play sound "sounds/moan02.mp3"
cm "Rub your giant pecker against my puckered backdoor then..."
scene milfmaledom12 with dissolve
play sound "sounds/moan03.mp3"
cm "Yes, just like that, [name]..."
if evilness <= 5:
    scene milfmaledom13a with dissolve
    mc "Let me carry you to the bed so we can make sweet anal love, Carol."
    cm "You're such a GOOD superhero landboy... I'll let you do ANYTHING you want to my poor little hole..."
if evilness >= 13:
    scene milfmaledom13b with dissolve
    cm "Wh.. What are you doing?"
    mc "I can't wait any longer, prepare to get ANALLY IMPALED on my giant cock!"
    cm "Oh, you're so ROUGH! You treat your landlady like a cheap whore!"
    mc "That's cos you ARE a CHEAP WHORE, Captain MILF!"
scene milfmaledom14 with dissolve
play sound "sounds/moan04.ogg"
if evilness <= 5:
    cm "Aaah, you're so STRONG, [name]! And I've lost all my superpowers anyway... PLease RAVISH me like the young STUD that you are!"
    mc "Are you ready to get STRETCHED by my massive dong, Carol?"
    if age >= 20:
        cm "Yes I am, go on, you can stick your giant pud in me as far as it will go, [name]!"
    if age >= 18 and age <= 19:
        cm "Yes I am, go on, you can stick your giant teenage pud in me as far as it will go, [name]!"
if evilness >= 13:
    cm "Aaah, You're holding my legs in such a tight muscular armlock, I can't move, I'm totally at the mercy of your HOLE-DESTROYER!"
    mc "That's right, so get ready for the ASS-POUNDING of your lifetime, Carol!"
    if age >= 20:
        cm "Go on, stick your giant pud as far as it will go and do your filthy deed with my landlady hole!"
    if age >= 18 and age <= 19:
        cm "Go on, stick your giant teenage pud as far as it will go and do your filthy deed with my landlady hole!"
window hide
stop music

label MilfAssFuckSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckslowvideo behind milfassfuckfastvideo
show milfassfuckslowvideo behind milfassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ milfassfuckfast = False
if milfassfuckslow == False:
    cm "Oh my God, you're stretching me so much with your enormous dong, [name]!"
    $ milfassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milfassfuckslow()
screen milfassfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfAssFuckFrontSlow")

label MilfAssFuckFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfastvideo behind milfassfuckslowvideo
show milfassfuckfastvideo behind milfassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckslowvideo
hide milfassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ milfassfuckslow = False
if milfassfuckfast == False:
    mc "I'm gonna POUND that ass even FASTER now, Carol!"
    $ milfassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen milfassfuckfast()
screen milfassfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfAssFuckFrontFast")

label MilfAssFuckFrontSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfrontslowvideo behind milfassfuckslowvideo
show milfassfuckfrontslowvideo behind milfassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckslowvideo
hide milfassfuckfrontfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ milfassfuckfast = False
if milfassfuckslow == False:
    cm "Oh my God, you're stretching me so much with your enormous dong, [name]!"
    $ milfassfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen milfassfuckfrontslow()
screen milfassfuckfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckSlow")

label MilfAssFuckFrontFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show milfassfuckfrontfastvideo behind milfassfuckfastvideo
show milfassfuckfrontfastvideo behind milfassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ milfassfuckslow = False
if milfassfuckfast == False:
    mc "I'm gonna POUND that ass even FASTER now, Carol!"
    $ milfassfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen milfassfuckfrontfast()
screen milfassfuckfrontfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfAssFuckFast")

label MilfAssFuckEnd:
hide cum
hide assview
hide faster
hide slower
hide front
mc "Your ass is milking my dong..."
cm "I can feel every ridge of your MONSTERCOCK, I KNOW you're about to blow! Do it for your landlady, paint her insides with your spunk!" 
scene milffuckcum01 with dissolve
play channel1 "sounds/splooge02.mp3"
hide milfassfuckslowvideo
hide milfassfuckfastvideo
hide milfassfuckfrontslowvideo
hide milfassfuckfrontfastvideo
play sound "sounds/boymoan05.mp3"
if evilness <= 5:
    mc "AAAH, take that, Carol, filling your ass with my cream!"
if evilness >= 13:
    mc "AAAH, take that you filthy cock-whore, filling your ass with my cream!"
window hide
with fastflash
cm "AAAH, you're so naughty, but your cock is just so good!"
window hide
with fastflash
cm "I can feel every MONSTERSHOT inside my ass!"
scene milffuckcum02 with dissolve
play sound "sounds/moan04.ogg"
play channel2 "sounds/boyorgasm01.mp3"
cm "[name], you're... PUMPING ME FULL! There's SO MUCH of it!"
window hide
with fastflash
mc "There's more where that came from, RHAAA!"
scene milffuckcum03 with dissolve
if evilness <= 5:
    cm "I need to SEE your CONVULSING cock as it BLASTS all that hot young sperm!"
if evilness >= 13:
    mc "Pull it out, I'm gonna repaint your body in my spunk and CLAIM you as MY slut, Carol!"
window hide
with fastflash
if evilness <= 5:
    mc "Go on, take it out, I'll BLAST all over your hot bod, AAAH!"
if evilness >= 13:
    cm "You're treating me like your SEX SLAVE, [name]! And I can't resist!"
    mc "That's cos you're MY SEX SLAVE NOW!"
scene milffuckcum04 with dissolve
stop channel1
play sound "sounds/moan01.mp3"
if age >= 20:
    cm "You're STILL cumming so MUCH, [name]! You're such a HUGE-DICKED STALLION!"
if age >= 18 and age <= 19:
    cm "You're STILL cumming so MUCH, [name]! You're such a HUGE-DICKED TEEN STALLION!"
window hide
with fastflash
mc "You're making me cum NON-STOP, FFFUUUUUUCCCCKKKK!"
scene milffuckcum05 with dissolve
play sound "sounds/moan03.mp3"
if evilness <= 5:
    cm "I'm so happy to be satisfying your sexual needs, [name]!"
if evilness >= 13:
    cm "More, MORE, cover your filthy cock-whore landlady with your scalding scum, [name]!"
window hide
with fastflash
mc "Take those shots, RHAAA!"
scene milffuckcum06 with dissolve
stop channel2
play sound "sounds/moan02.mp3"
if evilness <= 5:
    cm "You took my ass and turned it inside out, [name]... But I've never been pleasured so much in my life before! You deserve a REWARD!"
if evilness >= 13:
    cm "You totally DESTROYED my ass... And then you CAKED me in your red-hot sperm... I feel so filthy..."
scene milffuckcum07 with dissolve
if evilness <= 5:
    mc "Oooh, what do you have in store for me, Carol?"
    cm "I'm offering you... My tits! Stick your monster shaft between them and I will take you to heavens!"
if evilness >= 13:
    mc "You ARE filthy, Carol. And you deserve a PUNISHMENT for that."
    cm "Wh.. What? Please, I need to get my superpowers back. You've been fucking me for way too long, [name]!"
if evilness <= 5:
    scene milffuckcum08a with dissolve
    if age >= 20:
        cm "See how BIG they are? Perfect for your HUGE MONSTERDONG!"
    if age >= 18 and age <= 19:
        cm "See how BIG they are? Perfect for your HUGE TEEN MONSTERDONG!"
if evilness >= 13:
    scene milffuckcum08b with dissolve
    mc "My cock is DEMANDING more attention. From your MASSIVE funbags!"
    cm "But [name]... Oh, I can't say no to my GIANT-COCKED tenant! Just fuck my tits to your heart's content, [name]!"
scene milffuckcum09 with dissolve
if evilness <= 5:
    cm "Just FUCK MY TITS TO YOUR HEART'S CONTENT!"
    mc "I sure will. They are so fucking big. It will be the BEST titfuck I ever had."
if evilness >= 13:
    mc "I sure will. They are so fucking big. It will be the BEST titfuck I ever had."
play sound "sounds/moan01.mp3"
cm "You like your landlady's enormous breasts, don't you, you naughty boy?"
scene milffuckcum10 with dissolve
mc "Fuck yeah, I'm gonna PUMMEL my shaft between those soft pillows."
cm "I will make sure you cum a HUGE load again, until you are completely satisfied. I can't leave you like that with such an aching hardon!"
play channel1 "sounds/wank.mp3"
window hide

label MilfTitFuckSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckslowvideo behind milftitfuckfastvideo
show milftitfuckslowvideo behind milftitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
with dissolve
play channel2 "sounds/boymoan04.mp3"
$ milftitfuckfast = False
if milftitfuckslow == False:
    cm "Your cock is so big, it's stretching all the way to my face!"
    $ milftitfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen milftitfuckslow()
screen milftitfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFrontSlow")

label MilfTitFuckFast:
$ milftitfuckslow = False
if milftitfuckfast == False:
    mc "Damn, those big tits are so good around my shaft, Carol!"
    cm "Then pump that big fucking dick between them FASTER, [name]!"
    $ milftitfuckfast = True
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfastvideo behind milftitfuckslowvideo
show milftitfuckfastvideo behind milftitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckslowvideo
hide milftitfuckfrontfastvideo
with dissolve
play channel2 "sounds/boymoan02.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen milftitfuckfast()
screen milftitfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFrontFast")

label MilfTitFuckFrontSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfrontslowvideo behind milftitfuckslowvideo
show milftitfuckfrontslowvideo behind milftitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckslowvideo
hide milftitfuckfrontfastvideo
with dissolve
play channel2 "sounds/boymoan04.mp3"
$ milftitfuckfast = False
if milftitfuckslow == False:
    cm "Your cock is so big, it's stretching all the way to my face!"
    $ milftitfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen milftitfuckfrontslow()
screen milftitfuckfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckSlow")

label MilfTitFuckFrontFast:
$ milftitfuckslow = False
if milftitfuckfast == False:
    mc "Damn, those big tits are so good around my shaft, Carol!"
    cm "Then pump that big fucking dick between them FASTER, [name]!"
    $ milftitfuckfast = True
window hide
hide cum
hide slower
hide faster
hide front
hide sideicon
show milftitfuckfrontfastvideo behind milftitfuckfastvideo
show milftitfuckfrontfastvideo behind milftitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
with dissolve
play channel2 "sounds/boymoan02.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sideicon:
     xpos 1700 ypos 500     
call screen milftitfuckfrontfast()
screen milftitfuckfrontfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitFuckFast")

label MilfTitFuckEnd:
window hide
hide cum
hide sideicon
hide faster
hide slower
hide front
if evilness <= 5:
    cm "Are you going to BLAST that hot load for me?"
if evilness >= 13:
    cm "Are you going to BLAST that hot load for your filthy slut of a landlady?"
mc "Any minute now, Carol, any min..."
window hide
scene milftitfuckcum01 with dissolve
hide milftitfuckslowvideo
hide milftitfuckfastvideo
hide milftitfuckfrontslowvideo
hide milftitfuckfrontfastvideo
stop channel1
stop channel2
play sound "sounds/boymoan05.mp3"
cm "Oh, look at your huge pole cumming, my horny landboy!"
window hide
with fastflash
mc "AAAH, your giant milkbags did that!"
scene milftitfuckcum02 with dissolve
play sound "sounds/boymoan03.mp3"
cm "I'm so PROUD that your landlady's big fat filthy tits made you cum so hard, [name]!"
window hide
with fastflash
mc "I'm not done Captain MILF, RHAAA!"
scene milftitfuckcum03 with dissolve
play sound "sounds/boymoan05.mp3"
cm "I KNOW you still have a LOT of creamy fuckjuices for your landlady, don't you, my sweet young boy?"
window hide
with fastflash
mc "Oh, CAROL, AAAAH! You're such a dirty talker, you're making me CUUU-UUUUM!!!"
scene milftitfuckcum04 with dissolve
play sound "sounds/panting.mp3"
cm "You gave me so MUCH cum... I'm COVERED in your tenant splooge..."
mc "Then clean my cock up, I need to go back to my room. We wouldn't want the whole compound turning up here and seeing us like that, now would we?"
scene milftitfuckcum05 with dissolve
play sound "sounds/lick03.mp3"
if evilness <= 5:
    mc "Yeah, slurp it all up, Carol, I need a clean cock to fight our super-villain ENEMIES!"
if evilness >= 13:
    mc "Yeah, slurp it all up, like a good cum-whore..."
scene milftitfuckcum06 with dissolve
play sound "sounds/lick02.mp3"
if evilness <= 5:
    cm "I agree, [name]... * slurp * You can't go out like that with such a DIRTY, CUM-COVERED DONG!"
if evilness >= 13:
    cm "I'm a cum-whore for... * slurp * ...my horse-hung landboy who just came all over my big titties!"
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(1.0, hard='True')
scene milftitfuckcum06 with fastdissolve
play sound "sounds/lick02.mp3"
$ renpy.pause(0.5, hard='True')
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(1.0, hard='True')
scene milftitfuckcum06 with fastdissolve
play sound "sounds/lick02.mp3"
$ renpy.pause(0.5, hard='True')
mc "Fuck yeah, that's good, Carol... I'll give you your super-powers back now..."
scene milftitfuckcum05 with fastdissolve
play sound "sounds/lick03.mp3"
cm "By going back to your room?"
mc "Yeah, that's right."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label MILFMassage:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy04.mp3"
scene milfmassage01 with fade
voice "milf/room20"
cm "Where would you like me to go, sweetie pie?"
mc "You can just lie on the bed, Captain MILF."
scene milfmassage02 with dissolve
voice "milf/room21"
cm "And what kind of \"massage\" did you have in mind exactly?"
mc "I was thinking... Swedish."
scene milfmassage03 with dissolve
voice "milf/room22"
cm "Isn't that a bit naughty for a tenant to give to his old landlady?"
mc "Well, err... I already gave you one, remember?"
scene milfmassage04 with dissolve
voice "milf/room23"
cm "Ah yes, that's true, you ended up pounding me with your great big enhanced whopper. So I have to get naked then."
mc "Correctomundo!"
scene milfmassage05 with dissolve
voice "milf/room24"
cm "And YOU have to get naked too, my sweet tenant... Maybe I could help you achieve a hardon faster..."
mc "You certainly could, Carol! It's already starting to work!"
scene milfmassage06 with dissolve
voice "milf/room25"
cm "So soon? Does your landlady make you THAT horny, [name]?"
mc "Damn right she is!"
scene mcroomsex15 with dissolve
voice "milf/room26"
cm "But before that, I need to make sure I'm REALLY wet down there. Your level 02 dong is just so... HUGE now!"
scene mcroomsex16 with dissolve
play sound "sounds/moan04.ogg"
voice "milf/room27"
cm "Mmh, my pussy feels so tender..."
scene mcroomsex17 with dissolve
play sound "sounds/moan06.ogg"
mc "Yeah, you got yourself off, Carol!"
scene mcroomsex05 with dissolve
voice "milf/room28"
cm "Now I'm ready to lie down so you can start off with your SENSUOUS massage. Before FUCKING your landlady with your GIGANTIC pussy-wrecker!"
mc "Alright!"
scene mcroomsex06 with dissolve
voice "milf/room29"
cm "And I'm looking the other way so I don't see your huge... thingie and faint in admiration."
mc "I'll try and keep it out of the way for the moment..."
scene mcroomsex07 with dissolve
play sound "sounds/moan03.mp3"
voice "milf/room30"
cm "Mmh, that's nice, sweetie pie..."
scene mcroomsex08 with dissolve
mc "Your buns are just so... amazingly tight, Captain MILF!"
voice "milf/room31"
cm "I can crush a walnut between my cheeks, [name]."
mc "Right, err... You'll have to show me that one day."
scene mcroomsex09 with dissolve
mc "In the meantime..."
play sound "sounds/moan02.mp3"
voice "milf/room32"
cm "Oooh, what are you doing, naughty boy?"
mc "Massaging the INSIDE of your snatch. It needs to dilate quite a bit, considering the size of my level 02 Super-Dong..."
voice "milf/room33"
cm "Mmmh, my machine really did work, didn't it..."
mc "It sure did, Carol."
scene mcroomsex10 with dissolve
play sound "sounds/moan01.mp3"
voice "milf/room34"
cm "That was VERY good, my sweet young tenant... Now it is MY turn to show my appreciation."
scene mcroomsex11b with dissolve
play sound "sounds/gasp.mp3"
voice "milf/room35"
cm "Oh my dear Lord! Look at that GIANT boymeat you're sporting, sweetie pie!"
mc "Yes, and I'm so hard, it's literally aching!"
scene mcroomsex12 with dissolve
voice "milf/room36"
cm "Then I need to do something about it, don't I?"
mc "Ooh yeah!"
scene mcroomsex13 with dissolve
voice "milf/room37"
cm "Show me again how you please a woman with that giant pecker!"
mc "Oh God, this is about to get real HOT!"
scene mcroomsex18 with dissolve
mc "Fuck, I'm just so fucking HUGE for you!"
voice "milf/room38"
cm "I can't even watch, I fear I might faint seeing your behemoth plowing through my love canal..."
scene mcroomsex19a with dissolve
play sound "sounds/thud.mp3"
mc "Can you feel how HEAVY it is, Carol?"
play channel2 "sounds/moan02.mp3"
window hide
scene mcroomsex19b with dissolve
$ renpy.pause(.8, hard='True')
play channel1 [ "sounds/thud.mp3", "<silence .8>"]
scene milfcockslap
pause
voice "milf/room39"
cm "Oh God... It's the BIGGEST piece of [age]yo manmeat on Earth, sweetie pie! Just Give it to me, I WANT IT!"
stop channel1
stop channel2
scene mcroomsex20 with dissolve
play sound "sounds/moan06.ogg"
mc "I'll make you cum in no time with my Super-Cock!"
$ milfmassagetalkslow = True

label MILFloneMassageSlow:
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
call screen milflonemassageslow()
screen milflonemassageslow():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFloneMassageFast")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFloneMassagePOVSlow")

label MILFloneMassageFast:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfast == False:
    voice "milf/room40"
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
call screen milflonemassagefast()
screen milflonemassagefast():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFloneMassageSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEnd")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFloneMassagePOVFast")

label MILFloneMassagePOVSlow:
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
call screen milflonemassagepovslow()
screen milflonemassagepovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFloneMassagePOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFloneMassageSlow")

label MILFloneMassagePOVFast:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfast == False:
    voice "milf/room40"
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
call screen milflonemassagepovfast()
screen milflonemassagepovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFloneMassagePOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFloneMassageEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFloneMassageFast")

label MILFloneMassageEnd:
hide cum
hide faster
hide slower
hide pov
hide sceneicon
play sound "sounds/moan05.mp3"
voice "milf/room41"
cm "Sweetie, I... PLEASE CUM INSIDE ME, YOU STALLION!"
mc "Sure Carol, I'm right on the edge and..."
stop channel2
scene mcroomsex21 with dissolve
play channel2 "sounds/splooge01.mp3"
play sound "sounds/boyorgasm01.mp3"
mc "...AAAAH! Here it comes!"
window hide
with fastflash
mc "And it feels so fucking good!"
scene mcroomsex22 with dissolve
voice "milf/room42"
cm "Oh dear me, is that still the same shot? You've been pumping your seed for so long already, sweetie pie!"
window hide
with hpunch
mc "Oh Fuck, can't stop NU-UU-TTING!!"
scene mcroomsex23 with dissolve
voice "milf/room43"
cm "Maybe you should dump the rest on me, I'm starting to feel a bit... bloated with young spunk!"
window hide
with fastflash
mc "Oh damn, alright, gonna try and pull it out while I'm still spewing my sauce, RHAAAA!"
scene mcroomsex24 with dissolve
stop channel2
if age >= 20:
    voice "milf/room44a"
    cm "Oh my goodness, you're splattering your potent goo all over my body!"
if age >= 18 and age <= 19:
    voice "milf/room44b"
    cm "Oh my goodness, you're splattering your potent teenage goo all over my body!"
window hide
with fastflash
voice "milf/room45"
cm "Give me more [name], DROWN YOUR FILTHY LANDLADY IN YOUR SWEET CUM!"
scene mcroomsex25 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE YOU GO, AAAHHH!"
window hide
with fastflash
voice "milf/room46"
cm "You're blasting so FURIOUSLY for your landlady, you dirty tenant!"
scene mcroomsex26 with dissolve
play sound "sounds/panting.mp3"
play channel2 "sounds/splooge02.mp3"
voice "milf/room47"
cm "You came so much inside me, sweetie pie... Oooh..."
mc "Damn, I can see that..."
scene mcroomsex40 with dissolve
play sound "sounds/slurp.mp3"
voice "milf/room48"
cm "Let me slurp as much as I can of your sweet young nectar..."
mc "There's a LOT of cum to slurp up, Carol. And I'm still HARD for you!"
scene mcroomsex41 with dissolve
stop channel2
voice "milf/room49"
cm "Mmh, then why don't you come and sit on the bed so I can take care of your massive erection..."
scene mcroomsex42 with dissolve
voice "milf/room50"
cm "I'm totally under the spell of your giant [age]yo dong right now..."
mc "That's great but my hard-on is demanding attention, Captain MILF!"
voice "milf/room51"
cm "Then I guess I'll have to lick it and taste its manly musk."
scene mommassagelickvideo with dissolve
$ renpy.pause(1.0, hard='True')
mc "Fuck Carol, your tongue... I'm in heavens!"
pause
scene mcroomsex43 with dissolve
voice "milf/room52"
cm "I just want to care of you and your needs, like a good landlady."
mc "You're the best landlady ever!"
scene mcroomsex44 with dissolve
voice "milf/room53"
cm "And I'll prove it to you, [name]. By letting you fuck me until your balls are DRAINED! Let me get on the bed for you."
scene mcroomsex45 with dissolve
mc "Are you ready to receive my mighty love muscle, Captain MILF?"
voice "milf/room54"
cm "Yes, sweetie pie. I'm going to make you cum so many times that it will finally go down and I won't be under its gorgeous spell..."
scene mcroomsex45 with dissolve
play sound "sounds/moan05.mp3"
voice "milf/room55"
cm "OOOH! I can already feel your apple-sized helmet STRETCHING my pussylips... Be careful with that thing, [name]!"
$ milflonetalk01slow = True

label MILFLoneNoMilfSlow:
$ milflonetalk01fast = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slow == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slow = True
window hide
show milfloneslowvideo behind milflonefastvideo
show milfloneslowvideo behind milfloneslowpovvideo
$ renpy.pause(1.0, hard='True')
hide milfloneslowpovvideo
hide milflonefastvideo
stop channel2
play channel2 "sounds/womansex03.mp3"
if milflonetalkfirst == False:
    if age >= 20:
        voice "milf/room57a"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        voice "milf/room57b"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milflonetalkfirst = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500  
call screen milflonenomilfslow()
screen milflonenomilfslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVSlow") 

label MILFLoneNoMilfFast:
$ milflonetalk01slow = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fast == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fast = True
window hide
show milflonefastvideo behind milfloneslowvideo
show milflonefastvideo behind milflonefastpovvideo
$ renpy.pause(1.0, hard='True')
hide milflonefastpovvideo
hide milfloneslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonenomilffast()
screen milflonenomilffast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfPOVFast") 

label MILFLoneNoMilfPOVSlow:
$ milflonetalk01fast = False
stop channel2
play channel2 "sounds/womansex03.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slow == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slow = True
window hide
show milfloneslowpovvideo behind milflonefastpovvideo
show milfloneslowpovvideo behind milfloneslowvideo
$ renpy.pause(1.0, hard='True')    
hide milflonefastpovvideo
hide milfloneslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500   
call screen milflonenomilfpovslow()
screen milflonenomilfpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfSlow") 

label MILFLoneNoMilfPOVFast:
$ milflonetalk01slow = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fast == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fast = True
window hide
show milflonefastpovvideo behind milfloneslowpovvideo
show milflonefastpovvideo behind milflonefastvideo
$ renpy.pause(1.0, hard='True')    
hide milfloneslowpovvideo
hide milflonefastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonenomilfpovfast()
screen milflonenomilfpovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MILFLoneNoMilfPOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MILFLoneNoMilfFast") 
        
label MILFLoneNoMilfCum:
$ milflonetalk01slow = True
$ dpmilfcame += 1
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
play sound "sounds/boymoan02.mp3"
mc "I feel like I'm ready to blow a load, Carol!"
voice "milf/room59"
cm "Then pump your seed inside your landlady!"
scene milflonenocum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "Fuck, I'm cumming! RHAAA!"
window hide
with hpunch
voice "milf/room60"
cm "Dear Lord, your shots are just so POWERFUL, [name]!"
scene milflonenocum02 with dissolve
mc "Take these now, AAAH! I'm not done by a LONG SHOT!"
window hide
with fastflash
voice "milf/room61"
cm "Cover my back in your HOT, YOUNG, BALL-BATTER!"
scene milflonenocum03 with dissolve
stop channel1
mc "There you go, Catain MILF, RHOOO!"
window hide
with fastflash
voice "milf/room62"
cm "You're really cumming like a STALLION!"
window hide
with fastflash
mc "Still more shots BLASTING, RHAAA!"
play sound "sounds/moan05.mp3"
window hide
with fastflash
voice "milf/room63"
cm "I'm cumming too, just from the feel of those MASSIVE cumshots WHACKING my body! OOOH!"
scene milflonecum04 with dissolve
stop channel2
mc "Getting back in that tight snatch of yours, Carol!"
voice "milf/room64"
cm "Damn, you're still raring to go! How am I going to TAME your manly BEAST?"
jump MilfCameSlow   

label MilfCameSlow:
$ milflonetalk01fast = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slow == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slow = True
window hide
show milflonecumslowvideo behind milflonecumfastvideo
show milflonecumslowvideo behind milflonecumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide milflonecumpovslowvideo
hide milflonecumfastvideo
stop channel2
play channel2 "sounds/womansex03.mp3"
if milflonetalkfirst == False:
    if age >= 20:
        voice "milf/room57a"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        voice "milf/room57b"
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milflonetalkfirst = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500  
call screen milflonecumnomilfslow()
screen milflonecumnomilfslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCameFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVSlow") 

label MilfCameFast:
$ milflonetalk01slow = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fast == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fast = True
window hide
show milflonecumfastvideo behind milflonecumslowvideo
show milflonecumfastvideo behind milflonecumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide milflonecumpovfastvideo
hide milflonecumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonecumnomilffast()
screen milflonecumnomilffast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MilfCameCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCameSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCamePOVFast") 

label MilfCamePOVSlow:
$ milflonetalk01fast = False
stop channel2
play channel2 "sounds/womansex03.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01slow == False:
    voice "milf/room56"
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milflonetalk01slow = True
window hide
show milflonecumpovslowvideo behind milflonecumpovfastvideo
show milflonecumpovslowvideo behind milflonecumslowvideo
$ renpy.pause(1.0, hard='True')    
hide milflonecumpovfastvideo
hide milflonecumslowvideo
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500   
call screen milflonecumnomilfpovslow()
screen milflonecumnomilfpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVFast") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCameSlow") 

label MilfCamePOVFast:
$ milflonetalk01slow = False
stop channel2
play channel2 "sounds/womansex04.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
if milflonetalk01fast == False:
    voice "milf/room58"
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milflonetalk01fast = True
window hide
show milflonecumpovfastvideo behind milflonecumpovslowvideo
show milflonecumpovfastvideo behind milflonecumfastvideo
$ renpy.pause(1.0, hard='True')    
hide milflonecumpovslowvideo
hide milflonecumfastvideo
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen milflonecumnomilfpovfast()
screen milflonecumnomilfpovfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("MilfCameCum")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("MilfCamePOVSlow") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("MilfCameFast") 
        
label MilfCameCum:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
play sound "sounds/boymoan02.mp3"
mc "Gonna cum again, Captain MILF, I can feel it!"
voice "milf/room65"
cm "Then pump your sweet boyseed inside me and all over my back again!"
scene milflonecum01 with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge01.mp3"
mc "FLOODING YOUR SNATCH AGAIN, RHAAAA!"
window hide
with hpunch
voice "milf/room66"
cm "I can feel it [name], you're pumping all that sweet young cum inside me, you're such a good boy!"
scene milflonecum02 with dissolve
mc "Her's more for you, DEEP INSIDE, AAAH!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
voice "milf/room67"
cm "I'm coming too, your giant horsedick is sssooo virile!"
scene milflonecum03 with dissolve
stop channel1
mc "I'll add some more to your already spunk-covered back, FU-UUU-CK!"
window hide
with fastflash
voice "milf/room68"
cm "You shouldn't swear when you're blasting your spunk all over your horny landlady's body, my sweet tenant!"
window hide
with fastflash
mc "Sorry Carol, just can't stop NUTTING!"
stop channel2
play sound "sounds/panting.mp3"
scene milflonecumend01 with dissolve
mc "That's it, I think you finally drained me... After I came 3 MEGA-LOADS..."
scene milflonecumend02 with dissolve
play sound "sounds/moan03.mp3"
voice "milf/room69"
cm "I'm very proud of you, [name]. You've definitely MASTERED Level02 Super-Studliness! * slurp *"
scene milflonecumend03 with dissolve
stop sound
voice "milf/room70"
cm "Now I'd better go back to my room and clean up before some Super-Villains attack the compound."
mc "With my new BIGGER muscles, I could defeat anyone that dares set foot in our compound, Captain MILF!"
voice "milf/room71"
cm "Yeah, I know, you're VERY muscular my young sweet tenant... But you're still only Super-Strength level 02. Superman is less muscular than you but he's STRONGER..."
mc "Pff! I'll become STRONGER than this wimp in no time, mark my words!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
    
label MilfSaunaRewardHarem:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon    
stop channel1
play music "sounds/sexy14.mp3"
scene compoundmilfnightseduction02
show milfnewlingerie01
with dissolve
if milfharem == False:
    cm "Hello sweetie pie... You're back to visit your VERY grateful landlady... Who is now ready to join your extensive and well-deserved HAREM!"
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlmilf at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ milfharem = True
    mc "Alright! BINGO!"
    hide milfnewlingerie01
    show milfnewlingerie05:
        zoom 0.5 xpos 0.2
    with dissolve
    cm "And now we can do EVERYTHING at once for our VERY special harem night time, [name]!"
if milfharem:
    cm "Hello sweetie pie... You're back to visit your VERY grateful landlady... For a HOT HAREM SEX NIGHT!"
    mc "Precisely, Carol!"
    hide milfnewlingerie01
    show milfnewlingerie05:
        zoom 0.5 xpos 0.2
    with dissolve
    cm "Well, let's start off our very special night with some LANDLADY ANAL SEX, shall we?"
    mc "That sounds perfectly appropriate indeed for a regular landlady-tenant relationship."
jump NewMILFAnal

label MilfSaunaReward:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon    
stop channel1
play music "sounds/sexy14.mp3"
if seenmilfrewardstart and (chosemilftitjob == False or chosemilffootjob == False or chosemilfanal == False):
    scene compoundmilfnightseduction02
    show milfnewlingerie01
    with dissolve
    cm "Hello sweetie pie... You're back to visit your grateful landlady... in the evening..."
    mc "That's right, there are still rewards I haven't received..."
    hide milfnewlingerie01
    show milfnewlingerie05:
        zoom 0.5 xpos 0.2
    with dissolve
    cm "In that case, you'd better choose what you want to do for our special night time, [name]! Preferably a reward you didn't receive yet..."
    jump MilfSaunaRewardMenuB

if seenmilfrewardstart == False:
    $ seenmilfrewardstart = True
    scene compoundmilfnightseduction02
    show milfnewlingerie01
    with dissolve
    cm "Hello sweetie pie... I was wondering when you were going to come and visit your dear landlady... in the evening..."
    mc "Carol! You're wearing a..."
    hide milfnewlingerie01
    show milfnewlingerie02
    with dissolve
    cm "...sexy lingerie set for my courageous tenant who saved his landlady's life?"
    mc "Alright! Yeah, I did! I remember now!"
    hide milfnewlingerie02
    show milfnewlingerie03:
        xpos 0.2 zoom 0.5
    with dissolve
    cm "So, what do you think of this frilly set?"
    window hide
    show compoundmilfnightseduction02 blurred:
        subpixel True
        zoom 2.0
        xpos 0.4 ypos 1.0
        ease 5.5 xpos 0.42 ypos 1.3           
    show milfnewlingerie03:
        subpixel True
        zoom 1.0
        xpos -.2 ypos -1.0
        linear 6.0 xpos -.1 ypos -0.2
    with dissolve
    $ renpy.pause(5.0, hard='True')
    mc "I think... It's ideal for a landlady-tenant romp!"
    hide milfnewlingerie03
    show milfnewlingerie04:
        xpos 0.2 zoom 0.5
    with dissolve
    cm "That's such a sweet thing to say to your landlady. But have you checked the back yet?"
    window hide
    show compoundmilfnightseduction02 blurred:
        subpixel True
        zoom 2.0
        xpos 0.4 ypos 1.4
        ease 5.5 xpos 0.42 ypos 1.0           
    show milfnewlingerie04:
        subpixel True
        zoom 1.0
        xpos 0.0 ypos -0.1
        linear 6.0 xpos 0.1 ypos -1.0
    with dissolve
    $ renpy.pause(5.0, hard='True')
    mc "I'm checking it right now... Checked!"
    scene compoundmilfnightseduction02
    show milfnewlingerie05:
        xpos 0.2 zoom 0.5
    with dissolve
    cm "So I'm going to take it this is a \"yes\"?"
    window hide
    show compoundmilfnightseduction02 blurred:
        subpixel True
        zoom 2.0
        xpos 0.4 ypos 1.0
        ease 5.5 xpos 0.42 ypos 1.3           
    show milfnewlingerie05:
        subpixel True
        zoom 1.0
        xpos -0.1 ypos -1.0
        linear 6.0 xpos 0.0 ypos -0.2
    with dissolve
    $ renpy.pause(5.0, hard='True')
    mc "Oh, It's more than a \"yes\" Carol, it's a \"I want that hot hot bod NOW yes!\"!"
    jump MilfSaunaRewardMenu

label MilfSaunaRewardMenu:
scene compoundmilfnightseduction02
show milfnewlingerie05:
    zoom 0.5 xpos 0.2
with dissolve
cm "In that case, I'll even let you choose what you want to do for our special night time!"
label MilfSaunaRewardMenuB:
menu:
    "I choose a nice sumptuous landlady titjob.":
        $ chosemilftitjob = True
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "Oooh, you want my BIG tits wrapped around your HUGE cock, [name]? I can do that. Even better, I'm going to OIL myself up for it!"
        mc "Alright!"
        hide milfnewlingerie01
        show milfnewlingerie02
        with dissolve
        cm "Just stay put while I go to the bathroom and wait for me..."
        hide milfnewlingerie02 with moveoutright
        jump OilyMILFtitjob
    "I want your lovely feet to make my rod convulse with orgasmic bliss.":
        $ chosemilffootjob = True
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "Oooh, I didn't know you were a FOOT FETISHIST, [name]. I am too! And I'm going to OIL myself up to make it even more memorable for both of us!"
        hide milfnewlingerie01
        show milfnewlingerie02
        with dissolve
        cm "Just stay put while I go to the bathroom and wait for me..."
        hide milfnewlingerie02 with moveoutright
        jump OilyMILFfootjob
    "I choose... ANAL SEX!":
        $ chosemilfanal = True
        hide milfnewlingerie05
        show milfnewlingerie01
        with dissolve
        cm "I knew you might... You just can't get enough of my booty, can you? Well, I'm ready to receive a mighty anal pounding from your giant pillar, [name]!"
        mc "Alright!"
        cm "Let me just get out of this frilly lingerie outfit first... Before I put a blindfold on, so I never get to see your immense lovesword...."
        jump NewMILFAnal

label MilfSaunaRewardMenuC:
scene compoundmilfnightseduction02
show milfoillingerie05 with dissolve
cm "So, what else would you like to do my sweet tenant?"
menu:
    "I choose a nice sumptuous landlady titjob.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Oooh, you want my BIG tits wrapped around your HUGE cock, [name]? I can do that. For my HAREM MASTER!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump OilyMILFtitjobB
    "I want your feet to make my rod convulse with orgasmic bliss.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Oooh, you want my lovely little feet wrapped around your huge pole, my sweet tenant? Your landlady can do that!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump OilyMILFfootjobB
    "I choose... ANAL SEX AGAIN!":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "I knew you might... You just can't get enough of my booty, can you? Well, I'm ready to receive a mighty anal pounding from your giant pillar, [name]!"
        mc "Alright!"
        jump NewMILFAnalB
    "I choose... to have some intimate mating between my cock and your tight landlady pussy.":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        cm "Vanilla vaginal sex? Why not. We've hardly ever tried that, and a normal landlady-landboy relationship should always include wholesome sex!"
        mc "Damn right! Stop the PERVERSION!"
        hide milfoillingerie08
        show milfoillingerie06
        with dissolve
        jump NewMILFPussy
    "I choose... to go back to bed cos I'm EXHAUSTED!":
        hide milfoillingerie05
        show milfoillingerie08
        with dissolve
        if age >= 20:
            cm "I'm also rather tired. You were such a SEX BEAST tonight, sweetie!"
        if age >= 18 and age <= 19:
            cm "I'm also rather tired. You were such a TEENAGE SEX BEAST tonight, sweetie!"
        cm "So have sweet dreams, my STRONG, horse-hung tenant, I sure will!"
        stop music
        show screen calendar
        show screen statscreenicon
        show screen questscreenicon
        jump Main

label OilyMILFtitjob:
scene compoundmilfnightseduction02 blurred with fade
show milfoillingerie01 with moveinright
cm "Mmmh, I'm all oiled up for my horse-hung tenant..."
hide milfoillingerie01
show milfoillingerie02
with dissolve
if age >= 20:
    cm "Maybe you want to see a bit better the tits that will softly wrap around your mighty rod..."
if age >= 18 and age <= 19:
    cm "Maybe you want to see a bit better the tits that will softly wrap around your mighty teenage rod..."
mc "God, I'm gonna get hard..."
hide milfoillingerie02
show milfoillingerie03:
    xpos 0.2 zoom 0.5
with dissolve
cm "Not yet [name]! I can't actually {i}see{/i} your enormous fuckstick, remember?"
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.0
    ease 5.5 xpos 0.42 ypos 1.3           
show milfoillingerie03:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -1.0
    linear 6.0 xpos 0.1 ypos -0.2
with dissolve
$ renpy.pause(5.0, hard='True')
mc "But how are you supposed to give me that titjob reward without me getting HARD!!!"
scene compoundmilfnightseduction02 blurred
show milfoillingerie04:
    xpos 0.2 zoom 0.5
with dissolve
cm "Don't worry, I've thought of everything. I'll be wearing a blindfold..."
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.4
    ease 5.5 xpos 0.42 ypos 1.0           
show milfoillingerie04:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -0.1
    linear 6.0 xpos 0.1 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "That's a good idea. Especially since I'm getting hard anyway..."
scene compoundmilfnightseduction02 blurred
show milfoillingerie05
with dissolve
cm "There, I've put it on. Now you can get that massive [age]yo cock out of your thong, sweetie pie!"
mc "About time, Carol!"
play sound "sounds/ripping.mp3"
cm "Ooh, that sounds tells me you got an INSTANT BONER for your landlady!"
hide milfoillingerie05
show milfoillingerie06
with dissolve
label OilyMILFtitjobB:
mc "Damn right! Let me guide you to the bed..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm feeling something really BIG brushing against my back!"
scene milfnewtitjob01 with dissolve
mc "Now get on your knees on the floor."
scene milfnewtitjob02 with dissolve
mc "Here, let me help you guide your hand to..."
scene milfnewtitjob03 with dissolve
mc "...my ROCK-HARD shaft!"
cm "Oooh, it feels so HUGE, my over-hung tenant!"
scene milfnewtitjob04 with dissolve
cm "I have to imagine I'm holding something else. Like a large iron bar."
mc "Yeah, that sounds about right. Now get those tits around that giant iron bar!"
scene milfnewtitjob05 with dissolve
cm "Like this, [name]? Is the iron bar fitting snugly between my breasts?"
mc "It sure is, Carol..."

play channel1 "sounds/wetmassage.mp3"
$ milftitjobsofter = False
$ milftitjobharder = False

label MilfTitjobSlow:
play channel2 "sounds/boymoan02.mp3"
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharder:
    mc "Let's go back to some softer titfucking, Carol..."
    window hide
    show milftittransitionsoftervideo
    $ renpy.pause(.5, hard='True')
    scene milfnewtitjob05    
    $ milftitjobharder = False
show milftitjobslowvideo behind milftitjobfastvideo
show milftitjobslowvideo behind milftitjobharderslowvideo
$ renpy.pause(1.0, hard='True')
hide milftitjobfastvideo
hide milftitjobharderslowvideo
with dissolve
if milftitjobsofter == False:
    cm "Does it feel good, [name]?"
    mc "It sure does, Carol!"
    $ milftitjobsofter = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen milftitjobslow()
screen milftitjobslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitjobHarderSlow")

label MilfTitjobFast:
play channel2 "sounds/boymoan02.mp3"
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharder:
    mc "Let's go back to some softer titfucking, Carol..."
    window hide
    show milftittransitionsoftervideo
    $ renpy.pause(.5, hard='True')
    scene milfnewtitjob05    
    $ milftitjobharder = False
show milftitjobfastvideo behind milftitjobslowvideo
show milftitjobfastvideo behind milftitjobharderfastvideo
$ renpy.pause(1.0, hard='True')
hide milftitjobslowvideo
hide milftitjobharderfastvideo
with dissolve
if milftitjobsofter == False:
    cm "Does it feel good, [name]?"
    mc "It sure does, Carol!"
    $ milftitjobsofter = True
window hide
pause
show slower:
     xpos 50 ypos 500     
show harder:
     xpos 1700 ypos 500     
call screen milftitjobfast()
screen milftitjobfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfTitjobHarderFast")

label MilfTitjobHarderSlow:
$ milftitjobsofter = False
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharder == False:
    mc "I just want to bury my dong between those soft mounds!"
    cm "Oooh, I'll move forward and make sure MORE titflesh rubs against it then!"
    $ milftitjobharder = True
    show milftittransitionhardervideo
    $ renpy.pause(.5, hard='True')
    scene milftittransitionharderend01
show milftitjobharderslowvideo behind milftitjobslowvideo
show milftitjobharderslowvideo behind milftitjobharderfastvideo
show milftitjobharderslowvideo behind milftittransitionhardervideo
$ renpy.pause(.5, hard='True')
hide milftitjobslowvideo
hide milftitjobharderfastvideo
hide milftittransitionhardervideo
with dissolve
play channel2 "sounds/boyorgasm01.mp3"
window hide
pause
show cum:
     xpos 1750 ypos 1020
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen milftitjobharderslow()
screen milftitjobharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobSlow")

label MilfTitjobHarderFast:
$ milftitjobsofter = False
window hide
hide cum
hide slower
hide faster
hide harder
hide softer
if milftitjobharder == False:
    mc "I just want to bury my dong between those soft mounds!"
    cm "Oooh, I'll move forward and make sure MORE titflesh rubs against it then!"
    $ milftitjobharder = True
    show milftittransitionhardervideo
    $ renpy.pause(.5, hard='True')
    scene milftittransitionharderend01
show milftitjobharderfastvideo behind milftitjobfastvideo
show milftitjobharderfastvideo behind milftitjobharderslowvideo
$ renpy.pause(0.5, hard='True')
hide milftitjobfastvideo
hide milftitjobharderslowvideo
with dissolve
play channel2 "sounds/boyorgasm01.mp3"
window hide
pause
show cum:
     xpos 1750 ypos 1020
show slower:
     xpos 50 ypos 500     
show softer:
     xpos 1700 ypos 500     
call screen milftitjobharderfast()
screen milftitjobharderfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfTitjobEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfTitjobFast")

label MilfTitjobEnd:
hide nexticon
hide slower
hide faster
hide harder
hide softer
cm "I can feel your shaft trembling... Are you going to come for me?"
mc "Oh God, I..."
scene milfnewtitjobcum01 with dissolve
stop channel2
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "...AAAAH!"
window hide
with fastflash
cm "Are you blasting for your landlady? Her funbags wrapped around your [age]yo horny cock was just too much?"
scene milfnewtitjobcum02 with dissolve
mc "Y...YES! Your tits are the BEST, Carol! RHAAA!"
window hide
with hpunch
cm "Oooh, I can FEEL the heavy splatters of your HOT SPUNK on my tits now!"
scene milfnewtitjobcum03 with dissolve
play sound "sounds/moan02.mp3"
cm "Your shaft is CONVULSING even more and I can tell it's RAINING cum on me!"
window hide
with fastflash
mc "AAAH! Those HUGE TITS!!!! I can't stop NUTTING!!!"
scene milfnewtitjobcum04 with dissolve
cm "Ooh, so you're coming like a STALLION because of my mounds of titflesh rubbing against your veiny rod? Is that what you're saying, [name]?"
window hide
with vpunch
mc "Y... YYYYEEESSSS! RHAAAA!"
scene milfnewtitjobcum05 with dissolve
play sound "sounds/lick01.ogg"
cm "You're STILL pumping that load for me?"
window hide
with fastflash
if age >= 20:
    cm "Mmmmh, I need to get my tongue on that convulsing rod!"
if age >= 18 and age <= 19:
    cm "Mmmmh, I need to get my tongue on that convulsing teenage rod!"
scene milfnewtitjobcum06 with dissolve
stop channel1
play sound "sounds/slurp.mp3"
cm "Mmmh, it's so tasty, [name]! And I can tell you really came a LOT, didn't you?"
mc "I... I guess I did... Uuuhhh..."
scene milfnewtitjobcum07 with dissolve
play sound "sounds/panting.mp3"
cm "Did your landlady totally drain your fat balls?"
mc "Gggg... Yes, Carol, you were great..."
if milfharem:
    cm "But we're not done yet are we? That huge thing can remain HARD for some more fun?"
    mc "Damn right!"
    jump MilfSaunaRewardMenuC               
cm "Well, I guess you got your reward for the evening, you'd better go to your room, I need to get back in VIGILANT SUPER-HEROINE mode."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label OilyMILFfootjob:
scene compoundmilfnightseduction02 blurred with fade
show milfoillingerie01 with moveinright
cm "Mmmh, I'm all oiled up for my horse-hung tenant..."
mc "I'm about to get SO HARD for you, Carol!"
hide milfoillingerie01
show milfoillingerie03:
    xpos 0.2 zoom 0.5
with dissolve
cm "Not yet [name]! I can't actually {i}see{/i} your enormous fuckstick, remember?"
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.0
    ease 5.5 xpos 0.42 ypos 1.3           
show milfoillingerie03:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -1.0
    linear 6.0 xpos 0.1 ypos -0.2
with dissolve
$ renpy.pause(5.0, hard='True')
mc "But how are you supposed to give me that titjob reward without me getting HARD!!!"
scene compoundmilfnightseduction02 blurred
show milfoillingerie04:
    xpos 0.2 zoom 0.5
with dissolve
cm "Don't worry, your landlady has thought of everything. I'll be wearing a blindfold..."
window hide
show compoundmilfnightseduction02 blurred:
    subpixel True
    zoom 2.0
    xpos 0.4 ypos 1.4
    ease 5.5 xpos 0.42 ypos 1.0           
show milfoillingerie04:
    subpixel True
    zoom 1.0
    xpos 0.0 ypos -0.1
    linear 6.0 xpos 0.1 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "That's a good idea. Especially since I'm getting hard anyway..."
scene compoundmilfnightseduction02 blurred
show milfoillingerie05
with dissolve
cm "There, I've put it on. Now you can get that massive [age]yo cock out of your thong, sweetie pie!"
mc "About time!"
play sound "sounds/ripping.mp3"
cm "Ooh, that sounds tells me you got an INSTANT BONER for your landlady!"
hide milfoillingerie05
show milfoillingerie06
with dissolve
label OilyMILFfootjobB:
mc "Damn right! Let me guide you to the bed, Carol..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm feeling something really BIG brushing against my back, [name]!"
scene milffootjob01 with dissolve
mc "There, get on the bed while I place your feet..."
scene milffootjob02 with dissolve
mc "...around my fat dong!"
cm "Mmmh, I can FEEL the warmth of your HOT shaft on my little feet..."
scene milffootjob03 with dissolve
mc "Yeah, let's start this. Your oily feet on my rock-hard dong!"
play channel2 "sounds/wank.mp3"

label MilfFootjobSlow:
$ milffootjobfast = False
$ milffootharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milffootjobslow == False and milffootstart:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslow = True
window hide
show milffootjobslowvideo behind milffootjobfastvideo
show milffootjobslowvideo behind milffootjobslowpovvideo
show milffootjobslowvideo behind milffootjobharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide milffootjobfastvideo
hide milffootjobslowpovvideo
hide milffootjobharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if milffootjobslow == False and milffootstart == False:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslow = True
    $ milffootstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobslow()
screen milffootjobslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVSlow")

label MilfFootjobFast:
$ milffootharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milffootjobfast == False:
    cm "You can use my feet to jerk yourself off faster if you want, sweetie pie!"
    $ milffootjobfast = True
show milffootjobfastvideo behind milffootjobslowvideo
show milffootjobfastvideo behind milffootjobfastpovvideo
show milffootjobfastvideo behind milffootjobharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowvideo
hide milffootjobfastpovvideo
hide milffootjobharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milffootjobfast()
screen milffootjobfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVFast")

label MilfFootjobPOVSlow:
$ milffootharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milffootjobslow == False:
    mc "Oh yeah, just like that..."
    if age >= 20:
        cm "You like my feet on your giant iron bar, don't you?"
    if age >= 18 and age <= 19:
        cm "You like my feet on your giant teenage iron bar, don't you?"
    $ milffootjobslow = True
show milffootjobslowpovvideo behind milffootjobslowvideo
show milffootjobslowpovvideo behind milffootjobfastpovvideo
show milffootjobslowpovvideo behind milffootjobharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowvideo
hide milffootjobfastpovvideo
hide milffootjobharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobslowpov()
screen milffootjobslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobSlow")

label MilfFootjobPOVFast:
$ milffootharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milffootjobfast == False:
    cm "You can use my feet to jerk yourself off faster if you want, sweetie pie!"
    $ milffootjobfast = True
window hide
show milffootjobfastpovvideo behind milffootjobslowpovvideo
show milffootjobfastpovvideo behind milffootjobfastvideo
show milffootjobfastpovvideo behind milffootjobharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milffootjobslowpovvideo
hide milffootjobfastvideo
hide milffootjobharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milffootjobfastpov()
screen milffootjobfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobFast")

label MilfFootjobHarderSlow:
if milffootharder == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharder = True        
window hide
show milffootjobharderslowvideo behind milffootjobharderfastvideo
show milffootjobharderslowvideo behind milffootjobharderpovslowvideo
show milffootjobharderslowvideo behind milffootjobslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderfastvideo
hide milffootjobharderpovslowvideo
hide milffootjobslowvideo
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
call screen milffootjobharderslow()
screen milffootjobharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCum")

label MilfFootjobHarderFast:
if milffootharder == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharder = True        
window hide
show milffootjobharderfastvideo behind milffootjobharderslowvideo
show milffootjobharderfastvideo behind milffootjobharderpovfastvideo
show milffootjobharderfastvideo behind milffootjobfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderslowvideo
hide milffootjobharderpovfastvideo
hide milffootjobfastvideo
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
call screen milffootjobharderfast()
screen milffootjobharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCum")

label MilfFootjobHarderPOVSlow:
if milffootharder == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharder = True        
window hide
show milffootjobharderpovslowvideo behind milffootjobharderslowvideo
show milffootjobharderpovslowvideo behind milffootjobharderpovfastvideo
show milffootjobharderpovslowvideo behind milffootjobslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderslowvideo
hide milffootjobharderpovfastvideo
hide milffootjobslowpovvideo
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
call screen milffootjobharderpovslow()
screen milffootjobharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCum")

label MilfFootjobHarderPOVFast:
if milffootharder == False:
    mc "I need to foot-jerk myself off HARDER!"
    cm "Then go ahead, sweetie pie, my feet are there just for this!"
    $ milffootharder = True        
window hide
show milffootjobharderpovfastvideo behind milffootjobharderpovslowvideo
show milffootjobharderpovfastvideo behind milffootjobharderfastvideo
show milffootjobharderpovfastvideo behind milffootjobfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milffootjobharderpovslowvideo
hide milffootjobharderfastvideo
hide milffootjobfastpovvideo
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
call screen milffootjobharderpovfast()
screen milffootjobharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfFootjobHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfFootjobPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfFootjobHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfFootjobCum")

label MilfFootjobCum:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
play sound "sounds/boymoan02.mp3"
mc "That's it Carol, I think I'm about to..."
scene milffootjobcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "... CUUUUMMMM!!!"
window hide
with fastflash
cm "I want you to COVER your dear landlady in your fat load, you hear me?"
scene milffootjobcum02 with dissolve
mc "FUCK, AAAH!!!"
window hide
with hpunch
cm "Your iron bar is like a CUM-FIREHOSE!"
scene milffootjobcum03 with dissolve
if age >= 20:
    cm "I can feel really HEAVY splatters of spunk raining down on my back!"
if age >= 18 and age <= 19:
    cm "I can feel really HEAVY splatters of teenage spunk raining down on my back!"
window hide
with fastflash
mc "UUUH, There's MORE!"
scene milffootjobcum04 with dissolve
play sound "sounds/wow.mp3"
cm "Oh, wow! You're cumming like a WILD BRONCO for your landlady!"
window hide
with vpunch
mc "Just a... few more shots, RHAAA!"
scene milffootjobcum05 with dissolve
play sound "sounds/panting.mp3"
cm "Mmmh, all that slimy red-hot cream dripping down my back.... And my hair... You really made a CUM-MESS out of your landlady, didn't you?"
mc "Yeah, sorry... I just..."
cm "Don't you apologize sweetheart, it's perfectly natural for a horny young tenant like you to blast such a powerful load on his landlady."
if milfharem:
    cm "I'll clean everything up and we can continue having some HOT harem SEXY TIMES!"
    jump MilfSaunaRewardMenuC
cm "I'll clean everything up. You can go back to your room and have a good night's sleep, sweetie pie!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label NewMILFAnal:
scene milfnewanal01 with dissolve
cm "But first, I'm going to lather my big tits with some oily lotion, you don't mind waiting a bit [name]?"
mc "Not at all, not at all..."
scene milfnewanal02 with dissolve
cm "And now on the legs..."
mc "Hurry up Carol, I don't think I can hold off getting hard much longer!"
scene milfnewanal03 with dissolve
cm "That's it, sweetie, the blindfold is on and I'm ready! You can get hard now and join me on the bed..."
play sound "sounds/ripping.mp3"
mc "Finally..."
label NewMILFAnalB:
scene milfnewanal04 with dissolve
play sound "sounds/moan02.mp3"
cm "Oooh, is that your hand on my breast, [name]?"
mc "Yes it is. I just want to play with those oiled-up funbags a bit first..."
cm "Then kiss me while you fondle my giant funbags..."
scene milfnewanal05 with dissolve
play sound "sounds/kiss.mp3"
pause
scene milfnewanal06 with dissolve
play sound "sounds/kiss.mp3"
cm "Keep going, you're doing good. You're becoming such a SUPER-SEDUCER!"
scene milfnewanal07 with dissolve
play sound "sounds/moan01.mp3"
cm "Oooh, [name]! Your tongue on my breast... Mmmh..."
scene milfnewanal08 with dissolve
play sound "sounds/lick01.ogg"
cm "You're playing with my sensitive nipple... Aaaah... You're making me so horny! I just want you to FUCK ME now!"
mc "ALright, let's get into ANAL DESTRUCTION POSITIONS then!"
scene milfnewanal09 with dissolve
mc "You're going to have to really open that backdoor up, Carol!"
cm "Ooh, what did I let myself into..."
scene milfnewanal10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/moan01.mp3"
pause
mc "I'll help you by slowly inserting my lubricated glans..."
scene milfnewanal11 with dissolve
play sound "sounds/moan04.ogg"
cm "AAAH!"
mc "And a few inches of my ARM-THICK [age]yo MEGA-DONG!"

label MilfNewAnalSlow:
$ milfnewanalfast = False
$ milfanalharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewanalslow == False:
    if age >= 20:
        cm "Please go slowly so that I can get used to the size of your MASSIVE ass-breaker..."
    if age >= 18 and age <= 19:
        cm "Please go slowly so that I can get used to the size of your MASSIVE teenage ass-breaker..."
    $ milfnewanalslow = True
window hide
show milfnewanalslowvideo behind milfnewanalfastvideo
show milfnewanalslowvideo behind milfnewanalslowpovvideo
show milfnewanalslowvideo behind milfnewanalharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalfastvideo
hide milfnewanalslowpovvideo
hide milfnewanalharderslowvideo
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
call screen milfnewanalslow()
screen milfnewanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVSlow")

label MilfNewAnalFast:
$ milfanalharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewanalfast == False:
    cm "Go on, now I'm ready for your monster rod to fuck my ass FASTER!"
    $ milfnewanalfast = True
show milfnewanalfastvideo behind milfnewanalslowvideo
show milfnewanalfastvideo behind milfnewanalfastpovvideo
show milfnewanalfastvideo behind milfnewanalharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowvideo
hide milfnewanalfastpovvideo
hide milfnewanalharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewanalfast()
screen milfnewanalfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVFast")

label MilfNewAnalPOVSlow:
$ milfanalharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewanalslow == False:
    if age >= 20:
        cm "Please go slowly so that I can get used to the size of your MASSIVE ass-breaker..."
    if age >= 18 and age <= 19:
        cm "Please go slowly so that I can get used to the size of your MASSIVE teenage ass-breaker..."
    $ milfnewanalslow = True
show milfnewanalslowpovvideo behind milfnewanalslowvideo
show milfnewanalslowpovvideo behind milfnewanalfastpovvideo
show milfnewanalslowpovvideo behind milfnewanalharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowvideo
hide milfnewanalfastpovvideo
hide milfnewanalharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalslowpov()
screen milfnewanalslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalSlow")

label MilfNewAnalPOVFast:
$ milfanalharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewanalfast == False:
    cm "Go on, now I'm ready for your monster rod to fuck my ass FASTER!"
    $ milfnewanalfast = True
window hide
show milfnewanalfastpovvideo behind milfnewanalslowpovvideo
show milfnewanalfastpovvideo behind milfnewanalfastvideo
show milfnewanalfastpovvideo behind milfnewanalharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewanalslowpovvideo
hide milfnewanalfastvideo
hide milfnewanalharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewanalfastpov()
screen milfnewanalfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalFast")

label MilfNewAnalHarderSlow:
if milfanalharder == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharder = True        
window hide
show milfnewanalharderslowvideo behind milfnewanalharderfastvideo
show milfnewanalharderslowvideo behind milfnewanalharderpovslowvideo
show milfnewanalharderslowvideo behind milfnewanalslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderfastvideo
hide milfnewanalharderpovslowvideo
hide milfnewanalslowvideo
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
call screen milfnewanalharderslow()
screen milfnewanalharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCum")

label MilfNewAnalHarderFast:
if milfanalharder == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharder = True        
window hide
show milfnewanalharderfastvideo behind milfnewanalharderslowvideo
show milfnewanalharderfastvideo behind milfnewanalharderpovfastvideo
show milfnewanalharderfastvideo behind milfnewanalfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderslowvideo
hide milfnewanalharderpovfastvideo
hide milfnewanalfastvideo
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
call screen milfnewanalharderfast()
screen milfnewanalharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCum")

label MilfNewAnalHarderPOVSlow:
if milfanalharder == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharder = True        
window hide
show milfnewanalharderpovslowvideo behind milfnewanalharderslowvideo
show milfnewanalharderpovslowvideo behind milfnewanalharderpovfastvideo
show milfnewanalharderpovslowvideo behind milfnewanalslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderslowvideo
hide milfnewanalharderpovfastvideo
hide milfnewanalslowpovvideo
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
call screen milfnewanalharderpovslow()
screen milfnewanalharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCum")

label MilfNewAnalHarderPOVFast:
if milfanalharder == False:
    mc "Are you ready to take it up the ass HARDER, Carol?"
    cm "Not really sweetie pie, but my ass is YOUR reward so pound it as hard as you wish!"
    $ milfanalharder = True        
window hide
show milfnewanalharderpovfastvideo behind milfnewanalharderpovslowvideo
show milfnewanalharderpovfastvideo behind milfnewanalharderfastvideo
show milfnewanalharderpovfastvideo behind milfnewanalfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewanalharderpovslowvideo
hide milfnewanalharderfastvideo
hide milfnewanalfastpovvideo
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
call screen milfnewanalharderpovfast()
screen milfnewanalharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewAnalHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewAnalPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewAnalHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewAnalCum")

label MilfNewAnalCum:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "Gonna nut inside that tight ass!"
cm "Go on, fill me up with your sweet cum!"
scene milfanalnewcum01 with dissolve
stop channel1
play channel2 "sounds/splooge01.mp3"
play channel1 "v031/boyorgasm02.mp3"
mc "Here it CO-O-MES!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
cm "AAAH, it's so STRONG!"
scene milfanalnewcum02 with dissolve
play sound "sounds/moan06.ogg"
cm "Your landlady loves your cum, [name]! AAAH!"
window hide
with hpunch
mc "RHAAA! Fuck yeah, anal cum-plosion!"
scene milfanalnewcum03 with dissolve
play sound "sounds/womancum01.mp3"
cm "Oooh, that's just so naughty, it's making me come too!"
window hide
with fastflash
mc "Yeah, cum with me Carol, AAAAH!"
scene milfanalnewcum04 with dissolve
cm "You're coming so DEEP inside my ass!"
window hide
with vpunch
mc "AAAH!"
scene milfanalnewcum05 with dissolve
mc "Here, a few more shots for you!"
window hide
with fastflash
cm "You're such a good boy, coming so much for your dear old landlady!"
scene milfanalnewcum06 with dissolve
stop channel1
play sound "sounds/panting.mp3"
stop channel2
mc "That's it, I gave you all I had... Phew..."
play sound "sounds/splat.ogg"
cm "I can see that. My ass is leaking like a cum-faucet..."
scene milfanalnewcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
if milfharem:
    cm "I can Super-Sense that your monster dong is still READY for some more HAREM SEX! You're such a STALLION, my sweet tenant!"
    mc "Damn right!"
    jump MilfSaunaRewardMenuC
cm "I'm going to have to take the blindfold off to clean up all this cummy mess on my bed, [name]. You'd better leave so I don't see what caused it..."
mc "Sure Carol, good night then. And thanks for offering me your ass as a reward..."
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label NewMILFPussy:
mc "Let me guide you to the bed, Carol..."
hide milfoillingerie06
show milfoillingerie07
with dissolve
cm "I'm going to have to imagine that it's not your enormous fuckstick I feel against my back."
mc "Not at all, it's...err... A piece of large tubing I was carrying around to fix your plumbing."
scene milfoilpussy01:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
cm "I prefer that... My pussy is already so... WET!"
scene milfoilpussy02 with dissolve
mc "Let me inspect the grounds first... Yes, I see the problem. You have some leakage."
cm "Ooh, can you do something about it?"
mc "I will attempt a sealing procedure. I must get underneath you for easier access."
scene milfoilpussy03 with dissolve
play sound "sounds/moan02.mp3"
cm "Mmmh, you're such handyman, my sweet tenant!"
mc "In a tongue-in-cheek way, yes."
scene milfoilpussy04 with dissolve
play sound "sounds/moan05.mp3"
cm "Aaaah! Is it working?"
mc "I don't know yet, I feel some rumbling down the pipe..."
scene milfoilpussy05 with dissolve
play sound "sounds/womancum02.mp3"
cm "Ooooh!"
mc "I fear the leak is more severe than previously anticipated."
scene milfoilpussy06 with dissolve
cm "I sure hope you have the tools to fix it!"
mc "I've brought the biggest one available on the market. It should be to your satisfaction, Carol."
scene milfoilpussy07 with dissolve
play sound "sounds/moan02.mp3"
cm "Ooh, what are you doing naughty boy? You're so STRONG!"
mc "Sorry, I couldn't resist..."
scene milfoilpussy08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/lick01.ogg"
mc "And I can't resist this either. But it's time to lay on your back and start the procedure..."
cm "Alright, sweetie pie! I entrust my body into your hands. And BIG tool."
scene milfoilpussy09 with dissolve
cm "I feel something slimy falling on my tits..."
mc "Yeah, I'm preparing the lubricant. Gonna need LOTS of it to clean that clogged pipe!"
scene milfoilpussy10 with dissolve
cm "Ooh, now I feel something real BIG rubbing against my tender pussylips..."
mc "Yep, that's the BIG tool I was talking about."
scene milfoilpussy11 with dissolve
cm "It's INSIDE me! AAAH, it's so HUGE!"
mc "Need it that size for maximum friction! Here we go, Carol!"

label MilfNewPussySlow:
$ milfnewpussyfast = False
$ milfpussyharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewpussyslow == False:
    mc "Just relax while I start de-clogging that DEEP pipe of yours, Carol!"
    $ milfnewpussyslow = True
window hide
show milfnewpussyslowvideo behind milfnewpussyfastvideo
show milfnewpussyslowvideo behind milfnewpussyslowpovvideo
show milfnewpussyslowvideo behind milfnewpussyharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyfastvideo
hide milfnewpussyslowpovvideo
hide milfnewpussyharderslowvideo
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
call screen milfnewpussyslow()
screen milfnewpussyslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVSlow")

label MilfNewPussyFast:
$ milfpussyharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewpussyfast == False:
    cm "Uuuh, I can feel your TOOL being RAMMED right up inside me!"
    $ milfnewpussyfast = True
show milfnewpussyfastvideo behind milfnewpussyslowvideo
show milfnewpussyfastvideo behind milfnewpussyfastpovvideo
show milfnewpussyfastvideo behind milfnewpussyharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowvideo
hide milfnewpussyfastpovvideo
hide milfnewpussyharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen milfnewpussyfast()
screen milfnewpussyfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussySlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVFast")

label MilfNewPussyPOVSlow:
$ milfpussyharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if milfnewpussyslow == False:
    mc "Just relax while I start de-clogging that DEEP pipe of yours, Carol!"
    $ milfnewpussyslow = True
show milfnewpussyslowpovvideo behind milfnewpussyslowvideo
show milfnewpussyslowpovvideo behind milfnewpussyfastpovvideo
show milfnewpussyslowpovvideo behind milfnewpussyharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowvideo
hide milfnewpussyfastpovvideo
hide milfnewpussyharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyslowpov()
screen milfnewpussyslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussySlow")

label MilfNewPussyPOVFast:
$ milfpussyharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if milfnewpussyfast == False:
    cm "Uuuh, I can feel your TOOL being RAMMED right up inside me!"
    $ milfnewpussyfast = True
window hide
show milfnewpussyfastpovvideo behind milfnewpussyslowpovvideo
show milfnewpussyfastpovvideo behind milfnewpussyfastvideo
show milfnewpussyfastpovvideo behind milfnewpussyharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan01.mp3"
hide milfnewpussyslowpovvideo
hide milfnewpussyfastvideo
hide milfnewpussyharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen milfnewpussyfastpov()
screen milfnewpussyfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyFast")

label MilfNewPussyHarderSlow:
if milfpussyharder == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharder = True        
window hide
show milfnewpussyharderslowvideo behind milfnewpussyharderfastvideo
show milfnewpussyharderslowvideo behind milfnewpussyharderpovslowvideo
show milfnewpussyharderslowvideo behind milfnewpussyslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderfastvideo
hide milfnewpussyharderpovslowvideo
hide milfnewpussyslowvideo
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
call screen milfnewpussyharderslow()
screen milfnewpussyharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussySlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCum")

label MilfNewPussyHarderFast:
if milfpussyharder == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharder = True        
window hide
show milfnewpussyharderfastvideo behind milfnewpussyharderslowvideo
show milfnewpussyharderfastvideo behind milfnewpussyharderpovfastvideo
show milfnewpussyharderfastvideo behind milfnewpussyfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderslowvideo
hide milfnewpussyharderpovfastvideo
hide milfnewpussyfastvideo
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
call screen milfnewpussyharderfast()
screen milfnewpussyharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCum")

label MilfNewPussyHarderPOVSlow:
if milfpussyharder == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharder = True        
window hide
show milfnewpussyharderpovslowvideo behind milfnewpussyharderslowvideo
show milfnewpussyharderpovslowvideo behind milfnewpussyharderpovfastvideo
show milfnewpussyharderpovslowvideo behind milfnewpussyslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderslowvideo
hide milfnewpussyharderpovfastvideo
hide milfnewpussyslowpovvideo
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
call screen milfnewpussyharderpovslow()
screen milfnewpussyharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCum")

label MilfNewPussyHarderPOVFast:
if milfpussyharder == False:
    mc "I'm gonna need to PLUG THAT PIPE REAL HARD!"
    cm "If it's necessary, then go for it, my sweet handyman tenant!"
    $ milfpussyharder = True        
window hide
show milfnewpussyharderpovfastvideo behind milfnewpussyharderpovslowvideo
show milfnewpussyharderpovfastvideo behind milfnewpussyharderfastvideo
show milfnewpussyharderpovfastvideo behind milfnewpussyfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide milfnewpussyharderpovslowvideo
hide milfnewpussyharderfastvideo
hide milfnewpussyfastpovvideo
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
call screen milfnewpussyharderpovfast()
screen milfnewpussyharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MilfNewPussyHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MilfNewPussyPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MilfNewPussyHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MilfNewPussyCum")

label MilfNewPussyCum:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "Full-blown pressure down the hose coming!"
cm "I'm bracing myself for it!"
scene milfoilpussycum01 with dissolve
stop channel1
play channel2 "sounds/splooge01.mp3"
play channel1 "v031/boyorgasm02.mp3"
mc "BLASTING! RHAAA!!!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
cm "AAAH, it's a DELUGE!"
scene milfoilpussycum02 with dissolve
play sound "sounds/moan06.ogg"
cm "My insides are turning RED-HOT from your HUGE POUNDING TOOL!"
window hide
with hpunch
mc "Hold on, I'm gonna..."
scene milfoilpussycum03 with dissolve
play sound "sounds/womancum01.mp3"
mc "...COME BIG TIME, AAAH!"
window hide
with fastflash
play sound "sounds/womancum02.mp3"
cm "So much for me, I'm CONVULSING!"
scene milfoilpussycum04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
cm "I'm getting PUMPED FULL!"
window hide
with vpunch
mc "CAN'T HOLD THE HOSE STEADY! AAAH!"
scene milfoilpussycum05 with dissolve
stop channel2
mc "It slipped out but I'm still at FULL BLAST POWER, RHAAA!!!"
window hide
with fastflash
cm "That's because you've filled me up so full of CREAM!"
scene milfoilpussycum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "I'm gonna say the procedure worked and that your pipes are cleaned..."
play sound "sounds/moan02.mp3"
cm "Uuuhh..."
scene milfoilpussycum07 with dissolve
cm "I feel there's still a MASSIVE leakage down there."
mc "Yeah, but it's the good type."
cm "Is your tool ready for more handiwork?"
mc "Of course, Carol!"
jump MilfSaunaRewardMenuC               
