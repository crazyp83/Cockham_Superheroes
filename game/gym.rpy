label CompoundGym:
stop music
play music "sounds/gymmusic.mp3"
if period == 1 and (d10locnight == 5 or d10locnight == 6) and mcsenses >= 1 and mcagility >= 1 and mcseduction >= 2 and mcstrength >= 2 and (mccombat >= 2 or mcmind >= 1) and seenstroheimwonder and supergirltraining and (seenmilfgymendlevel01 == False or not mclevel02) and sawharley:
    jump GymMILFEndLevel1
if (period == 0 and d10locday <= 3):
    scene compoundgymdaynew with fade
    jump CompoundGymb
if (period == 0 and d10locday >= 9) or (period == 1 and d10locnight <= 2):
    scene compoundgym
    show gympoweridle
    with fade
    jump CompoundGymb
if period == 1 and (d10locnight == 5 or d10locnight == 6) and mclevel02:
    scene gymmilflevel02
    with fade
    jump CompoundGymb
if period == 1 and (d10locnight == 7 or d10locnight == 8) and mclevel02:
    scene compoundgymnightnew with fade
    jump CompoundGymb
if period == 1 and (d10locnight == 3 or d10locnight == 4) and mclevel02:
    scene compoundgymnightnew with fade
    jump CompoundGymb
scene compoundgym with fade
label CompoundGymb:
call screen gymcompound()
screen gymcompound():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action Jump ("MainTime")
    imagebutton:
        focus_mask True
        idle "icons/statsiconscreenidle.png"
        hover "icons/statsiconscreenhover.png"
        action ui.callsinnewcontext("Statscreen")
    imagebutton:
        focus_mask True
        idle "icons/questsiconscreenidle.png"
        hover "icons/questsiconscreenhover.png"
        action ui.callsinnewcontext("Questscreen")
    if (period == 0 and d10locday == 7) or (period == 1 and (d10locnight == 9 or d10locnight == 10)):
        imagebutton:
            focus_mask True
            idle "v02/gymwidowidle.png"
            hover "v02/gymwidowhover.png"
            action Jump ("GymWidow")
    if (period == 0 and (d10locday == 5 or d10locday == 6)) or ((period == 1 and (d10locnight == 5 or d10locnight == 6)) and mclevel02 == False):
        imagebutton:
            focus_mask True
            idle "v02/gymmilfidle.png"
            hover "v02/gymmilfhover.png"
            action Jump ("GymMILF")
    if period == 1 and (d10locnight == 5 or d10locnight == 6) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/gymmilflevel02weightidle.png"
            hover "v041/gymmilflevel02weighthover.png"
            action Jump ("GymMCCurl")
    if period == 1 and (d10locnight == 5 or d10locnight == 6) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/gymmilflevel02idle.png"
            hover "v041/gymmilflevel02hover.png"
            action Jump ("GymMILFLevel02")
    if (period == 0 and d10locday == 8) or ((period == 1 and (d10locnight == 7 or d10locnight == 8)) and mclevel02 == False):
        imagebutton:
            focus_mask True
            idle "v02/gymwonderidle.png"
            hover "v02/gymwonderhover.png"
            action Jump ("GymWonder")
    if (period == 1 and (d10locnight == 7 or d10locnight == 8)) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/gymwonder02idle.png"
            hover "v041/gymwonder02hover.png"
            action Jump ("GymWonderLevel02")
    if (period == 1 and (d10locnight == 7 or d10locnight == 8)) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/compoundgymnightnewweightsidle.png"
            hover "v041/compoundgymnightnewweightshover.png"
            action Jump ("GymMCCurl")
    if (period == 0 and d10locday >= 9) or (period == 1 and d10locnight <= 2):
        imagebutton:
            focus_mask True
            idle "v02/gympoweridle.png"
            hover "v02/gympowerhover.png"
            action Jump ("GymPower")
    if ((period == 0 and d10locday <= 8 and d10locday >= 2) or (period == 1 and d10locnight >= 3)) and mclevel02 == False:
        imagebutton:
            focus_mask True
            idle "v02/gymweightsidle.png"
            hover "v02/gymweightshover.png"
            action Jump ("GymMCLift")
    if ((period == 0 and d10locday <= 8 and d10locday >= 2) or (period == 1 and d10locnight >= 9 and d10locnight <= 10)) and mclevel02 == False:
        imagebutton:
            focus_mask True
            idle "v02/gymweightsidle.png"
            hover "v02/gymweightshover.png"
            action Jump ("GymMCCurl")
    if (period == 1 and d10locnight >= 3 and d10locnight <= 4) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/compoundgymnightnewweightsidle.png"
            hover "v041/compoundgymnightnewweightshover.png"
            action Jump ("GymMCCurl")
    if (period == 0 and d10locday >= 4 and d10locday <= 8) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v02/gymweightsidle.png"
            hover "v02/gymweightshover.png"
            action Jump ("GymMCCurl")
    if period == 0 and d10locday <= 1 and mclevel02 == False:
        imagebutton:
            focus_mask True
            idle "v021/gymsupermanidle.png"
            hover "v021/gymsupermanhover.png"
            action Jump ("GymSuperman")
    if period == 0 and d10locday <= 1 and mclevel02:
        imagebutton:
            focus_mask True
            idle "v041/gymauditidle.png"
            hover "v041/gymaudithover.png"
            action Jump ("GymAuditGirl01")
    if period == 0 and (d10locday == 2 or d10locday == 3) and mclevel02:
        imagebutton:
            focus_mask True
            idle "v052/gymaudit02idle.png"
            hover "v052/gymaudit02hover.png"
            action Jump ("GymAuditGirl02")

label GymAuditGirl01:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene auditgirlgym01 with dissolve
if seenauditgym or seenauditgym02:
    mc "Hey Kayla, how is your new gym regimen going?"
    ag "I... I'm working hard as you can see."
    mc "Something else is about to work HARD around here if you get my drift."
if seenauditgym == False and seenauditgym02 == False:
    mc "Hey Kayla, I never saw you around here before."
    ag "Oh, it's you... I... I have a new gym regimen. To tone up."
    mc "I have something in my thong that's toning up right now..."    
scene auditgirlgym02 with dissolve
ag "Eew, that's just... so CRUDE."
scene auditgirlgym03 with dissolve
if seenauditgym:
    mc "You're still going for pushups? I thought you gave up on that."
    ag "Just a few. Before I do situps like you taught me too."
if seenauditgym == False:
    mc "How about you show me where you're up too in your routine, I might be able to help. After all, I am a gym BUFF."
    ag "I suppose so..."
scene auditgirlgym04 with dissolve
if seenauditgym:
    ag "My stomach is still too... flabby."
if seenauditgym == False:
    ag "I was trying to do some ab exercises... My stomach is too... flabby."
    mc "Alright, let's have a closer look at this fat problem of yours...."
scene auditgirlgym05 with dissolve
if seenauditgym:
    mc "Good, so you've been listening to me then."
    ag "Well, you're the gym BUFF..."
if seenauditgym == False:
    ag "I find it tough to do push-ups."
    mc "Really? I can do them with just one hand."
scene auditgirlgym06 with dissolve
if seenauditgym:
    if age >= 20:
        mc "Damn right I am. Biggest muscle stud in town!"
    if age >= 18 and age <= 19:
        mc "Damn right I am. Biggest muscle stud in town! And I'm still just a teenager."
if seenauditgym == False:
    ag "My huge dangling tits always get in the way and they are also so damn heavy."
    mc "It's true that they must weigh you down quite a bit. Do some push-ups so I can more clearly see what the issue is."
scene auditgirlgym07 with dissolve
if seenauditgym:
    ag "I know. You're... incredibly muscular. And BIG."
if seenauditgym == False:
    ag "I'll try..."
stop music
play music "sounds/sexy10.mp3"
window hide
show auditpushupvideo with fastdissolve
pause
mc "* I could be a pervert and use my Super-Senses to see her doing push-ups in the nude. Or not. My choice. *"
call screen usepower("usesenses", "AuditGymNoNude", "AuditGymNude") with dissolve
label AuditGymNude:
window hide
show auditpushupnudevideo with fastdissolve
if seenauditgymnude == False:
    $ usedsenses += 1
    $ seenauditgymnude = True
pause
label AuditGymNoNude:
if seenauditgym:
    mc "My muscles are big, but your jugs are just MASSIVE. And still getting in the way of your pushups."
    ag "I can't do anything about that! Stop mentioning my disgustingly fat dangling tits please..."
if seenauditgym == False:
    mc "Mmmh, I see, your massive jugs are definitely in the way."
    ag "They're just TOO BIG! I can't reach the floor..."
scene auditgirlgym08 with dissolve
if seenauditgym:
    mc "So you're ready to do crunches now? I'll get the sit-up bench."
    ag "I suppose so, although I was hoping to be alone so you wouldn't ask me to..."
if seenauditgym == False:
    mc "How about crunches? That might be better for tightening those abdominal muscles anyway. I mean, look at MY EIGHT-PACK!"
    ag "Wow, I wish I had abs like these... But I'll never get them, I'm just too FLABBY!"
scene auditgirlgym09 with dissolve
if seenauditgym:
    mc "...take your top off? Well, I'm here and I am reminding you that is is ESSENTIAL that you remove your constraining top."
if seenauditgym == False:
    $ seenauditgym = True    
    mc "Nonsense, if you do enough of them, you'll get there. And I know where the sit-up bench is stored, I'll go and get it."
    ag "Thanks, [name]!"
    mc "Now obviously, you need to take your top off, it's just too constraining for sit-ups."
scene auditgirlgym10 with dissolve
ag "I just knew you were going to say something like that..."
mc "You know me, I'm a perfectionist. I'll be back in a sec!"
scene auditgirlgym11 with fade
mc "So, there it is, just sit on it with your head at the bottom end."
scene auditgirlgym12:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
ag "Like this?"
mc "I'll position your feet under the holding bar and then you're set to go. Just slowly force yourself to sit up for starters."
window hide
show auditsitupvideo with fastdissolve
pause
mc "Nice, I think we can raise it up a notch. Once you reach the top, turn sideways to build up muscle tension in your external obliques."
ag "I'll...try. But I'm starting to sweat."
window hide
show auditsitupsweatvideo with fastdissolve
pause
mc "I think you've done enough, how do you feel?"
scene auditgirlgym13 with dissolve
ag "I don't know. I feel all sweaty... And stinky."
mc "I can corroborate that second statement. Your funbags need to get cleaned up."
scene auditgirlgym14 with dissolve
ag "And... how do you plan on doing that?"
mc "With my expert tongue obviously."
ag "I just knew you were going to say something like that..."
scene auditgirlgym15 with dissolve
play sound "sounds/lick01.ogg"
ag "This is... so lewd. And so nice at the same time, your tongue is tickling my big fat boobs!"
scene auditgirlgym16 with dissolve
play sound "sounds/moan04.ogg"
mc "That's it, enjoy my soft tongue, Kayla..."
scene auditgirlgym17 with dissolve
play sound "sounds/lick02.mp3"
mc "Now I see some sweat on your stomach, need to clean that too..."
ag "Oooh..."
scene auditgirlgym18 with dissolve
mc "Is there something else all sweaty and wet that I could take care of for you, Layla?"
ag "But... What are you doing, that's my... pussy..."
scene auditgirlgym19 with dissolve
mc "That's right, and it looks like you're leaking quite a bit, aren't you? You're getting aroused by all this..."
ag "No! I... It was just your ton..."
scene auditgirlgym20 with dissolve
play sound "sounds/moan02.mp3"
ag "...Oooooh, you're getting very naughty, [name]!"
scene auditgirlgym21 with dissolve
mc "But it looks like you like it, don't you?"
play sound "sounds/moan03.mp3"
ag "Aah, your fingers are rubbing against my clit!"
scene auditgirlgym22:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
play sound "sounds/moan02.mp3"
mc "You're getting REALLY wet down there."
scene auditgirlgym23 with dissolve
mc "Actually, SO WET that I'm going to need to CLEAN that wet muff..."
ag "But... What is someone comes in right now?"
mc "Well, you're the one who's naked, not me..."
scene auditgirlgym24 with dissolve
play sound "sounds/slurp.mp3"
ag "This is so... naughty! AAAH!"
scene auditgirlgym25 with dissolve
play channel1 "sounds/moan01.mp3"
play sound "sounds/lick02.mp3"
ag "Uhh... Oooh!"
scene auditgirlgym26 with dissolve
play channel1 "sounds/womancum01.mp3"
play sound "sounds/splooge01.mp3"
mc "Nice. You came. I had my muff lunch. I thin we're done here."
stop channel1
ag "But... You're going to leave me like that?"
mc "I strongly suggest you pull your clothes back on before you leave, Kayla..."
$ seenauditgym = True
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label GymAuditGirl02:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene auditstretch01 with dissolve
if seenauditgym or seenauditgym02:
    mc "Hey Kayla, how is your new gym regimen going?"
    ag "I... I'm working hard as you can see. Really stretching my muscles."
    mc "Something else is about to work HARD around here if you get my drift."
if seenauditgym02 == False and seenauditgym == False:
    mc "Hey Kayla, I never saw you around here before."
    ag "Oh, it's you... I... I have a new gym regimen. To tone up."
    mc "I have something in my thong that's toning up right now..."    
scene auditstretch02 with dissolve
ag "Eew, that's just... so CRUDE."
scene auditstretch03 with dissolve
if seenauditgym02:
    mc "You're still just stretching?"
    ag "Yes, at least I can do that."
if seenauditgym02 == False:
    mc "How about you show me where you're up too in your routine, I might be able to help. After all, I am a gym BUFF."
    ag "I suppose so..."
scene auditstretch04 with dissolve
ag "Why are you looking at me like that?"
scene auditstretch05 with dissolve
mc "I was thinking. You need to do more than just stretch if you want to TONE UP."    
scene auditstretch06 with dissolve
if seenauditgym02:
    ag "You said that last time. And then you left me hanging."
    mc "Not this time. I'm here to help."
if seenauditgym02 == False:
    ag "What do you mean?"
    mc "I mean do some FEATS OF STRENGTH!"    
scene auditstretch07 with dissolve
ag "Fine, you're the gym BUFF after all..."
if age >= 20:
    mc "Damn right I am. Biggest muscle stud in town!"
if age >= 18 and age <= 19:
    mc "Damn right I am. Biggest muscle stud in town! And I'm still just a teenager."
ag "Yes I know. You're... so BIG. Everywhere... I'm big everywhere too, but it's just FAT!"
scene auditstretch08 with dissolve
if seenauditgym02:
    mc "I want you to do this exercise again."
    ag "* sigh* Bt we already tried and it didn't work."
    mc "It didn't work because YOU didn't give it all you've got."
if seenauditgym02 == False:
    mc "You see that pull-up bar? That's what you should be using. Wonder Woman uses it and she's damn fit."
    ag "It looks too high for me to reach..."
mc "I'll help you up."
scene auditstretch09 with dissolve
mc " Stand on my shoulders..."
ag "Almost there..."
scene auditstretch10 with dissolve
ag "I've got it!"
mc "Good. Now use it to lift yourself up."
scene auditstretch11 with dissolve
ag "Don't go away please!"
mc "I have to. You need to do it without my help."
scene auditstretch12 with dissolve
play sound "sounds/womangroan.mp3"
ag "It's too hard... I'm just too FAT and FLABBY!"
scene auditstretch13 with dissolve
if seenauditgym02:
    ag "Oh no! Just like last time. My tits are just too FAT... And now they're exposed..."
if seenauditgym02 == False:
    ag "Oh no! MY top stretched too much and now my dirty tits are exposed. This is so embarrassing..."    
scene auditstretch14 with dissolve
ag "Please help me down, [name]..."
mc "Hang on a minute, I need to check something..."
ag "Wh... What are you doing?"
scene auditstretch15 with dissolve
mc "Checking how fat your enormous breasts truly are... Yeah, I think I know what the problem is..."
ag "The problem is that I'm hanging from that pull-up bar with my flabby boobs hanging out!"
scene auditstretch16 with dissolve
mc "Na. That's definitely NOT a problem."
scene auditstretch17 with dissolve
play sound "sounds/womancum02.mp3"
mc "THIS is your problem. You've carrying too much titmilk around in those giant funbags of yours. It weighs you down."
ag "Oooh..."
scene auditstretch18 with dissolve
ag "I still feel... too fat."
mc "Let me check if those boobs are more squishy now."
ag "Wh...Why?"
scene auditstretch19 with dissolve
mc "Some people have accused the dev of not being able to do squishy milkjugs. So I'm here to prove them wrong."
ag "Uuuh! You're SQUISHING my boobs!"
scene auditstretch20 with dissolve
play sound "sounds/moan02.mp3"
mc "That's the idea. They seem perfectly soft and bouncy, no issue there. And there's even more titmilk splurting out when I dig my fingers into them."
play sound "sounds/splooge02.mp3"
ag "...Oooooh, you're getting very naughty, [name]!"
scene auditstretch21 with dissolve
mc "Well, you have a clean bill of health from me and the dev. Good luck with your exercises, Kayla!"
ag "What? You're leaving me like this... This is so embarrassing..."
if period == 0 and seenauditgym02:
    menu:
        "You want to get down? (fuck Audit Girl and get her to join harem)" if auditharem == False:
            ag "Y...Yes, please."
            jump AuditGirlHaremScene
        "I don't have time to take care of you anymore, Kayla. I have to do some SUPER-HERO STUFF! (+1 Super-Villain)" if auditgymevil == False:
            call Evil
            $ auditgymevil = True
            $ renpy.pause(2.0, hard='True')
            ag "That's not very nice of you..."
            mc "Whatever."
            pass
        "I don't have time to take care of you anymore, Kayla. I have to do some SUPER-HERO STUFF! ":
            ag "That's not very nice of you..."
            mc "Whatever."
            pass
