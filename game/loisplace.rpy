label LoisFlat:
stop music
if seenloisflat:
    if mclevel02:
        jump LoisBedroom02
    jump LoisBedroom
if seenloisflat == False:
    $ seenloisflat  = True
    play music "sounds/nightsounds.mp3"
    scene loisflatentrance01 with fade
    mc "Ah, this is the address..."
    stop music
    scene loisflatentrance02 with dissolve    
    play sound "sounds/doorbell.mp3"
    mc "I hope she's in and that I didn't come for nothing."    
    if mclevel02 == False:
        scene loisflatentrance03 with dissolve
        lp "[hero], what a nice surprise... Come in quick, I don't want my nosey neighbors to see you standing in front of my door... I'll take you to my DEN. * wink *"
        jump LoisBedroom
    if mclevel02:
        jump LoisBedroom02

label LoisBedroom:
stop channel1
play channel1 "sounds/sexy04.mp3"
scene loisbedroom01 with dissolve
if loistoldbedroom:
    lp "So, what are you into for tonight's BDSM entertainment? I need to feel some PAIN. Lots of it."
if loistoldbedroom == False:
    lp "I hope you're into BDSM, cos I love to play SUBMISSIVE!"
    mc "Interesting..."
    show loisbedroom02 with fastdissolve
    lp "I'm letting you choose. The restraining rack or the bondage sofa?"
call screen loisbedroom()
screen loisbedroom():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action Jump ("LoisFlatLeave")
    imagebutton:
        focus_mask True
        idle "v02/loisrestraintidle.png"
        hover "v02/loisrestrainthover.png"
        action Jump ("LoisRestraint")
    imagebutton:
        focus_mask True
        idle "v02/loissofaidle.png"
        hover "v02/loissofahover.png"
        action Jump ("LoisSofa")
    
label LoisFlatLeave:
mc "You know what, I think I made a big mistake coming here tonight. I need to leave... And fight SEX CRIME."
hide loisbedroom02
show loisbedroom03
with fastdissolve
lp "What? But we were about to engage in SEX CRIME! You're LAME!"
jump Main

label LoisRestraint:
mc "Get your butt in the restraining rack, Lois."
lp "Ooh, that's a really PAINFUL position for me. Ideal for abusing my body from both ends..."
scene loisrack01 with dissolve
lp "I'm ready. I'm tied up like a hog. I am at your MERCY, [hero]. What will you do to poor little me?"
scene loisrack02 with dissolve
mc "Let me check that you're really well settled in there first. Yeah, that filthy butt is sticking out, begging to be PUNISHED!"
lp "Yes, it is. I've been so naughty..."
menu:
    "Slap her ass with your hand":
        jump LoisSlapHand
    "Slap her ass with your cock":
        jump LoisSlapCock
label LoisSlapHand:
scene loisrack03 with dissolve
mc "A naughty girl needs to have her ass SLAPPED!"
lp "You're so strong, it's going to HURT a LOT!"
play sound "sounds/slap.mp3"
scene loisrack04 with dissolve
mc "Take that, you filthy slut!"
scene loisrack03 with dissolve
lp "AAH! MORE! MORE please! I deserve it!"
window hide
play music [ "sounds/slap.mp3", "<silence .7>" ]
scene loisrackhand
pause
stop music
jump LoisRackEnd

label LoisSlapCock:
scene loisrack05 with dissolve
mc "A filthy girl like you needs to have her ass SLAPPED! By a HARD COCK!"
lp "Your giant shaft is so HEAVY, it's going to HURT a LOT!"
scene loisrack06 with dissolve
play sound "sounds/thud.mp3"
mc "Take that, you filthy slut!"
scene loisrack05 with dissolve
lp "AAH! MORE! MORE please! I deserve it!"
window hide
play music [ "sounds/thud.mp3", "<silence .8>"]
scene loisrackcock
pause
stop music

