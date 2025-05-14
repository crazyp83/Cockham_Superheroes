label AuditGallery:
stop channel3
play channel3 "sounds/sexy02.mp3"
scene auditbackground with dissolve
show auditmaingallery at gallerypos01 with moveinleft
call screen galleryaudit()
screen galleryaudit():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Audit Girl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryaudit"), Jump ("MainGallery")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryaudit"), Jump ("AuditGalleryAnim")]
     
    if renpy.seen_image("lingeriestore03"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery01.png" xpos 400 ypos 100
            hover "gallery/auditgallery01.png"
            action Jump ("AuditGallery01")
    text "{font=Gui/Heroes Legend.ttf}Costume Store{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("lingeriestore03") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditmassage00"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery02.png" xpos 750 ypos 100
            hover "gallery/auditgallery02.png"
            action Jump ("AuditGallery02")
    text "{font=Gui/Heroes Legend.ttf}Tit Massage{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("auditmassage00") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditjacuzzi04"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery03.png" xpos 1100 ypos 100
            hover "gallery/auditgallery03.png"
            action Jump ("AuditGallery03")
    text "{font=Gui/Heroes Legend.ttf}Jacuzzi Cleaning{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext03
    if renpy.seen_image("auditjacuzzi04") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditjacuzzi41"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery04.png" xpos 1450 ypos 100
            hover "gallery/auditgallery04.png"
            action Jump ("AuditGallery04")
    text "{font=Gui/Heroes Legend.ttf}Jacuzzi Cleaning 02{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext04
    if renpy.seen_image("auditjacuzzi41") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1450 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditgirlgym01"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery05.png" xpos 400 ypos 380
            hover "gallery/auditgallery05.png"
            action Jump ("AuditGallery05")
    text "{font=Gui/Heroes Legend.ttf}Sexy Gym Training{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext05
    if renpy.seen_image("auditgirlgym01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditstretch01"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery06.png" xpos 750 ypos 380
            hover "gallery/auditgallery06.png"
            action Jump ("AuditGallery06")
    text "{font=Gui/Heroes Legend.ttf}Sexy Gym Liftup{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext06
    if renpy.seen_image("auditstretch01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

    if renpy.seen_image("auditstretch22"):
        imagebutton:
            focus_mask True
            idle "gallery/auditgallery07.png" xpos 1100 ypos 380
            hover "gallery/auditgallery07.png"
            action Jump ("AuditGallery07")
    text "{font=Gui/Heroes Legend.ttf}Gym Pounding{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext07
    if renpy.seen_image("auditstretch22") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 1100 ypos 380
            hover "gallery/gallerylocked.png"
            action Jump ("AuditGallery")

label AuditGalleryAnim:
call screen screenanimaudit()
screen screenanimaudit():
    modal True
    add "gallery/auditbackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "auditanimclo" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "auditanimcos" xalign -0.1 yalign 1.0
    if animcount == 3:
        add "auditanimlin" xalign -0.1 yalign 1.0
    if animcount == 4:
        add "auditanimbik" xalign -0.1 yalign 1.0
    if animcount == 5:
        add "auditanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimaudit"), SetVariable ("animcount", 1), Jump ("AuditGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Audit Girl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft2{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}36GGG-24-38{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Massage{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Titfuck/Paizuri{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Cunnilingus{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/auditanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimaudit")]
    add "gallery/auditanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimaudit")]
    add "gallery/auditanim03.png" xpos 1340 ypos 800
    button:
        xpos 1340
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 3), Show ("screenanimaudit")]
    add "gallery/auditanim04.png" xpos 1460 ypos 800
    button:
        xpos 1460
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 4), Show ("screenanimaudit")]
    add "gallery/auditanim05.png" xpos 1580 ypos 800
    button:
        xpos 1550
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 5), Show ("screenanimaudit")]
            
label AuditGallery01:
stop channel3
play music "sounds/storemusic.mp3"
scene lingeriestore03
ka "Please take off your... auditing garments Ms Audit Girl, so I can take your measurements."
ag "But... In front of [hero]?"
ka "He's a superhero madam, I'm sure he has seen his share of... women."
mc "I'm here to help, Kayla!"
ag "Oh. Uhm, okay. I'll get down to my... undies."
mc "That's a good girl."
scene lingeriestore04a with fade
ag "Do you think you'll be... able to find a costume for me... I have such a fat rump..."
ka "We... don't have many superheroines with your measurements, but I'm sure we'll find something."
mc "Relax, Kayla! Just let her take your measurements so you'll get a costume with a perfect fit for... those curves of yours."
if mcsenses >= 1:
    menu:
        "Use you Super-Senses to see her naked":
            scene lingeriestore04b with dissolve
            $ usedsensesauditlingerie = True
            mc "* Fuck yeah, that's better...*"
        "Don't bother.":
            jump AuditLingerieNext01x
         
label AuditLingerieNext01x:
if usedsensesauditlingerie == False:
    scene lingeriestore05a with dissolve
if usedsensesauditlingerie:
    scene lingeriestore05b with dissolve
ka "I think I have a few items in store for you to try on. Costumes that I'm sure Mr [hero] will appreciate."
mc "Ooooh, I can't wait!"
ag "Uh, alright. I... will be in the changing room."
mc "And I'll be right here waiting for you."

scene lingeriestoretrybackground blurred
show clerk02 at center:
    breathe
with dissolve
ka "This won't take a moment sir. Ms Audit Girl is trying on the first costume I found for her... size."
window hide
pause
hide clerk02
show clerk01 at center:
    breathe
with fastdissolve
ka "Still not interested in a pair of MEGA-sized superhero briefs for your great big fat young cock, sir?"
mc "Err, not at this stage, thanks. For asking."
hide clerk01
show clerk05
with fastdissolve
ka "Oh, there she comes. I will let her pose with this fine costume in front of a connoisseur such as yourself, sir."
scene lingeriestoretrybackground02 blurred
show auditcostume01a at centerright with slowmoveinright
ka "This patriotic costume is designed to remind everyone that..err... Audit Girl...here... is a true defender of the American Way of Life!"
hide auditcostume01a
show auditcostume01b
with dissolve
ag "And of the proper format of auditing documents."
mc "That's a selling point. Let's have a closer and longer examination here..."
scene lingeriestoretrybackgroundlarge blurred:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume01c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "What do you think of this costume then [name]?"
mc "I'm still pondering... Turn round."
scene lingeriestoretrybackground02 blurred
show auditcostume01d
with dissolve
ag "I don't like it so much. I can feel my fat booty just wiggling around in it, it seems too loose..."

scene lingeriestoretrybackground02 blurred:
    zoom 1.5 xpos -0.2 ypos -0.4
show auditcostume01e
with dissolve
mc "Yes, I see clearer now... Indeed... Uhm. Let's have a look at the next costume before making any rash decision."
ka "Of course sir, I will bring it at once."
scene lingeriestoretrybackground blurred
show clerk01 at center:
    breathe
with fade
ka "Are you comfortable, [hero]?"
mc "Yes, why are you asking?"
window hide
pause
hide clerk01
show clerk02 at center:
    breathe