$ seenauditgym02 = True
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label AuditGirlHaremScene:
scene auditstretch21b:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "And you'll do ANYTHING for me if I get you down won't you?"
ag "I... I suppose. As long as it's not embar..."
scene auditstretch22 with dissolve
mc "Is joining the harem of the biggest STUD in town embarrassing?"
ag "Oooh... I suppose...not..."
scene auditstretch23 with dissolve
ag "Wh...Where are you taking me?"
mc "Closer to the entrance door of the gym. Where I'll be FUCKING YOU SUPER-HARD for your harem initiation!"
scene auditstretch24 with dissolve
mc "Now take your top off for me, Kayla..."
ag "But... I... What if somebod..."
scene auditstretch25 with dissolve
play sound "sounds/ripping.mp3"
ag "My poor shorts!..."
mc "That's the thrill of it! I'm sure you'll appreciate this as an opportunity to boost your CONFIDENCE!"
scene auditstretch26 with dissolve
play sound "sounds/ripping.mp3"
mc "And in solidarity with your plight, my hardening rod is ripping my thong apart!"
ag "That's so dirty!"
scene auditstretch27:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "Yeah, but that's how you like it, cos you're a DIRTY GIRL!"
ag "I'm NOT! I'm..."
mc "Yes?"
ag "It's not fair! Your cock is making me so wet! And... dirty..."
scene auditstretch28 with dissolve
mc "Then it's time for you to open up that dirty snatch REAL WIDE for me!"
play sound "sounds/moan02.mp3"
ag "Uuuhh... Please be careful, you're so HUGE..."
scene auditstretch29:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
play sound "sounds/moan04.ogg"
if age>= 20:
    ag "AAAH, you're so BIG! But your giant boymeat feels so GOOD inside me!"
if age >= 18 and age <= 19:
    ag "AAAH, you're so BIG! But your giant teenage boymeat feels so GOOD inside me!"
mc "So, will you be a GOOD girl and join my harem?"
ag "I... Just FUCK ME PLEASE!"
scene auditgirlpregymfuck01 with dissolve
play sound "sounds/moan05.mp3"
mc "I'll take this as a YES!"
play sound "sounds/womancum02.mp3"
$ auditassslow = True
window hide

label AuditGymFuck:
$ auditassveryfast = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassslow == False:
    ag "Slowly, please... You're just so BIG!"
    $ auditassslow = True

show auditgymfuckslowvideo behind auditgymassslowvideo
show auditgymfuckslowvideo behind auditgymfuckfastvideo
show auditgymfuckslowvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassslowvideo
hide auditgymfuckfastvideo
hide auditgymfuckveryfastvideo
with dissolve
stop sound
stop channel1
play channel1 "sounds/womansex02.mp3"
with dissolve
show assview:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen auditgymsidescreen()
screen auditgymsidescreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoom")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckFast")

label AuditGymFuckZoom:
$ auditassveryfast = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassslow == False:
    ag "Slowly, please... You're just so BIG!"
    $ auditassslow = True

show auditgymassslowvideo behind auditgymfuckslowvideo
show auditgymassslowvideo behind auditgymassfastvideo
show auditgymassslowvideo behind auditgymassveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymfuckslowvideo
hide auditgymassfastvideo
hide auditgymassveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show sceneicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen auditgymassscreen()
screen auditgymassscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuck")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoomFast")

label AuditGymFuckFast:
$ auditassslow = False
$ auditassveryfast = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
show auditgymfuckfastvideo behind auditgymassfastvideo
show auditgymfuckfastvideo behind auditgymfuckslowvideo
show auditgymfuckfastvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassfastvideo
hide auditgymfuckslowvideo
hide auditgymfuckveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex03.mp3"
show assview:
     xpos 50 ypos 500
show slower:
    xpos 1700 ypos 400    
show insanelyfast:
     xpos 1600 ypos 600
call screen auditgymsidefastscreen()
screen auditgymsidefastscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoomFast")
    button:
        xpos 1700
        ypos 400
        xysize(120, 60)        
        action Jump ("AuditGymFuck")
    button:
        xpos 1600
        ypos 600
        xysize(220, 60)        
        action Jump ("AuditGymFuckFaster")

label AuditGymFuckZoomFast:
$ auditassslow = False
$ auditassveryfast = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
show auditgymassfastvideo behind auditgymassslowvideo
show auditgymassfastvideo behind auditgymfuckfastvideo
show auditgymassfastvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassslowvideo
hide auditgymfuckfastvideo
hide auditgymfuckveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show sceneicon:
     xpos 50 ypos 500
show slower:
    xpos 1700 ypos 400    
show insanelyfast:
     xpos 1600 ypos 600
call screen auditgymassfastscreen()
screen auditgymassfastscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuckFast")
    button:
        xpos 1700
        ypos 400
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoom")
    button:
        xpos 1600
        ypos  600
        xysize(220, 60)        
        action Jump ("AuditGymFuckZoomFaster")
            
label AuditGymFuckFaster:
$ auditassslow = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassveryfast == False:
    ag "Faster... FASTER!"
    $ auditassveryfast = True
show auditgymfuckveryfastvideo behind auditgymassveryfastvideo
show auditgymfuckveryfastvideo behind auditgymfuckfastvideo
show auditgymfuckveryfastvideo behind auditgymfuckslowvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassveryfastvideo
hide auditgymfuckfastvideo
hide auditgymfuckslowvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show nexticon:
    xpos 1700 ypos 1020    
show assview:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen auditgymsideveryscreen()
screen auditgymsideveryscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoomFaster")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditGymFuckEnd")

label AuditGymFuckZoomFaster:    
$ auditassslow = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassveryfast == False:
    ag "Faster... FASTER!"
    $ auditassveryfast = True
show auditgymassveryfastvideo behind auditgymfuckveryfastvideo
show auditgymassveryfastvideo behind auditgymassfastvideo
show auditgymassveryfastvideo behind auditgymassslowvideo
$ renpy.pause(0.5, hard=True)
hide auditgymfuckveryfastvideo
hide auditgymassfastvideo
hide auditgymassslowvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show nexticon:
    xpos 1700 ypos 1020    
show sceneicon:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen auditgymassveryscreen()
screen auditgymassveryscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuckFaster")
    button:
        xpos 1700
        ypos  500
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoomFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditGymFuckEnd")
        
label AuditGymFuckEnd:
hide zoomicon
hide slower
hide faster
hide insanelyfast
hide sceneicon
mc "Fuck... Getting close to blowing big time..."
ag "DO IT! I want to be your fat booty harem cum dumpster girl!"
scene auditgymfuckcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "Will you? RHAAA!"
window hide
with fastflash
ag "Yes! YESSSS!!!"
scene auditgymfuckcum02:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan04.ogg"
mc "Then I'll FILL YOU UP, AAAH!"
window hide
with vpunch
ag "Oh God, Y...YES!!!"
scene auditgymfuckcum03 with dissolve
play sound "sounds/splooge02.mp3"
mc "CUMMING SO MUCH!!!"
window hide
with fastflash
ag "Gggg...."
scene auditgymfuckcum04 with dissolve
ag "AAAH!!!"
window hide
with hpunch
mc "You're making me BLAST so much, I Don't know if I can h..."
scene auditgymfuckcum05 with dissolve
stop sound
play sound "sounds/splooge03.mp3"
mc "...HOLD OFF, AAAH! FUCK, YEAH!!!"
window hide
with fastflash
ag "Eeeeek!"
scene auditgymfuckcum06:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
stop sound
ag "You FIRED me off your cum-cannon!"
window hide
with fastflash
if age >= 20:
    ag "And you're STILL spewing great big globs of SUPER-HOT SPUNK!"
if age >= 18 and age <= 19:
    ag "And you're STILL spewing great big globs of SUPER-HOT TEEN SPUNK!"

scene auditgymfuckcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Damn it, Kayla, you made me cum... so much..."
ag "How are we going to clean this mess? Anyone could walk in..."

scene auditgymfuckcum08 with dissolve
mc "Well, that's YOUR problem. You're in my harem now, remember?"
window hide
play sound "sounds/achievement.mp3"
show haremgirlaudit at posharem
$ renpy.pause(0.5, hard='True')
show haremgirltext at posharemtext
pause
$ auditharem = True
ag "But..."
mc "Tss, tss... Harem girls are SLAVES. So YOU clean this up while I go and take a shower."
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label GymSuperman:
$ seengym = True
scene gymwidowbackground
show gymsuperman01
with dissolve
sm "What do you want?"
label GymSupermanDialogues:
menu:
    "Those dumbbells don't look that heavy.":
        hide gymsuperman01
        show gymsuperman03
        with fastdissolve
        sm "You think so? They're made of iridium..."
        mc "Yeah, so?"
        hide gymsuperman03
        show gymsuperman01
        with fastdissolve
        sm "It's the HEAVIEST element in the universe. Until scientists find a new one."
        mc "So?"
        hide gymsuperman01
        show gymsuperman02
        with fastdissolve
        sm "So these dumbbells weight 10 tonnes. EACH."
        mc "Ah. That's quite heavy actually."
        hide gymsuperman02
        show gymsuperman01
        with fastdissolve        
        jump GymSupermanDialogues
    "Why do you even bother training?":
        hide gymsuperman01
        show gymsuperman02
        with fastdissolve
        sm "I DON'T need to train. I come here to relax."
        hide gymsuperman02
        show gymsuperman01
        with fastdissolve
        jump GymSupermanDialogues
    "Could you train me so I can get stronger?" if mcstrength == 1:
        if usedstrength == 0:
            hide gymsuperman01
            show gymsuperman02
            with fastdissolve
            sm "You can't reach level 2 if you haven't even used your Super-Strength at least once succesfully!"
            mc "Oh, is that how it works?"
            hide gymsuperman02
            show gymsuperman03
            with fastdissolve
            sm "Yes, this is how it works."
            mc "I learn about game mechanics every day."
            hide gymsuperman03
            show gymsuperman01
            with fastdissolve
            sm "Now let me finish my relaxing iron pumping session. UNDISTURBED."
            jump Main
        if usedstrength >= 1:
            sm "I could. But why would I?"
            if inventorykryptonite == False:
                mc " * If I had some kryptonite, I could blackmail the fucker and have an extra option in the menu that's coming up... * "
            menu:
                "Because if you don't, I might pull a little rock out of my pocket... (+1 Super-Villain)" if inventorykryptonite:
                    hide gymsuperman01
                    show gymsuperman03
                    with fastdissolve
                    sm "What? You mean... Kr... Kryp..."
                    mc "Yeah, KRYPTONITE."
                    call Evil from _call_Evil_12
                    hide gymsuperman03
                    show gymsuperman02
                    with fastdissolve
                    sm "This is blackmail! I'm starting to think you're more of a Super-Villain than a Super-Hero!"
                    mc "Whatever, let's get to work. Out."
                    jump GymStrengthTraining
                "Because if you do, I'll teach how to seduce Lois Pane... (+1 Super-Hero)" if mcseduction >= 2:
                    $ nicegymsuperman = True
                    hide gymsuperman01
                    show gymsuperman03
                    with fastdissolve
                    sm "Lois? I... Fine, I agree."
                    mc "This is a win-win situation for both of us."
                    call Good from _call_Good_10
                    jump GymStrengthTraining
                "Err... Cos you're a nice super-hero?":
                    hide gymsuperman01
                    show gymsuperman02
                    with fastdissolve
                    sm "Sure I am. But YOU'RE NOT! So get lost!"
                    mc "Wow, that's, like, EVIL, dude."
                    hide gymsuperman02
                    show gymsuperman01
                    with fastdissolve                    
                    jump GymSupermanDialogues
    "How is it going with Lois Pane?":
        hide gymsuperman01
        show gymsuperman03
        with fastdissolve
        if loisevil == False:
            sm "Fine. I have a romantic dinner with her later tonight."
            mc "Oooh. Pity you won't be able to bring her back home and FUCK HER. Since you have no dick and all."
            hide gymsuperman03
            show gymsuperman01
            with fastdissolve
            sm "SEX isn't the only thing in life!"
            mc "Well, it is in THIS game."
            sm "Pfff."
            jump GymSupermanDialogues
        if loisevil:
            sm "I... She won't talk to me anymore. I don't know why..."
            mc "What a shame. Perhaps if you had a cock, she might at least look at that, but alas..."
            hide gymsuperman03
            show gymsuperman01
            with fastdissolve
            sm "Get out of here!"
            jump Main
    "Have you noticed how much BIGGER my muscles are?" if mclevel02:
        hide gymsuperman01
        show gymsuperman03
        with fastdissolve
        sm "So what? Muscles don't give Super-Strength. Superpowers give Super-Strength."
        mc "Well, sure, but still, it makes me more intimidating as an opponent. I will be feared by my enem..."
        hide gymsuperman03
        show gymsuperman01
        with fastdissolve
        sm "Not with that silly thong you're wearing."
        mc "I see. You don't seem to be in a good superhero mood. I'm done here anyway."
        jump Main        
    "I'm done here.":
        hide gymsuperman01
        show gymsuperman02
        with fastdissolve
        sm "Good. I need to finish my relaxing iron pumping session. ALONE."
        jump Main                     

label GymStrengthTraining:
scene gymwidowbackground
show gymsuperman06
with dissolve
sm "Take this bar of iridium and try and bend it."
mc "Alright, no problemo! WIth my huge muscles, it will be a piece of cake. I'll even do it in front of the mirror cos I like admiring my own body for some reason."
scene supermanstrengthtraining01 with fade
mc "On three. A one, a two, a..."
scene supermanstrengthtraining02 with fastdissolve
play sound "sounds/mangrunt01.mp3"
sm "I don't see it moving one bit."
scene supermanstrengthtraining01 with dissolve
mc "I was just testing its resistance. Now, watch. On a one, on a two, on a thr..."
scene supermanstrengthtraining02 with fastdissolve
play sound "sounds/mangrunt01.mp3"
sm "Nope, still nothing."
scene supermanstrengthtraining01 with dissolve
mc "Damn it! Ok, tell me how to do it then."
scene supermanstrengthtraining03 with fastdissolve
sm "Give me the bar, I'll show you."
scene supermanstrengthtraining04 with dissolve
sm "Like so."
mc "But you're Super-Strength level 3, that's not fair! I simply can't do it, I don't see how this training can change anything, this is bullshit!"
scene supermanstrengthtraining05 with dissolve
sm "Contrary to what you might think, Super-Strength can IMPROVE. It's all about channelling your strength into your arms. For this exercise anyway."
mc "And how do I do that?"
sm "You must put yourself in a distraction-free mode and disconnect the rest of your body from your mind."
scene supermanstrengthtraining01 with dissolve
sm "Only your willpower focused on your hands and arms, nothing else matters, nothing else EXISTS!" 
mc "Alright, I'll try..."
$ renpy.pause(1.0, hard='True')
mc "Focus. Focus..."
scene supermanstrengthtraining06 with dissolve
play sound "sounds/mcworkout.mp3"
sm "Keep going, keep FOCUSING!"
scene supermanstrengthtraining07 with dissolve
play sound "sounds/mangrunt01.mp3"
sm "You did it, well done!"
call StrengthPlus from _call_StrengthPlus
scene supermanstrengthtraining08 with dissolve
mc "FUCK YEAH! I'm da man, I'm DA MAN!"
sm "And I'm still SUPERMAN!"
if nicegymsuperman:
    scene gymwidowbackground
    show gymsuperman04
    with fade 
    "You then trained Superman in Super-Seduction. Which we didn't show, cos it was kinda gay."
    sm "Well, thank you for this...interesting training course. Now I know how to go about seducing my darling love Lois."
    mc "Obviously, this won't help you score in bed with her. Considering you don't have a dick and all."
    hide gymsuperman04
    show gymsuperman05
    with fastdissolve
    sm "Stop reminding me!"
    jump Main
scene gymwidowbackground
show gymsuperman05
with fade 
sm "Now leave me alone! And don't you dare try and blackmail me again, I'm warning you!"
mc "We'll see, we'll see. What route the player chooses. Whether he's evil or not basically."
jump Main

label GymMILF:
$ seengym = True
scene milfgymprerun01 with fade
mc "* Carol is running on the treadmill. Let's get closer... *"
window hide
play channel1 "sounds/treadmill.mp3"
label GymMILFScene:
hide closer
hide nexticon
hide sceneicon
show milfgymvideo behind milfgymvideo02
show milfgymvideo behind milfgymvideo07
$ renpy.pause(1.0, hard=True)
hide milfgymvideo07
hide milfgymvideo02
with dissolve
show closer:
     xpos 50 ypos 500
show nexticon:
     xpos 1700 ypos 500
call screen GymMILFscene()
screen GymMILFscene():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFBoobs")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("GymMILFNoNudeEnd")

label GymMILFBoobs:
hide closer
hide nexticon
hide sceneicon
mc "* I wanna see those jiggling MILF titties closer... *"
if period == 0:
    show milfgymvideo02 behind milfgymvideo
    show milfgymvideo02 behind milfgymvideo07
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo
    hide milfgymvideo07
    with dissolve
if period == 1:
    show milfgymvideo07 behind milfgymvideo
    show milfgymvideo07 behind milfgymvideo02
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo
    hide milfgymvideo02
    with dissolve

show nexticon:
    xpos 1750 ypos 1020
    
show sceneicon:
     xpos 1700 ypos 500     
call screen GymMILFboobs()
screen GymMILFboobs():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFScene")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFEnd")

label GymMILFEnd:
if mcsenses >= 1:
    call screen usepower("usesenses", "GymMILFNoNudeEnd", "GymMILFNude") with dissolve
if mcsenses == 0:
    jump GymMILFNoNudeEnd

label GymMILFNude:
hide closer
hide nexticon
hide sceneicon
hide slower
if period == 0:
    show milfgymvideo03 behind milfgymvideo02
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo02
    with dissolve
if period == 1:
    show milfgymvideo05 behind milfgymvideo07
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo07
    with dissolve

