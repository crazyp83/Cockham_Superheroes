label WidowGallery:
stop channel3
play channel3 "sounds/sexy07.mp3"
scene widowbackground with dissolve
show widowmaingallery at gallerypos01 with moveinleft
call screen gallerywidow()
screen gallerywidow():
    text "{font=Gui/Heroes Legend.ttf}Naughty Black Widow{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerywidow"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerywidow"), Jump ("WidowGalleryAnim")]

    imagebutton:
        focus_mask True
        idle "gallery/widowgallery01.png" xpos 400 ypos 100
        hover "gallery/widowgallery01.png"
        action Jump ("WidowGallery01")
    text "{font=Gui/Heroes Legend.ttf}Intro w/Frost{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    
    if renpy.seen_image("widowroom03"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery02.png" xpos 750 ypos 100
            hover "gallery/widowgallery02.png"
            action Jump ("WidowGallery02")
    text "{font=Gui/Heroes Legend.ttf}Room Sexy{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("widowroom03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("widowpool01"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery03.png" xpos 1100 ypos 100
            hover "gallery/widowgallery03.png"
            action Jump ("WidowGallery03")
    text "{font=Gui/Heroes Legend.ttf}Pool Sexy{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("widowpool01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("widowbed01"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery04.png" xpos 1450 ypos 100
            hover "gallery/widowgallery04.png"
            action Jump ("WidowGallery04")
    text "{font=Gui/Heroes Legend.ttf}Dildo Pleasure{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("widowbed01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("widowpoolshower02"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery05.png" xpos 400 ypos 380
            hover "gallery/widowgallery05.png"
            action Jump ("WidowGallery05")
    text "{font=Gui/Heroes Legend.ttf}Pool Shower Sex{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05

    if renpy.seen_image("widowpoolshower02") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("WidowGallery05hint")

    if renpy.seen_image("wrestling40"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery06.png" xpos 750 ypos 380
            hover "gallery/widowgallery06.png"
            action Jump ("WidowGallery06")
    text "{font=Gui/Heroes Legend.ttf}Naked Wrestling{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06

    if renpy.seen_image("wrestling40") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("WidowGallery06hint")

    if renpy.seen_image("widowbed21"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery07.png" xpos 1100 ypos 380
            hover "gallery/widowgallery07.png"
            action Jump ("WidowGallery07")
    text "{font=Gui/Heroes Legend.ttf}Bed Sex{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext07

    if renpy.seen_image("widowbed21") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 380
            hover "gallery/gallerylockedhint.png"
            action Jump ("WidowGallery07hint")

    if renpy.seen_image("larawidowpool01"):
        imagebutton:
            focus_mask True
            idle "gallery/laragallery03.png" xpos 1450 ypos 380
            hover "gallery/laragallery03.png"
            action Jump ("Widowgallery08")
    text "{font=Gui/Heroes Legend.ttf}Lesbian w/Lara{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext08
    if renpy.seen_image("larawidowpool01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("wrestlingnew13"):
        imagebutton:
            focus_mask True
            idle "gallery/widowgallery09.png" xpos 400 ypos 660
            hover "gallery/widowgallery09.png"
            action Jump ("WidowGallery09")
    text "{font=Gui/Heroes Legend.ttf}Sexy Fight{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext09
    if renpy.seen_image("wrestlingnew13") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

    if renpy.seen_image("widownatalya03"):
        imagebutton:
            focus_mask True
            idle "gallery/natalyagallery02.png" xpos 750 ypos 660
            hover "gallery/natalyagallery02.png"
            action Jump ("WidowGallery10")
    text "{font=Gui/Heroes Legend.ttf}3some w/Natalya{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext10
    if renpy.seen_image("widownatalya03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 660
            hover "gallery/gallerylocked.png"
            action Jump ("WidowGallery")

label WidowGallery05hint:
show widowmaingallery at gallerypos01
show widowgallery05 at posgalleryhintpic
show widowgalleryhint05 at posgalleryhint
pause
hide widowgalleryhint05
hide widowgallery05
call screen gallerywidow()

label WidowGallery06hint:
show widowmaingallery at gallerypos01
show widowgallery06 at posgalleryhintpic
show widowgalleryhint06 at posgalleryhint
pause
hide widowgalleryhint06
hide widowgallery06
call screen gallerywidow()

label WidowGallery07hint:
show widowmaingallery at gallerypos01
show widowgallery07 at posgalleryhintpic
show widowgalleryhint07 at posgalleryhint
pause
hide widowgalleryhint07
hide widowgallery07
call screen gallerywidow()

label WidowGalleryAnim:
call screen screenanimwidow()
screen screenanimwidow():
    modal True
    add "gallery/widowbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "widowanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "widowanimlin" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "widowanimbik" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "widowanimgym" xalign -0.1 yalign 1.0
    if animcount == 5:
        add "widowanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimwidow"), SetVariable ("animcount", 1), Jump ("WidowGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Black Widow{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 32{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft3{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}32DDD-22-34{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Teasing{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Anal{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/widowanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimwidow")]
    add "gallery/widowanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimwidow")]
    add "gallery/widowanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimwidow")]
    add "gallery/widowanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimwidow")]
    add "gallery/widowanim05.png" xpos 1580 ypos 800
    button:
        xpos 1550
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 5), Show ("screenanimwidow")]

label WidowGallery01:
stop channel3
$ frostlicksawx = False
play music "sounds/sexy01.mp3"
scene frostofficebackground
show handsfreescene at posiconup
show froststrip00:
    zoom 0.5 xpos 100 ypos 0    
show widowoffice01:
    zoom 0.5 xpos 800 ypos 0
ef "I will show you how my body is clearly SUPERIOR to the Black Widow's! {w=4.0}{nw}"
hide handsfreescene
bw "What-ever! {w=2.0}{nw}"
window hide
show frostofficebackground at frostzoombackgroundleft
show froststrip00 at frostzoomleft
show widowoffice01 at widowzoomleft
$ renpy.pause(2.0, hard='True')
ef "So just watch ME, and not that redhead trollop. {w=4.0}{nw}"
bw "Why would he watch an old hag like you? {w=4.0}{nw}"
ef "Despite my age, I keep VERY FIT as you can see... {w=4.0}{nw}"
window hide
hide widowoffice01
show widowoffice02:
    xoffset 1200 yoffset -100 
show froststrip00 at frostunzoomleft
show frostofficebackground at frostunzoombackgroundleft
show widowoffice02 at widowunzoomleft
$ renpy.pause(1.5, hard='True')
bw "Yeah, well so do I! I'll PROVE it to you! {w=4.0}{nw}"
window hide
show froststrip00 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice02 at widowzoomleft02
$ renpy.pause(2.0, hard='True')
ef "Your breasts are no where near as perfect as mine! {w=4.0}{nw}"
bw "I'll let [hero] be the judge of that... {w=4.0}{nw}"
window hide
hide widowoffice02
show widowoffice03:
    zoom 1.0 xoffset 0 yoffset -400
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice03 at widowzoomleftdown
$ renpy.pause(2.0, hard='True')
bw "And I'll let him be the judge of my fine ass, he won't find one better in Cockham! {w=6.0}{nw}"
window hide
show widowoffice03 at widowunzoomleftdown
show frostofficebackground at frostzoombackgroundleftdown
hide froststrip00
show froststrip01:
    zoom 1 xoffset -1200 yoffset -1080 
show froststrip01 at frostzoomleftdown
$ renpy.pause(2.0, hard='True')
ef "My tits are the most EFFICIENT in the city at bringing studs over the edge! Look at how LARGE they are, ideal for a HUGE-COCKED BOY like you I'd say! {w=8.0}{nw}"
window hide
show froststrip01 at frostzoomleftdownup
show frostofficebackground at frostzoombackgroundleftup
$ renpy.pause(1.0, hard='True')
ef "Don't you agree [hero]? {w=2.0}{nw}"
mc "Err... {w=2.0}{nw}"
window hide
hide widowoffice03
show widowoffice04:
    zoom 1.0 xoffset 1500 yoffset -400        
