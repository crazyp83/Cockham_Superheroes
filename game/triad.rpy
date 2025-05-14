label ChineseTriad:
if seentriad == False:
    jump FirstTriad
if seentriad and mclevel02 == False:
    jump SecondTriad
if seentriad and mclevel02:
    jump WangTriad
    
label SecondTriad:
scene triad01 with fade
mc "Okay, waiting..."
mc "Nobody? Not even some ninja about to appear suddenly?"
mc "I'm out of here then, this place is BORING."
jump Main

label FirstTriad:
$ seentriad = True
scene triad01 with fade
play music "sounds/relax.mp3"
show ajizzai01 at left with moveinleft
show ajizzai01 at left:
    breathe
aj "Bow down to the Chinese Triad Empress, vile creature!" 
play sound "sounds/gong.mp3"
mc "Who? Where?"
window hide
play sound "sounds/puffsmoke.mp3"
show smokepuff with dissolve
$ renpy.pause(0.5, hard='True')
hide smokepuff
show triadwangappear
with fastdissolve
aw "Me. Come forward, [hero]. I have heard of you."
hide ajizzai01
show ajizzai02 at left
with fastdissolve
aj "CRAWL on your knees as you approach her!"
show permanentada at posadatext with dissolve
$ renpy.pause(0.5, hard=True)
menu:
    "Ada Wang has a wang (futa option)":
        $ adafuta = True
    "Ada Wang has no wang (no futa option)":
        $ adafuta = False
play sound "sounds/gong.mp3"
if adafuta == False:
    scene wangthrone01
    with dissolve
    show lianshi01 at farright with moveinright
    show lianshi01 at farright:
        breathe
if adafuta:
    scene wangthrone01
    show wangthrone01b
    with dissolve
    show lianshi01 at farright with moveinright
    show lianshi01 at farright:
        breathe
aw "Why have you come? In MY palace."
mc "It's a... delicate matter. Involving a chastity device. I..."
hide lianshi01
show lianshi02 at farright
with fastdissolve
ls "SPEAK UP!"
mc "Do you know a girl named \"Honoka\"?"
hide lianshi02
show lianshi01 at farright
with fastdissolve
show lianshi01 at farright:
    breathe
aw "Maybe. What about her?"
mc "I suspect her being behind a devious plot to blackmail the Mayor."
if adafuta == False:
    scene wangthrone02
    show lianshi02 at farright
    with dissolve
if adafuta:
    scene wangthrone02
    show wangthrone02b 
    show lianshi02 at farright
    with dissolve
aw "The Mayor is a trouble-maker! He has brought this unto himself!"
mc "Are you... admitting that YOU are behind this?"
if adafuta == False:
    scene wangthrone01
    show lianshi01 at farright
    with dissolve
if adafuta:
    scene wangthrone01
    show wangthrone01b 
    show lianshi01 at farright
    with dissolve
aw "If the Mayor were to be more... lenient on building permits, I'm sure this matter could easily be resolved."
mc "I see. So it's YOU then!"
if adafuta == False:
    scene wangthrone02
    show lianshi02 at farright
    with dissolve
if adafuta:
    scene wangthrone02
    show wangthrone02b 
    show lianshi02 at farright
    with dissolve
aw "That is YOUR interpretation. Based on zero evidence."
mc "Yeah, but..."
if adafuta == False:
    scene wangthrone01
    show lianshi01 at farright
    with dissolve
if adafuta:
    scene wangthrone01
    show wangthrone01b 
    show lianshi01 at farright
    with dissolve
show lianshi01 at farright:
    breathe
aw "Ajizzai! Offer [hero] a Chinese massage as a sign of goodwill. And to make him understand what needs to be done here for that small matter to be resolved..."
aj "Yes, Mistress. What type of massage should we provide him?"
aw "Give him a... number 7. With a side of 11."
mc "Oooh, my lucky numbers! Do I get a fortune cookie too?"
show ajizzai02 at left with moveinleft
aj "Follow me to the parlor, [hero]."

label Misohawny:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
scene chinesemassage01 with fade
play music "sounds/asianmusic02.mp3"
aj "Welcome to Misohawny Chinese Parlor, [hero]."
mc "Thank you for the warm welcome, err, ninja girl. Who is now in a sexy kimono."
scene chinesemassage02 with dissolve
aj "Please take your towel off and lie on the massage table face down."
if newmassage:
    mc "With my cock hanging in that hole, right?"
    aj "Of course."
