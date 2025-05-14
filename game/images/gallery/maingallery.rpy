label MainGallery:
stop channel1
stop channel2
stop music
stop channel3
stop sound
jump MainGallery01

label MainGallery01a:
hide supergirlmaingallery
hide ivymaingallery
hide danimaingallery
hide cleomaingallery
hide natalyamaingallery
hide catwomanmaingallery
with moveoutleft

label MainGallery01b:
hide wangmaingallery
hide keenmaingallery
hide frostmaingallery
hide excellamaingallery
hide harleymaingallery
hide luthormaingallery
with moveoutright

label MainGallery01:
play channel3 "sounds/sexy07.mp3"
scene naughtygallery
show auditmaingallery at gallerypos01
show milfmaingallery at gallerypos02
show laramaingallery at gallerypos03
show powermaingallery at gallerypos04
show widowmaingallery at gallerypos05
show wondermaingallery at gallerypos06
show leftarrow at galleryposleftarrow
show rightarrow at galleryposrightarrow
with dissolve

call screen gallerymain()
screen gallerymain():
    modal True
    text "{font=Gui/Heroes Legend.ttf}Naughty Heroes{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext
    add "icons/returnicon.png"

    button:
        xpos 5
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain01"), Hide ("gallerymain"), Jump ("MainGallery05a")]
    button:
        xpos 35
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("AuditGallery")]
    button:
        xpos 345
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("MILFGallery")]
    button:
        xpos 655
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("LaraGallery")]
    button:
        xpos 965
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("PowerGallery")]
    button:
        xpos 1275
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("WidowGallery")]
    button:
        xpos 1585
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("WonderGallery")]
    button:
        xpos 1890
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain"), Jump ("MainGallery02a")]
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Hide ("gallerymain"), Jump ("LeaveMainGallery")]

return

label MainGallery02a:
hide auditmaingallery
hide milfmaingallery
hide laramaingallery
hide widowmaingallery
hide wondermaingallery
hide powermaingallery
with moveoutleft
jump MainGallery02

label MainGallery02b:
hide sawyermaingallery
hide sophiamaingallery
hide loismaingallery
hide tabithamaingallery
hide honokamaingallery
hide catherinemaingallery
with moveoutright

label MainGallery02:
scene naughtygallery
stop channel1
stop channel2
stop music
stop channel3
stop sound
play channel3 "sounds/underworld.mp3"
show wangmaingallery at gallerypos01
show keenmaingallery at gallerypos02
show frostmaingallery at gallerypos03
show excellamaingallery at gallerypos04
show harleymaingallery at gallerypos05
show luthormaingallery at gallerypos06
show leftarrow at galleryposleftarrow
show rightarrow at galleryposrightarrow
with dissolve

call screen gallerymain02()
screen gallerymain02():
    modal True
    text "{font=Gui/Heroes Legend.ttf}Naughty Villains{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext
    add "icons/returnicon.png"

    button:
        xpos 5
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain02"), Hide ("gallerymain"), Jump ("MainGallery01b")]
    button:
        xpos 35
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("WangGallery")]
    button:
        xpos 345
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("KeenGallery")]
    button:
        xpos 655
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("FrostGallery")]
    button:
        xpos 965
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("ExcellaGallery")]
    button:
        xpos 1275
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("HarleyGallery")]
    button:
        xpos 1585
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain"), Jump ("LuthorGallery")]
    button:
        xpos 1890
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain02"), Hide ("gallerymain"), Jump ("MainGallery03a")]
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Hide ("gallerymain"), Jump ("LeaveMainGallery")]

return

label MainGallery03a:
hide wangmaingallery
hide keenmaingallery
hide frostmaingallery
hide excellamaingallery
hide harleymaingallery
hide luthormaingallery
with moveoutleft
jump MainGallery03

label MainGallery03b:
hide katemaingallery
hide skullymaingallery
hide angelamaingallery
hide demonamaingallery
hide shehulkmaingallery
hide scarletmaingallery
with moveoutright

label MainGallery03:
stop channel1
stop channel2
stop music
stop channel3
stop sound
play channel3 "sounds/coolmusic.mp3"
scene naughtygallery
show sawyermaingallery at gallerypos01
show sophiamaingallery at gallerypos02
show loismaingallery at gallerypos03
show tabithamaingallery at gallerypos04
show honokamaingallery at gallerypos05
show catherinemaingallery at gallerypos06
show leftarrow at galleryposleftarrow
show rightarrow at galleryposrightarrow
with dissolve

