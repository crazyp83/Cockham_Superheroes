label SupergirlGallery:
stop channel3
play channel3 "sounds/intromusic.mp3"
scene supergirlbackground
show supergirlmaingallery at gallerypos01 with moveinleft
call screen gallerysupergirl()
screen gallerysupergirl():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Supergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerysupergirl"), Jump ("MainGallery05")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerysupergirl"), Jump ("SuperGalleryAnim")]
    
    if renpy.seen_image("powersuper01"):
        imagebutton:
            focus_mask True
            idle "gallery/supergirlgallery01.png" xpos 400 ypos 100
            hover "gallery/supergirlgallery01.png"
            action Jump ("SupergirlGallery01")
    text "{font=Gui/Heroes Legend.ttf}Lesbian w/Pgirl{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("powersuper01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")

    if renpy.seen_image("robinson01"):
        imagebutton:
            focus_mask True
            idle "gallery/poisongallery01.png" xpos 750 ypos 100
            hover "gallery/poisongallery01.png"
            action Jump ("SupergirlGallery02")
    text "{font=Gui/Heroes Legend.ttf}Poison Ivy Combat{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("robinson01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")

    if renpy.seen_image("supergirlgym05"):
        imagebutton:
            focus_mask True
            idle "gallery/supergirlgallery03.png" xpos 1100 ypos 100
            hover "gallery/supergirlgallery03.png"
            action Jump ("SupergirlGallery03")
    text "{font=Gui/Heroes Legend.ttf}Gym Training{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("supergirlgym05") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")

    if renpy.seen_image("supershower01"):
        imagebutton:
            focus_mask True
            idle "gallery/supergirlgallery04.png" xpos 1450 ypos 100
            hover "gallery/supergirlgallery04.png"
            action Jump ("SupergirlGallery04")
    text "{font=Gui/Heroes Legend.ttf}Shower Handjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("supershower01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")

    if renpy.seen_image("supergirlpoolcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/supergirlgallery05.png" xpos 400 ypos 380
            hover "gallery/supergirlgallery05.png"
            action Jump ("SupergirlGallery05")
    text "{font=Gui/Heroes Legend.ttf}Pool Fuck{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("supergirlpoolcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")

    if renpy.seen_image("mcroomsex01"):
        imagebutton:
            focus_mask True
            idle "gallery/milfgallery07.png" xpos 750 ypos 380
            hover "gallery/milfgallery07.png"
            action Jump ("SupergirlGallery06")
    text "{font=Gui/Heroes Legend.ttf}Cpt MILF 3some{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06
    if renpy.seen_image("mcroomsex01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("SupergirlGallery")
            
label SuperGalleryAnim:
stop channel3
play channel3 "sounds/sexy04.mp3"
call screen screenanimsuper()
screen screenanimsuper():
    modal True
    add "gallery/supergirlbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "superanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "superanimbik" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "superanimnak" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "superanimmus" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimsuper"), SetVariable ("animcount", 1), Jump ("SupergirlGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Supergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft2{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}30C-20-32{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Blowjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/superanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimsuper")]
    add "gallery/superanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimsuper")]
    add "gallery/superanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimsuper")]
    add "gallery/superanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimsuper")]
            
label SupergirlGallery01:
$ powersupertalkslowx = False
$ powersupertalkslowx = False
stop music
stop channel3
stop sound
scene powersuper01 with fade
play music "sounds/sexy07.mp3"
mc "Well, hello there ladies, what have we got going here? I think I might join!"
scene powersuper02 with dissolve
pg "This is a girls night ONLY! You're not invited, [name]."
mc "What? But I..."
sg "I'm on assignment with Powergirl, not YOU today..."
scene powersuper03 with dissolve
play sound "sounds/kiss.mp3"
pg "And after our tough day fighting crime, we deserve some relaxing time together, don't you agree, [name]?"
scene powersuper04 with dissolve
mc "Yeah, sure, but I've been fighting crime too! I deserve something too!"
pg "Don't interrupt us! You can watch, but you'd better shut up..."
scene powersuper05 with dissolve
play sound "sounds/kiss.mp3"
sg "Mmh..."
mc "* God, this is so Super-Sexy *"
scene powersuper06 with dissolve
mc "Pretty pl..."
pg "I said NO, [name]! Just enjoy the show. You're lucky enough to be watching it..."
window hide

label PowerSuperSlowxx:
hide nexticon
hide faster
hide slower
hide sideicon
hide front
show powersuperslowvideo behind powersuperfastvideo
show powersuperslowvideo behind powersuperfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powersuperfrontslowvideo
hide powersuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powersupertalkfastx = False
if powersupertalkslowx == False:
    sg "Mmh, Kara, just like that!"
    $ powersupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powersuperslowxx()
screen powersuperslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlowxx")

label PowerSuperFastxx:
hide nexticon
hide faster
hide slower
hide sideicon
hide front
show powersuperfastvideo behind powersuperslowvideo
show powersuperfastvideo behind powersuperfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powersuperslowvideo
hide powersuperfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powersupertalkslowx = False
if powersupertalkfastx == False:
    pg "Oooh! UUUH, it feels so good rubbing our pussies together!"
    $ powersupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powersuperfastxx()
screen powersuperfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEndxx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFastxx")

label PowerSuperFrontSlowxx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
show powersuperfrontslowvideo behind powersuperslowvideo
show powersuperfrontslowvideo behind powersuperfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powersuperslowvideo
hide powersuperfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powersupertalkfastx = False
if powersupertalkslowx == False:
    sg "Mmh, Kara, just like that!"
    $ powersupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powersuperfrontslowxx()
screen powersuperfrontslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFastxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlowxx")

label PowerSuperFrontFastxx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
show powersuperfrontfastvideo behind powersuperfastvideo
show powersuperfrontfastvideo behind powersuperfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powersuperfrontslowvideo
hide powersuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powersupertalkslowx = False
if powersupertalkfastx == False:
    pg "Oooh! UUUH, it feels so good rubbing our pussies together!"
    $ powersupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show sideicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powersuperfrontfastxx()
screen powersuperfrontfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEndxx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFastxx")

