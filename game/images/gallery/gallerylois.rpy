label LoisGallery:
stop channel3
play channel3 "sounds/ccpdoffice.mp3"
scene loisbackground with dissolve
show loismaingallery at gallerypos01 with moveinleft

call screen gallerylois()
screen gallerylois():
    text "{font=Gui/Heroes Legend.ttf}Naughty Lois Pane{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerylois"), Jump ("MainGallery03b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerylois"), Jump ("LoisGalleryAnim")]

    if renpy.seen_image("photopreshoot01"):
        imagebutton:
            focus_mask True
            idle "gallery/loisgallery01.png" xpos 400 ypos 100
            hover "gallery/loisgallery01.png"
            action Jump ("LoisGallery01")
    text "{font=Gui/Heroes Legend.ttf}Photoshoot{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("photopreshoot01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LoisGallery")

    if renpy.seen_image("loisbedroom01"):
        imagebutton:
            focus_mask True
            idle "gallery/loisgallery02.png" xpos 750 ypos 100
            hover "gallery/loisgallery02.png"
            action Jump ("LoisGallery02")
    text "{font=Gui/Heroes Legend.ttf}BDSM Night{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("loisbedroom01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LoisGallery")

    if renpy.seen_image("loisdildo01"):
        imagebutton:
            focus_mask True
            idle "gallery/loisgallery03.png" xpos 1100 ypos 100
            hover "gallery/loisgallery03.png"
            action Jump ("LoisGallery03")
    text "{font=Gui/Heroes Legend.ttf}Dildo Play & Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("loisdildo01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LoisGallery")

    if renpy.seen_image("loissupercum10"):
        imagebutton:
            focus_mask True
            idle "gallery/loisgallery04.png" xpos 1450 ypos 100
            hover "gallery/loisgallery04.png"
            action Jump ("LoisGallery04")
    text "{font=Gui/Heroes Legend.ttf}Super-Cucking{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("loissupercum10") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("LoisGallery")

label LoisGalleryAnim:
stop channel3
play channel3 "sounds/sexy04.mp3"
call screen screenanimlois()
screen screenanimlois():
    modal True
    add "gallery/loisbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "loisanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "loisanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "loisanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimlois"), SetVariable ("animcount", 1), Jump ("LoisGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Lois Pane{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 31{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft3{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}30D-20-32{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Male Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}BDSM{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Cum Showers{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/loisanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimlois")]
    add "gallery/loisanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimlois")]
    add "gallery/loisanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimlois")]
        
    
label LoisGallery01:
stop channel3
play channel1 "sounds/sexy05.mp3"
scene photopreshoot01 with fade
lp "This is our photo studio. Used mainly for shooting superheroes like yourself for our Special Superheroes Calendar Edition..."
mc "Which edition will I be featuring in?"
scene photopreshoot02 with dissolve
lp "Well, in your case, the \"Superheroes studmuffins Limited Edition\"..."
mc "I see... Mainly aimed at a female audience I gather?"
lp "That's right, half of our readership are women. So just act natural and don't be shy, our readers want some nice sexy but not too raunchy pics, you understand?"
mc "I get it. Where should I go to pose?"
scene photoshoot01 with dissolve
lp "Just over there on the stage in front of the white screen. I'll add a superhero-themed background later in post-editing."
scene photoshoot02 with dissolve
mc "Like here? Am I in the frame?"
lp "Don't worry, I'll move around to take pics from different angles."
scene photoshoot03 with dissolve
lp "Smile for your female fans, [hero]!"
scene photoshoot03 with fastflash
if age >= 20:
    lp "Perfect! Now flex those huge muscles for me..."
if age == 18 or age == 19:
    lp "Perfect! Now flex those huge teenage muscles for me..."
scene photoshoot04 with dissolve
mc "Like that?"
scene photoshoot04 with fastflash
lp "Damn boy, you are RIPPED! Now flex those biceps..."
scene photoshoot05 with dissolve
lp "These are the biggest boulders I ever shot..."
scene photoshoot05 with fastflash
lp "They seem to be rippling with POWER... Next, do a superhero pose with your fist up in the air."
scene photoshoot06 with dissolve
lp "Like you've just defeated the worst super-villain in Cockham City."
scene photoshoot06 with fastflash
lp "Keep that pose a bit longer..."
scene photoshoot07 with dissolve
lp "Nice..."
scene photoshoot07 with fastflash
lp "Just a few more pics..."
scene photoshoot08 with dissolve
mc "Your camera seems to be aimed rather... below the belt, Ms Pane."
scene photoshoot09 with dissolve
lp "What? Oh, I'm sorry, I was just..."
scene photoshoot10 with dissolve
mc "...Taking pictures of my dangling boyhood?"
lp "Well, I mean, it's just sssooo BIG!"
scene photoshoot11 with dissolve
mc "Well, let me help you if you're interested in a VERY \Special Edition\"..."
lp "What are you doing [hero]? I..."
scene photoshoot12 with dissolve
if age >= 20:
    lp "Oh My God, that's the biggest monster love muscle I've ever seen!"
if age == 18 or age == 19:
    lp "Oh My God, that's the biggest monster teenage love muscle I've ever seen!"
