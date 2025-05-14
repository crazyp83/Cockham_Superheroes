label SkullyGallery:
stop channel3
play channel3 "sounds/sexfiles.mp3"
scene skullybackground
show skullymaingallery at gallerypos01 with moveinleft
call screen galleryskully()
screen galleryskully():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Agent Skully{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("galleryskully"), Jump ("MainGallery04b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("galleryskully"), Jump ("SkullyGalleryAnim")]
    
    if renpy.seen_image("alienship01"):
        imagebutton:
            focus_mask True
            idle "gallery/skullygallery01.png" xpos 400 ypos 100
            hover "gallery/skullygallery01.png"
            action Jump ("SkullyGallery01")
    text "{font=Gui/Heroes Legend.ttf}Impregnation Sex{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("alienship01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylockedhint.png"
            action Jump ("SkullyGallery01hint")

label SkullyGallery01hint:
show skullymaingallery at gallerypos01
show skullygallery01 at posgalleryhintpic
show skullygalleryhint01 at posgalleryhint
pause
hide skullygalleryhint01
hide skullygallery01
call screen galleryskully()

label SkullyGalleryAnim:
stop channel3
play channel3 "sounds/sexy09.mp3"
call screen screenanimskully()
screen screenanimskully():
    modal True
    add "gallery/skullybackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "skullyanimcos" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "skullyanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimskully"), SetVariable ("animcount", 1), Jump ("SkullyGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Agent Skully{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 38{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}34D-24-35{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Muscle Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Dangerous Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    text "{font=Gui/Heroes Legend.ttf}Lesbian Sex{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink03
    add "gallery/skullyanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimskully")]
    add "gallery/skullyanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimskully")]
            
label SkullyGallery01:
stop channel3
stop music
stop channel2
scene alienship01 with fade
play music "sounds/underworld.mp3"
ba "This earthling looks different from the other ones..."
pa "Yes, his dangling tube looks MUCH bigger than the rest of them. I wonder why that is?"
scene alienship02 with dissolve
play sound "sounds/yawn.mp3"
pa "Oh, look, he's waking up."
ba "I can't wait to probe HIS backhole."
scene alienship03 with dissolve
mc "Wh...Who are you??? And where the hell am I?"
ba "We're Xela and Xelala from planet Xeloria. You've never heard of it because we don't want you to take us to your leader."
scene alienship08 with dissolve
pa "And you're on our spaceship. You don't remember being abducted?"
mc "I... I remember now. We were investigating traumat.... Hey, where is my partner, Agent Skully? What have you done to her?"
scene alienship04 with dissolve
pa "She's over there, getting ready to become our 384th earthling test subject for the Interplanetary Impregnation Program that we have undertaken. It's so exciting!"
mc "Hey, take that thing out of her ass!"
scene alienship05 with dissolve
play sound "sounds/moan06.ogg"
ba "Why would we do that? It's the only way to repopulate our dying galaxy. And you're NEXT, strange earthling."
scene alienship06 with dissolve
play sound "sounds/moan04.ogg"
mc "What are you talking about? You can't impregnate people up their asses!"
ba "What? How come?"
scene alienship07 with dissolve
mc "It's the WRONG hole!"
scene alienship09 with dissolve
ba "That might explain why we have failed so far then, Xela."
scene alienship08 with dissolve
pa "But what other hole is there? Surely, you can't be thinking of our female..."
scene alienship07 with dissolve
ba "...frontholes? Yuck!"
mc "Yeah, I'm exactly thinking of that! That's the way it's done here!"
scene alienship08 with dissolve
pa "I don't believe you. This is anatomically completely impossible."
mc "Well, I could, like, demonstrate to you. And if I'm right, you'll have to let us go."
scene alienship09 with dissolve
ba "I suppose... We could accept your conditions. We have fallen so far behind in our endeavors, we have nothing to lose."
scene alienship08 with dissolve
pa "How will you demonstrate your impregnation technique, strange earthling?"
mc "Let my partner down and I'll stick my mighty rod so far up her, err... \"fronthole\" that her ovaries will be swimming in my sperm."
scene alienship09 with dissolve
ba "Sperm??? I heard about that strange Earth liquid, but I thought it was a legend. An intergalactic joke so to speak."
scene alienship10 with dissolve
pa "Fine, we'll let the other earthling go if you manage to impregnate her with your \"sperm\"."
ba "Oh look, his dangling tube got HARD!"
mc "Yeah, it needs to be hard for impregnation. I'll show you."
scene alienship11 with dissolve
sk "Gggg... My ass... It hurts..."
mc "Err, Agent Skully? There is only one way out of our abduction. I need to... impregnate you."
scene alienship12 with dissolve
sk "What? With that monstrous THING of yours?"
mc "It's not my fault I'm hung like a horse. It's either my cock in your pussy or they'll turn your backhole inside out with their anal probe..."
sk "Why don't you use your superpowers to get us out of here?"
scene alienship13 with dissolve
mc "We're in deep trouble. And in deep space and I can't fly."
sk " * sigh *"
mc "Don't worry, I'll try and be gentle."
sk "How can you be gentle with that humongous cock of yours?"
mc "Errr... Let me carry you so we can show them how to make babies."
scene alienship14 with dissolve
pa "What are you doing with that female alien?"
mc "Hey! YOU'RE the aliens here! And I'm just carrying her over there... So we can better show you how babies are REALLY made in a NORMAL world."
ba "Pff, this eathling thinks he's normal when his species has been rated 5 out of 5 on the Intergalatic Freakiness Scale..."
scene alienship15 with dissolve
mc "Well, I'm level 1 on the Marvels Superpowers Scale for Super-Studliness and I'll prove it to you!"
scene alienship16 with dissolve
ba "I very much doubt your hard tube will fit inside her fronth..."
scene alienship17 with dissolve
play sound "sounds/gasp.mp3"
pa "Oh, wow, it DID fit! I have never seen something stranger in my 7000 Earth years of life scouring the galaxy for our Interplanetary Impregnation Program..."
mc "And now, WATCH. As I stick it even further up her fronthole..."
window hide

