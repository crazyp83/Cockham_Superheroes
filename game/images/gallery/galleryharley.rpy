label HarleyGallery:
stop channel3
play channel3 "sounds/sexy08.mp3"
scene harleybackground
show harleymaingallery at gallerypos01 with moveinleft
call screen galleryharley()
screen galleryharley():
    text "{font=Gui/Heroes Legend.ttf}Naughty Harley Quiff{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryharley"), Jump ("MainGallery02")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryharley"), Jump ("HarleyGalleryAnim")]
    
    if renpy.seen_image("harleybikini01"):
        imagebutton:
            focus_mask True
            idle "gallery/harleygallery01.png" xpos 400 ypos 100
            hover "gallery/harleygallery01.png"
            action Jump ("HarleyGallery01")
    text "{font=Gui/Heroes Legend.ttf}Anal Rape{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("harleybikini01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("HarleyGallery01hint")

    if renpy.seen_image("harleystore07"):
        imagebutton:
            focus_mask True
            idle "gallery/harleygallery02.png" xpos 750 ypos 100
            hover "gallery/harleygallery02.png"
            action Jump ("HarleyGallery02")
    text "{font=Gui/Heroes Legend.ttf}Lingerie Store{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("harleystore07") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("HarleyGallery")

    if renpy.seen_image("harleycell01"):
        imagebutton:
            focus_mask True
            idle "gallery/harleygallery03.png" xpos 1100 ypos 100
            hover "gallery/harleygallery03.png"
            action Jump ("HarleyGallery03")
    text "{font=Gui/Heroes Legend.ttf}Jail Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("harleycell01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("HarleyGallery")

label HarleyGallery01hint:
show harleymaingallery at gallerypos01
show harleygallery01 at posgalleryhintpic
show harleygalleryhint01 at posgalleryhint
pause
hide harleygalleryhint01
hide harleygallery01
call screen galleryharley()

label HarleyGalleryAnim:
call screen screenanimharley()
screen screenanimharley():
    modal True
    add "gallery/harleybackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "harleyanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "harleyanimbik" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "harleyanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimharley"), SetVariable ("animcount", 1), Jump ("HarleyGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Harley Quiff{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 27{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft7{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34DD-23-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Male Rape{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Female Rape{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    text "{font=Gui/Heroes Legend.ttf}Cum Enemas{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink04
    add "gallery/harleyanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimharley")]
    add "gallery/harleyanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimharley")]
    add "gallery/harleyanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimharley")]
            
label HarleyGallery01:
stop channel3
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
hq "I feel your dong GROWING between my ass cheeks. I'm guessing this a sign."
mc "A sign of what?"
voice "harley/lair23"
hq "A sign you're ready to stick your superhero pud in my ASS!"
stop music
play channel2 "sounds/crazytrain.mp3"
voice "harley/lair24"
hq "Let's start slow and then bring up the pace to INSANE speeds!"
jump HarleyBikiniFuckbx

label HarleyBikiniFuckx:
voice "harley/lair25"
hq "First stop! Choo-choo! All sane people disembark!"
label HarleyBikiniFuckbx:
stop channel1
play channel1 "sounds/womansex02.mp3"
scene harleysidebackground blurred
show harleysidevideo 
with dissolve
show zoomicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen harleysidescreenx()
screen harleysidescreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoombx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckFastx")

label HarleyBikiniFuckZoomx:
voice "harley/lair25"
hq "First stop! Choo-choo! All sane people disembark!"
label HarleyBikiniFuckZoombx:
stop channel1
play channel1 "sounds/womansex02.mp3"
scene harleyassbackground blurred at harleyassbackgroundpos01
show harleyassvideo 
with dissolve
show sceneicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen harleyassscreenx()
screen harleyassscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckbx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckZoomFastx")

label HarleyBikiniFuckFastx:
voice "harley/lair26"
hq "All aboard, ha ha ha, this is the express train to CRAZYTOWN!"
label HarleyBikiniFuckFastbx:
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
call screen harleysidefastscreenx()
screen harleysidefastscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoomFastbx")
    button:
        xpos 1600
        ypos 500
        xysize(220, 60)        
        action Jump ("HarleyBikiniFuckFasterx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEndx")

label HarleyBikiniFuckZoomFastx:
voice "harley/lair26"
hq "All aboard, ha ha ha, this is the express train to CRAZYTOWN!"
label HarleyBikiniFuckZoomFastbx:
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
call screen harleyassfastscreenx()
screen harleyassfastscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckFastbx")
    button:
        xpos 1600
        ypos  500
        xysize(220, 60)        
        action Jump ("HarleyBikiniFuckZoomFasterx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEndx")
            
label HarleyBikiniFuckFasterx:
voice "harley/lair27"
hq "Don't you move Puddin', I'm going off the rails on the crazy train!"
label HarleyBikiniFuckFasterbx:
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
call screen harleysideveryscreenx()
screen harleysideveryscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("HarleyBikiniFuckZoomFasterbx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEndx")