mc "Go ahead and take pictures of it..."
scene photoshoot13 with dissolve
lp "Okay, but just for my *personal* collection..."
scene photoshoot13 with fastflash
lp "It seems to be GROWING [hero]! I'm not sure if I should... Can I... touch it?"
mc "Sure, you need to FEEL its power to get a REAL-LIFE viewpoint for your article, right?"
lp "Yes, that's exactly why I'm doing this... [hero]."
scene photoshoot14 with dissolve
lp "It's so HEAVY... It weighs like several pounds of flesh."
mc "And it's not even half-hard Ms Pane..."
lp "I can feel it growing some more... It's so BEAUTIFUL up close..."
scene photoshoot15 with dissolve
play sound "sounds/lick01.ogg"
lp "I just wanna lick it..."
scene photoshoot16 with dissolve
play sound "sounds/slurp.mp3"
lp "And suck out the abundant precum flowing from its tip..."
scene photoshoot17 with dissolve
lp "And kiss it and worship it..."
play sound "sounds/kiss.mp3"
scene photoshoot18 with dissolve
play sound "sounds/lick02.mp3"
lp "And suck your tasty balls and make them churn an extra-big load for me..."
scene photoshoot19 with dissolve
stop sound
lp "You're going to do that for me [hero]? Deliver the BIGGEST superhero load of cum ever?"
scene photoshoot20 with dissolve
lp "And cover my titties in an inch-thick layer of it? Pleasure yourself for me please!"
scene photoshoot21 with dissolve
mc "Oh fuck, yeah, I'll do it Lois! I'm so fucking hard for you right now!"
scene photoshoot22 with dissolve
lp "I can see that, your cock is just... ENORMOUS! And your balls look so.. FULL!"
play channel2 "sounds/wank.mp3"
window hide
show photowankslow
with dissolve
pause
if age >= 20:
    lp "Yeah, jerk that fat superhero dong!"
if age == 18 or age == 19:
    lp "Yeah, jerk that fat teenage superhero dong!"
window hide
pause
hide photowankslow
show photowankfast
lp "God, I can't stop watching you pump that fat shaft... It's so... arousing!"
if age >= 20:
    mc "That's right, just watch me bring this fat fifteen-incher to a mighty eruption of cum!"
if age == 18 or age == 19:
    mc "That's right, just watch me bring this fat teenage fifteen-incher to a mighty eruption of cum!"
stop channel2
scene photoshootcum01 with dissolve
play sound "sounds/boymoan.mp3"
mc "AAAH!"
lp "Oh my God, that plume of spunk is GIGANTIC!"
scene photoshootcum02 with dissolve
play sound "sounds/splooge01.mp3"
lp "You're COVERING me in your warm seed... I LOVE IT, MORE, MORE!"
window hide
with fastflash
mc "Hang on, there's MORE, AAAH!"
scene photoshootcum03 with dissolve
lp "Still MORE cum for me? You are a true SUPERHERO CUM MACHINE!"
window hide
with fastflash
mc "Damn, can't stop CU-UU-MING!"
scene photoshootcum04 with dissolve
play sound "sounds/panting.mp3"
lp "I've never been so completely DRENCHED in anything, let alone a boy's red-hot seed... mmmh..."
mc "Come and suck out the afterdregs..."
scene photoshootcum05 with dissolve
play sound "sounds/slurp.mp3"
lp "Yes sir, it's sssoo tasty... Yummy!"
stop channel1
play sound "sounds/scratch.mp3"
scene photoshootcum06 with dissolve
lp "Shit, Clark? What are you doing here?"
mc "Err, Supe... I mean, wassup, Kunt?"
scene photoshootcum07 with dissolve
cl "How could you do this to me Lois?"
scene photoshootcum08 with dissolve
lp "I'm sorry Clark but [hero]'s cock was just... so enticing. And HE'S the one who showed it to me!"
mc "Hey! YOU'RE the one who was taking shots of it! (no change)"
scene photoshootcum09 with dissolve
lp "I... I admit it. But I WAS WRONG!"
lp "Please forgive me Clark. We could... go on a date tomorrow night?"
scene photoshootcum12 with dissolve
cl "I... forgive you. I'll try and pretend this never happened. *sigh*"
scene photoshootcum13 with dissolve
mc "Right, well, my photoshoot job is done here so... I 'll leave you two lovebirds to it then..."
jump LoisGallery

label LoisGallery02:
$ loissofatold01x = False
$ loissucktold01x = True
stop channel3
stop channel1
play channel1 "sounds/sexy04.mp3"
scene loisbedroom01 with dissolve
lp "So, what are you into for tonight's BDSM entertainment? I need to feel some PAIN. Lots of it."
call screen loisbedroomx()
screen loisbedroomx():
    modal True    
    imagebutton:
        focus_mask True
        idle "v02/loisrestraintidle.png"
        hover "v02/loisrestrainthover.png"
        action Jump ("LoisRestraintx")
    imagebutton:
        focus_mask True
        idle "v02/loissofaidle.png"
        hover "v02/loissofahover.png"
        action Jump ("LoisSofax")