if newmassage == False:
    mc "Why is there a hole in the middle?"
    if age >= 20:
        aj "That's for your cock. We are aware of how ENORMOUS you are, [hero] and we aim to minimize your discomfort. That way, your giant white package won't be squeezed underneath your body."
    if age >= 13 and age <= 19:
        aj "That's for your cock. We are aware of how ENORMOUS you are, [hero] and we aim to minimize your discomfort. That way, your giant white teenage package won't be squeezed underneath your body."
    if age <= 12:
        aj "That's for your cock. We are aware of how ENORMOUS you are, [hero] and we aim to minimize your discomfort. That way, your giant white preteen package won't be squeezed underneath your body."
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
if newmassage:
    aj "You seem quite tense. Let me relieve the stress for you..."
    mc "That's a good idea."
if newmassage == False:
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
if newmassage:
    mc "Oooh... I had forgotten how weirdly good that felt..."
if newmassage == False:
    mc "Oooh... That's a first, someone's sticking something up my ass. Good thing it's not a cock..."
scene chinesemassage10 with dissolve
aj "It appears this is causing an uncontrollable and PLENTIFUL precum leakage from your urethra... Let me call the clean-up girl..."
if newmassage:
    mc "That other chick?"
    scene chinesemassage11 with dissolve
    aj "That's right. Lian Shi will clean your cummy mess like last time. And provide you with a side of number 11."
    mc "And she's underneath the table again?"
    aj "Indeed."
    scene chinesemassage12 with dissolve
    play sound "sounds/boymoan.mp3"
    ls "I need to put some more STEEL in that massive weapon..."
    aj "Yes, you need to make him SUPER-HARD."
    scene chinesemassage13 with dissolve
    play sound "sounds/lick03.mp3"
    ls "My soft hands will do the trick..."
    scene chinesemassage14 with dissolve
    play sound "sounds/lick01.ogg"
    if age >= 20:
        ls "Your Alpha King Dong is growing... And getting harder."
    if age >= 13 and age <= 19:
        ls "Your Teen King Dong is growing... And getting harder."
    if age <= 12:
        ls "Your Preteen King Dong is growing... And getting harder."
    scene chinesemassage14b with dissolve
    play sound "sounds/lick03.mp3"
    ls "A few more tugs on that great big donkey-dick..."
    scene chinesemassage14 with dissolve
    play sound "sounds/lick01.ogg"
    mc "Oh God..."
    scene chinesemassage14c with dissolve
    play sound "sounds/lick03.mp3"
    ls "You are splattering pre-cum all over my breasts, you dirty boy... I think you are ready."
    scene chinesemassage15 with dissolve
    ls "Ready for a MIGHTY SPERM RELEASE."
    scene chinesemassage16 with dissolve
    ls "We are here to make you feel better, remember?"
    scene chinesemassage17 with dissolve
    play sound "sounds/boymoan03.mp3"
    mc "UUUUH! It hurts so much! And feels good too..."
    ls "And once I remove it, you will reach the NIRVANA of PLEASURE!"
    scene chinesemassage18 with dissolve
    aj "Just relax, [hero]. You know very well Lian Shi was an EXPERT MILKER, don't you?"
    mc "Sure, but...!"
    aj "Your MASSIVE cum-laden balls need sweet release..."
    scene chinesemassage19 with dissolve
    aj "And you need a good spanking for being such a horse-hung stud who thinks he can fuck anyone he wants!"
    mc "I only do it for the good of mankind!"
    scene chinesemassage20 with dissolve
    play sound "sounds/slap.mp3"
    aj "Liar! That's not what I heard!"
    mc "Ouch!"
    scene chinesemassage19 with dissolve
    aj "Your libido is so high you just can't help yourself!"
    scene chinesemassage20 with dissolve
    play sound "sounds/slap.mp3"
    mc "Please!"
    scene chinesemassage19 with dissolve
    aj "And you just LOVE showing what a STUD you are, SAY IT!"
    scene chinesemassage20 with dissolve
    play sound "sounds/slap.mp3"
    mc "Alright, alright, I admit it!"
    scene chinesemassage19 with dissolve
    aj "Now that's better! You filthy, dirty, donkey-dicked boy..."
