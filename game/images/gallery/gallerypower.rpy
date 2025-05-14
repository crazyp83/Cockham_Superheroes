label PowerGallery:
stop channel3
play channel3 "sounds/intromusic.mp3"
scene powerbackground
show powermaingallery at gallerypos01 with moveinleft
call screen gallerypower()
screen gallerypower():
    text "{font=Gui/Heroes Legend.ttf}Naughty Powergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerypower"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerypower"), Jump ("PowerGalleryAnim")]
    
    if renpy.seen_image("gymmcpower01"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery01.png" xpos 400 ypos 100
            hover "gallery/powergallery01.png"
            action Jump ("PowerGallery01")
    text "{font=Gui/Heroes Legend.ttf}Gym Handjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("gymmcpower01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("PowerGallery01hint")

    if renpy.seen_image("powerlingeriecum01"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery02.png" xpos 750 ypos 100
            hover "gallery/powergallery02.png"
            action Jump ("PowerGallery02")
    text "{font=Gui/Heroes Legend.ttf}Sexy Lingerie{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("powerlingeriecum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("PowerGallery02hint")

    if renpy.seen_image("powerpoolhandjobcum04"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery03.png" xpos 1100 ypos 100
            hover "gallery/powergallery03.png"
            action Jump ("PowerGallery03")
    text "{font=Gui/Heroes Legend.ttf}Pool Handjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("powerpoolhandjobcum04") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

    if renpy.seen_image("compoundpowermc20"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery04.png" xpos 1450 ypos 100
            hover "gallery/powergallery04.png"
            action Jump ("PowerGallery04")
    text "{font=Gui/Heroes Legend.ttf}Pool Breastfeeding{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("compoundpowermc20") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

    if renpy.seen_image("powersuper01"):
        imagebutton:
            focus_mask True
            idle "gallery/supergirlgallery01.png" xpos 400 ypos 380
            hover "gallery/supergirlgallery01.png"
            action Jump ("PowerGallery05")
    text "{font=Gui/Heroes Legend.ttf}Lesbian w/Supergirl{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("powersuper01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

    if renpy.seen_image("mccurlballcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery06.png" xpos 750 ypos 380
            hover "gallery/powergallery06.png"
            action Jump ("PowerGallery06")
    text "{font=Gui/Heroes Legend.ttf}Gym Teasing{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06
    if renpy.seen_image("mccurlballcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

    if renpy.seen_image("powerhot08"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery07.png" xpos 1100 ypos 380
            hover "gallery/powergallery07.png"
            action Jump ("PowerGallery07")
    text "{font=Gui/Heroes Legend.ttf}Bedroom Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext07
    if renpy.seen_image("powerhot08") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("PowerGallery07hint")

    if renpy.seen_image("powergirlpoolnew11"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery08.png" xpos 1450 ypos 380
            hover "gallery/powergallery08.png"
            action Jump ("PowerGallery08")
    text "{font=Gui/Heroes Legend.ttf}Pool Jerkoff{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext08
    if renpy.seen_image("powergirlpoolnew11") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

    if renpy.seen_image("powerpoolpostbell10"):
        imagebutton:
            focus_mask True
            idle "gallery/powergallery09.png" xpos 400 ypos 660
            hover "gallery/powergallery09.png"
            action Jump ("PowerGallery09")
    text "{font=Gui/Heroes Legend.ttf}Muscle Posing{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext09
    if renpy.seen_image("powerpoolpostbell10") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("PowerGallery")

label PowerGallery01hint:
show powermaingallery at gallerypos01
show powergallery01 at posgalleryhintpic
show powergalleryhint01 at posgalleryhint
pause
hide powergalleryhint01
hide powergallery01
call screen gallerypower()

label PowerGallery02hint:
show powermaingallery at gallerypos01
show powergallery02 at posgalleryhintpic
show powergalleryhint02 at posgalleryhint
pause
hide powergalleryhint02
hide powergallery02
call screen gallerypower()

label PowerGallery07hint:
show powermaingallery at gallerypos01
show powergallery07 at posgalleryhintpic
show powergalleryhint07 at posgalleryhint
pause
hide powergalleryhint07
hide powergallery07
call screen gallerypower()

label PowerGalleryAnim:
stop channel3
play channel3 "sounds/sexy12.mp3"
call screen screenanimpower()
screen screenanimpower():
    modal True
    add "gallery/powerbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "poweranimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "poweranimbik" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "poweranimlin" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "poweranimgym" xalign -0.1 yalign 1.0
    if animcount == 5:
        add "poweranimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimpower"), SetVariable ("animcount", 1), Jump ("PowerGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Powergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34E-24-34{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Teasing{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Handjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Footjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink04
    add "gallery/poweranim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimpower")]
    add "gallery/poweranim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimpower")]
    add "gallery/poweranim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimpower")]
    add "gallery/poweranim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimpower")]
    add "gallery/poweranim05.png" xpos 1580 ypos 800
    button:
        xpos 1580
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 5), Show ("screenanimpower")]
            
label PowerGallery01:
$ renpy.start_predict("v02/gymmcliftnude.webm")
$ renpy.start_predict("v02/gymmclifterecting.webm")
stop channel3
play music "sounds/gymmusic.mp3"
scene gymmcprelift01night
mc "It's already loaded with a HEAVY set of weights. Since I'm alone, I'll go COMMANDO!"
window hide
show gymmcliftnudevideo with dissolve
window hide
pause
mc "Fuck yeah! This is getting me hard actually..."
window hide
hide gymmcliftnudevideo
show gymmclifterectingvideo
with dissolve
$ renpy.pause(1.4, hard='True')
hide gymmclifterectingvideo
$ renpy.stop_predict("v02/gymmcliftnude.webm")
$ renpy.stop_predict("v02/gymmclifterecting.webm")
show gymmcnudeerect
play sound "sounds/thud.mp3"
mc "Goddamn it, gonna continue like that!"
scene gymmclifthardvideo with dissolve
pause
scene gymmcpowerprelift01 with dissolve
pg "What are you doing [name]???"
mc "Err, Kara?"
scene gymmcpowerprelift02 with dissolve    
pg "You thought you had the gym to yourself and that you could power-lift those weights NAKED and with a MASSIVE ERECTION?"
mc "Yeah... I did actually."
pg "Well let's see if you can cope under PRESSURE..."
scene gymmcpower01 with dissolve
pg "Now try and continue your bench presses with the EXTRA pressure I apply on the barbell... I'm not using my SUPER-STRENGTH... yet."
mc "Alright, I'll show you how STRONG I TRULY am then!"
scene gymmcpower01video with dissolve
pause
pg  "Impressive... Now let's try something more... DISTRACTING!"
scene gymmcpowerpost01 with dissolve
mc "Wh, what do you have in mind?"
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
pg "But... I thought they had ENDLESS supplies of cum... Aren't you supposed to be a SUPER-STUD, [hero]?"
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
stop channel1
stop music 
jump PowerGallery

label PowerGallery02:
stop channel3
play music "sounds/sexy09.mp3"
scene powerlingeriebackground01
show powerlingerie01:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerlingerie01 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
pg "Here's the first outfit. So what do you think?"
mc "Turn round so I can have a better look, Kara."
hide powerlingerie01
show powerlingerie02
with dissolve
pg "Like that?"
mc "Yeah, like that. It's nice, very nice. But I need an even CLOSER look. So let me zoom in with my Super-Eyes."
pg "You don't have Super-Eyes."
mc "Ok, fine. But let me zoom in anyway. By squinting my normal eyes."
window hide
hide powerlingerie02
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerlingerie03:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 at widowfullbackzoombackground
show powerlingerie03 at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "And the back now. The ass... I mean, the back is important too."
window hide
hide powerlingerie03
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerlingerie04:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerlingerie04 at powerfulldown
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Is the ASS to your liking, [name]?"
mc "Ooh yeah. But the babydoll hides it too much."
scene powerlingeriebackground01 blurred:
    zoom 1.5 yoffset -400
show powerlingerie05
with dissolve
pg "I'm surprised you haven't used your Super-Senses to see right through it yet..."
mc "Hey! I'm being PROFESSIONAL here. Readers of the Cockham Planet don't have superpowers..."
scene powerlingeriebackground01 blurred
show powerlingerie06
with dissolve
pg "Alright, Mr Professional. What about the front, what do you have to say about THAT?"
mc "Your tits are huge."
hide powerlingerie06
show powerlingerie07
with dissolve
pg "I'm talking about the lingerie set I'm wearing!"
mc "Ah, sorry, I was distracted. By your HUGE tits. Though I wish they would be even BIGGER."
hide powerlingerie07
show powerlingerie08
with dissolve
pg "I don't. They're quite heavy to carry around as it is."
mc "Oh well, you have Super-Strength so it shouldn't be too much trouble."
hide powerlingerie08
show powerlingerie07
with dissolve
pg "Let's change the subject, please. And my outfit. I'll be back with another one I was thinking of maybe wearing for the photo-session."
window hide
show powerlingerie07 at moveleftoutslow
$ renpy.pause(1.2, hard='True')      

