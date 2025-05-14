label DemonaGallery:
stop channel3
play channel3 "sounds/dark.mp3"
scene demonabackground
show demonamaingallery at gallerypos01 with moveinleft
call screen gallerydemona()
screen gallerydemona():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Demona{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerydemona"), Jump ("MainGallery04b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerydemona"), Jump ("DemonaGalleryAnim")]
    
    if renpy.seen_image("demonaroom01"):
        imagebutton:
            focus_mask True
            idle "gallery/demonagallery01.png" xpos 400 ypos 100
            hover "gallery/demonagallery01.png"
            action Jump ("DemonaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Dreamy titjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("demonaroom01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("DemonaGallery01hint")

    if renpy.seen_image("demonaroom11"):
        imagebutton:
            focus_mask True
            idle "gallery/demonagallery02.png" xpos 750 ypos 100
            hover "gallery/demonagallery02.png"
            action Jump ("DemonaGallery02")
    text "{font=Gui/Heroes Legend.ttf}Hellish Fuck{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("demonaroom11") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("DemonaGallery02hint")
            
label DemonaGallery01hint:
show demonamaingallery at gallerypos01
show demonagallery01 at posgalleryhintpic
show demonagalleryhint01 at posgalleryhint
pause
hide demonagalleryhint01
hide demonagallery01
call screen gallerydemona()

label DemonaGallery02hint:
show demonamaingallery at gallerypos01
show demonagallery02 at posgalleryhintpic
show demonagalleryhint02 at posgalleryhint
pause
hide demonagalleryhint02
hide demonagallery02
call screen gallerydemona()

label DemonaGalleryAnim:
call screen screenanimdemona()
screen screenanimdemona():
    modal True
    add "gallery/demonabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "demonaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "demonaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimdemona"), SetVariable ("animcount", 1), Jump ("DemonaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Demona{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero03
    text "{font=Gui/Heroes Legend.ttf}Age: 6500{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft9{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34F-23-35{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Titjob/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Cowgirl{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/demonaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimdemona")]
    add "gallery/demonaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimdemona")]

label DemonaGallery01:
$ demonatitfucktoldx = False
stop channel3
scene intromcsleep02
with dissolve
play sound "sounds/dream.mp3"
$ renpy.pause(1.0, hard='True')
play music "sounds/introdreaming.mp3"
show demona02a at topright with moveinright
hide demona02a
show demonafly02 at topright
voice "demona/titjob01"
de "Hey wake up, [hero]!"
scene intromcsleep02a
show intromcsleep02c
with dissolve
hide demonafly02 with dissolve
mc "But... You're gone?"
voice "demona/titjob02"
de "I'm still here, just REALLY open your eyes and look down this time..."
stop music
play sound "sounds/demon.mp3"
scene demonaroom01 with fade
mc "Is... Is this for real?"
voice "demona/titjob03"
de "Maybe. Maybe not. Who cares?"
scene demonaroom02 with dissolve
play music "sounds/sexy13.mp3"
mc "Aaaah, what are you doing, Demona?!"
voice "demona/titjob04"
de "What does it look like? I'm licking your fat pole with my super-long tongue!"    
scene demonaroom03 with dissolve
mc "Nice! And next, you're gonna RIDE IT WITH YOUR ASS, right?"
voice "demona/titjob05"
de "Humh, No, I don't want to. Just yet."
mc "But... why not???"
scene demonaroom04 with dissolve
if age >= 20:
    voice "demona/titjob06a"
    de "Cos I'm evil and I like to torture you, that's why! What did you expect? That we would sing \"kumbaya\" while you ass-fucked me with 15 inches of MEGA-COCK?"
if age >= 18 and age <= 19:
    voice "demona/titjob06b"
    de "Cos I'm evil and I like to torture you, that's why! What did you expect? That we would sing \"kumbaya\" while you ass-fucked me with 15 inches of TEEN MEGA-COCK?"
mc "So... What do I get?"
scene demonaroom05 with dissolve
voice "demona/titjob07"
de "A titjob. Still better than the lousy handjob the losers who chose the Hero route are getting! So get your legs up higher!"
scene demonaroom06 with dissolve
if age >= 20:
    voice "demona/titjob08a"
    de "Well, look at you, your giant dong is drooling pre-cum all over the place. That's just NASTY! You're a FILTHY boy, just like I like 'em!"