label GillianFuckSlowx: 
hide cum
hide faster
hide slower
show gillianfuckslowvideo behind gillianfuckfastvideo
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex01.mp3"
hide gillianfuckfastvideo with dissolve
mc "There you go, see how far it goes?"
ba "Earthling female frontholes are so DEEP!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen gillianfuckslowx()
screen gillianfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GillianFuckFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GillianFuckEndx")

label GillianFuckFastx:
show gillianfuckfastvideo behind gillianfuckslowvideo
hide cum
hide faster
hide slower
$ renpy.pause(1.0, hard='True')
pa "This is incredible. Stick your hard tube up her frontchute FASTER!"
window hide
stop channel2
play channel2 "sounds/womansex02.mp3"
hide gillianfuckslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen gillianfuckfastx()
screen gillianfuckfastx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GillianFuckSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GillianFuckEndx")

label GillianFuckEndx:
hide cum
hide faster
hide slower
sk "I can't... feel any of my holes... Please cum, you're PULVERIZING my ovaries!"
mc "Alright, I'll flood them with some sweet cum... Right..."
scene gillianfuckcum01 with dissolve
hide gillianfuckslowvideo
hide gillianfuckfastvideo
stop channel2
play sound "sounds/boymoan05.mp3"
mc "...NOW!"
window hide
with hpunch   
play sound "sounds/womancum02.mp3"
sk "AAAAAAAAH!!!!"
scene gillianfuckcum02 with dissolve
pa "He's BLASTING that sperm liquid right up her fronthole!  I need to see this!"
window hide
with fastflash
ba "Me too, let's get closer!"
scene gillianfuckcum03 with dissolve
play sound "sounds/womancum01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "RHAAAA!"
window hide
with fastflash
play sound "sounds/gasp.mp3"
ba "By the Galactic Black Hole, the sperm is being forced out of her fronthole with such force!"
with hpunch
pa "I have never seen such a lewd display in the whole galaxy!"
scene gillianfuckcum04 with dissolve
stop channel2
play channel2 "sounds/lick03.mp3"
play sound "sounds/boymoan04.mp3"
mc "STILL PUMPING MY SEED, AAAH!"
window hide
with fastflash
stop channel2
ba "It tastes... DELICIOUS! My antennas are tingling!"
scene gillianfuckcum05 with dissolve
play channel1 "sounds/splooge01.mp3"
play sound "sounds/lick02.mp3"
pa "You're right, this taste... It is simply out of this Galaxy!!!!"
stop channel1
play sound "sounds/panting.mp3"
ba "We need to collect MORE of this wonderful earthling \"Sperm\"!"
scene gillianfuckcum06 with dissolve
play channel2 "sounds/lick01.ogg"
mc "Oh God, they're... licking my spunk from all over my shaft with their tongues..."
sk "Never mind them, just kiss me for this amazing FUCK!"
play sound "sounds/kiss.mp3"
mc "Fuck yeah, Super-Studliness in action right there!"
scene gillianfuckcum07 with dissolve
play sound "sounds/lick03.mp3"
ba "What is this \"Super-Studliness\" that he speaks of?"
play sound "sounds/lick02.mp3"
pa "I don't know but the more I swallow his viscous sperm, the more I feel the urge to have him IMPREGNATE ME!"
ba "Me too, I just want him to stick his hard tube up my backhole and give me Intergalactic babies!"
scene gillianfuckcum08 with dissolve
mc "Hey! You promised you would release us if I showed you how to impregnate female earthli... I mean, us."
sk "But that won't solve Cockham Grand Hospital's problems! They'll just get tons of female patients coming in with traumatic vaginal injuries instead!"
mc "So... Are you suggesting I should try and impregnate these aliens?"
ba "We're NOT aliens! YOU are!"
sk "Yes, it's the only way to solve this S-X files once and for all..."
scene gillianfuckcum09 with dissolve
mc "Alright then, get ready for ANAL IMPREGNATION, my big-titted alien abducters!"
pa "I want it first!"
ba "No, me me me, I beg you!"
mc "Then I'll choose... the purple alien first, then the blue one! And the blue one can suck on my balls while I impregnate the purple one up her...err... backhole."
scene gillianfuckcum10 with dissolve
ba "I'm sssooo jealous! You'd better have enough spunk left for me, earthling!"
mc "Don't worry about that, I'm a SUPER-STUD SUPERHERO!"
pa "Why does he keep talking about being super-this or super-that? This alien is very strange..."
scene gillianfuckcum11 with dissolve
mc "Are you ready to get impaled on my massive Earth schlong, purple alien?"
pa "My name is Xelala! And of course I am ready, my backhole is 15 inches deep, like all normal beings in the galaxy."
if age >= 20:
    mc "Then it will be a nice snug fit since my manhood is fifteen inches long!"