label LoisRackEnd:
scene loisrack07 with dissolve
lp "My poor buttcheeks have been battered into submission by your POWERFUL blows... I feel so dirty and cheap. But not ENOUGH!"
mc "I see. Then, I'll use your throat as my CUMDUMP!"
lp "Oh, this is going to be so HUMILIATING for me!"
scene loispresuck00 with dissolve
if age >= 20:
    lp "It's so BIG. you're such a fucking BULLSTUD!"
if age >= 18 and age <= 19:
    lp "It's so BIG. you're such a fucking TEEN BULLSTUD!"
mc "You got that right, Lois!"
scene loispresuck01 with dissolve
play sound "sounds/lick02.mp3"
lp "Call me \"cumdump\", that's what I am. YOUR cumdump. Fuck my mouth with your monster schlong!"
scene loispresuck02 with dissolve
play sound "sounds/boymoan02.mp3"
mc "You want that dick, don't you, cumdump? Here it comes!"
stop sound
window hide
label LoisDeepThroatSlow: 
hide cum
hide faster
hide slower
show loissuckslowvideo behind loissuckfastvideo
pause 1.0
play music "sounds/blow02.mp3"
hide loissuckfastvideo with dissolve
if loissucktold01 == False:
    mc "Slowly to begin with... Yeah, just like that..."
    window hide
    $ loissucktold01 = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen loissuckslow()
screen loissuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDeepThroatFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDeepThroatEnd")

label LoisDeepThroatFast:
show loissuckfastvideo behind loissuckslowvideo
hide cum
hide faster
hide slower
mc "That throat is so warm, I think I'm going to face-fuck you FASTER, whether you're ready or not!"
lp "* gllur *"
stop music
play music "sounds/blow01.mp3"
hide loissuckslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen loissuckfast()
screen loissuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDeepThroatSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDeepThroatEnd")

label LoisDeepThroatEnd:
hide cum
hide slower
hide faster
mc "That's it, cumdump, I'm going to..."
stop music
play music "sounds/splooge02.mp3"
scene loissuckcum01 with dissolve
mc "...FUCKING BLOW!!!"
window hide
with fastflash
mc "AAAH!"
scene loissuckcum02 with dissolve
mc "I'm not done yet, there's plenty more where that came..."
window hide
with fastflash
mc "...from, RHOOAAAAR!"
scene loissuckcum03 with dissolve
lp " * gargle * gllll..."
mc "What was that, cumdump? Take those more shots and shut up!"
window hide
with fastflash
mc "And now I'm gonna cover your face in my seed!"
stop music
scene loissuckcum04 with dissolve
play sound "sounds/boymoan03.mp3"
lp "Oooh, you're STILL cumming?"
window hide
with fastflash
mc "FUCK YEAH, YOU BET, AAAH!"
scene loissuckcum05 with dissolve
play sound "sounds/moan03.mp3"
lp "You're blasting like a stallion on fire!"
window hide
with fastflash
mc "OOOH, DAMN RIGHT! Take those last half-dozen shots then!"
scene loissuckcum06 with dissolve
play sound "sounds/panting.mp3"
mc "You did well. Swallowing ounces of my ball-batter like that."
lp "I'm... so glad to have served you well, Master."  
mc "That was a nice little appetizer, don't you agree?"
lp "There's... cum everywhere... * cough *"
mc "Nonsense, it was just a small preliminary load."
scene loissuckcum07 with dissolve
lp "Wh... What? I can't... continue, [name], I need to recover after this brutal skull-fuck, I beg you! Another time, not TONIGHT!"
menu:
    "I didn't ask for your worthless opinion and I'm still HORNY! (+1 Super-Villain if not already obtained)" if loisevil == False:
        $ loisevil = True
        call Evil
        jump LoisPostScene
    "Alright, hopefully next time you'll have more stamina. (no change)":
        $ loisgood = True
        lp "I PROMISE! Next time, I'll be ready for MORE for YOU."
        mc "Then I'll untie you. This time."
        jump LoisBedroomEnd