if newmassage == False:
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
    if age >= 13 and age <= 19:
        ls "Your Teen King Dong is growing... And getting harder."
    if age <= 12:
        ls "Your Preteen King Dong is growing... And getting harder."
    scene chinesemassage14b with dissolve
    play sound "sounds/lick03.mp3"
    ls "A few more tugs on that great big donkey-dick..."
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
if newmassage:
    mc "Y... yes... I suppose she did... * pant *"
    scene chinesemassageend with dissolve
    aj "So you won't be coming back with Audit Girl, right?"
    mc "No, no, I won't. Can I come back alone though?"
    scene chinesemassage37 with dissolve
    aj "Of course, you are always welcome. For a nuber 7 with a side of 11."
                                                    
if newmassage == False:
    mc "Y... yes... * Hang on, I recognize this tattoo... It's the same one that Honoka has! *"
    window hide
    play sound "sounds/skill.mp3"
    show mission03progress at poslocation
    $ renpy.pause(0.5, hard='True')
    pause
    hide mission03progress
    scene chinesemassageend with dissolve
    aj "Before you leave, I have a message for you from Ada Wang..."
    mc "Uuurh, what?"
    aj "The message is: \"Don't fuck with the Triad or you'll regret it.\""
    mc "I would have preferred a fortune cookie message. They're usually less violent."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label WangTriad:
$ seenwangtriad = True
scene triad01 with fade
play music "sounds/relax.mp3"
show ajizzai01 at left with moveinleft
show ajizzai01 at left:
    breathe
aj "Bow to the mighty Ada Wang!" 
play sound "sounds/gong.mp3"
window hide
play sound "sounds/puffsmoke.mp3"
show smokepuff with dissolve
$ renpy.pause(0.5, hard='True')
hide smokepuff
show triadwangappearb
with fastdissolve
aw "You again. The traitor who tried to foil my blackmail attempt against the Mayor."
mc "Well, err... You still got your permit, right?"
hide ajizzai01
show ajizzai02 at left
with fastdissolve
aj "CRAWL on your knees as you approach her!"
scene wangthrone03 with dissolve
aw "Of course. Despite YOUR interference."
mc "Then it's just water under the bridge, right?"
scene wangthrone04 with dissolve
aw "I'll decide. What brings you here?"
menu:
    "I am your devoted servant. For any mission you may have for me." if adawanked == False:
        scene wangthrone03 with dissolve
        aw "Is that so? And how do I know I can trust you?"
        mc "Err... Cos I'm a trustworthy person?"
        $ adawanked = True
        jump AdaWangChambers
    "Just passing by and checking on your illicit activities.":
        scene wangthrone03 with dissolve
        aw "And what would be illicit about what I do here?"
        mc "Err... Like, those naughty massages? I think they might be illegal. I'll have to check with Audit Girl."
        scene wangthrone04 with dissolve
        aw "Why don't you get one first before you do that checking? I'm sure this will dissipate any suspicion you may have..."
        mc "I suppose I could try that indeed..."
        aw "Ajizzai! Give [hero] a... number 7. With a side of 11."
        show ajizzai02 at left with moveinleft
        aj "Follow me to the parlor, [hero]."
        $ newmassage = True
        jump Misohawny
    "Just passing by to show my respect." if adawanked:
        scene wangthrone03 with dissolve
        aw "You are starting to grow on me. But I have no use for you right now. You may leave."
        mc "Not even a handjob with your cock-choker?"
        scene wangthrone04 with dissolve        
        aw "I'm too busy. LEAVE and come back another time!"
        jump AdaWangChambers

label AdaWangChambers:
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
if age >= 13 and age <= 19:
    aw "That's a good boy. A good horse-hung TEENAGE boy."
if age <= 12:
    aw "That's a good boy. A good horse-hung PRETEEN boy."
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

if adafuta:
    label AdaFutaWankSlow:
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
    $ adawankfast = False
    if adawankslow == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslow = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show closer:
         xpos 50 ypos 500     
    call screen adafutawankslow()
    screen adafutawankslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaFutaWankFrontSlow")

    label AdaFutaWankFast:
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
    $ adawankslow = False
    if adawankfast == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfast = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show closer:
         xpos 1700 ypos 500     
    call screen adafutawankfast()
    screen adafutawankfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEnd")
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaFutaWankFrontFast")

    label AdaFutaWankFrontSlow:
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
    $ adawankfast = False
    if adawankslow == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslow = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adafutawankcloserslow()
    screen adafutawankcloserslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFrontFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankSlow")

    label AdaFutaWankFrontFast:
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
    $ adawankslow = False
    if adawankfast == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfast = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show sceneicon:
         xpos 1700 ypos 500     
    call screen adafutawankcloserfast()
    screen adafutawankcloserfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFrontSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaFutaWankEnd")
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaFutaWankFast")

    label AdaFutaWankEnd:
    hide cum
    hide slower
    hide faster
    hide closer
    hide sceneicon