scene powerlingeriebackground01
show powerlingerie11:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerlingerie11 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
pg "And now for something a bit more NAUGHTY!"
mc "Ooh! I wanna see MORE!"
hide powerlingerie11
show powerlingerie12
with dissolve
pg "Like that?"
mc "Oh God, I think you're going to give readers a HEART ATTACK!"
pg "Mmh, that's not good. We need them to finance the compound through these regular photo-sessions."
mc "It was just a figure of speech. Let me squint my eyes again, which is probably what the readers will do too."
window hide
hide powerlingerie12
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerlingerie13:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 at widowfullbackzoombackground
show powerlingerie13 at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "Now we're talking! What about the... you know. Booty?"
pg "My ass you mean?"
window hide
hide powerlingerie13
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerlingerie14:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerlingerie14 at powerfulldown
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Is it BETTER than the last one?"
mc "Definitely. I don't even need to use Super-Senses to see your fine glutes."
scene powerlingeriebackground01 blurred:
    zoom 1.5 yoffset -530
show powerlingerie15
with dissolve
pg "You don't think it's TOO naughty for the Cockham Planet readers?"
mc "If you show your tits like that, it might be."
hide powerlingerie15
show powerlingerie16
with dissolve
pg "I'm showing them to YOU. Exclusively. You have a problem with that, [name]?"
mc "Not at all. Not at all."
scene powerlingerie21 with dissolve
pg "I can see that. You're sporting a massive hardon in front of your landlady's daughter..."
mc "Well, you did show me your tits, so you're responsible."
scene powerlingerie22 with dissolve
pg "So I'm responsible for that great big drooling tentpole?"
play sound "sounds/boymoan.mp3"
pg "What's the matter? You can't take a little bit of TEASING?"
scene powerlingerie23 with dissolve
play sound "sounds/lick02.mp3"
pg "I think you should learn to control your libido, [name]..."
play sound "sounds/boymoan02.mp3"
mc "Are you... going to blow me, Kara?"
scene powerlingerie24 with dissolve
pg "No. That would make you cum TOO EASILY... Like right now, you're already spurting filthy pre-cum all over the place..."
mc "So what are you going to do, Kara? I NEED some relief!"
scene powerlingerie25 with dissolve
pg "I'll provide relief. with my FEET!"
scene powerlingerie26 with dissolve
pg "Look at you. I simply wanted your opinion about which lingerie set I should wear and you ended up sporting a great big erection right in front of your landlady's daughter!"
pg "I bet you want to FUCK me, right?"
mc "Y...YEAH I DO!"
pg "You'll have to make do with my feet tonight!"
window hide
play channel1 "sounds/wank.mp3"
$ powerfoottalkslowx = False
$ powerfoottalkfastx = False

label PowerFootSlowFuckx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootjobslowvideo behind powerfootjobfastvideo
show powerfootjobslowvideo behind powerfootsceneslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsceneslowvideo
hide powerfootjobfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerfoottalkfastx = False
if powerfoottalkslowx == False:
    pg "You're just such a DIRTY landboy!"
    $ powerfoottalkslowx = True
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootpovslowx()
screen powerfootpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFastFuckx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootFaceSlowx")

label PowerFootFastFuckx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootjobfastvideo behind powerfootjobslowvideo
show powerfootjobfastvideo behind powerfootscenefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootjobslowvideo
hide powerfootscenefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerfoottalkslowx = False
if powerfoottalkfastx == False:
    pg "You have no self-control. As soon as you see a scantily-clad woman, you get HARD as a rock. Even if it's your landlady's DAUGHTER!"
    $ powerfoottalkfastx = True
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootpovfastx()
screen powerfootpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFaceFastx")

label PowerFootFaceSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootsceneslowvideo behind powerfootjobslowvideo
show powerfootsceneslowvideo behind powerfootscenefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootjobslowvideo
hide powerfootscenefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerfoottalkfastx = False
if powerfoottalkslowx == False:
    pg "You're just such a DIRTY landboy!"
    $ powerfoottalkslowx = True
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerfootsceneslowx()
screen powerfootsceneslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFaceFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSlowFuckx")

label PowerFootFaceFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootscenefastvideo behind powerfootjobfastvideo
show powerfootscenefastvideo behind powerfootsceneslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsceneslowvideo
hide powerfootjobfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerfoottalkslowx = False
if powerfoottalkfastx == False:
    pg "You have no self-control. As soon as you see a scantily-clad woman, you get HARD as a rock. Even if it's your landlady's DAUGHTER!"
    $ powerfoottalkfastx = True
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show pov:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerfootscenefastx()
screen powerfootscenefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootFaceSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFastFuckx")

label PowerFootFuckEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
pg "Such a filthy boy... I bet you're churning up a MONSTERLOAD for your landlady's daughter, aren't you?"
mc "Oh my God, Kara, you're teasing me so much..."
scene powerlingeriecum01 with dissolve
hide powerfootjobslowvideo
hide powerfootjobfastvideo
hide powerfootsceneslowvideo
hide powerfootscenefastvideo
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "... I NEED TO COME, AAAAHHHH!"
window hide
with fastflash
pg "Oooh, I can see that!"
scene powerlingeriecum02 with dissolve
pg "Come on, [name], BLAST IT OUT!"
window hide
with fastflash
pg "I want you to REACH THE CEILING WITH YOUR NEXT SHOT!"
if inventorylustring:
    play sound "sounds/magic.mp3"
    scene powerlingeriecum03a with dissolve    
    mc "RHAAAA! MAXIMUM CUMSHOT POWER!"
    window hide
    with hpunch
    play sound "sounds/splat.ogg"
    pg "Oh my god, your cumshots are sssooo POWERFUL!"
    window hide 
    with fastflash
    play sound "sounds/splat.ogg"
    mc "Your feet... I can't stop CU-UUU-MMMING!"
    scene powerlingeriecum04
    pg "You're cumming sssooo MUCH, [name]! Does your landlady's daughter excite you THAT MUCH?"
    window hide
    with fastflash
    stop channel1
    play sound "sounds/boymoan03.mp3"
    mc "Uuuh...Y...YES! AAAAH!"
    stop sound
    scene powerlingeriecum05 with dissolve
    play sound "sounds/panting.mp3"
    if age >= 20:
        pg "That is so FILTHY! You've CAKED my ceiling with your spunk!"
    if age >= 18 and age <= 19:
        pg "That is so FILTHY! You've CAKED my ceiling with your teenage spunk!"
    scene powerlingeriecum06 with dissolve
    pg "Because of you and your great big fat MONSTERLOADS, I'm gonna end up sleeping in SPUNK-COVERED BEDSHEETS!"
    mc "You asked me to reach the ceiling!"
    play sound "sounds/lick03.mp3"
    pg "That's IRRELEVANT! * slurp * "
    stop sound

if inventorylustring == False:
    scene powerlingeriecum03b with dissolve
    mc "RHAAAA! I'm TRYING!"
    window hide
    with hpunch
    pg "You're ALMOST reaching the ceiling. But not quite..."
    window hide 
    with fastflash
    play sound "sounds/boymoan05.mp3"
    mc "But I'm cumming as HARD as I can! RHAAA!"
    scene powerlingeriecum04 with dissolve
    pg "You ARE cumming hard, just not HARD enough! Doesn't your landlady's daughter excite you ENOUGH?"
    window hide
    with fastflash
    stop channel1
    play sound "sounds/boymoan03.mp3"
    mc "Uuuh...Y...YES! You do!"
    scene powerlingeriecum06 with dissolve
    pg "Because of you and your great big fat LOADS, I'm gonna end up sleeping in SPUNK-COVERED BEDSHEETS!"
    mc "You asked me to cum a lot!"
    play sound "sounds/lick03.mp3"
    pg "And you did... But not ENOUGH! You'll need to UP YOUR GAME if you want MORE! * wink *"

scene powerlingeriecum07:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
pg "You've been a very NAUGHTY boy, you know that?"
mc "You're the one who teased me, Kara! And I'm STILL hard, can we...?"
scene powerlingeriecum08 with dissolve
pg "...FUCK? No, I'm not ready for that... You'll have to WAIT and learn to CONTROL your libido..."
pg "Now go back to your room and do whatever it is you need to do to get it down..."
stop music
stop channel1
jump PowerGallery

label PowerGallery03:
stop channel3
scene compoundpowermc00 with fade
play music "sounds/waterrun.mp3"
mc "Oh, Kara is relaxing in the pool."
scene compoundpowermc01 with dissolve
mc "She looks so peaceful, with her big gazoongas sticking out of the water like that..."
scene compoundpowermc02 with dissolve
mc "Therefore, it's the perfect opportunity to play a trick on her. GERONIMO!"
scene compoundpowermc03 with dissolve
play sound "sounds/diving.mp3"
mc "Shit, she plunged under the surface just in the nick of time!"
scene compoundpowermc04 with dissolve
play music "sounds/underwater.mp3"
mc " * But I see her, she won't escape me! *"
scene compoundpowermc05 with dissolve
if mcagility >= 1:
    mc " * Come on, my Super-Agility should be enough... *"
if mcagility == 0:
    mc " * She's trying to use her Super-Agility to evade me... *"
scene compoundpowermc06 with dissolve
mc "* Almost, just a few inches... *"
scene compoundpowermc07 with dissolve
play music "sounds/waterrun.mp3"
pg "Not fast enough, [name]!"
scene compoundpowermc08 with dissolve
play sound "sounds/diving.mp3"
play music "sounds/underwater.mp3"
mc "* Damn, where did she go? * "
scene compoundpowermc09 with dissolve
pg "* Got you, [name]! *"
mc "* AAARGH! She's holding me in a tight armlock! And my Super-Strength is... Gotta tense all my MUSCLES... *"
scene compoundpowermc10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "* My Super-Cock is also getting tense, her armlock is making all the blood RUSH to it! *"
play sound "sounds/ripping.mp3"
mc "* Uh oh... My speedo is about to get ripped apart... *"
scene compoundpowermc11 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "I need to get out of that armlock, I can't breathe!"
scene compoundpowermc12 with dissolve
play music "sounds/waterrun.mp3"
pg "Do you give up yet [name]? My Super-Strength is a perfect match to yours but I have the advantage!"
mc "I... Fine, I give up! Please let go of me, Kara!"
scene compoundpowermc13 with dissolve
play channel2 "sounds/sexy09.mp3"
pg "Oh, but what about this great big hardon you're sporting? I can't leave you all flustered like this..."
if helpedpowergirl:
    pg "After all, you did try to help me when I was fighting that evil nazi Valkyrie... Even if you did it CLUMSILY."