with fastdissolve
ka "I meant comfortable down there with your enormous dong stretching that poor thong of yours? Maybe a new super-stretchy pair of..."
mc "I'm here for Audit Girl, thank you very much. Is she ready yet?"
hide clerk02
show clerk05
with fastdissolve
ka "She is now. Please think of my offer while you admire this anime-themed costume which I hope will be to your liking. It's only 699 dollars."
scene lingeriestoretrybackground02 blurred
show auditcostume02a with slowmoveinright 
mc "Now that's a VERY interesting costume..."
ag "You... really think so?"
ka "High-quality Japanese import, sir!"
hide auditcostume02a
show auditcostume02b
with dissolve
ag "It's... a bit heavy though with those armor pads... And it barely covers my butt!"
mc "Ooh, really? Turn around then, let's have a look at this serious issue..."
scene lingeriestoretrybackgroundlarge blurred:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume02c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "Can you see? My fat glutes are just spilling all over the place! It's too LEWD!"
mc "Well, let's not get carried away here, I think it's..."
scene lingeriestoretrybackground02 blurred
show auditcostume02d
with dissolve
ag "Oh no, it's making me do weird poses against my will!"
mc "What are you talking about, this is a perfectly normal anime superhero pose..."
hide auditcostume02d
show auditcostume02e
with dissolve
ag "Look, I'm so silly! Please take it off, I can't control myself!"
ka "Err, I'll help you take it off Ms Audit Girl, don't panick. I'm going to have a strong word with the Japanese manufacturer after this..."
hide auditcostume02e with slowmoveoutright
mc "What a bummer."

scene lingeriestoretrybackground blurred
show clerk01 at center:
    breathe
with dissolve
ka "She will now try the last item I found that would fit her... ample figure."
mc "Good. I don't have all evening."
window hide
pause
hide clerk01
show clerk02 at center:
    breathe
with fastdissolve
ka "We do however have MANY pairs of XXXL-sized speedos and thongs that would perfectly suit a strapping young man with a giant monsterco..."
mc "Enough, jeez! I'll come back another day to try on your \"items\", how's that?"
hide clerk02
show clerk01 at center:
    breathe
with fastdissolve
ka "That would make me very happy indeed, Mister [hero]."
hide clerk01
show clerk05
with fastdissolve
ka "Ah, Ms Audit Girl is coming out of the changing room, I will leave her costume to your exquisite appreciation."

scene lingeriestoretrybackground02 blurred
show auditcostume03a at centerright with slowmoveinright
ag "I quite like this one, what do you think?"
mc "Ooh, it certainly looks high-tech!"
hide auditcostume03a
show auditcostume03b
with dissolve
ag "I feel... more confident and fiercer in it! Like I could take on some really nasty Super-Villains who failed to file their IRS forms in time!"
mc "Err, okay."
scene lingeriestoretrybackgroundlarge blurred:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume03c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "And it's not TOO lewd. Just enough to distract my ENEMIES while I audit their books and send them to jail for 20 years per count of tax fraud!"
window hide
scene lingeriestoretrybackground02 blurred:
    zoom 2.0 xpos -0.3 ypos -0.6
show auditasswigglevideo
pause
mc "Sure, whatever you say. Keep wiggling that ass for me."
scene lingeriestoretrybackground02 blurred
show auditcostume03d
with dissolve
ag "You don't seem to believe me but this is how ALL EVIL CRIMINALS go down eventually!"
mc "In that case, I know a guy from New York, who's now moved to Florida and..."
scene lingeriestoretrybackground02 blurred:
    zoom 1.5 xpos -0.2 ypos -0.1
show auditcostume03e
with dissolve
ag "Please tell me we're going to buy it, for real!"
mc "Yes of course, we're the Cockham League of Justice and we're LOADED!"
ag "Thank you so much [name]!"
ka "I will pack it up and I will also throw in a free jacket. The Cockham League of Justice being our finest customers." 
ag "I'm sssooo happy!"
jump AuditGallery

label AuditGallery02:
stop channel3
scene auditmassage00
play channel1 "sounds/relax.mp3"
mc "Ooh, you're in that sexy lingerie again?"
scene auditmassage01 with dissolve
voice "audit/massage03"
ag "Yes... I... don't have any other lingerie set yet..."
scene auditmassage00 with dissolve
mc "Do I lie on my front like last time?"
voice "audit/massage04"
ag "Yes, I'll give you a back rub first."
scene auditmassage02 with dissolve
voice "audit/massage05"
ag "You seem very tense. Your back muscles are super-hard. I hope my hands will help relieve the tension."
play sound "sounds/boymoan.mp3"
voice "audit/massage06"
ag "Yes, relax your muscles [name]. Just like that."
scene auditmassage03 with dissolve
voice "audit/massage07"
ag "And now I'm going to use my elbow to really push on the tension points..."
scene auditmassage04 with dissolve
play sound "sounds/boymoan02.mp3"
mc "Yeah, that's good..."
scene auditmassage05 with dissolve
voice "audit/massage08"
ag "You feel the tension in that muscle right there?"
mc "Ouch, yeah, oh, it hurts but in a good way..."
voice "audit/massage09"
ag "I need you to give me your arms, I'm going to really pull on those tension points. It might hurt a bit."
if renpy.seen_image("auditmassage06"):
    menu:
        "Uh, ok.":
            jump AuditMassageFirstx
        "Err, I'd rather not. Why don't you work my front?":
            voice "audit/massage10"
            ag "Your front? You have tension there?"
            mc "Yeah, PLENTY of tension."        
            jump AuditMassageSecondx

label AuditMassageFirstx:
scene auditmassage06 with dissolve
play sound "sounds/bonecrack.mp3"
mc "Oh God, AAAH!"
scene auditmassage08 with dissolve
voice "audit/massage11"
ag "Sorry, am I hurting you?"
mc "YES! I was hoping for something more... gentle!"
scene auditmassage09 with dissolve
voice "audit/massage12"
ag "I'm really sorry I'm... going to do it another way. Which I hope you'll like."
mc "Just don't crack any more ligaments please."
scene auditmassage10 with dissolve
voice "audit/massage13"
ag "I won't, I promise... I need to do something first though so that the rub will be much more slippery..."
scene auditmassage11 with dissolve
mc "What is it?"
voice "audit/massage14"
ag "I need to pour some baby oil on my hands..."
scene auditmassage12 with dissolve
voice "audit/massage14b"
ag "And my disgustingly fat tits..."
scene auditmassage13 with dissolve
voice "audit/massage15"
ag "Now I'm all oiled up and ready to give you a maximum-surface back rub..."
mc "With your breasts???"
voice "audit/massage16"
ag "Yes. They're so oversized and heavy that they should provide the most efficient back massage."
mc "Oooh! I'm READY, Kayla!"
scene auditmassage14 with dissolve
voice "audit/massage17"
ag "Alright, let me get into position. Placing my big fat dirty tits on your muscular back..."
play channel2 "sounds/wetmassage.mp3"
window hide
scene auditbackmassagea with dissolve
voice "audit/massage18"
ag "Can you feel my huge titflesh rubbing all over your back muscles?"
mc "Yeah... Mmmh, do it faster please."
scene auditbackmassageb with dissolve
pause
voice "audit/massage19"
ag "Like that? It's so LEWD, isn't it? I feel so dirty..."
mc "And I feel GOO-OOO-D."
stop channel2
scene auditmassage16 with fade
voice "audit/massage19b"
ag "I hope you're feeling better now. And relieved from the stress of being a superhero..."
mc "I sure am, thanks a lot for this wonderful... backrub, Audit Girl!"
mc "Hopefully, next time, we can work on relieving the stress out of some other part of my body... * wink*"
voice "audit/massage20"
ag "Err, I... I'll try my best to help you."
stop channel1  
jump AuditGallery

