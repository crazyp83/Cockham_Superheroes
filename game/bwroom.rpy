label BWRoomNight:
stop music
if d10locnight >= 4 and d10locnight <= 7 and mclevel02 == False:
    jump BWRoomNightWidow
if d10locnight >= 4 and d10locnight <= 5 and mclevel02 and quest06end and mission05end == False and premission05 == False:
    scene widowroomnight with fade
    show widowroom04 at centerleft with moveinright
    bw "What the hell are you doing in MY room?"
    mc "Err... I'm coming for some goo-ood ti..."
    hide widowroom04
    show widowroom02 at centerleft
    with fastdissolve
    bw "I'm DONE with YOU! You're just a PERVERT! You've been corrupted by Western porn decadence!"
    mc "Porn? What's that?"
    bw "Get out of my room, vile American Imperialist!"
    mc "* Gee, that was uncalled for! I'd better tell Captain MILF about this weird behavior... *"
    $ premission05 = True
    jump Main
if d10locnight >= 4 and d10locnight <= 5 and mclevel02 and (helpedwidow or mission05win) and quest07end and seennatalyawidow == False:
    $ seennatalyawidow = True
    jump NatalyaWidowRoom
if d10locnight >= 4 and d10locnight <= 5 and mclevel02 and (helpedwidow or mission05win):
    jump BWRoomNightBedLevel02
if ((d10locnight >= 6 and d10locnight <= 7) or helpedwidow == False) and mclevel02:
    jump BWMasturbationPre
scene widowroomnight with fade
mc "Not quite sure why I came here since the Black Widow is not around. Nice bedside lamp by the way."
jump MCRoomNight

label BWRoomNightWidow:
play channel1 "sounds/sexy04.mp3"
scene widowroomnight with fade
show widowroom01 at centerleft with moveinright
voice "widow/room01"
bw "I was expecting you... [hero]."
hide widowroom01
show widowroomeyeblink
with fastdissolve
menu:
    "Ooh? And why so?..." if widowpicked and sawpicked == False:
        $ sawpicked = True
        hide widowroomeyeblink
        show widowroom03 at centerleft
        with fastdissolve
        voice "widow/room02"
        bw "After that sumptuous titfuck I gave you, I thought you might come back for MORE... Was I right?"
        mc "Damn right you were right!"
        hide widowroom03
        show widowroomeyeblink
        with fastdissolve
        voice "widow/room03"
        bw "As a reward for your GOOD behavior, I have a show for you... Just watch."
        window hide
        hide widowroomeyeblink
        show widowroomnight blurred:
            subpixel True
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
            subpixel True
            zoom 1.0 xoffset 200 yoffset -1080    
        show widowroomnight blurred at widowfullbackzoombackground
        show widowroomfull at honokafullup
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause        
        voice "widow/room04"
        bw "How do I look in sexy black lace lingerie, [name]?"
        mc "Amazing. Your bod is just so fucking hot."
        window hide
        hide widowroomfull
        show widowroombackfull:
            subpixel True
            zoom 1.0 xoffset 300 yoffset 0    
        show widowroomnight blurred at widowbackfullbackzoombackground
        show widowroombackfull at widowbackfulldown
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause
        voice "widow/room05"
        bw "And you DEFINITELY agree that THIS booty is the MOST cock-hardening in Cockham City, right?"
        mc "Yes it is, and my cock is indeed hardening right now, so let's FUCK, WOO-HOO!"
        scene widowroomnight
        show widowroom03 at centerleft
        with dissolve
        voice "widow/room06"
        bw "You don't seem ready just yet. You *might* be ready if you come back another time."
        mc "So I came here for nothing?"
        hide widowroom03
        show widowroom04 at centerleft
        with fastdissolve
        voice "widow/room07"
        bw "No... You saw me in sexy lingerie. You got your reward and you should be grateful."
        mc "Sure, sure. But now I have blue balls."    
        hide widowroom04
        show widowroomeyeblink
        with fastdissolve
        voice "widow/room08"
        bw "Not MY problem. Have SWEET dreams, [name]! I know I will, after I play with my 12-inch dildo..."
        jump Main
    "Ooh? And why so?..." if frostpicked and sawpicked == False:
        $ sawpicked = True        
        hide widowroomeyeblink
        show widowroom02 at centerleft
        with fastdissolve
        voice "widow/room09"
        bw "To show you how WRONG you were in picking that EVIL White Queen!"
        mc "I never said you WEREN'T SUPER-HOT..."
        hide widowroom02
        show widowroom04 at centerleft
        with fastdissolve        
        voice "widow/room10"
        bw "Don't try and snivel out of your terrible decision, I'm going to CHANGE IT tonight!"
        mc "Okay, let's see how you accomplish that, Natasha..."
        hide widowroom04
        show widowroomeyeblink
        with fastdissolve                
        bw "Just watch..."
        window hide
        hide widowroomeyeblink
        show widowroomnight blurred:
            subpixel True
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
            subpixel True
            zoom 1.0 xoffset 200 yoffset -1080    
        show widowroomnight blurred at widowfullbackzoombackground
        show widowroomfull at honokafullup
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause        
        voice "widow/room11"
        bw "Can you HONESTLY claim THIS body isn't HOTTER than Emma Frost's?"
        mc "Well, err... Let's see more."
        window hide
        hide widowroomfull
        show widowroombackfull:
            subpixel True
            zoom 1.0 xoffset 300 yoffset 0    
        show widowroomnight blurred at widowbackfullbackzoombackground
        show widowroombackfull at widowbackfulldown
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause
        voice "widow/room12"
        bw "And that THIS booty isn't the MOST cock-hardening in Cockham City?"
        mc "Alright, alright, I admit I was wrong! You're WAY HOTTER than Emma Frost! So now let's FUCK, WOO-HOO!"
        scene widowroomnight
        show widowroom02 at centerleft
        with dissolve
        voice "widow/room15"
        bw "Who said I was going to let you fuck me?"
        mc "Err..."
        hide widowroom02
        show widowroomeyeblink
        with fastdissolve
        voice "widow/room14"
        bw "All I wanted was for you to recognize you were WRONG. And that's it."
        mc "That's it? So I came here for nothing?"
        hide widowroomeyeblink
        show widowroom04 at centerleft
        with fastdissolve
        voice "widow/room15"
        bw "No... You saw me in sexy lingerie. Didn't that get your cock hard at least?"
        mc "Sure, sure. But now I have blue balls."    
        hide widowroom04
        show widowroom03 at centerleft
        with fastdissolve
        voice "widow/room16"
        bw "Too bad... I've got a 12-inch dildo so I'll be fine. * wink *"
        mc "Damn it! * sigh *"
        jump Main
    "Ooh? And why so?..." if frostpicked == False and widowpicked == False and sawpicked == False:
        $ sawpicked = True        
        hide widowroomeyeblink
        show widowroom02 at centerleft
        with fastdissolve
        bw "To make it easier for you to pick ME in the future!"
        mc "I'm still undecided..."
        hide widowroom02
        show widowroom04 at centerleft
        with fastdissolve        
        bw "That's NOT how SUPERHEROES behave. So you're going to have to LEARN a few things, young boy!"
        mc "Okay, I'm all ears... and eyes..."
        hide widowroom04
        show widowroomeyeblink
        with fastdissolve                
        bw "Just watch..."
        window hide
        hide widowroomeyeblink
        show widowroomnight blurred:
            subpixel True
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
            subpixel True
            zoom 1.0 xoffset 200 yoffset -1080    
        show widowroomnight blurred at widowfullbackzoombackground
        show widowroomfull at honokafullup
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause        
        bw "Can you HONESTLY claim THIS body isn't HOTTER than Emma Frost's?"
        mc "Well, err... Let's see more."
        window hide
        hide widowroomfull
        show widowroombackfull:
            subpixel True
            zoom 1.0 xoffset 300 yoffset 0    
        show widowroomnight blurred at widowbackfullbackzoombackground
        show widowroombackfull at widowbackfulldown
        with dissolve
        $ renpy.pause(4.0, hard='True')
        pause
        bw "And that THIS booty isn't the MOST cock-hardening in Cockham City?"
        mc "Alright, alright, I admit I should have picked you! You're WAY HOTTER than Emma Frost! So now let's FUCK, WOO-HOO!"
        scene widowroomnight
        show widowroom02 at centerleft
        with dissolve
        bw "Who said I was going to let you fuck me?"
        mc "Err..."
        hide widowroom02
        show widowroomeyeblink
        with fastdissolve
        bw "All I wanted was for you to understand that you NEED to have the COURAGE of your CONVICTIONS. And that's it."
        mc "That's it? So I came here for nothing?"
        hide widowroomeyeblink
        show widowroom04 at centerleft
        with fastdissolve
        bw "No... You saw me in sexy lingerie. Didn't that get your cock hard at least?"
        mc "Sure, sure. But now I have blue balls."    
        hide widowroom04
        show widowroom03 at centerleft
        with fastdissolve
        bw "Too bad... I've got a 12-inch dildo so I'll be fine. * wink *"
        mc "Damn it! * sigh *"
        jump Main
    "And I wasn't expecting you.":
        hide widowroomeyeblink
        show widowroom02 at centerleft
        with fastdissolve
        voice "widow/room17"
        bw "You weren't expecting ME to be in MY room at night?"
        mc "No. I mean, yes, maybe. It could have been empty. But I guess it isn't."
        hide widowroom02
        show widowroom04 at centerleft
        with fastdissolve        
        voice "widow/room18"
        bw "Get out of MY room!"
        jump Main
    "I was thinking. Maybe I should boycott you.":
        hide widowroomeyeblink
        show widowroom04 at centerleft
        with fastdissolve
        bw "Why is that?"
        mc "Well, cos you're Russian, right?"
        hide widowroom04
        show widowroom02 at centerleft
        with fastdissolve        
        bw "I have no allegiance to Vladimir Pew-tin! Plus, the year is 1977 in case you didn't notice!"
        mc "Ok, fine. What about the dev, is HE Russian? Maybe I should boycott this game..."
        hide widowroom02
        show widowroom04 at centerleft
        with fastdissolve
        bw "No, the dev is NOT Russian. I repeat, the dev is NOT RUSSIAN. He's half-English, half-French."
        mc "Thanks for clearing that up. Now I feel better about playing this game and becoming a patron."
        jump Main
    "Are you going to tease me again?" if sawpicked and sawbmasturbation == False:
        hide widowroomeyeblink
        show widowroom03 at centerleft
        with fastdissolve
        voice "widow/room19"
        bw "You want to be teased?"
        mc "Well, to some extent, as long as we end up having some GOO-OOO-OOD times afterwards!"
        hide widowroom03
        show widowroom04 at centerleft
        with fastdissolve        
        voice "widow/room20"
        bw "You think I'm easy, hey? I'll show you something. Follow me to the edge of my bed."
        if mcsenses == 0:
            mc "Uh oh, I sense some extreme teasing. And I'm not even level 1 in Super-Senses."
        if mcsenses >= 1:
            mc "Uh oh, I sense some extreme teasing..."
        jump BWMasturbation
    "I'd like to watch you play with your dildo again." if sawbmasturbation:
        hide widowroomeyeblink
        show widowroom03 at centerleft
        with fastdissolve
        voice "widow/room21"
        bw "You want to be teased again? You know the rules..."
        mc "Yeah, NO TOUCHING."
        hide widowroom03
        show widowroom04 at centerleft
        with fastdissolve        
        voice "widow/room22"
        bw "That's right. NO TOUCHING. Follow me."
        if mcsenses == 0:
            mc "Uh oh, I sense some further extreme teasing. And I'm not even level 1 in Super-Senses."
        if mcsenses >= 1:
            mc "Uh oh, I sense some further extreme teasing..."
        jump BWMasturbation