label PowerSuperEndxx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
pg "[name] is being a naughty boy, he's rubbing himself while he's admiring the show..."
sg "A NAUGHTY, DIRTY boy! Knowing that he's getting hard watching us makes me want to cum... Even if boys' thingies are DISGUSTING."
scene powersupercum01 with dissolve
pg "Then let me help you reach that climax, Linda!"
play sound "sounds/moan05.mp3"
scene powersupercum02 with dissolve
play channel1 "sounds/moan02.mp3"
sg "... AAAAH!"
play sound "sounds/splooge02.mp3"
window hide
with hpunch
pg "UUUUH, come for me Supergirl!"
scene powersupercum03 with dissolve
stop channel1
play sound "sounds/panting.mp3"
pg "Mmmh, she squirted so much, it must have been REAL GOOD..."
scene powersupercum04 with dissolve
sg "Oooh... This is the BEST orgasm I ever had..."
scene powersupercum05 with dissolve
sg "But... You're all DIRTY with my juices, Kara. I need to clean up my mess..."
mc "I'll help you!"
pg "No you WON'T! I want her feminine touch and not your ROUGH hands and tongue on my breasts..."
play channel1 "sounds/lick01.ogg"
scene powersuperbreast
$ renpy.pause(1.0, hard='True') 
pause
stop channel1
pg "I think I'm all clean... Now it 's YOUR turn, Linda."
play channel1 "sounds/lick03.mp3"
scene powersuperpussy
$ renpy.pause(1.0, hard='True') 
pause
stop channel1
play sound "sounds/moan05.mp3"
scene powersuper10 with dissolve
sg "Oh my God, you lick pussy sssoo well! Where did you learn that?"
pg "It seems you're not the only one with some SUPER-SEX superpowers, [name]!"
mc "I'm the only one with a 15-inch long pussy-pleaser!"
scene powersuper06 with dissolve
pg "Yeah, I think we all know by now, you keep telling us."
sg "It's getting late and we need to take a shower TOGETHER before heading to bed. So off you go, [name]."
mc "I'll be BACK!"
stop channel2
stop channel1
stop music
jump SupergirlGallery

label SupergirlGallery02:
stop music
stop channel3
stop sound
scene robinson01
play music "v03/parkambience.mp3"
mc "So, let's look for some sex crime. * Damn, look at that hot chick jogging our way... *"
sg "Fine. What about this derelict greenhouse over there? It looks out of place..."
scene robinson02 with dissolve
mc "What greenhouse?"
sg "The one over there. The OTHER WAY, [name]!"
scene robinson03 with dissolve
mc "Err, what?"
scene robinson04 with dissolve
mc " *She's smiling at me...*"
sg "You're NOT listening to me!"
scene robinson05 with dissolve
mc "Sure, sure. The... greenhouse."
sg "You're not looking at it! You're just looking at that girl's big tits! That's the only thing you boys care about!"
scene robinson06 with dissolve
mc "What girl?"
sg "Don't try and pretend I didn't see you ogle her. I'm sick and tired of girls who get all the attention just because they have a bigger rack than mine!"
scene robinson07 with dissolve
mc "You rack is... just fine, Linda, I promise. I was just... distracted for a moment. But ok, let's investigate this greenhouse."
sg "Umpf! I don't feel like I'm getting any proper training from YOU!"
mc "I'll show you! We'll go there and we'll fight some SEX CRIME together!"

scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
show ivy01 with moveinleft
show ivy01:
    breathe
pi "Who are you? I didn't invite you HERE!"
mc "We're SUPERHEROES! And my specific job is to fight the scourge of SEX CRIME in this city! And you're, like, topless, which I believe is probably against the law."
hide ivy01
show ivy04
with dissolve
pi "The only LAW I obey is the MOTHER EARTH LAW! To be ONE with Mother Nature, in all its GLORIOUS BEAUTY!"
sg "She's just a hippy I think. There were a few in Smallcoxville and they smoked some disgusting stuff so I put them in jail."
hide ivy04
show ivy03
with dissolve
pi "The history of Humanity, people against people, WAR, DESTRUCTION OF OUR PLANET, you ALL deserve to be in jail! You all deserve to DIE!"
mc "Now let's all calm down here. I'll forgive your...err... toplessness, cos I'm a nice guy and all but..."
sg "You're defending her because she's got big boobs! But she's a fucking FREAK who lives in a DUMP!"
hide ivy03
show ivy05
with dissolve
pi "How dare you call the only plant paradise left in this filthy town a dump!"
sg "It is a DUMP! And I bet you're a Super-Villainess!"
window hide
play sound "v03/rumble.mp3"
hide ivy05
show ivy06
with dissolve
hide ivy06
show ivy07
with dissolve
hide ivy07
show ivy08
with dissolve
mc "What the??? Oh shit..."
sg "I KNEW it! Supergirl will show her the might of the Cockham League of Justice!"
hide ivy08
show ivy09
with dissolve
play sound "sounds/whoosh.mp3"
sg "Take that, MUTANT FREAK!"
mc "Hang on there for a moment, Sup..."
play sound "v03/rumble.mp3"
scene ivy10 with dissolve
pi "My venomous snapping friends will take care of you, Supergirl!"
mc "[hero] to the rescue!"
scene ivy11 with dissolve
play sound "sounds/bonecrack.mp3"
sg "AAAh, it bit me! Right on my sensitive nipple too!"
scene ivy12 with dissolve
mc "Stop biting Supergirl, Poison Ivy!"
pi "You desecrated my paradise with your presence, now you must DIE!"
scene ivy13 with dissolve
play sound "sounds/bonecrack.mp3"
mc "I'm gonna rip those creatures off your back! And get them off my back too..."
pi "Noooo, my Preciouses, my Preciouses!"
mc "I think I'll add of your carnivorous vines to my inventory, thank you very much!"
scene ivy14 with dissolve
play sound "sounds/punch.mp3"
pi "I will avenge you, my Preciouses!"
mc "Ouch, not thank you very much for that!"
scene ivy15 with dissolve
mc "She's escaping, but it's probably for the best, I need to tend to Supergirl..."
sg "Uuuhhh... I can't stand up..."
scene ivy16 with dissolve
sg "I feel... weak and tired..."
mc "The toxins must be starting to act, despite your Super-Resistance."
sg "I... I can't fight them, they are too strong!"
scene ivy17 with dissolve
sg "What... what are you doing?"
mc "There is no time to waste, I must suck the poison out or you'll probably die!"
scene ivy18 with dissolve
play sound "sounds/slurp.mp3"
sg "But... You're sucking right on my poor little nipple..."
scene ivy19 with dissolve
play sound "v03/spit.mp3"
mc "And now I spit it out..."
sg "Eew..."
scene ivy18 with dissolve
play sound "sounds/slurp.mp3"
sg "Again? But..."
scene ivy19 with dissolve
play sound "v03/spit.mp3"
mc "I need to suck it ALL out."
scene ivy20 with dissolve
sg "I feel... much better. Thank you so much, [name]... You saved my life. Probably."
mc "Let's get out of this gallery before she comes back."
stop channel2
stop channel1
stop music
jump SupergirlGallery