if age >= 18 and age <= 19:
    voice "demona/titjob08b"
    de "Well, look at you, your giant teenage dong is drooling pre-cum all over the place. That's just NASTY! You're a FILTHY boy, just like I like 'em!"
mc "Oh God, you're nasty too..."
voice "demona/titjob09"
de "You ain't seen nothing yet, you horse-hung muscle EVIL boy!"
play channel1 "sounds/wank.mp3"
play channel2 "sounds/boymoan02.mp3"
window hide
label DemonaTitfuckSlowx: 
hide cum
hide faster
hide slower
show demonatitfuckslowvideo behind demonatitfuckfastvideo
pause 1.0
hide demonatitfuckfastvideo with dissolve
if demonatitfucktoldx == False:
    if age >= 20:
        voice "demona/titjob10a"
        de "I'll start by teasing you with a slow, sensual, titfuck on your monstrous shaft..."
    if age >= 18 and age <= 19:
        voice "demona/titjob10b"
        de "I'll start by teasing you with a slow, sensual, titfuck on your monstrous teenage shaft..."
    window hide
    $ demonatitfucktoldx = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen demonatitfuckslowx()
screen demonatitfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DemonaTitfuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DemonaTitfuckEndx")

label DemonaTitfuckFastx:
show demonatitfuckfastvideo behind demonatitfuckslowvideo
hide cum
hide faster
hide slower
mc "Oh please... Titfuck me faster, I need to come!"
hide demonatitfuckslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen demonatitfuckfastx()
screen demonatitfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("DemonaTitfuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DemonaTitfuckEndx")

label DemonaTitfuckEndx:
voice "demona/titjob11"
de "Come for me, [name]. I want to see that NASTY cock SPEW ITS LOAD!"
scene demonaroomcum01 with dissolve
hide demonatitfuckfastvideo
hide demonatitfuckslowvideo
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
voice "demona/titjob12"
de "You're really close, the pre-cum is flowing..."
if demonawankevil:
    voice "demona/titjob13"
    de "It's better than jerking off to me in the jacuzzi, isn't it?"
    mc "Err... How did you know I was, like, dreaming about you?"
    voice "demona/titjob14"
    de "Because I'm your DIRTY conscience, [name]! I know your every thought...Now COME FOR DEMONA!"
if demonawankevil == False:
    voice "demona/titjob15"
    de "I can tell you're enjoying this, you DIRTY BOY! Now COME FOR DEMONA!"    
scene demonaroomcum02 with dissolve
mc "AAAAH!"
window hide
with fastflash
voice "demona/titjob16"
de "That's so hot, you're cumming like a STALLION! You have a LOT of NASTY, YOUNG CUM for me, don't you?"
scene demonaroomcum03 with dissolve
mc "Fuck, YEAH! Always a LOT for big-titted demon babes like you!"
window hide
with fastflash
voice "demona/titjob17"
de "My tits are going to EMPTY your balls, aren't they?"    
scene demonaroomcum04 with dissolve
voice "demona/titjob18"
de "That's it, let it RAIN DOWN ON ME!"
window hide
with fastflash
mc "RHAAA, CUMMING SO MUCH!"
scene demonaroomcum05 with dissolve
voice "demona/titjob19"
de "I'm fading out! Why are you waking up just when I was going to SLURP up all the salty nectar, godammit!"
mc "I...err..."
stop music
stop channel1
stop channel2
jump DemonaGallery

label DemonaGallery02:
$ demonafucktoldx = False
stop channel3
scene intromcsleep02
play sound "sounds/dream.mp3"
$ renpy.pause(1.0, hard='True')
play music "sounds/introdreaming.mp3"
show demona02a at topright with moveinright
hide demona02a
show demonafly02 at topright
de "Hey wake up, [hero]!"         
scene intromcsleep02a
show intromcsleep02c
with dissolve
hide demonafly02 with dissolve
mc "But... You're gone?"
de "I'm still here, just REALLY open your eyes and look down this time..."
stop music
play sound "sounds/demon.mp3"
scene demonaroom11 with fade
mc "Is... Is this for real?"
de "Maybe. Maybe not. Who cares?"
scene demonaroom12 with dissolve
stop sound
play music "sounds/sexy13.mp3"
if ivyharem and tolddemonaharem == False:
    de "What's important right now is that you got yourself a new WHORE for your EVIL HAREM!"
    mc "Ah yes, Poison Ivy. Although her tits have gone back to their normal size now that she's in my harem..."
    $ tolddemonaharem = True
