label DaniGallery:
stop channel3
play channel3 "sounds/policemusic.mp3"
scene danibackground
show danimaingallery at gallerypos01 with moveinleft
call screen gallerydani()
screen gallerydani():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Sergeant Dani{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerydani"), Jump ("MainGallery05")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerydani"), Jump ("DaniGalleryAnim")]
    
    if renpy.seen_image("luthorcase20"):
        imagebutton:
            focus_mask True
            idle "gallery/luthorgallery01.png" xpos 400 ypos 100
            hover "gallery/luthorgallery01.png"
            action Jump ("DaniGallery01")
    text "{font=Gui/Heroes Legend.ttf}Sexiest Prisoner{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("luthorcase20") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("DaniGallery")

    if renpy.seen_image("danishoot05"):
        imagebutton:
            focus_mask True
            idle "gallery/danigallery02.png" xpos 750 ypos 100
            hover "gallery/danigallery02.png"
            action Jump ("DaniGallery02")
    text "{font=Gui/Heroes Legend.ttf}Photoshoot{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("danishoot05") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("DaniGallery")

    if renpy.seen_image("danistrip03"):
        imagebutton:
            focus_mask True
            idle "gallery/danigallery03.png" xpos 1100 ypos 100
            hover "gallery/danigallery03.png"
            action Jump ("DaniGallery03")
    text "{font=Gui/Heroes Legend.ttf}Strip and BJ{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("danistrip03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("DaniGallery")

label DaniGalleryAnim:
stop sound
stop channel3
play channel3 "sounds/sexy14.mp3"
call screen screenanimdani()
screen screenanimdani():
    modal True
    add "gallery/danibackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "danianimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "danianimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimdani"), SetVariable ("animcount", 1), Jump ("DaniGallery")]
    text "{font=Gui/Heroes Legend.ttf} Sergeant Dani{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 26{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft9{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}36DD-24-38{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Male Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Hypno-Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/danianim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimdani")]
    add "gallery/danianim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimdani")]

label DaniGallery01:
$ danistudlinessxx = False
stop channel3
scene luthorcase04 with dissolve
mc "Ah, there she is. Cockham's most notorious Super-Villain. A criminal mastermind of the worst kind. Been caught again by Superman, Sexy Luthor?"
lu "A small hiccup, nothing to worry about. But I see the League doesn't trust the CCPD anymore. How times have changed..."
da "Just some EXTRA security to make sure you won't escape this time, Sexy Luthor!"
scene luthorcase05 with dissolve
lu "What does [hero] here think about this lousy assignment? He should be on the streets fighting sex crime, should he not?"
mc "Err..."
lu "The sooner I escape, the sooner you'll be able to go back to your proper superhero duties, [hero]..."
mc "Don't try and..."
da "Don't listen to her. It's dinner time anyway, I'll bring her her food, that should shut her up."
mc "Alright, I'll stay here to make sure nothing happens."
scene luthorcase06 with dissolve
mc "Ooh, pizza? Can I get some?"
scene luthorcase07 with dissolve
da "Dinner is served. I'll remove your handcuffs but don't turn around until I've left the cell."
lu "My pizza might get cold..."
scene luthorcase08 with dissolve
mc "I think you should hurry up, Sergeant, she's standing up..."
da "What, but I told her to..."
mc "Quick, let me get the door for you!"
scene luthorcase09:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
play sound "sounds/radiation02.mp3"
lu "Dani, why don't you share that lovely pizza with me?..."
da "What? Oh, thanks for offering, I'm starving!"
mc "It's a ruse, GET OUT OF THERE RIGHT NOW!"
scene luthorcase10 with dissolve
stop sound
lu "I think we would be more comfortable WITHOUT clothes, don't you agree, Dani?"
da "Y...Yes, I agree. Let me take my skirt off. And my shirt."
mc "Uh oh, full lesbian seduction ahead..."
stop music
play music "sounds/sexy04.mp3"
scene luthorcase11 with dissolve
lu "Now, Dani. I have something that I would like you to taste for me... Something much TASTIER than that pizza..."
da "What is it?"
lu "MY PUSSY!"
scene luthorcase12 with dissolve
lu "Enjoying the show, [hero]? Why don't you join us?"
mc "I'm not falling for your tricks, Sexy Luthor!"
lu "Too bad, your loss... Dani here is going to really ENJOY herself, I can guarantee that!"
scene luthorcase13 with dissolve
lu "You'll see, Dani, it's the tastiest pussy in town!"
mc "Damn, what should I do? Except watch obviously... And think later."
play channel1 "sounds/lick01.ogg"
play channel2 "sounds/moan02.mp3"
scene luthorlickcasevideo with dissolve
pause
mc "Make her cum with your tongue, Dani! She might get tired..."
pause
scene luthorcasepostlick01 with dissolve
lu "Right there, just right... th..."
scene luthorcasepostlick02 with dissolve
stop channel1
play sound "sounds/splooge02.mp3"
lu "AAAH, I'm CUMMING!"
window hide
with fastflash
mc "Great, you did it, Dani!"
scene luthorcasepostlick03 with dissolve
stop channel2
play sound "sounds/womancum01.mp3"
lu "UUUUUHH!!!!"
window hide
with fastflash
mc "You've had your fun, now let her go, Sexy Luthor! Plus, your pizza is getting cold. And it does look yummy."
scene luthorcase14 with dissolve
stop sound
lu "Oh, I'm FAR from done, [hero]... You can't stop me, I'm going to FUCK HER TO DEATH!"
mc "I can't let you do that!"
lu "Oh well, I guess you'll just have to enter my cell and try and stop me then..."
mc "Damn you, Sexy Luthor, DAMN YOUR EVIL GENIUS!"
scene luthorcase15 with dissolve
play sound "sounds/moan02.mp3"
lu "Oh yeah, keep going, lick my cunt until you PASS OUT!"
scene luthorcase16 with dissolve
mc "That's it, I have to intervene or poor Sergeant Dani will turn into a pussy-licking zombie!"
scene luthorcase17 with dissolve
play sound "sounds/radiation02.mp3"
lu "Why don't you join us, [hero]? I'm sure you want some of THAT pussy too, don't you?"
mc "Y...Yes, YES I WANT THAT SEXY PUSSY!"
stop sound
scene luthorcase18 with dissolve
lu "Then get your cock HARD, I want to see if the rumors are true..." 
scene luthorcase19 with dissolve
if age >= 20:
    lu "I don't need you anymore, Dani, let me handle that MONSTERCOCK on my own... For STARTERS!"
