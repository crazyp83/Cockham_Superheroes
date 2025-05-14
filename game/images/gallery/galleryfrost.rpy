label FrostGallery:
stop channel3
play channel3 "sounds/coolmusic.mp3"
scene frostbackground
show frostmaingallery at gallerypos01 with moveinleft
call screen galleryfrost()
screen galleryfrost():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Emma Frost{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryfrost"), Jump ("MainGallery02")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryfrost"), Jump ("FrostGalleryAnim")]
    
    imagebutton:
        focus_mask True
        idle "gallery/widowgallery01.png" xpos 400 ypos 100
        hover "gallery/widowgallery01.png"
        action Jump ("FrostGallery01")
    text "{font=Gui/Heroes Legend.ttf}Intro w/Widow{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01

    if renpy.seen_image("frostfuck01"):
        imagebutton:
            focus_mask True
            idle "gallery/frostgallery02.png" xpos 750 ypos 100
            hover "gallery/frostgallery02.png"
            action Jump ("FrostGallery02")
    text "{font=Gui/Heroes Legend.ttf}Fuck Lair{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("frostfuck01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("FrostGallery")

    if renpy.seen_image("frostanalcum02"):
        imagebutton:
            focus_mask True
            idle "gallery/frostgallery03.png" xpos 1100 ypos 100
            hover "gallery/frostgallery03.png"
            action Jump ("FrostGallery02")
    text "{font=Gui/Heroes Legend.ttf}Lair + Anal{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("frostanalcum02") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("FrostGallery")
    text "{font=Gui/Heroes Legend.ttf}Villain{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytexthero03

label FrostGalleryAnim:
call screen screenanimfrost()
screen screenanimfrost():
    modal True
    add "gallery/frostbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "frostanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "frostanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimfrost"), SetVariable ("animcount", 1), Jump ("FrostGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Emma Frost{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 45{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft8{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}32EE-20-34{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Female Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Titfucking/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Supernatural Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    add "gallery/frostanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimfrost")]
    add "gallery/frostanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimfrost")]

label FrostGallery01:
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

label FrostOfficeTitAnimxx:
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
    jump FrostTitfuckxx

stop channel1
hide frosttitfuckbackground
hide frostofficelick
hide frostofficemc03
with dissolve
show cum:
    xpos 1800 ypos 500
show licking:
    xpos 50 ypos 500
label FrostTitfuckxx:
play channel1 "sounds/wank.mp3"
call screen screentitfuckxx()
screen screentitfuckxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostOfficeLickAnimxx")
    button:
        xpos 1820
        ypos 500
        xysize(70, 60)        
        action Jump ("FrostOfficeCumxx")
    
label FrostOfficeLickAnimxx:
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
call screen screenlickfuckxx()
screen screenlickfuckxx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(240, 60)        
        action Jump ("FrostOfficeTitAnimxx")
 
label FrostOfficeCumxx:
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
mc "Well, there's a reason Ms Frost is known for her amazing beauty. She's the most beautiful woman on Earth! {w=6.0}{nw}"
hide froststrip06
hide widowoffice07
show froststrip09 at left
show widowoffice11 at centerright
with fastdissolve        
bw "So disappointing [hero]... I wonder what Captain MILF will make of that... {w=4.0}{nw}"
mc "Err, Captain MILF? Why don't we...err... leave her out of this... {w=4.0}{nw}"
hide froststrip09
hide widowoffice11
show froststrip10 at left
show widowoffice09 at centerright
with fastdissolve        
bw "You OWE me one, [name]. {w=2.0}{nw}"
ef "Oh, that's his little name? How cute... {w=3.0}{nw}"
hide widowoffice09
show widowoffice11 at centerright
with fastdissolve         
bw "Let's GO. NOW! {w=2.0}{nw}"
jump FrostGallery

label FrostGallery02:
stop channel3
scene frostfuck01
ef "You know the drill. Get into those \"easy-fuck-access\" shorts and I'll get ready for our FUCK SESSION."
mc "Err, alright."
scene frostfuck02 with dissolve
mc "Right, I'm ready. Ah, here she comes..."
play music "sounds/sexy02.mp3"
window hide
show frostfuck03 blurred:
    zoom 1.1 xoffset 0 yoffset -1000
show frostfuck04:
    xoffset -50 yoffset -1080    