label AuditMassageSecondx:
scene auditmassage09 with dissolve
voice "audit/massage21"
ag "I think I know what kind of LEWD massage you want. Let me get ready and then turn round..."
scene auditmassage19 with dissolve
mc "You guessed right. I need a good rub. DOWN THERE."
voice "audit/massage22"
ag "Should I help it get out of its tight confinement?"
scene auditmassage20 with dissolve
mc "Be my guest, Kayla, it's waiting to get HARDER and BIGGER so you can REALLY massage it ALL OVER!"
voice "audit/massage23"
ag "You're such a lewd boy... So young and yet so... HUNG!"
scene auditmassage21 with dissolve
voice "audit/massage24"
ag "Oh, look your great big snake is peeking out!"
mc "All the better, I'm getting HARD real quick!"
scene auditmassage22 with dissolve
if age >= 20:
    voice "audit/massage25a"
    ag "Wow, your veins are throbbing... And your behemoth is getting BIGGER so fast!"
if age >= 18 and age <= 19:
    voice "audit/massage25b"
    ag "Wow, your veins are throbbing... And your teenage behemoth is getting BIGGER so fast!"
scene auditmassage23 with dissolve
voice "audit/massage28"
ag "Still so HUGE! The perfect size for my HUGE MOUNDS!"
mc "That's what I was thinking too."
scene auditmassage24 with dissolve
play sound "sounds/kiss.mp3"
voice "audit/massage29"
ag "Let me help you get even more ROCK-HARD and SUPER-BIG for my monster boobs... By kissing the tip."
mc "Are you planning on a tit massage Kayla?"
scene auditmassage25 with dissolve
voice "audit/massage30"
ag "Isn't that what you wanted, [name]?"
mc "Fuck yeah!"
voice "audit/massage31"
ag "Just lie back and let me take care of your HUGE cock."
play channel2 "sounds/wank.mp3"
window hide

label AuditTitsAnimx:
window hide
hide cum
hide alternatetitfuck
hide titfucking
show auditmassage01video behind auditmassage02video
$ renpy.pause(1.0, hard='True')
hide auditmassage02video with dissolve
$ renpy.pause(2.0, hard='True')
mc "Damn that's good... Nice and slow between those huge tiddies..."
window hide
show alternatetitfuck:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500
call screen audittitfuckx()
screen audittitfuckx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(400, 60)        
        action Jump ("AuditTitsUpDownAnimx")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("AuditTitsCumx")

label AuditTitsUpDownAnimx:
hide cum
hide alternatetitfuck
hide titfucking
voice "audit/massage32"
ag "I think this cock needs more friction from my lewd tits!"
window hide
show auditmassage02video behind auditmassage01video
$ renpy.pause(1.0, hard='True')
window hide
hide auditmassage01video with dissolve
show titfucking:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen audittitfuckupx()
screen audittitfuckupx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(250, 60)        
        action Jump ("AuditTitsAnimx")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("AuditTitsCumx")

label AuditTitsCumx:
hide cum
hide alternatetitfuck
hide titfucking
voice "audit/massage33"
ag "Are you going to unleash all that pent-up young sperm and relieve your tension points, [name]?"
window hide
$ seentitmassage = True
$ renpy.pause(1.0, hard='True')
mc "Yeah, I think I'm close to..."
stop channel2
scene audittitcum01 with dissolve
hide auditmassage01video
hide auditmassage02video
play sound "sounds/boyorgasm01.mp3"
mc "...IT! AAAH!"
window hide
with fastflash
voice "audit/massage34"
ag "Let all that stress out!"   
scene audittitcum03 with dissolve
voice "audit/massage35"
ag "You're cumming like a FOUNTAIN! You must have been really TENSE!"
window hide
with fastflash
mc "Oh fuck, oh fuck, RHAAA!"
scene audittitcum03 with dissolve
voice "audit/massage36"
ag "You're STILL spewing all that pent-up tension? Keep PUMPING IT until it's ALL GONE!"
window hide
with fastflash
mc "I am, I am, FU-UUU-CK!"
stop sound
scene audittitcum04 with dissolve
play sound "sounds/panting.mp3"
voice "audit/massage37"
ag "There you go [name]. Did my filthy tits do a good job?"
mc "Yeah... A damn good job, Kayla... Phew..."
voice "audit/massage38"
ag "I think you need to rest for a while to recover from all that relieved stress..."
stop channel1
jump AuditGallery

label AuditGallery03:
stop channel3
scene auditjacuzzi01
mc "I'll get in first and turn the water heating up for you..."
ag "I'll... change in my bikini in the meantime then..."
play channel1 "sounds/jacuzzi.mp3"
scene auditjacuzzi02 with dissolve
ag "Is it warm yet? Can I get in?"
mc "Yeah, sure, it's the perfect temperature right now..."
play channel2 "sounds/sexy03.mp3"
scene auditjacuzzi03:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
mc "Damn fine fat booty right there..."
scene auditjacuzzi04 with dissolve
mc "Look at her, shee looks so relaxed and peaceful..."
scene auditjacuzzi05 with dissolve
mc "Wakey, wakey! Time for that thorough CLEANING!"
ag "Uh, what? Oh... Yes, you're right..."
mc "You should take your top off to clean yourself properly."
ag "I... suppose you're right."
stop channel1
scene auditjacuzzi05b with dissolve
mc "* Bingo, she's going topless... *"
scene auditjacuzzi06:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "Don't look, this is embarrassing..."
mc "Well, turn round, then you won't see me looking..."
scene auditjacuzzi07:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
pause
scene auditjacuzzi08 with dissolve
ag "I just KNOW you're still looking. At my fat ass..."
mc "If you don't want me to look at your booty, then let me help you clean your breasts. I think it's a two-man job considering their size..." 
scene auditjacuzzi09 with dissolve
ag "What..., but... I just cleaned them, I don't think they nee..."
mc "But you didn't clean your nipples properly. And there's only one proper way to do it. With my tongue! So just sit back and let me do the job..."
ag "Al...alright, if you say so..."
scene auditjacuzzi10 with dissolve
mc "Try not to move as I suck up all the dirt from those fat nipples of yours..."
play channel1 "sounds/lick03.mp3"
scene auditjacuzzi11 with dissolve
play sound "sounds/moan01.mp3"
ag "Oooh, I can feel some...milk coming out...!"
scene auditjacuzzi12 with dissolve
mc "And I can taste it... Definitely yummy warm breastmilk!"
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
scene auditjacuzzi11 with dissolve
$ renpy.pause(0.7, hard='True')
scene auditjacuzzi12 with dissolve
$ renpy.pause(1.0, hard='True')
pause
scene auditjacuzzi13 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
ag "You're... MILKING ME! AAAH!"
scene auditjacuzzi14 with dissolve
mc "Damn, there was a LOT of milk in those fat udders of yours..."
scene auditjacuzzi14 with fastflash
play sound "sounds/splooge01.mp3"
ag "Plese don't say that, I'm not a cow!"
scene auditjacuzzi14b with dissolve
play sound "sounds/moan02.mp3"
mc "Now, there's still another place that might still be dirty and needs cleaning..."
ag "Wh... What? But where?...."
mc "Turn around and I'll show you where..."
scene auditjacuzzi15 with dissolve
mc "Let me take that bikini bottom off you."
ag "But... You'll expose my filthy snatch!"
mc "And if it's filthy, then it needs cleaning..."
scene auditjacuzzi16 with dissolve
mc "Damn, these are some FAT pussylips...!"
ag "Don't say that, this is just so embarrassing..."
mc "I'm gonna have to really stick my tongue in there to clean you up properly, Kayla!"
ag "O...Okay, but try and be quick please, it feels so LEWD!"
play channel1 "sounds/lick01.ogg"
window hide
show auditmunchvideo
with dissolve
$ renpy.pause(4.0, hard='True')
play sound "sounds/moan03.mp3"
ag "OOOH, your tongue... It's so... ROUGH!"
window hide
pause
scene auditjacuzzi17 with dissolve
play sound "sounds/splooge02.mp3"
ag "AAAH!"
scene auditjacuzzi18 with dissolve
mc "Damn girl, you're squirting BIG TIME!"
play sound "sounds/moan03.mp3"
window hide
with fastflash
ag "It's your fault, you made me do it, UUUH, AAAH!"
stop sound
stop channel1
scene auditjacuzzi19 with dissolve
mc "I reckon you're squeaky clean now, Kayla..."
ag "Thanks... I guess. Can I go now? I'm clean but I feel so... dirty."
menu:
    "Yes, you can go. You won't smell bad for another five days at least I reckon.":
        stop channel2
        stop sound
        jump AuditGallery        
    "Not so fast. The back of your womb needs cleaning. From my COCK!":
        ag "You're...sure this is the correct way to do it?"
        scene auditfuckpre00 with dissolve
        mc "Abso-fucking-lutely! So turn round and stick that fat ass in the air. I'm going in!"
        pass

