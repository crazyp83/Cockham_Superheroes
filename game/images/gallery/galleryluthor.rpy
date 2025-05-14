label LuthorGallery:
stop channel3
play channel3 "sounds/underworld.mp3"
scene luthorbackground
show luthormaingallery at gallerypos01 with moveinleft
call screen galleryluthor()
screen galleryluthor():
    text "{font=Gui/Heroes Legend.ttf}Naughty Sexy Luthor{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryluthor"), Jump ("MainGallery02")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryluthor"), Jump ("LuthorGalleryAnim")]
    
    if renpy.seen_image("luthorcase20"):
        imagebutton:
            focus_mask True
            idle "gallery/luthorgallery01.png" xpos 400 ypos 100
            hover "gallery/luthorgallery01.png"
            action Jump ("LuthorGallery01")
    text "{font=Gui/Heroes Legend.ttf}Sexiest Prisoner{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("luthorcase20") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("LuthorGallery01hint")

label LuthorGallery01hint:
show luthormaingallery at gallerypos01
show luthorgallery01 at posgalleryhintpic
show luthorgalleryhint01 at posgalleryhint
pause
hide luthorgalleryhint01
hide luthorgallery01
call screen galleryluthor()

label LuthorGalleryAnim:
call screen screenanimluthor()
screen screenanimluthor():
    modal True
    add "gallery/luthorbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "luthoranimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "luthoranimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimluthor"), SetVariable ("animcount", 1), Jump ("LuthorGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Sexy Luthor{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 35{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}38GG-25-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Cowgirl{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/luthoranim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimluthor")]
    add "gallery/luthoranim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimluthor")]
            
label LuthorGallery01:
$ danistudlinessx = False
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

label LuthorCaseFuckx:
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
call screen luthorfuck01x()
screen luthorfuck01x():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuckPussyx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEndx")

label LuthorCaseFuckPussyx:
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
call screen luthorfuck02x()
screen luthorfuck02x():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEndx")

label LuthorCaseFuckEndx:
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
        $ danistudlinessx = True    
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
        
label DaniAnalSlowFuckx:
window hide
hide cum
hide faster
hide slower
play channel1 "sounds/danimassive.mp3"
show luthordanianalslowvideo behind luthordanianalfastvideo
$ renpy.pause(1.0, hard='True')
hide luthordanianalfastvideo with dissolve
pause
if danistudlinessx:
    da "Your cock is so HUGE! It's the BIGGEST bulldick I ever had!"
if danistudlinessx == False:
    da "Hurry up [name], we need to get that key!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen luthordanianalslowx()
screen luthordanianalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalFastFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEndx")

label DaniAnalFastFuckx:
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
if danistudlinessx:
    da "Oh my God, you're going so DEEP!"
if danistudlinessx == False:
    da "Why are you fucking me so HARD? Just blow your load already!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
call screen luthordanianalfastx()
screen luthordanianalfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEndx")

label DaniAnalFuckEndx:
hide slower
hide cum
hide faster
if danistudlinessx:
    da "You're making me CUM NON-STOP!"
    mc "I'm about to bust my nut too..."
if danistudlinessx == False:
    da "Are you finally going to cum? Please do it quickly!"
scene danianalcum01 with dissolve
hide luthordanianalslowvideo
hide luthordanianalfastvideo
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
if danistudlinessx:
    da "I'm gonna CREAM all over that gigantic discharging DONG!"
if danistudlinessx == False:
    da "Try and come a LOT!"
window hide
with fastflash
if danistudlinessx:
    mc "Get ready for more of MY cream too!"
if danistudlinessx == False:
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
jump LuthorGallery