show froststrip01 at frostunzoomleft
show widowoffice04 at widowunzoomleft
show frostofficebackground at frostunzoombackgroundleft
$ renpy.pause(1.0, hard='True')
bw "My SUPER-TITS aren't just for SMOTHERING ENEMIES, they can also wrap like velvet around a big hard shaft and make it CONVULSE WITH PLEASURE! {w=8.0}{nw}"
window hide
show froststrip01 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice04 at widowzoomleft02
$ renpy.pause(2.0, hard='True')
bw "I'll show you MORE if you're a GOOD boy... {w=4.0}{nw}"
window hide
hide froststrip01
show froststrip02:
    zoom 1 xoffset -1200 yoffset -100     
show froststrip02 at frostzoomleftcenter
show frostofficebackground at frostzoombackgroundleftcenter
show widowoffice04 at widowzoomleftfar
$ renpy.pause(1.5, hard='True')
ef "Why wait? He can have a closer look RIGHT NOW at MY sumptuous rack! {w=4.0}{nw}"
window hide
hide widowoffice04
show widowoffice05:
    zoom 1.0 xoffset 1500 yoffset -400        
show froststrip02 at frostunzoomleft
show widowoffice05 at widowunzoomleft
show frostofficebackground at frostunzoombackgroundleft
$ renpy.pause(1.5, hard='True')
bw "Oh, we're playing THAT game, hey? {w=4.0}{nw}"
window hide
show froststrip02 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice05 at widowzoomleft02
$ renpy.pause(2.0, hard='True')
bw "Then have a good LONG look at these titties [hero]. And imagine them SQUEEZING your hard shaft... Until you EXPLODE your warm nectar all over them. {w=8.0}{nw}"
window hide
hide froststrip02
show froststrip03:
    zoom 1 xoffset -1200 yoffset -100     
show froststrip03 at frostzoomleftdown
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice05 at widowunzoomleftdown
$ renpy.pause(2.0, hard='True')
ef "Look at how TIGHT my ass is! Ideal for PUMPING a nice big fat load out of a rockhard monstercock... {w=6.0}{nw}"
window hide
hide widowoffice05
show widowoffice06:
    zoom 1 xoffset 1600 yoffset -800 
show froststrip03 at frostzoomleftout
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice06 at widowzoomleftdown
$ renpy.pause(2.0, hard='True')
bw "Pff, my BUBBLE BUTT is the MOST cock-hardening in the whole town! It can make any dong BLOW ITS LOAD in a super-instant! {w=8.0}{nw}"
window hide
hide froststrip03
show froststripwiggle:
    zoom 1 xoffset -800 yoffset 0
show froststripwiggle at frostunzoomwiggle
show frostofficebackground at frostzoombackgroundleftup
show widowoffice06 at widowzoomleftfar02
$ renpy.pause(2.0, hard='True')
ef "Time to show [hero] the ULTIMATE PROOF that I AM the MOST BEAUTIFUL WOMAN IN THE WORLD! {w=6.0}{nw}"
window hide
hide widowoffice06
show widowofficewiggle:
    zoom 1 xoffset 1600 yoffset 0
show widowofficewiggle at frostunzoomwiggle
show frostofficebackground at frostzoombackgroundrightup
show froststripwiggle at frostunzoomwiggleout
$ renpy.pause(2.0, hard='True')
bw "That's no proof! THIS will DEFINITELY convince him that I am MORE BEAUTIFUL THAN YOU! {w=6.0}{nw}"
show froststripwiggle:
    zoom 1 xoffset -1200 yoffset 0
show froststripwiggle at frostwiggleleft
show frostofficebackground at frostunzoombackgroundleft
show widowofficewiggle at frostwiggleright
ef "Let HIM decide then, he'll have NO CHOICE but to RECOGNIZE MY UNWORLDLY BEAUTY! {w=6.0}{nw}"
mc "I'm STILL undecided. Do I really have to choose? {w=4.0}{nw}"
ef "YES you DO! And since you're INCAPABLE of taking IMPORTANT decisions, my tits will take them for YOU! {w=7.0}{nw}"
bw "I'm not letting you pervert his mind on your own, White Queen. Count me in for whatever SALACIOUS idea you have in mind! {w=8.0}{nw}"
window hide
$ renpy.pause(5.0, hard='True')
scene frostofficemc01 with dissolve
ef "Well, it involves our tits and that GROWING boyhood... Whoever makes him EXPLODE first is clearly the MOST BEAUTIFUL WOMAN IN THE WORLD! And it will be ME! {w=8.0}{nw}"
bw "Not a chance, my SUPER-TITS will bring him over the edge BEFORE yours do FOR SURE! {w=6.0}{nw}"
scene frostofficemc02 with dissolve
mc "Err... {w=2.0}{nw}"
ef "Just get your cock out of that straining thong, lie on the coffee table and let our FUNBAGS do the rest, [hero]! {w=7.0}{nw}"
window hide
scene frosttitfuckbackground
show frostofficemc03
with dissolve
play sound "sounds/gasp.mp3"
ef "Damn boy, that thing is just MASSIVE... {w=4.0}{nw}"
bw "It's even BIGGER than I imagined. {w=4.0}{nw}"
ef "This double-titfuck is going to be EPIC! {w=4.0}{nw}"
stop sound
window hide

label FrostOfficeTitAnimx:
show frosttitfuckbackgroundb behind frostofficelick at titfuckbackground
show frostofficetitfuck behind frostofficelick 
$ renpy.pause(1.0, hard='True')
if frostlicksawx:
    bw "Maybe we should go back to using our tits, he seems to be a bit more responsive to them..."
    ef "Especially to MINE. Let's make him cum then!"
    hide cum
    hide titfucking
    stop channel1
    hide frosttitfuckbackground
    hide frostofficelick
    hide frostofficemc03
    with dissolve
    show cum:
        xpos 1800 ypos 500
    show licking:
        xpos 50 ypos 500
    jump FrostTitfuckx

stop channel1
hide frosttitfuckbackground
hide frostofficelick
hide frostofficemc03
with dissolve
show cum:
    xpos 1800 ypos 500
show licking:
    xpos 50 ypos 500
label FrostTitfuckx:
play channel1 "sounds/wank.mp3"
call screen screentitfuckx()
screen screentitfuckx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostOfficeLickAnimx")
    button:
        xpos 1820
        ypos 500
        xysize(70, 60)        
        action Jump ("FrostOfficeCumx")
    
label FrostOfficeLickAnimx:
window hide
show frostofficelick behind frosttitfuckbackgroundb
show frostofficelick behind frostofficetitfuck
$ renpy.pause(1.0, hard='True')
hide cum
hide titfucking
hide licking
if frostlicksawx == False:
    $ frostlicksawx = True
    if age >= 20:
        ef "You like that don't you? Our big soft breasts rubbing against your rockhard alpha-cock?"
    if age >= 18 and age <=19:
        ef "You like that don't you? Our big soft breasts rubbing against your rockhard teenage alpha-cock?"
    mc "Damn it, yeah, it feels real good."
    bw "How about we lick that dong for a while? I wanna TASTE it!"
    ef "Good idea, Let's take turns so he can rate our licking..."
hide frostofficetitfuck
hide frosttitfuckbackgroundb
with dissolve
show titfucking:
    xpos 50 ypos 500
stop channel1
play channel1 "sounds/lick01.ogg"
call screen screenlickfuckx()
screen screenlickfuckx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(240, 60)        
        action Jump ("FrostOfficeTitAnimx")
 
label FrostOfficeCumx:
if age >= 20:
    ef "It looks like this monster alpha-dong is going to spew its load... {w=4.0}{nw}"
if age >= 18 and age <=19:
    ef "It looks like this monster teenage alpha-dong is going to spew its load... {w=4.0}{nw}"
window hide
$ renpy.pause(2.0, hard='True')
bw "Yeah, I can feel it too, his shaft is TREMBLING with anticipation... {w=4.0}{nw}"
window hide
$ renpy.pause(2.0, hard='True')
hide frostofficetitfuck
hide cum
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
scene frosttitfuckbackground
show frosttitfuckcum01
with dissolve
ef "That's it? My fat tits around your shaft are making you cum already, [hero]? {w=5.0}{nw}"
hide frosttitfuckcum01
show frosttitfuckcum02
with dissolve
bw "I very much doubt it, it's clearly the pumping action of MY EXQUISITE breasts that are making him BLAST such a load! {w=7.0}{nw}"
window hide
with fastflash
if age >= 20:
    ef "In your DREAMS! PROVE her WRONG and douse ME in your cream, [hero]! {w=5.0}{nw}"