label LoisRestraintx:
mc "Get your butt in the restraining rack, Lois."
lp "Ooh, that's a really PAINFUL position for me. Ideal for abusing my body from both ends..."
scene loisrack01 with dissolve
lp "I'm ready. I'm tied up like a hog. I am at your MERCY, [hero]. What will you do to poor little me?"
scene loisrack02 with dissolve
mc "Let me check that you're really well settled in there first. Yeah, that filthy butt is sticking out, begging to be PUNISHED!"
lp "Yes, it is. I've been so naughty..."
menu:
    "Slap her ass with your hand":
        jump LoisSlapHandx
    "Slap her ass with your cock":
        jump LoisSlapCockx
label LoisSlapHandx:
scene loisrack03 with dissolve
mc "A naughty girl needs to have her ass SLAPPED!"
lp "You're so strong, it's going to HURT a LOT!"
scene loisrack04 with dissolve
play sound "sounds/slap.mp3"
mc "Take that, you filthy slut!"
scene loisrack03 with dissolve
lp "AAH! MORE! MORE please! I deserve it!"
window hide
play music [ "sounds/slap.mp3", "<silence .7>" ]
scene loisrackhand
pause
stop music
jump LoisRackEndx

label LoisSlapCockx:
scene loisrack05 with dissolve
mc "A filthy girl like you needs to have her ass SLAPPED! By a HARD COCK!"
lp "Your giant shaft is so HEAVY, it's going to HURT a LOT!"
play sound "sounds/thud.mp3"
scene loisrack06 with dissolve
mc "Take that, you filthy slut!"
scene loisrack05 with dissolve
lp "AAH! MORE! MORE please! I deserve it!"
window hide
play music [ "sounds/thud.mp3", "<silence .8>"]
scene loisrackcock
pause
stop music
label LoisRackEndx:
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
label LoisDeepThroatSlowx: 
hide cum
hide faster
hide slower
show loissuckslowvideo behind loissuckfastvideo
pause 1.0
play music "sounds/blow02.mp3"
hide loissuckfastvideo with dissolve
if loissucktold01x == False:
    mc "Slowly to begin with... Yeah, just like that..."
    window hide
    $ loissucktold01x = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen loissuckslowx()
screen loissuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDeepThroatFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDeepThroatEndx")

label LoisDeepThroatFastx:
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

call screen loissuckfastx()
screen loissuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDeepThroatSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDeepThroatEndx")

label LoisDeepThroatEndx:
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
    "I didn't ask for your worthless opinion and I'm still HORNY!" if loisevil:
        jump LoisPostScenex
    "Alright, hopefully next time you'll have more stamina.":
        lp "I PROMISE! Next time, I'll be ready for MORE for YOU."
        mc "Then I'll untie you and go back to the gallery."
stop channel1
jump LoisGallery

label LoisSofax:
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
label LoisSofaSlowx:  
hide cum
hide faster
hide slower
show loissofaslowvideo behind loissofafastvideo
pause 1.0
play channel2 "sounds/boymoan02.mp3"
hide loissofafastvideo with dissolve
if loissofatold01x == False:
    mc "Slowly to begin with... Yeah, just like that..."
    lp "It's so LONG and THICK, Master!"
    window hide
    $ loissofatold01x = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
     
call screen loissofaslowx()
screen loissofaslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSofaFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSofaEndx")

label LoisSofaFastx:
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

call screen loissofafastx()
screen loissofafastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSofaSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSofaEndx")

label LoisSofaEndx:
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
stop channel2
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
stop channel1
stop music
jump LoisGallery

label LoisPostScenex:
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
mc "Because what it means is that I don't want you to see Clark Kunt again! EVER!"
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
stop channel3
stop music
jump LoisGallery

label LoisGallery03:
stop channel3
stop channel1
$ loisdildofuckslowx = False
stop music
play music "sounds/sexy04.mp3"
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

label LoisDildoFuckSlowx:
$ loisdildofuckfastx = False
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
if loisdildofuckslowx == False:
    $ loisdildofuckslowx = True
    mc "Nice, take it deep, Lois, cos my dong is even bigger than that dildo."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen loisdildofuckslowx()
screen loisdildofuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckPOVSlowx")

label LoisDildoFuckFastx:
$ loisdildofuckslowx = False
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
if loisdildofuckfastx == False:
    $ loisdildofuckfastx = True    
    mc "You're doing good, take it HARD and FAST, tht's the way I like to anally POUND my women!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen loisdildofuckfastx()
screen loisdildofuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckPOVFastx")


label LoisDildoFuckPOVSlowx:
$ loisdildofuckfastx = False
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
if loisdildofuckslowx == False:
    $ loisdildofuckslowx = True
    mc "Nice, take it deep, Lois, cos my dong is even bigger than that dildo."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loisdildofrontfuckslowx()
screen loisdildofrontfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckSlowx")

label LoisDildoFuckPOVFastx:
$ loisdildofuckslowx = False
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
if loisdildofuckfastx == False:
    $ loisdildofuckfastx = True    
    mc "You're doing good, take it HARD and FAST, tht's the way I like to anally POUND my women!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loisdildofrontfuckfastx()
screen loisdildofrontfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisDildoFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisDildoFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisDildoFuckFastx")

label LoisDildoFuckEndx:
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
    jump LoisPunishmentx

scene loisdildo10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with fade
mc "Now, now, what to do with that dildo?"
menu:
    "Leave it like that as punishment":
        jump LoisPunishmentBx
    "Remove it and pound her gaping pussy":
        jump LoisPunishmentPussyx

label LoisPunishmentx:
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
jump LoisGallery