label SupergirlGallery03:
stop music
stop channel3
stop sound
scene gymsuper01
mc "So, what do you say we do a bit of combat training. There's no one else in the gym..."
sg "Sure, why not. I won't use my cape to make it fair. Let me get dressed up then."
mc "I'll get dressed up too. I have a brand new pair of gym briefs..."
scene supergirlgym01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with fade
pause
sg "Let's not hit each other too hard though. I just had my hair done."
scene supergirlgym02 with dissolve
mc "What, are you scared Supergirl? Come and get some of those MUSCLES, I dare you!"
scene supergirlgym03 with dissolve
sg "Of course not! But I need to stretch first. To make sure I'll BEAT YOU."
mc "Pff! Stretching is for wimps. You won't have time to stretch in real-life situations."
scene supergirlgym04 with dissolve
sg "Yeah, but this is combat training. So don't tell me what I can or can't do."
scene supergirlgym05 with dissolve
sg "You should stretch too. It's good for coordination."
mc "Sure, whatever."
scene supergirlgym06 with dissolve
sg "If you're not going to do anything, then help me out in my exercises."
mc" Err, fine."
scene supergirlgym07 with dissolve
sg "A few push-ups to show you how STRONG I am. Even if I don't have big muscles like Kara."
mc "Pff, I can do hundreds without a sweat. You won't intimidate me if that's what you're trying to do."
scene supergirlgym08 with dissolve
sg "With only on hand? Push on my back with your arm to make it a bit harder."
play sound "sounds/womangroan.mp3"
scene supergympushup
$ renpy.pause(1.0, hard='True') 
pause
stop channel1
scene supergirlgym10 with dissolve
play sound "sounds/panting.mp3"
sg "See, I didn't break a sweat either. Now hold my ankles, I need to finish by doing some crunches."
window hide

label SuperGirlCrunchSlowx:  
play sound "sounds/womangroan.mp3"
hide faster
hide slower
hide nexticon
show supergirlcrunchslowvideo behind supergirlcrunchfastvideo
pause 1.0
hide supergirlcrunchfastvideo with dissolve
show faster:
     xpos 1700 ypos 500     
show nexticon:
    xpos 1750 ypos 1020       
call screen supercrunchslowx()
screen supercrunchslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperGirlCrunchFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SuperGirlCrunchEndx")

label SuperGirlCrunchFastx:
hide slower
hide faster
hide nexticon
show supergirlcrunchfastvideo behind supergirlcrunchslowvideo
mc "Now do it FASTER!"
sg "Not a problem for Supergirl!"
play sound "sounds/womangroan.mp3"
window hide
hide supergirlcrunchslowvideo with dissolve
show slower:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen supercrunchfastx()
screen supercrunchfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperGirlCrunchSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SuperGirlCrunchEndx")

label SuperGirlCrunchEndx:
hide nexticon
hide slower
hide faster
mc "* Mmmh, ideal time to use my Super-Senses I'd say... *"
scene supergirlgymcrunchsenses with dissolve 
sg "Just a few more..."
mc "Yeah, sure a few more. * in slow-mo...*"
play channel1 "v03/slowmo.mp3"
show supergirlgymsensesvideo behind supergirlgymcrunchsenses
pause 1.0
hide supergirlgymcrunchsenses with dissolve
show nexticon:
     xpos 1750 ypos 1020    
     
call screen supercrunchsensesx()
screen supercrunchsensesx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SuperGirlCrunchSensesEndx")

label SuperGirlCrunchSensesEndx:
stop channel1
scene supergirlgymcrunchnosenses with dissolve  
sg "No I'm ready to FIGHT you. And BEAT you!"
mc "In your dreams, Linda!"
play sound "sounds/barfight.mp3"
scene supergirlgymfight01 with fade
sg "Anything goes!"
scene supergirlgymfight02 with dissolve
mc "Well, not below the belt please. Let's keep this civil and my cock is the most important part of my body."
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
play channel2 "v03/fightmusic.mp3"
scene supergirlgymfight03 with dissolve
sg "HI-YAAAH"
scene supergirlgymfight04 with dissolve
mc "Too much screaming, you're giving your game away!"
scene supergirlgymfight05 with dissolve
play sound "sounds/punch.mp3"
sg "Maybe I did that ON PURPOSE!"
mc "Ouch, that WAS below the belt! Right on my fragile ALPHA-COCK!"
scene supergirlgymfight06 with dissolve
play sound "sounds/punch.mp3"
mc "And now you've made me ANGRY!"
sg "AAAH!"
scene supergirlgymfight07 with dissolve
sg "Let go of me! RRRRHHH!"
mc "My SUPER-STRENGTH is too much for you, Supergirl, I won't let you slip away from my clutches! And I quite like this position..."
play sound "sounds/womangroan.mp3"
sg "Must... lift myself up!"
scene supergirlgymfight08 with dissolve
mc "Nice try but I'm STILL in control. Now yield, Supergirl! I'm the strongest here!"
play sound "sounds/womangroan.mp3"
sg "UUUHHH. Ok, I submit. I can't get out of your armlock."
scene supergirlgymfight09 with dissolve
play sound "v03/winner.mp3"
mc "I'm a winner, baby!"
sg "Let's fight again. I want my REVENGE."
mc "You want another beating? I'm IN!"
scene supergirlgymfight10 with fade
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene supergirlgymfight11 with dissolve
play sound "sounds/punch.mp3"
sg "This time..."
scene supergirlgymfight12 with dissolve
play sound "sounds/punch.mp3"
sg "I will show NO RESTRAINT and NO PITY!"
mc "Jeezus, calm down, Supergirl!"
scene supergirlgymfight13 with dissolve
sg "What a WEAK opponent you make! Your Super-Combat abilities must be so LOW!"
mc "I'm not giving up, I'm just as high in level as you are in Super-Combat! And I beat you the first time round, remember?"
scene supergirlgymfight14 with dissolve
sg "But not THIS time. It's so easy to subdue boys. All I have to do is put a little bit of pressure of their useless, wrinkled, oversensitive peepee."
play sound "sounds/bonecrack.mp3"
mc "AAAAH! NO, I BEG YOU! I YIELD, I YIELD!"
sg "See? EASY!"
scene supergirlgymfight15 with dissolve
play sound "v03/winner.mp3"
sg "Supergirl, undefeated in Smallcoxville, wins again!"
mc "Hey, it's a TIE! I won the first round!"
sg "So you DIDN'T beat me then!"
mc "Fine, whatever. Time to go to bed. In MY room..."
stop channel2
stop channel1
stop music
jump SupergirlGallery