label BWMasturbationPre:
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar
play channel1 "sounds/sexy03.mp3"
scene widowbed01 with fade
voice "widow/room30"
bw "There you are... I was waiting for you. Waiting to TEASE you... So just sit back and enjoy the show, [name]. And NO TOUCHING! Not even yourself..."
jump BWMasturbationPost
label BWMasturbation:
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar
$ sawbmasturbation = True
play channel1 "sounds/sexy03.mp3"
scene widowbed01 with fade
voice "widow/room31"
bw "Just sit back and enjoy the show, [name]. And NO TOUCHING! Not even yourself..."
label BWMasturbationPost:
scene widowbed02:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
voice "widow/room32"
bw "First, let me take these puppies out of that constraining bra..."
scene widowbed03 with dissolve
voice "widow/room33"
bw "I just LOVE playing with them. They're so ROUND and FIRM!"
mc "I'd like to play with them too, please!"
voice "widow/room34"
bw "No! I said NO TOUCHING!"
scene widowbed04 with dissolve
voice "widow/room35"
bw "Let me get more comfortable..."
scene widowbed05 with dissolve
voice "widow/room36"
bw "My pussy is starting to get quite wet... You want to see?"
mc "Yeah, see AND tou..."
voice "widow/room36b"
bw "NO TOUCHING!"
scene widowbed06 with dissolve
voice "widow/room37"
bw "You see my puffy labia? It's waiting for something BIG to enter it."
mc "Well, what a coincidence, I happen to hav..."
voice "widow/room38"
bw "Not YOUR cock!"
scene widowbed07 with dissolve
play sound "sounds/moan01.mp3"
voice "widow/room39"
bw "First, my expert fingers..."
scene widowbed08 with dissolve
play music "sounds/moan02.mp3"
voice "widow/room40"
bw "... stretching it delicately... Oooh!"
scene widowbed07 with dissolve
$ renpy.pause(0.5, hard=True)
scene widowbed08 with dissolve
$ renpy.pause(0.7, hard=True)
scene widowbed07 with dissolve
$ renpy.pause(0.5, hard=True)
scene widowbed08 with dissolve
$ renpy.pause(0.7, hard=True)
scene widowbed07 with dissolve
$ renpy.pause(0.5, hard=True)
scene widowbed08 with dissolve
$ renpy.pause(0.7, hard=True)
stop music
voice "widow/room41"
bw "Mmh, that was a nice little foreplay..."
mc "Before my HUGE COCK?"
voice "widow/room42"
bw "NO, you're NOT GETTING ANY TONIGHT!"
if widowpoolassfuck == False:
    mc "But..."