label LoisPunishmentBx:
scene loisdildo08 with dissolve
play sound "sounds/moan01.mp3"
if age >= 19:
    mc "I order you to stay in that position for the whole night. It's the only way you're going be STRETCHED ENOUGH to accomodate my giant cock."
if age >= 18 and age <= 19:
    mc "I order you to stay in that position for the whole night. It's the only way you're going be STRETCHED ENOUGH to accomodate my giant teenage cock."
jump LoisGallery

label LoisPunishmentPussyx:
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
$ loispussypunishslowx = False

label LoisPussyPunishSlowx:
$ loispussypunishfastx = False
$ loispussypunishharderx = False
hide faster
hide slower
hide sceneicon
hide backicon
hide harder
hide softer
hide cum
if loispussypunishslowx == False and loispussypunishstart:
    mc "I've give your stretched pussy a respite by slowing down... For NOW."
    lp "Thank you... AAAH... Master."
    $ loispussypunishslowx = True
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
if loispussypunishslowx == False and loispussypunishstart == False:
    mc "Ooh yeah, that pussy is nicely stretched already, this is going to be easy..."
    $ loispussypunishslowx = True
    $ loispussypunishstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show backicon:
     xpos 50 ypos 500     
call screen loispussypunishslowx()
screen loispussypunishslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVSlowx")

label LoisPussyPunishFastx:
$ loispussypunishharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
window hide
if loispussypunishfastx == False:
    mc "Your slave fuckhole is asking to be fucked FASTER, isn't it?"
    lp "Y...Yes Master, fuck it as fast as you wish!"
    $ loispussypunishfastx = True
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
call screen loispussypunishfastx()
screen loispussypunishfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVFastx")

label LoisPussyPunishPOVSlowx:
$ loispussypunishharderx = False
window hide
hide faster
hide slower
hide sceneicon
hide backicon
hide harder
hide softer
hide cum
if loispussypunishslowx == False:
    mc "I've give your stretched pussy a respite by slowing down... For NOW."
    lp "Thank you... AAAH... Master."
    $ loispussypunishslowx = True
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
call screen loispussypunishslowpovx()
screen loispussypunishslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishSlowx")

label LoisPussyPunishPOVFastx:
$ loispussypunishharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide backicon
window hide
if loispussypunishfastx == False:
    mc "Your slave fuckhole is asking to be fucked FASTER, isn't it?"
    lp "Y...Yes Master, fuck it as fast as you wish!"
    $ loispussypunishfastx = True
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
call screen loispussypunishfastpovx()
screen loispussypunishfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishFastx")

label LoisPussyPunishHarderSlowx:
if loispussypunishharderx == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharderx = True        
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
call screen loispussypunishharderslowx()
screen loispussypunishharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCumx")

label LoisPussyPunishHarderFastx:
if loispussypunishharderx == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharderx = True        
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
call screen loispussypunishharderfastx()
screen loispussypunishharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCumx")

label LoisPussyPunishHarderPOVSlowx:
if loispussypunishharderx == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharderx = True        
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
call screen loispussypunishharderpovslowx()
screen loispussypunishharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCumx")

label LoisPussyPunishHarderPOVFastx:
if loispussypunishharderx == False:
    mc "You've taken half of my fat [age]yo fuckrod, now it's time for me to POUND the other half inside your dirty hole!"
    if age >= 20:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant battering ram!"
    if age >= 18 and age <= 19:
        lp "AAAH, Master, I deserve to be fucked mercilessly by your giant teenage battering ram!"
    $ loispussypunishharderx = True        
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
call screen loispussypunishharderpovfastx()
screen loispussypunishharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisPussyPunishHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisPussyPunishPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisPussyPunishHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPussyPunishCumx")

label LoisPussyPunishCumx:
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
stop music
stop channel1
jump LoisGallery