label SupergirlGallery04:
stop channel3
stop sound
scene supershower01
mc "So, you'll be sleeping in my room tonight."
scene supershower02 with dissolve
sg "Yes, Captain MILF told me. I don't know why she asked for this, it doesn't make any sense to me."
mc "It makes TOTAL sense. You need to IMMERSE yourself with your partner's life."
sg "But I need to take a shower before going to bed!"
scene supershower03 with dissolve
mc "Well, here's my OWN private shower. Be my guest."
scene supershower04 with dissolve
sg "But... You're in the room with me!"
scene supershower05 with dissolve
mc "I won't be looking I promise. And I'll take my shower after you, while you're getting dressed for a good night's sleep."
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene supershower06 with dissolve
play music "sounds/shower.mp3"
play channel1 "sounds/sexy02.mp3"
sg "I need to really rub my skin, so that it feels as soft as Kara's..." 
scene supershower07 with dissolve
sg "You're not looking?"
mc "No, no, not looking at all!"
scene supershower08 with dissolve
sg "I'm gonna be just as nice as her. People will be amazed by my baby skin!"
scene supershower09 with dissolve
mc "Damn, what a hot bod she has, she's making me hard..."
scene supershower10 with dissolve
mc "God, she's driving me crazy... Look at that fine ass..."
scene supershower11 with dissolve
stop music
sg "I'm done, you can take your shower now..."
mc "Alright, I'm coming... I've already taken my thong off and I'm covering my groin with a towel."
scene supershower12 with dissolve
sg "You'd better be, I don't want to see your great big floppy snake before I go to bed... Boys' bits are so... yuck!"
mc "Maybe you just haven't seen any hot-looking ones like mine."
scene supershower13 with dissolve
sg "Eeew... Yours is probably just diformed or something."
mc "No it's not! It's the most BEAUTIFUL penis in the WORLD, I'll have you know!"
scene supershower18 with dissolve
sg "Whatever. I don't wanna see it. Like, EVER!"
scene supershower19 with dissolve
mc "Your loss. It' super-studly too. That's why I have Super-Studliness as a superpower."
sg "That's just a ridiculous superpower. As if girls would fall for an ugly wrinkly penis just because it's huge. Pff!"
scene supershower20 with dissolve
mc "* Let's see how she feels when she actually SEES my monster rock-hard erection... *"
scene supershower21 with dissolve
sg "Oh my God, I can't believe it, you're just showering with a HARDON! That's, like, disgus..."
scene supershower22 with dissolve
sg "... Oh, your thingie... It's BEAUTIFUL!"
mc "I told you so. Why don't you help me clean it?..."
scene supershower23 with dissolve
stop music
sg "Mmh, your skin is really soft. And what HUGE muscles you have, [name]!"
mc "All the better to handle my SEX partners while I'm POUNDING them, Linda. Now my wang also needs some cleaning..."
scene supershower24 with dissolve
play sound "sounds/kiss.mp3"
sg "It's so THICK! You're really SUPER-HUNG! What BIG cock you have!"
mc "All the better to SHOVE it inside my sex partners, Linda. That's why my superhero name is \"[hero]\"!"
scene supershower25 with dissolve
sg "What... are you doing? You're fondling my tiny breasts, it feels... strange inside me."
mc "Your tits are just delicious to the touch, Linda."
sg "You really think so? They're not too small?"
scene supershower26 with dissolve
sg "Mmmh, your balls are so ENORMOUS! I can barely hold one in the palm of my hand! What GIANT balls you have, [name]!"
mc "All the better to impregnate my SEX partners, Linda."
scene supershower27 with dissolve
play sound "sounds/lick01.ogg"
sg "I LOVE the musky scent of your pre-cum."
mc "And my shaft tastes real good too. Or so I'm told. Why don't you try it out for yourself?"
sg "Alright, but just the tip then. Cos you're way too BIG for my tiny throat. I still don't understand why you need to be so big."
mc "All the bett..."
stop sound
window hide
$ blowsupertalkslowx = False
$ blowsupertalkfastx = False
$ wanksupertalkslowx = False
$ wanksupertalkfastx = False

label BlowSuperSlowx:
hide nexticon
hide faster
hide slower
hide sideicon
hide sceneicon
show blowsuperslowvideo behind blowsuperfastvideo
show blowsuperslowvideo behind blowsupersideslowvideo
$ renpy.pause(1.0, hard='True') 
hide blowsupersideslowvideo
hide blowsuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ blowsupertalkfastx = False
if blowsupertalkslowx == False:
    mc "Ooh yeah, swirl that tongue around my knob."
    $ blowsupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen blowsuperslowx()