if widowpoolassfuck:
    mc "But... You already took my cock up the ass!"
scene widowbed09 with dissolve
if widowpoolassfuck == False:
    voice "widow/room43"
    bw "You thought I was going to be the easy girl here, hey?"
    voice "widow/room44"
    bw "Just because my dossier says that I'm a cock-slut doesn't mean that I need YOU!"
if widowpoolassfuck:
    voice "widow/room45"
    bw "Just because I took your alpha-dong up this ass, you thought I was going to be an easy girl here, hey?"
    voice "widow/room46"
    bw "My PUSSY is reserved for the BEST. And you're NOT the best. Yet."
scene widowbed10 with dissolve
if widowpoolassfuck == False:
    voice "widow/room47"
    bw "After all, I have this BIG, LONG, thing to play with anytime I want..."
if widowpoolassfuck:
    voice "widow/room48"
    bw "Right now, the BEST thing is this BIG, LONG, thing which I can play with anytime I want..."
scene widowbed11 with dissolve
play sound "sounds/lick01.ogg"
mc "My cock is bigger and REAL! Warm to the touch, not like some fake plastic dildo..."
voice "widow/room49"
bw "I KNOW your perfect boymeat is MUCH BIGGER than my dildo, but..."
scene widowbed12 with dissolve
play sound "sounds/lick02.mp3"
voice "widow/room50"
bw "This one fits in my mouth just so PERFECTLY!"
scene widowbed13 with dissolve
stop sound
if age >= 20:
    voice "widow/room51a"
    bw "And surely, I first need to stretch my pussy to be able to accomodate your MONSTER shaft in the future, no?"
if age >= 18 and age <= 19:
    voice "widow/room51b"
    bw "And surely, I first need to stretch my pussy to be able to accommodate your MONSTER teenage shaft in the future, no?"
mc "No you don't! It will fit, it WILL FIT!"
voice "widow/room52"
bw "Sorry, but I'm not convinced. I think I need to..."
scene widowbed14 with dissolve
voice "widow/room53"
bw "....AAAAH... Stick this..."
scene widowbed15 with dissolve
play sound "sounds/womancum01.mp3"
voice "widow/room54"
bw "...OOOH, it's good! ...dildo as deep as it..."
scene widowbed16 with dissolve
play sound "sounds/moan03.mp3"
voice "widow/room55"
bw "AAAAH! ... WILL GO!"
scene widowbed15 with dissolve
voice "widow/room56"
bw "I'm sure you could stick quite a few MORE INCHES of YOUR ALPHA-COCK, couldn't you?"
scene widowbed16 with dissolve
play sound "sounds/moan01.mp3"
if age >= 20:
    mc "Oh yeah, PLENTY of THICK inches!"
if age >= 18 and age <= 19:
    mc "Oh yeah, PLENTY of THICK teen inches!"
scene widowbed15 with dissolve
voice "widow/room57"
bw "That's good to know, young STALLION. But right now, all I need is..."
scene widowbed16 with dissolve
play sound "sounds/moan02.mp3"
voice "widow/room58"
bw "... to get me off with this d..."
scene widowbed17 with dissolve
play channel2 "sounds/splooge02.mp3"
voice "widow/room59"
bw "Aaah, I'm cummmmmmiiingggg!"
window hide
scene widowbed17 with fastflash
play sound "sounds/womancum01.mp3"
voice "widow/room60"
bw "YES, yes, YEEEEESSS!"
stop channel2
scene widowbed18 with dissolve
stop channel1
play sound "sounds/moan03.mp3"
mc "I could have done that to your pussy..."
scene widowbed19 with dissolve
voice "widow/room61"
bw "But you didn't. MY DILDO dit the job. Just as WELL. That's why, I didn't NEED you... And now I can go to sleep. WITHOUT YOU."
mc "That's not fair, I have a MASSIVE ERECTION!"
voice "widow/room62"
bw "I'm sure you know how to TAKE CARE of it ON YOUR OWN! Goodnight, [name]!"
show screen statscreenicon
show screen questscreenicon
show screen calendar
jump Main

label BWRoomNightBedLevel02:
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar
play music "sounds/sexy09.mp3"
scene widowbed21 with fade
if widowharem:
    bw "It's you, daddy... I was waiting for you..."
    mc "As a good little harem cock-slut should..."
if widowharem == False:
    bw "It's you... I was waiting for you..."
if toldwidowbed and widowharem == False:
    mc "And I answered your call. Cos I can't get enough of that hot bod of yours!"
if toldwidowbed == False and widowharem == False:
    mc "Really? You're not going to just TEASE me this time?"
scene widowbed22 with dissolve
play sound "sounds/moan02.mp3"
if toldwidowbed or widowharem:
    bw "I'm prepping my holes again... For your COCK!"
if toldwidowbed == False and helpedwidow:
    bw "Since you clumsily helped me defeat that evil nazi nurse, I'm prepping my holes... For your COCK!"    
    $ toldwidowbed = True
if toldwidowbed == False and mission05win:
    bw "Since you brought back from the edge of treason, I'm prepping my holes... For your COCK!"    
    $ toldwidowbed = True
mc "Alright!"
scene widowbed23 with dissolve
play sound "sounds/moan04.ogg"
if widowharem:
    bw "My fingers are good, but I'm sure Daddy's cock will be even BETTER!"
    mc "Damn right, it will! I told you so since the beginning of the game but you wouldn't listen."
if widowharem == False:
    bw "OOOOh! You'd better be as GOOD as my fingers, [hero]..."
    mc "I will, I will, I promise!"
scene widowbed24:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
bw "I really got myself off... But that was just an appetizer for tonight."
scene widowbed25 with dissolve
if widowharem:
    bw "The main DISH is your GIANT COCK daddy! Please take it out of your thong and let me see it..."
    mc "I was just about to do that..."
if widowharem == False:
    bw "So get your pole out of that ridiculous thong and make it HARD for me!"
    mc "I'm getting hard, I'm getting ROCK-HARD for you Natasha!"
scene widowbed26 with dissolve
bw "Mmh, I see that... Your enormous fuckrod is ssoo tempting... Bring it over here."
scene widowbed27 with dissolve
play sound "sounds/wow.mp3"
bw "Look at this MASSIVE piece of boymeat. It looks so yummy..."
scene widowbed28 with dissolve
if widowharem:
    bw "I'm gonna have to taste it first, hope you don't mind daddy?"