label LoisGallery04:
stop channel3
scene supermanshoot00 with fade
lp "[hero], why don't you go and pick the costume I left for you in the backroom and put it on?"
mc "Will do, Ms Pane. I hope it has an XXL large pouch at the front."
lp "Oh, I made SURE of that! * wink *"
scene supermanshoot01 with dissolve
lp "While [hero] is changing, let's start off this photoshoot with you, Superman!"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "Smile!"
scene supermanshoot02 with dissolve
lp "Now pretend you're about to LIFT OFF!"
window hide
play sound "sounds/flash.mp3"
with fastflash
sm "I have a cape so I'm a REAL Superhero!"
scene supermanshoot03 with dissolve
lp "I didn't know the cape had anything to do with it."
sm "It's super-important!"
scene supermanshoot04 with dissolve
lp "Ah, I see [hero] is ready, let me do a few pictures with him alone then."
sm "But.."
mc "Come on man, it's MY turn!"
scene supermanshoot05 with dissolve
mc "I'll do a pose like I'm about to BANG on the ground and make my enemies TREMBLE WITH FEAR!"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "Ooh, you're such a STRONG superhero!"
sm "I'm stronger than him. Super-Strength level 3. He's only Level 2."
scene supermanshoot06 with dissolve
mc "How about these SUPER-MUSCLES?"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "My God, they're so BIG!"
sm "Pff, you don't need ridiculously huge muscles to have Super-Strength!"
scene supermanshoot07 with dissolve
lp "Why don't you join [hero] now, Superman? I'd like to have you BOTH in the same frame..."
sm "Umpf, I don't know if this is a good idea..."
mc "What, are you scared that you'll look PUNY next to me, Superman?"
sm "Absolutely NOT! A TRUE Superhero does not concern himself with such petty considerations. I'll stand next to you and PROVE it!"
scene supermanshoot08 with dissolve
sm "There, see? Nothing scares SUPERMAN!"
lp "Your tiny bulge reminds me of someone. A colleague of mine who otherwise wears glasses and therefore doesn't look like you at all..."
scene supermanshoot08 with dissolve
sm "Is he... someone nice that you like?"
lp "Sure... except for..."
mc "The fact that he doesn't have a dick?"
scene supermanshoot10 with dissolve
lp "I don't even know... I... never saw it."
mc "Probably best, you might be VERY disappointed."
sm "Hey!"
lp "Err, let's get back to the photoshoot shall we? Pose like you are both fighting some Super-Villain TOGETHER!"
scene supermanshoot11 with dissolve
sm "Take that Sexy Luthor!"
window hide
play sound "sounds/flash.mp3"
with fastflash
mc "Oh, she took something from me alright! My MASSIVE cock! That's how I, err..."
scene supermanshoot12 with dissolve
sm "What? You...?"
mc "Well, yeah, I mean, she Super-Seduced me, so I had no choice! But thanks to my Super-Studliness, I wasn't defeated by her super-tight pussy."
scene supermanshoot09 with dissolve
sm "She never Super-Seduced me... * sigh *"
window hide
play sound "sounds/flash.mp3"
with fastflash
mc "Why would she? You can't give it to her good like me."
scene supermanshoot13 with dissolve
lp "She could do... stuff TO him though."
window hide
play sound "sounds/flash.mp3"
with fastflash
sm "What... are you saying?"
scene supermanshoot12 with dissolve
mc "Oh yeah, I hadn't thought of that. She could wear a strap-on dildo and give it to YOU good. You might even enjoy it. Like losing your virginity."
sm "You... You think so?"
scene supermanshoot14 with dissolve
lp "I have a strap-on in my office. Don't ask me why, but I'll go and get it and we can show Superman how great SEX is really like!"
sm "But... I never said yes!"
lp "Oh come on, you clearly NEED some, don't pretend you don't... And I owe you for saving my life during that earthquake last year. Let me show you my appreciation... MY WAY."
sm "I... I suppose we could try... something...."
scene supermanshoot15 with dissolve
mc "Alright, it's a deal then. You take Superman up the ass while I take YOU up the ass!"
sm "What? How dare you treat Lois Pane like a cheap whore like that! And you might hurt her, your cock is just... TOO BIG!"
lp "Don't worry about me, Superman. I... do enjoy being treated like that... I'll be back in a moment, my sexy superheroes!"
scene supermanshoot16 with dissolve
sm "I... didn't know that she... liked that... But why?"
mc "Different women have different sex kinks, buddy. That's just the way the SEX world is. Trust me, I know everything about what women WANT."
mc "You might learn a few things from watching ME perform. Call it sexual education for dickless superheroes."
play music "sounds/sexy09.mp3"
scene supermanshoot17 with dissolve
lp "Here I am. Now you two, off with those tight bodysuits! * wink *"
mc "Ooh yeah! I was getting hard already anyway!"
scene supermanshoot18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
sm "I... I'm still not sure this is a goo...."
lp "Just get on all fours, Superman! I ORDER YOU!"
sm "Err, right Ms Pane..."
scene supermanshoot19 with dissolve
mc "Oh man, she's going to totally OWN YOUR ASS!"
sm "Don't say that please!"
mc "And I'm going to totally own HER ass!"
sm "That's even worse..."
scene supermanshoot20 with dissolve
mc "Wow, you look like a Ken doll! If they ever make a Barbie movie, you should be the main actor!"
lp "And I'll be \"Strap-on Barbie\" for you!"
scene supermanshoot21 with dissolve
lp "So, Superman, are you ready to take on my HUGE cock?"
sm "I..."
scene supermanshoot22 with dissolve
lp "Your backdoor looks really enticing, you're making me so HARD for you, Superman!"
mc "Why do you even have an asshole? I thought you never ate."
sm "Err..."
scene supermanshoot23 with dissolve
mc "Slap that dildo on his buttcheeks, Lois!"
lp "You think so? Let's try..."
scene supermanshoot24 with dissolve
play sound "sounds/slap.mp3"
play channel1 "sounds/boymoan02.mp3"
lp "Do you like that, Superman? Me slapping my MASSIVE dildo on your filthy ass?"
sm "I... I think so..."
window hide
play channel2 [ "sounds/slap.mp3", "<silence .7>" ]
scene loisrackdildo
pause
stop music
mc "Superman is clearly into it... If he had a dick, he'd be drooling pre-cum right now!"
scene supermanshoot25 with dissolve
stop channel2
lp "Now let's see how well this dildo fits into that lovely hole..."
sm "Please be careful, I've never..."
window hide
stop channel1
show supershootanim01video
play sound "sounds/boymoan03.mp3"
$ renpy.pause(1.36, hard='True')
scene supermanshoot25b
sm "...AAAH!"
scene supermanshoot26 with dissolve
lp "Enjoying it, Superman?"
sm "I... I do, yes."
scene supermanshoot27 with dissolve
if age >= 20:
    mc "And now it's MY turn to see how well my giant cock fits into YOUR lovely hole, Lois..."
