label ExcellaGallery:
stop channel3
play channel3 "sounds/covertmusic.mp3"
scene excellabackground
show excellamaingallery at gallerypos01 with moveinleft
call screen galleryexcella()
screen galleryexcella():
    text "{font=Gui/Heroes Legend.ttf}Naughty Excella Gionne{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryexcella"), Jump ("MainGallery02")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryexcella"), Jump ("ExcellaGalleryAnim")]

    if renpy.seen_image("excellaoffice01"):
        imagebutton:
            focus_mask True
            idle "gallery/excellagallery01.png" xpos 400 ypos 100
            hover "gallery/excellagallery01.png"
            action Jump ("ExcellaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Office Titfuck{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("excellaoffice01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("ExcellaGallery01hint")

    if renpy.seen_image("excellatease00"):
        imagebutton:
            focus_mask True
            idle "gallery/excellagallery02.png" xpos 750 ypos 100
            hover "gallery/excellagallery02.png"
            action Jump ("ExcellaGallery02")
    text "{font=Gui/Heroes Legend.ttf}Office Seduction{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("excellatease00") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("ExcellaGallery")

    if renpy.seen_image("mafiareward01"):
        imagebutton:
            focus_mask True
            idle "gallery/excellagallery03.png" xpos 1100 ypos 100
            hover "gallery/excellagallery03.png"
            action Jump ("ExcellaGallery03")
    text "{font=Gui/Heroes Legend.ttf}Harem Anal Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("mafiareward01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("ExcellaGallery")

label ExcellaGallery01hint:
show excellamaingallery at gallerypos01
show excellagallery01 at posgalleryhintpic
show excellagalleryhint01 at posgalleryhint
pause
hide excellagalleryhint01
hide excellagallery01
call screen galleryexcella()

label ExcellaGalleryAnim:
call screen screenanimexcella()
screen screenanimexcella():
    modal True
    add "gallery/excellabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "excellaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "excellaanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "excellaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimexcella"), SetVariable ("animcount", 1), Jump ("ExcellaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Excella Gionne{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero01
    text "{font=Gui/Heroes Legend.ttf}Age: 38{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height:5ft9{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}38EE-26-40{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Seduction{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Titfucking/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Doggy{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/excellaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimexcella")]
    add "gallery/excellaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimexcella")]
    add "gallery/excellaanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimexcella")]
            
label ExcellaGallery01:
stop channel3
play music "sounds/sexy11.mp3"
scene excellaoffice00 with dissolve
mc "Wh... Why is she showing me her leg like that???"
scene excellaoffice00b with dissolve
mc "Damn, she's changed into a SEXY gansta outfit!"
scene excellaoffice00c with dissolve
ex "So, [hero], let's talk \"business\"..."
scene excellaoffice01 with dissolve
mc "Wh.. What business did you have in mind?"
scene excellaoffice02 with dissolve
ex "I was thinking... You help me, and I help you... A win-win kind of business, right?"
mc "That sounds... like..."
scene excellaoffice03 with dissolve
ex "For example, our books... They're clean."
scene excellaoffice04 with dissolve
mc "Ar... Are they? Audit Girl is..."
scene excellaoffice05 with dissolve
ex "...looking at them, and she will find NOTHING, understood?"
scene excellaoffice02 with dissolve
mc "This is highly inap..."
scene excellaoffice04 with dissolve
ex "And in exchange, I'll help YOU."
mc "Err... How so?"
scene excellaoffice06 with dissolve
ex "I'm sure we can find some arrangements to your liking..."
mc "I... don't know if..."
scene excellaoffice07 with dissolve
ex "Your cock seems to be demanding some attention... I could tend to it..."
mc "I.. Damn it, I'm getting HARD!"
scene excellaoffice08 with dissolve
ex "Indeed you are... And this great big whopper needs some relief, I can tell..."
mc "Fuck, what an ass!"
scene excellaoffice09 with dissolve
ex "You ain't seen nothing yet, [hero]!"
mc " * She's Super-Seducing me and there's nothing I can do about it,I'm just TOO HORNY! *"
scene excellaoffice10 with dissolve
if age >= 20:
    ex "Let me take good care of that monstercock... With my HUGE BREASTS!"