scene compoundpowermc14 with dissolve
play sound "sounds/boymoan.mp3"
mc "Well, err..."
play music "sounds/underwater.mp3"
play channel1 "sounds/wank.mp3"

label PowerPoolSlowx:
hide cum
hide faster
hide slower
hide harder
hide softer
show powerpoolhjslowvideo behind powerpoolhjfastvideo
show powerpoolhjslowvideo behind powerpoolhardhjslowvideo
$ powerpooltalkfastx = False
$ powerpoolpoundtalkx = False
pg "I'll just jerk you off... Nice and slow..."
window hide
$ renpy.pause(1.0, hard='True') 
hide powerpoolhjfastvideo
hide powerpoolhardhjslowvideo
with dissolve
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen powerpoolpovslowx()
screen powerpoolpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolHardSlowx")

label PowerPoolFastx:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpooltalkfastx == False:
    pg "I think I need to go a little FASTER on that shaft, it's just BEGGING for it!"
    $ powerpooltalkfastx = True
show powerpoolhjfastvideo behind powerpoolhjslowvideo
show powerpoolhjfastvideo behind powerpoolhardhjfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerpoolhjslowvideo
hide powerpoolhardhjfastvideo
with dissolve
$ powerpoolpoundtalkx = False
pause
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen powerpoolpovfastx()
screen powerpoolpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolSlowx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolHardFastx")

label PowerPoolHardSlowx:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpoolpoundtalkx == False:
    mc "Please Kara... I need some release soon!"
    if age >= 20:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT monster schlong?"
    if age >= 18 and age <= 19:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT teenage monster schlong?"
    window hide
    $ powerpoolpoundtalkx = True
show powerpoolhardhjslowvideo behind powerpoolhjslowvideo
show powerpoolhardhjslowvideo behind powerpoolhardhjfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerpoolhjslowvideo
hide powerpoolhardhjfastvideo
with dissolve
$ powerpooltalkfastx = False
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen powerpoolpoundslowx()
screen powerpoolpoundslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolCumx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolSlowx")

label PowerPoolHardFastx:
hide cum
hide faster
hide slower
hide harder
hide softer
if powerpooltalkfastx == False:
    pg "I think I need to go a little FASTER on that shaft, it's just BEGGING for it!"
    $ powerpooltalkfast = True
if powerpoolpoundtalkx == False:
    mc "Please Kara... I need some release soon!"
    if age >= 20:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT monster schlong?"
    if age >= 18 and age <= 19:
        pg "Oooh, you want me to go HARDER on your giant cock, [name]? You want POWERGIRL to use her POWERGRIP on your FAT teenage monster schlong?"
    window hide
    $ powerpoolpoundtalkx = True
show powerpoolhardhjfastvideo behind powerpoolhardhjslowvideo
show powerpoolhardhjfastvideo behind powerpoolhjfastvideo
$ renpy.pause(1.0, hard='True') 
hide powerpoolhardhjslowvideo
hide powerpoolhjfastvideo
with dissolve
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerpoolpoundfastx()
screen powerpoolpoundfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolHardSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolCumx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolFastx")

label PowerPoolCumx:
window hide
hide cum
hide slower
hide faster
mc "Kara, I'm... about to..."
scene powerpoolhandjobcum01 with dissolve
stop channel1
play sound "sounds/boymoan04.mp3"
mc "... BLOW! AAAH!"
window hide
with hpunch
pg "That's it, release all that pent-up scum for your landlady's daughter!"
scene powerpoolhandjobcum02 with dissolve
stop music
play music "sounds/waterrun.mp3"
play sound "sounds/boymoan05.mp3"
pg "Ooh, you're cumming so HARD, your plumes of SPUNK are erupting right through the water!"
window hide
with fastflash
mc "RHAAAA! Blasting at FULL ALPHA-POWER!"
scene powerpoolhandjobcum03 with dissolve
play sound "sounds/boyorgasm01.mp3"
pg "Keep PUMPING all that nasty spunk, [name]! I LOVE IT when you cum like a STALLION!"
window hide
with fastflash
mc "Oh God, Kara, I'm..."
scene powerpoolhandjobcum03 with dissolve
play sound "sounds/boymoan05.mp3"
pg "...BLASTING at FULL STRENGTH? Yeah, I can see that..."
window hide
with fastflash
mc "AAAAH, it's so GOOD!!!!"
scene powerpoolhandjobcum04 with dissolve
pg "Oh my God, look at THAT SHOT! It's just GIGANTIC!"
window hide
with hpunch
pg "My expert POWER hand is just EMPTYING your balls, isn't it?"
scene powerpoolhandjobcum05 with dissolve
play sound "sounds/boymoan03.mp3"
pg "Still spewing that FAT load, [name]? Spewing that MONSTER LOAD for little me?"
window hide
with fastflash
pg "Look at you, you're COVERED in your own slime! That's just so FILTHY!"
scene powerpoolhandjobcum06 with dissolve
stop channel1
stop sound
pg "You're swimming in a puddle of your own cum. You're gonna have to clean the pool after this MIGHTY ORGASM, [name]!"
mc "Rrrrhoo..."
mc "Is that all you can say? After your landlady's daughter gave you such a POWERFUL handjob?"
scene powerpoolhandjobcum07 with dissolve
pg "I'll help you clean up just a bit before I go..."
play sound "sounds/slurp.mp3"
pg "Mmmh, [hero]'s spunk certainly has an ALPHA-TASTE! Goodnight, [name]!"
mc "Gggg..."
stop channel2
stop channel1
stop music
jump PowerGallery

label PowerGallery04:
stop channel3
scene compoundpowermc00 with fade
play music "sounds/waterrun.mp3"
mc "Oh, Kara is relaxing in the pool."
scene compoundpowermc01 with dissolve
mc "She looks so peaceful, with her big gazoongas sticking out of the water like that..."
scene compoundpowermc02 with dissolve
mc "Therefore, it's the perfect opportunity to play a trick on her. GERONIMO!"
scene compoundpowermc03 with dissolve
play sound "sounds/diving.mp3"
mc "Shit, she plunged under the surface just in the nick of time!"
scene compoundpowermc04 with dissolve
play music "sounds/underwater.mp3"
mc " * But I see her, she won't escape me! *"
scene compoundpowermc05 with dissolve
if mcagility >= 1:
    mc " * Come on, my Super-Agility should be enough... *"
if mcagility == 0:
    mc " * She's trying to use her Super-Agility to evade me... *"
scene compoundpowermc06 with dissolve
mc "* Almost, just a few inches... *"
scene compoundpowermc07 with dissolve
play music "sounds/waterrun.mp3"
pg "Not fast enough, [name]!"
scene compoundpowermc08 with dissolve
play sound "sounds/diving.mp3"
play music "sounds/underwater.mp3"
mc "* Damn, where did she go? * "
scene compoundpowermc09 with dissolve
pg "* Got you, [name]! *"
mc "* AAARGH! She's holding me in a tight armlock! And my Super-Strength is... Gotta tense all my MUSCLES... *"
scene compoundpowermc10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "* My Super-Cock is also getting tense, her armlock is making all the blood RUSH to it! *"
play sound "sounds/ripping.mp3"
mc "* Uh oh... My speedo is about to get ripped apart... *"
scene compoundpowermc11 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "I need to get out of that armlock, I can't breathe!"
scene compoundpowermc12 with dissolve
play music "sounds/waterrun.mp3"
pg "Do you give up yet [name]? You might be Super-Stronger than me, but I have the advantage and you're out of breath!"    
scene compoundpowermc20
play sound "sounds/mangrunt01.mp3"
mc "RHAAA! No, I WON'T GIVE UP!"
pg "Oh my God, you're so POWERFUL!"
scene compoundpowermc21 with dissolve
mc "Now [hero] has the UPPER HAND!"
pg " * cough * You're choking me [name], please be careful!"
mc "I will, I don't want to damage my SEXUAL GOODS!"
scene compoundpowermc22 with dissolve
play channel1 "sounds/sexy06.mp3"
pg "I'm totally at the mercy of your HUGE muscles now! What are you going to do to poor little me after I teased you so much?"
mc "You're NAUGHTY, Kara! And a naughty girl needs to be PUNISHED!"
scene compoundpowermc23 with dissolve
play sound "sounds/ripping.mp3"
pg "Hey, you're RIPPING my bikini top!"
mc "That's right, I want access to those sumptuous FUNBAGS!"
scene compoundpowermc24:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "I need some superhero tiddy milk!"
pg "Why would I be making breast milk?"
mc "Cos you're a SUPERHEROINE and I WANT tiddy milk! So GIVE ME TIDDY MILK!"
label PowerPoolBreastSlowx:
hide nexticon
hide faster
hide slower
pg "If you're prepared to work for it..."
play channel2 "sounds/moan02.mp3"
window hide
show powerpoolbreastslowvideo behind powerpoolbreastfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolbreastfastvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen powerpoolbreastslowbx()
screen powerpoolbreastslowbx():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("PowerPoolBreastFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolBreastEndx")