scene auditfuckpre01 with dissolve
mc "You'll see, once I'm done with your womb, it will be squeaky clean!"
scene auditfuckpre02 with dissolve
play sound "sounds/moan01.mp3"
ag "It's so BIG!"
mc "I'm not even halway in yet! Wait for the remaining 12 inches before you start moaning."
ag "TWELVE more inches! But..."
window hide
$ toldauditjacuzzix = True

label AuditJacuzziSlowFuckx:
window hide
show auditjacuzzislowvideo behind auditjacuzzifastvideo
show auditjacuzzislowvideo behind auditjacuzzipovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide auditjacuzzifastvideo
hide auditjacuzzipovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if toldauditjacuzzix == False:
    mc "I'll go slow at first to let you get used to my size..."
    $ toldauditjacuzzix = True
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen auditjacuzzifuckslowx()
screen auditjacuzzifuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziFastFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSideSlowx")

label AuditJacuzziFastFuckx:
window hide
show auditjacuzzifastvideo behind auditjacuzzislowvideo
show auditjacuzzifastvideo behind auditjacuzzipovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide auditjacuzzislowvideo
hide auditjacuzzipovfastvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if age >= 20:
    ag "You're fucking me so HARD with your giant cock!"
if age >= 18 and age <= 19:
    ag "You're fucking me so HARD with your giant teen cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen auditjacuzzifuckfastx()
screen auditjacuzzifuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSlowFuckx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSideFastx")

label AuditJacuzziSideSlowx:
window hide
show auditjacuzzipovslowvideo behind auditjacuzzislowvideo
show auditjacuzzipovslowvideo behind auditjacuzzipovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide auditjacuzzislowvideo
hide auditjacuzzipovfastvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen auditjacuzzisidefuckslowx()
screen auditjacuzzisidefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSideFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziSlowFuckx")

label AuditJacuzziSideFastx:
window hide
show auditjacuzzipovfastvideo behind auditjacuzzipovslowvideo
show auditjacuzzipovfastvideo behind auditjacuzzifastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide auditjacuzzifastvideo
hide auditjacuzzipovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if age >= 20:
    ag "You're fucking me so HARD with your giant cock!"
if age >= 18 and age <= 19:
    ag "You're fucking me so HARD with your giant teen cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen auditjacuzzisidefuckfastx()
screen auditjacuzzisidefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditJacuzziSideSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditJacuzziFastFuckx")

label AuditJacuzziFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "I'm gonna clean your womb, Kayla!"
ag "How???"
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
scene auditjacuzzicum01 with dissolve
hide auditjacuzzipovfastvideo
hide auditjacuzzipovslowvideo
hide auditjacuzzifastvideo
hide auditjacuzzislowvideo
mc "Like this, RHAAAA!"
play sound "sounds/boymoan05.mp3"
window hide
with hpunch
ag "With your CUM? AAAAH!"
scene auditjacuzzicum02 with dissolve
ag "You're PUMPING your seed so DEE-EEP inside my womb!"
window hide
with fastflash
mc "Yeah, that's the idea, WHITEWASHING YOU! AAAH!"
scene auditjacuzzicum03 with dissolve
mc "Fuck yeah, need to BLOW some MOARRRR!"
play channel1 "sounds/boyorgasm01.mp3"
window hide
with hpunch
ag "My poor pussy, I'm FULL already!"
scene auditjacuzzicum04 with dissolve
stop channel1
play sound "sounds/moan02.mp3"
mc "Then I'll clean your back too with my SPECIAL GEL!!!"
window hide
with fastflash
ag "But I just cleaned myself back there! UUUGGHH!"
scene auditjacuzzicum05 with dissolve
mc "This is BETTER than your soap! At least for me! RHAAA!"
window hide
with hpunch
if age >= 20:
    ag "I'm getting DRENCHED with your filthy scum!"
if age >= 18 and age <= 19:
    ag "I'm getting DRENCHED with your filthy teenage scum!"
scene auditjacuzzicum06 with dissolve
stop channel1
mc "Phew, that was damn GOOD? Audit Girl..."
ag "You're very naughty, I didn't ask for this..."
play sound "sounds/slap.mp3"
scene auditjacuzzicum07 with dissolve
mc "I told you you had to get cleaned very THOROUGHLY..."
play channel1 "sounds/moan02.mp3"
play music [ "sounds/slap.mp3", "<silence .8>"]
scene auditjacuzzisplash
$ renpy.pause(3.0, hard='True')
pause
stop music
scene auditjacuzzicum08 with dissolve
ag "Mmmh, you're still spewing small aftershots on my back... I feel so DIRTY..."
mc "Then you need to CLEAN YOURSELF again!"
scene auditjacuzzicum09 with dissolve
mc "I was thinking, my shaft is dirty. And kinda reeks of cum...."
ag "Wh... What? You need to clean it then..."
ag "No, YOU need to clean it! With your TONGUE!"
ag "But I..."
mc "No buts, the faster you clean my knob, the faster you'll be able to get back to your library and your nerdy books."
scene auditjacuzzicum10 with dissolve
play sound "sounds/lick03.mp3"
ag "Like this?"
mc "It's a good start but you have 15 full inches to clean with your tongue..."
scene auditjacuzzicum11 with dissolve
play sound "sounds/lick02.mp3"
ag "Gblike... glthat?"
if age >= 20:
    mc "Yeah, keep going... Slide that fat mouth of yours on my giant dong!"
if age >= 18 and age <= 19:
    mc "Yeah, keep going... Slide that fat mouth of yours on my giant teenage dong!"

label AuditJacuzziSuckSlowx:
hide nexticon
hide faster
hide slower
play music "sounds/blow01.mp3"
window hide
show auditsuckslowvideo behind auditsuckfastvideo
$ renpy.pause(1.0, hard='True')
hide auditsuckfastvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen auditjacuzzisuckslowx()
screen auditjacuzzisuckslowx():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditJacuzziSuckFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziSuckEndx")

label AuditJacuzziSuckFastx:
hide faster
hide slower
hide nexticon
play music "sounds/blow02.mp3"
mc "You might clean FASTER if you SUCKED FASTER!"
window hide
show auditsuckfastvideo behind auditsuckslowvideo
$ renpy.pause(1.0, hard='True')
hide auditsuckslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen auditjacuzzisuckfastx()
screen auditjacuzzisuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditJacuzziSuckSlowx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditJacuzziSuckEndx")