show nexticon:
    xpos 1750 ypos 1020
    
show slower:
     xpos 50 ypos 500     
call screen GymMILFnude()
screen GymMILFnude():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFNudeEnd")

label GymMILFNudeSlow:
hide closer
hide nexticon
hide sceneicon
hide slower
if period == 0:
    show milfgymvideo04 behind milfgymvideo03
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo03
    with dissolve
if period == 1:
    show milfgymvideo06 behind milfgymvideo05
    $ renpy.pause(1.0, hard=True)
    hide milfgymvideo05
    with dissolve

show nexticon:
    xpos 1750 ypos 1020
    
show faster:
     xpos 1700 ypos 500     
call screen GymMILFnudeslow()
screen GymMILFnudeslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNude")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFNudeEnd")

label GymMILFNoNudeEnd:
stop channel1
if period == 0:
    scene gymmilfpostrun with dissolve
if period == 1:
    scene gymmilfpostrunnight with dissolve
cm "Oh, it's you, sweetie. Let me get off the treadmill..."
jump GymMILFDialogues

label GymMILFNudeEnd:
stop channel1
if period == 0:
    scene gymmilfpostrunnude with dissolve
if period == 1:
    scene gymmilfpostrunnightnude with dissolve
cm "Oh, it's you, sweetie. Let me get off the treadmill..."

label GymMILFDialogues:
stop music
scene gymmilfbackground
show milfgymeyeblink
with dissolve
cm "So, what did you want to talk about?"
label GymMILFDialoguesb:
menu:
    "Oh, nothing, I was just admiring the VIEW.":
        hide milfgymeyeblink
        show milfgym04 at centerleft
        with fastdissolve
        cm "I see... And did you have a NICE view?"
        mc "I sure did, Carol..."
        if mcsenses >= 1:
            hide milfgym04
            show milfgym05 at centerleft
            with fastdissolve
            cm "Did you use your Super-Senses to ogle my boobs while you were admiring the view?"
            mc "What? Err, no, I ONLY use my Super-Powers for GOOD!"
            hide milfgym05
            show milfgym03 at centerleft
            with fastdissolve
            cm "I somehow find it hard to believe... With your young libido..."
            mc "I didn't mean to..."
            hide milfgym03
            show milfgym02 at centerleft
            with fastdissolve
            cm "Don't worry about it. After all, I'm the one who GAVE YOU that extreme libido. * wink *"
            if period == 0:
                cm "Goodbye, sweetie!"
            if period == 1:
                cm "Goodnight, sweetie!"
            jump Main            
        if mcsenses == 0:
            hide milfgym04
            show milfgym02 at centerleft
            with fastdissolve
            cm "Good thing you don't have Super-Senses then. The view might have given you a heart attack. * wink *"
            mc "* I see. If I had Super-Senses, there would be MORE to see in this scene... I NEED to get that Super-Power! *"
            hide milfgym02
            show milfgym03 at centerleft
            with fastdissolve
            cm "You seem to be thinking about something... Like pondering whether to acquire Super-Senses?"
            mc "Err... Maybe, one day. I mean, for my missions and all that."
            hide milfgym03
            show milfgym05 at centerleft
            with fastdissolve
            if period == 0:
                cm "Of course, just for your missions... Goodbye, [name]."
            if period == 1:
                cm "Of course, just for your missions... Goodnight, [name]."
        jump Main
    "I wanted to know where I could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide milfgymeyeblink
        show milfgym03 at centerleft
        with fastdissolve
        cm "But, she's just an intern. She doesn't need a costume."
        mc "How is she going to audit the books of super-villains if she's stuck in the compound?"
        hide milfgym03
        show milfgym04 at centerleft
        with fastdissolve
        cm "I suppose you're right. There is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide auditquestcostumeprogress01
        hide milfgym04
        show milfgym02 at centerleft
        with fastdissolve
        cm "Are you interested in her? Your landlady's puppies aren't big enough for you? * wink *"
        mc "Well, err... No, it's just..."
        cm "You're trying to help me manage the compound? You think I can't handle it by myself?"
        mc "Well, you must be busy all the time, so I thought..."
        hide milfgym02
        show milfgym05 at centerleft
        with fastdissolve
        cm "Just don't spend too much money on her. She's JUST an intern. And I'm the League's CAPTAIN."
        mc "Roger that, Carol!"
        stop channel1
        jump Main
    "I'm going to train. By bench-pressing over 3 TONS of weights!":
        hide milfgymeyeblink
        show milfgym02 at centerleft
        with fastdissolve
        cm "Mmh, that's nice, sweetie. I'd LOVE to watch, but I have to check on the latest Super-Villain bulletin update. You can never be too careful."
        mc "Ah, OK. Then I'll train on my own. With nobody to admire by bulging muscles..."
        hide milfgym02
        show milfgym03 at centerleft
        with fastdissolve
        cm "Remember to really PUSH yourself so you can grow even BIGGER! Goodnight, [name]."
        scene gymmcliftvideo with dissolve
        pause
        mc "Fuck yeah! Lifting Over three tons of weights! A few more reps..."
        window hide
        pause
        $ d3rollgymworkout = renpy.random.randint(1, 3)
        if d3rollgymworkout == 1:
            scene gymmcpostlift01 with dissolve
            mc "That was a nice workout... I feel like my muscles have GROWN a bit..."
        if d3rollgymworkout == 2:
            scene gymmcpostlift02 with dissolve
            mc "Grrr! I could scare away any Super-Villain with MY muscles now!"
        if d3rollgymworkout == 3:
            scene gymmcpostlift03 with dissolve
            if age >= 20:
                mc "Damn! Check those biceps, monster muscle stud right there!"
            if age >= 18 and age <= 19:
                mc "Damn! Check those biceps, monster teenage muscle stud right there!"
            mc "But no one around to admire them but me... * sigh *"
        stop channel1
        jump Main
    "I'm going to train my already MASSIVE biceps with super-heavy dumbbells." if mclevel02:
        hide milfgymeyeblink
        show milfgym02 at centerleft
        with fastdissolve
        cm "Mmh, that's nice, sweetie. I'd LOVE to watch, but I have to check on the latest Super-Villain bulletin update. You can never be too careful."
        mc "Ah, OK. Then I'll train on my own. With nobody to admire by bulging muscles..."
        hide milfgym02
        show milfgym03 at centerleft
        with fastdissolve
        cm "Remember to really PUSH yourself so you can grow even BIGGER! Goodnight, [name]."        
        $ seengym = True
        scene gymmcprecurl01 with fade
        mc "Let's get rid of this ridiculously light barbell and use Superman's iridium dumbbells instead. They weigh over 10 TONS each and I feel SUPER-STRONG right now!"
        scene gymmcprecurl02 with dissolve
        mc "That's it. Ready to RUMBLE!"
        window hide
        show gymmccurlvideo with dissolve
        pause
        mc "Fuck yeah! Chest-pressing over 20 TONS! A few more reps..."
        window hide
        pause
        $ d3rollgymworkout = renpy.random.randint(1, 3)
        if d3rollgymworkout == 1:
            scene gymmcpost04 with dissolve
            mc "That was a nice workout... I feel like my biceps have GROWN even MORE..."
        if d3rollgymworkout == 2:
            scene gymmcpost05 with dissolve
            mc "Grrr! I could scare away any enemy with THOSE muscles now!"
        if d3rollgymworkout == 3:
            scene gymmcpost06 with dissolve
            if age >= 20:
                mc "Damn! Check those biceps, monster muscle STUD right there!"
            if age >= 18 and age <= 19:
                mc "Damn! Check those biceps, monster teenage muscle STUD right there!"
            mc "But no one around to admire them but me... * sigh *"
        stop channel1
        jump Main

label GymMILFLevel02:
$ seengym = True
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene gymmilfnew01 with dissolve
mc "There's Captain MILF doing some squats. Let's get closer..."
scene gymmilfnew02 with dissolve
cm "Well hello there, sweetie pie! You want to watch your League Captain squat over 3 tons of Krypton steel weights?"
mc "I sure do."
show gymmilfsquatvideo with dissolve

show nexticon:
    xpos 1750 ypos 1020
call screen GymMILFsquatb()
screen GymMILFsquatb():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEndb")

label GymMILFSquatEndb:
if mcsenses >= 1:
    call screen usepower("usesenses", "GymMILFSquatEnd02b", "GymMILFNudePreSquatb") with dissolve
if mcsenses == 0:
    jump GymMILFSquatEnd02b

label GymMILFNudePreSquatb:
hide nexticon
mc "Let's focus my Super-Senses on her Super-Tits..."
window hide

label GymMILFNudeSquatb:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedfastvideo behind gymmilfsquatnakedslowvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedslowvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020
show slower:
     xpos 50 ypos 500     
call screen GymMILFnudesquatb()
screen GymMILFnudesquatb():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquatSlowb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02b")

label GymMILFNudeSquatSlowb:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedslowvideo behind gymmilfsquatnakedfastvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedfastvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen GymMILFnudesquatslowb()
screen GymMILFnudesquatslowb():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquatb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02b")

label GymMILFSquatEnd02b:
scene gymmilfnew03 with dissolve
cm "And now, lifted high above my head!"
mc "Not bad, I can do it too though, it's easy with Super-Strength level 2."
scene gymmilfnew04:
    zoom 0.5 xoffset 0 yoffset 0
with dissolve
cm "But can you do it with one hand while FLEXING your biceps?"
mc "Damn, Carol! Your biceps... They're BULGING!..."
scene gymmilfnew04:
    subpixel True
    zoom 0.5 xoffset 0 yoffset 0
    linear 5.0 zoom 1.0 xoffset -600 yoffset -600
$ renpy.pause(4.0, hard='True')
cm "Maybe I should turn round to prove to you how FIT your League Captain is..."
mc "Indeed you should. I need convincing right NOW!"
scene gymmilfnew05:
    subpixel True
    ypos 0.0
    ease 4.0 xpos -0.02 ypos -0.99
$ renpy.pause(4.0, hard='True')
mc "* What a tight ass! Maybe I should get h... *"
cm "Don't get any funny ideas, [name]. You wouldn't want to mess with your landlady while she's in this PUMPED-UP state!"
scene gymmilfnew06 with dissolve
cm "Imagine the DAMAGE those iron-hard abs could cause on some unsuspecting victim..."
mc "...You're not thinking about ME I hope?"
cm "Of course not, sweetie pie. Yet."
show screen calendar
show screen statscreenicon
show screen questscreenicon

stop music
scene gymwidowbackground
show milfgymeyeblink02
with dissolve
cm "So, what do you have to say to your landlady, [name]?"
label GymMILFDialoguesc:
menu:
    "Oh, nothing really, I was just admiring how easily you squatted that HEAVY barbell.":
        hide milfgymeyeblink02
        show milfgym80s02 at centerleft
        with fastdissolve
        cm "Did you use your Super-Senses to ogle my boobs while you were admiring the view, [name]?"
        mc "What? Err, no, I ONLY use my Super-Powers for GOOD!"
        hide milfgym80s02
        show milfgym80s04 at centerleft
        with fastdissolve
        cm "I somehow find it hard to believe... With your young libido..."
        mc "I didn't mean to..."
        hide milfgym80s04
        show milfgymeyeblink02
        with fastdissolve
        cm "Don't worry about it. After all, I'm the one who GAVE YOU that extreme libido. * wink *"
        if period == 0:
            cm "Goodbye, sweetie!"
        if period == 1:
            cm "Goodnight, sweetie!"
        jump Main            
    "I'm going to train my already MASSIVE biceps with super-heavy dumbbells." if mclevel02:
        hide milfgymeyeblink02
        show milfgym80s02 at centerleft
        with fastdissolve
        cm "Mmh, that's nice, sweetie. I'd LOVE to watch, but I have to check on the latest Super-Villain bulletin update. You can never be too careful."
        mc "Ah, OK. Then I'll train on my own. With nobody to admire by bulging muscles..."
        hide milfgym80s02
        show milfgym80s03 at centerleft
        with fastdissolve
        cm "Remember to really PUSH yourself so you can grow even BIGGER! Goodnight, [name]."        
        $ seengym = True
        scene gymmcprecurl01 with fade
        mc "Let's get rid of this ridiculously light barbell and use Superman's iridium dumbbells instead. They weigh over 10 TONS each and I feel SUPER-STRONG right now!"
        scene gymmcprecurl02 with dissolve
        mc "That's it. Ready to RUMBLE!"
        window hide
        show gymmccurlvideo with dissolve
        pause
        mc "Fuck yeah! Chest-pressing over 20 TONS! A few more reps..."
        window hide
        pause
        $ d3rollgymworkout = renpy.random.randint(1, 3)
        if d3rollgymworkout == 1:
            scene gymmcpost04 with dissolve
            mc "That was a nice workout... I feel like my biceps have GROWN even MORE..."
        if d3rollgymworkout == 2:
            scene gymmcpost05 with dissolve
            mc "Grrr! I could scare away any enemy with THOSE muscles now!"
        if d3rollgymworkout == 3:
            scene gymmcpost06 with dissolve
            if age >= 20:
                mc "Damn! Check those biceps, monster muscle STUD right there!"
            if age >= 18 and age <= 19:
                mc "Damn! Check those biceps, monster teenage muscle STUD right there!"
        mc "But no one around to admire them but me... * sigh *"
        stop channel1
        jump Main

label GymWonder:
$ seengym = True
stop music
play music "sounds/wwomanmusic01.mp3"
scene wondergymvideo with fade
pause
mc "* Damn, her abs and biceps are tightening up on each push... Nice. *"
window hide
pause
stop music
label GymWonderDialogues:
scene gymwonderbackground
show wondergymeyeblink
with dissolve
if seenstroheimwonder and wondertrain01 == False and mcagility >=1:
    ww "You dare show your face to me while I'm training to try and keep in shape despite becoming PREGNANT because of YOU?"
    mc "Well, err... I just came to..."
    hide wondergymeyeblink
    show wondergym03 at centerleft
    with fastdissolve
    ww "I CHALLENGE you to a duel in Super-Combat! I will restore my honor, for the purity of my race! In accordance with the superhero code, you may not back down!"
    mc "We have a superhero code? I didn't know about that. Alright, but let's not get all melodramatic about it, I mean you're from the past."
    hide wondergym03
    show wondergym04 at centerleft
    with fastdissolve
    ww "And it is MY FUTURE which is at stakes! Prepare to FIGHT! NAKED, as per the Amazonian rules of Combat!"
    jump WonderFight

ww "[hero]. Are you here to train your muscles?"
label GymWonderDialoguesb:
menu:
    "Yeah, Even though they are already HUGE.":
        hide wondergymeyeblink
        show wondergym02 at centerleft
        with fastdissolve
        ww "Bragging won't make your muscles stronger."
        mc "It can still help in spreading FEAR into my enemies!"
        hide wondergym02
        show wondergym04 at centerleft
        with fastdissolve
        ww "Wonder Woman is not afraid of ANYBODY!"
        mc "Yeah, sure, but Super-Villains might..."
        hide wondergym04
        show wondergymeyeblink
        with fastdissolve
        ww "Nazis are determined and fanatical. Not sure it would work, [name]..."
        jump GymWonderDialoguesb
    "You don't look very pregnant right now." if seenstroheimwonder and wonderbirth == False:
        hide wondergymeyeblink
        show wondergym02 at centerleft
        with fastdissolve
        ww "Nevertheless, I can feel that I am... Hopefully, not with NAZI babies. * sigh *"
        mc "Not a chance! With the mighty load I... err... delivered inside your...err..."
        hide wondergym02
        show wondergymeyeblink
        with fastdissolve        
        ww "Don't remind me! You have COMPROMISED the PURITY of my race! Get out of here!"
        jump Main
    "I was wondering, You're NOT wearing your costume right now. What if nazis turned up?":
        hide wondergymeyeblink
        show wondergym04 at centerleft
        with fastdissolve
        ww "Wonder Woman is ALWAYS READY!"
        mc "Doesn't look like it to me..."
        hide wondergym04
        show wondergym05 at centerleft
        with fastdissolve
        ww "I will show you..."
        play sound "sounds/wonderspin.mp3"
        hide wondergym05
        show wondergym06 at centerleft
        with dissolve
        hide wondergym06
        show wondergym07 at centerleft
        with dissolve
        hide wondergym07
        show wondergym08 at centerleft
        with dissolve
        hide wondergym08
        show wondergym09 at centerleft
        with dissolve
        hide wondergym09
        show wondergym10 at centerleft
        with dissolve
        hide wondergym10
        show wondergym11 at left
        with dissolve
        ww "See? Wonder Woman IS ready now!"
        mc "Wow! How do I get that Superpower?"
        hide wondergym11
        show wondergym12 at centerleft
        with dissolve
        ww "You can't. This is Wonder Woman's SPECIAL SUPERPOWER! Now if you'll excuse me, I have some Nazis' asses to KICK!"
        mc "You go, Wonder Woman!"
        jump Main
    "So you're in beast mode? Well, so am I, in SEXY BEAST MODE!":
        hide wondergymeyeblink
        show wondergym04 at centerleft
        with fastdissolve
        ww "My shirt doesn't mean it in THAT way. But let's see if you're really a beast like you pretend..."
        mc "Ooh Yeah!"
        hide wondergym04
        show wondergym03 at centerleft
        with fastdissolve
        ww "Come over here and let's compare MUSCLES!"
        jump WonderGymMuscles 
    "Will you teach me how to be Super-Agile, Princess Diana?" if (mcagility == 1 and mission03end == False) or (mcagility == 0 and seenwonderbeast == False):
        hide wondergymeyeblink
        show wondergym02 at centerleft
        with fastdissolve
        ww "Your agility is indeed very LIMITED. Perhaps one day, I will have time to teach you, [name]."
        mc "Why not today?"
        hide wondergym02
        show wondergym03 at centerleft
        with fastdissolve
        ww "Today, Wonder Woman is training her MUSCLES to stay on TOP of her form."
        mc "Ah, I see, Maybe I should do the same. I am Super-Strong after all..."
        jump GymMCLift
    "Will you teach me how to be Super-Agile, Princess Diana?" if mcagility == 0 and seenwonderbeast:
        hide wondergymeyeblink
        show wondergym02 at centerleft
        with fastdissolve
        ww "Your agility is indeed very LIMITED. But you're in luck, I finished my MUSCLE training and I can teach you, [name]."
        mc "Alright! What do we do?"
        hide wondergym02
        show wondergym03 at centerleft
        with fastdissolve
        ww "First, we need to STRETCH. Help me first, and I'll help you afterwards."
        jump GymWonderAgility
    "Could you give me some extra-training in Super-Agility, Princess Diana?" if mcagility >= 1 and mission03end:
        hide wondergymeyeblink
        show wondergym02 at centerleft
        with fastdissolve
        ww "You're already Level 1 in Super-Agility. I'm not sure I can help you reach level 2 at this stage."
        if seenwonderagility == False:
            mc "Still, let's try if you don't mind."        
        if seenwonderagility:
            mc "Still, let's try if you don't mind. Especially since I'll get a blowjob at the end, most likely."        
        hide wondergym02
        show wondergym04 at centerleft
        with fastdissolve
        if seenwonderagility == False:
            ww "You're in luck, I finished my MUSCLE training so I have a bit of time to waste in this present-day timeline."
        if seenwonderagility:
            ww "You want to RAPE my mouth again? I'll prove to you that Wonder Woman's mouth isn't rapable. By agreeing to your training request, thereby cancelling the rape charge." 
            mc "Err, OK..."
        hide wondergym04
        show wondergym03 at centerleft
        with fastdissolve
        ww "First, we need to STRETCH. Help me first, and I'll help you afterwards."
        jump GymWonderAgility
    "I'm done here. I'll go and lift super-heavy weights.":
        hide wondergymeyeblink
        show wondergym04 at centerleft
        with fastdissolve
        ww "Wonder Woman is NEVER DONE."
        jump GymMCLift