if age == 18 or age == 19:
    lu "I don't need you anymore, Dani, let me handle that teenage MONSTERCOCK on my own... For STARTERS!"
scene luthorcase20 with dissolve
lu "Are you ready to handle MY PUSSY, [hero]?"
mc "Of course, Sexy Luthor, anything for YOU!"
lu "Then get on your knees and show me how you worship it."
scene luthorcase21 with dissolve
play sound "sounds/lick01.ogg"
lu "That's nice... You're a natural, despite your age... Let's see how expert your giant cock is now!"
scene luthorcase22 with dissolve
lu "Damn boy, I've never felt such a heavy piece of equipment..."
scene luthorcase23 with dissolve
play sound "sounds/womangroan.mp3"
lu "But Sexy Luthor is up to the challenge! I'm going to FUCK this dong into OBLIVION!"
play channel1 "sounds/womansex02.mp3"
window hide

label LuthorCaseFuckxx:
hide cum
hide nexticon
hide zoomicon
show luthorfuckcasevideo behind luthorfuckcasepussyvideo
$ renpy.pause(1.0, hard='True')
hide luthorfuckcasepussyvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show zoomicon:
     xpos 50 ypos 500     
call screen luthorfuck01xx()
screen luthorfuck01xx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuckPussyxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEndxx")

label LuthorCaseFuckPussyxx:
hide cum
hide nexticon
hide zoomicon
show luthorfuckcasepussyvideo behind luthorfuckcasevideo
$ renpy.pause(1.0, hard='True')
hide luthorfuckcasevideo with dissolve
lu "Yeah, WORK that pussy!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 1700 ypos 500     
call screen luthorfuck02xx()
screen luthorfuck02xx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuckxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEndxx")