label AuditJacuzziSuckEndx:
hide nexticon
hide slower
hide faster
mc "Fuck yeah, that was nice, I think I'll almost all clean now..."
stop music
scene auditjacuzzicum12 with dissolve
mc "Yep, just as I predicted, ALMOST all clean. Still some spunk on my fat balls though... So get going, Kayla."
scene auditjacuzzicum13 with dissolve
play sound "sounds/lick01.ogg"
mc "Oooh, I love your warm tongue on my balls..."
scene auditjacuzzicum14 with dissolve
ag "Gglllbbb...."
play sound "sounds/lick02.mp3"
mc "Mmmh, yeah, that's it, lick all that nasty cum, SWALLOW IT TOO!"
scene auditjacuzzicum15 with dissolve
play sound "sounds/lick03.mp3"
mc "And the final dregs... Still enough to give you a mouthfull..."
scene auditjacuzzicum16 with dissolve
play sound "sounds/moan02.mp3"
ag "Your fat dong is resting on my head... But I hope it's clean enough for you to remove it now..."
mc "I'd say you did a decent job and you're fine to go. My jacuzzi is full of spunk however, I'm gonna have to change the water..."
stop channel2
stop sound
jump AuditGallery

label AuditGallery04:
stop music
stop channel3
scene auditjacuzzi41 with fade
play channel1 "sounds/jacuzzi.mp3"
mc "Come on Kayla, the water is super-warm and I can smell your stench from here."
play channel2 "sounds/sexy03.mp3"
scene auditjacuzzi42:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "I'm coming, don't rush me, I'm not used to this..."
stop channel1
scene auditjacuzzi43:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "And I don't want you to look at me like that when my swimsuit is clinging to my fat rump because of the heat..."
mc "Is it? Let me have a look then, maybe I can help you..."
scene auditjacuzzi44 with dissolve
mc "I see the problem. It's so tiny it's just being swallowed up by your crack. The best thing to do is to remove your bikini bottom altogether."
ag "You... really think so?"
mc "Absolutely. It's getting off at one stage or another anyway."
scene auditjacuzzi45:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
ag "Just don't look at my disgustingly fat butt."
mc "Not looking, not looking at all!"
scene auditjacuzzi46 with dissolve
ag "Oh no, now my bikini top is all clingy and... almost see-thru."
mc "Since I can basically see everything, you might as well take it off too."
ag "I... I guess it makes sense."
scene auditjacuzzi47:
    subpixel True
    ypos -1.0
    linear 8.0 ypos -0.0
with dissolve
$ renpy.pause(6.0, hard='True')
ag "Now I'm going to be totally naked. And all wet."
mc "It's the idea behind a steamy jacuzzi cleaning session."
scene auditjacuzzi08 with dissolve
ag "I'm cleaning myself now. So you don't say nasty things about how... I smell. For a week at least."
mc "Do you need any help?"
ag "No I don't. Let me do it myself, last time you were too naughty!"
scene auditjacuzzi48 with dissolve
mc "* God, look at that hot plump wet bod and those fat nipples... *"
scene auditjacuzzi49 with dissolve
mc "That's it, I can't take it anymore because you got me ROCK-HARD!"
ag "I... I did?"
scene auditjacuzzi50 with dissolve
mc "Yes, you're RESPONSIBLE. So I have no choice. I'm gonna pound your fat ass until my cock goes down!"
ag "My ass? But..."
scene auditjacuzzi51 with dissolve
mc "No ifs or buts, you OWE me this!"
scene auditjacuzzi52 with dissolve
ag "O...okay, but your cock... It might be TOO big!"
scene auditjacuzzi53 with dissolve
mc "There's only one way to find out!"
scene auditjacuzzi54 with dissolve
play sound "sounds/moan04.ogg"
mc "See? It fits just PERFECTLY.. Thanks to my abundant pre-cum and your FAT backdoor hole!"
$ auditupslowx = False
$ auditupfirstx = False

label AuditUpFuckSlowx:
$ auditupfastx = False
window hide
show auditupslowvideo behind auditupfastvideo
show auditupslowvideo behind auditupsideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditupfastvideo
hide auditupsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupslowx == False and auditupfirst:
    $ auditupslowx = True
    mc "That's it, just open up and let me slide my 18-incher right up your poop chute like that..."
if auditupfirst == False:
    $ auditupfirstx = True
    mc "Yeah, it slides down nice and easy..."
    ag "Uggh... it's so BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500    
call screen auditupslowx()
screen auditupslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckPOVSlowx")

label AuditUpFuckFastx:
$ auditupslowx = False
window hide
show auditupfastvideo behind auditupslowvideo
show auditupfastvideo behind auditupsidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditupsidefastvideo
hide auditupslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupfastx == False:
    $ auditupfastx = True    
    mc "It's so slimy up there, I can POUND your ass FASTER now!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500    
call screen auditupfastx()
screen auditupfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckPOVFastx")

label AuditUpFuckPOVSlowx:
$ auditupfastx = False
window hide
show auditupsideslowvideo behind auditupslowvideo
show auditupsideslowvideo behind auditupsidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditupsidefastvideo
hide auditupslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
if auditupslowx == False:
    $ auditupslowx = True
    mc "That's it, just open up and let me slide my 18-incher right up your poop chute like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditupsidefuckslowx()
screen auditupsidefuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckSlowx")

label AuditUpFuckPOVFastx:
$ auditupslowx = False
window hide
show auditupsidefastvideo behind auditupfastvideo
show auditupsidefastvideo behind auditupsideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditupfastvideo
hide auditupsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
if auditupfastx == False:
    $ auditupfastx = True    
    mc "It's so slimy up there, I can POUND your ass FASTER now!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditupsidefuckfastx()
screen auditupsidefuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditUpFuckPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditUpFuckEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditUpFuckFastx")

label AuditUpFuckEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
stop channel2
mc "That ass... It's just too good!"
scene auditfuckcum01 with dissolve
play channel2 "sounds/boyorgasm01.mp3"
mc "So good I'm gonna FLOOD IT with spunk! AAAAH!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
ag "You're going to make it all DIRTY again!"
scene auditfuckcum02 with dissolve
mc "Nonsense, a cum enema is good for CLEANING the insides of naughty girls like you, RHAAAA!"
window hide
with hpunch
ag "Then clean me WELL and DEEP [name] with your giant [age]yo SUPERDONG!"
scene auditfuckcum01
show auditfuckcum01b
with dissolve
mc "Can't stop nutting inside your fat hole!"
window hide
with fastflash
ag "You're blowing so HARD!"
scene auditfuckcum02
show auditfuckcum02b
with dissolve
mc "Not done yet, got more cream for your hungry rosebud, AAAH!"
window hide
with fastflash
ag "You're gonna make me..."
scene auditfuckcum03 with dissolve
play sound "sounds/womancum01.mp3"
ag "... AAAH, I'm cumming too! AAAH!"
window hide
with fastflash
mc "Feel the POWER of my SUPERHERO BLASTS!"
scene auditfuckcum04 with dissolve
play sound "sounds/womancum02.mp3"
mc "I'm coming so much, I think I'd better pull out..."
window hide
with fastflash
ag "Yes please, I've have too much of your heavy spunk inside me!"
scene auditfuckcum05 with dissolve
stop channel2
play sound "sounds/splooge02.mp3"
ag "Your cum is just... POURING out of my ass! It's so filthy!"
mc "Maybe, but now you're squeaky clean up there I reckon."
scene auditfuckcum06 with dissolve
mc "It's time to check more closely how clean your ass is. Keep it open while I inspect it, Kayla!"
ag "But... That's just so naughty!"
scene auditfuckcum07 with dissolve
mc "Yeah, I can't see any dirt anymore. This was a complete success."
ag "Oh good. now I can get back dressed and..."
scene auditfuckcum08 with dissolve
mc "Hang on a minute. There's ANOTHER HOLE that needs cleaning."
ag "But.. You're STILL HARD???"
scene auditfuckcum09 with dissolve
if age >= 20:
    mc "Of course I am. I'm a SEX SUPERHERO after all. So let my ROCK-HARD dong take care of your filthy poontang."