show frostfuck03 blurred at scarlettfullzoombackground
show frostfuck04 at scarlettfullzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause        
ef "So, how do like my FUCK OUTFIT, [hero]?"
mc "It's telling my cock: get HARD and READY!"
window hide
hide frostfuck04
show frostfuck03 blurred:
    zoom 1.1 xoffset 0 yoffset 0
show frostfuck05:
    xoffset 50 yoffset 0    
show frostfuck03 blurred at scarlettfulldownzoombackground
show frostfuck05 at scarlettfulldownzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause
ef "And is it? Are you getting HARD and READY for me, [name]?"
mc "I sure am! It just takes a little while to fill up with blood, cos it needs a GALLON of it!"
scene frostfuck06 with dissolve
ef " A gallon of blood? Now let's see this [age]yo MONSTERCOCK up close and personal then..."
scene frostfuck07 with dissolve
ef "Doesn't look very hard... Maybe it needs my warm mouth to speed things up... Bring that dong over here..."
scene frostfuck08 with dissolve
ef "Now that's better, I can feel it ENGORGING."
mc "Ooh yeah! Fuck, that's a warm, WIDE mouth!"
scene frostfuck09 with dissolve
ef "It can get even WIDER and WARMER... If you FUCK MY MOUTH WITH IT!"
play channel1 "v032/blow03.mp3"
$ frostbedsuckslowx = False

label FrostBedSuckSlowx:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckslowvideo behind frostbedsuckfastvideo
show frostbedsuckslowvideo behind frostbedsuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckfastvideo
hide frostbedsuckpovslowvideo
with dissolve
play channel1 "v032/blow03.mp3"
$ frostbedsuckfastx = False
if frostbedsuckslowx == False:
    mc "Damn, your mouth was really made for sucking HUGE COCKS!"
    $ frostbedsuckslowx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen frostbedsuckslowx()
screen frostbedsuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostBedSuckFrontSlowx")

label FrostBedSuckFastx:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckfastvideo behind frostbedsuckslowvideo
show frostbedsuckfastvideo behind frostbedsuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckslowvideo
hide frostbedsuckpovfastvideo
with dissolve
play channel1 "sounds/blow02.mp3"
$ frostbedsuckslowx = False
if frostbedsuckfastx == False:
    mc "Let me pump my shaft in that warm throat even FASTER!"
    $ frostbedsuckfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen frostbedsuckfastx()
screen frostbedsuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostBedSuckFrontFastx")

label FrostBedSuckFrontSlowx:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckpovslowvideo behind frostbedsuckslowvideo
show frostbedsuckpovslowvideo behind frostbedsuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckslowvideo
hide frostbedsuckpovfastvideo
with dissolve
play channel1 "v032/blow03.mp3"
$ frostbedsuckfastx = False
if frostbedsuckslowx == False:
    mc "Damn, your mouth was really made for sucking HUGE COCKS!"
    $ frostbedsuckslowx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen frostbedsuckpovslowx()
screen frostbedsuckpovslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFrontFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckSlowx")

label FrostBedSuckFrontFastx:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckpovfastvideo behind frostbedsuckfastvideo
show frostbedsuckpovfastvideo behind frostbedsuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckfastvideo
hide frostbedsuckpovslowvideo
with dissolve
play channel1 "sounds/blow02.mp3"
$ frostbedsuckslowx = False
if frostbedsuckfastx == False:
    mc "Let me pump my shaft in that warm throat even FASTER!"
    $ frostbedsuckfastx = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen frostbedsuckpovfastx()
screen frostbedsuckpovfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFrontSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEndx")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFastx")

label FrostBedSuckEndx:
hide nexticon
hide slower
hide faster
hide pov
hide front

stop channel1
scene frostpostsuck01 with dissolve
play sound "sounds/lick01.ogg"
ef "Let me clean up your godly boyhood..."
mc "Be my guest. I think you missed a spot."
scene frostpostsuck02 with dissolve
play sound "sounds/lick02.mp3"
ef "There?"
mc "Yeah, oooh, that's better..."
scene frostpostsuck03 with dissolve
stop sound
ef "Time for the main dish. MY PUSSY!"
mc "And I am HUNGRY!"
scene frostpostsuck04 with dissolve
ef "The most beautiful woman in the world is YOURS today... For a short while."
mc "Good enough for me!"
scene frostpostsuck05 with dissolve
ef "You will have to take your time of course. And don't you DARE cum before I DO!"
mc "I would never entertain such a preposterous proposition."
if age >= 20:
    ef "Good, now come and make me WET. Make me DESIRE you. You and your giant BOYMEAT!"