if age >= 18 and age <= 19:
    ex "Let me take good care of that teenage monstercock... With my HUGE BREASTS!"
scene excellaoffice11 with dissolve
play sound "sounds/boymoan.mp3"
mc "Damn! Mamma Mia!"
ex "Maybe I should squeeze my tits a little bit more around that shaft..."
scene excellaoffice12 with dissolve
play sound "sounds/boymoan02.mp3"
ex "And lick the abundant precum that is flowing from your throbbing cock..."
scene excellaoffice13 with dissolve
ex "There's so much of it, it seems like you're about to BURST!"
mc "Oh God, oh God..."
scene excellaoffice14 with dissolve
play sound "sounds/boymoan04.mp3"
ex "My tits were THAT enticing, [hero]?"
scene excellaoffice15 with dissolve
ex "You just couldn't hold back and now you're having a FULL-BLOWN ORGASM!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "AAAAH, FUCK, I'm CU-UUU-MMM-IIING!!!"
scene excellaoffice16 with dissolve
mc "AAAH, what are you doing?"
ex "Do you agree that our books are CLEAN, [hero]?"
mc "Yes, YES, I AGREE, LET ME CUM!!!"
scene excellaoffice17 with dissolve
ex "Good, now you can come! Come as MUCH AS YOU LIKE!"
play sound "sounds/boymoan03.mp3"
window hide
with hpunch
ex "That's it, let it all out, let my sumptuous tits MILK YOU DRY!"
scene excellaoffice18 with dissolve
play sound "sounds/slurp.mp3"
ex "Wow, your balls were FULL TO THE BRIM it seems!"
play sound "sounds/panting.mp3"
mc "No, I... usually come... That much..."
ex "Impressive, young stallone... And tasty too... Let me get cleaned up and let's go back to the gallery..."
stop music
jump ExcellaGallery

label ExcellaGallery02:
stop channel1
stop channel3
scene mafiaofficebackground with fade
show excella01 with dissolve
ex "So, you're back... And I suppose you want to prove to me once again that you would be an ideal asset to the Famiglia?"
mc "These were my intentions indeed..."
hide excella01
show excella02
with dissolve
ex "You're certainly already proven your studly worth... But I'd like to be reminded of how much of a young STALLONE you truly are..."
mc "I will do my best. Again."
play sound "sounds/sexy09.mp3"
scene excellatease00 with fade
ex "I'm back... Follow me and let's see if you've got the BALLS for the job..."
scene excellatease01 with dissolve
ex "You remember that FINE BOOTY?"
mc "I sure do!"
scene excellatease02 with dissolve
ex "Then you know how to treat it well, don't you?"
mc "I'll treat it like royalty!"
scene excellatease03 with dissolve
ex "Is that so? Well, why don't you try and seduce ME then? Let's see if your supposed superpowers really work..."
scene excellatease04 with dissolve
ex "You see this nice pussy... It needs some tender loving."
mc "It sure looks like it does! I'll give it my best!"
scene excellatease05 with dissolve
mc "Let me delicately expose that nice muff of yours..."
scene excellatease06 with dissolve
ex "Get that tongue right in there..."
scene excellatease07 with dissolve
play sound "sounds/moan02.mp3"
ex "Mmh, si, just like that..."
scene excellatease08 with dissolve
play sound "sounds/moan04.ogg"
ex "Oooh!"
scene excellatease08b with dissolve
play sound "sounds/moan04.ogg"
ex "Oooh!"
mc "Now turn round, I'm not done toying with your horny snatch..."
scene excellatease09 with dissolve
play sound "sounds/moan02.mp3"
ex "You're... sticking a finger inside me!"
mc "That's right..."
scene excellatease10 with dissolve
play sound "sounds/moan05.mp3"
mc "And now half my fist!"
ex "AAAH!"
window hide
scene excellateaselick with fastdissolve
pause
ex "You're going to make me..."
scene excellatease11 with dissolve
play sound "sounds/splooge01.mp3"
ex "...CUM!!!!"
scene excellatease12 with dissolve
play sound "sounds/womancum02.mp3"
ex "AAAH!"
scene excellatease13 with dissolve
ex "You did well, I might consider a position for y..."
scene excellatease14 with dissolve
mc "Ain't done yet! Gonna make that pussy SQUIRM with pleasure with my Super-Dong!"
ex "Ooh, you're such a NAUGHTY Super-Hero!"
scene excellatease15 with dissolve
ex "I've met quite a few \"Italian Stallions\" in my time, but none anywhere near as BIG as you!"
mc "I'm only half-hard, Mrs Gionne. But I'll soon be ROCK-HARD to pound that sweet MILF pussy of yours!"
scene excellatease16 with dissolve
ex "Just as MASSIVE as I remember..."
scene excellatease17 with dissolve
mc "This is going to be a tight fit but a big girl like you should be able to take it without too much complaining..."
scene excellatease18 with dissolve
play sound "sounds/moan01.mp3"
ex "You're talking like someone who is in total control of the situation, bambino! This is making me so horny, just do it!"
play channel1 "sounds/womansex02.mp3"
$ excelladeskfuckslowx = False