label LoisSofa:
mc "I'll tie you up like a hog in the bondage sofa, Lois."
lp "But... Master, I'll be at your COMPLETE MERCY!"
scene loisbedroom01 with dissolve
mc "Yeah, I know, now OBEY SLAVE!"
lp "YES MASTER!"
scene loissofa01 with dissolve
mc "Interesting sofa. I think I'll just sit down and have a glass of soda. Pepsi cos it's super-popular in the 70s for some reason."
scene loissofa02 with dissolve
mc "How are you doing my little bound slave?"
lp "I... I can't move."
scene loissofa03 with dissolve
mc "Oh well, that means I can fondle your tits and you can't do anything about it, right?"
lp "Y... Yes. I'm completely helpless."
scene loissofa04 with dissolve
mc "Good. Now let's have a look at this pussy. Oooh, it feels all wet. You're horny, slave?"
lp "I'm... ready to serve you. In ANY which way you desire."
mc "Good. Then I'll untie you, but keep your wrists bound."
scene loissofa05 with dissolve
lp "Wh... What should I do, Master?"
mc "I think you know perfectly well. Grind you ass on my ROCKHARD shaft and you'd better MAKE ME CUM or you will face SEVERE punishment!"
stop sound
window hide
label LoisSofaSlow:  
hide cum
hide faster
hide slower
show loissofaslowvideo behind loissofafastvideo
pause 1.0
play channel2 "sounds/boymoan02.mp3"
hide loissofafastvideo with dissolve
if loissofatold01 == False:
    mc "Slowly to begin with... Yeah, just like that..."
    lp "It's so LONG and THICK, Master!"
    window hide
    $ loissofatold01 = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
     
call screen loissofaslow()
screen loissofaslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSofaFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSofaEnd")

label LoisSofaFast:
hide cum
hide slower
hide faster
show loissofafastvideo behind loissofaslowvideo
mc "Now move those glutes FASTER!"
lp "Of course, my ass is here to make you EXPLODE with desire!"
play sound "sounds/moan02.mp3"
window hide
hide loissofaslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen loissofafast()
screen loissofafast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSofaSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSofaEnd")

label LoisSofaEnd:
hide cum
hide slower
hide faster
mc "That's it, slave, I'm going to..."
stop channel2
scene loissofacum01 with dissolve
hide loissofaslowvideo
hide loissofafastvideo
mc "...FUCKING BLOW!!!"
play sound "sounds/boymoan03.mp3"
window hide
with fastflash
mc "AAAH!"
scene loissofacum02 with dissolve
mc "I'm not done yet, there's plenty more where that came..."
window hide
with fastflash
mc "...from, RHOOAAAAR!"
scene loissofacum03 with dissolve
play sound "sounds/moan03.mp3"
lp "You're such a fucking STALLION, Master!"
window hide
with fastflash
lp "AAAH, you come MORE than 100 men put together!"
scene loissofacum04 with dissolve
mc "I'm gonna CLAIM you with my seed! RHAAA!"
window hide
with fastflash
lp "I belong to YOU, Master, ONLY YOU!"
scene loissofacum05 with dissolve
play sound "sounds/moan01.mp3"
lp "Are you... finished Master? I'm totally CAKED in your warm boycum..."
mc "Yeah, for now. Turn round and suck the afterdregs..."
scene loissofacum06 with dissolve
play sound "sounds/lick03.mp3"
if age >= 20:
    lp "Did I do good Master? Did I satiate your monster cum-cannon well enough?"
if age >= 18 and age <= 19:
    lp "Did I do good Master? Did I satiate your monster teenage cum-cannon well enough?"
mc "I am reasonably satisfied."
jump LoisBedroomEnd 

