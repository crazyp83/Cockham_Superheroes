label WangGallery:
stop channel3
play sound "sounds/gong.mp3"
scene wangbackground with dissolve
show wangmaingallery at gallerypos01 with moveinleft
call screen gallerywang()
screen gallerywang():
    text "{font=Gui/Heroes Legend.ttf}Naughty Ada Wang & Triad Ninjas{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerywang"), Jump ("MainGallery02")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerywang"), Jump ("WangGalleryAnim")]
    
    if renpy.seen_image("chinesemassage01"):
        imagebutton:
            focus_mask True
            idle "gallery/wanggallery01.png" xpos 400 ypos 100
            hover "gallery/wanggallery01.png"
            action Jump ("WangGallery01")
    text "{font=Gui/Heroes Legend.ttf}Chinese Massage{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("chinesemassage01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WangGallery")

    if adafuta == False:
        if renpy.seen_image("wangroom02"):
            imagebutton:
                focus_mask True
                idle "gallery/wanggallery02.png" xpos 750 ypos 100
                hover "gallery/wanggallery02.png"
                action Jump ("WangGallery02")
        text "{font=Gui/Heroes Legend.ttf}Cock Choking{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
        if renpy.seen_image("wangroom02") == False:
            imagebutton:
                focus_mask True
                idle "gallery/gallerylocked.png" xpos 750 ypos 100
                hover "gallery/gallerylocked.png"
                action Jump ("WangGallery")

    if adafuta:
        if renpy.seen_image("wangroom02"):
            imagebutton:
                focus_mask True
                idle "gallery/wanggallery02b.png" xpos 750 ypos 100
                hover "gallery/wanggallery02b.png"
                action Jump ("WangGallery02")
        text "{font=Gui/Heroes Legend.ttf}Cock Choking{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
        if renpy.seen_image("wangroom02") == False:
            imagebutton:
                focus_mask True
                idle "gallery/gallerylocked.png" xpos 750 ypos 100
                hover "gallery/gallerylocked.png"
                action Jump ("WangGallery")

    if adafuta == False:
        if renpy.seen_image("adaroom13"):
            imagebutton:
                focus_mask True
                idle "gallery/wanggallery03.png" xpos 1100 ypos 100
                hover "gallery/wanggallery03.png"
                action Jump ("WangGallery03")
        text "{font=Gui/Heroes Legend.ttf}Harem Anal Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
        if renpy.seen_image("adaroom13") == False:
            imagebutton:
                focus_mask True
                idle "gallery/gallerylocked.png" xpos 1100 ypos 100
                hover "gallery/gallerylocked.png"
                action Jump ("WangGallery")

    if adafuta:
        if renpy.seen_image("adaroom13"):
            imagebutton:
                focus_mask True
                idle "gallery/wanggallery03b.png" xpos 1100 ypos 100
                hover "gallery/wanggallery03b.png"
                action Jump ("WangGallery03")
        text "{font=Gui/Heroes Legend.ttf}Harem Anal Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
        if renpy.seen_image("adaroom13") == False:
            imagebutton:
                focus_mask True
                idle "gallery/gallerylocked.png" xpos 1100 ypos 100
                hover "gallery/gallerylocked.png"
                action Jump ("WangGallery")