if age >= 18 and age <=19:
    ef "In your DREAMS! PROVE her WRONG and douse ME in your teenage cream, [hero]! {w=5.0}{nw}"
hide frosttitfuckcum02
show frosttitfuckcum03a
with dissolve
ef "YEAH, just like that... {w=2.0}{nw}"
with fastflash
ef "More, MORE SUPER-SPUNK for ME! {w=2.0}{nw}"
hide frosttitfuckcum03a
show frosttitfuckcum03b
with fastdissolve
ef "COVER my face in your red-hot nectar! {w=2.0}{nw}"
play sound "sounds/moan02.mp3"
with fastflash
bw "You dirty whore, you're STEALING his cum from ME! Let me SWALLOW your cream, [hero]... {w=5.0}{nw}"
hide frosttitfuckcum03b
show frosttitfuckcum04
with dissolve
play sound "sounds/moan01.mp3"
bw "Gimme, gimme, gimme... mmggllurb.... {w=2.0}{nw}"
with fastflash
ef "My turn, I'm gonna drain him with my mouth! {w=3.0}{nw}"
hide frosttitfuckcum04
show frosttitfuckcum05
with dissolve
ef "Gl...uuu... *swallow* {w=2.0}{nw}"
with fastflash
ef "De...li...glllb...cious! {w=2.0}{nw}"
hide frosttitfuckcum05
show frosttitfuckcum06
with dissolve
play sound "sounds/panting.mp3"
stop channel1
stop music fadeout 1.0
bw "I think he's drained. For NOW. {w=2.0}{nw}"
ef "His cock is still hard though... Maybe we could... But no. We've done enough to his poor dong. {w=6.0}{nw}"    
scene frostofficebackground
show froststrip06 at left
show widowoffice07 at centerright
with fade
ef "I think you've seen enough to take a decision [hero]. Who is the most beautiful, me or her? {w=6.0}{nw}"
mc "I believe the Black Widow is the most beautiful here. {w=4.0}{nw}"
hide froststrip06
hide widowoffice07
show widowoffice08 at centerright
show froststrip07 at centerleft
with fastdissolve
ef "How dare you!"
play sound "sounds/slap.mp3"
mc "Hey! I didn't deserve that!"
hide froststrip07
hide widowoffice08
show froststrip08 at left
show widowoffice10 at centerright        
with fastdissolve 
bw "[hero] has CHOSEN! And he chose ME. take THAT, White Queen! HA HA HA! {w=4.0}{nw}"
ef "Get out of here, BOTH OF YOU! {w=2.0}{nw}"
hide widowoffice10
show widowoffice07 at centerright
with fastdissolve         
bw "With pleasure... Come [name], we're DONE here. {w=3.0}{nw}"
jump WidowGallery

label WidowGallery02:
stop channel3
play music "sounds/sexy04.mp3"
scene widowroomnight with fade
show widowroom01 at centerleft with moveinright
bw "I was expecting you... [hero]."
hide widowroom01
show widowroomeyeblink
with fastdissolve
menu:
    "Ooh? And why so?..." if widowpicked:
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
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
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
        stop music
        jump WidowGallery
    "Ooh? And why so?..." if frostpicked:
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
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
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
        stop music
        jump WidowGallery
    "Ooh? And why so?..." if frostpicked == False and widowpicked == False:
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
            zoom 1.8 xoffset -100 yoffset 0
        show widowroomfull:
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
        stop music
        jump WidowGallery

label WidowGallery03:
stop channel3
scene poolbackground with fade
mc "Once again, it appears that the Black Widow will only show up AFTER I've gone for a swim..."
scene poolmc01 with dissolve
mc "So I guess I have no choice but to swim... Alone."
stop music
play music "sounds/swim.mp3"
scene poolmc02 with dissolve
mc "* Surely the black widow will come anytime now... *"
scene poolmc03 with dissolve
if age >= 20:
    mc "* Ah, maybe she'll come as I do a back-crawl and my monster cock is clearly visible above the water surface... *"
if age == 18 or age == 19:
    mc "* Ah, maybe she'll come as I do a back-crawl and my monster teenage cock is clearly visible above the water surface... *"
stop music
scene widowpool01 with dissolve
bw "Well, well, well, if it isn't [hero] swimming in a super-tight speedo..."
mc "* bingo *"
scene widowpoolbackground02 blurred
show widowpool03
with dissolve
play music "sounds/sexy06.mp3"
bw "What do you think of MY super-tight bikini?"
window hide
show widowpoolbackground01 blurred:
    zoom 1.1 xoffset -100 yoffset 0
show widowpool02:
    zoom 1.0 xoffset -50 yoffset 0    
show widowpoolbackground01 blurred at widowpoolbackzoombackground
show widowpool02 at widowpoolfullup
with dissolve
$ renpy.pause(4.0, hard='True')     
bw "Have a good look at the back... How it fits snugly between my TIGHT asscheeks..."
mc "I am... having a good look."
scene widowpoolbackground02 blurred
show widowpool03
with dissolve
bw "Now don't get any funny ideas. After all, I came here to SWIM."
scene widowpoolbackground02 blurred:
    zoom 1.1
show widowpool04
with dissolve
bw "So let me do a bit of stretching first..."
mc "Damn, you're supple..."
hide widowpool04
show widowpool05
with dissolve
bw "As an expert COMBAT Super-Heroine, I NEED to be..."
scene widowpoolbackground02 blurred:
    zoom 1.2 yoffset -200
show widowpool06a
with dissolve
bw "...And to stay FIT!"
hide widowpool06a
show widowpool06b
with fastdissolve
bw "A few one-armed press-ups..."
window hide
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool06a
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06a
show widowpool06b
with fastdissolve
$ renpy.pause(0.5, hard=True)
hide widowpool06b
show widowpool07
with dissolve
bw "And a bit more teasing..."
mc "Ggg...ggg..."
hide widowpool07
show widowpool09
with dissolve
bw "Now you seem to be ready for some UNDERWATER combat training... Try and catch me if you can, [name]..."
stop music
scene widowpool10 with dissolve
mc "Wh...What???"
scene widowpool11 with dissolve
play sound "sounds/diving.mp3"
bw "You'd better hurry up, I already have a head-start!"
scene widowpool12 with dissolve
stop sound
play music "sounds/underwater.mp3"
mc "* She's taunting me... *"
scene widowpool13 with dissolve
mc "* Let's make a move... Not too sudden... So I can surprise her... *"
scene widowpool14 with dissolve
play sound "sounds/whoosh.mp3"
mc "What the??? Damn, she's fast!"
scene widowpool15 with dissolve
stop sound
mc "* Where did she go??? *"
scene widowpool16 with dissolve
bw "* I'm here, silly... SURPRISE! *"
play sound "sounds/kiss.mp3"
mc "* Ok, you win, Natasha... *"
scene widowpool17 with dissolve
stop sound
mc "* Let's grab her ass and see where that goes... *"
scene widowpool18 with dissolve
bw "* No, no, you naughty boy. Not yet... *"
mc "* Ah. Nowhere apparently... *"
stop music
scene widowpool19:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with fade
bw "Now you stay and cool down, [name]. I think you had enough emotions for the night..."
mc "No I didn't, no I didn't!"
bw "Goodnight and sweet dreams!"
jump WidowGallery

label WidowGallery04:
stop channel3
play channel1 "sounds/sexy03.mp3"
scene widowbed01
voice "widow/room31"
bw "Just sit back and enjoy the show, [name]. And NO TOUCHING! Not even yourself..."
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
jump WidowGallery