if age >= 18 and age <= 19:
    mc "Of course I am. I'm a SEX SUPERHERO after all. So let my ROCK-HARD teen dong take care of your filthy poontang."
$ auditsideslowx = False

label AuditSidePoonSlowx:
$ auditsidefastx = False
window hide
show auditsideslowvideo behind auditsidefastvideo
show auditsideslowvideo behind auditpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditsidefastvideo
hide auditpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsideslowx == False:
    $ auditsideslowx = True
    ag "Your huge pole feels so BIG inside my poor little pussy!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen auditsideslowx()
screen auditsideslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonPOVSlowx")

label AuditSidePoonFastx:
$ auditsideslowx = False
window hide
show auditsidefastvideo behind auditsideslowvideo
show auditsidefastvideo behind auditpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditpovfastvideo
hide auditsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsidefastx == False:
    $ auditsidefastx = True    
    mc "I NEED to pound FASTER! Gotta get my rocks off one more time!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen auditsidefastx()
screen auditsidefastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonPOVFastx")

label AuditSidePoonPOVSlowx:
$ auditsidefastx = False
window hide
show auditpovslowvideo behind auditsideslowvideo
show auditpovslowvideo behind auditpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide auditpovfastvideo
hide auditsideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if auditsideslowx == False:
    $ auditsideslowx = True
    ag "Your huge pole feels so BIG inside my poor little pussy!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditpovfuckslowx()
screen auditpovfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonPOVFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonSlowx")

label AuditSidePoonPOVFastx:
$ auditsideslowx = False
window hide
show auditpovfastvideo behind auditsidefastvideo
show auditpovfastvideo behind auditpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide auditsidefastvideo
hide auditpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if auditsidefastx == False:
    $ auditsidefastx = True    
    mc "I NEED to pound FASTER! Gotta get my rocks off one more time!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen auditpovfuckfastx()
screen auditpovfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("AuditSidePoonPOVSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditSidePoonEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditSidePoonFastx")

label AuditSidePoonEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "I think I'm about to clean your dirty fuck..."
scene auditfucknewcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge03.mp3"
mc "... HOLE! RHAAA!"
window hide
with fastflash
ag "I hope it works, I really need to smell nice for a week!"
scene auditfucknewcum02 with dissolve
ag "[name], you're going... TOO DEEP! AAH!"
window hide 
with hpunch
mc "You can take it Kayla, TAKE ALL MY CUM AND COCKMEAT UP THERE!"
scene auditfucknewcum03 with dissolve
ag "Your cumblasts are just so ENORMOUS! I don't know if I can..."
window hide
with fastflash
mc "Yes you CAN, you NEED to, I'm STILLLLLL CUMMMING!"
scene auditfucknewcum04 with dissolve
play sound "sounds/moan05.mp3"
ag "I'm also cumming now, I can't help myself, OOOOHHH!"
window hide
with fastflash
mc "That's good, come with me, don't ever stop, just like me, RHAAA!"
scene auditfucknewcum05 with dissolve
mc "I'm gonna whitewash your insides once and for all, AAAH!"
window hide
with fastflash
ag "Noooo, you're cumming like a firehose, I'm gonna lose my grip!"
stop channel2
scene auditfucknewcum06 with dissolve
mc "Damn, my cumshots are just BLASTING OUT of my enraged cock, RHAAA! And Kayla went FLYING across the room!"
window hide 
with vpunch
mc "Oh God, it's soo fucking GOOOODDD! NEED.. TO..."
window hide 
with fastflash
mc "..STOP AND CHECK ON HER!"
scene auditfucknewcum07 with dissolve
stop channel1
mc "I might have overdone it a bit. I didn't realize my cumshots could be so POWERFUL."
ag "Gggg..."
mc "I suppose I should carry her back to her bed in the cold library and hope for the best..."
stop music
jump AuditGallery

label AuditGallery05:
stop channel3
scene auditgirlgym01 with dissolve
play music "sounds/gymmusic.mp3"
mc "Hey Kayla, how is your new gym regimen going?"
ag "I... I'm working hard as you can see."
mc "Something else is about to work HARD around here if you get my drift."  
scene auditgirlgym02 with dissolve
ag "Eew, that's just... so CRUDE."
scene auditgirlgym03 with dissolve
mc "You're still going for pushups? I thought you gave up on that."
ag "Just a few. Before I do situps like you taught me too."
scene auditgirlgym04 with dissolve
ag "My stomach is still too... flabby."
scene auditgirlgym05 with dissolve
mc "Good, so you've been listening to me then."
ag "Well, you're the gym BUFF..."
scene auditgirlgym06 with dissolve
if age >= 20:
    mc "Damn right I am. Biggest muscle stud in town!"
if age >= 18 and age <= 19:
    mc "Damn right I am. Biggest muscle stud in town! And I'm still just a teenager."