if ivyharem == False or tolddemonaharem:
    de "What's important right now is that you have a GIANT 18-inch cum-cannon that needs some DEMONIC release!"
scene demonaroom13 with dissolve
if age >= 20:
    de "And since you've been such a NAUGHTY boy, I'm absolutely POSSESSED by your behemoth dong!"
if age >= 18 and age <= 19:
    de "And since you've been such a NAUGHTY boy, I'm absolutely POSSESSED by your teen behemoth dong!"
mc "Y... You are? So you're going to let me pummel your backdoor, right?"
scene demonaroom14 with dissolve
de "What is it with you and your obsession with ass-fucking me? It's just not healthy."
mc "Well, err..."
scene demonaroom15 with dissolve
de "There might be a stairway to heavens in most VN games, but right now, you're on the slide down to HELL!"
scene demonaroom16 with dissolve
de "Therefore, you're allowed to fuck my PUSSY. But let ME do the RIDING, cowboy!"
scene demonaroom17 with dissolve
play sound "sounds/moan05.mp3"
if age >= 20:
    de "Dear Beelzebub, I didn't expect such a... HUGE monstercock on such a young [age]yo man! But it's my job to entice young STALLIONS, so let's DO IT!"
if age >= 18 and age <= 19:
    de "Dear Beelzebub, I didn't expect such a... HUGE monstercock on such a young [age]yo teenage boy! But it's my job to entice young STALLIONS, so let's DO IT!"
window hide

label DemonaFuckSlowx: 
stop channel2
play channel2 "sounds/womansex06.mp3"
hide cum
hide faster
hide slower
show demonafuckslowvideo behind demonafuckfastvideo
pause 1.0
hide demonafuckfastvideo with dissolve
if demonafucktoldx == False:
    mc "Damn, your pussy is SCALDING HOT!"
    de "That's right, its walls are lined with embers from the INFERNO OF HELL!"
    window hide
    $ demonafucktoldx = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen demonafuckslowx()
screen demonafuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DemonaFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DemonaFuckEndx")

label DemonaFuckFastx:
show demonafuckfastvideo behind demonafuckslowvideo
hide cum
hide faster
hide slower
mc "Oh please... Fuck me faster, I need to come!"
hide demonafuckslowvideo with dissolve
stop channel1
play channel2 "sounds/womansex06.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen demonafuckfastx()
screen demonafuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("DemonaFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DemonaFuckEndx")

label DemonaFuckEndx:    
hide cum
hide slower
hide faster
de "It's time for you to FILL ME UP with your SPUNK!"
scene demonacum01 with dissolve
stop channel1
stop channel2
play channel1 "v031/boyorgasm02.mp3"
de "That's it, let it EXPLODE out of your cumslit and into my hungry snatch!"
window hide 
with hpunch
mc "AAAAH! Your pussy is so tight!"
scene demonacum02 with dissolve
if age >= 20:
    de "That's cos I'm CLAMPING down on your convulsing dong while you're cumming!"
if age >= 18 and age <= 19:
    de "That's cos I'm CLAMPING down on your convulsing teenage dong while you're cumming!"
window hide
with fastflash
mc "That's so NAAAA-AAASTY! UUUHH!"
scene demonacum03 with dissolve
de "DEEPER! FLOOD my 6500yo uterus!"
window hide
with vpunch
mc "OH MY GOD, YOUR PUSSY IS LIKE A VICE! AAAH!"
scene demonacum04 with dissolve
play sound "sounds/moan04.ogg"
de "Just there... just there, I'm gonna cum too!"
scene demonacum05 with dissolve
de "You're such an evil jerk! You're waking up just when I was getting MY rocks off!"
mc "I...err..."
stop music
stop channel1
stop channel2
scene mcwakecumlevel02 with fade
mc "Oh shit, it wasn't real after all... And I came all over myself instead of inside Demona's hellish twat... * sigh *"
jump DemonaGallery