label WidowGallery05:
stop channel3
stop music
play channel1 "sounds/shower.mp3"
scene widowpoolshower00 with fade
mc "I can hear the shower running. Which means that the Black Widow must be in there..."
scene widowpoolshower01 with dissolve
mc "And bingo! Topless no less..."
scene widowpoolshower02 with dissolve
mc " * Look at that fine ass, just LOOK AT IT! *"
scene widowpoolshower03 with dissolve
bw "I might not have any Super-Senses but I could still tell you were around. Lurking."
mc "I am NOT lurking! I was coming for a... fresh shower before heading for the pool."
scene widowpoolshower04 with fastdissolve
bw "Are you SURE about that? I feel like, maybe, you were ogling my backside."
mc "Err... No... Yes... I mean, damn, what an ASS!"
scene widowpoolshower05 with dissolve
bw "Why don't you drop that that ridiculously bulging swimtrunk and come inside then..."
mc "Alright!"
scene widowpoolshower06 with dissolve
stop channel1
play channel2 "sounds/sexy02.mp3"
bw "Even soft, it's still sssooo GIGANTIC!"
mc "And it's gonna get HARD real fast for you, Natasha!"
scene widowpoolshower07 with dissolve
mc "Especially if I start playing with these big funbags of yours..."
bw "Oooh, what do you have in mind for a FUN game with FUNBAGS?"
scene widowpoolshower08 with dissolve
play sound "sounds/lick01.ogg"
mc "This..."
scene widowpoolshower09 with dissolve
play sound "sounds/moan01.mp3"
bw "Mmmh, yeah, lick it clean... You naughty boy."
scene widowpoolshower10 with dissolve
play sound "sounds/kiss.mp3"
bw "Come and kiss me."
scene widowpoolshower11 with dissolve
mc "Are we finally going to fuck, Natasha?"
if age >= 20:
    bw "I hesitate. Let's start with you rubbing that fat donkey-dick against my asscheeks. Until you EXPLODE!"
if age >= 18 and age <= 19:
    bw "I hesitate. Let's start with you rubbing that fat teenage donkey-dick against my asscheeks. Until you EXPLODE!"
scene widowpoolshower12 with dissolve
mc "Can't I just stick it in your ass please?"
bw "No, you may NOT! Just rub it against my ass... You'll enjoy it, I promise."
play music "sounds/moan02.mp3"
label WidowShowerSlowx:
window hide
hide slower
hide cum
show widowshowerslowvideo behind widowshowerfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfastvideo with dissolve
$ renpy.pause(2.0, hard='True')
bw "Yeah, just like that. Mmmh, it feels so HEAVY!"
window hide
show faster:
     xpos 1700 ypos 500
play channel1 "sounds/boymoan04.mp3"
call screen screenwidowshowerslowx()
screen screenwidowshowerslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowShowerFastx")

label WidowShowerFastx:
hide faster
mc "I need to do it FASTER!"
bw "If that can help you spew your load faster, be my guest..."
window hide
show widowshowerfastvideo behind widowshowerslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerslowvideo with dissolve
stop channel1
play channel1 "sounds/boymoan02.mp3"
show slower:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen screenwidowshowerfastx()
screen screenwidowshowerfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowShowerSlowx")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("WidowShowerCumx")

label WidowShowerCumx:
hide slower
hide cum
mc "I'm gonna cum, Natasha. I'm..."
scene widowpoolshowercum01 with dissolve
hide widowshowerslowvideo
hide widowshowerfastvideo
stop music
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAh, fuck!"
window hide
with fastflash
bw "Mmh, dump that seed all over my backside!"
scene widowpoolshowercum02 with dissolve
bw "Ooh, your shots are getting even BIGGER!"
window hide
with fastflash
mc "AAAH!"
scene widowpoolshowercum03 with dissolve
bw "Keep going [name], I don't want you to stop!"
window hide
with fastflash
mc "I... Oooh FUCK, here's MORE!!!!"
if age >= 20:
    bw "I want you to PLASTER the shower wall. NOW. PROVE to me you're a fucking BULLSTUD, DO IT!"
if age >= 18 and age <= 19:
    bw "I want you to PLASTER the shower wall. NOW. PROVE to me you're a fucking TEEN BULLSTUD, DO IT!"
scene widowpoolshowercum04 with dissolve
play sound "sounds/splat.ogg"
mc "RHAAAA!"
window hide
with fastflash
play sound "sounds/splat.ogg"
bw "Mmmh,that's it, your MONSTERSHOTS are fucking HITTING the wall with such BRUTAL FORCE!"
stop channel1
scene widowpoolshowercum05 with dissolve
play channel1 "sounds/boymoan02.mp3"
play sound "sounds/lick02.mp3"
bw "Mmmh, I just want to FEED on this warm tasty spunk..."
scene widowpoolshowercum06 with dissolve
mc "Damn, I came so MUCH. And I'm STILL ROCKHARD!"
scene widowpoolshowercum07 with dissolve
bw "What??? Oh my God, it's true! I want to suck on your fat bloated balls then..."
scene widowpoolshowercum08 with dissolve
play sound "sounds/lick03.mp3"
mc "Yeah, get them to churn another HUGE load for you!"
scene widowpoolshowercum09 with dissolve
play sound "sounds/lick02.mp3"
bw "I would like THAT! * suck * "
scene widowpoolshowercum10 with dissolve
bw "Maybe I should switch to the other BLOATED ball?"
scene widowpoolshowercum11 with dissolve
play sound "sounds/lick03.mp3"
mc "Og God... You're suckling on it like a starved calf!"
scene widowpoolshowercum12 with dissolve
play sound "sounds/lick02.mp3"
bw "Mmmh, there's so much cummy afterdreg to lick still..."
scene widowpoolshowercum13 with dissolve
mc "I can't..."
scene widowpoolshowercum14 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "...HOLD OFF, AAAH!!!"
window hide
with fastflash
if age >= 20:
    bw "Ooh, I coaxed ANOTHER load out of your behemoth? I'm so NAUGHTY!"
if age >= 18 and age <= 19:
    bw "Ooh, I coaxed ANOTHER load out of your teenage behemoth? I'm so NAUGHTY!"
scene widowpoolshowercum15 with dissolve
play sound "sounds/moan01.mp3"
bw "Mmmh, I LOVE how your shaft CONTORTS and SPASMS with each POWERFUL SHOT OF SPUNK!"
window hide
with fastflash
mc "I can feel that..."

if inventorylustring == False:
    scene widowpoolshowercum16a
    show widowpoolshowercum16b
    with dissolve
    mc "... I... don't think I...can cum anymore! AAAH!"
    window hide
    with fastflash
    bw "Blast the last of it then, [name]!"
    scene widowpoolshowercum17 with dissolve
    play sound "sounds/slurp.mp3"
    bw "That's a decent amount of spunk... I won't let it go down the drain... * slurp *"
    scene widowpoolshowercum19 with dissolve
    play sound "sounds/panting.mp3"
    bw "But now your cock is totally spent. Defeated by the Black Widow's expert hands!"
    mc "Oh God... Yeah... I'd better..."
    bw "Go back to your room? Yes, you'd BETTER!"
    jump WidowGallery
if inventorylustring:
    scene widowpoolshowercum16a
    show widowpoolshowercum16c
    with dissolve
    mc "... I still have MORE, RHAAAA!"
    play sound "sounds/magic.mp3"
    hide widowpoolshowercum16c
    show widowpoolshowercum16d
    with fastdissolve
    $ renpy.pause(0.5, hard='True')
    hide widowpoolshowercum16d
    show widowpoolshowercum16e
    with fastdissolve
    $ renpy.pause(0.5, hard='True')
    play sound "sounds/boymoan05.mp3"
    window hide
    with fastflash
    bw "MUCH more by the looks of it! Wow!"

scene widowpoolshowercum17 with dissolve
play sound "sounds/slurp.mp3"
bw "Look at all that spunk... I won't let it go down the drain... * slurp *"
scene widowpoolshowercum18 with dissolve
mc "That's all very well, but my cock needs a tight hole this TIME!"
bw "What are you going to do???"
mc "I'm gonna ASSFUCK YOU, that's what I'm going to do!"
bw "But..."
window hide

label WidowPoolSlowFuckx:
hide cum
hide slower
hide faster
hide assview
hide front
$ widowpoolassharderx = False
show widowshowerfaceslowvideo behind widowshowerfacefastvideo
show widowshowerfaceslowvideo behind widowshowerassslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerassslowvideo
hide widowshowerfacefastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen widowpoolassfacefuckslowx()
screen widowpoolassfacefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFastFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolFaceSlowx")

label WidowPoolFastFuckx:
hide cum
hide slower
hide faster
hide assview
hide front
if widowpoolassharderx == False:
    bw "Are you going to pound me harder?"
    mc "Is that what you want, Natasha?"
    bw "YES! I want your giant cock ripping my ass apart!"
    $ widowpoolassharderx = True    
show widowshowerfacefastvideo behind widowshowerfaceslowvideo
show widowshowerfacefastvideo behind widowshowerasssfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfaceslowvideo
hide widowshowerassfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen widowpoolassfacefuckfastx()
screen widowpoolassfacefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFaceFastx")


