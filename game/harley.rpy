label HarleyPlace:
play music "sounds/dark.mp3"
if period == 1:
    scene harleyplace01night with fade
    mc "Oh, it's empty. Harley Quiff is probably raping someone somewhere. But since I'm not concerned about petty crime, I don't care and I'll go home to sleep soundly..."
    jump Main
scene harleyplace01 with fade
mc "Ms Quiff?"
window hide
show harley01 with moveinright
voice "harley/lair01"
hq "Dontcha knock before entering a lady’s boudoir?"
mc "Err, this doesn't look like a boudoir."
hide harley01
show harley02
with fastdissolve
if sawharley:
    voice "harley/lair02"
    hq "Oh, lookee here, it's [hero] again! You came back for more of ME? You must be OUT OF YOUR MIND!"
    mc "Well, I still have to check on you from time to time..."
    hide harley02
    show harley04
    with fastdissolve
    voice "harley/lair03"
    hq "Check on me??? I DO have a pulse, you know?" 
    mc "Yeah, I meant..."
if sawharley == False:
    voice "harley/lair04"
    hq "Oh, lookee here, it's [hero]! He probably thinks I'm a NAUGHTY girl. Isn't that right, Puddin?"
    mc "I've been told you are indeed completely insane."
    hide harley02
    show harley03
    with fastdissolve
    voice "harley/lair05"
    hq "How rude!"
    mc "And to check whether you have committed any serious SEX CRIME."
    hide harley03
    show harley04
    with fastdissolve
    voice "harley/lair06"
    hq "Me? I'm known to be quite VEXING, I'm just forewarning you..."  
    mc "Just doing my job."
hide harley04
show harley01
with fastdissolve
voice "harley/lair07"
hq "Step into my office, sweetie... There's a nice comfy chair over there. Let's talk about this rapey thing."
if sawharley:
    mc "Fine, I'm STILL not scared of you! Even after what happened last time..."
if sawharley == False:
    mc "Alright, but only because I'm a SUPERHERO and I'm NOT SCARED OF YOU!"
voice "harley/lair08"
hq "I'll powder myself for ya, puddin'... Don't go anywhere!"

stop music
play music "sounds/sexy04.mp3"
scene harleyplace02 with fade
mc "Where is she?..."
window hide
show harleybikini01small with moveinright
voice "harley/lair09"
hq "Here I am, it's just ssssooo hot in here, dontcha think?"
scene harleyplace03 blurred:
    zoom 2.0 xoffset -400 yoffset -980
show harleybikini01:
    xoffset 0 yoffset -1080
show harleyplace03 blurred at poolbackgroundup
show harleybikini01 at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True')
pause        
voice "harley/lair10"
hq "That's why I'm wearing this skimpy bikini, Puddin'..."
mc "I see... I feel hot too suddenly."
window hide
hide harleybikini01
show harleyplace03 blurred:
    zoom 1.8 xoffset -450 yoffset 0
show harleybikini02:
    zoom 1.0 xoffset 100 yoffset 0
show harleyplace03 blurred at harleybackgrounddown
show harleybikini02 at widowbackfulldown
with dissolve
$ renpy.pause(4.0, hard='True')
pause
voice "harley/lair11"
hq "Do you know what all these ticks mean?"
mc "Err, no, what do they mean?"
voice "harley/lair12"
hq "I don't know either, isn't that just CRAZY?"
window hide
scene harleyplace03 blurred:
    zoom 2.0 xoffset -400 yoffset -980
show harleybikini03:
    xoffset 0 yoffset -1080