label LoisPostScene:
mc "Now I want you to change into something more provocative, befitting of a little cock-slut like you. I want to see some TITTIES, you hear me? And call me MASTER!"
lp "Y...Yes, Master..."
scene loisshame00 with fade
play music "sounds/sexy04.mp3"
lp "Is this better Master?"
mc "Yeah, come forward, my little cock-slave..."
scene loisshame01a with dissolve
mc "Don't cover your tits! I WANT to see them!"
lp "Sorry, Master..."
mc "Get on your knees!"
scene loisshame01b with dissolve
lp "I am at your disposal, Master. Like a good slave."
mc "Good, you're getting the hang of this."
scene loisshame02 with dissolve
mc "Now, let me think... You see my cock?"
lp "Yes, Master. It's hard again. And huge."
scene loisshame03 with dissolve
mc "That's right. It's HARD and HUGE. You want it, don't you, little cock-slut?"
if age >= 20:
    lp "Y... Yes, Master. I am entirely devoted to your monster phallus."
if age >= 18 and age <= 19:
    lp "Y... Yes, Master. I am entirely devoted to your monster teenage phallus."
mc "Then come and worship it!"
scene loisshame04 with dissolve
play sound "sounds/lick03.mp3"
mc "I'm drooling pre-cum all over your face. I'm marking my TERRITORY. You know why?"
lp "Because I'm your cock-slut?"
scene loisshame05 with dissolve
mc "And ONLY MY cock-slut!"
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
mc "Now remember this!"
scene loisshame05 with dissolve
lp "Yes Master!"
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
mc "I think you need a few more cock-slaps to your face to really understand what this means..."
scene loisshame05 with dissolve
$ renpy.pause(.5, hard='True')
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.2, hard='True')
scene loisshame05 with dissolve
$ renpy.pause(.5, hard='True')
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.2, hard='True')
scene loisshame05 with dissolve
$ renpy.pause(.5, hard='True')
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.2, hard='True')
scene loisshame05 with dissolve
mc "Because what it means is that I don't want you to see Clarke Kunt again! EVER!"
scene loisshame06 with fastdissolve
play sound "sounds/thud.mp3"
mc "Did you get that?"
scene loisshame05 with dissolve
lp "Y... Yes Master..."
mc "And to seal the contract, I'm signing with my CUM!"
scene loisshame07 with dissolve
play sound "sounds/boymoan02.mp3"
mc "AAAH, it's coming..."
scene loisshame08 with dissolve
play sound "sounds/boymoan05.mp3"
mc "FUCK, RHAAA!!!"
window hide
with fastflash
play sound "sounds/boymoan03.mp3"
lp "I belong to you, Master!"
scene loisshame09 with dissolve
play sound "sounds/boymoan.mp3"
lp "You've caked me in your scalding spunk again, Master..."
mc "I sure did. And now I'm off to bed in MY bed. While you must remain here covered in my cream for the WHOLE night, you hear me?"
lp "Yes, Master. I will obey."
jump Main

label LoisBedroomEnd:
stop channel1
scene loisbedroom01 
show loisbedroomend
with fade
lp "Come back anytime you want, MASTER. And please don't tell Clarke Kunt about my... dirty fetish."
mc "I'll think about it..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label LoisBedroom02:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy04.mp3"
$ seenloisdildo = True
scene loisbedroomlevel02a with dissolve
if loisharem:
    lp "I'm wearing my slave outfit for you, Master. Now that I am officially in your harem..."
    mc "I applaud  my slave's efforts at pleasing her Master."
    scene loisbedroomlevel02b with dissolve
    lp "I designed the nipple pasties myself especially for YOU, Master."
    scene loisbedroomlevel02c with dissolve
    lp "And I also bought this HUGE dildo to prime my cavities for YOUR Super-Cock, Master."
    mc "Good, cos tonight I feel like possibly ramming my level 02 Super-Cock inside your pussy!"
    lp "Oooh, anything to please you, Master."