label ExcellaDeskFuckSlowx:
$ excelladeskfuckfastx = False
$ excelladeskharderx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if excelladeskfuckslowx == False:
    if age >= 20:
        ex "Be careful with that huge weapon of yours, it might accidentally discharge inside me!"
    if age >= 18 and age <= 19:
        ex "Be careful with that huge teenage weapon of yours, it might accidentally discharge inside me!"
    $ excelladeskfuckslowx = True
window hide
show excelladeskfuckslowvideo behind excelladeskfuckfastvideo
show excelladeskfuckslowvideo behind excelladeskfuckslowpovvideo
show excelladeskfuckslowvideo behind excelladeskfuckharderslowvideo
pause 1.0
hide excelladeskfuckfastvideo
hide excelladeskfuckslowpovvideo
hide excelladeskfuckharderslowvideo
hide cum
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
call screen excelladeskfuckslowx()
screen excelladeskfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVSlowx")

label ExcellaDeskFuckFastx:
$ excelladeskharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if excelladeskfuckfastx == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ excelladeskfuckfastx = True
show excelladeskfuckfastvideo behind excelladeskfuckslowvideo
show excelladeskfuckfastvideo behind excelladeskfuckfastpovvideo
show excelladeskfuckfastvideo behind excelladeskfuckharderfastvideo
pause 1.0
hide excelladeskfuckslowvideo
hide excelladeskfuckfastpovvideo
hide excelladeskfuckharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen excelladeskfuckfastx()
screen excelladeskfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVFastx")

label ExcellaDeskFuckPOVSlowx:
$ excelladeskharderx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if excelladeskfuckslowx == False:
    if age >= 20:
        ex "Be careful with that huge weapon of yours, it might accidentally discharge inside me!"
    if age >= 18 and age <= 19:
        ex "Be careful with that huge teenage weapon of yours, it might accidentally discharge inside me!"
    $ excelladeskfuckslowx = True
show excelladeskfuckslowpovvideo behind excelladeskfuckslowvideo
show excelladeskfuckslowpovvideo behind excelladeskfuckfastpovvideo
show excelladeskfuckslowpovvideo behind excelladeskfuckharderpovslowvideo
pause 1.0
hide excelladeskfuckslowvideo
hide excelladeskfuckfastpovvideo
hide excelladeskfuckharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen excelladeskfuckslowpovx()
screen excelladeskfuckslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckSlowx")

label ExcellaDeskFuckPOVFastx:
$ excelladeskharderx = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if excelladeskfuckfastx == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ excelladeskfuckfastx = True
window hide
show excelladeskfuckfastpovvideo behind excelladeskfuckslowpovvideo
show excelladeskfuckfastpovvideo behind excelladeskfuckfastvideo
show excelladeskfuckfastpovvideo behind excelladeskfuckharderpovfastvideo
pause 1.0
hide excelladeskfuckslowpovvideo
hide excelladeskfuckfastvideo
hide excelladeskfuckharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen excelladeskfuckfastpovx()
screen excelladeskfuckfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckFastx")

label ExcellaDeskFuckHarderSlowx:
if excelladeskharderx == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharderx = True        
window hide
show excelladeskfuckharderslowvideo behind excelladeskfuckharderfastvideo
show excelladeskfuckharderslowvideo behind excelladeskfuckharderpovslowvideo
show excelladeskfuckharderslowvideo behind excelladeskfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderfastvideo
hide excelladeskfuckharderpovslowvideo
hide excelladeskfuckslowvideo
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
call screen excelladeskfuckharderslowx()
screen excelladeskfuckharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCum")