label HarleyBikiniFuckZoomFasterx:
voice "harley/lair27"
hq "Don't you move Puddin', I'm going off the rails on the crazy train!"
label HarleyBikiniFuckZoomFasterbx:
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
call screen harleyassveryscreenx()
screen harleyassveryscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("HarleyBikiniFuckFasterbx")
    button:
        xpos 1700
        ypos  500
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckZoomx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBikiniFuckEndx")
        
label HarleyBikiniFuckEndx:
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
hq "I was thinking of installing a cum jacuzzi in my boudoir and I'm well on my way now! Thank, Puddin'!"
mc "Aaarhh..."
scene harleyplace02
show harleybikinicum08
with dissolve
voice "harley/lair45"
hq "I'm off to buy myself a new buttplug. Still have plenty inside and I don't want to lose my DINNER! HA HA HA!"
stop music
stop channel3
stop channel1
stop channel2
jump HarleyGallery

label HarleyGallery02:
stop music
stop channel3
scene harleystore04 with dissolve
hq "I don't know... It' just not CRAZY enough for me!"
jo "It's PRACTICAL. How are we supposed to blend into a crowd?"
scene harleystore05 with dissolve
hq "Number 1: No one is like me. Have you seen your face in a mirror recently? You wouldn't even fit in a freak circus, puddin!"
scene harleystore06 with dissolve
hq "Na, I want something else, so get me something SEXY you stupid bitch!"
ka "Yy..yes ma'am, of course!"
scene harleystore07 with dissolve
mc "Kate is clearly being FORCED to comply at batpoint. But I need to see more before intervening... Also, I want to see what sexy outfit Harley will be wearing next."
play music "sounds/sexy08.mp3"
scene harleystore08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "Alright! Let's wait for her to pose in that fishnet bodysuit..."
scene harleystore09 :
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
$ renpy.pause(4.0, hard='True')
hq "Now that's better, whaddya reckon, puddin?"
jo "Err..."
scene harleystore10:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
with dissolve
$ renpy.pause(4.0, hard='True')
jo "You want to walk down the street like that? That's nuts!"
hq "Why not, you're walking down the street looking like a supervillain clown freak!"
jo "Hey!"
hq "Oh, boo hoo."
scene harleystore11 with dissolve
hq "I'm getting real horny wearing this bodysuit."
jo "Yeah, I'm getting horny too, my belov..."
scene harleystore12 with dissolve
hq "I ain't talking to you, Mr J.! I'm talking to that brunette harlot over there. Why dontya come over here and taste my cunt, you sweet thing?"
ka "But... I'm not a lesbian, Ms Quiff!"
hq "That's okay, cos I AM! So come over here and put that face where it can't talk no more. Right between my legs!"
scene harleystore13 with dissolve
jo "You'd better do as you're told, she's crazy and I have a gun!"
scene harleystore14 with dissolve
hq "Love your perfume, what is that? The scent of Death?"
scene harleystore15 with dissolve
hq "My pussy is welcoming you with open legs!"
scene harleystore16 with dissolve
hq "Go on, have a good lick, twist that tongue in there!"
scene harleystore17 with dissolve
play sound "sounds/moan05.mp3"
hq "Mmh, yes, just like that, mamma's gonna paint your face with white juice!"
scene harleystore18 with dissolve
play sound "sounds/moan05.mp3"
hq "Sweetie, you're getting mommy's bazookas all tingly!"
scene harleystore12 with dissolve
hq "That was good, now it's my turn to return the favor. So get naked, my sweet girl, cos Mamma has a SURPRISE for you!"
scene harleystore19 with dissolve
hq "Wow, what's this? I knew I was carrying some HEAVY WEAPONRY today!"
scene harleystore20 with dissolve
ka "Wh.. What are you going to do with this???"
jo "It's getting steamy in here, I'll just, like, polish my gun real quick..."
hq "Do it quietly puddin, I can hear your voices inside my head!"
scene harleystore21 with dissolve
play sound "sounds/lick02.mp3"
hq "Isn't it tasty, darlin'? Hang on, I'm the one choking on it, silly me!"
hq "Just come over here and I'll let your backdoor have a real good taste of it too!"
scene harleystore22 with dissolve
ka "I've never had something this huge inside my hole, please be gentle, Ms Quiff!"
hq "It's not that big, I've had bigger, so don't ya worry! Your ass looks ready to swallow it whole!"
ka "But, no, plea..."
scene harleystore23 with dissolve
play sound "sounds/moan05.mp3"
ka "AAAH!"
hq "Tada! I always wanted to be a magician and make stuff disappear inside holes. But I'm stuck with a clown..."
jo "Not clown, Joker!"
scene harleystore24 with dissolve
play sound "sounds/moan03.mp3"
hq "How deep is that rabid hole, only one way to find out!"
window hide
play channel2 "sounds/moan04.ogg"
show harleystoredildo with dissolve
pause
stop channel2
scene harleystore24 with fastdissolve
hq "How about we have a DEEPER look at that gaping hole of yours?"
ka "No, please Ms Quiff, this is too deep already, I can't take that much!"
scene harleystore25 with dissolve
play sound "sounds/moan06.ogg"
ka "AAAAAHHHH!"
hq "I’m sorry girl, I’m just a terrible person I guess."
scene harleystore26 with dissolve
play sound "sounds/moan02.mp3"
hq "Well, look at that, your ass looks happier than your face!"
scene harleystore27 with dissolve
hq "I wonder if it'll be THRILLED if I go EVEN DEEPER?"
stop sound
ka "NO, I BEG YOU!"
mc "Maybe I should do something now. Even if I am quite intrigued to see how deep she can take it..."
scene harleystore28 with dissolve
stop music
play music "sounds/dark.mp3"
play sound "sounds/moan04.ogg"
mc "Drop that dildo! And that gun!"
hq "What a party-pooper, boo-hoo!"
scene harleystore29 with dissolve
jo "What, you mean my gun? The one pointed right at your head?"
mc "Err... How did you...?"
scene harleystore30 with dissolve
jo "You're not the only one with Super-Senses, [hero]! I KNEW you were spying on us all along. Now the Joker's on you!"
hq "Don't you just love the CRAZINESS of it all!"
scene harleystore31 with dissolve
jo "I think you've been a very NAUGHTY boy."
scene harleystore30 with dissolve
jo "What kind of superhero RAPES innocent store managers?"
mc "What, I didn't do any such thing!"
scene harleystore31 with dissolve
jo "But what about that picture of you? Harley, put some handcuffs on the young fellow."
scene harleystore32 with dissolve
mc "What picture?"
jo "Why so serious, you'll see."
scene harleystore33 with dissolve
jo "Now you just stand over there while we escape, and don't you move an inch, or I put a bullet in your DONG!"
scene harleystore34 with dissolve
hq "Don't smile puddin', it's for the camera!"
play sound "sounds/flash.mp3"
window hide
with fastflash
jo "I used to think my life was a tragedy, but now I realize it's a comedy! Ha ha ha!"
stop channel1
stop music
jump HarleyGallery