if loisharem == False:
    lp "Do you like my new outfit?"
    mc "Oh yeah!"
    scene loisbedroomlevel02b with dissolve
    lp "I designed the nipple pasties myself especially for YOU, Master."
    mc "That's a nice touch. I am moved."
    scene loisbedroomlevel02c with dissolve
    lp "And I also bought this HUGE dildo to prime my cavities for YOUR Super-Cock, Master."
    mc "Now, I am emotionally overwhelmed. Almost to tears at such slavish devotion."
    lp "Please sit down on the sofa Master, and I will demonstrate to you how I will dilate my fuckholes with it."
window hide
show loisbedroombackground01 blurred:
    zoom 1.1 xoffset -100 yoffset 0
show loispng01:
    zoom 1.0 xoffset -50 yoffset 0 
with dissolve
lp "Let's have a more... intimate lighting atmosphere."
window hide
show loisbedroombackground01 blurred at widowpoolbackzoombackground
show loispng01 at widowpoolfullup
with dissolve
$ renpy.pause(4.0, hard='True')  
mc "Yeah, it's so intimate it's just like I'm there."
window hide
hide loispng01
show loisbedroombackground01 blurred:
    zoom 1.1 xoffset -100 yoffset -1080
show loispng02:
    zoom 1.0 xoffset -50 yoffset -1080
with dissolve
mc "Oooh, nice backview."
window hide
show loisbedroombackground01 blurred at poolbackgroundpowerup
show loispng02 at powerfullup
with dissolve
$ renpy.pause(4.0, hard='True')  
mc "Your Master is getting hard, slave!"
scene loisdildo01 with dissolve
lp "I'm sure he is, he's such an ALPHA-STUD. But your slave needs to make sure she'll be ready for when you PUNISH her with your MASSIVE pussy-wrecker."
scene loisdildo02 with dissolve
lp "Watch your sex slave take her 12-inch huge dildo up her ASS for you, Master!"
scene loisdildo03 with dissolve
play sound "sounds/moan05.mp3"
mc "You're going to need to make more than just a few inches, slave!"
lp "Ughh... Of... course, Master..."

label LoisDildoFuckSlow:
$ loisdildofuckfast = False
window hide
show loisdildoslowvideo behind loisdildofastvideo
show loisdildoslowvideo behind loisdildofrontslowvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide loisdildofastvideo
hide loisdildofrontslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if loisdildofuckslow == False:
    $ loisdildofuckslow = True
    mc "Nice, take it deep, Lois, cos my dong is even bigger than that dildo."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen loisdildofuckslow()
screen loisdildofuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckPOVSlow")

label LoisDildoFuckFast:
$ loisdildofuckslow = False
window hide
show loisdildofastvideo behind loisdildoslowvideo
show loisdildofastvideo behind loisdildofrontfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loisdildofrontfastvideo
hide loisdildoslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if loisdildofuckfast == False:
    $ loisdildofuckfast = True    
    mc "You're doing good, take it HARD and FAST, tht's the way I like to anally POUND my women!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen loisdildofuckfast()
screen loisdildofuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckPOVFast")


label LoisDildoFuckPOVSlow:
$ loisdildofuckfast = False
window hide
show loisdildofrontslowvideo behind loisdildoslowvideo
show loisdildofrontslowvideo behind loisdildofrontfastvideo
pause 1.0
stop channel1
play channel1 "sounds/moan02.mp3"
hide loisdildofrontfastvideo
hide loisdildoslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if loisdildofuckslow == False:
    $ loisdildofuckslow = True
    mc "Nice, take it deep, Lois, cos my dong is even bigger than that dildo."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loisdildofrontfuckslow()
screen loisdildofrontfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckSlow")

label LoisDildoFuckPOVFast:
$ loisdildofuckslow = False
window hide
show loisdildofrontfastvideo behind loisdildofastvideo
show loisdildofrontfastvideo behind loisdildofrontslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loisdildofastvideo
hide loisdildofrontslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
if loisdildofuckfast == False:
    $ loisdildofuckfast = True    
    mc "You're doing good, take it HARD and FAST, tht's the way I like to anally POUND my women!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loisdildofrontfuckfast()