if adafuta == False:
    label AdaWankSlow:
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
    $ adawankfast = False
    if adawankslow == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslow = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show closer:
         xpos 50 ypos 500     
    call screen adawankslow()
    screen adawankslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaWankFrontSlow")

    label AdaWankFast:
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
    $ adawankslow = False
    if adawankfast == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfast = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show closer:
         xpos 1700 ypos 500     
    call screen adawankfast()
    screen adawankfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEnd")
        button:
            xpos 1700
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaWankFrontFast")

    label AdaWankFrontSlow:
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
    $ adawankfast = False
    if adawankslow == False:
        aw "Well, look at that, your cock really seems to like it, doesn't it? It's literally TWITCHING!"
        $ adawankslow = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500     
    show sceneicon:
         xpos 50 ypos 500     
    call screen adawankcloserslow()
    screen adawankcloserslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFrontFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEnd")
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankSlow")

    label AdaWankFrontFast:
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
    $ adawankslow = False
    if adawankfast == False:
        aw "Let me increase the pace and get that ROCK-HARD dong closer to the edge!"
        $ adawankfast = True
    window hide
    pause
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 50 ypos 500     
    show sceneicon:
         xpos 1700 ypos 500     
    call screen adawankcloserfast()
    screen adawankcloserfast():
        modal True
        button:
            xpos 50
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFrontSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaWankEnd")
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaWankFast")

    label AdaWankEnd:
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
if age >= 13 and age <= 19:
    aw "Keep going, you filthy teenage boy! You're spewing EVERYWHERE!"
if age <= 12:
    aw "Keep going, you filthy pre-teen boy! You're spewing EVERYWHERE!"
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

label AdaTest:
    
if mission07win and mission08 == False:
    scene wangpremission01 with dissolve
    aw "Since you've been such a good little slave-boy, I've decided to grant you the honor of a try-out in the Triad. As a reward, you will be allowed to stick yur giant dong up my wanghole."
    mc "Really? Wow, I'm so honored to be recognized as a potential violent criminal."
    aw "Shut up! Your insolence is duly noted. Do you accept the mission or must I torture your cock into submission?"
    menu:
        "Err... I guess I... accept the mission? (work for the Triad)":
            aw "Excellent... Let me get cleaned up and I'll tell what it's about."
            jump TriadMission
        "Na, it sounds fishy. Like a Chinese dish of rat-à-touille.":
            scene wangpremission02 with dissolve
            aw "That is VERY disappointing! And also won't make you advance much towards your ultimate goal... Except if you decide to work for the ENEMY!"
            mc "Oh, and...who would that be?"
            aw "The Mafia of course! You'd better not go and see them or I'll have to TORTURE YOUR COCK UNTIL IT FALLS OFF!"
            mc "Right, right..."
            jump EndWangCockwank

label EndWangCockwank:
aw "You did reasonably well... I might have to work on you a bit more before I decide to USE you."
mc "My...my pleasure..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop sound
stop music
jump Main

label TriadMission:
$ mission08triad = True
scene mafiaofficebackground
show excella04 with fade
ex "So [hero]...Welcome to the Famiglia! Here's our mission. The Famiglia's mission. And therefore YOUR mission."
mc "There's no way out is there once you're in?"
hide excella04
show excella03
with fastdissolve
ex "There is. In a coffin."
mc "I see. I totally accept the mission then. What is it about?"

play music "sounds/mafiamusic.mp3"
scene docks04 with fade
play sound "v07/carpark.mp3"
$ renpy.pause(1.0, hard='True')
scene docks05 with fastdissolve
$ renpy.pause(2.0, hard='True')
scene docks06 with fastdissolve
$ renpy.pause(1.0, hard='True')
stop sound
scene docks07:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with fastdissolve
play sound "v07/cardoor.mp3"
aw "The seller should arrive soon. Let's check out the hangar beforehand, I don't want any nasty surprises!"    
scene docks12 with dissolve
aw "Lian, you wait for the seller's truck, Ajizzai and [hero], go check the back room while I check the front room."
mc "I don't have any decent weapon, like the gun that you have."
scene docks13 with dissolve
aw "You have a samurai sword, don't you? That's a VERY DECENT weapon and the one that is typically used by Triad gang members. Use that if you want to be one of ours."
mc "Ah yes, that's true, I remember now. A gift from the Mayor. It's in my inventory."