label WidowPoolFaceSlowx:
$ widowpoolassharderx = False
hide cum
hide slower
hide faster
hide assview
hide front
show widowshowerassslowvideo behind widowshowerfaceslowvideo
show widowshowerassslowvideo behind widowshowerasssfastvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerfaceslowvideo
hide widowshowerassfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen widowpoolassfuckslowx()
screen widowpoolassfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFaceFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolSlowFuckx")

label WidowPoolFaceFastx:
hide cum
hide slower
hide faster
hide assview
hide front
if widowpoolassharderx == False:
    bw "Go on, stick your monster shaft harder into my booty! ANAL-DESTROY ME!"
    mc "Since you ask so politely..."
    $ widowpoolassharderx = True
show widowshowerassfastvideo behind widowshowerfacefastvideo
show widowshowerassfastvideo behind widowshowerassslowvideo
$ renpy.pause(1.0, hard='True')
hide widowshowerassslowvideo
hide widowshowerfacefastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show front:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen widowpoolassfuckfastx()
screen widowpoolassfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowPoolFaceSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowPoolFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowPoolFastFuckx")

label WidowPoolFuckEndx:
bw "You've got another big load for my ass, STUD?"
mc "Fuck yeah, you want it?"
bw "Yes, BLAST that young spunk inside me [name], go on, FILL ME UP TO THE BRIM!"
scene widowpoolasscum01 with dissolve
hide widowshowerassfastvideo
hide widowshowerfacefastvideo
hide widowshowerassslowvideo
hide widowshowerfaceslowvideo
stop channel1
play channel1 "sounds/splooge02.mp3"
mc "Alright, here it comes, AAAH!"
window hide
with fastflash
bw "Mmh, I can FEEL every shot, they are so POWERFUL!"
scene widowpoolasscum02 with dissolve
play sound "sounds/womancum01.mp3"
mc "Fuck, I'm just coming NON-STOP! RHAAA!"
window hide
with fastflash
if age >= 20:
    bw "Your warm spunk is overflowing down my back!"
if age >= 18 and age <= 19:
    bw "Your warm teenage spunk is overflowing down my back!"
scene widowpoolasscum03 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "And here's more baby-batter for your back, DAMN IT, FU-UU-UUCK!"
window hide
with fastflash
bw "Keep going, more, MORE!"
scene widowpoolasscum04 with dissolve
play sound "sounds/boymoan05.mp3"
mc "RHAAA!"
window hide
with fastflash
bw "You could DROWN a woman in your virile load!..."
scene widowpoolasscum05 with dissolve
play sound "sounds/panting.mp3"
bw "...But not the Black Widow... Looks like I finally managed to tame that BEAST..."
mc "My balls hurt ssooo much..."
scene widowpoolasscum06 with dissolve
play sound "sounds/slap.mp3"
bw "That's what happens when you try to outfuck ME! Now let me finish my shower... I need to clean off all that SPUNK!"
jump WidowGallery

label WidowGallery06:
stop music
stop channel3
play sound "sounds/barfight.mp3"
scene wrestling40 with fade
mc "Why are we naked exactly? Apart from the fact that the dev is a pervert."
scene wrestling41 with dissolve
bw "You are too easily distracted by... womanly bits. It's the only way to teach you to FOCUS!"
mc "I buy it, it makes total sense."
bw "So be ready. TO FIGHT!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestling42 with dissolve
play sound "sounds/punch.mp3"
bw "Take that for starters!"
mc "Hey!"
scene wrestling43 with dissolve
play sound "sounds/punch.mp3"
bw "And THIS!"
mc "Watch out for my groin! It's super-important to me!"
scene wrestling44 with dissolve
play sound "sounds/panting.mp3"
bw "The Black Widow's aim is always SPOT ON."
scene wrestling45 with dissolve
mc "That's it, now you've made my cock ANGRY!"
bw "Ooh, I'm so scared. NOT!"
scene wrestling46 with dissolve
play sound "sounds/gasp.mp3"
mc "You will be soon, Black Widow..."
scene wrestling47 with dissolve
bw "What do you think you're doing?"
mc "I am making sure you SUBMIT to my SUPERIOR MUSCLES!"
scene wrestling48 with dissolve
mc "And I'm fondling your tits while I'm at it!"
scene wrestling49 with dissolve
bw "You're just a filthy PERVERT! But that will be your downfall..."
scene wrestling50 with dissolve
play sound "sounds/whoosh.mp3"
bw "For your strength is no match to the Black Widow's Super-Agility and Super-Combat stats!"
mc "How on...?"
play channel1 "sounds/sexy10.mp3"
scene wrestling57 with dissolve
bw "Now you are at MY mercy. And so is your COCK!"
scene wrestling58 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Oooh, you want to cum so badly, don't you? But my GRIP on your spermtube won't let you reach that pleasure spot... Just yet."
mc "Please Natasha, this is excrutiating!"
scene wrestling57 with dissolve
bw "I'll make you come when I DECIDE!"
play sound "sounds/boymoan02.mp3"
mc "Decide quickly then!"
scene wrestling59 with dissolve
bw "I'll let you come... Just a LITTLE!"
play sound "sounds/boymoan05.mp3"
scene wrestling58 with dissolve
bw "But not a full-blown orgasm..."
play sound "sounds/boymoan02.mp3"
mc "That is so cruel!"
scene wrestling57 with dissolve
bw "I'm teaching you SELF-CONTROL, [name]. You should be grateful. It is an essential part of Super-Combat."
mc "Alright, I got it, I got it, I am self-controlling, I swear! Just let me come!"
scene wrestling59 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Are you really though... I wonder. Let's see... Come just a little and then... STOP!"
scene wrestling57 with dissolve
play sound "sounds/panting.mp3"
if age >= 20:
    bw "Maybe you are after all, I'm not even gripping THAT tightly around your engorged monsterdong and you've stopped SPEWING."
if age >= 18 and age <= 19:
    bw "Maybe you are after all, I'm not even gripping THAT tightly around your engorged teenage monsterdong and you've stopped SPEWING."
mc "So, do I get a rew..."
scene wrestling59 with dissolve
play music "sounds/boyorgasm01.mp3"
bw "Now COME! BLAST THAT HOT SAUCE!"
window hide
with fastflash
mc "AAAH!"
scene wrestling60 with dissolve
play sound "sounds/thud.mp3"
bw "Oooh, look at you... You're coming all over yourself now, that's so FILTHY!"
window hide
with fastflash
mc "Oh GOD..."
scene wrestling61 with dissolve
play sound "sounds/wow.mp3"
bw "You really NEEDED to come, didn't you?"
window hide
with fastflash
if age >= 20:
    bw "That's a LOT of dirty scum you're spewing right there!"
if age >= 18 and age <= 19:
    bw "That's a LOT of dirty teen scum you're spewing right there!"
scene wrestling62 with dissolve
stop music
bw "You've BLASTED so MUCH cum! It's all over yourself..."
play sound "sounds/panting.mp3"
mc "Ggg..."
scene wrestling63 with dissolve
play sound "sounds/lick01.ogg"
bw "I'll help you clean it up... It's so TASTY!"
scene wrestling64 with dissolve
play sound "sounds/slurp.mp3"
bw "I gather I got MOST of it... Mmmh... * slurp * Goodnight, [name]!"
stop channel1
jump WidowGallery

label WidowGallery07:
$ widowharderx = False
$ widowblowfuckslowx = False
$ widowblowfuckfastx = False
$ widowbedanalslowx = False
$ widowbedanalfastx = False
stop music
stop channel3
play music "sounds/sexy09.mp3"
scene widowbed21 with fade
bw "It's you... I was waiting for you..."
if toldwidowbed:
    mc "And I answered your call. Cos I can't get enough of that hot bod of yours!"
if toldwidowbed == False:
    mc "Really? You're not going to just TEASE me this time?"
scene widowbed22 with dissolve
play sound "sounds/moan02.mp3"
if toldwidowbed:
    bw "I'm prepping my holes again... For your COCK!"
if toldwidowbed == False:
    bw "Since you clumsily helped me defeat that evil nazi nurse, I'm prepping my holes... For your COCK!"    
    $ toldwidowbed = True