label LuthorCaseFuckEndxx:
hide sceneicon
hide nexticon
hide zoomicon
lu "* puff * Still going, stud? But I can feel that you're getting close, aren't you?"
window hide
pause
mc "Uuuh, your sexy pussy is gripping me so tight..."
lu "I'm gonna PUMP you DRY!"
scene luthorcasefuckcum01 with dissolve
hide luthorfuckcasevideo
hide luthorfuckcasepussyvideo
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "And I'm gonna pump you FULL! RHAAA!"
window hide
with fastflash
lu "A challenge, boy?"
scene luthorcasefuckcum02 with dissolve
stop channel1
play sound "sounds/thud.mp3"
lu "Here, challenge THAT!"
window hide
with fastflash
play channel1 "sounds/splooge02.mp3"
mc "Oh FUCK, AAAH!"
scene luthorcasefuckcum03 with dissolve
stop sound
play sound "sounds/boymoan02.mp3"
lu "You're BLOATING my insides with your MASSIVE pellets of young cum!"
window hide
with fastflash
mc "I cum a lot... I'm a SEX SUPERHERO!"
stop channel1
scene luthorcasefuckcum04 with dissolve
lu "I can't believe you're STILL spewing such FAT WADS!"
window hide
with fastflash
mc "Your sexy pussy is making cum non-stop, AAH!"
scene luthorcase25 with dissolve
stop sound
stop channel1
play sound "sounds/panting.mp3"
lu "Finally... You are true to your reputation, [hero]. What a cock... And it looks like it's still raring to go?"
mc "Yeah, SEXY PUSSY. NEED MORE SEXY PUSSY!"
lu "Well, I would love to hang around and have some fun all together, but I need to go... But why don't you two stay behind and get to know each other better?"
da "Uuh, his cock is sssooo BIG!"
lu "That's right, his cock is enormous, you want it, don't you? [hero], come and pick her up and show her what a STUD you are! While I get dressed..."
scene luthorcase26 with dissolve
lu "That's good, [hero], I'm sure you'll have a GOOD time with her. Fucking her up her tight ass!"
scene luthorcase27 with dissolve
da "Up my ass? But... His cock is too big for that!"
lu "Don't worry Dani, YOU will enjoy it too!"
scene luthorcase28 with dissolve
lu "Make her nice and wet [hero], she's going to need it..."
play sound "sounds/moan02.mp3"
scene luthorcase29 with dissolve
play sound "sounds/radiation02.mp3"
lu "And now I'll make sure that you'll be so taken by your lovemaking that you won't bother raising the alarm for a while..."
stop sound
lu "I think I'll take the key with me, just in case... Cheerio!"
scene luthorcase30 with dissolve
play sound "sounds/moan01.mp3"
da "Please fuck me in the ass, I NEED that HUGE COCK IN ME!"
mc "Alright, I'm going to POUND you against the cell wall!"
window hide
play channel1 "sounds/danimassive.mp3"
show luthordanianalslowvideo with dissolve
da "Your cock is so MASSIVE! It's the BIGGEST bulldick I ever had!"
window hide
pause
da "What's going on? Hey, stop fucking me, she's gone and her Super-Seduction powers aren't active anymore!"
window hide
menu:
    "Keep going (use Super-Studliness, +1 Super-Villain)":
        mc "No way, I'm enjoying myself too much! And I'll make YOU enjoy yourself too!"
        $ danistudlinessxx = True    
        if age >= 20:
            da "This young monster dong is so GOOD! Please fuck me senseless, fuck me till I cream all over your giant cunt-splitter!"
        if age >= 18 and age <= 19:
            da "This monster teenage dong is so GOOD! Please fuck me senseless, fuck me till I cream all over your giant cunt-splitter!"
        mc "Get ready for some HEAVY POUNDING, Dani!"   
        jump DaniAnalFastFuckx      
    "Stop fucking her (no change)":
        mc "Damn, I was just about to blow..."
        da "Since she locked us out, cum quick inside my ass, I have a key double hidden in there!"
        mc "Alright!"
        jump DaniAnalSlowFuckx
        
label DaniAnalSlowFuckxx:
window hide
hide cum
hide faster
hide slower
play channel1 "sounds/danimassive.mp3"
show luthordanianalslowvideo behind luthordanianalfastvideo
$ renpy.pause(1.0, hard='True')
hide luthordanianalfastvideo with dissolve
pause
if danistudlinessxx:
    da "Your cock is so HUGE! It's the BIGGEST bulldick I ever had!"
if danistudlinessxx == False:
    da "Hurry up [name], we need to get that key!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen luthordanianalslowxx()
screen luthordanianalslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalFastFuckxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEndxx")

label DaniAnalFastFuckxx:
window hide
hide cum
hide faster
hide slower
play channel1 "sounds/danimassive.mp3"
show luthordanianalfastvideo behind luthordanianalslowvideo
$ renpy.pause(1.0, hard='True')
hide luthordanianalslowvideo with dissolve
pause
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
if danistudlinessxx:
    da "Oh my God, you're going so DEEP!"