if age >= 18 and age <= 19:
    mc "Then it will be a nice snug fit since my teenage boyhood is fifteen inches long!"
pa "Good, make it go ALL THE WAY up my impregnation hole..."

label Alien02FuckSlowUpx:
window hide
hide cum
hide faster
hide slower
hide zoomicon
hide sceneicon
show alien02fuckslowvideo behind alien02fuckzoomslowvideo
show alien02fuckslowvideo behind alien02fuckfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien02fuckzoomslowvideo
hide alien02fuckfastvideo
with dissolve
pa "Mmmh, just like that... It's so THICK!"
show faster:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500     
call screen alien02fuckupslowx()
screen alien02fuckupslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckFastUpx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("Alien02FuckDownSlowx")

label Alien02FuckFastUpx:
window hide
hide cum
hide faster
hide slower
hide zoomicon
hide sceneicon
show alien02fuckfastvideo behind alien02fuckslowvideo
show alien02fuckfastvideo behind alien02fuckzoomfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex02.mp3"
hide alien02fuckzoomfastvideo
hide alien02fuckslowvideo
with dissolve
pa "That hard tube is causing so much friction inside my normal fuckhole!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show zoomicon:
     xpos 50 ypos 500     
call screen alien02fuckupfastx()
screen alien02fuckupfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckSlowUpx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien02FuckUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("Alien02FuckDownFastx")