if widowharem == False:
    bw "I'm gonna have to taste it first, hope you don't mind [name]?"
mc "Not at all, we have all evening for our lo-oove-mak..."
scene widowbed29 with dissolve
play sound "sounds/boymoan.mp3"
mc "...Oooh!"

label WidowBlowShortSlow:
window hide
$ widowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowshortslowvideo behind widowblowshortfastvideo
show widowblowshortslowvideo behind widowblowshortpovslowvideo
show widowblowshortslowvideo behind widowblowhardslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide widowblowshortfastvideo
hide widowblowshortpovslowvideo
hide widowblowhardslowvideo
$ widowblowfuckfast = False
if widowblowfuckslow == False:
    mc "Ooh yeah, go nice and easy, get your mouth used to my alpha-dong's girth!"
    $ widowblowfuckslow = True
window hide
pause
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowshortslow()
screen widowblowshortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVSlow")

label WidowBlowShortFast:
$ widowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowshortfastvideo behind widowblowshortslowvideo
show widowblowshortfastvideo behind widowblowshortpovfastvideo
show widowblowshortfastvideo behind widowblowhardfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide widowblowshortslowvideo
hide widowblowshortpovfastvideo
hide widowblowhardfastvideo
$ widowblowfuckslow = False
if widowblowfuckfast == False:
    mc "Yeah, you blow me so good, keep going!"
    $ widowblowfuckfast = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowshortfast()
screen widowblowshortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVFast")

label WidowBlowShortPOVSlow:
$ widowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowshortpovslowvideo behind widowblowshortslowvideo
show widowblowshortpovslowvideo behind widowblowshortpovfastvideo
show widowblowshortpovslowvideo behind widowblowhardpovslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide widowblowshortslowvideo
hide widowblowshortpovfastvideo
hide widowblowhardpovslowvideo
$ widowblowfuckfast = False
if widowblowfuckslow == False:
    mc "Ooh yeah, go nice and easy, get your mouth used to my alpha-dong's girth!"
    $ widowblowfuckslow = True
window hide
pause

show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowshortpovslow()
screen widowblowshortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortSlow")

label WidowBlowShortPOVFast:
$ widowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowshortpovfastvideo behind widowblowshortpovslowvideo
show widowblowshortpovfastvideo behind widowblowshortfastvideo
show widowblowshortpovfastvideo behind widowblowhardpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "v032/blow03.mp3"
hide widowblowshortpovslowvideo
hide widowblowshortfastvideo
hide widowblowhardpovfastvideo
$ widowblowfuckslow = False
if widowblowfuckfast == False:
    mc "Yeah, you blow me so good, keep going!"
    $ widowblowfuckfast = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowshortpovfast()
screen widowblowshortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortFast")

label WidowBlowHardSlow:
if widowharder == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharder = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowhardslowvideo behind widowblowhardfastvideo
show widowblowhardslowvideo behind widowblowhardpovslowvideo
show widowblowhardslowvideo behind widowblowshortslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide widowblowhardfastvideo
hide widowblowhardpovslowvideo
hide widowblowshortslowvideo

show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowhardslow()
screen widowblowhardslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEnd")

label WidowBlowHardFast:
if widowharder == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharder = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowhardfastvideo behind widowblowhardslowvideo
show widowblowhardfastvideo behind widowblowhardpovfastvideo
show widowblowhardfastvideo behind widowblowshortfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide widowblowhardslowvideo
hide widowblowhardpovfastvideo
hide widowblowshortfastvideo

window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowhardfast()
screen widowblowhardfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEnd")

label WidowBlowHardPOVSlow:
if widowharder == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharder = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowhardpovslowvideo behind widowblowhardslowvideo
show widowblowhardpovslowvideo behind widowblowhardpovfastvideo
show widowblowhardpovslowvideo behind widowblowshortpovslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide widowblowhardslowvideo
hide widowblowhardpovfastvideo
hide widowblowshortpovslowvideo

show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowhardpovslow()
screen widowblowhardpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEnd")

label WidowBlowHardPOVFast:
if widowharder == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharder = True        
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
show widowblowhardpovfastvideo behind widowblowhardpovslowvideo
show widowblowhardpovfastvideo behind widowblowhardfastvideo
show widowblowhardpovfastvideo behind widowblowshortpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/blow01.mp3"
hide widowblowhardpovslowvideo
hide widowblowhardfastvideo
hide widowblowshortpovfastvideo

window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowhardpovfast()
screen widowblowhardpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEnd")

label WidowBlowEnd:
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
stop channel1
scene widowbed30 with dissolve
if widowharem:
    bw "Oohh, daddy!... You're leaking pre-cum like a faucet. Your little harem cock-slave was that good, hey?"
if widowharem == False:
    bw "MMmh, it looks like it was GOOD for you [name]... You're leaking pre-cum like a faucet."
mc "Gggg..."
scene widowbed31 with dissolve
play sound "sounds/slurp.mp3"
bw "Let me clean up your knob by slurping up as much of that salty pre-spunk as I can..."
mc "Oh God..."
scene widowbed32 with dissolve
play sound "sounds/lick02.mp3"
bw "Oops, there's still some MORE. There's so MUCH of it!"
mc "Yeah, now I'm squeaky clean."
stop sound
scene widowbed33 with dissolve
if widowharem:
    bw "Does Daddy want to play with my little Russian pussy first perhaps?"
    mc "Daddy does, daddy does..."
if widowharem == False:
    bw "I reckon it's time for you to show ME some good time. Some tender love first, if you're capable of it that is..."
    mc "Yeah, I can be romantic when I want, I'll prove it to you!"
scene widowbed34 with dissolve
play sound "sounds/moan02.mp3"
bw "Yes, just like that..."
bw "Now kiss me while you play with my muff..."
scene widowbed35 with dissolve
play sound "sounds/kiss.mp3"
if widowharem:
    bw "MMmmh, daddy is kissing his little slut so well... Now she's feeling real NAUGHTY!"
if widowharem == False:
    bw "You CAN be romantic. While still being a FILTHY NAUGHTY BOY! But how FILTHY can you get?"
scene widowbed36 with dissolve
mc "What do you mean?"
bw "I want you to do a RIMJOB on me."
mc "Asshole licking it is then!"
scene widowbed37 with dissolve
bw "I can't wait for you to stick that tongue and wiggle it around in there."
mc "Sure, I can do that. It does look, reasonably clean."
scene widowbed38 with dissolve
play channel1 "sounds/moan03.mp3"
play sound "sounds/lick03.mp3"
bw "Mmmh, really get in there [name]!"
play channel2 "sounds/lick01.ogg"
scene widowbed39:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
bw "Yes, you're doing good..."
play sound "sounds/moan04.ogg"
bw "AAAH, you made me cum with your naughty tongue..."                                                      
stop channel1
stop channel2
scene widowbed37 with dissolve
mc "My pleasure. And now your ass is ready for the main dish. MY 18-inch ALPHA-DONG!"
if widowharem:
    bw "Ooh, that is so naughty of you daddy! I'll ride you and make you come like you deserve to!"