if danistudlinessxx == False:
    da "Why are you fucking me so HARD? Just blow your load already!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
call screen luthordanianalfastxx()
screen luthordanianalfastxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalSlowFuckxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEndxx")

label DaniAnalFuckEndxx:
hide slower
hide cum
hide faster
if danistudlinessxx:
    da "You're making me CUM NON-STOP!"
    mc "I'm about to bust my nut too..."
if danistudlinessxx == False:
    da "Are you finally going to cum? Please do it quickly!"
scene danianalcum01 with dissolve
hide luthordanianalslowvideo
hide luthordanianalfastvideo
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
if danistudlinessxx:
    da "I'm gonna CREAM all over that gigantic discharging DONG!"
if danistudlinessxx == False:
    da "Try and come a LOT!"
window hide
with fastflash
if danistudlinessxx:
    mc "Get ready for more of MY cream too!"
if danistudlinessxx == False:
    mc "I AM, RHAAA!"
scene danianalcum02 with dissolve
da "More, MORE CUM!"
window hide
with fastflash
mc "You want some more, here's some MORE, AAAH!"
scene danianalcum03 with dissolve
stop channel1
play sound "sounds/moan03.mp3"
da "I'm just leaking your slimy scum out of my battered butthole... Uuuh..."
mc "Yeah, sorry about that, got carried away a bit. After all, I'm a Super-Hero."
stop music
stop channel2
stop channel1 
jump DaniGallery

label DaniGallery02:
stop channel3
scene danipreshoot01
lp "Since you work in liaison with the CCPD, you two must have met before, right?"
mc "Err, vaguely, I might have seen her around at one stage but..."
scene danipreshoot02 with dissolve
if mission02win:
    da "We did a MISSION together. Which ended in almost complete success thanks to my quick thinking."
if mission02fail:
    da "We did a MISSION together. Which ended in complete disaster."
lp "Really? You'll have to tell me MORE about this mission of yours. After the photoshoot."
scene danipreshoot03 with dissolve
lp "So let's get started, Sergeant Dani, just be natural, I'll take the photos and make sure I take them from the BEST angles... And take the props I prepared for you."
play music "sounds/sexy13.mp3"
scene danishoot01 with dissolve
da "Like this?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Perfect! Keep going."
scene danishoot02 with dissolve
lp "Turn around and keep holding your baton."
window hide
with fastflash
play sound "sounds/flash.mp3"
mc "This is getting steamy..."
scene danishoot03 with dissolve
lp "That's it, look like you're about to arrest a dangerous criminal."
scene danishoot04:
    subpixel True
    xpos 0.0 ypos 0.0
    ease 6.0 ypos -1.3 xpos 0.0
with dissolve
$ renpy.pause(2.0, hard='True')
pause
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "You might as well take your skirt off."
scene danishoot05 with dissolve
mc "Damn, I'd like to get arrested RIGHT NOW!"
scene danishoot06 with dissolve
lp "Can you lift up your blouse? This calendar is for the Hustler Supplement of our weekend edition, the readers want to see some FLESH."
scene danishoot07 with dissolve
mc "Mamma Mia!"
window hide
with fastflash
play sound "sounds/flash.mp3"
da "I have an idea of what to do with my baton."
scene danishoot08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
lp "I like your improvisation style Sergeant Dani!"
scene danishoot09 with dissolve
mc "So do I..."
scene danishoot10 with dissolve
da "This is making me quite horny actually..."
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Then take off your panties and play with your pussy, Sergeant Dani."
scene danishoot11 with dissolve
lp "That's perfect, nicely trimmed and very APPETIZING!"
scene danishoot12 with dissolve
play sound "sounds/moan02.mp3"
da "Uh..."
scene danishoot13 with dissolve
mc "Can I make a suggestion? Stick your fing..."
scene danishoot14 with dissolve
play sound "sounds/moan05.mp3"
window hide
with fastflash
play sound "sounds/flash.mp3"
mc "Ah, okay, you didn't need my suggestion."
scene danishoot13 with fastdissolve
play sound "sounds/moan03.mp3"
$ renpy.pause(0.5, hard='True')
scene danishoot14 with fastdissolve
play sound "sounds/moan05.mp3"
$ renpy.pause(0.5, hard='True')
da "Aaaah..."
scene danishoot15 with dissolve
stop sound
da "I almost came..."
scene danishoot16 with dissolve
da "Maybe with the help of my baton..."
scene danishoot17 with dissolve
mc "Or MY baton perhaps?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Please [hero], this is meant to be a solo shoot only."
scene danishoot18 with dissolve
play sound "sounds/moan04.ogg"
da "Mmmh... Oooh..."
show daniwankslowvideo with dissolve
play channel1 "sounds/moan02.mp3"
show faster:
    xpos 1700 ypos 500    