mc "Alright!"
scene widowbed23 with dissolve
play sound "sounds/moan04.ogg"
bw "OOOOh! You'd better be as GOOD as my fingers, [hero]..."
mc "I will, I will, I promise!"
scene widowbed24:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
bw "I really got myself off... But that was just an appetizer for tonight."
scene widowbed25 with dissolve
bw "So get your pole out of that ridiculous thong and make it HARD for me!"
mc "I'm getting hard, I'm getting ROCK-HARD for you Natasha!"
scene widowbed26 with dissolve
bw "Mmh, I see that... Your enormous fuckrod is ssoo tempting... Bring it over here."
scene widowbed27 with dissolve
play sound "sounds/wow.mp3"
bw "Look at this MASSIVE piece of boymeat. It looks so yummy..."
scene widowbed28 with dissolve
bw "I'm gonna have to taste it first, hope you don't mind [name]?"
mc "Not at all, we have all evening for our lo-oove-mak..."
scene widowbed29 with dissolve
play sound "sounds/boymoan.mp3"
mc "...Oooh!"

label WidowBlowShortSlowx:
window hide
$ widowharderx = False
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
$ widowblowfuckfastx = False
if widowblowfuckslowx == False:
    mc "Ooh yeah, go nice and easy, get your mouth used to my alpha-dong's girth!"
    $ widowblowfuckslowx = True
window hide
pause
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowshortslowx()
screen widowblowshortslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVSlowx")

label WidowBlowShortFastx:
$ widowharderx = False
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
$ widowblowfuckslowx = False
if widowblowfuckfastx == False:
    mc "Yeah, you blow me so good, keep going!"
    $ widowblowfuckfastx = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowblowshortfastx()
screen widowblowshortfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVFastx")

label WidowBlowShortPOVSlowx:
$ widowharderx = False
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
$ widowblowfuckfastx = False
if widowblowfuckslowx == False:
    mc "Ooh yeah, go nice and easy, get your mouth used to my alpha-dong's girth!"
    $ widowblowfuckslowx = True
window hide
pause

show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowshortpovslowx()
screen widowblowshortpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortPOVFastx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortSlowx")

label WidowBlowShortPOVFastx:
$ widowharderx = False
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
$ widowblowfuckslowx = False
if widowblowfuckfastx == False:
    mc "Yeah, you blow me so good, keep going!"
    $ widowblowfuckfastx = True
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen widowblowshortpovfastx()
screen widowblowshortpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowShortPOVSlowx")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowShortFastx")

label WidowBlowHardSlowx:
if widowharderx == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharderx = True        
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
call screen widowblowhardslowx()
screen widowblowhardslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEndx")

label WidowBlowHardFastx:
if widowharderx == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharderx = True        
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
call screen widowblowhardfastx()
screen widowblowhardfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEndx")

label WidowBlowHardPOVSlowx:
if widowharderx == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharderx = True        
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
call screen widowblowhardpovslowx()
screen widowblowhardpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardPOVFastx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVSlowx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEndx")

label WidowBlowHardPOVFastx:
if widowharderx == False:
    mc "Now get it all the way down your cock-hungry throat, Black Widow!"
    $ widowharderx = True        
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
call screen widowblowhardpovfastx()
screen widowblowhardpovfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBlowHardPOVSlowx")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("WidowBlowShortPOVFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBlowHardFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBlowEndx")

label WidowBlowEndx:
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sideicon
stop channel1
scene widowbed30 with dissolve
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
bw "I reckon it's time for you to show ME some good time. Some tender love first, if you're capable of it that is..."
mc "Yeah, I can be romantic when I want, I'll prove it to you!"
scene widowbed34 with dissolve
play sound "sounds/moan02.mp3"
bw "Yes, just like that..."
bw "Now kiss me while you play with my muff..."
scene widowbed35 with dissolve
play sound "sounds/kiss.mp3"
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

label WidowBedAnalSlowx:
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
$ widowbedanalfastx = False
if widowbedanalslowx == False:
    bw "Your cock is just so fucking HUGE, AAAH!"
    $ widowbedanalslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen widowbedanalslowx()
screen widowbedanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBedAnalFrontSlowx")

label WidowBedAnalFastx:
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
$ widowbedanalslowx = False
if widowbedanalfastx == False:
    mc "POUND that dick with your ass even FASTER now, Natasha!"
    $ widowbedanalfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen widowbedanalfastx()
screen widowbedanalfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WidowBedAnalFrontFastx")

label WidowBedAnalFrontSlowx:
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
$ widowbedanalfastx = False
if widowbedanalslowx == False:
    bw "Your cock is just so fucking HUGE, AAAH!"
    $ widowbedanalslowx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen widowbedanalpovslowx()
screen widowbedanalpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalSlowx")

label WidowBedAnalFrontFastx:
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
$ widowbedanalslowx = False
if widowbedanalfastx == False:
    mc "POUND that dick with your ass even FASTER now, Natasha!"
    $ widowbedanalfastx = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen widowbedanalpovfastx()
screen widowbedanalpovfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WidowBedAnalEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WidowBedAnalFastx")

label WidowBedAnalEndx:
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
bw "I've never been impaled on such a MONSTER (age)yo cock!"
scene widowbedanalcum03 with dissolve
play sound "sounds/moan05.mp3"
bw "How can you still be cumming after dumping two MASSIVE loads already???"
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
bw "You gave me a MASSIVE cum enema..."
mc "I can see that. It's POURING out of your gaping ass. It's going to get messy on you bedsheets tonight."
scene widowbedanalcum06 with dissolve
mc "Time for me to go back to the gallery, cos I sure ain't cleaning this up."
bw "I should have known. Men always leave the women with the BURDENS. * sigh *"
stop music
jump WidowGallery

label WidowGallery08:
stop channel3
play channel2 "sounds/waterrun.mp3"
scene larawidowpool01 with dissolve
lc "I'm so glad you came. I heard you were... rather busy lately."
bw "Yeah, I am. But I thought it would be a nice change from my NEW routine."
scene larawidowpool02 with dissolve
lc "So, what new routine is that? Would you like to talk about it?"
bw "I'm fighting Western DECADENCE. Greed is the root of all evil. Speaking of which, your GOLDEN swimsuit is... rather tasteless."
scene larawidowpool03 with dissolve
lc "Ah, err... I can take it off if you want. I wanted to get a new one. A more modest one anyway."
scene larawidowpool04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
bw "That's better... I see you are ready to abandon your depraved ways."
stop music
play music "sounds/sexy03.mp3"
scene larawidowpool05 with dissolve
bw "Now there's ONE thing that needs sharing more than money..."
lc "And what is that?"
scene larawidowpool06 with dissolve
bw "LOVE..."
lc "Oooh... I ssooo agree..."
scene larawidowpool07 with dissolve
play sound "sounds/slurp.mp3"
lc "Mmmh..."
scene larawidowpool08 with dissolve
play sound "sounds/lick02.mp3"
lc "Aaah... You know my weak spots, Natasha..."
scene larawidowpool09 with dissolve
play sound "sounds/kiss.mp3"
bw "And you know mine..."
scene larawidowpool10 with dissolve
mc "Mmmh, I wonder whether now is a good time? My Super-Libido tells me to wait a bit longer for this lesbian show to escalate..."
lc "Now it's my turn to return the favor. I'm gonna hold you up in the water so you can play with your pussy in zero gravity..."
scene larawidowpool11a with dissolve
bw "Oh yeah, I like that..."
play channel1 "sounds/wank.mp3"
window hide
show widowlarapoolwank with fastdissolve
pause
bw "Gonna..."
scene larawidowpool12 with dissolve
stop channel1
play sound "sounds/moan05.mp3"
bw "... CUM, AAAHH!"
scene larawidowpool13 with dissolve
play sound "sounds/kiss.mp3"
bw "That was wonderful... Now your pussy needs some tender loving too... From my fingers!"
scene larawidowprewank01 with dissolve
lc "Ooooh..."
play channel1 "sounds/wetmassage.mp3"
window hide

label LaraPoolWankSlowxx: 
hide nexticon
hide faster
hide slower
show larawidowpoolwankslowvideo behind larawidowpoolwankfastvideo
pause 1.0
hide larawidowpoolwankfastvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen larawidowpoolwankslowxx()
screen larawidowpoolwankslowxx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankFastxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPoolWankEndxx")