label WonderFight:
$ wondertrain01 = True
scene wonderfight01 with fade
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
    jump WonderFight02
if evilness <= 12:
    scene wonderfight13 with dissolve
    ww "I will, and since you are not a concealed Super-Villain, despite my suspicions, Wonder Woman will train you in Super-Combat Level 2."
    mc "Alright! Getting closer to that upgrade everyone's been waiting for..."
    jump WonderFight02
label WonderFight02:
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
    jump WonderFight03b
    
if evilness <= 12:
    scene wonderfight18 with dissolve
    ww "After Woman Woman once again PROVED her superiority over mere male mortals, you may rise again and get prepared for your training."
    mc "Gee, thank you, oh Mighty and Gracious Highness Princess Diana..."
    jump WonderFight03

label WonderFight03:
stop music
play music "v03/fightmusic.mp3"
scene wonderfight20 with dissolve
ww "We shall train without equipment. In pure hand-to-hand Amazonian COMBAT!"
label WonderFight03b:
scene wonderfight02b with dissolve
mc "Fine by me! This time, I'll prove my worth! HEEE-YAH!"
scene wonderfight21 with dissolve
play sound "sounds/punch.mp3"
ww "You need to be FASTER and more Super-Agile if you plan to beat Wonder Woman!"
mc "Ouch! Not in my cock!"
label WonderFight04:
scene wonderfight22 with dissolve
mc "FUCK ME! That hurts like hell!"
ww "You won't be impregnating anyone anytime soon, [hero]!"
scene wonderfight23 with dissolve
mc "That's it, I've had enough of this. You want Super-Fast Combat, I'll give you Super-Fast Combat!"
call screen usepower("usecombat", "WonderNoCombat", "WonderCombat") with dissolve

label WonderNoCombat:
scene wonderfight21 with dissolve
play sound "sounds/punch.mp3"
ww "You want some MORE of this? I can do this ALL DAY!"
mc "Ouch! Not in my cock! AGAIN!"
jump WonderFight04

label WonderCombat:
scene wonderfight24 with dissolve
$ usedcombat += 1
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

label WonderAnalSlow:
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
$ wonderanalfast = False
if wonderanalslow == False:
    ww "My ass is yours, [hero]! Pound it like the filthy underserving hole it is!"
    $ wonderanalslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500     
call screen wonderanalslow()
screen wonderanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFrontSlow")

label WonderAnalFast:
$ wonderanalslow = False
if wonderanalfast == False:
    ww "Thrust faster, please!"
    mc "Damn, you really want that cock, don't you, Servile Wonder Woman!"
    $ wonderanalfast = True
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
call screen wonderanalfast()
screen wonderanalfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalSlow")
    button:
        xpos 1650
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalHard")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFrontFast")

label WonderAnalFrontSlow:
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
$ wonderanalfast = False
if wonderanalslow == False:
    ww "My ass is yours, [hero]! Pound it like the filthy underserving hole it is!"
    $ wonderanalslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderanalfrontslow()
screen wonderanalfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalSlow")

label WonderAnalFrontFast:
$ wonderanalslow = False
if wonderanalfast == False:
    ww "Thrust faster, please!"
    mc "Damn, you really want that cock, don't you, Servile Wonder Woman!"
    $ wonderanalfast = True
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
call screen wonderanalfrontfast()
screen wonderanalfrontfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontSlow")
    button:
        xpos 1650
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalZoomHard")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalFast")

label WonderAnalHard:
if wonderanalhard == False:
    mc "Now I'm gonna POUND that ass to OBLIVION until you SUBMIT!"
    $ wonderanalhard = True
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
call screen wonderanalhard()
screen wonderanalhard():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalZoomHard")

label WonderAnalZoomHard:
if wonderanalhard == False:
    mc "Now I'm gonna POUND that ass to OBLIVION until you SUBMIT!"
    $ wonderanalhard = True
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
call screen wonderanalfronthard()
screen wonderanalfronthard():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAnalFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAnalEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAnalHard")

label WonderAnalEnd:
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
    mc "That's a good girl. Now go back to your room and take a shower. I'll go back to mine and we'll forget everything about tonight."
    jump Main
if evilness <= 12:
    mc "Well, you're the future mother of my offspring, so that's alright."
    ww "Y...Yes, [name] , I'm just your breeding wife now. * sob *"
    mc "Ok, let's not push it, I was only trying to get better at Super-Combat, not humiliate you, Wonder Woman..."
    call CombatPlus from _call_CombatPlus_1
    mc "Ah, there you go, I got my point, so I'll unbound you and we can both forget about this little incident, which YOU started by challenging ME."
    ww "It was my mistake, Master. I am sorry."
    jump Main

label GymWonderAgility:
$ seenwonderagility = True
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
if period == 0:
    scene wonderstretch14day with dissolve
if period == 1:
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
if age >= 18 and age <= 19:
    ww" Your fat teen BULLBALLS look like they are churning up something..."
scene wonderstretch19 with dissolve
ww "What, you're getting hard while doing the exercise I assigned you???"
mc "AM I? I can't tell from where I'm standing. Or sitting."
ww "Can't you feel all that blood that RUSHED towards your enormous penis?"
mc "I'll go soft once you get me soft... It's the only way out of this sticky situation, Gal. I mean, Princess Diana."
ww "I've had enough of your childish shenanigans! I'm going to pump the seed right out of that filthy dong of yours!"
mc "Alright!"
ww "If I manage to make it fit..."
window hide

label GymWonderStretchSlow:
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
call screen gymwonderstretchslow()
screen gymwonderstretchslow():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("GymWonderStretchFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymWonderStretchEnd")

label GymWonderStretchFast:
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
call screen gymwonderstretchfast()
screen gymwonderstretchfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("GymWonderStretchSlow")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymWonderStretchEnd")

label GymWonderStretchEnd:
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
if mcagility == 0:
    call AgilityPlus from _call_AgilityPlus_1
    mc "FUCK YEAH!"
ww "That was NOT meant to happen... You fucked my throat and I'm full of your semen!"
mc "Yeah, sure, but it was tasty, right?"
scene wonderblowcum06 with dissolve
ww "I... suppose it was... Very tasty. Please go back to your room, I need to get cleaned up..."
jump Main

label WonderGymMuscles:
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar
$ seenwonderbeast = True
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
if age >= 18 and age <= 19:
    mc "Fifteen inches of prime teenage boymeat for you, Wonder Woman!"
ww "Wonder Woman's biceps will handle this BEAST!"
play channel2 "sounds/boymoan04.mp3"
window hide

label GymWonderBeast:
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
call screen gymwonderbeast()
screen gymwonderbeast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("GymWonderBeastPOV")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("GymWonderBeastEnd")

label GymWonderBeastPOV:
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
call screen gymwonderbeastpov()
screen gymwonderbeastpov():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("GymWonderBeast")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("GymWonderBeastEnd")

label GymWonderBeastEnd:
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
show screen statscreenicon
show screen questscreenicon
show screen calendar
jump Main

label GymWonderLevel02:
stop music
play music "sounds/relax.mp3"
scene wonderyoga01 with dissolve
ww "Shush, [name]. I need to concentrate."
mc "Alright, I'll just watch."
scene wonderyoga02 with dissolve
$ renpy.pause(1.0, hard=True)
scene wonderyoga03 with fastdissolve
mc "* Damn, look at her abs tensing... *"
scene wonderyoga03b with fastdissolve
mc "* Even better with a zoom-in... *"
window hide
show wonderyogaflex
pause
scene wonderyoga04 with dissolve
play sound "sounds/femalegrunt01.mp3"
$ renpy.pause(1.0, hard=True)
scene wonderyoga05 with dissolve
mc "* This exercise ball doesn't stand a chance in hell against Wonder Woman. *"

scene wonderyoga06 with dissolve
$ renpy.pause(1.0, hard=True)
scene wonderyoga07 with dissolve
play sound "sounds/moan02.mp3"
mc "She seems to be enjoying herself. A LOT!"
scene wonderyoga08 with dissolve
stop sound
ww "Now we can talk. Mano a Wonder Womano."
stop music
scene gymwidowbackground
show level02wondergym01 at centerleft
with dissolve
show level02wondergym01 at centerleft:
    breathe
ww "Are you here to train your muscles?"
label GymWonderDialoguesc:
menu:
    "Damn right, Princess Diana!" if wondertalkbaby == False:
        hide level02wondergym01
        show level02wondergym03 at centerleft
        with fastdissolve
        ww "I appreciate you calling me by my regal name. The support for monarchy is lacking in this modern world. I think the people need a TRUE Queen."
        mc "Err, Cockham City is a democracy, you know. We elect our mayor and all that."
        hide level02wondergym03
        show level02wondergym04 at centerleft
        with fastdissolve
        ww "I see. What a weird concept it is, to trust professional liars."
        mc "You ain't making Cockham great again with that attitude."
        hide level02wondergym04
        show level02wondergym01 at centerleft
        with fastdissolve
        show level02wondergym01 at centerleft:
            breathe
        jump GymWonderDialoguesc
    "Of course, I need to keep them in shape. And that shape is HU-U-UGE!" if wondertalkbaby and wonderbirth == False:
        $ level02gymspokewonder01 = True
        hide level02wondergym01
        show level02wondergym04 at centerleft
        with fastdissolve
        ww "Bragging won't make your muscles stronger."
        mc "It can still help in spreading FEAR into my enemies!"
        hide level02wondergym04
        show level02wondergym05 at centerleft
        with fastdissolve
        ww "Wonder Woman is not afraid of ANYBODY!"
        mc "But you're kind of afraid about our baby, aren't you?"
        hide level02wondergym05
        show level02wondergym04 at centerleft
        with fastdissolve
        ww "I... fear FOR him."
        mc "Oh, so it's a boy then?"
        hide level02wondergym04
        show level02wondergym02 at centerleft
        with fastdissolve
        ww "Yes, I can feel it. His... Never mind."
        hide level02wondergym02
        show level02wondergym01 at centerleft
        with fastdissolve
        show level02wondergym01 at centerleft:
            breathe
        jump GymWonderDialoguesc
    "What were you doing with that exercise ball?" if wonderbirth == False:
        hide level02wondergym01
        show level02wondergym04 at centerleft
        with fastdissolve
        ww "I need to work on my stomach muscles. I don't want to get all flabby and ugly during my pregnancy."
        mc "But you still don't look very pregnant."
        hide level02wondergym04
        show level02wondergym02 at centerleft
        with fastdissolve        
        ww "I can feel a small bump. That is getting bigger and bigger by the day."
        mc "Well, you still look Super-Sexy to me. Level 03 at least."
        hide level02wondergym02
        show level02wondergym03 at centerleft
        with fastdissolve        
        ww "Thank you... [name]."
        hide level02wondergym03
        show level02wondergym01 at centerleft
        with fastdissolve
        show level02wondergym01 at centerleft:
            breathe
        jump GymWonderDialoguesc
    "What were you doing with that exercise ball?" if wonderbirth:
        hide level02wondergym01
        show level02wondergym04 at centerleft
        with fastdissolve
        ww "I need to work on my stomach muscles. After giving birth, I feel that my skin is a bit... stretched."
        mc "You already seeem to be in great shape again. And my cock is also starting to get into great sh..."
        hide level02wondergym04
        show level02wondergym02 at centerleft
        with fastdissolve        
        ww "This is not the time and place, [name]...."
        mc "Well, just saying you still look Super-Sexy to me. Level 03 at least."
        hide level02wondergym02
        show level02wondergym03 at centerleft
        with fastdissolve        
        ww "Thank you... [name]."
        hide level02wondergym03
        show level02wondergym01 at centerleft
        with fastdissolve
        show level02wondergym01 at centerleft:
            breathe
        jump GymWonderDialoguesc
    "Can you do that Wonder Woman costume changing trick again?":
        hide level02wondergym01
        show level02wondergym05 at centerleft
        with fastdissolve
        ww "Does Wonder Woman look like a circus clown?"
        mc "Err.. No. No, she doesn't."
        hide level02wondergym05
        show level02wondergym01 at centerleft
        with fastdissolve
        show level02wondergym01 at centerleft:
            breathe
        jump GymWonderDialoguesc
    "Will you teach me how to enhance my Super-Senses, Princess Diana?" if level02gymspokewonder01:
        if mcsenses == 2:
            hide level02wondergym01
            show level02wondergym05 at centerleft
            with fastdissolve
            ww "But you're already on Level02 like me. I can't train you further than my level."
            mc "Oh. Ok, how about we train TOGETHER then? You know, just to keep up with stuff and all that."
            hide level02wondergym05
            show level02wondergym02 at centerleft
            with fastdissolve
            ww "Fine, I suppose Super-Senses need to be refreshed every now and then."
            hide level02wondergym02
            show level02wondergym01 at centerleft
            with fastdissolve
            show level02wondergym01 at centerleft:
                breathe
            jump WonderSensesTrain
        if mcsenses == 1 and evilness >= 13:
            hide level02wondergym01
            show level02wondergym05 at centerleft
            with fastdissolve
            ww "And why would Wonder Woman train a Super-Hero who is fast becoming a SUPER-VILLAIN?"
            mc "Do you want me to remind you who is the Master here? I'm not sure our baby could survive another mighty ANAL POUNDING."
            hide level02wondergym01
            show level02wondergym05 at centerleft
            with fastdissolve
            ww "You are truly a Super-Villain of the most evil nature, threatening the very future mankind of your past. I will teach you, but under duress."
            hide level02wondergym05
            show level02wondergym01 at centerleft
            with fastdissolve
            show level02wondergym01 at centerleft:
                breathe
            jump WonderSensesTrain
        if mcsenses == 1 and evilness <= 12:
            hide level02wondergym01
            show level02wondergym03 at centerleft
            with fastdissolve
            ww "I suppose it is a League member's duty to train her fellow companions. Especially those of inferior rank like yourself."
            mc "Hey! I'm LEVEL OH-TWO NOW!"
            hide level02wondergym03
            show level02wondergym04 at centerleft
            ww "Hopefully, our child won't be born on Level 01. Let me train you. And him at the same time."            
            hide level02wondergym04
            show level02wondergym01 at centerleft
            with fastdissolve
            show level02wondergym01 at centerleft:
                breathe
            jump WonderSensesTrain
    "I'm done here. I'll go and lift super-heavy iridium barbells.":
        hide level02wondergym01
        show level02wondergym05 at centerleft
        with fastdissolve
        ww "Wonder Woman is NEVER DONE."
        jump GymMCCurl

label WonderSensesTrain:
ww "First, you need to prep your body. You choose your own method. I'll be doing squats. The important thing is to feel TENSE afterwards."
mc "That's weird, it's totally the opposite of what Powergirl told me."
hide level02wondergym01
show level02wondergym05 at centerleft
with fastdissolve
ww "She was only teaching you Level01 Super-Senses. For Level02, you need to up your game!"
mc "Right, right, totally makes super-sense now. I'll be doing curls then, I'm good at that lately."
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar

window hide
stop music
play music "sounds/gymmusic.mp3"

label WonderSquat: 
hide mccurlicon
hide wondersquaticon
show wondersquatvideo behind mcupcurlvideo
hide mcupcurlvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show mccurlicon:
     xpos 1700 ypos 500     

call screen wondersquat()
screen wondersquat():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McUpCurl")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderSensesTrainEnd")

label McUpCurl:
hide mccurlicon
hide wondersquaticon
show mcupcurlvideo behind wondersquatvideo
hide wondersquatvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show wondersquaticon:
     xpos 50 ypos 500     

call screen mcupcurl()
screen mcupcurl():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderSquat")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderSensesTrainEnd")

label WonderSensesTrainEnd:
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
if mcsenses == 1:
    call SensesPlus from _call_SensesPlus_2
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

label WonderBlowShortSlow:
window hide
$ wonderblowharder = False
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
$ wonderblowfuckfast = False
if wonderblowfuckslow == False:
    mc "AAAh, this is so good, Wonder Woman!"
    $ wonderblowfuckslow = True