label PowerPoolBreastFastx:
hide faster
hide slower
hide nexticon
play sound "sounds/moan03.mp3"
pg "Mmmh, do it faster, [name], I think it might be coming..."
window hide
show powerpoolbreastfastvideo behind powerpoolbreastslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolbreastslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen powerpoolbreastfastbx()
screen powerpoolbreastfastbx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("PowerPoolBreastSlowx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolBreastEndx")

label PowerPoolBreastEndx:
hide nexticon
mc "Gimme gimme gimme!"
stop channel2
scene powerpoolbreastmilk01 with dissolve
play sound "sounds/moan03.mp3"
pg "AAAH, I'm lactating!"
window hide
with fastflash
mc "Mmmh, fill up my mouth, Kara!"
scene powerpoolbreastmilk02 with dissolve
play sound "sounds/slurp.mp3"
pg "You're so... NAUGHTY! Licking my breast like that, I..."
window hide
with hpunch
play sound "sounds/moan06.ogg"
pg "... I'm CUMMMING! AAAH!"
scene powerpoolbreastmilk03 with dissolve
mc "That was really... * swallow* tasty..."
pg "Can I go now, please?"
scene powerpoolbreastmilk04 with dissolve
mc "Yeah, OK, let me just admire the view as you leave the pool, Kara..."
scene powerpoolbreastmilk05:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "I'm sorry to be leaving you with such a great big HARDON, [name]! I guess you'll have to take care of it yourself this time..."
scene powerpoolbreastmilk06 with dissolve
mc "Yeah, I'm so fucking hard. Hopefully, this scene will be expanded in the future when I feel BAD enough to force her into giving me a BJ..."
stop channel2
stop channel1
stop music
jump PowerGallery

label PowerGallery05:
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

label PowerSuperSlowx:
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
call screen powersuperslowx()
screen powersuperslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlowx")

label PowerSuperFastx:
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
call screen powersuperfastx()
screen powersuperfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFastx")

label PowerSuperFrontSlowx:
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
call screen powersuperfrontslowx()
screen powersuperfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlowx")

label PowerSuperFrontFastx:
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
call screen powersuperfrontfastx()
screen powersuperfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFastx")

label PowerSuperEndx:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
pg "[name] is being a naughty boy, he's rubbing himself while he's admiring the show..."
sg "A NAUGHTY, DIRTY boy! Knowing that he's getting hard watching us makes me want to cum..."
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
sg "But... You're all DIRTY with my juices, Kara. I need to clean up my mess.."
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
jump PowerGallery

label PowerGallery06:
stop channel3
scene gymmcprecurl01
mc "Let's get rid of this ridiculously light barbell and use Superman's iridium dumbbells instead. They weigh over 10 TONS each and I feel SUPER-STRONG right now!"
play channel2 "sounds/effort01.mp3"
play channel2 "sounds/effort01.mp3"
show gymmccurlsoftvideo with dissolve
window hide
pause
mc "Fuck yeah! I can feel the blood PUMPING..."
window hide
$ renpy.pause(1.0, hard='True')
show gymmccurlgettingvideo
hide gymmccurlsoftvideo
with fastdissolve
$ renpy.pause(1.8, hard='True')
scene gymmccurlerect
play sound "sounds/thud.mp3"
mc "...PUMPING EVERYWHERE! So fucking hard, gonna continue like this!"
window hide
show gymmccurlhardvideo
pause
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
scene mccurlpower05 with dissolve    
pg "So if I grind my tight ass against your giant dangling boulders like this, you won't get distracted?"
play sound "sounds/effort01.mp3"
mc "Ggg... No... I'm still pumping... iron..."
scene mccurlpower06 with dissolve    
pg "What if I squeeze your balls like this with my knee? A TRUE superhero can ignore the pain."
play sound "sounds/boymoan02.mp3"
mc "I... don't feel... a thing... * puff * I... can keep on... going..."
scene mccurlpower07 with dissolve    
pg "But can a superhero ignore the warm sensation of a soft mouth on his cum factories?"
mc "Wh... what?"
scene mccurlpower08 with dissolve    
play sound "sounds/lick03.mp3"
mc "Oh God... Still going though, you won't stop  me from doing my reps Kara!"
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
pg "But you're still ssooo HARD! That was just a little premature ejaculation, you still have a LOT of pent-up baby sauce left over in those fat balls, haven't you?"
scene mccurlballcum04 with dissolve
pg "I think I have an idea of what to do with this monstrous thing that just won't go down..."
mc "Wh... what are you doing Kara?"
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
$ powertitslowx = False
$ powertitsensesx = False
call screen usepower("usesenses", "McCurlTitSlowx", "McCurlTitSlowSensesPrex") with dissolve

label McCurlTitSlowx:
$ powertitfastx = False
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
scene gymbackgroundnight
show mccurltitslowvideo
with fastdissolve
pg "You like it when my tits slowly rub against your fat shaft don't you? You're DROOLING pre-cum all over the place!"
window hide
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
if powertitsensesx == True:
    show nudeicon:
        xpos 50 ypos 500  
call screen mccurltitslowx()
screen mccurltitslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitFastx")
    if powertitsensesx == True:
        button:
            xpos 50
            ypos 500
            xysize(100, 60)        
            action Jump ("McCurlTitSlowSensesx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEndx")

label McCurlTitFastx:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
if powertitfastx == False:
    pg "I want you to curl those 10 tons dumbbells FASTER! Show me how STRONG you are!"
    window hide
    $ powertitfastx = True
scene gymbackgroundnight
show mccurltitfastvideo
with fastdissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
if powertitsensesx == True:
    show nudeicon:
         xpos 1700 ypos 500    
call screen mccurltitfastx()
screen mccurltitfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitSlowx")
    if powertitsensesx == True:
        button:
            xpos 1700
            ypos 500
            xysize(100, 60)        
            action Jump ("McCurlTitFastSensesx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEndx")

label McCurlTitSlowSensesPrex:
hide mccurltitslowvideo
show mccurltitslowsensesvideo
with fastdissolve

label McCurlTitSlowSensesx:
$ powertitsensesx = True
$ powertitfastx = False
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
if powertitsensesx == True:
    show nonudeicon:
        xpos 50 ypos 500  
call screen mccurltitslowsensesx()
screen mccurltitslowsensesx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitFastSensesx")
    if powertitsensesx == True:
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("McCurlTitSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEndx")

label McCurlTitFastSensesx:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
if powertitfastx == False:
    pg "I want you to curl those 10 tons dumbbells FASTER! Show me how STRONG you are!"
    window hide
    $ powertitfastx = True
scene gymbackgroundnight
show mccurltitfastsensesvideo
with fastdissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500    
if powertitsensesx == True:
    show nonudeicon:
         xpos 1700 ypos 500    