scene auditgirlgym07 with dissolve
ag "I know. You're... incredibly muscular. And BIG."
stop music
play music "sounds/sexy10.mp3"
window hide
show auditpushupvideo with fastdissolve
pause
mc "* I could be a pervert and use my Super-Senses to see her doing push-ups in the nude. Or not. My choice. *"
call screen usepower("usesenses", "AuditGymNoNudex", "AuditGymNudex") with dissolve
label AuditGymNudex:
window hide
show auditpushupnudevideo with fastdissolve
pause
label AuditGymNoNudex:
mc "My muscles are big, but your jugs are just MASSIVE. And still getting in the way of your pushups."
ag "I can't do anything about that! Stop mentioning my disgustingly fat dangling tits please..."
scene auditgirlgym08 with dissolve
mc "So you're ready to do crunches now? I'll get the sit-up bench."
ag "I suppose so, although I was hoping to be alone so you wouldn't ask me to..."
scene auditgirlgym09 with dissolve
mc "...take your top off? Well, I'm here and I am reminding you that is is ESSENTIAL that you remove your constraining top."
scene auditgirlgym10 with dissolve
ag "I just knew you were going to say something like that..."
mc "You know me, I'm a perfectionist. I'll be back in a sec!"
scene auditgirlgym11 with fade
mc "So, there it is, just sit on it with your head at the bottom end."
scene auditgirlgym12:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
ag "Like this?"
mc "I'll position your feet under the holding bar and then you're set to go. Just slowly force yourself to sit up for starters."
window hide
show auditsitupvideo with fastdissolve
pause
mc "Nice, I think we can raise it up a notch. Once you reach the top, turn sideways to build up muscle tension in your external obliques."
ag "I'll...try. But I'm starting to sweat."
window hide
show auditsitupsweatvideo with fastdissolve
pause
mc "I think you've done enough, how do you feel?"
scene auditgirlgym13 with dissolve
ag "I don't know. I feel all sweaty... And stinky."
mc "I can corroborate that second statement. Your funbags need to get cleaned up."
scene auditgirlgym14 with dissolve
ag "And... how do you plan on doing that?"
mc "With my expert tongue obviously."
ag "I just knew you were going to say something like that..."
scene auditgirlgym15 with dissolve
play sound "sounds/lick01.ogg"
ag "This is... so lewd. And so nice at the same time, your tongue is tickling my big fat boobs!"
scene auditgirlgym16 with dissolve
play sound "sounds/moan04.ogg"
mc "That's it, enjoy my soft tongue, Kayla..."
scene auditgirlgym17 with dissolve
play sound "sounds/lick02.mp3"
mc "Now I see some sweat on your stomach, need to clean that too..."
ag "Oooh..."
scene auditgirlgym18 with dissolve
mc "Is there something else all sweaty and wet that I could take care of for you, Layla?"
ag "But... What are you doing, that's my... pussy..."
scene auditgirlgym19 with dissolve
mc "That's right, and it looks like you're leaking quite a bit, aren't you? You're getting aroused by all this..."
ag "No! I... It was just your ton..."
scene auditgirlgym20 with dissolve
play sound "sounds/moan02.mp3"
ag "...Oooooh, you're getting very naughty, [name]!"
scene auditgirlgym21 with dissolve
mc "But it looks like you like it, don't you?"
play sound "sounds/moan03.mp3"
ag "Aah, your fingers are rubbing against my clit!"
scene auditgirlgym22:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
play sound "sounds/moan02.mp3"
mc "You're getting REALLY wet down there."
scene auditgirlgym23 with dissolve
mc "Actually, SO WET that I'm going to need to CLEAN that wet muff..."
ag "But... What is someone comes in right now?"
mc "Well, you're the one who's naked, not me..."
scene auditgirlgym24 with dissolve
play sound "sounds/slurp.mp3"
ag "This is so... naughty! AAAH!"
scene auditgirlgym25 with dissolve
play channel1 "sounds/moan01.mp3"
play sound "sounds/lick02.mp3"
ag "Uhh... Oooh!"
scene auditgirlgym26 with dissolve
play channel1 "sounds/womancum01.mp3"
play sound "sounds/splooge01.mp3"
mc "Nice. You came. I had my muff lunch. I thin we're done here."
stop channel1
ag "But... You're going to leave me like that?"
mc "I strongly suggest you pull your clothes back on before you leave, Kayla..."
stop music
stop channel2
stop sound
jump AuditGallery

label AuditGallery06:
stop channel3
scene auditstretch01 with dissolve
mc "Hey Kayla, I never saw you around here before."
ag "Oh, it's you... I... I have a new gym regimen. To tone up."
mc "I have something in my thong that's toning up right now..."    
scene auditstretch02 with dissolve
ag "Eew, that's just... so CRUDE."
scene auditstretch03 with dissolve
mc "How about you show me where you're up too in your routine, I might be able to help. After all, I am a gym BUFF."
ag "I suppose so..."
scene auditstretch04 with dissolve
ag "Why are you looking at me like that?"
scene auditstretch05 with dissolve
mc "I was thinking. You need to do more than just stretch if you want to TONE UP."    
scene auditstretch06 with dissolve
ag "What do you mean?"
mc "I mean do some FEATS OF STRENGTH!"    
scene auditstretch07 with dissolve
ag "Fine, you're the gym BUFF after all..."
if age >= 20:
    mc "Damn right I am. Biggest muscle stud in town!"
if age >= 18 and age <= 19:
    mc "Damn right I am. Biggest muscle stud in town! And I'm still just a teenager."
ag "Yes I know. You're... so BIG. Everywhere... I'm big everywhere too, but it's just FAT!"
scene auditstretch08 with dissolve
mc "You see that pull-up bar? That's what you should be using. Wonder Woman uses it and she's damn fit."
ag "It looks too high for me to reach..."
mc "I'll help you up."
scene auditstretch09 with dissolve
mc " Stand on my shoulders..."
ag "Almost there..."
scene auditstretch10 with dissolve
ag "I've got it!"
mc "Good. Now use it to lift yourself up."
scene auditstretch11 with dissolve
ag "Don't go away please!"
mc "I have to. You need to do it without my help."
scene auditstretch12 with dissolve
play sound "sounds/womangroan.mp3"
ag "It's too hard... I'm just too FAT and FLABBY!"
scene auditstretch13 with dissolve
ag "Oh no! MY top stretched too much and now my dirty tits are exposed. This is so embarrassing..."    
scene auditstretch14 with dissolve
ag "Please help me down, [name]..."
mc "Hang on a minute, I need to check something..."
ag "Wh... What are you doing?"
scene auditstretch15 with dissolve
mc "Checking how fat your enormous breasts truly are... Yeah, I think I know what the problem is..."
ag "The problem is that I'm hanging from that pull-up bar with my flabby boobs hanging out!"
scene auditstretch16 with dissolve
mc "Na. That's definitely NOT a problem."
scene auditstretch17 with dissolve
play sound "sounds/womancum02.mp3"
mc "THIS is your problem. You've carrying too much titmilk around in those giant funbags of yours. It weighs you down."
ag "Oooh..."
scene auditstretch18 with dissolve
ag "I still feel... too fat."
mc "Let me check if those boobs are more squishy now."
ag "Wh...Why?"
scene auditstretch19 with dissolve
mc "Some people have accused the dev of not being able to do squishy milkjugs. So I'm here to prove them wrong."
ag "Uuuh! You're SQUISHING my boobs!"
scene auditstretch20 with dissolve
play sound "sounds/moan02.mp3"
mc "That's the idea. They seem perfectly soft and bouncy, no issue there. And there's even more titmilk splurting out when I dig my fingers into them."
play sound "sounds/splooge02.mp3"
ag "...Oooooh, you're getting very naughty, [name]!"
scene auditstretch21 with dissolve
mc "Well, you have a clean bill of health from me and the dev. Good luck with your exercises, Kayla!"
ag "What? You're leaving me like this... This is so embarrassing..."
stop music
stop channel2
stop sound
jump AuditGallery

label AuditGallery07:
stop channel3
scene auditstretch21b:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "And you'll do ANYTHING for me if I get you down won't you?"
ag "I... I suppose. As long as it's not embar..."
scene auditstretch22 with dissolve
mc "Is joining the harem of the biggest STUD in town embarrassing?"
ag "Oooh... I suppose...not..."
scene auditstretch23 with dissolve
ag "Wh...Where are you taking me?"
mc "Closer to the entrance door of the gym. Where I'll be FUCKING YOU SUPER-HARD for your harem initiation!"
scene auditstretch24 with dissolve
mc "Now take your top off for me, Kayla..."
ag "But... I... What if somebod..."
scene auditstretch25 with dissolve
play sound "sounds/ripping.mp3"
ag "My poor shorts!..."
mc "That's the thrill of it! I'm sure you'll appreciate this as an opportunity to boost your CONFIDENCE!"
scene auditstretch26 with dissolve
play sound "sounds/ripping.mp3"
mc "And in solidarity with your plight, my hardening rod is ripping my thong apart!"
ag "That's so dirty!"
scene auditstretch27:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "Yeah, but that's how you like it, cos you're a DIRTY GIRL!"
ag "I'm NOT! I'm..."
mc "Yes?"
ag "It's not fair! Your cock is making me so wet! And... dirty..."
scene auditstretch28 with dissolve
mc "Then it's time for you to open up that dirty snatch REAL WIDE for me!"
play sound "sounds/moan02.mp3"
ag "Uuuhh... Please be careful, you're so HUGE..."
scene auditstretch29:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
play sound "sounds/moan04.ogg"
if age>= 20:
    ag "AAAH, you're so BIG! But your giant boymeat feels so GOOD inside me!"