screen loisdildofrontfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckFast")

label LoisDildoFuckEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide front
mc "I'm going to cum and show you how superior your Master's loads are to anyone else, SLAVE!"
lp "Yes Master, cum with me, drown me in your sweet [age]yo spunk!"
scene loisdildo04 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "Here it CU-UUU-MMMS!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
lp "I'm cumming too Master, AAAH!"
scene loisdildo05 with dissolve
mc "Now take those shots, feel the POWER of my SUPER-SPUNK!"
window hide
with fastflash
lp "My God, Master, your sperm plumes are sssooo MASSIVE and POWERFUL! AAAH!"
scene loisdildo06 with dissolve
mc "I'm ain't done yet, RHAAA!"
window hide
with fastflash
if age >= 20:
    lp "You're BLASTING at FULL POWER and re-painting my bedroom in your viscous virile cum!"
if age >= 18 and age <= 19:
    lp "You're BLASTING at FULL POWER and re-painting my bedroom in your viscous virile teenage cum!"
window hide
with hpunch
mc "AAAH, for the last of it!"
stop channel1
if loisharem == False:
    scene loisdildo07 with fade
    jump LoisPunishment

scene loisdildo10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with fade
mc "Now, now, what to do with that dildo?"
if mission06 and mission06end == False and loisevil == False:
    mc "I should probably pick the first option if I want to advance in my current quest... Just saying..."
menu:
    "Leave it like that as punishment":
        pass
    "Remove it and pound her gaping pussy":
        jump LoisPunishmentPussy

label LoisPunishment:
label LoisPunishmentB:
mc "And now, I'm going to leave you like that. But I'll be magnagnimous and stick that dildo up your dirty slave poontang."
play sound "sounds/moan03.mp3"
lp "Uuuh, thank you, Master..."
scene loisdildo08 with dissolve
play sound "sounds/moan01.mp3"
if age >= 19:
    mc "I order you to stay in that position for the whole night. It's the only way you're going be STRETCHED ENOUGH to accomodate my giant cock."
if age >= 18 and age <= 19:
    mc "I order you to stay in that position for the whole night. It's the only way you're going be STRETCHED ENOUGH to accomodate my giant teenage cock."
if loisevil == False:
    lp "But... I can't stay like this all night, I'll get cramps!"
    mc "I didn't ask for your worthless opinion, you do as you're told!"
    $ loisevil = True
    lp "Y... Yes Master."
jump LoisPunishmentEnd

label LoisPunishmentPussy:
scene loisdildo11 with dissolve
play sound "v041/plop.mp3"
mc "Let's get rid of this tiny dildo..."
lp "Tiny??? But...."
scene loisdildo12 with dissolve
mc "Tiny compared to THIS!"
play sound "sounds/moan02.mp3"
lp "It feels so BIG laying in my ass-crack, Master!"
scene loisdildo13 with dissolve
mc "Fuck yeah! And I'm going to use this tight ass-crack to prime it for what's coming..."
play channel1 "sounds/wetmassage.mp3"
scene loisasscrack
pause

scene loisdildo14 with dissolve
stop channel1
lp "I feel like such a filthy SLUT for you, Master..."
mc "Good, cos that's what you are."
scene loisdildo15 with fastdissolve
play sound "sounds/slap.mp3"
mc "MY filthy slave SLUT!"
lp "YES MASTER!"
scene loisdildo14 with fastdissolve
mc "And don't you forget it!"
scene loisdildo15 with fastdissolve
play sound "sounds/slap.mp3"
lp "AAAH! I NEVER WILL, MASTER!"
scene loisdildo16 with dissolve
mc "Now let's get down to the serious business..."
scene loisdildo17 with dissolve
play sound "sounds/thud.mp3"
lp "Your young cock is... so HEAVY!"
mc "Ten pounds of boymeat right there... Not counting the balls."
scene loisdildo18 with dissolve
lp "I hope I stretched myself out enough for your immense pillar to...."
scene loisdildo19 with dissolve
mc "We're about to find out..."
scene loisdildo20 with dissolve
play sound "sounds/moan04.ogg"
lp "...AAAAH!"
mc "It fits."
play channel1 "v031/womansex07.mp3"