if age >= 18 and age <= 19:
    ef "Good, now come and make me WET. Make me DESIRE you. You and your giant TEENAGE BOYMEAT!"
scene frostpostsuck06 with dissolve
play sound "sounds/moan02.mp3"
ef "Mmh, I like my boys MUSCULAR and HUNG! And you are th..."
scene frostpostsuck07 with dissolve
play sound "sounds/kiss.mp3"
ef "* kiss * You know how to NOT TALK to a woman..."
scene frostpostsuck08 with dissolve
mc "Let's get this pussy nice and wet for a MASSIVE INSERTION!"
play sound "sounds/moan02.mp3"
ef "Oooh..."                                  

label FrostRoomFuckSlowx:
hide cum
hide faster
hide slower
show frostbedfuckslowvideo behind frostbedfuckfastvideo
$ renpy.pause(1.0, hard=True)
hide frostbedfuckfastvideo with dissolve
play channel1 "sounds/womansex03.mp3"
ef "I've never been stretched like this before in my life, you're a SEX GOD!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500
call screen frostbefuckslowx()
screen frostbefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(110, 60)        
        action Jump ("FrostRoomFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostRoomFuckEndx")

label FrostRoomFuckFastx:
hide cum
hide faster
hide slower
ef "Fuck me FASTER, I NEED to CUM!"
show frostbedfuckfastvideo behind frostbedfuckslowvideo
$ renpy.pause(1.0, hard=True)
play channel1 "sounds/womansex04.mp3"
hide frostbedfuckslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen frostbefuckfastx()
screen frostbefuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("FrostRoomFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostRoomFuckEndx")

label FrostRoomFuckEndx:
hide cum
hide slower
hide faster
ef "Oh, I'm cumming, just right there, just right... THERE... AAAH!"
play sound "v032/womancum04.mp3"
scene frostfuckcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "So am I!"
window hide
with fastflash
ef "Yes, give me your YOUNG CUM!"
scene frostfuckcum02 with dissolve
play sound "sounds/womancum01.mp3"
ef "AAAH, so DEEP!"
window hide
with hpunch
mc "Fuck yeah, take that, CUM-SLUT!"
scene frostfuckcum03 with dissolve
play sound "sounds/womancum02.mp3"
ef "You're insulting me but I don't care, I just LOVE the feel of your massive shots filling me up!"
window hide
with fastflash
mc "There's more for YOU, as DEEP as I can go! EIGHTEEN INCHES DEEP!"
scene frostfuckcum04 with dissolve
play sound "v032/womancum03.mp3"
ef "AAAH!"
window hide
with hpunch
ef "There's so much sweet cum sloshing inside my belly!"
scene frostfuckcum05 with dissolve
mc "That's right! I'm gonna make you pregnant and you're going to be MINE!"
window hide
with fastflash
play sound "v032/womancum04.mp3"
ef "Dear Lord, you're a CUM-MACHINE! AAAH!"
scene frostfuckcum06 with dissolve
ef "gggg....So...Gggg-oood!"
window hide
with fastflash
mc "Here's the last of my monster load, RHAAA!"
stop channel2
stop channel1
scene frostfuckcum07 with dissolve
play sound "sounds/panting.mp3"
mc "Wow, I totally impregnated you. Again."
ef "And I totally will take an abortion pill to stop my pregnancy. Again."
mc "DAMN IT!"
if renpy.seen_image("frostanalcum02"):
    scene frostpreanal01 with dissolve
    ef "But since you've been such a VILLAINOUS Super-hero, I'm offering you my ASS as a SEX REWARD!"
    mc "Alright!"
    play sound "sounds/slurp.mp3"
    ef "After I finish cleaning myself up. I don't like being dirty at all."
    jump FrostGallery03
ef "Now go back to the gallery, I need to get cleaned up. STUD."    
stop music
jump FrostGallery