label HarleyGallery03:
stop channel3
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
play music "sounds/sexy08.mp3" volume 0.5
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

$ harleyblowslowx = False

label HarleyBlowSlowx:
$ harleyblowfastx = False
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
if harleyblowslowx == False:
    $ harleyblowslowx = True
    mc "It's crazy how big your mouth is when you think about it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen harleyblowslowx()
screen harleyblowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowPOVSlowx")

label HarleyBlowFastx:
$ harleyblowslowx = False
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
if harleyblowfastx == False:
    $ harleyblowfastx = True    
    mc "Yeah, do it faster. But don't bite!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen harleyblowfastx()
screen harleyblowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowPOVFastx")

label HarleyBlowPOVSlowx:
$ harleyblowfastx = False
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
if harleyblowslowx == False:
    $ harleyblowslowx = True
    mc "It's crazy how big your mouth is when you think about it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleyblowpovfuckslowx()
screen harleyblowpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowSlowx")

label HarleyBlowPOVFastx:
$ harleyblowslowx = False
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
if harleyblowfastx == False:
    $ harleyblowfastx = True    
    mc "Yeah, do it faster. But don't bite!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleyblowpovfuckfastx()
screen harleyblowpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyBlowPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyBlowFastx")

label HarleyBlowEndx:
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
hq "...Rape me reall good? But you'll have to open the door to catch me, Mr Rapist!"
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
$ harleypoundslowx = False

label HarleyPoundSlowx:
$ harleypoundfastx = False
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
if harleypoundslowx == False:
    $ harleypoundslowx = True
    mc "Damn you... * puff * I'm going to fuck you silly!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen harleypoundslowx()
screen harleypoundslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundPOVSlowx")

label HarleyPoundFastx:
$ harleypoundslowx = False
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
if harleypoundfastx == False:
    $ harleypoundfastx = True    
    voice "harley/jail36"
    hq "Come on, bang me harder, give it all you've got, Mr Rapist!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen harleypoundfastx()
screen harleypoundfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundPOVFastx")

label HarleyPoundPOVSlowx:
$ harleypoundfastx = False
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
if harleypoundslowx == False:
    $ harleypoundslowx = True
    hq "Do you like my little innocent sex-crazed hole, Mr Rapist?"
    mc "Damn you... * puff * I'm going to fuck you silly!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleypoundfrontfuckslowx()
screen harleypoundfrontfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundSlowx")

label HarleyPoundPOVFastx:
$ harleypoundslowx = False
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
if harleypoundfastx == False:
    $ harleypoundfastx = True    
    voice "harley/jail36"
    hq "Come on, bang me harder, give it all you've got, Mr Rapist!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen harleypoundfrontfuckfastx()
screen harleypoundfrontfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HarleyPoundPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HarleyPoundEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HarleyPoundFastx")

label HarleyPoundEndx:
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
stop channel1
stop music
jump HarleyGallery