if widowharem == False:
    bw "Lie down on my bed, I'll ride it reverse cowgirl, wild bronco!"
scene widowbedpreanal01 with dissolve
mc "Now open that rosebud nice and easy for me, Natasha."
bw "I'll... try. But you're just so HUGE!"
scene widowbedpreanal02 with dissolve
play sound "sounds/moan05.mp3"
bw "AAAH, it's stretching my tight ass so WIDE!"
scene widowbedpreanal03 with dissolve
play sound "sounds/moan06.ogg"
bw "I... I think I'm ready for some ANAL POUNDING!"
window hide

label WidowBedAnalSlow:
window hide
hide cum
hide slower
hide faster
hide pov
hide front
show widowbedanalslowvideo behind widowbedanalfastvideo
show widowbedanalslowvideo behind widowbedanalpovslowvideo
$ renpy.pause(1.0, hard='True')
hide widowbedanalfastvideo
hide widowbedanalpovslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ widowbedanalfast = False
if widowbedanalslow == False:
    if widowharem:
        bw "Your cock is just so fucking HUGE DADDY!"
    if widowharem == False:
        bw "Your cock is just so fucking HUGE, AAAH!"
    $ widowbedanalslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowbedanalslow()
screen widowbedanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBedAnalFrontSlow")

label WidowBedAnalFast:
window hide
hide cum
hide slower
hide faster
hide pov
hide front
show widowbedanalfastvideo behind widowbedanalslowvideo
show widowbedanalfastvideo behind widowbedanalpovfastvideo
$ renpy.pause(1.0, hard='True')
hide widowbedanalslowvideo
hide widowbedanalpovfastvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ widowbedanalslow = False
if widowbedanalfast == False:
    mc "POUND that dick with your ass even FASTER now, Natasha!"
    $ widowbedanalfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen widowbedanalfast()
screen widowbedanalfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBedAnalFrontFast")

label WidowBedAnalFrontSlow:
window hide
hide cum
hide slower
hide faster
hide pov
hide front
show widowbedanalpovslowvideo behind widowbedanalslowvideo
show widowbedanalpovslowvideo behind widowbedanalpovfastvideo
$ renpy.pause(1.0, hard='True')
hide widowbedanalslowvideo
hide widowbedanalpovfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ widowbedanalfast = False
if widowbedanalslow == False:
    if widowharem:
        bw "Your cock is just so fucking HUGE DADDY!"
    if widowharem == False:
        bw "Your cock is just so fucking HUGE, AAAH!"
    $ widowbedanalslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen widowbedanalpovslow()
screen widowbedanalpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalSlow")

label WidowBedAnalFrontFast:
window hide
hide cum
hide slower
hide faster
hide pov
hide front
show widowbedanalpovfastvideo behind widowbedanalfastvideo
show widowbedanalpovfastvideo behind widowbedanalpovslowvideo
$ renpy.pause(1.0, hard='True')
hide widowbedanalfastvideo
hide widowbedanalpovslowvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
$ widowbedanalslow = False
if widowbedanalfast == False:
    mc "POUND that dick with your ass even FASTER now, Natasha!"
    $ widowbedanalfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen widowbedanalpovfast()
screen widowbedanalpovfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFast")

label WidowBedAnalEnd:
hide cum
hide slower
hide faster
hide pov
hide front
mc "I'm about to blow... BIG TIME!"
stop channel1
scene widowbedanalcum01 with dissolve
mc "Like right NOW! RHAAA!"
play channel1 "sounds/boyorgasm01.mp3"
window hide
with fastflash
play sound "sounds/moan04.ogg"
bw "I can feel it, you're flooding my ass with your hot spunk, I'm coming too, AAAH!"
scene widowbedanalcum02 with dissolve
mc "Get down on that cock, I want to cream your guts, RHAAA!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
bw "I've never been impaled on such a MONSTER [age]yo cock!"
scene widowbedanalcum03 with dissolve
play sound "sounds/moan05.mp3"
bw "How can you still be cumming after dumping one MASSIVE load already???"
window hide
with fastflash
mc "Cos I'm a SUPERSEX SUPERHERO, RHAAA!"
scene widowbedanalcum04 with dissolve
if age >= 20:
    mc "And now I'll douse your back in my thick sauce!"
if age >= 18 and age <= 19:
    mc "And now I'll douse your back in my thick teenage sauce!"
window hide
with fastflash
bw "I can feel it SPLASHING against my skin, it's RED-HOT, you must be so HORNY!"
scene widowbedanalcum05 with dissolve
stop channel1
play sound "sounds/splooge02.mp3"
if widowharem:
    bw "Daddy, you gave me a MASSIVE cum enema..."
if widowharem == False:
    bw "You gave me a MASSIVE cum enema..."
mc "I can see that. It's POURING out of your gaping ass. It's going to get messy on you bedsheets tonight."
scene widowbedanalcum06 with dissolve
mc "Time for me to go cos I sure ain't cleaning this up."
if widowharem:
    bw "I'll clean it all up for your next visit, Daddy!"
if widowharem == False:
    bw "I should have known. Men always leave the women with the BURDENS. * sigh *"
stop music
show screen statscreenicon
show screen questscreenicon
show screen calendar
jump Main

label NatalyaWidowRoom:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy09.mp3"
scene widownatalya01:
    zoom 0.5
with fade
mc "* What's going on here? I bet that Soviet agent is trying to manipulate the Black Widow again! Let me zoom in and try and listen to what they are talking about... *"
show widownatalya01:
    subpixel True
    linear 4.0 zoom 1.0 xpos -0.5 ypos -0.3
nt "You know this is for the best. For the best of Mother Russia!"
scene widownatalya02 with dissolve
bw "I understand my mission, I will obey, Major Natalya."
nt "Good, then maybe I can finally UNLEASH you..."
scene widownatalya03 with dissolve
nt "There. What are you going to do now to thank me for showing you the right path?"
scene widownatalya04 with dissolve
bw "I..."
scene widownatalya05 with dissolve
play sound "sounds/kiss.mp3"
nt "Don't say a word. Just kiss me, Natasha..."
scene widownatalya06 with dissolve
nt "Now I will implant the bugging device you know where."
bw "I'm very... sensitive down there."
nt "I bet you are. You have been DEPRAVED by Western decadence!"
scene widownatalya07 with dissolve
nt "But I will show you the way of Soviet PURITY!"
scene widownatalya08 with dissolve
play sound "sounds/moan02.mp3"
nt "With a iron FIST if need be!"
scene widownatalya09 with dissolve
nt "Normally, you shouldn't be enjoying this AT ALL... We'll see if you have been well-trained..."
play channel1 "sounds/wetmassage.mp3"
play channel2 "sounds/moan02.mp3"
window hide

label NatalyaFistSlow:  
hide faster
hide slower
hide nexticon
show natalyafistslowvideo behind natalyafistfastvideo
pause 1.0
hide natalyafistfastvideo with dissolve
show faster:
     xpos 1700 ypos 500     