call screen gallerymain03()
screen gallerymain03():
    modal True
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Others{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext
    button:
        xpos 35
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("SawyerGallery")]
    button:
        xpos 345
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("SophiaGallery")]
    button:
        xpos 655
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("LoisGallery")]    
    button:
        xpos 965
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("TabithaGallery")]    
    button:
        xpos 1275
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("HonokaGallery")]    
    button:
        xpos 1585
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain03"), Jump ("CatherineGallery")]
    button:
        xpos 5
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain03"), Hide ("gallerymain"), Jump ("MainGallery02b")]
    button:
        xpos 1890
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain03"), Hide ("gallerymain"), Jump ("MainGallery04a")]
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Hide ("gallerymain"), Jump ("LeaveMainGallery")]

label MainGallery04a:
hide sawyermaingallery
hide sophiamaingallery
hide loismaingallery
hide tabithamaingallery
hide honokamaingallery
hide catherinemaingallery
with moveoutleft

label MainGallery04b:
hide supergirlmaingallery
hide ivymaingallery
hide danimaingallery
hide cleomaingallery
hide natalyamaingallery
hide catwomanmaingallery
with moveoutright

label MainGallery04:
stop channel1
stop channel2
stop music
stop channel3
stop sound
play channel3 "sounds/coolmusic.mp3"
scene naughtygallery
show katemaingallery at gallerypos01
show skullymaingallery at gallerypos02
show angelamaingallery at gallerypos03
show demonamaingallery at gallerypos04
show shehulkmaingallery at gallerypos05
show scarletmaingallery at gallerypos06
show leftarrow at galleryposleftarrow
show rightarrow at galleryposrightarrow
with dissolve

call screen gallerymain04()
screen gallerymain04():
    modal True
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Others Too{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext
    button:
        xpos 5
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain04"), Hide ("gallerymain"), Jump ("MainGallery03b")]
    button:
        xpos 35
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("KateGallery")]
    button:
        xpos 345
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("SkullyGallery")]
    button:
        xpos 655
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("AngelaGallery")]
    button:
        xpos 965
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("DemonaGallery")]
    button:
        xpos 1275
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("SheHulkGallery")]
    button:
        xpos 1585
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain04"), Jump ("ScarletGallery")]
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Hide ("gallerymain"), Hide ("gallerymain"), Jump ("LeaveMainGallery")]
    button:
        xpos 1890
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain04"), Jump ("MainGallery05a")]

label MainGallery05a:
hide katemaingallery
hide skullymaingallery
hide angelamaingallery
hide demonamaingallery
hide shehulkmaingallery
hide scarletmaingallery
with moveoutleft

label MainGallery05b:
hide auditmaingallery
hide milfmaingallery
hide laramaingallery
hide powermaingallery
hide widowmaingallery
hide wondermaingallery
with moveoutright

label MainGallery05:
stop channel1
stop channel2
stop music
stop channel3
stop sound
play channel3 "sounds/coolmusic.mp3"
scene naughtygallery
show supergirlmaingallery at gallerypos01
show ivymaingallery at gallerypos02
show danimaingallery at gallerypos03
show cleomaingallery at gallerypos04
show natalyamaingallery at gallerypos05
show catwomanmaingallery at gallerypos06
show leftarrow at galleryposleftarrow
show rightarrow at galleryposrightarrow
with dissolve

call screen gallerymain05()
screen gallerymain05():
    modal True
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Yet More Others{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext
    button:
        xpos 5
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain05"), Jump ("MainGallery04b")]
    button:
        xpos 35
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("SupergirlGallery")]
    button:
        xpos 345
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("IvyGallery")]
    button:
        xpos 655
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("DaniGallery")]
    button:
        xpos 965
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("CleopatraGallery")]
    button:
        xpos 1275
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("NatalyaGallery")]
    button:
        xpos 1585
        ypos 100
        xysize(308, 900)      
        action [renpy.music.stop, Hide ("gallerymain05"), Jump ("CatwomanGallery")]
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [Hide ("gallerymain"), Jump ("LeaveMainGallery")]
    button:
        xpos 1890
        ypos 500
        xysize(25, 40)        
        action [Hide ("gallerymain04"), Jump ("MainGallery01a")]
        
label LeaveMainGallery:
stop channel3
$ _in_gallery = False
return