if age >= 18 and age <= 19:
    mc "And now it's MY turn to see how well my giant teenage cock fits into YOUR lovely hole, Lois..."
window hide
show supershootanim02video
$ renpy.pause(1.40, hard='True')
play sound "sounds/moan01.mp3"
scene supermanshoot27b
lp "OOOOH! Let me get used to that GIRTH!"
scene supermanshoot28 with dissolve
mc "No time to waste here, let's FUCK!"
play channel2 "sounds/boymoan02.mp3"
$ strapfuckslowx = False

label StrapFuckSlowx:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckslowvideo behind strapfuckfastvideo
show strapfuckslowvideo behind strapfuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckfastvideo
hide strapfuckpovslowvideo
with dissolve
play channel1 "v031/womansex07.mp3"
$ strapfuckfastx = False
if strapfuckslowx == False:
    lp "You're a Barbie boy, in a Barbie world, strap-on plastic, it's fantastic!"
    $ strapfuckslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen strapfuckslowx()
screen strapfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("StrapFuckFrontSlowx")

label StrapFuckFastx:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckfastvideo behind strapfuckslowvideo
show strapfuckfastvideo behind strapfuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckslowvideo
hide strapfuckpovfastvideo
with dissolve
play channel1 "v031/womansex08.mp3"
$ strapfuckslowx = False
if strapfuckfastx == False:
    mc "Fuck, get ready for a MASSIVE ANAL POUNDING. BOTH OF YOU!"
    $ strapfuckfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen strapfuckfastx()
screen strapfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("StrapFuckFrontFastx")

label StrapFuckFrontSlowx:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckpovslowvideo behind strapfuckslowvideo
show strapfuckpovslowvideo behind strapfuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckslowvideo
hide strapfuckpovfastvideo
with dissolve
play channel1 "v031/womansex07.mp3"
$ strapfuckfastx = False
if strapfuckslowx == False:
    lp "You're a Barbie boy, in a Barbie world, strap-on plastic, it's fantastic!"
    $ strapfuckslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen strapfuckpovslowx()
screen strapfuckpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckSlowx")

label StrapFuckFrontFastx:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckpovfastvideo behind strapfuckfastvideo
show strapfuckpovfastvideo behind strapfuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckfastvideo
hide strapfuckpovslowvideo
with dissolve
play channel1 "v031/womansex08.mp3"
$ strapfuckslowx = False
if strapfuckfastx == False:
    mc "Fuck, get ready for a MASSIVE ANAL POUNDING. BOTH OF YOU!"
    $ strapfuckfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen strapfuckpovfastx()
screen strapfuckpovfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFastx")

label StrapFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide front
mc "This is so HAWT, it's making want to..."
stop channel1
scene supershootcum01 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "...blast! RHAAAA!"
window hide
with fastflash
play sound "v032/womancum03.mp3"
lp "AAAH, I can feel it, right in my guts!"
scene supershootcum02 with dissolve
play sound "v032/womancum04.mp3"
lp "SSSSOOO DEEP!"
window hide
with hpunch
sm "TOO DEEP for me, please Lois, take it out!"
scene supershootcum03 with dissolve
mc "No! Keep it in in his pussy ass, while I pump my load inside yours, AAAH!"
window hide
with fastflash
play sound "sounds/splooge02.mp3"
lp "Yes, MASTER!"
scene supershootcum04 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "Take those fat wads, still NU-UUU-TTTIIINNNG!"
window hide
with hpunch
play channel1 "sounds/boyorgasm01.mp3"
if age >= 20:
    lp "Can you see that, Superman? Can you see how much spunk is ERUPTING from this SUPERSTUD'S STALLION COCK?"
if age >= 18 and age <= 19:
    lp "Can you see that, Superman? Can you see how much spunk is ERUPTING from this SUPERSTUD'S TEENAGE STALLION COCK?"