window hide
pause
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowshortslow()
screen wonderblowshortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVSlow")

label WonderBlowShortFast:
$ wonderblowharder = False
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
$ wonderblowfuckslow = False
if wonderblowfuckfast == False:
    mc "Mmmh, my cock LIKES that!"
    $ wonderblowfuckfast = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderblowshortfast()
screen wonderblowshortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVFast")

label WonderBlowShortPOVSlow:
$ wonderblowharder = False
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
$ wonderblowfuckfast = False
if wonderblowfuckslow == False:
    mc "AAAh, this is so good, Wonder Woman!"
    $ wonderblowfuckslow = True
window hide
pause

show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowshortpovslow()
screen wonderblowshortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortSlow")

label WonderBlowShortPOVFast:
$ wonderblowharder = False
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
$ wonderblowfuckslow = False
if wonderblowfuckfast == False:
    mc "Mmmh, my cock LIKES that!"
    $ wonderblowfuckfast = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderblowshortpovfast()
screen wonderblowshortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowShortPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowShortFast")

label WonderBlowHardSlow:
if wonderblowharder == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharder = True        
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
call screen wonderblowhardslow()
screen wonderblowhardslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEnd")

label WonderBlowHardFast:
if wonderblowharder == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharder = True        
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
call screen wonderblowhardfast()
screen wonderblowhardfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEnd")

label WonderBlowHardPOVSlow:
if wonderblowharder == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharder = True        
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
call screen wonderblowhardpovslow()
screen wonderblowhardpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEnd")

label WonderBlowHardPOVFast:
if wonderblowharder == False:
    mc "Please go deeper, my cock is just ssso HARD, it almost hurts, I NEED to come!"
    $ wonderblowharder = True        
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
call screen wonderblowhardpovfast()
screen wonderblowhardpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBlowHardPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WonderBlowShortPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBlowHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBlowEnd")

label WonderBlowEnd:
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
show screen statscreenicon
show screen questscreenicon
show screen calendar
jump Main
    
label GymWidow:
$ seengym = True
if period == 0:
    scene gymwidowhit01 with fade
if period == 1:
    scene gymwidowhit01night with fade
mc "Let's have a look at how the Black Widow handles this MASSIVE punching bag..."
if period == 0:
    scene gymwidowhit02 with dissolve
if period == 1:
    scene gymwidowhit02night with dissolve
play sound "sounds/punch.mp3"
$ renpy.pause(1.0, hard='True')
if period == 0:
    scene gymwidowhit01 with dissolve
if period == 1:
    scene gymwidowhit01night with dissolve
mc "She's kicking the hell out of it..."
if period == 0:
    scene gymwidowhit03 with dissolve
if period == 1:
    scene gymwidowhit03night with dissolve
play sound "sounds/punch.mp3"
$ renpy.pause(1.0, hard='True')
mc " * cough *"

label GymWidowDialogues:
stop music
scene gymwidowbackground
with fade
show gymwidow03 at centerleft with moveinright
bw "That was a nice COMBAT workout..."
hide gymwidow03
show widowgymeyeblink
with dissolve
if mclevel02 == False:
    bw "You want to spar with me on the punching bag, [name]?"
if mclevel02:
    bw "What brings you here [name]? You feel like you NEED the Black Widow's help again?"
label GymWidowDialoguesb:
menu:
    "Sure. I'm gonna show you how STRONG I am!" if mclevel02 == False:
        hide widowgymeyeblink
        show gymwidow05 at centerleft
        with fastdissolve
        $ gymwidowspar = True
        bw "Let's see what you've got, big boy..."
        jump WidowPunchingBall
    "Maybe it's time to raise it up one notch and FIGHT in the arena!" if period == 1 and gymwidowspar and mclevel02 == False:
        jump SuperCombatTraining
    "No, I'd rather train on the weights and keep my muscles HUGE!" if mclevel02 == False:
        hide widowgymeyeblink
        show gymwidow02 at centerleft
        with fastdissolve
        bw "Alright... Maybe I'll come and watch your progress at the end..."
        jump GymMCLift
    "With how BIG I've grown, I don't need any help anymore. And I'm gonna curl super-heavy dumbbells to prove it!" if mclevel02:
        hide widowgymeyeblink
        show gymwidow02 at centerleft
        with fastdissolve
        bw "Alright... Maybe I'll come and watch your progress at the end..."
        jump GymMCCurl
    "I'm ready to FIGHT! And this time, I'll BEAT you!" if mclevel02:
        hide widowgymeyeblink
        show gymwidow02 at centerleft
        with fastdissolve
        bw "Is that so? You think you can beat the Black Widow in a fight?"
        mc "Do you accept my challenge Natasha, or are you chickening out?"
        hide gymwidow02
        show gymwidow04 at centerleft
        with fastdissolve
        bw "Of course I accept! Just to show you how preposterous your hopes are. Get on the ring and wait for me!"
        jump WidowWrestlingLevel02
    "I'm good, I was just watching you is all.":
        hide widowgymeyeblink
        show gymwidow02 at centerleft
        with fastdissolve
        bw "Like a pervy voyeur."
        mc "Yeah, pretty much."
        hide gymwidow02
        show gymwidow04 at centerleft
        with fastdissolve
        bw "Well, what do you think about what you saw?"
        mc "You can beat the crap out of a punching bag is the the conclusion I can reach."
        hide gymwidow04
        show gymwidow03 at centerleft
        with fastdissolve
        bw "Oh, you'll find that I can beat the hell out of much MORE than that! * wink *"
        mc "Right, right... I'd better go, it's getting late."
        jump Main

label WidowPunchingBall:
play music "sounds/gymmusic.mp3"
scene widowgymspar01 with fade
bw "Put on some gloves and let's PUNCH!"
if period == 0:
    scene widowgymspar02 with dissolve
if period ==1:
    scene widowgymspar02night with dissolve
bw "Ready [hero]?"
mc "I AM, Black Widow!"
if period == 0:
    scene widowgymspar03 with dissolve
if period ==1:
    scene widowgymspar03night with dissolve
play sound "sounds/punch.mp3"
bw "Punch back if you can!"
if mccombat == 0:
    call screen usepower("usestrength", "WidowGymNoStrength", "WidowGymStrength") with dissolve
if mccombat == 1:
    call screen usepower("usecombat", "WidowGymNoStrength", "WidowGymStrength") with dissolve

label WidowGymStrength:
play sound "sounds/punch.mp3"
if period == 0:
    scene widowgymspar04 with dissolve
if period ==1:
    scene widowgymspar04night with dissolve
mc "Take that mighty punch!"
bw "Brute strength will get you nowhere..."
if period == 0:
    scene widowgymspar05 with dissolve
if period ==1:
    scene widowgymspar05night with dissolve
bw "...EXCEPT EXACTLY WHERE I WANTED YOU TO BE!"
play sound "sounds/whoosh.mp3"
if period == 0:
    scene widowgymspar06 with dissolve
if period ==1:
    scene widowgymspar06night with dissolve
mc "Err, what the???"
scene widowgymspar07 with dissolve
bw "You didn't see that coming [hero]? Your superpowers are no match for MY Super-Combat abilities!"
mc "Hey, get off me, the punching bag is..."
scene widowgymspar08 with dissolve
play sound "sounds/punch.mp3"
bw "..swinging back right AT YOU!"
scene widowgymspar09a with dissolve
bw "I hope you learnt a valuable lesson [name]..."
scene widowgymspar09b with dissolve
bw "The lesson being, you CAN'T BEAT THE BLACK WIDOW!"
mc "Okay, okay, I give up, you win..." 
scene widowgymspar09c with dissolve
bw "And you can't just get a hardon while I'm pinning you down to the ground and hope something will come out of it..."
mc "I can't? Damn..."
scene widowgymspar09b with dissolve
bw "Next time, we might try and fine-tune your combat abilities so you don't end up in such an embarrassing predicament..."
bw "But for now... You can get back to your room and reflect on your mistakes..."
jump Main

label WidowGymNoStrength:
play sound "sounds/punch.mp3"
if period == 0:
    scene widowgymspar10 with dissolve
if period == 1:
    scene widowgymspar10night with dissolve
mc "I'll play her little game..."
if period == 0:
    scene widowgymspar12 with dissolve
if period == 1:
    scene widowgymspar12night with dissolve
play sound "sounds/punch.mp3"
bw "Nice punch, but take that now!"
if period == 0:
    scene widowgymspar11 with dissolve
if period == 1:
    scene widowgymspar11night with dissolve
play sound "sounds/punch.mp3"
mc "I'm not done!"
if period == 0:
    scene widowgymspar12 with dissolve
if period == 1:
    scene widowgymspar12night with dissolve
play sound "sounds/punch.mp3"
bw "Keep it up a while longer..."

stop music
scene gymwidowbackground
with fade
show gymwidow01 at centerleft with moveinright
"A while later..."
hide gymwidow01
show widowgymeyeblink
bw "I think we trained well. You might acquire some Super-Combat abilities one day..."
mc "Yeah, like when?"
hide widowgymeyeblink
show gymwidow04 at centerleft
with dissolve
bw "Come back another time and I'll train you. Perhaps."
mc "I see... See you then, Natasha."
jump Main

label SuperCombatTraining:
hide widowgymeyeblink
show gymwidow05 at centerleft
with fastdissolve
$ combattraining += 1
if combattraining == 1:
    bw "I guess you're ready for some preliminary ass-kicking... Get into your Super-Combat gear... There's a singlet in your locker."
    mc "Is there? I didn't even know..."
    hide gymwidow05
    show gymwidow02 at centerleft
    with fastdissolve
    bw "I'll be waiting for you in the ring... In MY Super-Combat gear."
    jump CombatTraining
if combattraining >= 2:
    bw "I think it's time to up the challenge even more. NAKED FIGHTING! The PUREST form of Super-Combat!"
    mc "Alright!"
    jump CombatTrainingNaked

label CombatTraining:
stop music
play sound "sounds/barfight.mp3"
scene wrestling01 with fade
mc "I'm ready, Black Widow!"
scene wrestling02 with dissolve
bw "So am I!"
mc "I'll show you how a REAL MAN fights! Against a girl."
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestling03 with dissolve
bw "You think you're stronger than me in Super-Combat just because you have bigger muscles? Let's see how you cope with my SPECIAL attack!"
scene wrestling04 with dissolve
play sound "sounds/whoosh.mp3"
mc "Hey! What are you doing?"
bw "You can't catch me? I thought you were a TRUE warrior!"
scene wrestling05 with dissolve
play sound "sounds/punch.mp3"
mc "Ouch! From the back, that's not fair!"
bw "There are NO RULES in SUPER-COMBAT!"
scene wrestling06 with dissolve
play sound "sounds/bonecrack.mp3"
bw "And now you are at my mercy!"
mc "Please! You're going to break my back!"
scene wrestling07 with dissolve
bw "A SUPERHERO needs to learn to sustain EXTREME injury. How would you cope with fighting POWERFUL Super-Villains?"
mc "I... Yield! Let's try again, I'll do better this time!"
scene wrestling08 with dissolve
bw "Oh, you think so? You think you can beat the Black Widow, do you?"
mc "Err... I'll try at least, let me go and I'll show you!"
bw "Fine... I won't break your neck. This time."
scene wrestling01 with fade
play sound "sounds/barfight.mp3"
mc "I've studied your tactics, this time, you won't get me!"
scene wrestling02 with dissolve
bw "Is that so? Let's see..."
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestling10 with dissolve
play sound "sounds/whoosh.mp3"
mc "You're... levitating now?"
bw "No, I'm CONCENTRATING!...MY PUNCHING POWER!"
scene wrestling11 with dissolve
play sound "sounds/punch.mp3"
mc "I saw it coming, I'm blocking your mighty punch!"
bw "It was just a distracting punch..."
scene wrestling12 with dissolve
play sound "sounds/punch.mp3"
bw "...for THIS!"
mc "OU-OU-CH! My dick!"
scene wrestling13 with dissolve
play sound "sounds/panting.mp3"
mc "That was BELOW THE BELT!"
bw "I told you there are no rules in Super-Combat!"
mc "Now you've made me Super-Angry!"
bw "Oh yeah? Well, I..."
scene wrestling14 with dissolve
play sound "sounds/whoosh.mp3"
mc "So angry I might break YOUR neck this time!"
bw "What? No, I... Let me down, I yield!"
scene wrestling15 with dissolve
play sound "sounds/thud.mp3"
mc "Admit I'm the strongest here, Black Widow!"
bw "Oh yeah, you're so strong! I'm so in awe at your amazing Super-Com..."        
scene wrestling16 with dissolve
play sound "sounds/punch.mp3"
bw "You're too easily distracted, [name]!"
scene wrestling17 with dissolve
bw "Now I hold you in a tight leglock. What are you going to do?"
mc "AAAH! Err, yield?"
bw "NO! FOCUS all your RAGE and POWER! It's the only way to defeat your ENEMIES!" 
scene wrestling18 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "RHAAA!"
bw "That's good! Your muscles... They're getting BIGGER and STRONGER!"
scene wrestling19 with dissolve
mc "GET OFF ME! I AM THE MIGHTY SUPERHERO!"
bw "I... can't hold my grip, you did it, [name]!"
scene wrestling20 with dissolve
mc "I HOLD THE ABSOLUTE SUPER-POWER!"
if mccombat == 0:
    bw "Err, calm down now... You only levelled up a bit. Put me down, your training is done!"
if mccombat >= 1:
    bw "Err, calm down now... Let's not get carried away. Put me down, your training is done!"
scene wrestling21 with dissolve
if age >= 20:
    bw "Now I truly am in AWE of your MONSTER MUSCLE BODY!"
if age >= 18 and age <= 19:
    bw "Now I truly am in AWE of your MONSTER TEENAGE MUSCLE BODY!"
if mccombat == 0:
    call CombatPlus from _call_CombatPlus_2
    mc "FUCK YEAH!"
bw "I think we're done for the evening... I'm going back to my room to play with my... little \"friend\"."
jump Main

label CombatTrainingNaked:
stop music
play sound "sounds/barfight.mp3"
scene wrestling40 with fade
mc "Why are we naked exactly? Apart from the fact that the dev is a pervert."
scene wrestling41 with dissolve
bw "You are too easily distracted by... womanly bits. It's the only way to teach you to FOCUS!"
mc "I buy it, it makes total sense."
bw "So be ready. TO FIGHT!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestling42 with dissolve
play sound "sounds/punch.mp3"
bw "Take that for starters!"
mc "Hey!"
scene wrestling43 with dissolve
play sound "sounds/punch.mp3"
bw "And THIS!"
mc "Watch out for my groin! It's super-important to me!"
scene wrestling44 with dissolve
play sound "sounds/panting.mp3"
bw "The Black Widow's aim is always SPOT ON."
scene wrestling45 with dissolve
mc "That's it, now you've made my cock ANGRY!"
bw "Ooh, I'm so scared. NOT!"
scene wrestling46 with dissolve
play sound "sounds/gasp.mp3"
mc "You will be soon, Black Widow..."
scene wrestling47 with dissolve
bw "What do you think you're doing?"
mc "I am making sure you SUBMIT to my SUPERIOR MUSCLES!"
scene wrestling48 with dissolve
mc "And I'm fondling your tits while I'm at it!"
scene wrestling49 with dissolve
bw "You're just a filthy PERVERT! But that will be your downfall..."
scene wrestling50 with dissolve
play sound "sounds/whoosh.mp3"
bw "For your strength is no match to the Black Widow's Super-Agility and Super-Combat stats!"
mc "How on...?"
play channel1 "sounds/sexy10.mp3"
scene wrestling57 with dissolve
bw "Now you are at MY mercy. And so is your COCK!"
scene wrestling58 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Oooh, you want to cum so badly, don't you? But my GRIP on your spermtube won't let you reach that pleasure spot... Just yet."
mc "Please Natasha, this is excrutiating!"
scene wrestling57 with dissolve
bw "I'll make you come when I DECIDE!"
play sound "sounds/boymoan02.mp3"
mc "Decide quickly then!"
scene wrestling59 with dissolve
bw "I'll let you come... Just a LITTLE!"
play sound "sounds/boymoan05.mp3"
scene wrestling58 with dissolve
bw "But not a full-blown orgasm..."
play sound "sounds/boymoan02.mp3"
mc "That is so cruel!"
scene wrestling57 with dissolve
bw "I'm teaching you SELF-CONTROL, [name]. You should be grateful. It is an essential part of Super-Combat."
mc "Alright, I got it, I got it, I am self-controlling, I swear! Just let me come!"
scene wrestling59 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Are you really though... I wonder. Let's see... Come just a little and then... STOP!"
scene wrestling57 with dissolve
play sound "sounds/panting.mp3"
if age >= 20:
    bw "Maybe you are after all, I'm not even gripping THAT tightly around your engorged monsterdong and you've stopped SPEWING."
if age >= 18 and age <= 19:
    bw "Maybe you are after all, I'm not even gripping THAT tightly around your engorged teenage monsterdong and you've stopped SPEWING."
mc "So, do I get a rew..."
scene wrestling59 with dissolve
play music "sounds/boyorgasm01.mp3"
bw "Now COME! BLAST THAT HOT SAUCE!"
window hide
with fastflash
mc "AAAH!"
scene wrestling60 with dissolve
play sound "sounds/thud.mp3"
bw "Oooh, look at you... You're coming all over yourself now, that's so FILTHY!"
window hide
with fastflash
mc "Oh GOD..."
scene wrestling61 with dissolve
play sound "sounds/wow.mp3"
bw "You really NEEDED to come, didn't you?"
window hide
with fastflash
if age >= 20:
    bw "That's a LOT of dirty scum you're spewing right there!"
if age >= 18 and age <= 19:
    bw "That's a LOT of dirty teen scum you're spewing right there!"