show nexticon:
    xpos 1750 ypos 1020       
call screen natalyafistslow()
screen natalyafistslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEnd")

label NatalyaFistFast:
hide slower
hide faster
hide nexticon
show natalyafistfastvideo behind natalyafistslowvideo
nt "What if I fisted you a bit faster? I wonder what would happen then..."
window hide
hide natalyafistslowvideo with dissolve
show slower:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen natalyafistfast()
screen natalyafistfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEnd")

label NatalyaFistEnd:
hide nexticon
hide slower
hide faster
nt "You're enjoying this, aren't you? All that Western decadence CORRUPTION is showing!"
bw "No, I ... It just reminds me of someone's c..."
nt "Oh, I see. That stupid Super-Hero with the stupid thong? Did he go as deep as THIS though?"

label NatalyaFistHarderSlow:  
hide faster
hide slower
hide nexticon
show natalyafistharderslowvideo behind natalyafistharderfastvideo
pause 1.0
hide natalyafistharderfastvideo with dissolve
play sound "sounds/womangroan.mp3"
bw "AAAH, it's so DEEP!"
show faster:
     xpos 1700 ypos 500     
show nexticon:
    xpos 1750 ypos 1020       
call screen natalyafistharderslow()
screen natalyafistharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEnd")

label NatalyaFistHarderFast:
hide slower
hide faster
hide nexticon
show natalyafistharderfastvideo behind natalyafistharderslowvideo
play sound "sounds/moan04.ogg"
nt "You want it even FASTER, don't you, Natasha?"
bw "No... I..."
window hide
hide natalyafistharderslowvideo with dissolve
show slower:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen natalyafistharderfast()
screen natalyafistharderfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEnd")

label NatalyaFistHarderEnd:
hide nexticon
hide slower
hide faster
scene widownatalya10 with dissolve
nt "I think... I placed it in the right spot..."
stop channel1
stop channel2
scene natalyafistcum01 with dissolve
play sound "sounds/moan06.ogg"
nt "Oh yeah, most definitely!"
scene natalyafistcum02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1        
with dissolve
play sound "sounds/moan03.mp3"
pause
nt "Look at all that filthy anal cream. We should invent a word for it. Like santorum or something."
mc "* I think it's time to intervene... *"
scene widownatalya11 with dissolve
mc "Stop this right there! I kind of enjoyed this, but it's going too far! And too deep."
nt "You again! Always at the wrong place at the wrong time..."
mc "What are you up to, Agent Natalya? SPEAK!"
scene widownatalya12 with dissolve
nt "We were discussing how DEPRAVED this country is. And how superior the PURITY of the Soviet Way of Life is!"
mc "Says the commie fister!"
scene widownatalya13 with dissolve
nt "Why are you so angry? People in the Soviet Union are never angry. You could be their hero. If you wanted..."
bw "Yes. And MY hero..."
mc "Pure propaganda! I'm not as easily manipulated as an Iowa country bumpkin during a Republican primary!"
scene widownatalya14 with dissolve
nt "You're walking around in a thong, that's just disgusting! If you were a Soviet Super-Hero, you would have a PROPER costume... With a CAPE."
mc "I would?"
    
scene widownatalya15:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/dream.mp3"
show mcsoviethero01:
    xpos 0.02 ypos 0.02
with dissolve
nt "And the Black Widow could be your PERSONAL side-kick to bring Soviet Peace and Justice to this country..."
mc "I..."
hide mcsoviethero01
show mcsoviethero02:
    xpos 0.02 ypos 0.02
with fastdissolve
nt "Imagine how the people of Cockham would worship you once you give them back what was STOLEN from them by the evil capitalists! Such as Bruce Vayne... Or Batman if you prefer..."
scene widownatalya16:
    subpixel True
    zoom 1 xpos 0 ypos -0.02
    ease 10 xpos -0.05 ypos 0.0 zoom 1.05
show mcsoviethero03:
    xpos 0.52 ypos 0.02
with dissolve
mc "Ah yeah, that billionaire dude, he's not even a REAL Super-Hero!"
nt "No he's not. But YOU ARE. A Super-Hero of the PEOPLE... With my help... And the Black Widow, she's just ACHING to be your side-kick, aren't you, Natasha?"
scene widownatalya17 with dissolve
bw "Yes. Join us [name], the Soviets are destined to rule the world. The Soviet Union will NEVER fall."
nt "We are ONE people, Russian and Ukrainian brothers who would never fight each other like the Americans do all the time. We are the country of Peace, and your country NEEDS us!"
bw "Join us..."
nt "Yes, JOIN US!"
if evilness <= 12:
    scene widownatalya18a with dissolve
    mc "Not a chance, I'm an ALL-AMERICAN SUPER-HERO!"
    nt "So be it, then I will have to SUBDUE you!"
if evilness >= 13:
    scene widownatalya18b with dissolve
    mc "Maybe... It sounds like it could fit my plan for Super-Domination of Cockham pretty well, it's a deal. BUT..."
    nt "But WHAT?"
    scene widownatalya18c with dissolve
    mc "You'll be the ones under MY COMMAND!"
    nt "Mother Russia has no Master but Mother Russia! And whoever is the First Secretary of the Communist Party obviously."
    scene widownatalya18a with dissolve
    mc "Then we are at an impasse, Agent Natalya..."
    nt "I think not!"

play music "sounds/radiation02.mp3"
show spiral:
    subpixel True
    rotate 0 xanchor 0.285 yanchor 0.375    
    linear 10.0 rotate 360
    repeat
show natalyahypno:   
    subpixel True
    zoom 0.9 xpos -0.05 ypos 0.0
    linear 5.0 zoom 1.0 xpos -0.1 ypos -0.05
    linear 5.0 zoom 0.9 xpos -0.05 ypos 0.0
    repeat
nt "Submit to my will, [name]."
mc "She's trying to hypnotize me! I must... RESIST..."
call screen usepower("useresistance", "HypnoNoResistance", "HypnoResistance") with dissolve

label HypnoNoResistance:
"You are slowly being turned into a Soviet zombie sleeper agent..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return    

label HypnoResistance:
stop music
scene widownatalya18a with dissolve
mc "Now, it's MY turn!"
$ img_l = []
$ l2_l = []
if mccombat >= 2:
    $ img_l.append("usecombat")
    $ l2_l.append("HypnoCombat")
if mcmind >= 1:
    $ img_l.append("usemind")
    $ l2_l.append("HypnoCombat")
if img_l:
    call screen usepower(img_l, "HypnoNoCombat", l2_l) with dissolve

label HypnoNoCombat:
mc "* You're too slow, player! Let's try this again..."
jump HypnoResistance

label HypnoCombat:
$ usedresistance += 1
if selected_power == "usemind":
    $ usedmind += 1
    play music "sounds/radiation02.mp3"    
    scene widownatalya20 with dissolve
    mc "YOU submit to my will!"
    stop music