label LaraPoolWankFastxx:
show larawidowpoolwankfastvideo behind larawidowpoolwankslowvideo
hide nexticon
hide faster
hide slower
hide larawidowpoolwankslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen larawidowpoolwankfastxx()
screen larawidowpoolwankfastxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankSlowxx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisPoolWankEndxx")

label LoisPoolWankEndxx:
hide nexticon
hide slower
hide faster
lc "Just like that, just like that...You're going to make me..."
scene larawidowpostwank01 with dissolve
stop channel1
play sound "sounds/moan06.ogg"
lc "...SQUIRT! AAAH!"
scene larawidowpool14 with dissolve
bw "Now I NEED to taste those yummy juices of yours..."
scene larawidowpool15 with dissolve
play channel1 "sounds/moan02.mp3"
lc "Oh God... Your tongue..."
play sound "sounds/lick02.mp3"
bw " * lick *"
scene larawidowpool16 with dissolve
lc "Yes, just keep going Natasha... "
mc "* Why is she holding her hand like that? *"
scene larawidowpool17 with dissolve
mc "* Oh, I got it. NOW is the time! Here's the gem, Lara! *"
scene larawidowpool18 with dissolve
play sound "sounds/magic.mp3"
lc "Patra-Khok-..."
scene larawidowpool19 with dissolve
lc "...Mindh-Khon-Troll!"
scene larawidowpool20 with dissolve
lc "Let go of your mind, Natasha! Remove the lock and escape from the grip of your enslaver! You are not working for the Soviets!"
scene larawidowpool21 with dissolve
play sound "sounds/magic.mp3"
lc "I FREE YOU, by the Power of the Queen Jewel!"
scene larawidowpool22 with dissolve
mc "Did it work?"
lc "Of course it did. I said the correct incantation which were left in a notebook by my late explorer father!"
mc "So she's no longer a radical leftist lunatic then? She's a normal decadent American capitalist right?"
lc "She needs to recover from the exhaustion. Let me take her back to the gallery and make sure she sleeps well."
stop music
stop channel1
stop channel2
jump WidowGallery

label WidowGallery09:
stop channel3
scene wrestlingnew01 with fade
mc "* This time, I'm wearing my re-inforced kevlar thong. I won't let her kick me in the nuts! *"
scene wrestlingnew02 with dissolve
bw "I see you're wearing a new outfit... Is that because I scare you?"
mc "No! It's just... for convenience."
play music "sounds/sexy04.mp3"
scene wrestlingnew03 with dissolve
bw "I'm wearing a new outfit too. It's all the latest rage in Cockham. Do you like it?"
mc "I... I suppose so..."
bw "You SUPPOSE so? Not much confidence there."
scene wrestlingnew04 with dissolve
bw "Let me stretch a bit before our FIGHT..."
mc "Err, alright. But then, we FIGHT!"
scene wrestlingnew05 with dissolve
bw "Sure. We fight. And I beat the crap out of you. As usual."
mc "Not THIS time, Natasha!"
scene wrestlingnew06:
    zoom 1.0 xoffset -40 yoffset -1800    
show wrestlingnew06 at widowgymfullup
with dissolve
$ renpy.pause(6.0, hard='True')    
bw "Oooh! Well then, I'd better REALLY stretch, shouldn't I?"
scene wrestlingnew07:
    zoom 1.0 xoffset 0 yoffset 0    
show wrestlingnew07 at widowgymfulldown
with dissolve
$ renpy.pause(6.0, hard='True')    
bw "I hope you're not LOSING YOUR CONCENTRATION by looking at my fine ass, [hero]?"
mc "Err... Not at all."
scene wrestlingnew08 with dissolve
bw "What about my nice round puppies? Can you ignore such sumptuous funbags?"
mc "I... Y...Yes, I CAN!"
scene wrestlingnew09 with dissolve
bw "Even when I SQUEEZE them together like this?"
mc "* Damn, I might get a HARDON! Need...to....concentrate! *"
stop music
play music "v03/fightmusic.mp3"
scene wrestlingnew11 with dissolve
mc "Your sexual teasing won't help you win this time! I'm ready to fight whenever YOU are!"
scene wrestlingnew12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
bw "I see. You have toughened up a bit. You might be a worthy opponent for once!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene wrestlingnew13 with dissolve
play sound "sounds/whoosh.mp3"
mc "* Damn! She moved away too fast *"
bw "You're looking for me? Look up then!"
scene wrestlingnew14 with dissolve
mc "* Where did she go now??? *"
bw "Behind you!"
scene wrestlingnew15 with dissolve
play sound "sounds/punch.mp3"
bw "Right on your back now!"
mc "What the???"
scene wrestlingnew16 with dissolve
bw "And now for the final..."
scene wrestlingnew17 with dissolve
play sound "sounds/punch.mp3"
mc "NOT YET!"
scene wrestlingnew18 with dissolve
bw "Hey!!!"
mc "You're taking flying lessons, Natasha? Be careful not to CRASH!"
scene wrestlingnew19 with dissolve
play sound "sounds/thud.mp3"
bw "Don't you worry about me. The Black Widow always lands on her two feet. Like this."
scene wrestlingnew20 with dissolve
play sound "sounds/punch.mp3"
bw "Let me finish where I left off!"
scene wrestlingnew21 with dissolve
play sound "sounds/mangrunt01.mp3"
bw "You're trying to escape from the Black Widow's grip, [hero]? Wishful thinking!"
mc "I'm not yielding, I know I can do it! I'll NEVER yield!"
scene wrestlingnew22 with dissolve
play sound "sounds/wank.mp3"
bw "What if I squeezed your fat balls a little? Would that change your mind?"
mc "NO-O-O-O! I mean, YES, my mind has totally CHANGED! I YIELD!"
bw "I thought so... Men are just ssoo attached to their little jewels, aren't they?"
mc "Please stop fondling them, I'm getting..."
scene wrestlingnew23 with dissolve
play sound "v041/metalbreak.mp3"
mc "...HARD! AAAH, it HURTS!"
scene wrestlingnew24 with dissolve
stop music
play music "sounds/sexy04.mp3"
if age >= 20:
    bw "Ooooh! Look what decided to join the party? A giant rock-hard dong!"
if age >= 18 and age <= 19:
    bw "Ooooh! Look what decided to join the party? A giant rock-hard teenage dong!"
scene wrestlingnew25 with dissolve
play sound "sounds/boymoan.mp3"
bw "It seems to be awfully HORNY! Look at all that cum splatter flying everywhere when I slightly tug on it!"
mc "Gggg..."
scene wrestlingnew26 with dissolve
bw "And now it's just LEAKING pre-spunk all the way down the trembling shaft... It must be ACHING for release, don't you think?"
mc "Y...YES, LET ME CUM!"
bw "Where would be the enjoyment in that?"
scene wrestlingnew27 with dissolve
play sound "sounds/boymoan02.mp3"
if age >= 20:
    bw "It's much more fun to watch that horny cock trying to spew its load..."
if age >= 18 and age <= 19:
    bw "It's much more fun to watch that horny teen cock trying to spew its load..."
scene wrestlingnew28 with dissolve
play sound "sounds/boyorgasm01.mp3"
bw "...but just not getting there because my hand is pressing so TIGHTLY against its spermtube..."
mc "Uuuuh... You're TEASING me so much!"
scene wrestlingnew29  with dissolve
play sound "sounds/boymoan03.mp3"
bw "But you LIKE to be teased. I can tell. That young horsedick of yours is just so HARD!"
window hide
with fastflash
play sound "sounds/panting.mp3"
mc "Aaah..."
bw "It doesn't look like you can hold off much longer. Your balls are getting BLOATED!"
scene wrestlingnew30 with dissolve
play sound "v031/boyorgasm02.mp3"
mc "I can't... I... NEED TO COME!"
bw "Sure, we all have \"needs\". But we don't always get what we want, now do we? Especially after LOSING a fight against the Black Widow!"
window hide
with fastflash
mc "Please, I beg you, let me RELIEVE MYSELF!"
scene wrestlingnew31 with dissolve
play sound "sounds/boymoan02.mp3"
if age >= 20:
    bw "Why would I do that when I'm having so much FUN? Watching your great big cum-cannon contorting itself and {i}trying{/i} to let loose HUGE WADS OF PENT-UP CUM?"
if age >= 18 and age <= 19:
    bw "Why would I do that when I'm having so much FUN? Watching your great big teenage cum-cannon contorting itself and {i}trying{/i} to let loose HUGE WADS OF PENT-UP CUM?"