scene wrestling62 with dissolve
stop music
bw "You've BLASTED so MUCH cum! It's all over yourself..."
play sound "sounds/panting.mp3"
mc "Ggg..."
scene wrestling63 with dissolve
play sound "sounds/lick01.ogg"
bw "I'll help you clean it up... It's so TASTY!"
scene wrestling64 with dissolve
play sound "sounds/slurp.mp3"
bw "I gather I got MOST of it... Mmmh... * slurp * Goodnight, [name]!"
stop channel1
jump Main

label GymMCLift:
$ seengym = True
if period == 0:
    scene gymmcprelift01 with fade
if period == 1:
    scene gymmcprelift01night with fade
mc "It's already loaded with a HEAVY set of weights. Now it's my turn to PROVE I'm a Super-Strong Superhero!"
if (period == 0 and d10locday <= 4) or (period == 1 and (d10locnight == 3 or d10locnight == 4 or d10locnight == 7)):
    menu:
        "Train with thong on":
            jump GymMCLiftThong
        "Go commando and train naked":
            mc "Well, there's no one around so I could do that..."
            jump GymMCLiftNude

label GymMCLiftThong:
scene gymmcliftvideo with dissolve
pause
mc "Fuck yeah! Lifting over three tons of weights! A few more reps..."
window hide
pause
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymmcpostlift01 with dissolve
    mc "That was a nice workout... I feel like my muscles have GROWN a bit..."
if d3rollgymworkout == 2:
    scene gymmcpostlift02 with dissolve
    mc "Grrr! I could scare away any Super-Villain with MY muscles now!"
if d3rollgymworkout == 3:
    scene gymmcpostlift03 with dissolve
    if age >= 20:
        mc "Damn! Check those biceps, monster muscle stud right there!"
    if age >= 18 and age <= 19:
        mc "Damn! Check those biceps, monster teenage muscle stud right there!"

if (period == 0 and d10locday == 7) or (period == 1 and d10locnight == 9):
    scene gymmcpostliftwidow01 with dissolve
    bw "Instead of flexing for nobody but yourself, why don't you let ME feel up those huge muscles..."
    mc "Yeah, I feel so buffed up, you want to feel them?"
    scene gymmcpostliftwidow02 with dissolve
    bw "I sure do... Wow, sssoo, so BIG and STRONG!"
    if mcstrength == 1:
        mc "Damn right, Super-Strength level 1 in action!"
    if mcstrength == 2:
        mc "Damn right, Super-Strength level 2 in action!"
    if mcstrength == 3:
        mc "Damn right, Super-Strength level 3 in action!"
    scene gymmcpostliftwidow03 with dissolve
    bw "And there's something else that's BIG and STRONG..."
    mc "Oh yeah, MASSIVE even!"
    scene gymmcpostliftwidow04 with dissolve
    if age >= 20:
        bw "Stop bragging and kiss me, STUD!"
    if age >= 18 and age <= 19:
        bw "Stop bragging and kiss me, TEENAGE STUD!"
    scene gymmcpostliftwidow05 with dissolve
    play sound "sounds/kiss.mp3"
    bw "Let's see if you're a good kisser..."
    play sound "sounds/kiss.mp3"
    if period == 0:
        scene gymmcpostliftwidow06 with dissolve
    if period == 1:
        scene gymmcpostliftwidow06night with dissolve
    bw "Not bad for such a young'un..."
    mc "Good kisser AND good fuc..."
    bw "Shush... Remember what happened to my late husband?... I wouldn't want to EXHAUST you after this heavy workout, [name]!"
    stop channel1
    jump Main

if (period == 0 and d10locday == 6) or (period == 1 and d10locnight == 5):
    if period == 0:
        scene gymmcmilf01 with dissolve
    if period == 1:
        scene gymmcmilf01night with dissolve
    cm "Oooh, sweetie, you're so RIPPED!"
    scene gymmcmilf02 with dissolve
    cm "Let me get a CLOSER look at your muscles after this HEAVY workout..."
    mc "Yeah, get as CLOSE as you like!"
    scene gymmcmilf03 with dissolve
    cm "Is that your hand I can feel trying to reach for my ass?"
    mc "Yes, I want to feel YOUR body too..."
    cm "Right now, it's MY turn and MY turn ONLY... Flex your arm for your landlady and I'll show you..."
    scene gymmcmilf04 with dissolve
    cm "Wow, they are like heavy globes of TITANIUM!"
    mc "You like them, Carol?"
    cm "I LOVE them... Let me kiss this montainous bicep..."
    if period == 0:
        scene gymmcmilf05 with dissolve
    if period == 1:
        scene gymmcmilf05night with dissolve
    play music "sounds/kiss.mp3"
    mc "Yeah, kiss those huge boulders, Captain MILF!"
    stop music
    if age >= 20:
        cm "Please hold me and let me FEEL the POWER of your young muscled body!"
    if age >= 18 and age <= 19:
        cm "Please hold me and let me FEEL the POWER of your young muscled teenage body!"
    scene gymmcmilf06 with dissolve
    cm "Mmmh, yes... Kiss my neck please..."
    play sound "sounds/kiss.mp3"
    scene gymmcmilf07 with dissolve
    mc "There's no one else around, Carol..."
    cm "So you were thinking we could do something NAUGHTY? Not today, sweetie, I have a lot of work to do..."
    mc "So... You're leaving? Like, just when my muscles are even MORE MASSIVE than normal?"
    cm "Yes... You're not level 2 yet. You need to GROW some more... * wink *"
    stop channel1
    jump Main
stop channel1
jump Main

label GymMCCurl:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ seengym = True
scene gymmcprecurl01 with fade
mc "Let's get rid of this ridiculously light barbell and use Superman's iridium dumbbells instead. They weigh over 10 TONS each and I feel SUPER-STRONG right now!"
if (period == 0 and d10locday <= 4) or (period == 1 and (d10locnight == 3 or d10locnight == 4 or d10locnight == 7)):
    menu:
        "Train with thong on":
            jump GymMCCurlThong
        "Go commando and train naked":
            mc "And since no one is around, I'll go COMMANDO and train NAKED!"
            jump GymMCCurlNude

label GymMCCurlThong:
scene gymmcprecurl02 with dissolve
mc "That's it. Ready to RUMBLE!"
window hide
play channel2 "sounds/effort01.mp3"
show gymmccurlvideo with dissolve
pause
mc "Fuck yeah! Chest-pressing over 20 TONS! A few more reps..."
window hide
pause
stop channel2
scene gymmcpostcurl01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
mc "Wow, look at those damn MASSIVE biceps! Need to pose and admire my hot muscled body like a total narcisssist pronto!"
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymmcpost04 with dissolve
    mc "That was a nice workout... I feel like my biceps have really GROWN even MORE..."
if d3rollgymworkout == 2:
    scene gymmcpost05 with dissolve
    mc "Grrr! I could scare away any enemy with THOSE muscles now!"
if d3rollgymworkout == 3:
    scene gymmcpost06 with dissolve
    if age >= 20:
        mc "Damn! Check those biceps, monster muscle STUD right there!"
    if age >= 18 and age <= 19:
        mc "Damn! Check those biceps, monster teenage muscle STUD right there!"
    mc "But no one around to admire them but me... * sigh *"

if period == 1 and (d10locnight == 5 or d10locnight == 6):
    play music "sounds/sexy03.mp3"
    scene gymmcmilflevel01 with dissolve
    cm "Ooh, my landboy is getting so BIG!" 
    mc "Err, Captain MILF?"
    scene gymmcmilflevel02 with dissolve
    cm "I also finished my gym session and was feeling like POSING in front of the mirror too!" 
    mc "So maybe we should do it together? Like, some superhero COUPLE facing the most DASTARDLY Super-Villains."
    scene gymmcmilflevel03 with dissolve
    cm "Why not, I like your way of thinking, [name]. Let's make sure they can sense their imminent DOOM!"
    mc "I'll talk them down until they SUBMIT to the Cockham League of Justice! Watch me, Carol."
    scene gymmcmilflevel04 with dissolve
    mc "Are you talking to me? Are YOU talking to ME?"
    cm "Look at them, I can read the FEAR on their faces... Get on your knees in front of me, please [name], I want to see us like that..."
    scene gymmcmilflevel05 with dissolve
    cm "Mmmh, yes, you look so MENACING, even though you're crouching, we're definitely the PERFECT superhero couple!"
    scene gymmcmilflevel06 with dissolve
    mc "So if we are a perfect couple, we should hold each other tight."
    scene gymmcmilflevel07 with dissolve
    cm "But, what are you doing, [name]? I'm... your League Captain, not just your landlady, this is..."
    scene gymmcmilflevel08 with dissolve
    mc "Please Carol, you can't leave me like this, my cock... It's getting HARD!"
    scene gymmcmilflevel09 with dissolve
    play sound "sounds/ripping.mp3"
    if age >= 20:
        cm "Oh dear, I can see that, it's getting so BIG too! You've got take it out of your thong or you'll RIP it apart! Bring that giant fuckstick over here, I want to FEEL it!"
    if age >= 18 and age <= 19:
        cm "Oh dear, I can see that, it's getting so BIG too! You've got take it out of your thong or you'll RIP it apart! Bring that giant teen fuckstick over here, I want to FEEL it!"
    scene gymmcmilflevel10 with dissolve
    cm "It's so BIG... You keep GROWING and GROWING, like a true SEX Superhero!"
    mc "Please let me take your bottom off now Carol, I'm dying to CUM inside you again!"
    cm "Right here, where everyone could see us if they walked in? I... can't allow this, my dear boy. But stick it between my legs and pretend you're fucking my wet snatch..."
    scene gymmcmilflevel11 with dissolve
    play sound "sounds/moan01.mp3"
    mc "At least help me get your top off..."
    cm "Fine, just this once..."
    scene gymmcmilflevel12 with dissolve
    mc "You have the best titties of the whole League, Captain MILF!"
    cm "What a charmer you are! Are you ready now? You'll see, the feel of the lycra rubbing against your hard dong will send ELECTRIC shockwaves down your shaft all the way to your balls!"
    play channel2 "sounds/wetmassage.mp3"

    label MilfGymWankSlow:
    play channel1 "sounds/moan02.mp3"
    $ milfwankgymtalkfast = False
    window hide
    hide nexticon
    hide faster
    hide slower
    hide front
    hide sceneicon
    show milfwankgymslowvideo behind milfwankgymfrontslowvideo
    show milfwankgymslowvideo behind milfwankgymfastvideo
    $ renpy.pause(1.0, hard='True')
    hide milfwankgymfrontslowvideo
    hide milfwankgymfastvideo
    with dissolve
    if milfwankgymtalkslow == False:
        if age >= 20:
            cm "Look at that huge monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
        if age >= 18 and age <= 19:
            cm "Look at that huge teenage monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
        $ milfwankgymtalkslow = True
    window hide
    
    show faster:
         xpos 1700 ypos 500     
    show front:
         xpos 50 ypos 500     
    call screen milfwankgymslow()
    screen milfwankgymslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymWankFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("MilfGymWankFrontSlow")

    label MilfGymWankFast:
    play channel1 "sounds/moan03.mp3"
    $ milfwankgymtalkslow = False
    window hide
    hide nexticon
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfwankgymtalkfast == False:
        mc "I'm gonna slide my shaft between those legs faster now, Captain MILF!"
        cm "Oooh God, it's gonna be so HOT!"
        $ milfwankgymtalkfast = True
    window hide
    show milfwankgymfastvideo behind milfwankgymfrontfastvideo
    show milfwankgymfastvideo behind milfwankgymslowvideo
    $ renpy.pause(1.0, hard='True')
    hide milfwankgymfrontfastvideo
    hide milfwankgymslowvideo
    with dissolve
    show nexticon:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500     
    show front:
         xpos 50 ypos 500     
    call screen milfwankgymfast()
    screen milfwankgymfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymWankSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("MilfGymWankFrontFast")

    label MilfGymWankFrontSlow:
    play channel1 "sounds/moan02.mp3"
    $ milfwankgymtalkfast = False
    window hide
    hide nexticon
    hide faster
    hide slower
    hide front
    hide sceneicon
    show milfwankgymfrontslowvideo behind milfwankgymslowvideo
    show milfwankgymfrontslowvideo behind milfwankgymfrontfastvideo
    $ renpy.pause(1.0, hard='True')
    hide milfwankgymslowvideo
    hide milfwankgymfrontfastvideo
    with dissolve
    if milfwankgymtalkslow == False:
        if age >= 20:
            cm "Look at that huge monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
        if age >= 18 and age <= 19:
            cm "Look at that huge teenage monstercock. It's sticking so far in front of my wet pussy when you slide it between my thighs!"
        $ milfwankgymtalkslow = True
    window hide

    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen milfwankgymfrontslow()
    screen milfwankgymfrontslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymWankFrontFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 80)        
            action Jump ("MilfGymWankSlow")

    label MilfGymWankFrontFast:
    play channel1 "sounds/moan03.mp3"
    $ milfwankgymtalkslow = False
    window hide
    hide nexticon
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfwankgymtalkfast == False:
        mc "I'm gonna slide my shaft between those legs faster now, Captain MILF!"
        cm "Oooh God, it's gonna be so HOT!"
        $ milfwankgymtalkfast = True
    window hide
    show milfwankgymfrontfastvideo behind milfwankgymfastvideo
    show milfwankgymfrontfastvideo behind milfwankgymfrontslowvideo
    $ renpy.pause(1.0, hard='True')
    hide milfwankgymfastvideo
    hide milfwankgymfrontslowvideo
    with dissolve
    show nexticon:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen milfwankgymfrontfast()
    screen milfwankgymfrontfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymWankFrontSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 80)        
            action Jump ("MilfGymWankFast")

    label MilfGymWankEnd:
    hide nexticon
    hide faster
    hide slower
    hide front
    hide sceneicon
    stop channel1
    mc "Why don't you grab it with your hands and slowly wank me off, Carol? You know you want to..."
    cm "Oooh, you're such a naughty landboy... But you're right, I can't help myself, I want to just hold this beautiful piece of boymeat in my hands!"
    play sound "sounds/moan01.mp3"
    scene milfwankhold01:
        subpixel True
        xpos 0.0
        linear 3.0 xpos -0.1    
    with dissolve
    cm "Sssoo huge.. So STURDY..."
    stop channel2
    play channel2 "sounds/wank.mp3"
    
    label MilfGymHandjobSlow:
    play channel1 "sounds/womansex06.mp3"
    $ milfhjgymtalkfast = False
    window hide
    hide cum
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfhjgymtalkslow == False:
        cm "It's like I have my own huge futa cock!"
        $ milfhjgymtalkslow = True
    window hide
    show milfhjgymslowvideo behind milfhjgymfrontslowvideo
    show milfhjgymslowvideo behind milfhjgymfastvideo
    $ renpy.pause(1.0, hard='True')
    hide milfhjgymfrontslowvideo
    hide milfhjgymfastvideo
    with dissolve

    show faster:
         xpos 1700 ypos 500     
    show front:
         xpos 50 ypos 500     
    call screen milfhjgymslow()
    screen milfhjgymslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymHandjobFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("MilfGymHandjobFrontSlow")

    label MilfGymHandjobFast:
    play channel1 "sounds/womansex02.mp3"
    $ milfhjgymtalkslow = False
    window hide
    hide cum
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfhjgymtalkfast == False:
        mc "Do it faster, I'm right on the edge, ready to BLAST OFF for you!"
        $ milfhjgymtalkfast = True
    window hide
    show milfhjgymfastvideo behind milfhjgymfrontfastvideo
    show milfhjgymfastvideo behind milfhjgymslowvideo
    $ renpy.pause(1.0, hard='True')
    hide milfhjgymfrontfastvideo
    hide milfhjgymslowvideo
    with dissolve
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500     
    show front:
         xpos 50 ypos 500     
    call screen milfhjgymfast()
    screen milfhjgymfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymHandjobSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymHandjobEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("MilfGymHandjobFrontFast")

    label MilfGymHandjobFrontSlow:
    play channel1 "sounds/womansex06.mp3"
    $ milfhjgymtalkfast = False
    window hide
    hide cum
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfhjgymtalkslow == False:
        cm "It's like I have my own huge futa cock!"
        $ milfhjgymtalkslow = True
    window hide
    show milfhjgymfrontslowvideo behind milfhjgymslowvideo
    show milfhjgymfrontslowvideo behind milfhjgymfrontfastvideo
    $ renpy.pause(1.0, hard='True')
    hide milfhjgymslowvideo
    hide milfhjgymfrontfastvideo
    with dissolve
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen milfhjgymfrontslow()
    screen milfhjgymfrontslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymHandjobFrontFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymHandjobEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 80)        
            action Jump ("MilfGymHandjobSlow")

    label MilfGymHandjobFrontFast:
    play channel1 "sounds/womansex02.mp3"
    $ milfhjgymtalkslow = False
    window hide
    hide cum
    hide faster
    hide slower
    hide front
    hide sceneicon
    if milfhjgymtalkfast == False:
        mc "Do it faster, I'm right on the edge, ready to BLAST OFF for you!"
        $ milfhjgymtalkfast = True
    window hide
    show milfhjgymfrontfastvideo behind milfhjgymfastvideo
    show milfhjgymfrontfastvideo behind milfhjgymfrontslowvideo
    $ renpy.pause(1.0, hard='True')
    hide milfhjgymfastvideo
    hide milfhjgymfrontslowvideo
    with dissolve
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen milfhjgymfrontfast()
    screen milfhjgymfrontfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("MilfGymHandjobFrontSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("MilfGymHandjobEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 80)        
            action Jump ("MilfGymHandjobFast")

    label MilfGymHandjobEnd:
    hide cum
    hide faster
    hide slower
    hide front
    hide sceneicon
    mc "I'm gonna come, Carol!"
    scene milfholdcum01 with dissolve
    play sound "sounds/boyorgasm01.mp3"
    stop channel2
    cm "No, I'm coming, not YOU, AAAH!"
    window hide
    with fastflash
    cm "I've got so much pent-up cum to discharge, I wanna cum and cum and cum!"
    scene milfholdcum02 with dissolve
    play sound "sounds/boymoan05.mp3"
    mc "Ooooh, AAAAH!"
    window hide
    with hpunch
    stop channel1
    play sound "sounds/moan02.mp3"
    cm "Mmmh, look at how much MY cock is spewing, it's flying just EVERYWHERE!"
    scene milfholdcum03 with dissolve
    stop channel2
    play channel2 "v031/boyorgasm02.mp3"
    cm "Sssooo, ssooo much CUM! I want to keep BLASTING! I NEED to, you hear me, [name]?"
    window hide
    with fastflash
    mc "I... RHAAAA!"
    scene milfholdcum04 with dissolve
    cm "Yes, hold your landlady's milkbags while she holds her HUGE convulsing MEGADONG!"
    window hide
    with hpunch
    cm "My cock is just on FULL BLAST, isn't it?"
    scene milfholdcum05 with dissolve
    cm "OOoh, I'm still got some MORE, more YUMMY CREAM to pump out of this monster!"
    window hide
    with fastflash
    mc "Oh God... AAAH!"
    scene milfholdcum06 with dissolve
    cm "And it's so tasty too? Do you want to taste some of my cream, [hero]?"
    window hide
    with vpunch
    mc "Ggggg..."
    cm "I seem to be have drained myself GOOD. * wink *"
    scene milfholdcum07 with dissolve
    stop channel2
    play sound "sounds/panting.mp3"
    cm "I came so MUCH, I guess I'm gonna need to ask Consuela to come and clean the gym again..."
    mc "* pant * I didn't even know we had a cleaning lady..."
    show screen calendar
    show screen statscreenicon
    show screen questscreenicon
    jump Main    