label ExcellaDeskFuckHarderFastx:
if excelladeskharderx == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharderx = True        
window hide
show excelladeskfuckharderfastvideo behind excelladeskfuckharderslowvideo
show excelladeskfuckharderfastvideo behind excelladeskfuckharderpovfastvideo
show excelladeskfuckharderfastvideo behind excelladeskfuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderslowvideo
hide excelladeskfuckharderpovfastvideo
hide excelladeskfuckfastvideo
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
call screen excelladeskfuckharderfastx()
screen excelladeskfuckharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCumx")

label ExcellaDeskFuckHarderPOVSlowx:
if excelladeskharderx == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharderx = True        
window hide
show excelladeskfuckharderpovslowvideo behind excelladeskfuckharderslowvideo
show excelladeskfuckharderpovslowvideo behind excelladeskfuckharderpovfastvideo
show excelladeskfuckharderpovslowvideo behind excelladeskfuckslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderslowvideo
hide excelladeskfuckharderpovfastvideo
hide excelladeskfuckslowpovvideo
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
call screen excelladeskfuckharderpovslowx()
screen excelladeskfuckharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCumx")

label ExcellaDeskFuckHarderPOVFastx:
if excelladeskharderx == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharderx = True        
window hide
show excelladeskfuckharderpovfastvideo behind excelladeskfuckharderpovslowvideo
show excelladeskfuckharderpovfastvideo behind excelladeskfuckharderfastvideo
show excelladeskfuckharderpovfastvideo behind excelladeskfuckfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderpovslowvideo
hide excelladeskfuckharderfastvideo
hide excelladeskfuckfastpovvideo
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
call screen excelladeskfuckharderpovfastx()
screen excelladeskfuckharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCumx")

label ExcellaDeskFuckCumx:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
ex "I want you to give me your young spunk! Can you do that for me, amico?"
mc "Ooh yeah I can, I certainly..."
scene excelladeskcum00 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "...CAAAAAAN!"
window hide
with fastflash
if age >= 20:
    ex "Oh my, you certainly are a true STALLONE!"
if age >= 13 and age <= 19:
    ex "Oh my, you certainly are a true TEENAGE STALLONE!"
if age <= 12:
    ex "Oh my, you certainly are a true PRETEEN STALLONE!"
scene excelladeskcum01 with dissolve
ex "STILL BLOWING! AAAH!"
window hide
with hpunch
ex "Ooh, look at that, it's already leaking from my pussy!"
scene excelladeskcum02 with dissolve
mc "Now DEEP INSIDE YOUR MAFIOSO FUCKHOLE! RHAAA!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
ex "AAAH!"
scene excelladeskcum03 with dissolve
ex "You're pumping too much seed into my poor pussy!"
window hide
with hpunch
mc "It's never too much spunk for a SEX Super-Hero! AAAH!"
window hide
with vpunch
ex "Please... PULL OUT!"
scene excelladeskcum04 with dissolve
stop channel1
mc "Alright, you asked for it, then you'll take my scum all over your chest and face, RHAAA!"
window hide
with fastflash
play sound "sounds/moan03.mp3"
ex "Oh God, you're going to PLASTER me with your [age]yo cream!"
scene excelladeskcum05 with dissolve
mc "Damn right I will! Take that!"
window hide
with vpunch
ex "Mamma Mia! So much young HOT SPUNK!"
scene excelladeskcum06 with dissolve
stop music
stop channel2
play sound "sounds/moan02.mp3"
ex "I'm definitely going to try and find some \"employment\" for you with the Famiglia..."
mc "I'll bear that in mind..."
jump ExcellaGallery

label ExcellaGallery03:
stop channel3
stop music

scene mafiareward01
ex "You want some more of my fine Italian ass, don't you [name]?"
mc "Well, you're in my harem now and I need to take care of my harem girls REGULARLY."
scene mafiareward02 with dissolve
ex "And I certainly have my NEEDS. And my ASS TOO."
mc "Then you found the right Harem Master. I service asses 24/7!"