scene supershootcum05 with dissolve
play sound "sounds/moan01.mp3"
lp "Oooh yeah, cover Superman in your hot sauce, make him BEG FOR MORE!"
window hide
with fastflash
mc "Sure Lois, here I CO-O-MMME!"
stop channel2
scene supershootcum06 with dissolve
play sound "sounds/splat.ogg"
sm "This is so humiliating...."
window hide
with fastflash
lp "What are you complaining about? I thought you liked it. I definitely heard you moan a lot."
scene supershootcum07 with dissolve
play sound "sounds/splat.ogg"
sm "I... might have, but..."
window hide
with fastflash
lp "You deserve a good spanking for LYING!"
scene supershootcum08 with dissolve
play sound "sounds/slap.mp3"
lp "Admit that you LIKE this and that you DESERVE this!"
window hide
with hpunch
sm "I... Please stop, it's... nice but not very nice..."
scene supershootcum09 with dissolve
lp "I didn't hear you well enough! Say it out LOUD!"
scene supershootcum10 with dissolve
play sound "sounds/slap.mp3"
sm "Alright, I DO, Lois, I deserve it!"
lp "You sure as hell do, you dickless superhero!"
stop channel1
scene supershootcum11 with dissolve
play sound "sounds/slurp.mp3"
lp "Let me clean you of all this tasty virile seed..."
scene supershootcum12 with dissolve
play sound "sounds/slap.mp3"
mc "Hey, maybe HE wants to have a taste..."
scene supershootcum11 with dissolve
play sound "sounds/slurp.mp3"
lp "I want it all for ME!"
scene supershootcum12 with dissolve
play sound "sounds/slap.mp3"
mc "Well, hurry up Lois, cos I'm STILL HARD as you can feel from my fat rod slapping your backside!"
lp "Of course Master. Superman, get back on your feet, I wil let you have a taste. From somewhere I can't reach. My little overfilled rosebud!"
scene supermanshoot30:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/kiss.mp3"
lp "While I kiss [hero] and show my total devotion to his Super-Studliness!"
scene supermanshoot31 with dissolve
sm "But, I... never..."
lp "Just stick your tongue in there and slurp up all of [hero]'s manly juices. Including what's dripping OUT of my hole... DO IT NOW!"
scene supermanshoot32 with dissolve
play sound "sounds/lick03.mp3"
sm "If this please you, Lois..."
play sound "sounds/lick02.mp3"
lp "Mmmh, twirl that tongue DEEPER..."
scene supermanshoot33 with dissolve
play sound "sounds/slurp.mp3"
lp "Yes, that's it, you're hitting the right spot, AAAH!"
play sound "sounds/moan03.mp3"
scene supermanshoot34 with dissolve
play sound "sounds/kiss.mp3"
lp "You did well, Superman..."
scene supermanshoot35 with dissolve
stop sound
if age >= 20:
    lp "Now, gently take my strapon off. I want to get FUCKED by a REAL cock! A HUGE, MASSIVE, DONKEY-DICK!"
if age <= 19:
    lp "Now, gently take my strapon off. I want to get FUCKED by a REAL cock! A HUGE, MASSIVE, YOUNG DONKEY-DICK!"
scene supermanshoot36 with dissolve
play sound "sounds/wow.mp3"
lp "Just look at it, Superman! It's so GIGANTIC!"
sm "I wish I had a cock now..."
mc "Why don't you have a quick taste first Lois?"
scene supermanshoot37 with dissolve
play sound "sounds/lick01.ogg"
lp "It's just DEE-LI-CIOUS!"
scene supermanshoot38 with dissolve
lp "Best shaft I've EVER tasted!"
window hide
show loissuperlick
play channel2 "sounds/lick01.ogg"
pause
mc "Now that I'm SUPER-HARD, let's show Superman how to Super-Please a woman!"
stop channel2
scene supermanshoot39 with dissolve
lp "Mmmh, look at this thing! It's DROOLING pre-cum everywhere... He must be so HORNY!"
sm "Please stop doing that Lois, it's... all sticky..."
if age >= 20:
    lp "I'm just having a little bit of fun. Just to show you how WIDE I'm going to have to open my legs to let this monstercock slide into my tight little fuckhole..."
if age >= 18 and age <= 19:
    lp "I'm just having a little bit of fun. Just to show you how WIDE I'm going to have to open my legs to let this teenage monstercock slide into my tight little fuckhole..."
scene supermanshoot40 with dissolve
play sound "sounds/moan02.mp3"
mc "Now watch closely, this is how a Super-Stud like me gets all the girls..."
scene supermanshoot41 with dissolve
lp "I'm already dripping wet just by looking at his beautiful piece of boymeat!"
sm "Please don't say that, Lois..."
lp "But it's TRUE! FUCK ME, YOU MONSTER-DICKED YOUNG STALLION!"
$ loissuperfuckslowx = False

label LoisSuperShortSlowx:
$ loissuperharderx = False
window hide
show loissupershortslowvideo behind loissupershortfastvideo
show loissupershortslowvideo behind loissupershortpovslowvideo
show loissupershortslowvideo behind loissuperfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissupershortfastvideo
hide loissupershortpovslowvideo
hide loissuperfuckslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
$ loissuperfuckfastx = False
if loissuperfuckslowx == False:
    lp "You're fucking me sssoo good!"
    $ loissuperfuckslowx = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen loissupershortslowx()
screen loissupershortslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVSlowx")

label LoisSuperShortFastx:
$ loissuperharderx = False
window hide
show loissupershortfastvideo behind loissupershortslowvideo
show loissupershortfastvideo behind loissupershortpovfastvideo
show loissupershortfastvideo behind loissuperfuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissupershortslowvideo
hide loissupershortpovfastvideo
hide loissuperfuckfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
$ loissuperfuckslowx = False
if loissuperfuckfastx == False:
    lp "He's stretching my cunt so much! If only Clark Kunt had a huge cock like that..."
    $ loissuperfuckfastx = True
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen loissupershortfastx()
screen loissupershortfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVFastx")

label LoisSuperShortPOVSlowx:
$ loissuperharderx = False
window hide
show loissupershortpovslowvideo behind loissupershortslowvideo
show loissupershortpovslowvideo behind loissupershortpovfastvideo
show loissupershortpovslowvideo behind loissuperfuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissupershortslowvideo
hide loissupershortpovfastvideo
hide loissuperfuckpovslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
$ loissuperfuckfastx = False
if loissuperfuckslowx == False:
    lp "You're fucking me sssoo good!"
    $ loissuperfuckslowx = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loissupershortpovslowx()