label LoisPussyPunishSlow:
$ loispussypunishfast = False
$ loispussypunishharder = False
hide faster
hide slower
hide sceneicon
hide backicon
hide harder
hide softer
hide cum
if loispussypunishslow == False and loispussypunishstart:
    mc "I've give your stretched pussy a respite by slowing down... For NOW."
    lp "Thank you... AAAH... Master."
    $ loispussypunishslow = True
window hide
show loispussypunishslowvideo behind loispussypunishfastvideo
show loispussypunishslowvideo behind loispussypunishslowpovvideo
show loispussypunishslowvideo behind loispussypunishharderslowvideo
pause 1.0
hide loispussypunishfastvideo
hide loispussypunishslowpovvideo
hide loispussypunishharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
with dissolve
if loispussypunishslow == False and loispussypunishstart == False:
    mc "Ooh yeah, that pussy is nicely stretched already, this is going to be easy..."
    $ loispussypunishslow = True
    $ loispussypunishstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show backicon:
     xpos 50 ypos 500     
call screen loispussypunishslow()
screen loispussypunishslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVSlow")

label LoisPussyPunishFast:
$ loispussypunishharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
window hide
if loispussypunishfast == False:
    mc "Your slave fuckhole is asking to be fucked FASTER, isn't it?"
    lp "Y...Yes Master, fuck it as fast as you wish!"
    $ loispussypunishfast = True
show loispussypunishfastvideo behind loispussypunishslowvideo
show loispussypunishfastvideo behind loispussypunishfastpovvideo
show loispussypunishfastvideo behind loispussypunishharderfastvideo
pause 1.0
hide loispussypunishslowvideo
hide loispussypunishfastpovvideo
hide loispussypunishharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show backicon:
     xpos 50 ypos 500     
call screen loispussypunishfast()
screen loispussypunishfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVFast")

label LoisPussyPunishPOVSlow:
$ loispussypunishharder = False
window hide
hide faster
hide slower
hide sceneicon
hide backicon
hide harder
hide softer
hide cum
if loispussypunishslow == False:
    mc "I've give your stretched pussy a respite by slowing down... For NOW."
    lp "Thank you... AAAH... Master."
    $ loispussypunishslow = True
show loispussypunishslowpovvideo behind loispussypunishslowvideo
show loispussypunishslowpovvideo behind loispussypunishfastpovvideo
show loispussypunishslowpovvideo behind loispussypunishharderpovslowvideo
pause 1.0
hide loispussypunishslowvideo
hide loispussypunishfastpovvideo
hide loispussypunishharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loispussypunishslowpov()
screen loispussypunishslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishSlow")

label LoisPussyPunishPOVFast:
$ loispussypunishharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
window hide
if loispussypunishfast == False:
    mc "Your slave fuckhole is asking to be fucked FASTER, isn't it?"
    lp "Y...Yes Master, fuck it as fast as you wish!"
    $ loispussypunishfast = True
window hide
show loispussypunishfastpovvideo behind loispussypunishslowpovvideo
show loispussypunishfastpovvideo behind loispussypunishfastvideo
show loispussypunishfastpovvideo behind loispussypunishharderpovfastvideo
pause 1.0
hide loispussypunishslowpovvideo
hide loispussypunishfastvideo
hide loispussypunishharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loispussypunishfastpov()
screen loispussypunishfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishFast")