scene mafiareward03:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan02.mp3"
ex "Mmmh, I know you do... You're such a young handsome STALLIONE..."
mc "Just show me that fine booty and I'll show you my SUPERHERO cock!"
scene mafiareward04:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
if age >= 20:
    ex "You MONSTER SUPERHERO cock? The one that will DESTROY my ass?"
if age >= 18 and age <= 19:
    ex "You MONSTER TEENAGE SUPERHERO cock? The one that will DESTROY my ass?"
play sound "sounds/moan04.ogg"
mc "That's right, Excella... Once it gets HARD from feeling that superb rump of yours..."
scene mafiareward05 with dissolve
mc "And to feel it, I need to remove that G-string..."
scene mafiareward06 with dissolve
play sound "sounds/moan02.mp3"
ex "OOOOH!"
scene mafiareward07 with dissolve
play sound "sounds/ripping.mp3"
mc "...FORCEFULLY!"
play sound "sounds/moan05.mp3"
ex "AAAH, you're such a BEAST!"
scene mafiareward08 with dissolve
play sound "sounds/slap.mp3"
ex "I can hear your giant horsedick SLAPPING against your hard pecs!"
play sound "sounds/boymoan.mp3"
mc "Fuck yeah, I'm sssooo HARD!"
scene mafiareward09 with dissolve
mc "Let me check that your ass is nice and wet for my ANAL-DESTROYER!"
play sound "sounds/moan02.mp3"
mc "Yeah, even more than last time. You're really looking forawrd toit, aren't you my little cock-slut?"
scene mafiareward10 with dissolve
ex "Last time, you totally DESTROYED me. My ass hurt so much..."
scene mafiareward11:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
mc "...Tsss... A harem girl shouldn't complain. It does not please her Harem Master. And I AM YOUR HAREM MASTER!"
ex "I'm sorry, Master. It's just that... you're so HUGE!"
ex "Oh God..."
scene mafiareward12 with dissolve
play sound "sounds/moan03.mp3"
mc "You can take it. You took it last time, remember?"
scene mafiareward13:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan06.ogg"
mc "And a few more inches..."
scene mafiaassprestart:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan05.mp3"
ex "I can't believe it fits!"
scene mafiaassstart with dissolve
if age >= 20:
    mc "It totaly does, that ass of yours is THICK! A perfect match for my FAT FUCKSTICK!"
if age >= 18 and age <= 19:
    mc "It totaly does, that ass of yours is THICK! A perfect match for my FAT TEENAGE FUCKSTICK!"
window hide

$ mafiaasssoftx = True
$ mafiaassharderx = False

label MafiaAssSlowx:
$ mafiaassfastx = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if mafiaasssoftx == False:
    ex "Calm down STALLONE! I want it nice and slow please..."
    show mafiaassstart behind mafiaassharderfastvideo
    show mafiaassstart behind mafiaassharderslowvideo
    show mafiaassstart behind mafiaassharderpovfastvideo
    show mafiaassstart behind mafiaassharderpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide mafiaassharderfastvideo
    hide mafiaassharderslowvideo
    hide mafiaassharderpovslowvideo
    hide mafiaassharderpovfastvideo
    hide mafiaasstransition
    with dissolve
    mc "Alright, I'll show you I can be a GENTLE Harem Master... sometimes."
    $ mafiaasssoftx = True        
    $ mafiaassharderx = False        
window hide
show mafiaassslowvideo behind mafiaassfastvideo
show mafiaassslowvideo behind mafiaasspovslowvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassfastvideo
hide mafiaasspovslowvideo
with dissolve
play channel2 "sounds/womansex02.mp3"
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassslowx()
screen mafiaassslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssPOVSlowx")

label MafiaAssFastx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if mafiaassfastx == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ mafiaassfastx = True
show mafiaassfastvideo behind mafiaassslowvideo
show mafiaassfastvideo behind mafiaasspovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassslowvideo
hide mafiaasspovfastvideo
with dissolve
play channel2 "sounds/womansex03.mp3"
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassfastx()
screen mafiaassfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssPOVFastx")