label WangGalleryAnim:
stop channel3
play channel3 "sounds/sexy02.mp3"
call screen screenanimada()
screen screenanimada():
    modal True
    add "gallery/wangbackground.png"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "adaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "adaanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "adaanimlinfuta" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "adaanimnak" xalign -0.1 yalign 1.0
    if animcount == 5:
        add "adaanimnakfuta" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimada"), SetVariable ("animcount", 1), Jump ("WangGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Ada Wang{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 32{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft7{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34D-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Male Rape{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/adaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimada")]
    if adafuta == False:
        add "gallery/adaanim02a.png" xpos 1220 ypos 800
        button:
            xpos 1220
            ypos 800
            xysize(100, 100)        
            action [SetVariable ("animcount", 2), Show ("screenanimada")]
    if adafuta:
        add "gallery/adaanim02b.png" xpos 1220 ypos 800
        button:
            xpos 1220
            ypos 800
            xysize(100, 100)        
            action [SetVariable ("animcount", 3), Show ("screenanimada")]
    if adafuta == False:
        add "gallery/adaanim03a.png" xpos 1340 ypos 800
        button:
            xpos 1340
            ypos 800
            xysize(100, 100)        
            action [SetVariable ("animcount", 4), Show ("screenanimada")]
    if adafuta:
        add "gallery/adaanim03b.png" xpos 1340 ypos 800
        button:
            xpos 1340
            ypos 800
            xysize(100, 100)        
            action [SetVariable ("animcount", 5), Show ("screenanimada")]
            
label WangGallery01:
stop sound
scene chinesemassage01 with fade
play music "sounds/asianmusic02.mp3"
aj "Welcome to Misohawny Chinese Parlor, [hero]."
mc "Thank you for the warm welcome, err, ninja girl. Who is now in a sexy kimono."
scene chinesemassage02 with dissolve
aj "Please take your towel off and lie on the massage table face down."
mc "Why is there a hole in the middle?"
if age >= 20:
    aj "That's for your cock. We are aware of how ENORMOUS you are, [hero] and we aim to minimize your discomfort. That way, your giant white package won't be squeezed underneath your body."
if age >= 18 and age <= 19:
    aj "That's for your cock. We are aware of how ENORMOUS you are, [hero] and we aim to minimize your discomfort. That way, your giant white teenage package won't be squeezed underneath your body."
mc "Oooh, interesting..."
scene chinesemassage03 with dissolve
aj "Are you comfortable, [hero]? I see your monstrous dick and balls fit snugly in the table hole provided."
mc "Mmh, yeah, I am. You can go ahead with your sweet Asian massage."
aj "CHINESE massage. Chinese Triad \"traditional\" massage..."
scene chinesemassage04 with dissolve
mc "* I'm even getting a semi just thinking about how GOOD it will feel... * "
aj "I will start with your muscular back."
scene chinesemassage05 with dissolve
play sound "sounds/boymoan04.mp3"
aj "Does this feel pleasant to you, [hero]?"
mc "Mmmh, yeah..."
scene chinesemassage06 with dissolve
aj "You seem quite tense. Are you scared because you are in the hands of a Triad Ninja?"
mc "I'm NOT! Also, ninjas are supposed to be Japanese. Just pointing that out. Big dev mistake right there."
scene chinesemassage07 with dissolve
aj "These are some nice tight buns you have there, [hero]."
mc "Thanks, I like to keep in s..."
scene chinesemassage08 with dissolve
play sound "sounds/boymoan02.mp3"
mc "Aaah, what are you...?"
scene chinesemassage09 with dissolve
aj "Just massaging your prostate. From the INSIDE. Feels good, doesn't it?"
play sound "sounds/boymoan03.mp3"
mc "Oooh... That's a first, someone's sticking something up my ass. Good thing it's not a cock..."
scene chinesemassage10 with dissolve
aj "It appears this is causing an uncontrollable and PLENTIFUL precum leakage from your urethra... Let me call the clean-up girl..."
mc "A clean-up girl?"
scene chinesemassage11 with dissolve
aj "Yes. Lian Shi will clean your cummy mess. And provide you with a side of number 11."
mc "Ooh, where is she?"
aj "Underneath the table."
scene chinesemassage12 with dissolve
play sound "sounds/boymoan.mp3"
mc "AAAH! Is... Is that her grabbing my knob?"
aj "Of course. She is a skilled milking expert with her hands. You will see."
scene chinesemassage13 with dissolve
play sound "sounds/lick03.mp3"
ls "I need to put some more STEEL in that massive weapon..."
scene chinesemassage14 with dissolve
play sound "sounds/lick01.ogg"
if age >= 20:
    ls "Your Alpha King Dong is growing... And getting harder."
if age >= 18 and age <= 19:
    ls "Your Teen King Dong is growing... And getting harder."
scene chinesemassage14b with dissolve
play sound "sounds/lick03.mp3"
ls "A few more tugs of that great big donkey-dick..."
scene chinesemassage14 with dissolve
play sound "sounds/lick01.ogg"
mc "Oh God..."
scene chinesemassage14c with dissolve
play sound "sounds/lick03.mp3"
ls "You are splattering pre-cum all over my breasts, you dirty boy... I think you are ready."
mc "Ready for what?"
scene chinesemassage15 with dissolve
ls "You will see. And FEEL."
scene chinesemassage16 with dissolve
mc "UUUUH! What's going on?"
ls "Don't worry, it will eventually allow you to reach a PRODIGIOUS orgasm."
scene chinesemassage17 with dissolve
play sound "sounds/boymoan03.mp3"
mc "AAAH, It hurts!"
ls "Only for a short while. Once I remove it, you will reach the NIRVANA of PLEASURE!"
scene chinesemassage18 with dissolve
aj "Just relax, [hero]. I told you Lian Shi was an EXPERT MILKER, didn't I?"
mc "But I'm not a cow!"
aj "No, you're a BULL though! A bull with MASSIVE cum-laden balls who needs sweet release..."
scene chinesemassage19 with dissolve
aj "And a good spanking for being such a horse-hung stud and hiding this from us all this time..."
mc "I didn't hide it, I only just recently grew this enormous dong!"
scene chinesemassage20 with dissolve
play sound "sounds/slap.mp3"
aj "Liar! That's not what I heard!"
mc "Ouch!"
scene chinesemassage19 with dissolve
aj "You were already hung like a fucking horse when you were a kid, admit it!"
scene chinesemassage20 with dissolve
play sound "sounds/slap.mp3"
mc "Please!"
scene chinesemassage19 with dissolve
aj "And you already had huge muscles too, SAY IT!"
scene chinesemassage20 with dissolve
play sound "sounds/slap.mp3"
mc "Alright, alright, I admit it!"
scene chinesemassage19 with dissolve
aj "Now that's better! You filthy, dirty, donkey-dicked boy..."
scene chinesemassage30 with dissolve
play sound "sounds/lick03.mp3"
ls "And I'm gonna make that donkey-dick EXPLODE soon!..."
scene chinesemassage31 with dissolve
play sound "sounds/lick01.ogg"
ls "But first, I want to lick it. ALL OVER."
scene chinesemassage30 with dissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(0.5, hard='True')
scene chinesemassage31 with dissolve
$ renpy.pause(0.5, hard='True')
scene chinesemassage30 with dissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(0.5, hard='True')
scene chinesemassage31 with dissolve
$ renpy.pause(0.5, hard='True')
scene chinesemassage30 with dissolve
play sound "sounds/lick03.mp3"
$ renpy.pause(0.5, hard='True')
scene chinesemassage31 with dissolve
$ renpy.pause(0.5, hard='True')
scene chinesemassage18 with dissolve
aj "Are you enjoying Lian Shi's side number 11?"
mc "Ggg... Yes, Yes, I am...."
scene chinesemassage32 with dissolve
ls "It is now time for your RELEASE."
mc "Uuuuh, finally... My dong feels like it's going to burst..."
scene chinesemassage33 with dissolve
play sound "sounds/splooge01.mp3"
mc "AAAAH! FU-UUUU-UUUCCCCCKKKKK!"
scene chinesemassage34 with dissolve
play sound "sounds/splooge02.mp3"
ls "let it all out [hero], whitewash the floor with your scum!"
scene chinesemassage35 with dissolve
play sound "sounds/splooge01.mp3"
mc "GODAMM-MMMM-MIT!"
scene chinesemassage36 with dissolve
play sound "sounds/moan02.mp3"
aj "AAAH, keep pumping TONS of boycum! I'm getting there myself!"
scene chinesemassage34 with dissolve
play sound "sounds/splooge02.mp3"
ls "Mmmh, it's STILL leaking everywhere... Let me slurp it up!"
stop sound
scene chinesemassage37 with dissolve
aj "Lian Shi did well, didn't she [hero]?"
mc "Y... yes..."
scene chinesemassageend with dissolve
aj "Before you leave, I have a message for you from Ada Wang..."
mc "Uuurh, what?"
aj "The message is: \"Don't fuck with the Triad or you'll regret it.\""
mc "I would have preferred a fortune cookie message. They're usually less violent."
stop music
jump WangGallery

label WangGallery02:
stop channel3
stop music
if adafuta:
    scene wangthrone05
    show wangthrone05b
    with dissolve
if adafuta == False:
    scene wangthrone05 with dissolve
aw "Join me in my chambers to discuss this matter further..."
mc "Of course, your Empressness."
play music "sounds/sexy08.mp3"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene wangroom02 with dissolve
aw "I would like to get more... comfortable, if you don't mind. I will change behind this divider. Which is Super-Senses-proof for your information."
mc "Ah, damn."
window hide
show wangroom01 blurred:
    zoom 1.1 xoffset 0 yoffset -1000
if adafuta:
    show wangroompose01b:
        xoffset -50 yoffset -1080    
    show wangroom01 blurred at scarlettfullzoombackground
    show wangroompose01b at scarlettfullzoom
    with dissolve
    $ renpy.pause(5.0, hard='True')
    pause        
    aw "Now, let's test your WILLPOWER. Can you resist THIS body? And my BIG FUTA COCK?"
    mc "It's going to be tough..."
if adafuta == False:
    show wangroompose01:
        xoffset -50 yoffset -1080    
    show wangroom01 blurred at scarlettfullzoombackground
    show wangroompose01 at scarlettfullzoom
    with dissolve
    $ renpy.pause(5.0, hard='True')
    pause        
    aw "Now, let's test your WILLPOWER. Can you resist THIS body?"
    mc "It's going to be tough..."
window hide
hide wangroompose01
hide wangroompose01b
show wangroom01 blurred:
    zoom 1.1 xoffset 0 yoffset 0
show wangroompose02:
    xoffset 50 yoffset 0    
show wangroom01 blurred at scarlettfulldownzoombackground
show wangroompose02 at scarlettfulldownzoom
with dissolve
$ renpy.pause(5.0, hard='True')
pause
aw "What about the back. Does it make your ALPHA-COCK SUPER-HARD?"
mc "Err, let me check. Yes, it does."
if adafuta:
    scene wangroom03
    show wangroom03b
    with dissolve
    aw "Good, then bring that donkey-dick over. I'm getting HARD too. And I have a GAME for you."    
if adafuta == False:
    scene wangroom03 with dissolve
    aw "Good, then bring that donkey-dick over. I have a GAME for you."    
mc "Oooh, a GAME?"
aw "It's called \"Do as Ada Says or you Die!\" Ada says: ON YOUR KNEES, SLAVE!"
if adafuta:
    scene wangroom04
    show wangroom04b
    with dissolve
    aw "That naughty cock of yours deserves to be tormented so that you understand that you are nothing but a PIECE OF BOYMEAT at MY command!"
    mc "Err, not with YOUR cock I hope?"
    aw "The dev is still thinking about it. Ada says: LICK MY SHOES!"
if adafuta == False:
    scene wangroom04 with dissolve
    aw "That naughty cock of yours deserves to be tormented so that you understand that you are nothing but a PIECE OF BOYMEAT at MY command!"
    mc "Err, whatever you SAY, Mistress Ada."
    aw "Ada says: LICK MY SHOES"
if adafuta:
    scene wangroom05
    show wangroom05b
    with dissolve
if adafuta == False:
    scene wangroom05 with dissolve
play sound "sounds/lick01.ogg"
if age >= 20:
    aw "That's a good boy. A good horse-hung YOUNG boy."
if age >= 18 and age <= 19:
    aw "That's a good boy. A good horse-hung TEENAGE boy."
if adafuta:
    scene wangroom06
    show wangroom06b
    with dissolve
if adafuta == False:
    scene wangroom06 with dissolve
aw "And now let's see how your engorged MONSTERCOCK fares against my knob-chocker..."
mc "Please be careful with that th..."
if adafuta:
    scene wangroom07
    show wangroom07b
    with dissolve
if adafuta == False:
    scene wangroom07 with dissolve
play sound "sounds/boymoan03.mp3"
aw "It fits just snugly, doesn't it?"
mc "I... I guess so..."
aw "And now, let's begin the session!"
play channel1 "sounds/wetmassage.mp3"
play channel2 "sounds/boymoan04.mp3"
$ adawankslowx = False

if adafuta:
    label AdaFutaWankSlowx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adafutawankslowvideo behind adafutawankfastvideo
    show adafutawankslowvideo behind adafutawankcloserslowvideo
    $ renpy.pause(1.0, hard='True')
    hide adafutawankfastvideo
    hide adafutawankcloserslowvideo
    with dissolve
    $ adawankfastx = False
    if adawankslowx == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslowx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show closer:
         xpos 50 ypos 500     
    call screen adafutawankslowx()
    screen adafutawankslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaFutaWankFrontSlowx")

    label AdaFutaWankFastx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adafutawankfastvideo behind adafutawankslowvideo
    show adafutawankfastvideo behind adafutawankcloserfastvideo
    $ renpy.pause(1.0, hard='True')
    hide adafutawankslowvideo
    hide adafutawankcloserfastvideo
    with dissolve
    $ adawankslowx = False
    if adawankfastx == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfastx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show closer:
         xpos 1700 ypos 500     
    call screen adafutawankfastx()
    screen adafutawankfastx():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEndx")
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaFutaWankFrontFastx")

    label AdaFutaWankFrontSlowx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adafutawankcloserslowvideo behind adafutawankslowvideo
    show adafutawankcloserslowvideo behind adafutawankcloserfastvideo
    $ renpy.pause(1.0, hard='True')
    hide adafutawankslowvideo
    hide adafutawankcloserfastvideo
    with dissolve
    $ adawankfastx = False
    if adawankslowx == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslowx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adafutawankcloserslowx()
    screen adafutawankcloserslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFrontFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEndx")
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankSlowx")

    label AdaFutaWankFrontFastx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adafutawankcloserfastvideo behind adafutawankfastvideo
    show adafutawankcloserfastvideo behind adafutawankcloserslowvideo
    $ renpy.pause(1.0, hard='True')
    hide adafutawankfastvideo
    hide adafutawankcloserslowvideo
    with dissolve
    $ adawankslowx = False
    if adawankfastx == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfastx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show sceneicon:
         xpos 1700 ypos 500     
    call screen adafutawankcloserfastx()
    screen adafutawankcloserfastx():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFrontSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEndx")
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFastx")

    label AdaFutaWankEndx:
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon

if adafuta == False:
    label AdaWankSlowx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adawankslowvideo behind adawankfastvideo
    show adawankslowvideo behind adawankcloserslowvideo
    $ renpy.pause(1.0, hard='True')
    hide adawankfastvideo
    hide adawankcloserslowvideo
    with dissolve
    $ adawankfastx = False
    if adawankslowx == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslowx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show closer:
         xpos 50 ypos 500     
    call screen adawankslowx()
    screen adawankslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaWankFrontSlowx")

    label AdaWankFastx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adawankfastvideo behind adawankslowvideo
    show adawankfastvideo behind adawankcloserfastvideo
    $ renpy.pause(1.0, hard='True')
    hide adawankslowvideo
    hide adawankcloserfastvideo
    with dissolve
    $ adawankslowx = False
    if adawankfastx == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfastx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show closer:
         xpos 1700 ypos 500     
    call screen adawankfastx()
    screen adawankfastx():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEndx")
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaWankFrontFastx")

    label AdaWankFrontSlowx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adawankcloserslowvideo behind adawankslowvideo
    show adawankcloserslowvideo behind adawankcloserfastvideo
    $ renpy.pause(1.0, hard='True')
    hide adawankslowvideo
    hide adawankcloserfastvideo
    with dissolve
    $ adawankfastx = False
    if adawankslowx == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslowx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adawankcloserslowx()
    screen adawankcloserslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFrontFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEndx")
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankSlowx")

    label AdaWankFrontFastx:
    window hide
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon
    show adawankcloserfastvideo behind adawankfastvideo
    show adawankcloserfastvideo behind adawankcloserslowvideo
    $ renpy.pause(1.0, hard='True')
    hide adawankfastvideo
    hide adawankcloserslowvideo
    with dissolve
    $ adawankslowx = False
    if adawankfastx == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfastx = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show sceneicon:
         xpos 1700 ypos 500     
    call screen adawankcloserfastx()
    screen adawankcloserfastx():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFrontSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEndx")
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFastx")

    label AdaWankEndx:
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon

mc "I can't hold out for much longer!"
aw "Is that so? That wasn't very long. You have a WEAK mind, young Superhero!"
if adafuta:
    scene adawankcum01 with dissolve
if adafuta == False:
    scene adawankcum01
    show adawankcum01b
    with dissolve    
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "AAAH, TOO LATE, SO-RRRRYYYYY!"
window hide
with fastflash
aw "If you're gonna to blow your nut, you might as well BLAST A SUPER-LOAD!"
if adafuta:
    scene adawankcum02
    show adawankcum02b
    with dissolve    
if adafuta == False:
    scene adawankcum02 with dissolve
aw "That's better, big American superhero plumes of boyspunk! Me love this long time!"
window hide
with fastflash
mc "Oh God, RHAAA!"
if adafuta:
    scene adawankcum03 with dissolve
if adafuta == False:
    scene adawankcum03
    show adawankcum03b
    with dissolve    
if age >= 20:
    aw "Keep going, you filthy boy! You're spewing EVERYWHERE!"
if age >= 18 and age <= 19:
    aw "Keep going, you filthy teenage boy! You're spewing EVERYWHERE!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
mc "My balls are on FIRE, AAAH!"
if adafuta:
    scene adawankcum04b with dissolve
    play sound "sounds/moan06.ogg"
    aw "AAH, let's cum together!"
    window hide
    with fastflash
    mc "Gggg...."
if adafuta == False:
    scene adawankcum04 with dissolve    
    play sound "sounds/boymoan03.mp3"
    aw "That's it, let it ALL out, empty your huge ballsack for your Mistress!"
    window hide
    with fastflash
    mc "Gggg...."
stop channel1
if adafuta:
    scene adawankcum05b with dissolve
    play sound "sounds/moan05.mp3"
    aw "I'm coming all over your head, OOOH!"
    window hide
    with fastflash
    mc "I don't even care at this stage, rhawww...."
if adafuta == False:
    scene adawankcum05 with dissolve  
    aw "It looked like it was really GOOD for you, wasn't it?"
    mc "Y...yes....rhawwww..."
scene adawankcum06 with dissolve    
play sound "sounds/panting.mp3"
aw "You did reasonably well... I might have to work on you a bit more before I decide to USE you."
mc "My...my pleasure..."
stop music
jump WangGallery

label WangGallery03:
stop channel3
stop music

play music "sounds/sexy08.mp3" volume 0.5
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon

scene adaroom00:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.03
with fade
if seentriadreward:
    aw "What do you want, [hero]?"
    mc "Well, I want your ASS, Ada Wang. With or without wang. Cos you're MY Harem Girl!"
if seentriadreward == False:
    aw "There you are. Here to get your reward..."
    mc "I sure am. Your ass is MINE tonight, Ada Wang!"
scene wangroom02 with dissolve
if seentriadreward:
    aw "I suppose I am. After the treatment you gave it last time, I am truly your ASS SLAVE."
    mc "That's the kind of talk I like to hear from my girls..."
if seentriadreward == False:
    aw "You helped me get rid of my worst enemies. Since I am a woman of honor, I will grant you what you seek. My ANAL VIRGINITY!"
    mc "Ooh! I didn't realize you were an anal virgin. This is going to be extra-sweet, especially for the extremist anti-NTR brigade players."
aw "Let me get changed into something more appropriate for this... intimate moment."

if adafuta == False:
    scene adaroom01a:
        subpixel True
        xoffset 0 yoffset -1200  
        ease 8.0 xoffset -80 yoffset -20
    with dissolve
    $ renpy.pause(2.0, hard='True')
    aw "Is this lingerie set to your liking, [name]?..."

if adafuta:
    scene adaroom01b:
        subpixel True
        xoffset 0 yoffset -1200  
        ease 8.0 xoffset -80 yoffset -20
    with dissolve
    $ renpy.pause(2.0, hard='True')
    aw "Is this lingerie set to your liking, [name]?... With my big futa cock hanging out..."

mc "FUCK YEAH!"
scene adaroom02:
    subpixel True
    xoffset 0 yoffset 0 
    ease 8.0 xoffset -80 yoffset -1200
with dissolve
aw "I hope your ALPHA-COCK is getting SUPER-HARD right now..."
mc "It is, I can assure you, IT IS!"

if adafuta == False:
    scene adaroom03:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve    
if adafuta:
    scene adaroom03b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
aw "Please let me see that huge dick of yours."    
mc "My pleasure."

if adafuta == False:
    scene adaroom04 with dissolve
if adafuta:
    scene adaroom04
    show adaroom04b
    with dissolve
aw "You're HAULING it out like a heavy piece of equipment."    
mc "That's cos it IS a heavy piece of equipment!"

if adafuta == False:
    scene adaroom05:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.03
    with fastdissolve
if adafuta:
    scene adaroom05b:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.03
    with fastdissolve
play sound "sounds/wow.mp3"
aw "You could split a woman in half with this dong!"  
mc "You'd think so and yet it fits. Most of the times."

if adafuta == False:
    scene adaroom06 with dissolve
if adafuta:
    scene adaroom06
    show adaroom06b
    with dissolve
play sound "sounds/moan01.mp3"
aw "And it's already leaking so much precum!"
mc "A necessary leakage so as to lube it up for maximum penetration."

if adafuta == False:
    scene adaroom07 with dissolve
if adafuta:
    scene adaroom07
    show adaroom07b
    with dissolve
aw "I still think I should make it easier on my little backdoor. By lubing it up even more with my mouth!"

play sound "sounds/blow01.mp3"
if adafuta == False:
    scene adaroom08 with dissolve

if adafuta:
    scene adaroom08
    show adaroom08b
    with dissolve
mc "Yeah, you go, girl!"

if adafuta == False:
    scene adaroom09 with dissolve

if adafuta:
    scene adaroom09b with dissolve
play sound "sounds/lick01.ogg"
if age >= 20:
    aw "You like that don't you, dirty boy? You like having a mature woman slurp up all the excess pre-cum that you MEGA-DONG can produce?"
if age >= 18 and age <= 18:
    aw "You like that don't you, dirty boy? You like having a mature woman slurp up all the excess pre-cum that you TEENAGE MEGA-DONG can produce?"
   

if adafuta == False:
    scene adasuckstart with dissolve

if adafuta:
    scene adasuckfutastart with dissolve
mc "Fuck yeah, keep sucking, keep sucking Ada and I'll reward with a mighty dose of a REAL MAN'S CUM!"

if adafuta == False:
    label AdaSuckSlowx:
    $ adasuckharderx = False
    $ adasuckfastx = False
    hide faster
    hide slower
    hide pov
    hide sceneicon
    hide harder
    hide softer
    hide cum
    window hide
    show adasuckslowvideo behind adasuckfastvideo
    show adasuckslowvideo behind adasuckpovslowvideo
    show adasuckslowvideo behind adasuckharderslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckfastvideo
    hide adasuckpovslowvideo
    hide adasuckharderslowvideo
    with dissolve
    play channel2 "sounds/blow01.mp3"
    show harder:
        xpos 1700 ypos 700    
    show faster:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckslowx()
    screen adasuckslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckFastx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowx")

    label AdaSuckFastx:
    $ adasuckharderx = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfastx == False:
        mc "Do it FASTER, Harem Girl!"
        $ adasuckfastx = True
    show adasuckfastvideo behind adasuckslowvideo
    show adasuckfastvideo behind adasuckpovfastvideo
    show adasuckfastvideo behind adasuckharderfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckslowvideo
    hide adasuckpovfastvideo
    hide adasuckharderfastvideo
    with dissolve
    play channel2 "sounds/blow02.mp3"
    window hide
    show harder:
        xpos 1700 ypos 700    
    show slower:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckfastx()
    screen adasuckfastx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckSlowx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastx")

    label AdaSuckPOVSlowx:
    $ adasuckharderx = False
    $ adasuckfastx = False
    window hide
    hide faster
    hide slower
    hide pov
    hide sceneicon
    hide harder
    hide softer
    hide cum
    show adasuckpovslowvideo behind adasuckslowvideo
    show adasuckpovslowvideo behind adasuckpovfastvideo
    show adasuckpovslowvideo behind adasuckharderpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckslowvideo
    hide adasuckpovfastvideo
    hide adasuckharderpovslowvideo
    with dissolve
    play channel2 "sounds/blow01.mp3"
    show harder:
        xpos 1700 ypos 700    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckslowpovx()
    screen adasuckslowpovx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVFastx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckSlowx")

    label AdaSuckPOVFastx:
    $ adasuckharderx = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfastx == False:
        mc "Do it FASTER, Harem Girl!"
        $ adasuckfastx = True
    window hide
    show adasuckpovfastvideo behind adasuckpovslowvideo
    show adasuckpovfastvideo behind adasuckfastvideo
    show adasuckpovfastvideo behind adasuckharderpovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckpovslowvideo
    hide adasuckfastvideo
    hide adasuckharderpovfastvideo
    with dissolve
    play channel2 "sounds/blow02.mp3"
    window hide
    show harder:
        xpos 1700 ypos 700    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckfastpovx()
    screen adasuckfastpovx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVSlowx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckFastx")

    label AdaSuckHarderSlowx:
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderslowvideo behind adasuckharderfastvideo
    show adasuckharderslowvideo behind adasuckharderpovslowvideo
    show adasuckharderslowvideo behind adasuckslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderfastvideo
    hide adasuckharderpovslowvideo
    hide adasuckslowvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show faster:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckharderslowx()
    screen adasuckharderslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderFastx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckSlowx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderFastx:     
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderfastvideo behind adasuckharderslowvideo
    show adasuckharderfastvideo behind adasuckharderpovfastvideo
    show adasuckharderfastvideo behind adasuckfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderslowvideo
    hide adasuckharderpovfastvideo
    hide adasuckfastvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show slower:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckharderfastx()
    screen adasuckharderfastx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderSlowx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckFastx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderPOVSlowx:      
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderpovslowvideo behind adasuckharderslowvideo
    show adasuckharderpovslowvideo behind adasuckharderpovfastvideo
    show adasuckharderpovslowvideo behind adasuckpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderslowvideo
    hide adasuckharderpovfastvideo
    hide adasuckpovslowvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckharderpovslowx()
    screen adasuckharderpovslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVFastx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderPOVFastx:    
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderpovfastvideo behind adasuckharderpovslowvideo
    show adasuckharderpovfastvideo behind adasuckharderfastvideo
    show adasuckharderpovfastvideo behind adasuckpovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderpovslowvideo
    hide adasuckharderfastvideo
    hide adasuckpovfastvideo
    with dissolve
    window hide
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckharderpovfastx()
    screen adasuckharderpovfastx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVSlowx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")


if adafuta:
    label AdaSuckSlowbx:
    $ adasuckharderx = False
    $ adasuckfastx = False
    hide faster
    hide slower
    hide pov
    hide sceneicon
    hide harder
    hide softer
    hide cum
    window hide
    show adasuckfutaslowvideo behind adasuckfutafastvideo
    show adasuckfutaslowvideo behind adasuckpovslowvideo
    show adasuckfutaslowvideo behind adasuckharderfutaslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckfutafastvideo
    hide adasuckpovslowvideo
    hide adasuckharderfutaslowvideo
    with dissolve
    play channel2 "sounds/blow01.mp3"
    show harder:
        xpos 1700 ypos 700    
    show faster:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckslowbx()
    screen adasuckslowbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckFastbx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowbx")

    label AdaSuckFastbx:
    $ adasuckharderx = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfastx == False:
        mc "Do it FASTER, Harem Girl!"
        $ adasuckfastx = True
    show adasuckfutafastvideo behind adasuckfutaslowvideo
    show adasuckfutafastvideo behind adasuckpovfastvideo
    show adasuckfutafastvideo behind adasuckharderfutafastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckfutaslowvideo
    hide adasuckpovfastvideo
    hide adasuckharderfutafastvideo
    with dissolve
    play channel2 "sounds/blow02.mp3"
    window hide
    show harder:
        xpos 1700 ypos 700    
    show slower:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckfastbx()
    screen adasuckfastbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckSlowbx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastbx")

    label AdaSuckPOVSlowbx:
    $ adasuckharderx = False
    $ adasuckfastx = False
    window hide
    hide faster
    hide slower
    hide pov
    hide sceneicon
    hide harder
    hide softer
    hide cum
    show adasuckpovslowvideo behind adasuckfutaslowvideo
    show adasuckpovslowvideo behind adasuckpovfastvideo
    show adasuckpovslowvideo behind adasuckharderpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckfutaslowvideo
    hide adasuckpovfastvideo
    hide adasuckharderpovslowvideo
    with dissolve
    play channel2 "sounds/blow01.mp3"
    show harder:
        xpos 1700 ypos 700    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckslowpovbx()
    screen adasuckslowpovbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVFastbx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckSlowbx")

    label AdaSuckPOVFastbx:
    $ adasuckharderx = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfastx == False:
        mc "Do it FASTER, Harem Girl!"
        $ adasuckfastx = True
    window hide
    show adasuckpovfastvideo behind adasuckpovslowvideo
    show adasuckpovfastvideo behind adasuckfutafastvideo
    show adasuckpovfastvideo behind adasuckharderpovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckpovslowvideo
    hide adasuckfutafastvideo
    hide adasuckharderpovfastvideo
    with dissolve
    play channel2 "sounds/blow02.mp3"
    window hide
    show harder:
        xpos 1700 ypos 700    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckfastpovbx()
    screen adasuckfastpovbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVSlowbx")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckFastbx")

    label AdaSuckHarderSlowbx:
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderfutaslowvideo behind adasuckharderfutafastvideo
    show adasuckharderfutaslowvideo behind adasuckharderpovslowvideo
    show adasuckharderfutaslowvideo behind adasuckfutaslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderfutafastvideo
    hide adasuckharderpovslowvideo
    hide adasuckfutaslowvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show faster:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckharderslowbx()
    screen adasuckharderslowbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderFastbx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckSlowbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderFastbx:     
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderfutafastvideo behind adasuckharderfutaslowvideo
    show adasuckharderfutafastvideo behind adasuckharderpovfastvideo
    show adasuckharderfutafastvideo behind adasuckfutafastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderfutaslowvideo
    hide adasuckharderpovfastvideo
    hide adasuckfutafastvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show slower:
         xpos 1700 ypos 500     
    show pov:
         xpos 50 ypos 500     
    call screen adasuckharderfastbx()
    screen adasuckharderfastbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderSlowbx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckFastbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderPOVSlowbx:      
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderpovslowvideo behind adasuckharderfutaslowvideo
    show adasuckharderpovslowvideo behind adasuckharderpovfastvideo
    show adasuckharderpovslowvideo behind adasuckpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderfutaslowvideo
    hide adasuckharderpovfastvideo
    hide adasuckpovslowvideo
    with dissolve
    play channel2 "v032/blow03.mp3"
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckharderpovslowbx()
    screen adasuckharderpovslowbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVFastbx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

    label AdaSuckHarderPOVFastbx:    
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharderx == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharderx = True
    window hide
    show adasuckharderpovfastvideo behind adasuckharderpovslowvideo
    show adasuckharderpovfastvideo behind adasuckharderfutafastvideo
    show adasuckharderpovfastvideo behind adasuckpovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide adasuckharderpovslowvideo
    hide adasuckharderfutafastvideo
    hide adasuckpovfastvideo
    with dissolve
    window hide
    play channel2 "v032/blow03.mp3"
    show cum:
        xpos 1750 ypos 1020    
    show softer:
        xpos 1700 ypos 300    
    show slower:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adasuckharderpovfastbx()
    screen adasuckharderpovfastbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVSlowbx")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastbx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCumx")

label AdaSuckCumx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
mc "You're gonna make me blow if you keep this up! I..."
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
if adafuta == False:
    scene adasuckcum01 with dissolve
if adafuta:
    scene adasuckcum01
    show adasuckcum01b
    with dissolve
mc "FUCK! AAAH!!!"
window hide
with fastflash
mc "SO GOOD!"
if adafuta == False:
    scene adasuckcum02 with dissolve
if adafuta:
    scene adasuckcum02
    show adasuckcum02b
    with dissolve
mc "Oh DAMN!"
window hide
with hpunch
mc "GULP IT DOWN YOUR FUCKING SLAVE THROAT!!!"
if adafuta == False:
    scene adasuckcum03:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve  
    mc "Yeah, that's it, suck it ALL UP with that crazy tongue of yours!"
if adafuta:
    scene adasuckcum03b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
    mc "Yeah, that's it, suck it ALL UP with that crazy tongue of yours! It's making you cum too, isn't it? You FILTHY FUTA GIRL!"
window hide
with fastflash
aw "MMMMHHH! GGLLLBBB!"
play sound "v061/blowend.mp3"
if adafuta == False:
    scene adasuckcum04 with dissolve
    aw "Sssoo, ssssooo MUCH! I can't swallow it all!"
if adafuta:
    scene adasuckcum04
    show adasuckcum04b
    with dissolve
    aw "Yes Master! You're cumming SSSOO MUCH, it's making my cock fire like CRAZY!"

if adafuta == False:
    scene adasuckcum05:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.1
    with dissolve
if adafuta:
    scene adasuckcum05b:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.1
    with dissolve
play sound "sounds/wow.mp3"
aw "Your shots are so POWERFUL, Harem MASTER!"
window hide
with vpunch
mc "Just a few more shots, just a few more..."
stop channel2
if adafuta == False:
    scene adasuckcum06 with dissolve
if adafuta:
    scene adasuckcum06
    show adasuckcum06b
    with dissolve
play sound "sounds/lick02.mp3"
aw "But... * slup * ...What about your ASS REWARD?"
mc "Don't you worry about that... I'll get hard again in no time, cos I'm a SUPER-STUD!"

if adafuta == False:
    scene adasuckcum07 with dissolve
if adafuta:
    scene adasuckcum07b with dissolve
aw "Is that so? Then PROVE IT! And ravish my backdoor NOW! I WANT IT!"

if adafuta == False:
    scene adasuckcum08:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve    
if adafuta:
    scene adasuckcum08b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
if age >= 20:
    mc "You were doubting me? HERE, see that hard MEGADICK?"
if age >= 18 and age <= 19:
    mc "You were doubting me? HERE, see that hard TEENAGE MEGADICK?"
aw "Oh my..."
if adafuta == False:
    mc "That's what you want? SAY IT, you dirty girl!"
if adafuta:
    mc "That's what you want? SAY IT you dirty FUTA-GIRL!"
aw "I DO! TAKE ME, DO WHAT YOU WANT WITH MY DIRTY WHORE BODY, HAREM MASTER!"

if adafuta == False:
    scene adaroom10:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.1
    with dissolve
    mc "Then come and FEEL its HARDNESS pressing against you..."
if adafuta:
    scene adaroom10b:
        subpixel True
        xpos 0.0
        linear 6.0 xpos -0.1
    with dissolve
    mc "Then come and FEEL its HARDNESS pressing against your...still-hard but smaller futa-dick..."
play sound "sounds/moan02.mp3"
aw "Oooh..."
if adafuta == False:
    scene adaroom11 with dissolve

if adafuta:
    scene adaroom11
    show adaroom11b
    with dissolve
aw "What are you doing?"
mc "You won't be needing this..."
aw "WAIT, I..."

if adafuta == False:
    scene adaroom12 with dissolve
if adafuta:
    scene adaroom12
    show adaroom12b
    with dissolve
play sound "sounds/ripping.mp3"
aw "That was an expensive set!"
mc "Just buy a new one with that drug money. DO AS YOU'RE TOLD!"

scene adaroom13 with dissolve
aw "You're so MANLY... I can't say no even if I'm supposed to be the BOSS here..."
mc "That's right. When it comes to SEX, I'm DA BOSS!"

if adafuta == False:
    scene adaroom14:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
if adafuta:
    scene adaroom14b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
play sound "sounds/moan03.mp3"
aw "That feeling... OF a HUMONGOUS HORSECOCK right up my buttcrack..."
mc "Hop on the sofa, you need to stick your rosebud MUCH HIGHER than that!"

if adafuta == False:
    scene adaanalprefuck01a with dissolve
if adafuta:
    scene adaanalprefuck01b with dissolve
aw "You'd better fuck me REAL GOOD you hear me? Make it worth my while..."
mc "Come and IMPALE yourself on my ROCK-HARD DONG and I'll make it worth your while!"

if adafuta == False:
    scene adaanalstart with dissolve
if adafuta:
    scene adaanalfutastart with dissolve
play sound "sounds/moan06.ogg"
aw "OOOH... It's so BIG AND DEEP ALREADY!"
mc "Just take a deep breath. And..."
play channel2 "sounds/womansex04.mp3"

$ adaanalslowx = True

if adafuta == False:
    label AdaAssSlowx:
    $ adaanalfastx = False
    window hide
    show adaanalslowvideo behind adaanalfastvideo
    show adaanalslowvideo behind adaanalcloserslowvideo
    pause 1.0
    hide adaanalfastvideo
    hide adaanalcloserslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalslowx == False:
        $ adaanalslowx = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckslowx()
    screen adaanalfuckslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserSlowx")

    label AdaAssFastx:
    $ adaanalslowx = False
    window hide
    show adaanalfastvideo behind adaanalslowvideo
    show adaanalfastvideo behind adaanalcloserfastvideo
    pause 1.0
    hide adaanalcloserfastvideo
    hide adaanalslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalfastx == False:
        $ adaanalfastx = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckfastx()
    screen adaanalfuckfastx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserFastx")

    label AdaAssCloserSlowx:
    $ adaanalfastx = False
    window hide
    show adaanalcloserslowvideo behind adaanalslowvideo
    show adaanalcloserslowvideo behind adaanalcloserfastvideo
    pause 1.0
    hide adaanalcloserfastvideo
    hide adaanalslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalslowx == False:
        $ adaanalslowx = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckslowx()
    screen adaanalcloserfuckslowx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserFastx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssSlowx")

    label AdaAssCloserFastx:
    $ adaanalslowx = False
    window hide
    show adaanalcloserfastvideo behind adaanalfastvideo
    show adaanalcloserfastvideo behind adaanalcloserslowvideo
    pause 1.0
    hide adaanalfastvideo
    hide adaanalcloserslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    if adaanalfastx == False:
        $ adaanalfastx = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckfastx()
    screen adaanalcloserfuckfastx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserSlowx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssFastx")

if adafuta:
    label AdaAssSlowbx:
    $ adaanalfastx = False
    window hide
    show adaanalfutaslowvideo behind adaanalfutafastvideo
    show adaanalfutaslowvideo behind adaanalcloserfutaslowvideo
    pause 1.0
    hide adaanalfutafastvideo
    hide adaanalcloserfutaslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalslowx == False:
        $ adaanalslowx = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckslowbx()
    screen adaanalfuckslowbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssFastbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserSlowbx")

    label AdaAssFastbx:
    $ adaanalslowx = False
    window hide
    show adaanalfutafastvideo behind adaanalfutaslowvideo
    show adaanalfutafastvideo behind adaanalcloserfutafastvideo
    pause 1.0
    hide adaanalcloserfutafastvideo
    hide adaanalfutaslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalfast == False:
        $ adaanalfastx = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckfastbx()
    screen adaanalfuckfastbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssSlowbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserFastbx")

    label AdaAssCloserSlowbx:
    $ adaanalfastx = False
    window hide
    show adaanalcloserfutaslowvideo behind adaanalfutaslowvideo
    show adaanalcloserfutaslowvideo behind adaanalcloserfutafastvideo
    pause 1.0
    hide adaanalcloserfutafastvideo
    hide adaanalfutaslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    with dissolve
    if adaanalslowx == False:
        $ adaanalslowx = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckslowbx()
    screen adaanalcloserfuckslowbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserFastbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssSlowbx")

    label AdaAssCloserFastbx:
    $ adaanalslowx = False
    window hide
    show adaanalcloserfutafastvideo behind adaanalfutafastvideo
    show adaanalcloserfutafastvideo behind adaanalcloserfutaslowvideo
    pause 1.0
    hide adaanalfutafastvideo
    hide adaanalcloserfutaslowvideo
    hide cum
    hide sceneicon
    hide faster
    hide slower
    hide closer
    if adaanalfastx == False:
        $ adaanalfastx = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckfastbx()
    screen adaanalcloserfuckfastbx():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserSlowbx")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEndx")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssFastbx")

label AdaAssEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
mc "Get ready for a heavy dose of CUM ENEMA!!!"
if adafuta == False:
    scene adaanalcum01 with dissolve
if adafuta:
    scene adaanalcum01b with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge02.mp3"

mc "Like, RIGHT NOW! RHAAA!"
window hide
with fastflash
aw "AAAH, you're BLASTING with so much FORCE!"

if adafuta == False:
    scene adaanalcum02 with dissolve
    aw "And it's making ME blast titmilk all over the place too!"
    
if adafuta:
    scene adaanalcum02b with dissolve
    play sound "sounds/womancum01.mp3"
    aw "And it's making me cum again too!"
window hide
with hpunch
mc "OHHHH! GODAMN!!!"

if adafuta == False:
    scene adaanalcum03:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
if adafuta:
    scene adaanalcum03b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve

aw "Pull it out, I can't take it anymore, I'm gonna pass out!"

if adafuta == False:
    scene adaanalcum04 with dissolve
if adafuta:
    scene adaanalcum04b with dissolve
stop channel1
if age >= 20:
    mc "Alright, I'll spare your guts and deliver my MONSTERLOAD all over your Chinese bedchamber! RHAAA!"
if age >= 18 and age <= 19:
    mc "Alright, I'll spare your guts and deliver my TEENAGE MONSTERLOAD all over your Chinese bedchamber! RHAAA!"
window hide
with fastflash
aw "You're so filthy!"
window hide
with hpunch
mc "Claiming it as MY OWN as a TRUE HAREM MASTER!!!"
stop channel2
play sound "sounds/panting.mp3"
if adafuta == False:
    scene adaanalcum05:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
if adafuta:
    scene adaanalcum05b:
        subpixel True
        xpos -0.01 ypos -0.01 zoom 1
        linear 6 xpos -0.05 ypos -0.05 zoom 1.05
    with dissolve
aw "I'm going to have to get Ajizzai and Lian to help me clean up this massive CUM MESS you made..."
mc "Well, I think my job as Harem Master is done here."
play sound "sounds/moan03.mp3"
aw "My poor little harem slave ass..."
stop music
stop sound
stop channel2
stop channel1
jump WangGallery