window hide
with fastflash
mc "I'll do anything for you if you let my balls unload!"
scene wrestlingnew32 with dissolve
play sound "sounds/boymoan04.mp3"
bw "Anything? First, I want you to RECOGNIZE the Black Widow's SUPERIOR skills in Super-Combat..."
mc "I do, I do! You're the best at Super-Combat! Nobody can beat you!"
bw "Then, I want you to..."
scene wrestlingnew33 with dissolve
play sound "sounds/boymoan05.mp3"
bw "...BLAST THE BIGGEST LOAD OF SPUNK EVER!"
window hide
with hpunch
mc "AAAAH!"
scene wrestlingnew34 with dissolve
play sound "sounds/boymoan03.mp3"
bw "And..."
scene wrestlingnew35 with dissolve
play sound "sounds/boymoan05.mp3"
bw "...AGAIN! Give me all that sweet young cream!"
window hide
with vpunch
play sound "sounds/boyorgasm01.mp3"
mc "UUUH! TOO STRONG!"
scene wrestlingnew36 with dissolve
bw "Not too strong for the Black Widow's mouth! Feed me your seed!"
window hide 
with fastflash
mc "Oh God!"
scene wrestlingnew37 with dissolve
play sound "sounds/lick02.mp3"
bw "* swallow * Yeah, so tasty..."
window hide 
with fastflash
bw "KEEP CUMMING FOR ME, I'm not DONE with you!"
scene wrestlingnew38 with dissolve
play sound "sounds/blow01.mp3"
mc "You're draining me, AAAH!"
window hide
with hpunch
bw " * slurp * Mmmggg..."
scene wrestlingnew39 with dissolve
play sound "sounds/panting.mp3"
mc "UUUH, my balls hurt so much..."
bw "That's the price you pay for LOSING to me, [name]..."
scene wrestlingnew40 with dissolve
bw "But here's your reward for being a good boy and cumming SO MUCH for the Black Widow..."
play sound "sounds/lick03.mp3"
bw "Your own tasty SPUNK!"
mc "Gggg..."
bw "Now off you go. Don't ever think you can BEAT the Black Widow in SUPER-COMBAT again!"
stop music
stop channel1
stop channel2
jump WidowGallery

label WidowGallery10:
stop channel3
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

label NatalyaFistSlowx: 
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
call screen natalyafistslowx()
screen natalyafistslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEndx")

label NatalyaFistFastx:
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
call screen natalyafistfastx()
screen natalyafistfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistEndx")

label NatalyaFistEndx:
hide nexticon
hide slower
hide faster
nt "You're enjoying this, aren't you? All that Western decadence CORRUPTION is showing!"
bw "No, I ... It just reminds me of someone's c..."
nt "Oh, I see. That stupid Super-Hero with the stupid thong? Did he go as deep as THIS though?"

label NatalyaFistHarderSlowx:  
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
call screen natalyafistharderslowx()
screen natalyafistharderslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEndx")

label NatalyaFistHarderFastx:
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
call screen natalyafistharderfastx()
screen natalyafistharderfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFistHarderSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFistHarderEndx")

label NatalyaFistHarderEndx:
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
call screen usepower("useresistance", "HypnoNoResistancex", "HypnoResistancex") with dissolve

label HypnoNoResistancex:
"You are slowly being turned into a Soviet zombie sleeper agent..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
jump WidowGallery    

label HypnoResistancex:
stop music
scene widownatalya18a with dissolve
mc "Now, it's MY turn!"
$ img_l = []
$ l2_l = []
if mccombat >= 0:
    $ img_l.append("usecombat")
    $ l2_l.append("HypnoCombatx")
if mcmind >= 0:
    $ img_l.append("usemind")
    $ l2_l.append("HypnoCombatx")
if img_l:
    call screen usepower(img_l, "HypnoNoCombatx", l2_l) with dissolve

label HypnoNoCombatx:
mc "* You're too slow, player! Let's try this again..."
jump HypnoResistancex

label HypnoCombatx:
if selected_power == "usemind":
    play music "sounds/radiation02.mp3"    
    scene widownatalya20 with dissolve
    mc "YOU submit to my will!"
    stop music

if selected_power == "usecombat":
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
$ natalyablowslowx = False

label NatalyaBlowSlowx:
$ natalyablowfastx = False
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
if natalyablowslowx == False:
    $ natalyablowslowx = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowslowx()
screen natalyablowslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVSlowx")

label NatalyaBlowFastx:
$ natalyablowslowx = False
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
if natalyablowfastx == False:
    $ natalyablowfastx = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyablowfastx()
screen natalyablowfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowPOVFastx")

label NatalyaBlowPOVSlowx:
$ natalyablowfastx = False
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
if natalyablowslowx == False:
    $ natalyablowslowx = True
    mc "Yeah, just like that, my little cock-sluts!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckslowx()
screen natalyablowpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowSlowx")

label NatalyaBlowPOVFastx:
$ natalyablowslowx = False
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
if natalyablowfastx == False:
    $ natalyablowfastx = True    
    mc "You're well on your way to becoming my harem slaves, is that understood?"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyablowpovfuckfastx()
screen natalyablowpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaBlowPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaBlowFastx")

label NatalyaBlowEndx:
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
$ natalyaswitchslowx = False

label NatalyaSwitchBlowSlowx:
$ natalyaswitchfastx = False
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
if natalyaswitchslowx == False:
    $ natalyaswitchslowx = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchslowx()
screen natalyaswitchslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlowx")

label NatalyaSwitchBlowFastx:
$ natalyaswitchslowx = False
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
if natalyaswitchfastx == False:
    $ natalyaswitchfastx = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen natalyaswitchfastx()
screen natalyaswitchfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowPOVFastx")

label NatalyaSwitchBlowPOVSlowx:
$ natalyaswitchfastx = False
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
if natalyaswitchslowx == False:
    $ natalyaswitchslowx = True
    mc "Oh God, your warm mouths..."
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckslowx()
screen natalyaswitchcloserfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowSlowx")

label NatalyaSwitchBlowPOVFastx:
$ natalyaswitchslowx = False
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
if natalyaswitchfastx == False:
    $ natalyaswitchfastx = True    
    mc "You girls have a double-O License to Blow for sure!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyaswitchcloserfuckfastx()
screen natalyaswitchcloserfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaSwitchBlowPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaSwitchBlowFastx")

label NatalyaSwitchBlowEndx:
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
$ natalyafuckslowx = False

label NatalyaFuckSlowx:
$ natalyafuckfastx = False
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
if natalyafuckslowx == False:
    $ natalyafuckslowx = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckslowx()
screen natalyafuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVSlowx")

label NatalyaFuckFastx:
$ natalyafuckslowx = False
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
if natalyafuckfastx == False:
    $ natalyafuckfastx = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen natalyafuckfastx()
screen natalyafuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckPOVFastx")

label NatalyaFuckPOVSlowx:
$ natalyafuckfastx = False
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
if natalyafuckslowx == False:
    $ natalyafuckslowx = True
    mc "How is it? Are you SUBMITTING to my GIANT cock yet, Agent Natalya?"
    nt "I... AAAH, it's so BIG!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckslowx()
screen natalyafuckpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckSlowx")

label NatalyaFuckPOVFastx:
$ natalyafuckslowx = False
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
if natalyafuckfastx == False:
    $ natalyafuckfastx = True    
    mc "And if I pound you even FASTER?"
    bw "You're fucking her so HARD, I don't think she can even answer you..."
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen natalyafuckpovfuckfastx()
screen natalyafuckpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("NatalyaFuckFastx")

label NatalyaFuckEndx:
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

label NatalyaWidowFuckSlowx:
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
call screen natalyawidowfuckslowx()
screen natalyawidowfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFastx")

label NatalyaWidowFuckFastx:
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
call screen natalyawidowfuckfastx()
screen natalyawidowfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("NatalyaWidowFuckFasterx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckSlowx")

label NatalyaWidowFuckFasterx:
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
call screen natalyawidowfuckfasterx()
screen natalyawidowfuckfasterx():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("NatalyaWidowFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("NatalyaWidowFuckFastx")

label NatalyaWidowFuckEndx:
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
stop music
stop channel1
stop channel2
jump WidowGallery