if (period == 0 and d10locday == 7) or (period == 1 and (d10locnight == 9 or d10locnight == 10)):
    scene gymmcpostcurlwidow01 with dissolve
    bw "Let's check on those big muscles of yours..."
    scene gymmcpostcurlwidow02 with dissolve
    bw "Mmmh, they sure look pretty damn HUGE. And HARD."
    mc "Yeah, ROCK-HARD even, for you Natasha!"
    scene gymmcpostcurlwidow03 with dissolve
    bw "Why don't you flex your abs for me? I'd like to check something..."
    mc "Alright! No problem, I'll turn them into a solid eight-pack armor plate for you!"
    scene gymmcpostcurlwidow04 with dissolve
    play sound "sounds/mangrunt01.mp3"
    mc "See? Nothing can..."
    scene gymmcpostcurlwidow05 with dissolve
    play sound "sounds/punch.mp3"
    bw "TAKE THAT!"
    mc "Didn't feel a thing!"
    if period == 0:
        scene gymmcpostcurlwidow06 with dissolve
    if period == 1:
        scene gymmcpostliftwidow06night with dissolve
    bw "Impressive I must say."
    mc "I told you, I'm just a solid wall of MUSCL... "
    scene gymmcpostcurlwidow07 with dissolve
    play sound "sounds/punch.mp3"
    bw "What about THERE? Not so confident anymore are we?"
    if age >= 20:
        mc "Ouch! My fragile monster cock!"
    if age >= 18 and age <= 19:
        mc "Ouch! My fragile teen monster cock!"
    scene gymmcpostcurlwidow08 with dissolve
    play sound "sounds/panting.mp3"
    bw "As I expected, your cock remains your weak point. It will ALWAYS BE men's weakest point. Enjoy your life as the INFERIOR sex, [name]!"
    mc "Damn... Ever since I'm grown bigger, that kind of shit just keeps happening to me..."
    if seengymwidowlevel02 == False:
        $ seengymwidowlevel02 = True
        menu:
            "I'm starting to really hate her constant cock-teasing and ball-busting... (+1 Super-Villain)":
                call Evil from _call_Evil_13
                pause
                pass
            "She's just trying to help me. In her own way. (+1 Super-Hero)":
                call Good from _call_Good_11
                pass        
    stop channel1
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label GymMCCurlNude:
play channel2 "sounds/effort01.mp3"
scene gymmccurlsoft01 with dissolve
show gymmccurlsoftvideo
window hide
pause
mc "Fuck yeah! I can feel the blood PUMPING..."
window hide
$ renpy.pause(1.0, hard='True')
show gymmccurlgettingvideo with fastdissolve
$ renpy.pause(1.7, hard='True')
scene gymmccurlerect
play sound "sounds/thud.mp3"
mc "...PUMPING EVERYWHERE! So fucking hard, gonna continue like this!"
window hide
show gymmccurlhardvideo
pause
if period == 1:
    stop channel2
    stop music
    play music "sounds/sexy07.mp3"
    scene mccurlpower01 with dissolve
    pg "I catch you AGAIN, [name]... Doing DIRTY things in the gym..."
    mc "Err, Powergirl?"
    scene mccurlpower02 with dissolve  
    play sound "sounds/wow.mp3"
    pg "And this time, your erection and your muscles truly are ENORMOUS!"
    mc "Err, it's just that..."
    pg "... You can't help youself getting HARD when you train your HUGE MUSCLES?"
    scene mccurlpower03 with dissolve    
    pg "But can you KEEP hard while I try and distract you?..."
    mc "Err, these dumbbells are quite heavy, like 10 tons each, Kara..."
    scene mccurlpower04 with dissolve    
    pg "Still, a REAL superhero shouldn't get distracted when performing his DUTIES... Let's find out if you're a REAL superhero, shall we?"
    jump GymCurlPowerNude
    
pause
mc "Fuck yeah! Chest-pressing over 20 TONS while sporting a giant hardon! A few more reps..."
window hide
pause
stop channel2
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymmcpost04b with dissolve
    mc "That was a nice workout... I feel like my biceps have GROWN even MORE..."
if d3rollgymworkout == 2:
    scene gymmcpost05b with dissolve
    mc "Grrr! I could scare away any enemy with THOSE muscles now!"
if d3rollgymworkout == 3:
    scene gymmcpost06b with dissolve
    if age >= 20:
        mc "Damn! Check those biceps, monster muscle STUD right there!"
    if age >= 18 and age <= 19:
        mc "Damn! Check those biceps, monster teenage muscle STUD right there!"
    mc "But no one around to admire them but me... * sigh *"
jump Main

label GymMCLiftNude:
show gymmcliftnudevideo with dissolve
window hide
pause
mc "Fuck yeah! This is getting me hard actually..."
show gymmclifterectingvideo
$ renpy.pause(1.9, hard='True')
hide gymmcliftnudevideo
show gymmcnudeerect
play sound "sounds/thud.mp3"
mc "Goddamn it, gonna continue like that!"
window hide
show gymmclifthardvideo
hide gymmclifterectingvideo
pause
stop channel2
if period == 1:
    stop music
    play music "sounds/sexy07.mp3"
    scene gymmcpowerprelift01 with dissolve
    pg "What are you doing [name]???"
    mc "Err, Powergirl?"
    scene gymmcpowerprelift02 with dissolve    
    pg "You thought you had the gym to yourself and that you could power-lift those weights NAKED and with a MASSIVE ERECTION?"
    mc "Yeah... I did actually."
    pg "Well let's see if you can cope under PRESSURE..."
    jump GymLiftPowerNude

window hide
pause
$ d3rollgymworkout = renpy.random.randint(1, 3)
if d3rollgymworkout == 1:
    scene gymmcpostlift01nude with dissolve
    mc "That was a nice workout... I feel like my muscles have GROWN a bit..."
if d3rollgymworkout == 2:
    scene gymmcpostlift02nude with dissolve
    mc "Grrr! I could scare away any Super-Villain with MY muscles now!"
if d3rollgymworkout == 3:
    scene gymmcpostlift03nude with dissolve
    if age >= 20:
        mc "Damn! Check those biceps, monster muscle stud right there!"
    if age >= 18 and age <= 19:
        mc "Damn! Check those biceps, monster teenage muscle stud right there!"
stop music
jump Main

label GymLiftPowerNude:
scene gymmcpower01 with dissolve
pg "Now try and continue your bench presses with the EXTRA pressure I apply on the barbell... I'm not using my SUPER-STRENGTH... yet."
call screen usepower("usestrength", "PowerliftNoStrength", "PowerliftStrength") with dissolve

label PowerliftStrength:
mc "Alright, I'll show you how STRONG I TRULY am then!"
scene gymmcpower01video with dissolve
pause
pg  "Impressive... Now let's try something more... DISTRACTING!"
scene gymmcpowerpost01 with dissolve
mc "Wh, what do you have in mind, Kara?"
pg "Well, you're DROOLING pre-cum all over your chest... I think you need some relief, don't you?"
mc "Yeah, I do! Fuck yeah!"
pg "Then try and KEEP that pose for as long as you can..."
play channel1 "sounds/wank.mp3"
scene gymmcpower02video with dissolve
pause
mc" Oh God, you're going to make me cum..."
pg "Not yet, [name], you haven't kept the barbell up long enough. You MUST concentrate..."
window hide
pause
mc "I don't think I can cont..."
scene gympowercum01 with dissolve
play sound "sounds/boyorgasm01.mp3"
stop channel1
mc "...AAAAH!"
window hide
with fastflash
pg "Oooh, too distracting for you, [name]?"
scene gympowercum02 with dissolve
mc "RHOOOA, you made me do it!"
window hide
with fastflash
pg "Did I? I was just gently caressing your giant shaft, nothing more..."
scene gympowercum03 with dissolve
pg "Like so... You cum THAT easily?"
window hide
with fastflash
mc "You're EMPTYING my balls, OOOH!"
scene gympowercum04 with dissolve
pg "But... I thought they had ENDLESS supplies of cum... Aren't you supposed to be a SUPER-STUD, [name]?"
window hide
with fastflash
mc "AAAH, STILL BLASTING!"
scene gympowercum05 with dissolve
stop sound
play sound "sounds/panting.mp3"
pg "Finally... You DID have a LOT of young cum that needed to be released didn't you?"
mc "Ggg..."
pg "Next time, try and FOCUS and keep that bar up a bit longer... * wink * I'm off to bed!"
mc "I guess... I'm off to bed too then. After I clean this MESS... Thanks for the handjob, Kara."
stop music
jump Main

label PowerliftNoStrength:
show gymmcpowershortvideo with dissolve
$ renpy.pause(.15, hard='True')
hide gymmcpowershortvideo
show gymmcpowerlose01
mc "Shit, I'm losing my grip..."
pg "Already? This is embarrassing..."
mc "It's not my fault, I didn't press the button in time, but I AM Super-Strong!"
scene gymmcpowerlose02 with dissolve
play sound "sounds/clank.mp3"
pg "Well, get your act together, [name]. Until then, you can take care of that blood flow to your cock on your own..."
mc "But... Kara..."
stop music
jump Main

label GymCurlPowerNude:
scene mccurlpower05 with dissolve    
pg "So if I grind my tight ass against your giant dangling boulders like this, you won't get distracted?"
play sound "sounds/effort01.mp3"
mc "Ggg... No... I'm still pumping... iron..."
scene mccurlpower06 with dissolve    
pg "What if I squeeze your balls like this with my knee? A TRUE superhero can ignore the pain."
play sound "sounds/boymoan02.mp3"
mc "I... don't feel... a thing... * puff * I... can keep on... going..."
scene mccurlpower07 with dissolve    
pg "But can a superhero ignore the warm sensation of his landlady's daughter's soft mouth on his cum factories?"
mc "Wh... what?"
scene mccurlpower08 with dissolve    
play sound "sounds/lick03.mp3"
mc "Oh God... Still going though, you won't stop  me from doing my reps, Kara!"
scene mccurlpower07 with dissolve    
pg "Maybe not yet... But what if I really get to work on your other sensitive testicle?"
window hide
show mccurlballsuckvideo with dissolve
play channel2 "sounds/boymoan.mp3"
play channel1 "sounds/lick01.ogg"
pause
pg " *gglll * Looks like you're about to get distracted, [name]..."
stop channel1
stop channel2
scene mccurlballcum01 with dissolve
play sound "sounds/boymoan03.mp3"
mc "Uuuh..."
window hide
with fastflash
pg "Mmh, that's right, you're spurting a little bit already. How naughty of you!"
scene mccurlballcum02 with dissolve
play sound "sounds/boymoan05.mp3"
pg "My ball-sucking was that good, hey? You couldn't help but spew big fat ropes of young spunk all over yourself!"
window hide
with hpunch
mc "Oh God, that was... too much..."
play sound "sounds/boymoan.mp3"
scene mccurlballcum03 with dissolve
pg "But you're still ssooo HARD! That was just a little premature ejaculation, you still have a LOT of pent-up baby sauce left over in those fat balls for your landlady's daughter, haven't you?"
scene mccurlballcum04 with dissolve
pg "I think I have an idea of what to do with this monstrous thing that just won't go down..."
mc "Wh... what are you doing?"
scene mccurlballcum05 with dissolve
pg "I've trapped your giant pole between my soft boobies, you have a problem with that?"
mc "Err... I guess not."
pg "Then keep going, curl those super-heavy dumbbells, do as many reps as you can before your dong can't take it anymore!"
play channel1 "sounds/boymoan02.mp3"
play channel2 "sounds/wetmassage.mp3"
scene gymbackgroundnight
show mccurltitslowvideo
with dissolve
pause
pg "Keep going [name], you're doing pretty good considering your predicament..."
call screen usepower("usesenses", "McCurlTitSlow", "McCurlTitSlowSensesPre") with dissolve

label McCurlTitSlow:
$ powertitfast = False
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
scene gymbackgroundnight
show mccurltitslowvideo
with fastdissolve
pg "You like it when my tits slowly rub against your fat shaft don't you? You're DROOLING pre-cum all over the place! Such a NAUGHTY boy!"
window hide
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
if powertitsenses == True:
    show nudeicon:
        xpos 50 ypos 500  
call screen mccurltitslow()
screen mccurltitslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitFast")
    if powertitsenses == True:
        button:
            xpos 50
            ypos 500
            xysize(100, 60)        
            action Jump ("McCurlTitSlowSenses")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEnd")

label McCurlTitFast:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
if powertitfast == False:
    pg "I want you to curl those 10 tons dumbbells FASTER! Show me how STRONG you are!"
    window hide
    $ powertitfast = True
scene gymbackgroundnight
show mccurltitfastvideo
with fastdissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
if powertitsenses == True:
    show nudeicon:
         xpos 1700 ypos 500    
call screen mccurltitfast()
screen mccurltitfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitSlow")
    if powertitsenses == True:
        button:
            xpos 1700
            ypos 500
            xysize(100, 60)        
            action Jump ("McCurlTitFastSenses")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEnd")

label McCurlTitSlowSensesPre:
hide mccurltitslowvideo
show mccurltitslowsensesvideo
with fastdissolve
label McCurlTitSlowSenses:
$ powertitsenses = True
$ powertitfast = False
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
scene gymbackgroundnight
show mccurltitslowsensesvideo
with fastdissolve
pg "You like it when my tits slowly rub against your fat shaft don't you? You're DROOLING pre-cum all over the place!"
window hide
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
if powertitsenses == True:
    show nonudeicon:
        xpos 50 ypos 500  
call screen mccurltitslowsenses()
screen mccurltitslowsenses():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitFastSenses")
    if powertitsenses == True:
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("McCurlTitSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEnd")

label McCurlTitFastSenses:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
if powertitfast == False:
    pg "I want you to curl those 10 tons dumbbells FASTER! Show me how STRONG you are!"
    window hide
    $ powertitfast = True
scene gymbackgroundnight
show mccurltitfastsensesvideo
with fastdissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
if powertitsenses == True:
    show nonudeicon:
         xpos 1700 ypos 500    
call screen mccurltitfastsenses()
screen mccurltitfastsenses():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitSlowSenses")
    if powertitsenses == True:
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("McCurlTitFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEnd")

label McCurlTitEnd:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
pg "Look at you, you're ready to burst aren't you? Your ENORMOUS fuckstick is convulsing between my soft pillows..."
mc "Uh... Aahh... Kara..."
stop channel1
scene mccurltitcum01 with dissolve
play sound "sounds/boymoan04.mp3"
mc "AAAAH!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
pg "There you go, [name]! Cum for your landlady's daughter!"
scene mccurltitcum02 with dissolve
play channel1 "sounds/boyorgasm01.mp3"
pg "Give me the BIGGEST cumshots you can and keep curling these MASSIVE weights!"
window hide
with fastflash
pg "Mmmh, my God, you really are EXPLODING aren't you?"
scene mccurltitcum03 with dissolve
pg "But you're not done... I can feel your spermtube ENLARGING between my tits..."
window hide
with hpunch
pg "You still want to BLAST away and give me MORE. Give ALL YOU HAVE to your teasing landlady's daughter!"
scene mccurltitcum04 with dissolve
pg "Look at you, you're CAKED in your own slimy spunk and you just won't let up."
window hide
with fastflash
pg "You just keep cumming and cumming, like a sperm hose at FULL BLAST!"
scene mccurltitcum05 with dissolve
pg "Maybe I should aim your GIANT spunk plumes closer to your face... So you can give yourself a bukkake facial!"
window hide
with fastflash
mc "UUUH, AAAH, it's landing right on my face, Kara!"
window hide
with hpunch
pg "That's right, but you love it don't you, you're STILL pumping that sweet young seed... Mmh, what a MONSTERLOAD you gave me! AND yourself! * giggles *"
scene mccurltitcum06 with dissolve
stop music
stop channel1
stop channel2
play sound "sounds/panting.mp3"
pg "Once again, Powergirl drained the POWER out of her mother's landboy! * giggles *"
mc "I... need to go to sleep."
pg "Yes, you do, you need to get your power back. For tomorrow. You might get drained AGAIN by your landlady's daughter! Goodnight, [name]!"
jump Main