call screen daniwankslowx()
screen daniwankslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniWankFastx")

label DaniWankFastx:
hide faster
show daniwankfastvideo behind daniwankslowvideo
lp "Frig yourself off, I want to see some pussy juices squirting eveywhere!"
$ renpy.pause(2.0, hard='True')
hide daniwankslowvideo
with fastdissolve
show nexticon:
    xpos 1750 ypos 1020    
call screen daniwankfastx()
screen daniwankfastx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(180, 60)        
        action Jump ("DaniWankEndx")

label DaniWankEndx:
hide nexticon
scene danishoot20 with dissolve
stop channel1
play sound "sounds/womancum02.mp3"
da "AHHH, I'm coming!!!"
scene danishoot21 with dissolve
play sound "sounds/moan06.ogg"
mc "Damn, she's squirting big time!"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "That's the centerfold pic right there!"
scene danishoot22 with dissolve
play sound "sounds/moan04.ogg"
mc "Do I get a free copy of that issue?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "No, you'll have to pay for it, like everyone else."         
scene danishoot23 with dissolve
mc "That's not fair, I don't have any money."
play sound "sounds/lick01.ogg"
lp "That's a wrap, thank you Sergeant Dani."                           
stop music
scene danipostshoot01 with dissolve
stop sound
lp "Well, I need to interrogate, I mean interview Sergeant Dani now about this \"mission\" you did together, so if you'll excuse us..."
mc "What? I get to leave the gallery?"
scene danipostshoot02 with dissolve
lp "Yes, we wouldn't want Clark Kunt barging in on us right now, would we?"
mc "Err, yeah, I get your point..."
stop music
stop channel1
stop channel2
jump DaniGallery

label DaniGallery03:
stop channel3
scene danistrip01 with dissolve
mc "* The room is packed. I hope she makes a good impression... *"
play sound "v061/applause.mp3"
scene danistrip02:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "* Well, she got some applause at least. Must be the big tits. *"
scene danistrip03 with dissolve
mc "* Nice. She's really taking this seriously. *"
scene danistrip04 with dissolve
mc "* I wonder if I'll get any applause... *"
scene danistrip05 with dissolve
mc "* Stripping is so stressful. *"
scene danistrip06 with dissolve
mc "* But she's such a natural... *"
scene danistrip07:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
"(guest) Show us some MOAR!"
"(other guest) YES, SHOW US YER PUSSY!"
scene danistrip08 with dissolve
mc "* I thought this was a high-class joint, but I see they still let the riffraff in! *"
scene danistrip09:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "* Ooh, I think she's doing what they asked for. Not that I can see anything, since I'm behind the curtain.*"
scene danistrip10 with dissolve
mc "* She's really giving them quite a show! *"
scene danistrip11 with dissolve
mc "* ...And putting the pressure on me... *"
scene danistrip12 with dissolve
"(guest) YEAH! WOO-HOO!"
scene danistrip13:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan01.mp3"
mc "* Now she's even playing with her pussy. *"
scene danistrip14 with dissolve
"(guest) Great pussy and nice tits!"
play sound "v061/applause.mp3"
scene danistrip15:
    zoom 1.0 xoffset -80 yoffset 0    