label FrostGallery03:
stop music
play music "sounds/sexy13.mp3" volume 0.5
scene frostpreanal02 with dissolve
ef "First, I want you to show me how NASTY you can be, boy! By giving me a RIMJOB!"
mc "I've done it before and I'll gladly do it again. If ANAL SEX follows, obviously."
scene frostpreanal03 with dissolve
ef "It will, it will... But my rosebud needs some prepping for your mighty pecker."
mc "Alright then..."
scene frostpreanal04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "It does look... appetizing."
ef "Of course it is, I keep it squeaky clean!"
scene frostpreanal05 with dissolve
play sound "sounds/lick01.ogg"
ef "Mmh, yeah. Stick that tongue in there and WIGGLE IT!"
window hide
play channel1 "sounds/lick02.mp3"
show frostrimjobvideo
$ renpy.pause(1.0, hard='True')
pause
stop channel1
scene frostpreanal06 with dissolve
play sound "sounds/moan02.mp3"
ef "Mmmh, you did very well, my young trainee..."
scene frostpreanal07 with dissolve
mc "Then it's time to move on to the MAIN COURSE. My [age]yo SUPER-COCK in your SUPER-TIGHT ASS!"
scene frostpreanal08 with dissolve
mc "First, let's stick the head in..."
play sound "sounds/moan01.mp3"
ef "Slowly please..."
mc "And the rest should follow..."
scene frostpreanal09 with dissolve
mc "...Like so..."
play sound "sounds/moan04.ogg"
ef "AAAH!"
scene frostpreanal10 with dissolve
mc "And now we're ready for ANAL DESTRUCTION!"
ef "Oh Lord, why did I acce..."
$ frostanalslowx = False

label FrostAnalSlowx:
$ frostanalfastx = False
window hide
show frostanalslowvideo behind frostanalfastvideo
show frostanalslowvideo behind frostanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide frostanalfastvideo
hide frostanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalslowx == False:
    $ frostanalslowx = True
    ef "You're filling me up so MUCH!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen frostanalslowx()
screen frostanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalBackSlowx")

label FrostAnalFastx:
$ frostanalslowx = False
window hide
show frostanalfastvideo behind frostanalslowvideo
show frostanalfastvideo behind frostanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide frostanalbackfastvideo
hide frostanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalfastx == False:
    $ frostanalfastx = True    
    ef "Oh God, you're gonna ass-fuck me even FASTER? AAAH!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen frostanalfastx()
screen frostanalfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalBackFastx")

label FrostAnalBackSlowx:
$ frostanalfastx = False
window hide
show frostanalbackslowvideo behind frostanalslowvideo
show frostanalbackslowvideo behind frostanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide frostanalbackfastvideo
hide frostanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalslowx == False:
    $ frostanalslowx = True
    ef "You're filling me up so MUCH!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen frostanalbackfuckslowx()
screen frostanalbackfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalBackFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalSlowx")

label FrostAnalBackFastx:
$ frostanalslowx = False
window hide
show frostanalbackfastvideo behind frostanalfastvideo
show frostanalbackfastvideo behind frostanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide frostanalfastvideo
hide frostanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
if frostanalfastx == False:
    $ frostanalfastx = True    
    ef "Oh God, you're gonna ass-fuck me even FASTER? AAAH!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen frostanalbackfuckfastx()
screen frostanalbackfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalBackSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalFastx")

label FrostAnalEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
ef "Come on, I can't take much more of this, BLOW YOUR NUTSAUCE IN MY ASS!"
mc "I could be Super-Villain and carry on but since you're my landlord, I'll..."
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge02.mp3"
scene frostanalcum01 with dissolve
mc "...give you what you want, RHAAA!!!"
window hide
with fastflash
ef "YES, FINALLY!"
scene frostanalcum02 with dissolve
mc "You want nutsauce? I'll give you NUTSAUCE, AAAH!"
window hide
with hpunch
mc "RIGHT UP YOUR INTESTINES!"
scene frostanalcum03 with dissolve
play sound "sounds/womancum01.mp3"
ef "AAAH, you're so fucking DEEP!!!!"
window hide
with fastflash
if age >= 20:
    mc "Eighteen inches of MEGACOCK DEEP!!!!"
if age >= 18 and age <= 19:
    mc "Eighteen inches of TEEN MEGACOCK DEEP!!!!"
scene frostanalcum04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan02.mp3"
ef "I'm so full... so fulll... Uuuuh..."
window hide
with vpunch
mc "Oooh god, cumming so MUCH!!!!"
scene frostanalcum05 with dissolve
mc "Hold on, I've got a few more MONSTERSHOTS TO UNLOAD! GGGUUUU!!!!"
window hide
with fastflash
ef "I can't...take it anymore... Please stop pummeling my poor ass!"
window hide
with fastflash
mc "Just a few more... There..."
stop channel1
stop channel2
scene frostanalcum06:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
play sound "sounds/moan02.mp3"
ef "Uuh... there's so much cum pouring out of my gaping ass..."
mc "Yeah, I ain't doing a rimjob anymore, that's for sure..."
stop music
stop sound
jump FrostGallery