label MafiaAssPOVSlowx:
play channel2 "sounds/womansex02.mp3"
$ mafiaassfastx = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
show mafiaasspovslowvideo behind mafiaassslowvideo
show mafiaasspovslowvideo behind mafiaasspovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassslowvideo
hide mafiaasspovfastvideo
with dissolve
play channel2 "sounds/womansex02.mp3"
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassslowpovx()
screen mafiaassslowpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssSlowx")

label MafiaAssPOVFastx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if mafiaassfastx == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ mafiaassfastx = True
window hide
show mafiaasspovfastvideo behind mafiaasspovslowvideo
show mafiaasspovfastvideo behind mafiaassfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaasspovslowvideo
hide mafiaassfastvideo
with dissolve
play channel2 "sounds/womansex03.mp3"
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassfastpovx()
screen mafiaassfastpovx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssFastx")

label MafiaAssHarderSlowx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if mafiaassharderx == False:
    ex "STALLONE! Give it to me REALLY HARD!"
    show mafiaasstransition behind mafiaassfastvideo
    show mafiaasstransition behind mafiaassslowvideo
    show mafiaasstransition behind mafiaasspovslowvideo
    show mafiaasstransition behind mafiaasspovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide mafiaassslowvideo
    hide mafiaassfastvideo
    hide mafiaasspovslowvideo
    hide mafiaasspovfastvideo
    hide mafiaassstart    
    with dissolve
    mc "Alright, you asked for it!"
    $ mafiaassharderx = True
    $ mafiaasssoftx = False
window hide
show mafiaassharderslowvideo behind mafiaassharderfastvideo
show mafiaassharderslowvideo behind mafiaassharderpovslowvideo
$ renpy.pause(0.5, hard=True)
stop channel2
play channel2 "v031/womansex08.mp3"
hide mafiaassharderfastvideo
hide mafiaassharderpovslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassharderslowx()
screen mafiaassharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCumx")

label MafiaAssHarderFastx:     
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderfastvideo behind mafiaassharderslowvideo
show mafiaassharderfastvideo behind mafiaassharderpovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderslowvideo
hide mafiaassharderpovfastvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassharderfastx()
screen mafiaassharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCumx")

label MafiaAssHarderPOVSlowx:      
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderpovslowvideo behind mafiaassharderslowvideo
show mafiaassharderpovslowvideo behind mafiaassharderpovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderslowvideo
hide mafiaassharderpovfastvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassharderpovslowx()
screen mafiaassharderpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCumx")

label MafiaAssHarderPOVFastx:    
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderpovfastvideo behind mafiaassharderpovslowvideo
show mafiaassharderpovfastvideo behind mafiaassharderfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderpovslowvideo
hide mafiaassharderfastvideo
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
call screen mafiaassharderpovfastx()
screen mafiaassharderpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCumx")

label MafiaAssCumx:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
ex "Are you going to BLAST THAT LOAD for me, bambino?"
mc "Mamma Mia, si, SI..."
stop channel2
play channel2 "v031/boyorgasm02.mp3"
scene mafiahardcum01 with dissolve
mc "...SI!!!!! AAAH!"
window hide
with vpunch
play sound "sounds/moan05.mp3"
ex "OOOH!"
scene mafiahardcum02 with dissolve
mc "RHAAAAAA!!!!"
window hide
with fastflash
play sound "sounds/splooge01.mp3"
ex "AAAH! SO DEEP!!!"
scene mafiahardcum03:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "Take THAT right up your backside!"
play sound "sounds/splooge01.mp3"
window hide
with fastflash
ex "SO MCUH YOUNG CUM!"
scene mafiahardcum04:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "And THAT!!!!"
play sound "sounds/splooge02.mp3"
window hide 
with hpunch
ex "Santissima Madonna!!!!"
scene mafiahardcum05:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
mc "Damn, I'm cumming so hard, your ass can't take all of it!"
window hide
with fastflash
ex "No ass can hold a load that HUGE!"
scene mafiahardcum06 with dissolve
stop channel2
mc "Well, I had hoped your fat booty would."
ex "Now I have MASSIVE streamers of young spunk all over my back. My hubby is totally cucked..."
scene mafiahardcum07 with dissolve
stop music
stop channel1
play sound "sounds/panting.mp3"
mc "And I think my job as Harem Master is done here."
play sound "sounds/moan03.mp3"
ex "And a job well done it is..."
jump ExcellaGallery