label GymPower:
$ seengym = True
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
mc "Kara is about to lift a pretty heavy set of weights... Over 3 tons by my account. Let's watch."
scene gympowerliftvideo with dissolve
pause
mc "Damn, she's not letting up. That's already over 100 reps she's done."
scene gympowerliftpost01 with dissolve
pg "I'm almost done, [name]. If you wanted to use the bench press..."
mc "I'm good, Kara. Just watching your awesome Super-Strenth in action."
pg "Oh, you enjoy watching MUSCLE GIRLS, do you? Especially when it's your LANDLADY's DAUGHTER?"
mc "Yeah... You're so hot, Kara."
pg "Then let me do a few more reps for you..."
scene gympowerliftvideo with dissolve
pause
scene gympowerliftpost01 with dissolve
if period == 0:
    pg "That's it, I'm done for today. I DO feel like my muscles have GROWN afer this workout. What d'you reckon, [name]?"
if period == 1:
    pg "That's it, I'm done for tonight. I DO feel like my muscles have GROWN afer this workout. What d'you reckon, [name]?"
mc "Let's have a look then..."
if mclevel02 == False:
    scene gympowerliftpost02 with dissolve
    mc "Damn, you're SUPER-RIPPED!!!"
    pg "I feel like I could..."
    scene gympowerliftpost03 with dissolve
    pg "Lift you up like a rag doll!"
    mc "Hey, what are you doing!"
    if period == 0:
        scene gympowerliftpost04 with dissolve
    if period == 1:
        scene gympowerliftpost04night with dissolve
    pg "Just having a bit of fun with my (temporarily) ENHANCED MUSCLES!"
    mc "I'm NOT having fun, please let me down, Kara!"
    pg "I thought you were into MUSCLE GIRLS?"
    mc "Yes, but from AFAR, from FAR FAR AWAY!"
    scene gympowerliftpost05 with dissolve
    play sound "sounds/thud.mp3"
    pg "Fine, I'll let you down. I'll continue flexing my body in front of the mirror. And you can go FAR, FAR AWAY!"
    mc "I guess my bedroom qualifies..."
if mclevel02:
    if period == 0:
        scene gympowerliftpost06 with dissolve
    if period == 1:
        scene gympowerliftpost06night with dissolve
    pg "For sure, my biceps have grown after this heavy workout, can you tell?"
    mc "Yeah, not bad, but check my HUGE [age]yo muscles out..."
    if period == 0:
        scene gympowerliftpost07 with dissolve
    if period == 1:
        scene gympowerliftpost07night with dissolve
    pg "You're just showing off!"
    mc "Why shouldn't I? I'm just so fuckin' RIPPED!"
    if period == 0:
        scene gympowerliftpost08 with dissolve
    if period == 1:
        scene gympowerliftpost08night with dissolve
    pg "That's it, you've asked for it, [name]!"
    mc "Hey! What are you doing Kara?"
    if period == 0:
        scene gympowerliftpost09 with dissolve
    if period == 1:
        scene gympowerliftpost09night with dissolve
    pg "I'm showing you that you shouldn't try and outdo your landlady's daughter!"
    mc "Please Kara, let me down! I must be too heavy for you anyway."
    if period == 0:
        scene gympowerliftpost10:
            subpixel True
            xpos 0.0
            linear 3.0 xpos -0.04
        with dissolve
    if period == 1:
        scene gympowerliftpost10night:
            subpixel True
            xpos 0.0
            linear 3.0 xpos -0.04
        with dissolve
    pg "Oh, you think so? I just need to FLEX my abs and I could keep you suspended like that for HOURS..."
    mc "Alright, alright, but it's getting late, so we don't have time for that!"
    scene gympowerliftpost11 with dissolve
    pg "Fine [name], I'll let you down..."
    scene gympowerliftpost12 with dissolve
    play sound "sounds/punch.mp3"
    mc "Hey, I'm not a bag of potatoes!"
    pg "I don't need you anymore anyway. My muscles are already SO STRONG!"
    if period == 0:
        scene gympowerliftpost13 with dissolve
    if period == 1:
        scene gympowerliftpost13night with dissolve
    pg "I'll just continue flexing my body in front of the mirror. While YOU go back to your room and think about how you should show more RESPECT for your landlady's daughter!"
    mc "I thought my new muscles would change things around here but no... * sigh *."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label GymMILFEndLevel1:
$ seenmilfgymendlevel01 = True
scene gymmilfnew01 with dissolve
mc "There's Captain MILF doing some squats. Let's get closer..."
scene gymmilfnew02 with dissolve
cm "Well hello there, sweetie pie!"
mc "Man, that outfit is like ssooo 80s."
cm "Yes, it is very modern isn't it? I love this avant-garde style! Don't you, [name]?"
mc "Err... Yeah I guess. When YOU wear it that is."
cm "Hum, I don't know if what you said was sweet or had some kind of sexual connotation..."
cm "Anyway, you can watch your landlady squat over 3 tons of Krypton steel weights if you want."
mc "I do want."
show gymmilfsquatvideo with dissolve

show nexticon:
    xpos 1750 ypos 1020
call screen GymMILFsquat()
screen GymMILFsquat():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd")

label GymMILFSquatEnd:
if mcsenses >= 1:
    call screen usepower("usesenses", "GymMILFSquatEnd02", "GymMILFNudePreSquat") with dissolve
if mcsenses == 0:
    jump GymMILFSquatEnd02

label GymMILFNudePreSquat:
hide nexticon
mc "Let's focus my Super-Senses on her Super-Tits..."
window hide

label GymMILFNudeSquat:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedfastvideo behind gymmilfsquatnakedslowvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedslowvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020
show slower:
     xpos 50 ypos 500     
call screen GymMILFnudesquat()
screen GymMILFnudesquat():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquatSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02")

label GymMILFNudeSquatSlow:
hide closer
hide nexticon
hide sceneicon
hide slower
show gymmilfsquatnakedslowvideo behind gymmilfsquatnakedfastvideo
$ renpy.pause(1.0, hard=True)
hide gymmilfsquatnakedfastvideo
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen GymMILFnudesquatslow()
screen GymMILFnudesquatslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GymMILFNudeSquat")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GymMILFSquatEnd02")

label GymMILFSquatEnd02:
scene gymmilfnew03 with dissolve
cm "And now, lifted high above my head!"
if mcstrength >= 2:
    mc "Not bad, I can do it too though, it's easy with Super-Strength level 2."
if mcstrength == 1:
    mc "Not bad, but I can do it too even with just Super-Strength level 1."
scene gymmilfnew04:
    zoom 0.5 xoffset 0 yoffset 0
with dissolve
cm "But can you do it with one hand while FLEXING your biceps?"
mc "Damn, Carol! Your biceps... They're BULGING!..."
scene gymmilfnew04:
    subpixel True
    zoom 0.5 xoffset 0 yoffset 0
    linear 5.0 zoom 1.0 xoffset -600 yoffset -600
$ renpy.pause(4.0, hard='True')
cm "Maybe I should turn round to prove to you how FIT your League Captain is..."
mc "Indeed you should. I need convincing right NOW!"
scene gymmilfnew05:
    ypos 0.0
    ease 4.0 xpos -0.02 ypos -0.99
$ renpy.pause(4.0, hard='True')
mc "* What a tight ass! Maybe I should get h... *"
cm "Don't get any funny ideas, [name]. You wouldn't want to mess with your landlady while she's in this PUMPED-UP state!"
scene gymmilfnew06 with dissolve
cm "Imagine the DAMAGE those iron-hard abs could cause on some unsuspecting victim..."
mc "By victim you're talking about ME and my COCK?"
scene gymmilfnew07 with dissolve
cm "Maybe I am... Let's see how YOU fare in the muscle department now that your superpowers have improved a bit... Flex those guns for me, sweetie pie!"
scene gymmilfnew08 with dissolve
mc "Alright, I've been practising my routine after watching a movie with a new young Austrian muscled actor in it. It was a rubbish B-flick but I learnt a few things about..."
scene gymmilfnew09 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "...MUSCLE FLEXING!"
cm "Mmmh, they really are getting VERY BIG, [name]! Captain MILF has a big announcement for you, come closer my dear landboy..."
scene gymmilfnew10 with dissolve
cm" It's time for you to reach Super-Hero LEVEL 2. My machine is ready."
mc "ALRIGHT! Can we do it, like, right now?"
cm "Then let me change into my engineering outfit and meet me in the radiation room. You remember where it is, don't you?"
mc "Err, yeah, I guess I do even though it seems like such a long time ago, Carol."
jump Level02lab

label WidowWrestlingLevel02:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene wrestlingnew01 with fade
if lostwidowwrestling == False:
    mc "* This time, I'm wearing my re-inforced kevlar thong. I won't let her kick me in the nuts! *"
if lostwidowwrestling:
    mc "* I had my re-inforced kevlar thong re-worked! This time, it will even resist the pressure from my Super-Hard cock*"
scene wrestlingnew02 with dissolve
if lostwidowwrestling == False:
    bw "I see you're wearing a new outfit... Is that because I scare you?"
    mc "No! It's just... for convenience."
if lostwidowwrestling:
    bw "Still wearing your kevlar thong. As if it would make any difference to the outcome of the fight..."
    mc "At laest, you can't CHEAT by kicking me in the nuts!"
play music "sounds/sexy04.mp3"
scene wrestlingnew03 with dissolve
if lostwidowwrestling == False:
    bw "I'm wearing a new outfit too. It's all the latest rage in Cockham. Do you like it?"
if lostwidowwrestling:
    bw "Well, I'm wearing the same SEXY outfit I did last time... Do you still like it?"
mc "I... I suppose so..."
bw "You SUPPOSE so? Not much confidence there."
scene wrestlingnew04 with dissolve
bw "Let me stretch a bit before our FIGHT..."
mc "Err, alright. But then, we FIGHT!"
scene wrestlingnew05 with dissolve
bw "Sure. We fight. And I beat the crap out of you. As usual."
mc "Not THIS time, Natasha!"
scene wrestlingnew06:
    zoom 1.0 xoffset -40 yoffset -1800    
show wrestlingnew06 at widowgymfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
bw "Oooh! Well then, I'd better REALLY stretch, shouldn't I?"
scene wrestlingnew07:
    zoom 1.0 xoffset 0 yoffset 0    
show wrestlingnew07 at widowgymfulldown
with dissolve
$ renpy.pause(6.0, hard='True')    
bw "I hope you're not LOSING YOUR CONCENTRATION by looking at my fine ass, [hero]?"
mc "Err... Not at all."
scene wrestlingnew08 with dissolve
bw "What about my nice round puppies? Can you ignore such sumptuous funbags?"
mc "I... Y...Yes, I CAN!"
scene wrestlingnew09 with dissolve
bw "Even when I SQUEEZE them together like this?"
mc "* Damn, I might get a HARDON! Need...to....concentrate! *"
if mcresistance >= 1:
    call screen usepower("useresistance", "WidowGymNewNoResistance", "WidowGymNewResistance") with dissolve

label WidowGymNewNoResistance:
scene wrestlingnew10 with dissolve
mc "* Oh God, my enlarging dong has no space to grow... It hurts! But I can't chicken out of this fight now! *"
  
label WidowGymNewResistance:
stop music
play music "v03/fightmusic.mp3"
if usedresistancewidowgym == False:
    $ usedresistance += 1
    $ usedresistancewidowgym = True
scene wrestlingnew11 with dissolve
mc "Your sexual teasing won't help you win this time! I'm ready to fight whenever YOU are!"
scene wrestlingnew12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
bw "I see. You have toughened up a bit. You might be a worthy opponent for once!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestlingnew13 with dissolve
play sound "sounds/whoosh.mp3"
mc "* Damn! She moved away too fast *"
bw "You're looking for me? Look up then!"
scene wrestlingnew14 with dissolve
mc "* Where did she go now??? *"
bw "Behind you!"
scene wrestlingnew15 with dissolve
play sound "sounds/punch.mp3"
bw "Right on your back now!"
mc "What the???"
scene wrestlingnew16 with dissolve
bw "And now for the final..."
scene wrestlingnew17 with dissolve
play sound "sounds/punch.mp3"
mc "NOT YET!"
scene wrestlingnew18 with dissolve
bw "Hey!!!"
mc "You're taking flying lessons, Natasha? Be careful not to CRASH!"
scene wrestlingnew19 with dissolve
play sound "sounds/thud.mp3"
bw "Don't you worry about me. The Black Widow always lands on her two feet. Like this."
scene wrestlingnew20 with dissolve
play sound "sounds/punch.mp3"
bw "Let me finish where I left off!"
scene wrestlingnew21 with dissolve
play sound "sounds/mangrunt01.mp3"
bw "You're trying to escape from the Black Widow's grip, [hero]? Wishful thinking!"
mc "I'm not yielding, I know I can do it! I'll NEVER yield!"
scene wrestlingnew22 with dissolve
play sound "sounds/wank.mp3"
bw "What if I squeezed your fat balls a little? Would that change your mind?"
mc "NO-O-O-O! I mean, YES, my mind has totally CHANGED! I YIELD!"
bw "I thought so... Men are just ssoo attached to their little jewels, aren't they?"
mc "Please stop fondling them, I'm getting..."
scene wrestlingnew23 with dissolve
play sound "v041/metalbreak.mp3"
mc "...HARD! AAAH, it HURTS!"
scene wrestlingnew24 with dissolve
stop music
play music "sounds/sexy04.mp3"
if age >= 20:
    bw "Ooooh! Look what decided to join the party? A giant rock-hard dong!"
if age >= 18 and age <= 19:
    bw "Ooooh! Look what decided to join the party? A giant rock-hard teenage dong!"
scene wrestlingnew25 with dissolve
play sound "sounds/boymoan.mp3"
bw "It seems to be awfully HORNY! Look at all that cum splatter flying everywhere when I slightly tug on it!"
mc "Gggg..."
scene wrestlingnew26 with dissolve
bw "And now it's just LEAKING pre-spunk all the way down the trembling shaft... It must be ACHING for release, don't you think?"
mc "Y...YES, LET ME CUM!"
bw "Where would be the enjoyment in that?"
scene wrestlingnew27 with dissolve
play sound "sounds/boymoan02.mp3"
if age >= 20:
    bw "It's much more fun to watch that horny cock trying to spew its load..."
if age >= 18 and age <= 19:
    bw "It's much more fun to watch that horny teen cock trying to spew its load..."
scene wrestlingnew28 with dissolve
play sound "sounds/boyorgasm01.mp3"
bw "...but just not getting there because my hand is pressing so TIGHTLY against its spermtube..."
mc "Uuuuh... You're TEASING me so much!"
scene wrestlingnew29  with dissolve
play sound "sounds/boymoan03.mp3"
bw "But you LIKE to be teased. I can tell. That young horsedick of yours is just so HARD!"
window hide
with fastflash
play sound "sounds/panting.mp3"
mc "Aaah..."
bw "It doesn't look like you can hold off much longer. Your balls are getting BLOATED!"
scene wrestlingnew30 with dissolve
play sound "v031/boyorgasm02.mp3"
mc "I can't... I... NEED TO COME!"
bw "Sure, we all have \"needs\". But we don't always get what we want, now do we? Especially after LOSING a fight against the Black Widow!"
window hide
with fastflash
mc "Please, I beg you, let me RELIEVE MYSELF!"
scene wrestlingnew31 with dissolve
play sound "sounds/boymoan02.mp3"
if age >= 20:
    bw "Why would I do that when I'm having so much FUN? Watching your great big cum-cannon contorting itself and {i}trying{/i} to let loose HUGE WADS OF PENT-UP CUM?"
if age >= 18 and age <= 19:
    bw "Why would I do that when I'm having so much FUN? Watching your great big teenage cum-cannon contorting itself and {i}trying{/i} to let loose HUGE WADS OF PENT-UP CUM?"
window hide
with fastflash
mc "I'll do anything for you if you let my balls unload!"
scene wrestlingnew32 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Anything? First, I want you to RECOGNIZE the Black Widow's SUPERIOR skills in Super-Combat..."
mc "I do, I do! You're the best at Super-Combat! Nobody can beat you!"
bw "Then, I want you to..."
scene wrestlingnew33 with dissolve
play sound "sounds/boymoan05.mp3"
bw "...BLAST THE BIGGEST LOAD OF SPUNK EVER!"
window hide
with hpunch
mc "AAAAH!"
scene wrestlingnew34 with dissolve
play sound "sounds/boymoan03.mp3"
bw "And..."
scene wrestlingnew35 with dissolve
play sound "sounds/boymoan05.mp3"
bw "...AGAIN! Give me all that sweet young cream!"
window hide
with vpunch
play sound "sounds/boyorgasm01.mp3"
mc "UUUH! TOO STRONG!"
scene wrestlingnew36 with dissolve
bw "Not too strong for the Black Widow's mouth! Feed me your seed!"
window hide 
with fastflash
mc "Oh God!"
scene wrestlingnew37 with dissolve
play sound "sounds/lick02.mp3"
bw "* swallow * Yeah, so tasty..."
window hide 
with fastflash
bw "KEEP CUMMING FOR ME, I'm not DONE with you!"
scene wrestlingnew38 with dissolve
play sound "sounds/blow01.mp3"
mc "You're draining me, AAAH!"
window hide
with hpunch
bw " * slurp * Mmmggg..."
scene wrestlingnew39 with dissolve
play sound "sounds/panting.mp3"
mc "UUUH, my balls hurt so much..."
bw "That's the price you pay for LOSING to me, [name]..."
scene wrestlingnew40 with dissolve
bw "But here's your reward for being a good boy and cumming SO MUCH for the Black Widow..."
play sound "sounds/lick03.mp3"
bw "Your own tasty SPUNK!"
mc "Gggg..."
bw "Now off you go. Don't ever think you can BEAT the Black Widow in SUPER-COMBAT again!"
$ lostwidowwrestling = True
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop music
jump Main