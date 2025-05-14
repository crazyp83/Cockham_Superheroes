label HonokaGallery:
stop channel3
play channel3 "sounds/asianmusic02.mp3"
scene honokabackground
show honokamaingallery at gallerypos01 with moveinleft
call screen galleryhonoka()
screen galleryhonoka():
    text "{font=Gui/Heroes Legend.ttf}Naughty Honoka{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    add "icons/returnicon.png"
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerysawyer"), Jump ("MainGallery03b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryhonoka"), Jump ("HonokaGalleryAnim")]
    
    if renpy.seen_image("honokafuckcum01"):
        imagebutton:
            focus_mask True
            idle "gallery/honokagallery01.png" xpos 400 ypos 100
            hover "gallery/honokagallery01.png"
            action Jump ("HonokaGallery01")
    text "{font=Gui/Heroes Legend.ttf}Office Sex{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("honokafuckcum01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("HonokaGallery")

label HonokaGalleryAnim:
call screen screenanimhonoka()
screen screenanimhonoka():
    modal True
    add "gallery/honokabackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "honokaanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "honokaanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimhonoka"), SetVariable ("animcount", 1), Jump ("HonokaGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Honoka{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero03
    text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft2{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}36FF-24-36{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Male Domination{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Titfucking/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    add "gallery/honokaanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimhonoka")]
    add "gallery/honokaanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimhonoka")]
            
label HonokaGallery01:
stop channel3
play music "sounds/covertmusic.mp3"
scene mayorsoffice01
show mayorsofficehonoka01
with fade
mc "Honoka is here. Just in time for her gallery SEX SCENE."
window hide
scene honokafullback blurred:
    zoom 1.0 xoffset 0 yoffset -920
show honokafull:
    zoom 1.0 xoffset 200 yoffset -1080    
show honokafullback blurred at honokafullbackzoombackground
show honokafull at honokafullup
$ renpy.pause(6.0, hard='True')
scene mayorsofficehonokaback
show honoka01
with dissolve
mc "So, you have your own gallery?"
ho "Yes sir. Just for you..."
mc "For me to make Sweee-eee-t dirty love to you, right?"
hide honoka01
show honoka02
with fastdissolve
ho "Well, I guess I haven't finished cleaning the desk. So we might as well make it absolutely FILTHY!"
mc "Yeah, filthy with my CUM!"
hide honoka02
show honoka03
with fastdissolve
ho "Hopefully, the Mayor won't come home for another couple of hours..."
mc "Unlikely in this gallery."
stop music
play music "sounds/sexy06.mp3"
scene honokaprelick01 with fade
mc "First, I'm gonna lick that dirty pussy clean. WITH MY TONGUE!"
ho "Ooh, sir, I'm sure you're gonna make me squirt in no time with your expert tongue!"
scene honokalickvideo with dissolve
play channel1 "sounds/lick01.ogg"
$ renpy.pause(2.0, hard='True')
ho "Oooh, sir... My pussy... You're..."
play sound "sounds/moan03.mp3"
window hide
$ renpy.pause(2.0, hard='True')
pause
ho "...going to make me cum soon!"
play sound "sounds/moan01.mp3"
window hide
$ renpy.pause(2.0, hard='True')
pause
scene honokalickcum01 with dissolve
stop channel1
play sound "sounds/womancum01.mp3"
ho "AAAH, you've made me squirt!"
window hide
with fastflash
mc " * Bingo! *"
scene honokalickcum02 with dissolve
play sound "sounds/moan05.mp3"
mc "Come on, squirt it all out like a good girl, and try and aim better, you're plastering my face in your juices!"
window hide
with fastflash
ho "But sir, I can't help it, AAAH!"
scene honokalickcum03 with dissolve
mc "Finally... Now you deserve a punishment for this... "
ho "But what did I do wrong, sir? You licked my pussy so good..."
mc "And now I'm gonna FUCK your pussy GOOD too!"
scene honokaprefuck01 with dissolve
mc "Yeah, that tight pussy is enticing me... TO FUCK IT!"
ho "I've been playing with my pussy all morning thinking about your cock, sir!"
scene honokaprefuck02 with dissolve
play sound "sounds/moan01.mp3"
mc "Yeah? Now get the REAL thing then!"
ho "THANK YOU SIR! THANK YOU FOR FUCKING MY TIGHT LITTLE ASIAN PUSSY WITH YOUR WHITE MONSTER BOYCOCK!"
mc "And now, here we go..."
label HonokaSlowFuckbx:
$ honokaharderx = False
play channel1 "sounds/womansex02.mp3"
scene honokafuckbackground blurred
show honokafuckslowvideo
with dissolve
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen honokafuckslowbx()
screen honokafuckslowbx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFastFuckbx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndbx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceSlowbx")

label HonokaFastFuckbx:
if honokaharderx == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharderx = True
stop channel1
play channel1 "sounds/womansex01.mp3"
scene honokafuckbackground blurred
show honokafuckfastvideo
with dissolve
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen honokafuckfastbx()
screen honokafuckfastbx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaSlowFuckbx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndbx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceFastbx")


label HonokaFaceSlowbx:
$ honokaharderx = False
play channel1 "sounds/womansex02.mp3"
scene honokafuckfacebackground blurred
show honokafaceslowvideo
with dissolve
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen honokafacefuckslowbx()
screen honokafacefuckslowbx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceFastbx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndbx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaSlowFuckbx")

label HonokaFaceFastbx:
if honokaharderx == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharderx = True
stop channel1
play channel1 "sounds/womansex01.mp3"
scene honokafuckfacebackground blurred
show honokafacefastvideo
with dissolve
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen honokafacefuckfastbx()
screen honokafacefuckfastbx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceSlowbx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndbx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFastFuckbx")

label HonokaFuckEndbx:
mc "I'm gonna fill you up with so much cum, just like last time!"
ho "I remember, there was so MUCH of it, sir!"
scene honokafuckfacebackground blurred
show honokafuckcum01
with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
ho "Oh my God, sir, you're pumping your seed so DEEP inside me!"
window hide
with fastflash
mc "And it's only just the beginning!"
scene honokafrisk05back:
    zoom 2.0 xpos -1200 ypos 0
show honokafuckcum02
with dissolve
mc "AAAH! Take that, your naughty maid!"
window hide
with fastflash
ho "No, my poor little pussy! It can't hold that much spunk!"
hide honokafuckcum02
show honokafuckcum03
with dissolve
mc "Too bad, cos I'm still PUMPING!"
window hide
with fastflash
ho "You're DESTROYING my little Asian pussy! But I LOVE IT!"
window hide
with fastflash
mc "That's a good girl, I'll cover your back in my cum now... Cos I still have LOADS left!"
stop channel1
scene honokafuckcum04 with dissolve
mc "Fuck, THAR SHE BLOWS! AAAH!"
window hide
with fastflash
ho "Sir, you will make a BIG mess and I will have to clean it up!"
window hide
with fastflash
mc "A good reason for the Mayor to keep you in that job then, RHAAA!"
scene honokafuckcum05 with dissolve
play sound "sounds/moan02.mp3"
ho "I'm CAKED in your scalding boycum, sir..."
mc "Yep, you've been SUPER-STUDDED! AGAIN... Time to leave you to your cleaning."
stop music
jump HonokaGallery