label Alien02FuckDownSlowx:
window hide
hide cum
hide faster
hide slower
hide zoomicon
hide sceneicon
show alien02fuckzoomslowvideo behind alien02fuckslowvideo
show alien02fuckzoomslowvideo behind alien02fuckzoomfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien02fuckzoomfastvideo
hide alien02fuckslowvideo
with dissolve
ba "His nutbag is sssoo tasty..."
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen alien02fuckdownfuckslowx()
screen alien02fuckdownfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckDownFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien02FuckSlowUpx")

label Alien02FuckDownFastx:
window hide
hide cum
hide faster
hide slower
hide zoomicon
hide sceneicon
show alien02fuckzoomfastvideo behind alien02fuckzoomslowvideo
show alien02fuckzoomfastvideo behind alien02fuckfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex02.mp3"
hide alien02fuckzoomslowvideo
hide alien02fuckfastvideo
with dissolve
window hide
mc "Get my HERO schlong in there, FUCK YEAH!"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen alien02fuckdownfuckfastx()
screen alien02fuckdownfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckDownSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien02FuckUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien02FuckFastUpx")

label Alien02FuckUpEndx:
window hide
hide cum
hide faster
hide slower
hide zoomicon
hide sceneicon
ba "His balls are tightening... I think he's about to FLOOD your backhole, Xelala!"
stop channel1
scene alienfuckcum01 with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge01.mp3"
mc "FUCK, AAAAH!"
window hide
with hpunch
ba "There he goes! This earthling is really DIFFERENT from the other ones!"
scene alienfuckcum02 with dissolve
play sound "sounds/womancum01.mp3"
pa "I'm... feeling all tingly in my antennae, AAAH"
window hide
with fastflash
scene alienfuckcum03 with dissolve
mc "I'm not done with you, purple alien, RHAAA!"
window hide
with fastflash
ba "There's so much of this \"sperm\" liquid and it's so TASTY!"
scene alienfuckcum04 with dissolve
play sound "sounds/womancum02.mp3"
pa "I can feel it, my eggs are being DROWNED in his sex liquid!"
window hide
with hpunch
mc "Yeah, take that, IMPREGNATING AN ALIEN, AAAH!"
scene alienfuckcum05 with dissolve
stop channel1
stop channel2
ba "Now it's my turn! I want your HUGE earthling fuckstick up my backdoor too!"
mc "If your backdoor is as tight as your friend, I'm going to have to THRUST into with extreme FORCE!"
scene alienfuckcum06 with dissolve
pa "He just dumped me like a cheap whore!"
ba "And he's alien-handling me like a ragdoll!"
scene alienfuckcum07 with dissolve
ba "My nipples are elongating. This means I am ready to receive your impregnation liquid!"
mc "Then I'm going for it! FULL STEAM AHEAD!"

label Alien01FuckSlowUpx:
window hide
hide cum
hide faster
hide slower
hide assview
hide sceneicon
show alien01fuckslowvideo behind alien01fuckzoomslowvideo
show alien01fuckslowvideo behind alien01fuckfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien01fuckzoomslowvideo
hide alien01fuckfastvideo
with dissolve
pa "This is so nasty... You're getting ass-fucked by an earthling!"
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen alien01fuckupslowx()
screen alien01fuckupslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckFastUpx")
    button:
        xpos 50
        ypos 500
        xysize(120, 120)        
        action Jump ("Alien01FuckDownSlowx")