label LoisPussyPunishHarderSlow:
if loispussypunishharder == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharder = True        
window hide
show loispussypunishharderslowvideo behind loispussypunishharderfastvideo
show loispussypunishharderslowvideo behind loispussypunishharderpovslowvideo
show loispussypunishharderslowvideo behind loispussypunishslowvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide loispussypunishharderfastvideo
hide loispussypunishharderpovslowvideo
hide loispussypunishslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show backicon:
     xpos 50 ypos 500     
call screen loispussypunishharderslow()
screen loispussypunishharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCum")

label LoisPussyPunishHarderFast:
if loispussypunishharder == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharder = True        
window hide
show loispussypunishharderfastvideo behind loispussypunishharderslowvideo
show loispussypunishharderfastvideo behind loispussypunishharderpovfastvideo
show loispussypunishharderfastvideo behind loispussypunishfastvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide loispussypunishharderslowvideo
hide loispussypunishharderpovfastvideo
hide loispussypunishfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show backicon:
     xpos 50 ypos 500     
call screen loispussypunishharderfast()
screen loispussypunishharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCum")

label LoisPussyPunishHarderPOVSlow:
if loispussypunishharder == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharder = True        
window hide
show loispussypunishharderpovslowvideo behind loispussypunishharderslowvideo
show loispussypunishharderpovslowvideo behind loispussypunishharderpovfastvideo
show loispussypunishharderpovslowvideo behind loispussypunishslowpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide loispussypunishharderslowvideo
hide loispussypunishharderpovfastvideo
hide loispussypunishslowpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loispussypunishharderpovslow()
screen loispussypunishharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCum")

label LoisPussyPunishHarderPOVFast:
if loispussypunishharder == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharder = True        
window hide
show loispussypunishharderpovfastvideo behind loispussypunishharderpovslowvideo
show loispussypunishharderpovfastvideo behind loispussypunishharderfastvideo
show loispussypunishharderpovfastvideo behind loispussypunishfastpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide loispussypunishharderpovslowvideo
hide loispussypunishharderfastvideo
hide loispussypunishfastpovvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
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
call screen loispussypunishharderpovfast()
screen loispussypunishharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCum")

label LoisPussyPunishCum:
hide faster
hide slower
hide sceneicon
hide backicon
hide cum
hide softer
hide harder
mc "You want my cum, don't you SLAVE?"
lp "I... would be honored if you flooded my insides with your virile seed, Master..."
scene loispunishmentcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "IMMINENT FLOODING ALERT! RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
lp "AAAH, Master, thank you so much!"
scene loispunishmentcum02 with dissolve
play sound "sounds/thud.mp3"
lp "You're coming so DEEP inside me!"
window hide
with hpunch
mc "FUCK YEAH, AAAH!"
scene loispunishmentcum03 with dissolve
mc "Gonna dump a MASTER load inside your SLAVE pussy, RHAAA!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
lp "Yes, YES! Knock me up, Master, your slave will carry your baby!"
scene loispunishmentcum04 with dissolve
mc "You want some STRONG sperm?"
scene loispunishmentcum05 with dissolve
play sound "sounds/thud.mp3"
mc "Here's SOME BILLIONS OF THEM!"
window hide
with fastflash
lp "SO STRONG!"
scene loispunishmentcum04 with dissolve
mc "Not done yet!"
scene loispunishmentcum05 with dissolve
play sound "sounds/thud.mp3"
mc "RHAAA!"
window hide
with hpunch
lp "I'm getting PREGNANT with your load!"
scene loispunishmentcum04 with dissolve
mc "That's the idea!"
scene loispunishmentcum05 with dissolve
play sound "sounds/slap.mp3"
mc "TAKE SOME MORE, TAKE ALL OF IT!!!"
window hide
with vpunch 
lp "AAAH, Master, you're the BEST MASTER EVER!!!"
scene loispunishmentcum06 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Now get that mouth over here..."
lp "You...You want to kiss your slave?"
scene loispunishmentcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pause
mc "You'd better give me a boy... Or else..."
lp "Y.. Yes, Master."

label LoisPunishmentEnd:
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main