window hide
show harleyplace03 blurred at poolbackgroundup
show harleybikini03 at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True')
pause        
mc "Ok, enough of this nonsense, what are you trying to do?"
scene harleyplace02 blurred
show harleybikini04
with dissolve
voice "harley/lair13"
hq "You thought I was just another bubble-headed blonde bimbo! Well, the joke’s on you, ’cause I’m not even a real blonde."
scene harleybikini05 with dissolve
mc "Wh... What are you doing?"
voice "harley/lair14"
hq "What's wrong, Puddin'? You don't like my big tits?"
mc "Err, no, I mean, yes, but..."
scene harleyplace02 blurred
show harleytitsvideo
with dissolve
pause
mc "I'm not supposed to get aroused by a Super-Villainess!..."
voice "harley/lair15"
hq "Give me a softie, I dare ya!"
mc "No! I must resis..."
play sound "sounds/buzz.mp3"
scene harleyelectric with hpunch
mc "What the hell, what is this?"
voice "harley/lair16"
hq "This thing is just ELECTRIC! Y'know, [hero]? I always thought there was a spark between us..."
play sound "sounds/buzz.mp3"
scene harleyelectric with hpunch
mc "Hey, you crazy bitch, stop this, I don't have Super-Resistance to electric shock yet!"
voice "harley/lair17"
hq "And you have Super-Resistance to big fat titties? Cos I'm taking this top off..."
scene harleyplace02 blurred
show harleybikini06
with dissolve
voice "harley/lair18"
hq "Huh? What was that? I should rape [hero] and escape?"
mc "What? I didn't say that!"
voice "harley/lair19"
hq "Sorry. The Voices. In my head."
mc "The voices in your head are CRAZY!"
hide harleybikini06
show harleybikini07
with fastdissolve
voice "harley/lair19b"
hq "I’m kidding! Jeez! That’s not what they really said."
hide harleybikini07
show harleybikini08
with fastdissolve
voice "harley/lair20"
hq "I don't need to... ESCAPE!"
voice "harley/lair21"
hq "Now come on, Puddin', I can see your monster hero cock sticking out... Begging for RELEASE! And then maybe, I'll release YOU!"
scene harleyassbackground blurred
show harleyprefuck01
with dissolve
voice "harley/lair22"
hq "I feel your dong GROWING between my ass cheeks. I'm guessing this is a sign."
mc "A sign of what?"
voice "harley/lair23"
hq "A sign you're ready to stick your superhero pud in my ASS!"
stop music
play channel2 "sounds/crazytrain.mp3"
voice "harley/lair24"
hq "Let's start slow and then bring up the pace to INSANE speeds!"
jump HarleyBikiniFuckb

label HarleyBikiniFuck:
voice "harley/lair25"
hq "First stop! Choo-choo! All sane people disembark!"
label HarleyBikiniFuckb:
stop channel1
play channel1 "sounds/womansex02.mp3"
scene harleysidebackground blurred
show harleysidevideo 
with dissolve
show zoomicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen harleysidescreen()
screen harleysidescreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoomb")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckFast")

label HarleyBikiniFuckZoom:
voice "harley/lair25"
hq "First stop! Choo-choo! All sane people disembark!"
label HarleyBikiniFuckZoomb:
stop channel1
play channel1 "sounds/womansex02.mp3"
scene harleyassbackground blurred at harleyassbackgroundpos01
show harleyassvideo 
with dissolve
show sceneicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen harleyassscreen()
screen harleyassscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckb")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckZoomFast")

label HarleyBikiniFuckFast:
voice "harley/lair26"
hq "All aboard, ha ha ha, this is the express train to CRAZYTOWN!"
label HarleyBikiniFuckFastb:
stop channel1
play channel1 "sounds/womansex03.mp3"
scene harleysidebackground blurred
show harleysidefastvideo 
with dissolve
show nexticon:
    xpos 1700 ypos 1020    
show zoomicon:
     xpos 50 ypos 500
show insanelyfast:
     xpos 1600 ypos 500
call screen harleysidefastscreen()
screen harleysidefastscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoomFastb")
    button:
        xpos 1600
        ypos 500
        xysize(220, 60)        
        action Jump ("HarleyBikiniFuckFaster")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEnd")

label HarleyBikiniFuckZoomFast:
voice "harley/lair26"
hq "All aboard, ha ha ha, this is the express train to CRAZYTOWN!"
label HarleyBikiniFuckZoomFastb:
stop channel1
play channel1 "sounds/womansex03.mp3"
scene harleyassbackground blurred at harleyassbackgroundpos02
show harleyassfastvideo 
with dissolve
show nexticon:
    xpos 1700 ypos 1020    
show sceneicon:
     xpos 50 ypos 500
show insanelyfast:
     xpos 1600 ypos 500
call screen harleyassfastscreen()
screen harleyassfastscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckFastb")
    button:
        xpos 1600
        ypos  500
        xysize(220, 60)        
        action Jump ("HarleyBikiniFuckZoomFaster")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEnd")
            
label HarleyBikiniFuckFaster:
voice "harley/lair27"
hq "Don't you move Puddin', I'm going off the rails on the crazy train!"
label HarleyBikiniFuckFasterb:
stop channel1
play channel1 "sounds/womansex04.mp3"
scene harleysidebackground blurred
show harleysideveryvideo 
with dissolve
show nexticon:
    xpos 1700 ypos 1020    