scene docks14:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
aj "Watch out for anything unusual and be at the ready to intervene IMMEDIAT..."

scene docks15 with dissolve
play sound "sounds/gunfire.mp3"
aj "...Someone is shooting at us!"

$ img_l = []
$ l2_l = []
$ img_l.append("usestrength")
$ l2_l.append("DocksTriadStrength")
$ img_l.append("useagility")
$ l2_l.append("DocksTriadStrength")
if img_l:
    call screen usepower(img_l, "DocksTriadNoStrength", l2_l) with dissolve

label DocksTriadStrength:
if selected_power == "useagility":
    jump DocksTriadAgility
scene docks16 with dissolve
$ usedstrength += 1
play sound "sounds/gunfire.mp3"
mc "MASSIVE ROCK-HARD ABS FLEX!"
jump DocksTriadNext

label DocksTriadAgility:
scene docks17 with dissolve
$ usedagility += 1
play sound "v07/matrixbullet.mp3"
mc "SUPER-BULLET-DODGE!"
jump DocksTriadNext


label DocksTriadNoStrength:
scene docks18:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/gunfire.mp3"
mc "AAAH, I'm hit... Like, CRITICALLY!"
scene blackscreen with fade
show gameovericon:
    xpos 600 ypos 400
pause
return

label DocksTriadNext:
aj "Let's take covert, quick!"
scene docks19 with dissolve
play channel2 "sounds/gunfire.mp3"
mc "We need some FIREPOWER. These damn samurai swords will never be enough against machine guns!"
aj "The Triad never surrenders and ALWAYS FIGHTS ON!"
scene docks20 with dissolve
aw "I'll cover you! [hero], take the mafia goon overhead, Ajizzai, cut that generic G8 male figure down below into pieces!"
mc "But... He's got a MACHINE GUN!"
scene docks21 with dissolve
aw "You're a SUPERHERO! ACT LIKE ONE!"
mc "I don't like my chances..."
scene docks22 with dissolve
mc "* Alright, HERE I GO! *"
scene docks23 with dissolve
stop channel2
play sound "sounds/knifecut.mp3"
mc "SUPER-FAST NINJA MOVE!"
gg "Noooo!"
scene docks24 with dissolve
play channel2 "v07/forklift.mp3"
ex "I haven't said my last word, hero!"
scene docks25 with dissolve
mc "* Ajizzai is hurt. And Excella Gionne is going to kill her if I don't do something!"
scene docks26 with dissolve
mc "That's it, I don't have any choice!"
ex "Don't stand in my way [hero] or you'll REGRET IT!"
scene docks27 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "My Super-Strength should be enough to hold this pallet from falling over and crushing Ajizzai!"
ex "Damn you [hero]!"
scene docks28 with dissolve
mc "Good move, [name], now I've got her! Get down Excella or I'll shoot you on the spot!"
scene docks29 with dissolve
stop channel2  
aw "What are your last words, Excella Gionne?"
ex "[hero]! You can't let her kill me in cold blood like this, you're a Super-Hero!"
menu:
    "Interfere to stop the killing (+1 Super-Hero)":
        scene docks32 with dissolve
        play sound "sounds/panting.mp3"
        mc "Stop this, Ada! She needs to face the justice of the Justice League! Or the CCPD, or some randomly-assigned judge. But NOT LIKE THIS!"
        call Good
        $ sparedexcella = True
        aw "By stopping me, you are disturbing the Yin and the Wang of the Triad [hero]! But I suppose seeing her rot in a damp cell has its benefits, so I'll spare her for you..."
        jump TriaMissionEnd
    "Let Ada Wang dispose of her (+1 Super-Villain)":
        scene docks31 with dissolve
        mc "I ain't seen nothin'. Apart from YOU shooting at us and dying during the ensuing fire exchange, Excella! Your reign of terror is OVER! (* And MINE begins! *)"
        $ sparedexcella = False
        call Evil
        aw "You made the right choice [hero]... The SUPER-VILLAIN CHOICE. And now..."