show danistrip15 at powerpoolfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
mc "* Ah, it looks like it's going to be my turn soon. *"
scene backstage07 with dissolve
ta "Your turn. Get on the stage and make sure to display that boymeat of yours for the ladies!"
mc "I feel just so cheap..."
ta "You ARE cheap. You work for free, remember?"
stop music
play music "sounds/sexy11.mp3" volume 0.5
scene mcstrip01 with dissolve
mc "* Now I'm super-stressed... *"
scene mcstrip02 with dissolve
mc "* Hope they don't laugh at my routine... *"
scene mcstrip03 with dissolve
mc "* Smile for the ladies... *"
scene mcstrip04 with dissolve
mc "* And now the helicopter cock... *"
window hide
scene mcstrip05 with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip06a with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip06b with dissolve
$ renpy.pause(.5, hard='True')
scene mcstrip03 with dissolve
play sound "sounds/wow.mp3"
mc "* Someone likes it at least... *"
show helicock
pause
play sound "v061/applause.mp3"
mc "* I got my first applause... *"
scene mcstrip07 with dissolve
mc "* Now I need to concentrate for my next acrobatic move... *"
scene mcstrip08:
    subpixel True
    xpos 0.0
    linear 5.0 xpos -0.1
with dissolve
mc "* Come on, I can do it... *"

scene mcstrip09 with dissolve
play sound "v061/applause.mp3"
mc "* I'm getting some more applause! *"
scene mcstrip10 with dissolve
"(female guest) GET THAT THING HARD FOR US!"
scene mcstrip11 with dissolve
mc "* Jesus... These people feel so entitled... I guess they're high-society. Or freeloading pirates on f95zone. *"
scene mcstrip12:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
play sound "sounds/audiencegasp.mp3"
mc "* Yeah, that shut them up alright! *"
scene mcstrip13 with dissolve
mc "* Check this mammoth rock-hard boymeat, you filthy perverts! *"
scene mcstrip14:
    subpixel True
    zoom 1
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05    
with dissolve
play sound "sounds/boymoan.mp3"
mc "* Yeah... Fondling my balls and twisting my nipple... *"
stop music
play music "sounds/sexy14.mp3" volume 0.5
scene mcstrip15 with dissolve
mc "Sergeant Dani??? What are you doing?"
da "They want us to put on a show, so we'd better do as we're told, I don't want to blow my cover..."
scene mcstrip16 with dissolve
da "So I'll blow YOU instead! Just play along..."
mc "ALRIGHT!"
scene mcstrip17 with dissolve
play sound "sounds/slurp.mp3"
if age >= 20:
    da "It looks like it's getting you very EXCITED to know that I'm about to suck on your giant dong in front of all these people..."
if age >= 18 and age <= 19:
    da "It looks like it's getting you very EXCITED to know that I'm about to suck on your giant teenage dong in front of all these people..."
mc "Ohhh.... Fuck..."
scene mcstrip18 with dissolve
mc "AAAH..."
play channel1 "sounds/blow01.mp3"
$ daniblowslowx = False

label DaniBlowSlowx:
$ daniblowfastx = False
window hide
show daniblowslowvideo behind daniblowfastvideo
show daniblowslowvideo behind daniblowsceneslowvideo
pause 1.0
hide daniblowfastvideo
hide daniblowsceneslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowslowx == False:
    $ daniblowslowx = True
    mc "Yeah, gobble this cock for the audience, they like it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowslowx()
screen daniblowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowPOVSlowx")

label DaniBlowFastx:
$ daniblowslowx = False
window hide
show daniblowfastvideo behind daniblowslowvideo
show daniblowfastvideo behind daniblowscenefastvideo
pause 1.0
hide daniblowscenefastvideo
hide daniblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowfastx == False:
    $ daniblowfastx = True    
    mc "You want to go a bit faster, hey, Yeah, that's right, we need to put on a SHOW tonight!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowfastx()
screen daniblowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowPOVFastx")

label DaniBlowPOVSlowx:
$ daniblowfastx = False
window hide
show daniblowsceneslowvideo behind daniblowslowvideo
show daniblowsceneslowvideo behind daniblowscenefastvideo
pause 1.0
hide daniblowscenefastvideo
hide daniblowslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowslowx == False:
    $ daniblowslowx = True
    mc "Yeah, gobble this cock for the audience, they like it..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowscenefuckslowx()
screen daniblowscenefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowSlowx")

label DaniBlowPOVFastx:
$ daniblowslowx = False
window hide
show daniblowscenefastvideo behind daniblowfastvideo
show daniblowscenefastvideo behind daniblowsceneslowvideo
pause 1.0
hide daniblowfastvideo
hide daniblowsceneslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if daniblowfastx == False:
    $ daniblowfastx = True    
    mc "You want to go a bit faster, hey, Yeah, that's right, we need to put on a SHOW tonight!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowscenefuckfastx()
screen daniblowscenefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowFastx")