show zoomicon:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen harleysideveryscreen()
screen harleysideveryscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoomFasterb")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuck")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEnd")

label HarleyBikiniFuckZoomFaster:
voice "harley/lair27"
hq "Don't you move Puddin', I'm going off the rails on the crazy train!"
label HarleyBikiniFuckZoomFasterb:
stop channel1
play channel1 "sounds/womansex04.mp3"
scene harleyassbackground blurred at harleyassbackgroundpos03
show harleyassveryvideo 
with dissolve
show nexticon:
    xpos 1700 ypos 1020    
show sceneicon:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen harleyassveryscreen()
screen harleyassveryscreen():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckFasterb")
    button:
        xpos 1700
        ypos  500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckZoom")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEnd")
        
label HarleyBikiniFuckEnd:
$ sawharley = True
voice "harley/lair28"
hq "You're driving me insane, Puddin'! I'm vaginally numb, what's to blame? YOU and your MONSTERCOCK!"
mc "It can't be my fault, you're RAPING me! You're the SUPER-VILLAIN!"
voice "harley/lair29"
hq "Shush, Puddin, learn how to love and forget how to hate! Give me your love DEEP INSIDE. NOW!"
stop channel1
stop channel2
scene harleyassbackground blurred
show harleybikinicum01
with dissolve
play sound "sounds/splooge02.mp3"
play channel1 "sounds/boyorgasm01.mp3"
mc "DAMN, FUCK, AAAHHHHH!"
window hide
with fastflash
voice "harley/lair30"
hq "You gotta listen to my words, fuck ME, YEAH!"
play sound "sounds/splooge01.mp3"
hide harleybikinicum01
show harleybikinicum02
with fastdissolve
if age >= 20:
    voice "harley/lair31a"
    hq "Give me your sweet seed, Puddin'! I ain't never been filled up by such a YOUNG STUD!"
if age >= 18 and age <= 19:
    voice "harley/lair31b"
    hq "Give me your sweet seed, Puddin'! I ain't never been filled up by such a YOUNG TEENAGE STUD!"
window hide
with fastflash
hide harleybikinicum02
show harleybikinicum01
with fastdissolve
voice "harley/lair34"
hq "Not enough, I want MORE!"
play sound "sounds/splooge01.mp3"
hide harleybikinicum01
show harleybikinicum02
with fastdissolve
voice "harley/lair35"
hq "and MORE!"
hide harleybikinicum02
show harleybikinicum01
with fastdissolve
mc "AAAH!"
hide harleybikinicum01
show harleybikinicum02
with fastdissolve
play sound "sounds/splooge01.mp3"
voice "harley/lair36"
hq "and even MORE!"
window hide
with fastflash
voice "harley/lair37"
hq "...MUCH MORE!"
scene harleycumbackground
show harleybikinicum03
with dissolve
voice "harley/lair38"
hq "You're getting there Puddin'!"
scene harleyassbackground blurred
show harleybikinicum04
with dissolve
play sound "sounds/splooge02.mp3"
voice "harley/lair39"
hq "Mama gonna paint this office with cum!"
window hide
with fastflash
mc "Godam, I can't..."
scene harleycumbackground
show harleybikinicum05
with dissolve
play sound "sounds/splooge01.mp3"
voice "harley/lair40"
hq "Sure you can, and even if you can't, you WILL! HA HA HA!"
play sound "sounds/splooge02.mp3"
scene harleysidebackground blurred
show harleybikinicum06
with dissolve
voice "harley/lair41"
hq "Oooh, I can feel it, I hear the voices in my vagina! Isn't that just CRAZY?"
window hide
with fastflash
play sound "sounds/splooge02.mp3"
mc "You're... DRAINING MY NUTS!"
window hide
with fastflash
play sound "sounds/splooge01.mp3"
voice "harley/lair42"
hq "That's the idea, silly!"
mc "I can't come THAT much!"
voice "harley/lair43"
hq "Too late, you JUST DID! And it's POURING cum out of my backhole!" 
stop channel1
play sound "sounds/panting.mp3"
scene harleycumbackground
show harleybikinicum07
with dissolve
voice "harley/lair44"
hq "I was thinking of installing a cum jacuzzi in my boudoir and I'm well on my way now! Thanks, Puddin'!"
mc "Aaarhh..."
scene harleyplace02
show harleybikinicum08
with dissolve
voice "harley/lair45"
hq "I'm off to buy myself a new buttplug. Still have plenty inside and I don't want to lose my DINNER! HA HA HA!"
jump Main