label TriaMissionEnd:
scene docks33 with fade
aw "Lin, secure the cargo. Ajizzai, pay the seller. And give a box to [hero] as a gift from the Triad..."
window hide
$ inventorydrugs = True
play sound "sounds/achievement.mp3"
show acquiredchromium at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Drugs? And what do they do?"
aw "A boost of energy, some memory loss and an increase in heart failures."
mc "That sounds... dangerous."
hide acquiredchromium
if sparedexcella:
    mc "I'll wait for the cops to hand them Excella and I'll meet you back at the Triad HQ for my \"reward\"..."
    aw "Sure, whatever..."
if sparedexcella == False:
    aw "Let's get out of here and head back to the temple. You and me [name]... For your \"reward\"..."
window hide
play sound "sounds/winning.mp3"
show mission08icon at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
$ mission08triadwin = True
stop channel2
stop music

label AdaWangAnal:

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
if age >= 13 and age <= 18:
    aw "You like that don't you, dirty boy? You like having a mature woman slurp up all the excess pre-cum that you TEENAGE MEGA-DONG can produce?"
if age <= 12:
    aw "You like that don't you, dirty boy? You like having a mature woman slurp up all the excess pre-cum that you PRE-TEEN MEGA-DONG can produce?"
   

if adafuta == False:
    scene adasuckstart with dissolve

if adafuta:
    scene adasuckfutastart with dissolve
mc "Fuck yeah, keep sucking, keep sucking Ada and I'll reward with a mighty dose of a REAL MAN'S CUM!"

if adafuta == False:
    label AdaSuckSlow:
    $ adasuckharder = False
    $ adasuckfast = False
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
    call screen adasuckslow()
    screen adasuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckFast")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlow")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlow")

    label AdaSuckFast:
    $ adasuckharder = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfast == False:
        if adaharem == False:
            mc "Do it FASTER!"
        if adaharem :
            mc "Do it FASTER, Harem Girl!"
        $ adasuckfast = True
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
    call screen adasuckfast()
    screen adasuckfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckSlow")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFast")

    label AdaSuckPOVSlow:
    $ adasuckharder = False
    $ adasuckfast = False
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
    call screen adasuckslowpov()
    screen adasuckslowpov():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVFast")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlow")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckSlow")

    label AdaSuckPOVFast:
    $ adasuckharder = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfast == False:
        if adaharem == False:
            mc "Do it FASTER!"
        if adaharem :
            mc "Do it FASTER, Harem Girl!"
        $ adasuckfast = True
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
    call screen adasuckfastpov()
    screen adasuckfastpov():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVSlow")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckFast")

    label AdaSuckHarderSlow:
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderslow()
    screen adasuckharderslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderFast")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckSlow")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderFast:     
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderfast()
    screen adasuckharderfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderSlow")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderPOVSlow:      
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderpovslow()
    screen adasuckharderpovslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVFast")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlow")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderPOVFast:    
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderpovfast()
    screen adasuckharderpovfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVSlow")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFast")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")


if adafuta:
    label AdaSuckSlowb:
    $ adasuckharder = False
    $ adasuckfast = False
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
    call screen adasuckslowb()
    screen adasuckslowb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckFastb")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowb")

    label AdaSuckFastb:
    $ adasuckharder = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfast == False:
        if adaharem == False:
            mc "Do it FASTER!"
        if adaharem :
            mc "Do it FASTER, Harem Girl!"
        $ adasuckfast = True
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
    call screen adasuckfastb()
    screen adasuckfastb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckSlowb")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastb")

    label AdaSuckPOVSlowb:
    $ adasuckharder = False
    $ adasuckfast = False
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
    call screen adasuckslowpovb()
    screen adasuckslowpovb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVFastb")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckSlowb")

    label AdaSuckPOVFastb:
    $ adasuckharder = False
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    window hide
    if adasuckfast == False:
        if adaharem == False:
            mc "Do it FASTER!"
        if adaharem :
            mc "Do it FASTER, Harem Girl!"
        $ adasuckfast = True
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
    call screen adasuckfastpovb()
    screen adasuckfastpovb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckPOVSlowb")
        button:
            xpos 1700
            ypos 700
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckFastb")

    label AdaSuckHarderSlowb:
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderslowb()
    screen adasuckharderslowb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderFastb")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckSlowb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVSlowb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderFastb:     
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderfastb()
    screen adasuckharderfastb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderSlowb")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckFastb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderPOVFastb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderPOVSlowb:      
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderpovslowb()
    screen adasuckharderpovslowb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVFastb")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVSlowb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderSlowb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

    label AdaSuckHarderPOVFastb:    
    hide cum
    hide faster
    hide slower
    hide harder
    hide softer
    hide pov
    hide sceneicon
    with dissolve
    if adasuckharder == False:
        mc "You can go deeper on that dong, I know you can!"
        $ adasuckharder = True
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
    call screen adasuckharderpovfastb()
    screen adasuckharderpovfastb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaSuckHarderPOVSlowb")
        button:
            xpos 1700
            ypos 300
            xysize(120, 60)        
            action Jump ("AdaSuckPOVFastb")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaSuckHarderFastb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaSuckCum")