if selected_power == "usecombat":
    $ usedcombat += 1
    scene widownatalya21 with dissolve
    play sound "sounds/punch.mp3"
    mc "Take THAT, filthy commie spy!"
    scene widownatalya22 with dissolve
    play sound "sounds/femalegrunt01.mp3"
    mc "Are you going to be a good little girl and SUBMIT, Natalya?"
    nt "I... Fine, I SUBMIT, please let me go, you're hurting me!"

scene widownatalya23:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
if evilness <= 12:
    mc "The tables have turned... And to make sure you understand what I mean when I say I'm an All-American Super-Hero, I'll show you what makes me such a SUPER-HERO!" 
if evilness >= 13:
    mc "The tables have turned... And to make sure you understand what our agreement is all about, I'll show you what makes me such a powerful secret SUPER-VILLAIN!" 
play music "sounds/sexy09.mp3"
scene natalyapreblow01 with dissolve
play sound "sounds/wow.mp3"
nt "I've never seen a Soviet cock THIS big!"
mc "That's right. THIS is a REAL SUPERHERO COCK!"
scene natalyapreblow02 with dissolve
play sound "sounds/slap.mp3"
mc "One that carries a heavy punch!"
scene natalyapreblow03 with dissolve
play sound "sounds/slap.mp3"
mc "For those who DISOBEY me!"
scene natalyapreblow04 with dissolve
mc "So get going and get SUCKING!"
bw "Yes MASTER!"
play channel2 "sounds/wank.mp3"

label NatalyaBlowSlow:
$ natalyablowfast = False
window hide
show natalyablowslowvideo behind natalyablowfastvideo
show natalyablowslowvideo behind natalyablowpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyablowfastvideo
hide natalyablowpovslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowslow == False:
    $ natalyablowslow = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowslow()
screen natalyablowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVSlow")

label NatalyaBlowFast:
$ natalyablowslow = False
window hide
show natalyablowfastvideo behind natalyablowslowvideo
show natalyablowfastvideo behind natalyablowpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyablowpovfastvideo
hide natalyablowslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowfast == False:
    $ natalyablowfast = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowfast()
screen natalyablowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVFast")

label NatalyaBlowPOVSlow:
$ natalyablowfast = False
window hide
show natalyablowpovslowvideo behind natalyablowslowvideo
show natalyablowpovslowvideo behind natalyablowpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyablowpovfastvideo
hide natalyablowslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
with dissolve
if natalyablowslow == False:
    $ natalyablowslow = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckslow()
screen natalyablowpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowSlow")

label NatalyaBlowPOVFast:
$ natalyablowslow = False
window hide
show natalyablowpovfastvideo behind natalyablowfastvideo
show natalyablowpovfastvideo behind natalyablowpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyablowfastvideo
hide natalyablowpovslowvideo
hide nexticon
hide closer
hide faster
hide slower
hide pov
if natalyablowfast == False:
    $ natalyablowfast = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckfast()
screen natalyablowpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowFast")

label NatalyaBlowEnd:
hide nexticon
hide closer
hide faster
hide slower
hide pov
mc "I think your jaws need some more stretching, don't you think?"
if evilness <= 12:
    nt "I... Yes, Good Master."
if evilness >= 13:
    nt "I... Yes, Evil Master."
stop channel1
stop channel2
scene natalyapostblow01:
    subpixel True
    zoom 1 xpos 0 ypos -0.02
    ease 10 xpos -0.05 ypos 0.0 zoom 1.05
with dissolve
mc "So time for your big mouths to OPEN WIDE!"
play channel2 "sounds/wank.mp3"

label NatalyaSwitchBlowSlow:
$ natalyaswitchfast = False
window hide
show natalyaswitchslowvideo behind natalyaswitchfastvideo
show natalyaswitchslowvideo behind natalyaswitchcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyaswitchfastvideo
hide natalyaswitchcloserslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchslow == False:
    $ natalyaswitchslow = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchslow()
screen natalyaswitchslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlow")

label NatalyaSwitchBlowFast:
$ natalyaswitchslow = False
window hide
show natalyaswitchfastvideo behind natalyaswitchslowvideo
show natalyaswitchfastvideo behind natalyaswitchcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyaswitchcloserfastvideo
hide natalyaswitchslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchfast == False:
    $ natalyaswitchfast = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchfast()
screen natalyaswitchfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVFast")

label NatalyaSwitchBlowPOVSlow:
$ natalyaswitchfast = False
window hide
show natalyaswitchcloserslowvideo behind natalyaswitchslowvideo
show natalyaswitchcloserslowvideo behind natalyaswitchcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/lick01.ogg"
hide natalyaswitchcloserfastvideo
hide natalyaswitchslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
with dissolve
if natalyaswitchslow == False:
    $ natalyaswitchslow = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckslow()
screen natalyaswitchcloserfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowSlow")

label NatalyaSwitchBlowPOVFast:
$ natalyaswitchslow = False
window hide
show natalyaswitchcloserfastvideo behind natalyaswitchfastvideo
show natalyaswitchcloserfastvideo behind natalyaswitchcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/lick03.mp3"
hide natalyaswitchfastvideo
hide natalyaswitchcloserslowvideo
hide nexticon
hide pov
hide faster
hide slower
hide closer
if natalyaswitchfast == False:
    $ natalyaswitchfast = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckfast()
screen natalyaswitchcloserfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowFast")

label NatalyaSwitchBlowEnd:
stop channel1
stop channel2
scene natalyapostblow02 with dissolve
mc "Nice, you did a good enough job. Now turn round and offer your womanhoods to my CUNT-DESTROYER!"
bw "Who should go first?"
mc "Agent Natalya. She needs to be PUNISHED what what she's done!"
scene natalyaprefuck01 with dissolve
mc "And PUNISHED she will be!"
scene natalyaprefuck02 with dissolve
if age >= 20:
    nt "Your Western monstercock... It's just TOO BIG!"
if age >= 18 and age <= 19:
    nt "Your Western teenage monstercock... It's just TOO BIG!"
mc "Or maybe it's your tiny Commie pussy that's TOO TIGHT! Let's find out..."
scene natalyaprefuck03 with dissolve
play sound "sounds/womancum01.mp3"
nt "AAAH!"
mc "I guess you're right. It's my American cock that's just HUMONGOUS. Your pussy is just fine."
bw "He's going to DESTROY you, Natalya, get ready for it... I'm sorry, but I can't help you, he's just too... MANLY!"

label NatalyaFuckSlow:
$ natalyafuckfast = False
window hide
show natalyafuckslowvideo behind natalyafuckfastvideo
show natalyafuckslowvideo behind natalyafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyafuckfastvideo
hide natalyafuckpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckslow == False:
    $ natalyafuckslow = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckslow()
screen natalyafuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVSlow")

label NatalyaFuckFast:
$ natalyafuckslow = False
window hide
show natalyafuckfastvideo behind natalyafuckslowvideo
show natalyafuckfastvideo behind natalyafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "v031/womansex07.mp3"
hide natalyafuckpovfastvideo
hide natalyafuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckfast == False:
    $ natalyafuckfast = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckfast()