if age >= 18 and age <= 19:
    ag "AAAH, you're so BIG! But your giant teenage boymeat feels so GOOD inside me!"
mc "So, will you be a GOOD girl and join my harem?"
ag "I... Just FUCK ME PLEASE!"
scene auditgirlpregymfuck01 with dissolve
play sound "sounds/moan05.mp3"
mc "I'll take this as a YES!"
play sound "sounds/womancum02.mp3"
$ auditassslowx = True
window hide

label AuditGymFuckx:
$ auditassveryfastx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassslowx == False:
    ag "Slowly, please... You're just so BIG!"
    $ auditassslowx = True

show auditgymfuckslowvideo behind auditgymassslowvideo
show auditgymfuckslowvideo behind auditgymfuckfastvideo
show auditgymfuckslowvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassslowvideo
hide auditgymfuckfastvideo
hide auditgymfuckveryfastvideo
with dissolve
stop sound
stop channel1
play channel1 "sounds/womansex02.mp3"
with dissolve
show assview:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen auditgymsidescreenx()
screen auditgymsidescreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoomx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckFastx")

label AuditGymFuckZoomx:
$ auditassveryfastx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassslowx == False:
    ag "Slowly, please... You're just so BIG!"
    $ auditassslowx = True

show auditgymassslowvideo behind auditgymfuckslowvideo
show auditgymassslowvideo behind auditgymassfastvideo
show auditgymassslowvideo behind auditgymassveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymfuckslowvideo
hide auditgymassfastvideo
hide auditgymassveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show sceneicon:
     xpos 50 ypos 500
show faster:
     xpos 1700 ypos 500
call screen auditgymassscreenx()
screen auditgymassscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuckx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoomFastx")

label AuditGymFuckFastx:
$ auditassslowx = False
$ auditassveryfastx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
show auditgymfuckfastvideo behind auditgymassfastvideo
show auditgymfuckfastvideo behind auditgymfuckslowvideo
show auditgymfuckfastvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassfastvideo
hide auditgymfuckslowvideo
hide auditgymfuckveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex03.mp3"
show assview:
     xpos 50 ypos 500
show slower:
    xpos 1700 ypos 400    
show insanelyfast:
     xpos 1600 ypos 600
call screen auditgymsidefastscreenx()
screen auditgymsidefastscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoomFastx")
    button:
        xpos 1700
        ypos 400
        xysize(120, 60)        
        action Jump ("AuditGymFuckx")
    button:
        xpos 1600
        ypos 600
        xysize(220, 60)        
        action Jump ("AuditGymFuckFasterx")

label AuditGymFuckZoomFastx:
$ auditassslowx = False
$ auditassveryfastx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
show auditgymassfastvideo behind auditgymassslowvideo
show auditgymassfastvideo behind auditgymfuckfastvideo
show auditgymassfastvideo behind auditgymfuckveryfastvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassslowvideo
hide auditgymfuckfastvideo
hide auditgymfuckveryfastvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show sceneicon:
     xpos 50 ypos 500
show slower:
    xpos 1700 ypos 400    
show insanelyfast:
     xpos 1600 ypos 600
call screen auditgymassfastscreenx()
screen auditgymassfastscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuckFastx")
    button:
        xpos 1700
        ypos 400
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoomx")
    button:
        xpos 1600
        ypos  600
        xysize(220, 60)        
        action Jump ("AuditGymFuckZoomFasterx")
            
label AuditGymFuckFasterx:
$ auditassslowx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassveryfastx == False:
    ag "Faster... FASTER!"
    $ auditassveryfastx = True
show auditgymfuckveryfastvideo behind auditgymassveryfastvideo
show auditgymfuckveryfastvideo behind auditgymfuckfastvideo
show auditgymfuckveryfastvideo behind auditgymfuckslowvideo
$ renpy.pause(0.5, hard=True)
hide auditgymassveryfastvideo
hide auditgymfuckfastvideo
hide auditgymfuckslowvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show nexticon:
    xpos 1700 ypos 1020    
show assview:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen auditgymsideveryscreenx()
screen auditgymsideveryscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(110, 60)        
        action Jump ("AuditGymFuckZoomFasterx")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("AuditGymFuckFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditGymFuckEndx")

label AuditGymFuckZoomFasterx:    
$ auditassslowx = False
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
if auditassveryfastx == False:
    ag "Faster... FASTER!"
    $ auditassveryfastx = True
show auditgymassveryfastvideo behind auditgymfuckveryfastvideo
show auditgymassveryfastvideo behind auditgymassfastvideo
show auditgymassveryfastvideo behind auditgymassslowvideo
$ renpy.pause(0.5, hard=True)
hide auditgymfuckveryfastvideo
hide auditgymassfastvideo
hide auditgymassslowvideo
with dissolve
stop channel1
play channel1 "sounds/womansex02.mp3"
show nexticon:
    xpos 1700 ypos 1020    
show sceneicon:
     xpos 50 ypos 500
show slower:
     xpos 1700 ypos 500
call screen auditgymassveryscreenx()
screen auditgymassveryscreenx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("AuditGymFuckFasterx")
    button:
        xpos 1700
        ypos  500
        xysize(120, 60)        
        action Jump ("AuditGymFuckZoomFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("AuditGymFuckEndx")
        
label AuditGymFuckEndx:
hide zoomicon
hide slower
hide faster
hide insanelyfast
hide sceneicon
hide assview
hide nexticon
mc "Fuck... Getting close to blowing big time..."
ag "DO IT! I want to be your fat booty harem cum dumpster girl!"
scene auditgymfuckcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "Will you? RHAAA!"
window hide
with fastflash
ag "Yes! YESSSS!!!"
scene auditgymfuckcum02:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan04.ogg"
mc "Then I'll FILL YOU UP, AAAH!"
window hide
with vpunch
ag "Oh God, Y...YES!!!"
scene auditgymfuckcum03 with dissolve
play sound "sounds/splooge02.mp3"
mc "CUMMING SO MUCH!!!"
window hide
with fastflash
ag "Gggg...."
scene auditgymfuckcum04 with dissolve
ag "AAAH!!!"
window hide
with hpunch
mc "You're making me BLAST so HARD, I don't know if I can h..."
scene auditgymfuckcum05 with dissolve
stop sound
play sound "sounds/splooge03.mp3"
mc "...HOLD OFF, AAAH! FUCK, YEAH!!!"
window hide
with fastflash
ag "Eeeeek!"
scene auditgymfuckcum06:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
stop sound
ag "You FIRED me off your cum-cannon!"
window hide
with fastflash
if age >= 20:
    ag "And you're STILL spewing great big globs of SUPER-HOT SPUNK!"
if age >= 18 and age <= 19:
    ag "And you're STILL spewing great big globs of SUPER-HOT TEEN SPUNK!"
scene auditgymfuckcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Damn it, Kayla, you made me cum... so much..."
ag "How are we going to clean this mess? Anyone could walk in..."
scene auditgymfuckcum08 with dissolve
mc "Well, that's YOUR problem. You're in my harem now, remember?"
ag "But..."
mc "Tss, tss... Harem girls are SLAVES. So YOU clean this up while I go and take a shower."
stop music
stop channel2
stop sound
jump AuditGallery