label Alien01FuckFastUpx:
window hide
hide cum
hide faster
hide slower
hide assview
hide sceneicon
show alien01fuckfastvideo behind alien01fuckslowvideo
show alien01fuckfastvideo behind alien01fuckzoomfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien01fuckzoomfastvideo
hide alien01fuckslowvideo
with dissolve
ba "You're thrusting your enormous pole so HARD and FAST, AAAH!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen alien01fuckupfastx()
screen alien01fuckupfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckSlowUpx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien01FuckUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 120)        
        action Jump ("Alien01FuckDownFastx")


label Alien01FuckDownSlowx:
window hide
hide cum
hide faster
hide slower
hide assview
hide sceneicon
show alien01fuckzoomslowvideo behind alien01fuckslowvideo
show alien01fuckzoomslowvideo behind alien01fuckzoomfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien01fuckzoomfastvideo
hide alien01fuckslowvideo
with dissolve
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen alien01fuckdownfuckslowx()
screen alien01fuckdownfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckDownFastx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien01FuckSlowUpx")

label Alien01FuckDownFastx:
window hide
hide cum
hide faster
hide slower
hide assview
hide sceneicon
show alien01fuckzoomfastvideo behind alien01fuckzoomslowvideo
show alien01fuckzoomfastvideo behind alien01fuckfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex01.mp3"
hide alien01fuckzoomslowvideo
hide alien01fuckfastvideo
with dissolve
window hide
pa "He's really giving it to you! I bet you LOVE every single inch!"
ba "YES, it's so good! * puff *"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen alien01fuckdownfuckfastx()
screen alien01fuckdownfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckDownSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien01FuckUpEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien01FuckFastUpx")

label Alien01FuckUpEndx:
window hide
hide cum
hide faster
hide slower
hide assview
hide sceneicon
pa "Looks like he's going to UNLEASH his sperm inside you, Xela!"
ba "I hope he has enough left to IMPREGNATE ME!"
scene alien01fuckcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
mc "Don't worry, I STILL have plenty of cum left to fill you up, AAAH!"
window hide
with fastflash
ba "Then give me your alien BABIES!!!"
scene alien01fuckcum02 with dissolve
mc "I'll give you SUPERIOR earthling ones, RHAAA!"
window hide
with hpunch
scene alien01fuckcum03 with dissolve
stop channel1
pa "That's it, give it to her good, ALL THE WAY IN!"
scene alien01fuckcum04 with dissolve
play sound "sounds/moan06.ogg"
ba "AAAH! It's so DEEP!"
play sound "sounds/splooge01.mp3"
window hide
with hpunch
mc "FFF-UUUCK!"
scene alien01fuckcum03 with dissolve
pa "And again! HARDER!"
scene alien01fuckcum04 with dissolve
play sound "sounds/moan05.mp3"
ba "OOOH!"
play sound "sounds/splooge01.mp3"
window hide
with hpunch
play channel1 "sounds/womancum01.mp3"
pa "Keep Going, earthling STUD, FILL HER UP!"
scene alien01fuckcum03 with dissolve
$ renpy.pause(0.5, hard='True')
scene alien01fuckcum04 with dissolve
play sound "sounds/splooge01.mp3"
$ renpy.pause(1.0, hard='True')
scene alien01fuckcum03 with dissolve
$ renpy.pause(0.5, hard='True')
scene alien01fuckcum04 with dissolve
play sound "sounds/splooge01.mp3"
$ renpy.pause(1.0, hard='True')
mc "Oh God, that's it, I've emptied my balls for you girls..."
stop channel1
scene alien01fuckcum05 with dissolve
play sound "sounds/panting.mp3"
ba "He totally anal-impregnated me for sure..."
scene postaliens01 with dissolve
mc "Are you going to send me back to the gallery? Please don't..."
pa "Yes, we are. You can't linger here for too long or you'll get stuck."
scene postaliens03 with dissolve
ba "Please look at the small light right here."
mc "What light?"
window hide
play sound "sounds/flash.mp3"
with fastflash
stop channel3
stop channel1
stop music
jump SkullyGallery