screen blowsuperslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("BlowSuperFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("BlowSuperFrontSlowx")

label BlowSuperFastx:
hide nexticon
hide faster
hide slower
hide sideicon
hide sceneicon
show blowsuperfastvideo behind blowsuperslowvideo
show blowsuperfastvideo behind blowsupersidefastvideo
$ renpy.pause(1.0, hard='True')      
hide blowsuperslowvideo
hide blowsupersidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ blowsupertalkslowx = False
if blowsupertalkfastx == False:
    mc "Damn, you're a pro, Linda, your mouth was made to gobble up HUGE cocks!"
    $ blowsupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen blowsuperfastx()
screen blowsuperfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("BlowSuperSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("BlowSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("BlowSuperFrontFastx")

label BlowSuperFrontSlowx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show blowsupersideslowvideo behind blowsuperslowvideo
show blowsupersideslowvideo behind blowsupersidefastvideo
$ renpy.pause(1.0, hard='True')      
hide blowsuperslowvideo
hide blowsupersidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ blowsupertalkfastx = False
if blowsupertalkslowx == False:
    mc "Ooh yeah, swirl that tongue around my knob."
    $ blowsupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen blowsupersideslowx()
screen blowsupersideslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("BlowSuperFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("BlowSuperSlowx")

label BlowSuperFrontFastx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show blowsupersidefastvideo behind blowsuperfastvideo
show blowsupersidefastvideo behind blowsupersideslowvideo
$ renpy.pause(1.0, hard='True') 
hide blowsupersideslowvideo
hide blowsuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ blowsupertalkslowx = False
if blowsupertalkfastx == False:
    mc "Damn, you're a pro, Linda, your mouth was made to gobble up HUGE cocks!"
    $ blowsupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen blowsupersidefastx()
screen blowsupersidefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("BlowSuperFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("BlowSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("BlowSuperFastx")

label BlowSuperEndx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
mc "Yeah, try and get it further down your throat now..."
scene supershower28 with dissolve
if age >= 20:
    sg "I can't! Your dong is just.. too big! I'll make you come some other way. If that's what you want..."
if age >= 18 and age <= 19:
    sg "I can't! Your teen dong is just.. too big! I'll make you come some other way. If that's what you want..."
mc "Yes, I WANT! You can't leave me like that!"
scene supershower29 with dissolve
play sound "sounds/lick03.mp3"
sg "Gee, I'm not your sex slave you know. I'm a Super-HEROINE. Treat me with respect, you horse-hung super-stud..."
mc "Okay, sorry Linda. Please, I beg you, do something to relieve my bloated balls!"
scene supershower30 with dissolve
sg "Alright, but you'd better not come all over me. I just had a shower."
stop sound
window hide
play music "sounds/wank.mp3"
            
label WankSuperSlowx:
hide nexticon
hide faster
hide slower
hide sideicon
hide pov
show wanksuperslowvideo behind wanksuperfastvideo
show wanksuperslowvideo behind wanksuperpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wanksuperpovslowvideo
hide wanksuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wanksupertalkfastx = False
if wanksupertalkslowx == False:
    sg "You like that, [name]? It's my \"Supergirl Wank Special\"...!"
    $ wanksupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wanksuperslowx()
screen wanksuperslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WankSuperFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WankSuperFrontSlowx")

label WankSuperFastx:
hide nexticon
hide faster
hide slower
hide sideicon
hide pov
show wanksuperfastvideo behind wanksuperslowvideo
show wanksuperfastvideo behind wanksuperpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wanksuperslowvideo
hide wanksuperpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wanksupertalkslowx = False
if wanksupertalkfastx == False:
    sg "When I do it faster, I can feel your veins ready to BURST!"
    $ wanksupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wanksuperfastx()
screen wanksuperfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WankSuperSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WankSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WankSuperFrontFastx")

label WankSuperFrontSlowx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide pov
show wanksuperpovslowvideo behind wanksuperslowvideo
show wanksuperpovslowvideo behind wanksuperpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wanksuperslowvideo
hide wanksuperpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wanksupertalkfastx = False
if wanksupertalkslowx == False:
    sg "You like that, [name]? It's my \"Supergirl Wank Special\"...!"
    $ wanksupertalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen wanksuperpovslowx()
screen wanksuperpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WankSuperFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WankSuperSlowx")

label WankSuperFrontFastx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide pov
show wanksuperpovfastvideo behind wanksuperfastvideo
show wanksuperpovfastvideo behind wanksuperpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wanksuperpovslowvideo
hide wanksuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wanksupertalkslowx = False
if wanksupertalkfastx == False:
    sg "When I do it faster, I can feel your veins ready to BURST!"
    $ wanksupertalkfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show sideicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wanksuperpovfastx()
screen wanksuperpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WankSuperFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WankSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WankSuperFastx")

label WankSuperEndx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide pov
mc "It's gonna come Linda, I can feel..."
stop music
stop channel2
scene superwankcum01 with dissolve
play sound "sounds/boymoan03.mp3"
mc "...IT, AAAHHHH!"
window hide
with hpunch
sg "Wow, what HUGE LOADS YOU HAVE!"
scene superwankcum02 with dissolve
mc "All the better to... RHAAA!..."
window hide
with fastflash
sg "...Don't cover my face with it!"
menu:
    "Do as you're told. (no change)":
        jump SuperFaceNoCumx
    "Come on her face anyway":
        jump SuperFaceCumx

label SuperFaceNoCumx:
scene superwankcum04 with dissolve
play sound "sounds/boymoan02.mp3"
if age >= 20:
    sg "That's a GOOD boy! Keep spewing those fat wads!"
if age >= 18 and age <= 19:
    sg "That's a GOOD boy! Keep spewing those fat teenage wads!"
window hide
with fastflash
mc "FUCK YEAH! OOOH!"
scene superwankcum05 with dissolve
play sound "sounds/blow01.mp3"
mc "Of Fuck, you're sucking me straight after I came... AAAAHH...."
scene superwankcum06 with dissolve
sg "That's cos when it's the most DELICIOUS... Now that you've been drained, it's time to go to bed. Me on your bed and you on the floor that is."
jump SupergirlGallery

label SuperFaceCumx:
scene superwankcum03 with dissolve
play sound "sounds/boymoan02.mp3"
mc "...COVER YOUR FACE WITH IT!!!! AHHHH!"
window hide
with fastflash
sg "You FREAK! I told you not to come on my face!"
scene superwankcum07 with dissolve
play sound "sounds/punch.mp3"
sg "Take THAT in your nuts, you SUPER-FREAK!"
window hide
with hpunch
mc "UUURGH, OUCH!!!"
scene superwankcum08 with dissolve
sg "You can't be trusted. So you'll sleep ON THE FLOOR tonight or I'll tell Captain MILF what you did!"
scene superwankcum09 with dissolve
play sound "sounds/panting.mp3"
mc "Fine. It was totally worth it. Even if my balls hurt like hell.... Aaaaah...."    
stop channel2
stop channel1
stop music
jump SupergirlGallery

label SupergirlGallery05:
scene compoundpooldaybackground
show supergirlpool00
with fade
sg "This is where you want me to swim? It looks TOO DEEP to me. I'm scared..."
mc "Come on now, you have nothing to fear. I'll be with you to keep you safe. Plus, Super-Heroes aren't supposed to be scared of anything."
scene compoundpooldaybackground blurred:
    zoom 1.9 xoffset -400 yoffset -900
show supergirlpool01:
    xoffset 0 yoffset -1080
show compoundpooldaybackground blurred at poolbackgroundup
show supergirlpool01 at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True')
sg "You promise?"
mc "Yeah, I swear. So turn round and face your worst fears to overcome them."
scene compoundpooldaybackground blurred:
    zoom 1.9 xoffset -400 yoffset 0
show supergirlpool02:
    xoffset 0 yoffset 0
show compoundpooldaybackground blurred at powerfulldownbackground
show supergirlpool02 at harleyfulldown
with dissolve
$ renpy.pause(4.0, hard='True')
mc "* And let me admire your tight little behind while I'm at it... *"
sg "Okay... I suppose I need to know how to swim, even if the only water in Smallcoxville is a tiny river."
scene supergirlpool03 with dissolve
mc "So come on now, get in the water, Linda!"
sg "You promise you won't let me drown?"
mc "Sure, why would I do that. I'm not a Super-Villain."
scene supergirlpool04 with dissolve
mc "So, just spread your arms and we'll first check if you can float."
scene supergirlpool05 with dissolve
sg "Does this work with normal humans?"
mc "Sure, but I heard people from Krypton sometimes have a higher density than..."
scene supergirlpool06 with dissolve
mc "Shit, she really is much heavier than she looks and now she's sinking like a stone!"
scene supergirlpool07 with dissolve
play music "sounds/underwater.mp3"
sg "Gggllllbbbb!"
mc "I'd better get her fast!"
scene supergirlpool08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with dissolve
mc "Damn, she's SUPER-HEAVY! Thanks God I'm SUPER-STRONG!"
scene supergirlpool09 with dissolve
play music "sounds/waterrun.mp3"
mc "Supergirl! LINDA! Damn, she's unconscious! I have to try some CPR. Which might not work since I'm not sure about Kryptonian anatomy."
scene supergirlpool10 with dissolve
mc "Come on! Why can't people from Krypton be more normal?"
scene supergirlpool11 with dissolve
mc "It's not working. But I heard of another technique used by lifeguards in some weird comic I found in an adult bookstore while I was on the beat called \"Cock-to-Pussy resuscitation\"."
mc "I guess it's worth a try, I have nothing to lose and time is running out!"
scene supergirlpool12 with dissolve
mc "If I remember correctly, I have to insert my schlong right here..."
scene supergirlpool13 with dissolve
mc "... And then vigorously POUND the back wall of her womb!"
window hide
$ superpooltalkx= False
window hide
stop music
play music "sounds/sexy03.mp3"

label SuperPoolSlowFuckx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show superpoolslowvideo behind superpoolfastvideo
show superpoolslowvideo behind superpoolpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide superpoolpovslowvideo
hide superpoolfastvideo
with dissolve
$ superpooltalk = False
stop channel2
play channel2 "sounds/boymoan04.mp3"
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen superpoolslowx()
screen superpoolslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperPoolFastFuckx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SuperPoolFaceSlowx")

label SuperPoolFastFuckx:
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show superpoolfastvideo behind superpoolslowvideo
show superpoolfastvideo behind superpoolpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide superpoolslowvideo
hide superpoolpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
if superpooltalkx == False:
    mc "I need to POUND faster to revive her!"
    $ superpooltalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen superpoolfastx()
screen superpoolfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SuperPoolSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SuperPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperPoolFaceFastx")

label SuperPoolFaceSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show superpoolpovslowvideo behind superpoolslowvideo
show superpoolpovslowvideo behind superpoolpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide superpoolslowvideo
hide superpoolpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ superpooltalkx = False
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen superpoolpovslowx()
screen superpoolpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperPoolFaceFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SuperPoolSlowFuckx")

label SuperPoolFaceFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show superpoolpovfastvideo behind superpoolfastvideo
show superpoolpovfastvideo behind superpoolpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide superpoolpovslowvideo
hide superpoolfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
if superpooltalkx == False:
    mc "I need to POUND faster to revive her!"
    $ superpooltalkx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen superpoolpovfastx()
screen superpoolpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SuperPoolFaceSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SuperPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("SuperPoolFastFuckx")

label SuperPoolFuckEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "I guess the only left in the books is cumming inside her."
stop channel2
scene supergirlpoolcum01 with dissolve
play channel2 "sounds/boyorgasm01.mp3"
mc "Like SO! RHAAA!"
window hide
with hpunch
mc "FU-UUU-CK, if that doesn't REVIVE her, nothing will!"
scene supergirlpoolcum02 with dissolve
sg "What are you doing???"
window hide
with fastflash
mc "Reviving you! AAAAH!"
scene supergirlpoolcum03 with dissolve
sg "Get OFF me! This is DISGUSTING!"
window hide
with fastflash
mc "I'm still blowing my nut but I'll try, RHAAA!"
scene supergirlpoolcum04 with dissolve
mc "Damn, it's still spurting NON-STOP, AAAH!"
window hide
with fastflash
sg "Oh my God, now you dare to blow all over my body???"
scene supergirlpoolcum05 with dissolve
play sound "sounds/punch.mp3"
sg "Take that for cumming all over me without my consent!"
scene supergirlpoolcum06 with dissolve
play sound "sounds/diving.mp3"
mc "AAAH! Still cumming after getting kicked in the balls!"
sg "You JERK! All you had to do was to perform mouth-to-mouth! That's how it works with Kryptonians. We have LUNGS, you know!"
stop channel2
stop channel1
scene supergirlpoolcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with dissolve
play sound "sounds/boymoan.mp3"
mc "I did it! Even if she didn't appreciate it, I did it. And I feel GOOO-OOOD."
stop channel1
stop channel2
stop music
jump SupergirlGallery

label SupergirlGallery06:
$ milfdptalkfirstx = False
$ supdptalkfirstx = False
$ dpmilfcamex = 0
$ dpsupcamex = 0
$ milfdptalkcumfirstx = False
$ supdptalkcumfirstx = False
$ talkedswitchmilfx = False
$ talkedswitchsupx = False
$ talkedswitchmilfcumx = False
$ talkedswitchsupcumx = False
stop channel3
scene mcroomsex01
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
    call Good from _call_Good_16
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
cm "Oh God... It's the BIGGEST piece of [age]yo boymeat on Earth, sweetie pie! Just Give it to me, I WANT IT!"
stop channel1
stop channel2
scene mcroomsex20 with dissolve
play sound "sounds/moan06.ogg"
mc "I'll make you recover your superpowers by giving you my Super-Cock!"
$ milfmassagetalkslowx = True

label MILFMassageSlowxx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
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
call screen milfmassageslowxx()
screen milfmassageslowxx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageFastxx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVSlowxx")

label MILFMassageFastxx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
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
call screen milfmassagefastxx()
screen milfmassagefastxx():
    modal True
    button:
        xpos 1700
        ypos 800
        xysize(180, 60)        
        action Jump ("MILFMassageSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndxx")
    button:
        xpos 50
        ypos 800
        xysize(120, 60)        
        action Jump ("MILFMassagePOVFastxx")

label MILFMassagePOVSlowxx:
play channel2 "sounds/womansex01.mp3"
$ milfmassagetalkfastx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkslowx == False:
    if age >= 20:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive love muscle better..."
    if age >= 18 and age <= 19:
        mc "I think I should give your tight pussy a little break... I'll go slower so you can enjoy my massive teenage love muscle better..."
    $ milfmassagetalkslowx = True
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
call screen milfmassagepovslowxx()
screen milfmassagepovslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageSlowxx")

label MILFMassagePOVFastxx:
play channel2 "sounds/womansex02.mp3"
$ milfmassagetalkslowx = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
if milfmassagetalkfastx == False:
    cm "It's just so big, pound me HARDER please [name]!"
    $ milfmassagetalkfastx = True
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
call screen milfmassagepovfastxx()
screen milfmassagepovfastxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MILFMassagePOVSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MILFMassageEndxx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("MILFMassageFastxx")

label MILFMassageEndxx:
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

label LindaDeepThroatSlowxx:
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
call screen lindasuckslowxx()
screen lindasuckslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEndxx")

label LindaDeepThroatFastxx:
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

call screen lindasuckfastxx()
screen lindasuckfastxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LindaDeepThroatSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LindaDeepThroatEndxx")

label LindaDeepThroatEndxx:
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
$ milfdptalk01slowx = True
$ supdptalk01slowx = True

label DoubleFuckNoMilfSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slowx = True
window hide
show doublefuckslowvideo behind doublefuckfastvideo
show doublefuckslowvideo behind doublefuckslowpovvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckslowpovvideo
hide doublefuckfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkfirstx == False:
    if age >= 20:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge cock..."
    if age >= 18 and age <= 19:
        cm "Mmmh, that's it sweetie, just fuck my pussy nice and slow with your huge teenage cock..."
        $ milfdptalkfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefucknomilfslowxx()
screen doublefucknomilfslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlowxx") 

label DoubleFuckNoMilfFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
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
call screen doublefucknomilffastxx()
screen doublefucknomilffastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfPOVFastxx") 

label DoubleFuckNoMilfPOVSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "Oh God, please go a bit more slowly with your enormous fuckstick..."
    $ milfdptalk01slowx = True
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
call screen doublefucknomilfpovslowxx()
screen doublefucknomilfpovslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSlowxx") 

label DoubleFuckNoMilfPOVFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
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
call screen doublefucknomilfpovfastxx()
screen doublefucknomilfpovfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfPOVSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoMilfFastxx") 

label DoubleFuckNoSupSwitchxx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupslowvideo
if talkedswitchsupx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    cm "As long as you come back to cum inside me, sweetie pie!"
    $ talkedswitchsupx = True
window hide
show doublefuckmilfswitchvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupslowvideo behind doublefuckmilfswitchvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchvideo
hide doublefuckmilfswitchvideo
if supdptalkfirstx == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirstx = True
window hide
$ supdptalk01slowx = True
jump DoubleFuckNoSupSlowx

label DoubleFuckNoMilfSwitchxx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckslowvideo
if talkedswitchmilfx == False:
    mc "I'm gonna switch for a while and ram my shaft inside Captain MILF's pussy again!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilfx = True
window hide
show doublefucksupswitchvideo
$ renpy.pause(0.6, hard='True')
show doublefuckslowvideo behind doublefucksupswitchvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchvideo
hide doublefucksupswitchvideo
$ milfdptalk01slowx = True
jump DoubleFuckNoMilfSlowxx

label DoubleFuckNoSupSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slowx = True
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
call screen doublefucknosupslowxx()
screen doublefucknosupslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMilfSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlowxx") 

label DoubleFuckNoSupFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
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
call screen doublefucknosupfastxx()
screen doublefucknosupfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupPOVFastxx") 

label DoubleFuckNoSupPOVSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "It's... sssooo BIG. Slow down, bronco!"
    $ supdptalk01slowx = True
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
call screen doublefucknosuppovslowxx()
screen doublefucknosuppovslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckNoMILFSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupSlowxx") 

label DoubleFuckNoSupPOVFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
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
call screen doublefucknosuppovfastxx()
screen doublefucknosuppovfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckNoSupPOVSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckNoSupFastxx") 

label DoubleFuckNoMilfCumxx:
$ milfdptalk01slowx = True
$ dpmilfcamex += 1
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
jump DoubleFuckMilfSlowxx

label DoubleFuckNoSupCumxx:
$ supdptalk01slowx = True
$ dpsupcamex += 1
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
if dpsupcamex == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcamex >= 1:
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
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndx
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcamex == 0:
    jump DoubleFuckNoSupSlowxx
jump DoubleFuckSupSlowxx

label DoubleFuckMilfSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slowx = True
window hide
show doublefuckcumslowvideo behind doublefuckcumfastvideo
show doublefuckcumslowvideo behind doublefuckcumpovslowvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckcumpovslowvideo
hide doublefuckcumfastvideo
stop channel2
play channel2 "v031/womansex07.mp3"
if milfdptalkcumfirstx == False:
    if age >= 20:
        cm "You just came and you're STILL hard? My tenant is such a STALLION!"
    if age >= 18 and age <= 19:
        cm "You just came and you're STILL hard? My tenant is such a TEENAGE STALLION!"
        $ milfdptalkcumfirstx = True
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500 
show switch:
    xpos 1750 ypos 1020   
call screen doublefuckmilfslowxx()
screen doublefuckmilfslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlowxx") 

label DoubleFuckMilfFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
window hide
show doublefuckcumfastvideo behind doublefuckcumslowvideo
show doublefuckcumfastvideo behind doublefuckcumpovfastvideo
$ renpy.pause(1.0, hard='True')
hide doublefuckcumpovfastvideo
hide doublefuckcumslowvideo
show slower:
     xpos 50 ypos 500     
show zoomicon:
    xpos 1700 ypos 500 
show cum:
    xpos 1750 ypos 1020   
call screen doublefuckmilffastxx()
screen doublefuckmilffastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfPOVFastxx") 

label DoubleFuckMilfPOVSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01slowx == False:
    cm "You've been pounding your landlady's pussy so much, please go easy on her, [name]!"
    $ milfdptalk01slowx = True
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
call screen doublefuckmilfpovslowxx()
screen doublefuckmilfpovslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSlowxx") 

label DoubleFuckMilfPOVFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if milfdptalk01fastx == False:
    cm "You can pound your landlady faster now, sweetie pie! She's ready for your Level02 SUPER-COCK!"
    $ milfdptalk01fastx = True
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
call screen doublefuckmilfpovfastxx()
screen doublefuckmilfpovfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckMilfCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfPOVSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckMilfFastxx")

label DoubleFuckSupSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slowx = True
if supdptalkcumfirstx == False and dpsupcamex >= 1:
    sg "You're fucking me again! In my already cum-filled pussy... Mmmh, this is so good!"
    mc "It's so slippery with my spunk now, I can pound away even deeper!"
    $ supdptalkcumfirstx = True
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
call screen doublefucksupslowxx()
screen doublefucksupslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMilfSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlowxx") 

label DoubleFuckSupFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
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
call screen doublefucksupfastxx()
screen doublefucksupfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupPOVFastxx") 

label DoubleFuckSupPOVSlowxx:
$ milfdptalk01fastx = False
$ supdptalk01fastx = False
stop channel2
play channel2 "v031/womansex07.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01slowx == False:
    sg "My pussy... Even if it's a new, ENHANCED Super-Pussy... I can't take that much MONSTERCOCK pounding, please slow down!"
    mc "Alright, for a short while, you'll get a respite. But I need to pump FASTER to CUM, I'm warning you!"
    $ supdptalk01slowx = True
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
call screen doublefucksuppovslowxx()
screen doublefucksuppovslowxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)        
        action Jump ("DoubleFuckMILFSwitchxx")
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVFastxx") 
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupSlowxx") 

label DoubleFuckSupPOVFastxx:
$ milfdptalk01slowx = False
$ supdptalk01slowx = False
stop channel2
play channel2 "v031/womansex08.mp3"
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
if supdptalk01fastx == False:
    sg "You want to really pound my new Super-Pussy with your [age]yo MONSTERCOCK, [name]?"
    mc "Oooh yeah, here I come!"
    $ supdptalk01fastx = True
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
call screen doublefucksuppovfastxx()
screen doublefucksuppovfastxx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(150, 60)
        action Jump ("DoubleFuckSupCumxx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("DoubleFuckSupPOVSlowxx") 
    button:
        xpos 1700
        ypos 500
        xysize(150, 60)
        action Jump ("DoubleFuckSupFastxx")

label DoubleFuckSupSwitchxx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefucksupcumslowvideo
if talkedswitchsupcumx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    if dpmilfcamex <= 1:
        cm "As long as you give me another BIG load, sweetie pie!"
    if dpmilfcamex >= 2:
        cm "Alright-ee, sweetie pie. You already gave your landlady so many MASSIVE cumloads!"
    $ talkedswitchsupcumx = True
window hide
show doublefuckmilfswitchcumvideo 
$ renpy.pause(0.6, hard='True')
show doublefucksupcumslowvideo behind doublefuckmilfswitchcumvideo
$ renpy.pause(.04, hard='True')
hide doublefuckmilfswitchcumvideo
hide doublefuckmilfswitchcumvideo
if supdptalkfirstx == False:
    if age >= 20:
        sg "Oh Fuck, your dong is really MASSIVE!"
    if age >= 18 and age <= 19:
        sg "Oh Fuck, your teenage dong is really MASSIVE!"
        $ supdptalkfirstx = True
window hide
$ supdptalk01slowx = True
jump DoubleFuckSupSlowxx

label DoubleFuckMilfSwitchxx:
hide faster
hide slower
hide zoomicon
hide sceneicon
hide cum
hide switch
hide doublefuckcumslowvideo
if talkedswitchmilfcumx == False:
    mc "I'm gonna switch for a while and dip my dong inside Supergirl's snatch!"
    play sound "sounds/boymoan.mp3"
    sg "Just don't forget you OWE me a HUGE load!"
    $ talkedswitchmilfcumx = True
window hide
show doublefucksupswitchcumvideo
$ renpy.pause(0.6, hard='True')
show doublefuckcumslowvideo behind doublefucksupswitchcumvideo
$ renpy.pause(0.04, hard='True')
hide doublefucksupswitchcumvideo
hide doublefucksupswitchcumvideo
$ milfdptalk01slowx = True
jump DoubleFuckMilfSlowxx

label DoubleFuckMilfCumxx:
$ milfdptalk01slowx = True
$ dpmilfcamex += 1
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
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndx
scene dpmilfcum05 with dissolve
mc "Getting back in that tight snatch of yours, Captain MILF!"
cm "Damn, you're STILL raring to go? How are we going to TAME your BEAST?"
stop channel2
jump DoubleFuckMilfSlowxx

label DoubleFuckSupCumxx:
$ supdptalk01slowx = True
$ dpsupcamex += 1
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
if dpsupcamex == 0:
    sg "I'm getting BLOATED but it feels so good!"
if dpsupcamex >= 1:
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
if dpmilfcamex >= 2 and dpsupcamex >= 2:
    mc "FUUU-UUU-CK!"
    jump DoubleFuckEndxx
mc "And now going straight back in, I'm still ROCK-HARD!"
if dpmilfcamex == 0:
    jump DoubleFuckNoSupSlowxx
jump DoubleFuckSupSlowxx

label DoubleFuckEndxx:
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
sg "I HATE YOU! GO BACK TO THE GALLERY"
stop channel2
stop channel1
stop music
$ dpmilfcamex = 0
$ dpsupcamex = 0
jump SupergirlGallery