screen loissupershortpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortSlowx")

label LoisSuperShortPOVFastx:
$ loissuperharderx = False
window hide
show loissupershortpovfastvideo behind loissupershortpovslowvideo
show loissupershortpovfastvideo behind loissupershortfastvideo
show loissupershortpovfastvideo behind loissuperfuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissupershortpovslowvideo
hide loissupershortfastvideo
hide loissuperfuckpovfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
$ loissuperfuckslowx = False
if loissuperfuckfastx == False:
    lp "He's stretching my cunt so much! If only Clark Kunt had a huge cock like that..."
    $ loissuperfuckfastx = True
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loissupershortpovfastx()
screen loissupershortpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortFastx")

label LoisSuperFuckSlowx:
if loissuperharderx == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharderx = True        
window hide
show loissuperfuckslowvideo behind loissuperfuckfastvideo
show loissuperfuckslowvideo behind loissuperfuckpovslowvideo
show loissuperfuckslowvideo behind loissupershortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissuperfuckfastvideo
hide loissuperfuckpovslowvideo
hide loissupershortslowvideo
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
call screen loissuperfuckx()
screen loissuperfuckx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEndx")

label LoisSuperFuckFastx:
if loissuperharderx == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharderx = True        
window hide
show loissuperfuckfastvideo behind loissuperfuckslowvideo
show loissuperfuckfastvideo behind loissuperfuckpovfastvideo
show loissuperfuckfastvideo behind loissupershortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissuperfuckslowvideo
hide loissuperfuckpovfastvideo
hide loissupershortfastvideo
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
call screen loissuperfuckfastx()
screen loissuperfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEndx")

label LoisSuperFuckPOVSlowx:
if loissuperharderx == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharderx = True        
window hide
show loissuperfuckpovslowvideo behind loissuperfuckslowvideo
show loissuperfuckpovslowvideo behind loissuperfuckpovfastvideo
show loissuperfuckpovslowvideo behind loissupershortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissuperfuckslowvideo
hide loissuperfuckpovfastvideo
hide loissupershortpovslowvideo
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
call screen loissuperfuckpovslowx()
screen loissuperfuckpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEndx")

label LoisSuperFuckPOVFastx:
if loissuperharderx == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharderx = True        
window hide
show loissuperfuckpovfastvideo behind loissuperfuckpovslowvideo
show loissuperfuckpovfastvideo behind loissuperfuckfastvideo
show loissuperfuckpovfastvideo behind loissupershortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissuperfuckpovslowvideo
hide loissuperfuckfastvideo
hide loissupershortpovfastvideo
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
call screen loissuperfuckpovfastx()
screen loissuperfuckpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEndx")

label LoisSuperFuckCumEndx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
mc "I'm gonna pump you full of cum soon, Lois!"
lp "Do it, STUD! Fill me up till I'm bloated with your hot spunk and I BELONG TO YOU!"
stop channel1
scene loissupercum01 with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "HERE I GO! AAAH!"
window hide
with hpunch
mc "Have a good look, Superman, while I BREED Lois Pane!"
scene loissupercum02 with dissolve
sm "This is... horrible, she seems to be in such pain!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
lp "No I'm not, I'm CU....MMMMIIIING! AAAH!"
scene loissupercum03 with dissolve
mc "Looks like my huge dick is stuck in there, gonna need your help a little..."
window hide
with hpunch
lp "I've never been pumped so FULL of warm nutsauce in my life, this is so GOO-OOD!"
scene loissupercum04 with dissolve
mc "You're gonna need to pull harder... I'm still blowing and Lois is getting bloated real quick!"
window hide
with fastflash
sm "I... I'm trying..."
scene loissupercum05 with dissolve
stop channel1
play sound "v041/plop.mp3"
mc "AAAH, that's better, FUCK!"
window hide
with hpunch
sm "Yuck, you're still blasting this weird white stuff!"
scene loissupercum06 with dissolve
play sound "sounds/moan02.mp3"
lp "Cover my body in it, I LOVE IT, I CRAVE YOUR YOUNG SPUNK!"
window hide
with fastflash
mc "Will do, Lois! Oh Fuck, I'm in HEAVENS, AAAH!"
scene loissupercum07 with dissolve
stop channel2
play sound "sounds/panting.mp3"
mc "Damn it... I came so much..."
lp "Mmmh, look at that huge dollop of sperm dangling from his engorged tip, there's more cum in that single drop than a normal man could produce in a week!"
scene loissupercum08 with dissolve
play sound "sounds/slurp.mp3"
lp "And he's TOTALLY covered me with OUNCES of his sweet young semen... It's so tasty..."
sm "Is it?..."
play sound "sounds/lick02.mp3"
lp "Ooh yeah, you want to taste it too, Superman?"
sm "I..."
scene loissupercum09 with dissolve
lp "Go on, have a lick, it might give you enough testosterone to grow you a dicklet one day..."
play sound "sounds/lick01.ogg"
mc "I doubt it but it's worth a try..."
scene loissupercum10 with dissolve
mc "This is how you get the girls, Superman, got it?"
stop music
stop channel1
jump LoisGallery