label DaniBlowEndx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Fuck yeah... Now hold it still..."
scene mcstrip19 with dissolve
play sound "sounds/blow02.mp3"
mc "Hold it..."
scene mcstrip20 with dissolve
play sound "v032/blow03.mp3"
mc "Let me help you get my shaft DEEPER down your hungry throat..."
scene mcstrip21 with dissolve
mc "Yeah, that's nice... Now keep going on your own, you can do it..."
play channel1 "sounds/blow02.mp3"
$ daniblowharderslowx = False

label DaniBlowHarderSlowx:
$ daniblowharderfastx = False
window hide
show daniblowharderslowvideo behind daniblowharderfastvideo
show daniblowharderslowvideo behind daniblowharderpovslowvideo
pause 1.0
hide daniblowharderfastvideo
hide daniblowharderpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderslowx == False:
    $ daniblowharderslowx = True
    mc "Oh God, I don't know where my cock is going, but it's going somewhere NICE and WARM!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowharderslowx()
screen daniblowharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCumx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderPOVSlowx")

label DaniBlowHarderFastx:
$ daniblowharderslowx = False
window hide
show daniblowharderfastvideo behind daniblowharderslowvideo
show daniblowharderfastvideo behind daniblowharderpovfastvideo
pause 1.0
hide daniblowharderpovfastvideo
hide daniblowharderslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderfastx == False:
    $ daniblowharderfastx = True    
    mc "Look at all those perverts watching us... It's making me so fucking HARD!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen daniblowharderfastx()
screen daniblowharderfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCumx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderPOVFastx")

label DaniBlowHarderPOVSlowx:
$ daniblowharderfastx = False
window hide
show daniblowharderpovslowvideo behind daniblowharderslowvideo
show daniblowharderpovslowvideo behind daniblowharderpovfastvideo
pause 1.0
hide daniblowharderpovfastvideo
hide daniblowharderslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if daniblowharderslowx == False:
    $ daniblowharderslowx = True
    mc "Oh God, I don't know where my cock is going, but it's going somewhere NICE and WARM!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowharderpovfuckslowx()
screen daniblowharderpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCumx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderSlowx")

label DaniBlowHarderPOVFastx:
$ daniblowharderslowx = False
window hide
show daniblowharderpovfastvideo behind daniblowharderfastvideo
show daniblowharderpovfastvideo behind daniblowharderpovslowvideo
pause 1.0
hide daniblowharderfastvideo
hide daniblowharderpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if daniblowharderfastx == False:
    $ daniblowharderfastx = True    
    mc "Look at all those perverts watching us... It's making me so fucking HARD!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen daniblowharderpovfuckfastx()
screen daniblowharderpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniBlowHarderPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniBlowHarderCumx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("DaniBlowHarderFastx")

label DaniBlowHarderCumx:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Oh fuck, I'm gonna blow..."
play sound "sounds/splooge02.mp3"
scene mcstripcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "Ohhhh!"
window hide
with hpunch
mc "COMING!!!!"
scene mcstripcum02 with dissolve
da "Mmmgggbb...."
window hide
with fastflash
mc "SO GOOD, AAAH!"
scene mcstripcum03 with dissolve
mc "Keep swallowing that boyload, I have more for you, RHAAA!"
window hide
with hpunch
mc "Goddam... UUUH!"
scene mcstripcum04:
    zoom 0.5
with dissolve
show mcstripcum04:
    subpixel True
    linear 8.0 zoom 1.0 xpos -0.5 ypos -0.5
play sound "sounds/splooge03.mp3"
if age >= 20:
    da "Looks like your erupting MEGA-DONG needed some fresh air! Look at that MONSTER SHOT!!!"
if age >= 18 and age <= 19:
    da "Looks like your erupting teen MEGA-DONG needed some fresh air! Look at that MONSTER SHOT!!!"
window hide
with fastflash
mc "AAAH! Oh God!!!"
scene mcstripcum05 with dissolve
play sound "sounds/moan02.mp3"
da "Keep going, cover me in your red-hot ball-batter!!!!"
window hide
with fastflash
mc "That's... AAAAH..."
window hide
with fastflash
mc ".... The last of it... Phew..."
stop channel1
scene mcstripcum06 with dissolve
play sound "sounds/lick02.mp3"
da "There's so much warm cum... We really gave them quite a show..."
mc "And yet, they didn't even give us a tip. Ungrateful high-society pirates..."
stop music
stop channel2
jump DaniGallery