label AdaSuckCum:
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
if age >= 13 and age <= 19:
    mc "You were doubting me? HERE, see that hard TEENAGE MEGADICK?"
if age <= 12:
    mc "You were doubting me? HERE, see that hard PRE-TEEN MEGADICK?"
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

if adafuta == False:
    label AdaAssSlow:
    $ adaanalfast = False
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
    if adaanalslow == False:
        $ adaanalslow = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckslow()
    screen adaanalfuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserSlow")

    label AdaAssFast:
    $ adaanalslow = False
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
    if adaanalfast == False:
        $ adaanalfast = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckfast()
    screen adaanalfuckfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserFast")

    label AdaAssCloserSlow:
    $ adaanalfast = False
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
    if adaanalslow == False:
        $ adaanalslow = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckslow()
    screen adaanalcloserfuckslow():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserFast")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssSlow")

    label AdaAssCloserFast:
    $ adaanalslow = False
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
    if adaanalfast == False:
        $ adaanalfast = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckfast()
    screen adaanalcloserfuckfast():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserSlow")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssFast")

if adafuta:
    label AdaAssSlowb:
    $ adaanalfast = False
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
    if adaanalslow == False:
        $ adaanalslow = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckslowb()
    screen adaanalfuckslowb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssFastb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserSlowb")

    label AdaAssFastb:
    $ adaanalslow = False
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
        $ adaanalfast = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show closer:
         xpos 50 ypos 500    
    call screen adaanalfuckfastb()
    screen adaanalfuckfastb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssSlowb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssCloserFastb")

    label AdaAssCloserSlowb:
    $ adaanalfast = False
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
    if adaanalslow == False:
        $ adaanalslow = True
        mc "Your tight ass is just so exquisite, Ada..."
    show cum:
        xpos 1750 ypos 1020    
    show faster:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckslowb()
    screen adaanalcloserfuckslowb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserFastb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssSlowb")

    label AdaAssCloserFastb:
    $ adaanalslow = False
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
    if adaanalfast == False:
        $ adaanalfast = True
        play sound "sounds/boymoan02.mp3"
        mc "Oh Damn... Faster is BETTER!"    
    window hide
    show cum:
        xpos 1750 ypos 1020    
    show slower:
         xpos 1700 ypos 500    
    show sceneicon:
         xpos 50 ypos 500    
    call screen adaanalcloserfuckfastb()
    screen adaanalcloserfuckfastb():
        modal True
        button:
            xpos 1700
            ypos 500
            xysize(180, 60)        
            action Jump ("AdaAssCloserSlowb")
        button:
            xpos 1750
            ypos 1020
            xysize(120, 60)        
            action Jump ("AdaAssEnd")
        button:
            xpos 50
            ypos 500
            xysize(120, 60)        
            action Jump ("AdaAssFastb")

label AdaAssEnd:
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
if age >= 13 and age <= 19:
    mc "Alright, I'll spare your guts and deliver my TEENAGE MONSTERLOAD all over your Chinese bedchamber! RHAAA!"
if age <= 12:
    mc "Alright, I'll spare your guts and deliver my PRE-TEEN MONSTERLOAD all over your Chinese bedchamber! RHAAA!"
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
aw "I'm going ot have to get Ajizzai and Lian to help me clean up this massive CUM MESS you made..."
if seentriadreward:
    mc "Well, I think my job as Harem Master is done here."
    play sound "sounds/moan03.mp3"
    aw "My poor little harem slave ass..."
if seentriadreward == False:
    mc "Phew!... And now, you're in my Harem, you hear me?"
    $ adaharem = True
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlada at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause            
    play sound "sounds/moan03.mp3"
    aw "I hear you... Harem MASTER."

$ seentriadreward = True
jump Main