call screen mccurltitfastsensesx()
screen mccurltitfastsensesx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("McCurlTitSlowSensesx")
    if powertitsensesx == True:
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("McCurlTitFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("McCurlTitEndx")

label McCurlTitEndx:
hide cum
hide slower
hide faster
hide nudeicon
hide nonudeicon
pg "Look at you, you're ready to burst aren't you? Your ENORMOUS fuckstick is convulsing between my soft pillows..."
mc "Uh... Aahh..."
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
pg "You still want to BLAST away and give me MORE. Give ALL YOU HAVE to your landlady's daughter!"
scene mccurltitcum04 with dissolve
pg "Look at you, you're CAKED in your own slimy spunk and you just won't let up."
window hide
with fastflash
pg "You just keep cumming and cumming, like a sperm hose at FULL BLAST!"
scene mccurltitcum05 with dissolve
pg "Maybe I should aim your GIANT spunk plumes closer to your face... So you can give yourself a bukkake facial!"
window hide
with fastflash
mc "UUUH, AAAH, it's landing right on my face!"
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
pg "Yes, you do, you need to get your power back. For tomorrow. You might get drained AGAIN! Goodnight, [name]!"
stop channel2
stop channel1
stop music
jump PowerGallery

label PowerGallery07:
stop channel3
stop music
play music "sounds/sexy09.mp3"
scene powerlingeriebackground01
show powerhot01:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerhot01 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
mc "Wow, this set is really HOT, Kara!"
window hide
hide powerhot01
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerhot02:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerhot02 at powerfulldown02
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Really, you like it? You're not just saying that to get inside my panties?"
mc "I mean it. AND I want to get into your panties."
scene powerlingeriebackground01 blurred
show powerhot03a
with dissolve
pg "Does it showcase my MUSCLES well enough?"
mc "I can see your abs CLEARLY."
window hide
hide powerhot03a
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerhot03b:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 blurred at widowfullbackzoombackground
show powerhot03b at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "And now I can see them TENSING and your biceps BULGING!"
scene powerlowbackground
show powerhot04
with dissolve
pg "And is YOUR muscle tensing [name]? * wink *"
mc "It's tensing, it's tensing fast and HARD!"
hide powerhot04
show powerhot05
with dissolve
pg "So you're telling me you're getting a great big hardon from looking at your landgirl posing in sexy lingerie?"
mc "Well, err..."
hide powerhot05
show powerhot06
with dissolve
pg "Pull it out then, I want to see how HARD I make you. And it better be TITANIUM-HARD!"
mc "I'll show you, Kara, I'll show you, I'll get totally TITANIUM-HARD for you!"
hide powerhot06
show powerhot07
with dissolve
pg "And if you ARE as HARD as I want you to be, maybe I'll take my bra off for you..."
scene powerhot08 with dissolve
pg "I'll give you a sneak peek... Cos you're such a naughty boy."
scene powerhot09 with dissolve
play sound "sounds/wow.mp3"
pg "Wow, you really are SUPER-HARD for me..."
mc "You've got to do something about it, I don't know how long I can..."
scene powerhot10:
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "... You poor thing, you need some relief, don't you? You'd love to stick that big fat pile-driver right up my wet pussy, wouldn't you?"
mc "Yes, YES, I NEED TO! I beg you, Kara!"
scene powerhot11 with dissolve
play sound "sounds/kiss.mp3"
pg "Just kiss me first, silly boy, try and make this WORTH it for me too..."
scene powerhot12 with dissolve
play sound "sounds/kiss.mp3"
pg "That's it, with your tongue, I LOVE French-kissing... While I grind my butt on your ROCK-HARD shaft..."
scene powerhot13 with dissolve
play sound "sounds/boymoan02.mp3"
mc "Please, Kara, let me put it inside you..."
scene powerhot14 with dissolve
pg "Not yet cowboy, what would be the fun in that? I want to take it SLOWLY. Meaning, I'll use my lovely feet first..."
play channel1 "sounds/wetmassage.mp3"
$ powerhottalkslowx = False

label PowerFootHotSlowx:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootslowvideo behind powerfootfastvideo
show powerfootslowvideo behind powerfootsideslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootfastvideo
hide powerfootsideslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerhottalkfastx = False
if powerhottalkslowx == False:
    pg "I'm in control now, [name]. In control of YOUR horny [age]yo MONSTERCOCK!"
    $ powerhottalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powerfootslowx()
screen powerfootslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootHotFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSideSlowx")

label PowerFootHotFastx:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootfastvideo behind powerfootslowvideo
show powerfootfastvideo behind powerfootsidefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootslowvideo
hide powerfootsidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerhottalkslowx = False
if powerhottalkfastx == False:
    pg "You need some sweet relief, don't you? Let my feet take you over the edge, give me a truly SUPERHERO load of sweet young cum!"
    $ powerhottalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powerfootfastx()
screen powerfootfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootHotSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootHotEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootSideFastx")

label PowerFootSideSlowx:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootsideslowvideo behind powerfootslowvideo
show powerfootsideslowvideo behind powerfootsidefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootslowvideo
hide powerfootsidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerhottalkfastx = False
if powerhottalkslowx == False:
    pg "I'm in control now, [name]. In control of YOUR horny [age]yo MONSTERCOCK!"
    $ powerhottalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootsideslowx()
screen powerfootsideslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootSideFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootHotSlowx")

label PowerFootSideFastx:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootsidefastvideo behind powerfootfastvideo
show powerfootsidefastvideo behind powerfootsideslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsideslowvideo
hide powerfootfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerhottalkslowx = False
if powerhottalkfastx == False:
    pg "You need some sweet relief, don't you? Let my feet take you over the edge, give me a truly SUPERHERO load of sweet young cum!"
    $ powerhottalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerfootsidefastx()
screen powerfootsidefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSideSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootHotEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootHotFastx")

label PowerFootHotEndx:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
pg "Are you going to spew that filthy load yet? I think you REALLY need to, don't you?"
mc "Oh Kara, I'm gonna cum, gonna cum so much for you!"
scene powerhotfootcum01 with dissolve
mc "FUCK, here it comes, AAAH!"
stop channel2
play channel2 "v031/boyorgasm02.mp3"
window hide
with hpunch
pg "Mmmh, yeah, I love seeing that great big fat donkey-cock CONVULSING with pleasure!"
scene powerhotfootcum02 with dissolve
pg "Look at all that yummy spunk, you're really giving your naughty landgirl a BIG load, aren't you?"
window hide
with fastflash
mc "I am Kara, just for YOOOOOUUUU, AAAAH!"
scene powerhotfootcum03 with dissolve
pg "But it's not enough, I want MORE, give me MORE!"
window hide
with hpunch
mc "Your feet are DRAINING me, RHAAA!"
scene powerhotfootcum04 with dissolve
pg "Give me a few more POWERFUL SHOTS, [name]! I know you can do it! Do it for your LANDLADY'S DAUGHTER!"
window hide
with fastflash
pg "MORE!"
scene powerhotfootcum03 with dissolve
pg "That's it, let it ALL out, [name]..."
window hide
with hpunch
pg "You're such a good boy, pumping all that sweet cum just for me..."
stop channel2
stop channel1
scene powerhotfootcum05 with dissolve
play sound "sounds/panting.mp3"
pg "Now, your giant cock had better not go soft on me..."
scene powerhotfootcum06 with dissolve
play sound "sounds/slurp.mp3"
pg "Cos I have MUCH MORE in store for it..."
scene powerhotfootcum07 with dissolve
pg "But I should really take my panties off if you plan to get that rod inside me, right?"
mc "Oh God, Kara..."
scene powerhotfootcum08 with dissolve
if age >= 20:
    pg "You're still so HARD for me! My feet didn't pump enough cream out of your giant cum factories after all..."
if age >= 18 and age <= 19:
    pg "You're still so HARD for me! My feet didn't pump enough cream out of your giant teenage cum factories after all..."
scene powerhotfootcum09 with dissolve
play sound "sounds/lick03.mp3"
pg "Maybe I should help you replenish them to FULL CAPACITY. With MY cream! Hi hi!"
scene powerhotfootcum10 with dissolve
play sound "sounds/slurp.mp3"
pg "That's it, suck up that milk, it will make you STRONG [name]! * giggles*"
scene powerhotfootcum11 with dissolve
pg "So are you ready for another round of TEASING and CUMMING, [name]?"
mc "As long as it involved your crotch teasing my pussy and my cock cumming INSIDE you!"
scene powerhotfootcum12 with dissolve
pg "You've got it half-right, naughty landboy! I'll show you..."
window hide
play channel1 "sounds/wank.mp3"
$ powerridetalkslowx = False

label PowerRideHotSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerrideslowvideo behind powerridefastvideo
show powerrideslowvideo behind powerridepovslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerridefastvideo
hide powerridepovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerridetalkfastx = False
if powerridetalkslowx == False:
    mc "You're rubbing your clit on my shaft Kara, Oh God..."
    pg "That's the teasing idea, [name]!"
    $ powerridetalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerrideslowx()
screen powerrideslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideHotFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRidePOVSlowx")

label PowerRideHotFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridefastvideo behind powerrideslowvideo
show powerridefastvideo behind powerridepovfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerrideslowvideo
hide powerridepovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerridetalkslowx = False
if powerridetalkfastx == False:
    if age >= 20:
        pg "I should really do it faster now, cos your giant dong just NEEDS to come, doesn't it?"
    if age >= 18 and age <= 19:
        pg "I should really do it faster now, cos your giant teenage dong just NEEDS to come, doesn't it?"
    $ powerridetalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerridefastx()
screen powerridefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideHotSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerRideHotEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRidePOVFastx")

label PowerRidePOVSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridepovslowvideo behind powerrideslowvideo
show powerridepovslowvideo behind powerridepovfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerrideslowvideo
hide powerridepovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerridetalkfastx = False
if powerridetalkslowx == False:
    mc "You're rubbing your clit on my shaft Kara, Oh God..."
    pg "That's the teasing idea, [name]!"
    $ powerridetalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerridepovslowx()
screen powerridepovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRidePOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideHotSlowx")

label PowerRidePOVFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridepovfastvideo behind powerridefastvideo
show powerridepovfastvideo behind powerridepovslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerridepovslowvideo
hide powerridefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerridetalkslowx = False
if powerridetalkfastx == False:
    if age >= 20:
        pg "I should really do it faster now, cos your giant dong just NEEDS to come, doesn't it?"
    if age >= 18 and age <= 19:
        pg "I should really do it faster now, cos your giant teenage dong just NEEDS to come, doesn't it?"
    $ powerridetalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerridepovfastx()
screen powerridepovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRidePOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerRideHotEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideHotFastx")

label PowerRideHotEndx:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
pg "Looks like my teasing is going to push you over the edge. AGAIN!"
scene powerridecum01 with dissolve
stop channel1
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "YES IT IS, AAAH!"
window hide
with fastflash
pg "Mmmh, I love it when you BLAST so POWERFULLY for me!"
scene powerridecum02 with dissolve
play sound "sounds/moan02.mp3"
pg "That's it, cover my tits in your warm cream!"
window hide
with hpunch
pg "Ooh, you're CONVULSING, aren't you? Convulsing with pleasure for your teasing landgirl!"
scene powerridecum03 with dissolve
mc "OOOOH, AAAH!"
window hide
with fastflash
pg "You just want to come and come and never stop, don't you?"
scene powerridecum04 with dissolve
mc "Oh God, Kara..."
window hide
with hpunch
pg "That great big [age]yo horsecock is just aching to empty its nasty nut, isn't it?"
scene powerridecum05 with dissolve
pg "Come on, I know you have a few shots left in those giant cum boulders of yours!"
window hide
with fastflash
mc "Ggg... I... I can't anymore..."
scene powerridecum06 with dissolve
stop channel2
stop channel1
play sound "sounds/panting.mp3"
pg "You're not tired, are you [name]? Cos you still haven't put your massive 18-incher up my fuckhole..."
mc "Oh God..."
scene powerridecum07 with dissolve
pg "Look at you, you're STILL HARD just thinking about sticking your huge pud up my hungry hole... Such a dirty boy..."
scene powerridecum08 with dissolve
pg "Now it's time for me to ride this wild beast and REALLY tame it like I did last time, [name]!"
scene powerridecum08 with dissolve
play sound "sounds/slurp.mp3"
pg "But first, I'll clean up the aftermath of your second MONSTER LOAD..."
scene powerridecum09 with dissolve
mc "Yeah, fuck, that's keeping me ROCK-HARD for you, Kara!"
pg "I want to check this myself. Hold me in your muscular arms, [name]..."
scene powerridecum10 with dissolve
pg "Mmh... I can FEEL its hardness, but... Can it STAY the course? If I rub my hungry snatch all over it?"
mc "I... err."
play channel1 "sounds/boymoan02.mp3"
play channel2 "sounds/wetmassage.mp3"
window hide

$ powerdicktoldx  = False

label PowerDickSlowx: 
hide nexticon
hide faster
hide slower
show powerdickslowvideo behind powerdickfastvideo
pause 1.0
hide powerdickfastvideo with dissolve
if powerdicktoldx == False:
    pg "Yeah, it does feel quite HARD, doesn't it?"
    window hide
    $ powerdicktoldx = True
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen powerdickslowx()
screen powerdickslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerDickFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerDickEndx")

label PowerDickFastx:
show powerdickfastvideo behind powerdickslowvideo
hide nexticon
hide faster
hide slower
pg "But what if I grind my ass on it a bit HARDER and FASTER? Will it hold up?"
mc "I..."
hide powerdickslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen powerdickfastx()
screen powerdickfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerDickSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerDickEndx")

label PowerDickEndx:    
hide nexticon
hide slower
hide faster
pg "Well done [name]... You stayed ROCK-HARD for Powergirl. I hope it was good for you!"
scene powerdickcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
pg "Ooh, it WAS good for you, wasn't it?"
window hide
with fastflash
play sound "sounds/wow.mp3"
pg "You can't help but spurt some great big globs of yummy spunk from me grinding on your fat [age]yo donkey-dick!"
stop sound
play sound "sounds/boymoan.mp3"
$ renpy.pause(0.5, hard='True')
scene powerdickcum02 with dissolve
stop channel1
play sound "sounds/boymoan02.mp3"
pg "Are you done wih those  pre-orgasmic spurts? Mmmh, now you're going to be ROCK-HARD for me for a LONG TIME!"
pg "It's just what I wan..."
scene powerprefuck01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with dissolve
pg "...Ooh, look at you, you're so HORNY, you've decided to MANHANDLE your poor landlady's daughter?"
mc "That's right, I can't take it any more, you've teased me too much Kara!"
scene powerprefuck02 with dissolve
pg "Are you going to REALLY give it to me? To really POUND my poor little pussy to total oblivion with your massive cunt-splitter?"
play sound "sounds/thud.mp3"
scene powerprefuck03 with dissolve
mc "Feel how fucking heavy and hard my cock feels! This is going to SPLIT you in two!"
scene powerprefuck02 with dissolve
pg "Do it again, I NEED to feel its POWER!"
window hide
play music ["sounds/thud.mp3", "<silence .75>"]
scene powercockslap
pause
pg "Now SHOW ME, DRILL MY HOLE, you horse-hung STUD!"
stop music

label PowerFuckSlowx:
$ powerharderx = False
window hide
show powershortslowvideo behind powershortfastvideo
show powershortslowvideo behind powershortpovslowvideo
show powershortslowvideo behind powerhardslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powershortfastvideo
hide powershortpovslowvideo
hide powerhardslowvideo
hide nexticon
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
call screen powershortslowx()
screen powershortslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckPOVSlowx")

label PowerFuckFastx:
$ powerharderx = False
window hide
show powershortfastvideo behind powershortslowvideo
show powershortfastvideo behind powershortpovfastvideo
show powershortfastvideo behind powerhardfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powershortslowvideo
hide powershortpovfastvideo
hide powerhardfastvideo
hide nexticon
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
call screen powershortfastx()
screen powershortfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckPOVFastx")

label PowerFuckPOVSlowx:
$ powerharderx = False
window hide
show powershortpovslowvideo behind powershortslowvideo
show powershortpovslowvideo behind powershortpovfastvideo
show powershortpovslowvideo behind powerhardpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powershortslowvideo
hide powershortpovfastvideo
hide powerhardpovslowvideo
hide nexticon
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
call screen powershortpovslowx()
screen powershortpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckSlowx")

label PowerFuckPOVFastx:
$ powerharderx = False
window hide
show powershortpovfastvideo behind powershortpovslowvideo
show powershortpovfastvideo behind powershortfastvideo
show powershortpovfastvideo behind powerhardpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powershortpovslowvideo
hide powershortfastvideo
hide powerhardpovfastvideo
hide nexticon
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
call screen powershortpovfastx()
screen powershortpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckFastx")

label PowerHardSlowx:
if powerharder == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharderx = True        
window hide
show powerhardslowvideo behind powerhardfastvideo
show powerhardslowvideo behind powerhardpovslowvideo
show powerhardslowvideo behind powershortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powerhardfastvideo
hide powerhardpovslowvideo
hide powershortslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerhardlowx()
screen powerhardlowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEndx")

label PowerHardFastx:
if powerharderx == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharderx = True        
window hide
show powerhardfastvideo behind powerhardslowvideo
show powerhardfastvideo behind powerhardpovfastvideo
show powerhardfastvideo behind powershortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerhardfastx()
screen powerhardfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEndx")

label PowerHardPOVSlowx:
if powerharderx == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharderx = True        
window hide
show powerhardpovslowvideo behind powerhardslowvideo
show powerhardpovslowvideo behind powerhardpovfastvideo
show powerhardpovslowvideo behind powershortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortpovslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerhardpovslowx()
screen powerhardpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEndx")

label PowerHardPOVFastx:
if powerharderx == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharderx = True        
window hide
show powerhardpovfastvideo behind powerhardpovslowvideo
show powerhardpovfastvideo behind powerhardfastvideo
show powerhardpovfastvideo behind powershortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powerhardpovslowvideo
hide powerhardfastvideo
hide powershortpovfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerhardpovfastx()
screen powerhardpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEndx")

label PowerFuckEndx:
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
pg "Now I don't want you to come just yet, so pull out your donkey-dick, I'm gonna RIDE you like a wild bronco!"
mc "I'm so close though, so, so very close..."
pg "PULL OUT GODAMMIT!"
mc "Oh God, too late, I..."
play sound "sounds/boymoan05.mp3"
show powerpullcumend behind powerpullanimvideo
hide powerhardfastvideo
hide powershortpovfastvideo
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortpovslowvideo
hide powerhardpovslowvideo
hide powershortslowvideo
hide powershortpovfastvideo
hide powershortfastvideo
show powerpullanimvideo
with fastdissolve
$ renpy.pause(1.33, hard='True')
scene powerpull01 with dissolve
stop channel1
play sound "sounds/boymoan02.mp3"
pg "That's just... NASTY! You just blurped a great big wad of cum on my tummy! My pussy was just sooo enticing, wasn't it?"
mc "Y... yes, I just couldn't hold off... Sorry, Kara..."
scene powerpull02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "Now you're going to have to make it up to me, I'm going to RIDE YOU TILL YOU SPEW A GIANT BOYLOAD!"
mc "Uh oh..."
scene powerfuckpreride01 with dissolve
pg "Just keep that great big [age]yo whopper steady..."
scene powerfuckpreride02 with dissolve
play sound "sounds/moan04.ogg"
pg "It's so BIG! AAAH!!!"
mc "That's just my helmet Kara. You've got 15 more inches to go."
scene powerfuckpreride03 with dissolve
pg "You think I'm scared? Powergirl is NEVER scared, I'll prove it to you!"

$ powercowgirltalkslowx = False

label PowerCowgirlSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlslowvideo behind powercowgirlfastvideo
show powercowgirlslowvideo behind powercowgirlfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powercowgirlfastvideo
hide powercowgirlfrontslowvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkfastx = False
if powercowgirltalkslowx == False:
    mc "That's it, you've getting the hang of it, nice and slow..."
    $ powercowgirltalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powercowgirlslowx()
screen powercowgirlslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerCowgirlFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideFrontSlowx")

label PowerCowgirlFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfastvideo behind powercowgirlslowvideo
show powercowgirlfastvideo behind powercowgirlfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powercowgirlslowvideo
hide powercowgirlfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkslowx = False
if powercowgirltalkfastx == False:
    mc "Damn Kara, you're really riding my dong now!"
    if age >= 20:
        pg "* puff * I told... you... Powergirl can take it... All your FAT INCHES!"
    if age >= 18 and age <= 19:
        pg "* puff * I told... you... Powergirl can take it... All your FAT TEENAGE INCHES!"
    $ powercowgirltalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powercowgirlfastx()
screen powercowgirlfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerCowgirlSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerCowgirlEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideFrontFastx")

label PowerRideFrontSlowx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfrontslowvideo behind powercowgirlslowvideo
show powercowgirlfrontslowvideo behind powercowgirlfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powercowgirlslowvideo
hide powercowgirlfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkfastx = False
if powercowgirltalkslowx == False:
    mc "That's it, you've getting the hang of it, nice and slow..."
    $ powercowgirltalkslowx = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powercowgirlfrontslowx()
screen powercowgirlfrontslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideFrontFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerCowgirlSlowx")

label PowerRideFrontFastx:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfrontfastvideo behind powercowgirlfastvideo
show powercowgirlfrontfastvideo behind powercowgirlfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powercowgirlfrontslowvideo
hide powercowgirlfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkslowx = False
if powercowgirltalkfastx == False:
    mc "Damn Kara, you're really riding my dong now!"
    if age >= 20:
        pg "* puff * I told... you... Powergirl can take it... All your FAT INCHES!"
    if age >= 18 and age <= 19:
        pg "* puff * I told... you... Powergirl can take it... All your FAT TEENAGE INCHES!"
    $ powercowgirltalkfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powercowgirlfrontfastx()
screen powercowgirlfrontfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerCowgirlEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerCowgirlFastx")

label PowerCowgirlEndx:
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
pg "I want you to COME now [name], the BIGGEST LOAD OF CUM YOU CAN MUSTER FOR ME!"
mc "But... I..."
scene powerridefuckcum01 with dissolve
pg "CUM NOW FOR POWERGIRL!"
play sound "sounds/splooge02.mp3"
stop channel2
window hide
with hpunch
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAH!"
scene powerridefuckcum02 with dissolve
play sound "sounds/splooge01.mp3"
pg "That's it, just KEEP PUMPING THAT SPUNK INSIDE ME!"
window hide
with fastflash
mc "My balls... they're EXPLODING, RHAAA!"
scene powerridefuckcum03 with dissolve
play sound "sounds/womancum01.mp3"
pg "Let me make them BURST even more then!"
window hide
with hpunch
mc "AAAAH, this is sssooo GOOOOOD!"
scene powerridefuckcum04 with dissolve
play sound "sounds/splooge03.mp3"
pg "Powergirl's pussy is just the BEST pussy, isn't it?"
window hide
with fastflash
mc "Y... YES, UUUUH, BLASTING SOME MORE!"
scene powerridefuckcum03 with vpunch
play sound "sounds/splooge01.mp3"
pg "Good, cos I want you to COME some more!..."
scene powerridefuckcum04 with dissolve
play sound "sounds/splooge03.mp3"
pg "... To TOTALLY EMPTY YOUR BALLS FOR ME!"
scene powerridefuckcum03 with vpunch
play sound "sounds/splooge01.mp3"
pg "KEEP PUMPING YOUR SEED UNTIL I TELL YOU STOP!"
scene powerridefuckcum05 with dissolve
mc "OOOOH, I'm..."
window hide
with hpunch
pg "...not yet giving up on me, IS THAT CLEAR?"
scene powerridefuckcum06 with dissolve
pg "I can feel your cream sloshing inside me [name], just KEEP IT UP!"
window hide
with fastflash
mc "AAAAH! I can't... I'm..."
scene powerridefuckcum07 with dissolve
stop channel2
play sound "sounds/splooge01.mp3"
pg "... DRAINED by Powergirl!"
scene powerridefuckcum08 with dissolve
play sound "sounds/panting.mp3"
pg "Well, look at you. You look like a tired superhero. I suppose after that MANY loads, I can let you go back to your room."
play sound "sounds/panting.mp3"
mc "Ggg... Thanks Kara."
stop channel2
stop channel1
stop music
jump PowerGallery

label PowerGallery08:
stop channel3
scene compoundpooldaybackground
show powerpoolnew01
with fade
mc "Oooh, Kara is here. In a *HOT* new bikini..."
hide powerpoolnew01
show powerpoolnew02
with fastdissolve
pg "I Super-Sensed you behind my back, [name]..."
hide powerpoolnew02
show powerpooleyeblink
with dissolve
mc "Ah, yeah, you're good at that."
pg "I'm the GOAT at that."
mc "That's a HOT bikini you got there, Kara..."
hide powerpooleyeblink
show powerpoolnew04 at centerleft
with fastdissolve        
pg "You like it? Maybe you deserve a closer look then..."
stop music
play music "sounds/sexy06.mp3"
window hide
scene compoundpooldaybackground blurred:
    zoom 1.9 xoffset -400 yoffset 0
show powergirlpoolnew01:
    xoffset 0 yoffset 0
show compoundpooldaybackground blurred at powerfulldownbackground
show powergirlpoolnew01 at harleyfulldown
with dissolve
$ renpy.pause(4.0, hard='True')
pg "A closer look at how it hugs my shapely rump like a second skin..."
mc "Ooh, mamma mia!"
scene compoundpooldaybackground blurred:
    zoom 1.9 xoffset -400 yoffset -900
show powergirlpoolnew02:
    xoffset 0 yoffset -1080
show compoundpooldaybackground blurred at poolbackgroundup
show powergirlpoolnew02 at poolbackgroundpowerup
with dissolve
$ renpy.pause(4.0, hard='True') 
pg "And how it maintains my large breasts in a tight confine..."
mc "They need to get OUT of that tight confine!"
pg "Not yet, don't hurry things..."
scene compoundpooldaybackground blurred:
    zoom 1.9 xoffset -400 yoffset 0
show powergirlpoolnew03:
    xoffset 0 yoffset 0
show compoundpooldaybackground blurred at powerfulldownbackground
show powergirlpoolnew03 at harleyfulldown
with dissolve
$ renpy.pause(4.0, hard='True')
pg "But I'll give you a sneak peek of what's hiding under my teenie thong..."
mc "Oh God..."
stop music
play music "sounds/waterrun.mp3"
scene powergirlpoolnew07 with dissolve
pg "It's getting hot, isn't it? I need to cool down in the pool..."
scene powergirlpoolnew08b with dissolve
play sound "sounds/diving.mp3"
mc "Hey, wait for me, Kara!"
pg "Well, dive in, what are you waiting for?"
scene powergirlpoolnew09 with dissolve
mc "Alright, I'll catch you in no time!"
scene powergirlpoolnew10 with dissolve
stop music
play music "sounds/underwater.mp3"
mc "Here I come!"
scene powergirlpoolnew11 with dissolve
mc "* Where did she disappear??? *"
scene powergirlpoolnew12 with dissolve
play sound "sounds/thud.mp3"
mc "* Hey! She's kicking me, better get back to the surface soon!* "
scene powergirlpoolnew13 with dissolve
pg "* Where do you think you're going, [name]? *"
mc "* Quick, before she pulls my... *"
scene powergirlpoolnew14 with dissolve
stop music
play music "sounds/waterrun.mp3"
mc "* ... Too late... *"
pg "I think you lost these, [name]..."
mc "That's not fair. Now I'm naked and you're not!"
scene powergirlpoolnew15 with dissolve
pg "Maybe we should level things a bit then? Just for you, I'll take my top off..."
scene powergirlpoolnew16 with dissolve
pg "Is that more fair?"
scene powergirlpoolnew17 with dissolve
pg "Are you... jerking off underwater? Watching your landlady's daughter half-naked in the pool? Eew, that's kinda gross..."
mc "It's... your hot bod. I can't help it!"
scene powergirlpoolnew18 with dissolve
pg "I think I'd better get out of the pool now before you start sexually assaulting me..."
mc "I wouldn't do that! I just want to get my rocks off, please help me Kara!"
stop music
play music "sounds/sexy06.mp3"
window hide    
scene powergirlpoolnew19:
    zoom 1.0 xoffset -80 yoffset 0    
show powergirlpoolnew19 at powerpoolfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
pg "Now I feel safer. Away from that horny dong of yours..."
scene powergirlpoolnew20:
    zoom 1.0 xoffset -40 yoffset -1500    
show powergirlpoolnew20 at powerpoolfulldown02
with dissolve
$ renpy.pause(6.0, hard='True')    
pg "You're going to be a good boy and stay put in the pool?"
mc "Depends, what do I get in exchange?"
scene powergirlpoolnew21 with dissolve
pg "Something to get your \"rocks off\" as you put it..."
mc "Then I stay put. And get my rocks off."
scene powergirlpoolnew22 with dissolve
pg "Good. You've got to learn to keep that overshooting libido of yours under control. Fortunately, your landlady's daughter's pussy is here to help..."
mc "I don't think it's helping much, I'm getting HARDER and HARDER!"
scene powergirlpoolnew23 with dissolve
if age >= 20:
    pg "Just watch me play with my little pussy and imagine it's your giant piledriver that's plowing it..."
if age >= 18 and age <= 19:
    pg "Just watch me play with my little pussy and imagine it's your giant teenage piledriver that's plowing it..."
window hide
play channel2 "sounds/wetmassage.mp3"

$ powerpoolpussyslowx = False

label PowerPoolPussySlowx:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussyslowvideo behind powerpoolpussyfastvideo
show powerpoolpussyslowvideo behind powerpoolpussycloserslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyfastvideo
hide powerpoolpussycloserslowvideo
with dissolve
play channel1 "sounds/moan02.mp3"
$ powerpoolpussyfastx = False
if powerpoolpussyslowx == False:
    pg "That's it, jerk that fat cock of yours while you watch me stroke my pussy..."
    $ powerpoolpussyslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show closer:
     xpos 50 ypos 500     
call screen powerpoolpussyslowx()
screen powerpoolpussyslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolPussyFrontSlowx")

label PowerPoolPussyFastx:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussyfastvideo behind powerpoolpussyslowvideo
show powerpoolpussyfastvideo behind powerpoolpussycloserfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyslowvideo
hide powerpoolpussycloserfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ powerpoolpussyslowx = False
if powerpoolpussyfastx == False:
    pg "Go on, keep PUMPING that shaft, Do it as FAST as I frig myself!"
    $ powerpoolpussyfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show closer:
     xpos 1700 ypos 500     
call screen powerpoolpussyfastx()
screen powerpoolpussyfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussySlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerPoolPussyFrontFastx")

label PowerPoolPussyFrontSlowx:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussycloserslowvideo behind powerpoolpussyslowvideo
show powerpoolpussycloserslowvideo behind powerpoolpussycloserfastvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyslowvideo
hide powerpoolpussycloserfastvideo
with dissolve
play channel1 "sounds/moan02.mp3"
$ powerpoolpussyfastx = False
if powerpoolpussyslowx == False:
    pg "That's it, jerk that fat cock of yours while you watch me stroke my pussy..."
    $ powerpoolpussyslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerpoolpussycloserslowx()
screen powerpoolpussycloserslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussySlowx")

label PowerPoolPussyFrontFastx:
window hide
hide cum
hide slower
hide faster
hide closer
hide sceneicon
show powerpoolpussycloserfastvideo behind powerpoolpussyfastvideo
show powerpoolpussycloserfastvideo behind powerpoolpussycloserslowvideo
$ renpy.pause(1.0, hard='True')
hide powerpoolpussyfastvideo
hide powerpoolpussycloserslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
$ powerpoolpussyslowx = False
if powerpoolpussyfastx == False:
    pg "Go on, keep PUMPING that shaft, Do it as FAST as I frig myself!"
    $ powerpoolpussyfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen powerpoolpussycloserfastx()
screen powerpoolpussycloserfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerPoolPussyEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerPoolPussyFastx")

label PowerPoolPussyEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
pg "Are you gonna cum for me, [name]? Are you going to unload a MASSIVE explosion of SPUNK for your landlady's daughter?"
mc "Y...Yeah, I'm getting close!"
scene powerpoolwankcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
pg "Then cum for me, BLAST that sweet baby-batter!!!"
window hide
with fastflash
mc "I'm NUTTING FOR YOU, KARA!!! AAAHHH!"
scene powerpoolwankcum02 with dissolve
play sound "sounds/moan06.ogg"
pg "Watching you is making me cum too! OOOH!"
window hide 
with fastflash
pg "Look at me squirting, AAAH, it's sooo HOT!"
scene powerpoolwankcum03 with dissolve
mc "Oh God, it's making me BLAST even STRONGER! RHAAA!"
window hide
with hpunch
pg "I can see that, CUM SOME MORE FOR ME!"
scene powerpoolwankcum04 with dissolve
pg "Make it the BIGGEST load ever! Your shots are getting so HUGE, make them COVER me in your warm spunk!"
scene powerpoolwankcum03 with dissolve
mc "Here you GO, MORE FOR YOUUUUU!"
scene powerpoolwankcum05 with dissolve
play sound "sounds/moan02.mp3"
pg "You're a CUM-MACHINE! Look at poor little me, you've CAKED MY TITS in your MONSTER LOAD!"
mc "Just a few last shots, AAAAH!"
stop channel1
play sound "sounds/panting.mp3"
scene powerpoolwankcum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1        
with dissolve
pg "You've made GIANT puddles of cum on the pool surface... I wonder what it tastes like, I just need to grab some..."
scene powerpoolwankcum07 with dissolve
play sound "sounds/lick01.ogg"
pg "Mmh, it tastes GREAT! Chlorine enhances the flavor..."
scene powerpoolwankcum08 with dissolve
play sound "sounds/slurp.mp3"
mc "You learn something new every day."
pg "Thank you for this wonderful CUM-MEAL. But you need to go before the cleaning lady sees the mess you made...."
stop channel3
stop channel1
stop music
jump PowerGallery

label PowerGallery09:
stop channel3
scene compoundpooldaybackground
show powerpoolnew01
with fade
mc "Oooh, Kara is here. In a *HOT* new bikini..."
hide powerpoolnew01
show powerpoolnew02
with fastdissolve
pg "I Super-Sensed you behind my back, [name]..."
hide powerpoolnew02
show powerpooleyeblink
with dissolve
mc "Ah, yeah, you're good at that."
pg "I'm the GOAT at that."
mc "I was just going for a swim. You know, to maintain my ROCK-HARD muscles."
hide powerpooleyeblink
show powerpoolnew04 at centerleft
with fastdissolve        
pg "Is that so? Then I'll watch you and train with my ultra-heavy dumbbells. Let's see who has the most SOLID muscles after that!"
scene poolmclevel02a with dissolve
pg "Well go on then, I'll get my set ready..."
mc "Err, okay."
scene poolmclevel02b with dissolve
play sound "sounds/swim.mp3"
pg "Keep going, do as many laps as you can while I pump MY muscles!"
play music "sounds/gymmusic.mp3"
scene powerpoolbellback blurred:
    zoom 1.9 xoffset -400 yoffset -900
show powerpoolbell01:
    xoffset 0 yoffset -1080
show powerpoolbellback blurred at poolbackgroundup
show powerpoolbell01 at poolbackgroundpowerup
with dissolve
$ renpy.pause(7.0, hard='True') 
pg "I'll show how to REALLY train your muscles!"
mc "They don't look so big. How much do they weigh?"
scene powerpoolbellanimback blurred:
    zoom 1.5 xoffset -500 yoffset -100
show powerbellanim01start:
    zoom 1.5 xoffset 100 yoffset -100
with dissolve
pg "Over a TON. EACH!"
mc "Ok, that's a lot then."
pg "First, some heavy wrist curls..."
scene powerpoolbellanimback blurred
show powerbellanim01:
    zoom 1 xoffset 450 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanim01 at powerbellanim
with dissolve
$ renpy.pause(1.0, hard='True')
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbell01x()
screen powerbell01x():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellFast01x")

label PowerBellFast01x:
scene powerpoolbellanimback blurred
show powerbellanimfast01:
    zoom 1 xoffset 450 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanimfast01 at powerbellanim
with dissolve
$ renpy.pause(1.0, hard='True')
pg "And now, even FASTER!"
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbellfast01x()
screen powerbellfast01x():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellEnd01x")

label PowerBellEnd01x:
scene powerpoolbellback blurred:
    zoom 1.9 xoffset -400 yoffset -900
show powerbellanim02start:
    xoffset 0 yoffset -1080
show powerpoolbellback blurred at poolbackgroundup
show powerbellanim02start at poolbackgroundpowerup02
with dissolve
$ renpy.pause(7.0, hard='True') 
mc "Wow, your muscles have already GROWN some, Kara!"
pg "Gonna continue PUMPING then. Some Arnold press. Apparently some young Austrian bodybuilder came up with that recently."
window hide
scene powerpoolbellanimback blurred
show powerbellanim02:
    zoom 1 xoffset 350 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanim02 at powerbellanim2
with dissolve
$ renpy.pause(2.0, hard='True')
pg "It's a tough exercise, but Powergirl can DO IT!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbell02x()
screen powerbell02x():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellFast02x")

label PowerBellFast02x:
play sound "sounds/womangroan.mp3"
scene powerpoolbellanimback blurred
show powerbellanimfast02:
    zoom 1 xoffset 350 yoffset 0
show powerpoolbellanimback blurred behind powerbellanim01 at powerbellanimback
show powerbellanimfast02 at powerbellanim2
with dissolve
$ renpy.pause(1.0, hard='True')
pg "F...FASTER! I can do it, I have the POWER!"
show nexticon:
    xpos 1750 ypos 1020    
call screen powerbellfast02x()
screen powerbellfast02x():
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("PowerBellEnd02x")

label PowerBellEnd02x:
stop music
play sound "sounds/panting.mp3"
scene powerpoolbellanimback blurred:
    zoom 1.2 xoffset -300 yoffset -100
show powerpoolpostbell01:
    zoom 1.2 xoffset 100 yoffset -100
with dissolve
pg "That was...INTENSE.... I..."
mc "Kara, what's happening, you're all flustered!"
hide powerpoolpostbell01
show powerpoolpostbell02
with fastdissolve
pg "Aaah...."
scene powerpoolpostbell03 with dissolve
mc "Damn, she fainted! She must have over-exhausted herself with those super-heavy dumbbells."
scene powerpoolpostbell04 with dissolve
mc "Say something, Kara! Wake up! Oh my God, I have to do something, her skin is SCALDING HOT and her pulse is weak!"
scene powerpoolpostbell05 with dissolve
mc "First, some CPR... Damn, it's not working! I can't do cock-to-pussy resuscitation like you all thought I would, because her pussy would BURN my cock!"
scene powerpoolpostbell06 with dissolve
mc "I'll have to carry her and throw her in the pool so her body temperature can cool down. Without burning myself..."
scene powerpoolpostbell07 with dissolve
mc "Just in the nick of time, it was starting to HEAT UP a LOT!"
scene powerpoolpostbell08 with dissolve
mc "And now I'll jump in and make sure she doesn't drown!"
play sound "sounds/diving.mp3"
mc "I need to be quick!"
scene powerpoolpostbell09 with dissolve
play music "sounds/underwater.mp3"
mc "There she is, her skin doesn't look scalding HOT anymore, thanks God!"
scene powerpoolpostbell10 with dissolve
play music "sounds/waterrun.mp3"
mc "Let's get you out of the water now, your body temperature is back to normal..."
pg "What... What happened?..."
scene powerpoolpostbell11 with dissolve
pg "You were overheating. But I saved you... Kara..."
scene powerpoolpostbell12 with dissolve
play sound "sounds/kiss.mp3"
pg "You did? You saved ME? Let me kiss you..."
mc "Mmh, your tongue is still super-HOT!"
pg "It ALWAYS is... * wink *"
pg "I need to get back to the gallery and stick some ice inside my... girly bits."
mc "Right, right..."
stop channel3
stop channel1
stop music
jump PowerGallery