screen natalyafuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVFast")

label NatalyaFuckPOVSlow:
$ natalyafuckfast = False
window hide
show natalyafuckpovslowvideo behind natalyafuckslowvideo
show natalyafuckpovslowvideo behind natalyafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyafuckpovfastvideo
hide natalyafuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if natalyafuckslow == False:
    $ natalyafuckslow = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckslow()
screen natalyafuckpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckSlow")

label NatalyaFuckPOVFast:
$ natalyafuckslow = False
window hide
show natalyafuckpovfastvideo behind natalyafuckfastvideo
show natalyafuckpovfastvideo behind natalyafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "v031/womansex07.mp3"
hide natalyafuckfastvideo
hide natalyafuckpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if natalyafuckfast == False:
    $ natalyafuckfast = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckfast()
screen natalyafuckpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckFast")

label NatalyaFuckEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
bw "Are you about to give her your nutload, [hero]?"
play sound "sounds/panting.mp3"
mc "Fuck yeah, close..."
scene natalyafuckcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "CLOSER, RHAAA!"
window hide
with fastflash
nt "I'm being stuffed by a giant Western cock! AAAH!"
scene natalyafuckcum02 with dissolve
play sound "sounds/splooge02.mp3"
mc "That's right, and now I'm going to fill you up like an AMERICAN GAS-GUZZLER!"
window hide
with vpunch
mc "FUCK YEAH!!!!"
scene natalyafuckcum03 with dissolve
play sound "sounds/splooge03.mp3"
bw "Go on, [hero], fill her tight Russian fuckhole with your super-hero cream, show her what she's been missing!"
window hide
with fastflash
nt "TOO MUCH! AAAH!!!"
scene natalyafuckcum04 with dissolve
mc "Never ENOUGH for a All-American SUPER-STUD!!!"
window hide
with hpunch
bw "COVER HER WITH YOUR CREAM!"
scene natalyafuckcum05 with dissolve
mc "YAAAH!"
window hide
with fastflash
nt "I Submit, I submit! I'll leave the Black Widow alone and help you in any way I can..."
scene natalyafuckcum06 with dissolve
stop channel1
mc "Phew... I knew you would... Eventually..."
bw "But what about me, [hero]? I never said I would submit... * wink *"
scene natalyafuckcum07:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "Oh, I see. You want me to make you SUBMIT, hey?"
bw "Yes, Daddy! Then I'll become your harem slave... You want that, don't you?"
mc "Oh fuck, that's it, I'm STILL HARD because of your naughty talk!"
scene natalyafuckcum08 with dissolve
mc "SO HARD in fact that I'm just going to need to POUND that nice pussy of yours HARD and FAST!"
bw "Oooh, I'm going to get punished too for being such a naughty commie spy then?"
scene natalyafuckcum09 with dissolve
play sound "sounds/moan05.mp3"
mc "Yes! And I'll turn you into my personal obedient harem cock-slut!"
bw "AAAH, I can't wait Daddy!"

label NatalyaWidowFuckSlow:
window hide
show natalyawidowfuckslowvideo behind natalyawidowfuckfastvideo
show natalyawidowfuckslowvideo behind natalyawidowfuckfastervideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide natalyawidowfuckfastvideo
hide natalyawidowfuckfastervideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
mc "So you want to become my harem slave, Natasha?"
bw "Ooh, yes daddy! But fuck me some more first... Aaah..."
show faster:
     xpos 1700 ypos 500    
call screen natalyawidowfuckslow()
screen natalyawidowfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFast")

label NatalyaWidowFuckFast:
window hide
show natalyawidowfuckfastvideo behind natalyawidowfuckslowvideo
show natalyawidowfuckfastvideo behind natalyawidowfuckfastervideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide natalyawidowfuckfastervideo
hide natalyawidowfuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
bw "Ooh... God... Daddy, you fuck me so POWERFULLY!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show slower:
     xpos 50 ypos 500    
call screen natalyawidowfuckfast()
screen natalyawidowfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFaster")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckSlow")

label NatalyaWidowFuckFaster:
window hide
show natalyawidowfuckfastervideo behind natalyawidowfuckfastvideo
show natalyawidowfuckfastervideo behind natalyawidowfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide natalyawidowfuckfastvideo
hide natalyawidowfuckslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov  
bw "Yes, Yes, fuck me HARD and FAST DADDY!!!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
call screen natalyawidowfuckfaster()
screen natalyawidowfuckfaster():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckFast")

label NatalyaWidowFuckEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
bw "Am I going to get impregnated by your fat load, daddy?"
mc "Is that what you want?"
bw "Yes daddy, give your little Russian cock-whore a baby!"
scene widownatalyafuckcum01 with dissolve
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "THERE YOU GO THEN!!!"
window hide
with fastflash
bw "I can feel it Daddy, I can feel your fertile seed inside my poor little slut pussy!!!"
scene widownatalyafuckcum02 with dissolve
play sound "sounds/boymoan05.mp3"
mc "HERE, YOU'LL FEEL IT EVEN BETTER, RHAAA!"
window hide
with vpunch
play sound "sounds/womancum02.mp3"
bw "AAAAH!"
scene widownatalyafuckcum03 with dissolve
mc "COMING SO MUCH, RHAAA!"
window hide
with fastflash
nt "Her... stomach is distending from the super-heroic amount of come you're dumping inside her!"
scene widownatalyafuckcum04:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
nt "Are you alright, Natasha? Say something!"
window hide
with fastflash
bw "Uuuh.... HE'S STILL PUMPING ME FULL!"
nt "Pull out, I beg you [hero], I'll do anything you want but don't destroy her womb like that!"
scene widownatalyafuckcum05 with dissolve
stop channel2
play sound "sounds/femalegrunt01.mp3"
bw "I can do it myself, AAAAH!"
window hide
with vpunch
nt "Well done, you're plastering him with his own cum, that will teach him a lesson!"
scene widownatalyafuckcum06 with dissolve
play sound "sounds/splooge01.mp3"
mc "I'm not done yet, I'll keep showering you with even MORE scum than you pump out, Natasha!"
window hide
with fastflash
play sound "sounds/splat.ogg"
bw "UUUUH! NEED... TO.... BEAT... HIM!"
scene widownatalyafuckcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Came... so much... Did I win?..."
scene widownatalyafuckcum08 with dissolve
nt "I have to admit you... caked her in GALLONS of cum. We are defeated. And the Black Widow is now yours to dispose of as you wish..."
window hide
play sound "sounds/achievement.mp3"
show haremgirlwidow at posharem
$ renpy.pause(0.5, hard='True')
show haremgirltext at posharemtext
pause
$ widowharem = True
mc "Woo-Hoo! One more girl into my Harem!"
nt "And not just anybody. The BLACK WIDOW."
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop music
jump Main
