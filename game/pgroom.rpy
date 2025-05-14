label PGRoomDay:
stop music

if d10locday >= 2 and d10locday <= 4:
    jump PGRoomDay01

scene compoundpowerroomday with fade
if pgroomsneaked:
    mc "Ah, Powergirl isn't around. And I've already toured her room, so there's no point hanging around."
    jump MainTime

if pgroomsneaked == False:
    $ pgroomsneaked = True
    mc "Ah, Powergirl isn't around. Let's have a sneak around then. Cos I'm nosey."
    scene compoundpgroom02 with dissolve
    mc "She's got pictures of us... Including one of me. Zooming in on my superhero thong. Interesting."
    scene compoundpgroom03 with dissolve
    mc "And that's her bed. It's a King-sized bed too. That means there's an extra-space for ME."
    mc "But I notice there are no plants around. I'm guessing it's cos she hates them."
    mc "Well, I did my little tour. Nothing else to see here, let's go back to my room, it's getting late already."
    jump Main
    
label PGRoomDay01:
scene compoundpowerroomday
show poweryoga01
with fade
mc "Oh, Powergirl is doing some yoga. Let's join her..."
scene poweryoga02 with dissolve
voice "power/yoga01"
pg "Hi [name]! I was about to start my intense supersensory yoga session, would you like to join me?"
menu:
    "Sure, I need to acquire some Super-Senses." if mcsenses == 0:
        voice "power/yoga02"
        pg "Oh yeah, that's right, you're on level 0. You have no sense at all."
        mc "Hey!"
        jump PowerYoga
    "Sure, even if I already have Super-Senses." if mcsenses == 1:
        voice "power/yoga03"
        pg "Exercising your Super-Powers is a sure way to maintain them in top condition! Level 1 for you in that case."
        jump PowerYoga02
    "Na, I'm good. Yoga is for girls.":
        scene poweryoga03 with dissolve        
        voice "power/yoga04"
        pg "Umpf. Your \"manliness\" will be your downfall, [name]..."
        jump MainTime

label PowerYoga:
play channel1 "sounds/relax.mp3"
scene poweryoga04 with dissolve        
voice "power/yoga05"
pg "Just relax. Let all the tension in your muscles fade away..."
mc "Alright..."
voice "power/yoga06"
pg "Be aware of your surroundings..."
mc "I AM aware. Very aware."
scene poweryoga05 with dissolve        
voice "power/yoga07"
pg "You need to CONCENTRATE."
mc "Am I supposed to follow your movements?"
voice "power/yoga08"
pg "If you can."
scene poweryoga06 with dissolve
$ renpy.pause(1.0, hard=True)
mc "Hang on, you're LEVITATING???"
voice "power/yoga09"
pg "Shush, [name]. Just relax. Let the power of Super-Senses submerge you in its aura..."
scene poweryoga07 with dissolve
voice "power/yoga10"
pg "Close your eyes. See despite the blackness."
mc "You mean like some kind of night vision?"
voice "power/yoga11"
pg "I suppose..."
scene poweryoga08 with dissolve
voice "power/yoga12"
pg "Can you hear the sound of the ocean waves?"
mc "Err... Hang on, yes, it's faint but, yeah, I CAN HEAR!"
scene poweryoga09:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
voice "power/yoga13"
pg "Can you smell... err... your own sweat? I sure can, not sure if it's thanks to my Super-Senses or not..."
mc "Oh yeah, suddenly, I can smell myself. Damn, I smell good."
voice "power/yoga14"
pg "Yeah, good enough for a shower after this, [name]."
if mcsenses == 0:
    call SensesPlus from _call_SensesPlus
mc "I think that did it! I can feel the Super-Power of Super-Senses flowing through my veins!"
scene poweryoga10a with dissolve
voice "power/yoga15"
pg "Really? Then concentrate and see if you can use your Super-Senses to be Super-Aware of your surroundings..." 
label PowerYogaTrySenses:
call screen usepower("usesenses", "PowerYogaNoSenses", "PowerYogaSenses") with dissolve

label PowerYogaNoSenses:
mc "Err, no. I failed miserably."
voice "power/yoga16"
pg "Didn't click fast enough? Have another try then."
jump PowerYogaTrySenses

label PowerYogaSenses:
scene poweryoga10b with dissolve
mc "Ooh yeah, I'm Super-Aware... This superpower is Super-COOL!"
scene poweryoga11b with dissolve
voice "power/yoga17"
pg "Let's finish off with a bit of stretching to clear our minds then..."
mc "I don't think I want to clear my mind right now..."
scene poweryoga12b with dissolve
voice "power/yoga18"
pg "Why not, [name]?"
mc "Err.... I'll clear my mind once I go back to my room. Thanks for teaching me Super-Senses, Kara!"
stop channel1
jump Main

label PowerYoga02:
play channel1 "sounds/relax.mp3"
scene poweryoga11 with dissolve
voice "power/yoga20"
pg "Let's start off with a bit of stretching to clear our minds..."
mc "Alright, although I don't think I'm as flexible as you are. Due to my massive muscles."
scene poweryoga12 with dissolve
voice "power/yoga21"
pg "Yes, you are indeed VERY muscular, [name]..."    
scene poweryoga04 with dissolve        
voice "power/yoga22"
pg "And now let us relax. Let all the tension in your muscles fade away..."
mc "Alright..."
voice "power/yoga06"
pg "Be aware of your surroundings..."
mc "I AM aware. Very aware. I have Super-Senses now, remember?"
scene poweryoga05 with dissolve        
voice "power/yoga23"
pg "Stop talking and CONCENTRATE."
mc "Sure, sis, sorry."
scene poweryoga06 with dissolve
$ renpy.pause(1.0, hard=True)
mc "I don't think I can levitate like you do though..."
scene poweryoga06b with dissolve
mc "Hang on, I'm LEVITATING TOO???"
voice "power/yoga24"
pg "And you don't even have Super-Flight. This is all thanks to Super-Senses."
mc "Can I fly then?"
voice "power/yoga25"
pg "No you can't. You can only levitate as long as you keep your concentration up and you stay AWARE."
scene poweryoga09:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
voice "power/yoga26"
pg "Now reach up, as if you wanted to fly, reach up to another realm of SUPERSENSORY experience."
mc "I can feel it, my senses are super-sensitive..."
scene poweryoga10a with dissolve
voice "power/yoga27"
pg "That's exactly where I wanted you to be."
mc "Thanks, sis, this was an amazing experience..."
voice "power/yoga28"
pg "You're welcome, [name]..."
stop channel1
jump Main

label PGRoomNight:
stop music
if seensupergirl and seensuperpowergirl == False:
    jump PowergirlSupergirl
if d10locnight >= 6:
    if d10locnightpgroom == 1:
        jump PGRoomNight01
    if d10locnightpgroom == 2:
        jump PGRoomNight02

scene compoundpowerroomnight with fade
mc "Powergirl isn't there. She's got a nice rooom though."
jump MainTime

label PGRoomNight01:
play music "sounds/sexy06.mp3"
scene compoundpowerroomnight with fade
if helpedpowergirl == False and unlockedpowergirl:
    show powerhot00 at centerleft with moveinright
    show powerhot00 at centerleft:
        breathe
    with fastdissolve
    pg "Well, look which naughty boy has just come into my room in the evening..."
    mc "I didn't think I was being naughty."
    hide powerhot00
    show powerhot00b
    with fastdissolve
    if toldunlockedpowergirl:        
        pg "You probably noticed I was wearing that lovely lingerie set... So get on the bed and get ready for some HOT SEX with your landlady's daughter!"
    if toldunlockedpowergirl == False:
        $ toldunlockedpowergirl = True
        pg "You're a SEX superhero, you're a DIRTY boy to begin with anyway. But since you saved me at the pool the other day..."
        mc "You're agreeing to have sex with me?"
        hide powerhot00b
        show powerhot00c
        with fastdissolve
        pg "That's why I'm wearing that lovely lingerie set... So get on the bed and get ready for some HOT SEX with your landlady's daughter!"
        $ powerhotlingerie = True
    jump PowerRoomHot

if helpedpowergirl and mclevel02:
    show powerhot00 at centerleft with moveinright
    show powerhot00 at centerleft:
        breathe
    with fastdissolve
    pg "Well, look which naughty boy has just come into my room in the evening..."
    mc "I didn't think I was being naughty."
    hide powerhot00
    show powerhot00b
    with fastdissolve
    pg "You're a SEX superhero, you're a DIRTY boy to begin with anyway. But you're in luck, I'm also feeling NAUGHTY tonight..."
    mc "Ooh yeah!"
    hide powerhot00b
    show powerhot00c
    with fastdissolve
    if powerhotlingerie:
        pg "You probably noticed I was wearing that lovely lingerie set... So get on the bed and get ready for some HOT SEX with your landlady's daughter!"
    if powerhotlingerie == False:
        pg "I want to show you a new lingerie set. One that will make this a night to REMEMBER!"
        $ powerhotlingerie = True
    jump PowerRoomHot

show powerpj03 at centerleft with moveinright
show powerpj03 at centerleft:
    breathe
pg "What a lovely surprise. Usually, nobody comes into my room in the evening."
if powerlingerie == False and mission03end and mclevel02 == False:
    hide powerpj03
    show powerpj05
    with fastdissolve
    pg "And you were just the boy I was looking for!"
    mc "Why is that?"
    hide powerpj05
    show powerpj02
    with fastdissolve
    pg "I was just going through my dresser, I need to pick a lingerie set for a photo session with Lois Pane. Care to help me pick the right one?"
    mc "Ooh yeah!"
    hide powerpj02
    show powerpj04
    with fastdissolve
    pg "I thought you might. Go and sit on the bed and I'll come round with some HOT outfits for you, [name]..."
    $ powerlingerie = True
    jump PowerLingerie
    
label PGRoomDialogues:
menu:
    "Oh, so you don't have... anyone then?" if pgspeak05 == False:
        $ pgspeak05 = True
        hide powerpj03
        show powerpj01 at centerleft
        with fastdissolve
        pg "No... I think men are scared of me..."
        mc "I'm not scared of you."
        hide powerpj01
        show powerpj05 at centerleft
        with fastdissolve
        pg "And that means we could be a match in your eyes?"
        mc "I would say so."
        hide powerpj05
        show powerpj04 at centerleft
        with fastdissolve
        pg "You'll have to seduce me first. I'm not an easy girl... * wink*"
        hide powerpj04
        show powerpj03 at centerleft
        with fastdissolve 
        show powerpj03 at centerleft:
            breathe        
        jump PGRoomDialogues
    "Can you fly without your cape?":
        hide powerpj03
        show powerpj01 at centerleft
        with fastdissolve
        pg "Obviously not. How would I fly without a cape?"
        mc "Yeah, makes sense. So, if I had a cape, I would be able to fly?"
        hide powerpj01
        show powerpj05 at centerleft
        with fastdissolve
        pg "I suppose. I'm not sure. I've always had a cape, even when I was a baby, so..."
        hide powerpj05
        show powerpj03 at centerleft
        with fastdissolve       
        show powerpj03 at centerleft:
            breathe
        jump PGRoomDialogues
    "Do you remember when we used to have pillows fights when we were kids?":
        hide powerpj03
        show powerpj05 at centerleft
        with fastdissolve
        pg "You mean landlady's daughter-landboy pillow fights?"
        mc "Yeah, those ones."
        hide powerpj05
        show powerpj02 at centerleft
        with fastdissolve
        pg "Yeah, I remember. You want to have a pillow fight with me, [name]?"
        mc "Yes I do."
        hide powerpj02
        show powerpj04 at centerleft
        with fastdissolve
        pg "Not tonight... Maybe in a later version, I'm off to bed."
        mc "Oh. Goodnight then, Kara."
        jump Main
    "You're so beautiful, I would like to offer you some flowers.":
        hide powerpj03
        show powerpj01 at centerleft
        with fastdissolve
        pg "Flowers? HOW DARE YOU!"
        mc "What? They're lovely, I picked th..."
        hide powerpj01
        show powerpj06 at centerleft
        with fastdissolve
        pg "AAARGH, I HATE YOU, I HATE YOU! I HATE FLOWERS, GET OUT OF MY ROOM!"
        mc "* Wow, that didn't go down well. Then again, if I had bothered reading her dossier, I might have known this would happen. *"
        jump Main
    "I'm done.":
        hide powerpj03
        show powerpj02 at centerleft
        with fastdissolve
        pg "Then go back to your room and sleep, you're too young to be staying up so late, [name]."
        mc "Hey, I'm a superhero! Captain MILF gave me permission to stay up late to fight SEX CRIME!"
        hide powerpj02
        show powerpj05 at centerleft
        with fastdissolve
        pg "So why are you in my room? You were hoping to find some sex crime here?"
        hide powerpj05
        show powerpj01 at centerleft
        with fastdissolve
        pg "Or maybe you were thinking of COMMITTING some sex crime?..."
        mc "Err. Okay, I'll go back to my room. Goodnight Kara. Or Karen."
        hide powerpj01
        show powerpj03 at centerleft
        with fastdissolve
        pg "I prefer Kara. Good night [name]!"
        jump Main

label PGRoomNight02:
scene compoundpowerroomnight
show compoundpowerroomnightwindows
with fade
mc "Well, where is she?"
window hide
play sound "sounds/powergirl.mp3"
hide compoundpowerroomnightwindows
show powerenterroom01
with dissolve
pause
hide powerenterroom01
show powerenterroom02
with dissolve
mc "Is it a plane, is it a bird?"
hide powerenterroom02
show powerenterroom03
with dissolve
mc "No, It's Powergirl!"
hide powerenterroom03
show powerroomcostume01 at centerleft
with dissolve
stop sound
pg "And a perfect landing. Which doesn't ALWAYS happen."
hide powerroomcostume01
show powerroomcostume02 at centerleft
with dissolve
pg "Were you waiting for me to come back, [name]?"
mc "Yes indeed. Fabulous landing by the way."
label PGRoomDialogues02:
menu:
    "Who were you fighting on your exciting mission?":
        hide powerroomcostume02
        show powerroomcostume03 at centerleft
        with dissolve
        pg "Actually, I went to get some groceries for Captain MILF.... We're out of milk."
        mc "I see. Very exciting stuff."
        hide powerroomcostume03
        show powerroomcostume04 at centerleft
        with dissolve
        pg "We need to eat, you know?"
        mc "I didn't know that superheroes needed to eat but now that you mention it, it makes perfect physiological sense."
        hide powerroomcostume04
        show powerroomcostume02 at centerleft
        with dissolve
        jump PGRoomDialogues02
    "I would like to fly with you, Kara..." if mission02end and locarkham == False:
        hide powerroomcostume02
        show powerroomcostume03 at centerleft
        with dissolve
        pg "Why not, we could indeed fly together. Well, you on my back obviously since you can't fly."
        mc "And hopefully, you won't drop me."
        hide powerroomcostume03
        show powerroomcostume02 at centerleft
        with dissolve
        pg "I am level 2 in Super-Flight, that should be enough. You don't look THAT heavy."
        mc "Still, over 200 pounds of RAW MUSCLES."
        hide powerroomcostume02
        show powerroomcostume04 at centerleft
        with dissolve
        pg "200 pounds? I didn't realize you were... so ripped!"
        mc "You're pretty ripped yourself..."
        hide powerroomcostume04
        show powerroomcostume01 at centerleft
        with dissolve
        pg "That's right, look at these biceps when I flex..."
        mc "NICE! Can't wait to see them up close and personal... * wink * From your back."
        hide powerroomcostume01
        show powerroomcostume02 at centerleft
        with dissolve
        pg "Alright, let's GO, [name]!"
        jump PowerFlying
    "I would like to fly with you one day, Kara..." if mission02end == False:
        hide powerroomcostume02
        show powerroomcostume03 at centerleft
        with dissolve
        pg "Maybe one day when I'm not too busy, we can fly together. Well, you on my back obviously since you can't fly."
        mc "And hopefully, you won't drop me."
        hide powerroomcostume03
        show powerroomcostume02 at centerleft
        with dissolve
        pg "I am level 2 in Super-Flight, that should be enough. You don't look THAT heavy."
        mc "Still, over 200 pounds of RAW MUSCLES."
        hide powerroomcostume02
        show powerroomcostume04 at centerleft
        with dissolve
        pg "200 pounds? I didn't realize you were... so ripped!"
        mc "You're pretty ripped yourself..."
        hide powerroomcostume04
        show powerroomcostume01 at centerleft
        with dissolve
        pg "That's right, look at these biceps when I flex..."
        mc "NICE! Can't wait to see them up close and personal... * wink *"
        hide powerroomcostume01
        show powerroomcostume02 at centerleft
        with dissolve
        jump PGRoomDialogues02    
    "I'm done here.":
        hide powerroomcostume02
        show powerroomcostume03 at centerleft
        with dissolve
        pg "Well, thank you for dropping by and guarding my room while I was grocery shopping."
        hide powerroomcostume03
        show powerroomcostume04 at centerleft
        pg "Goodnight, [name]!"
        jump Main

label PowerFlying:
stop music
play channel2 "sounds/coldwind.mp3"
show cockham01:
    subpixel True
    zoom 1.2 xpos 0.0 ypos -0.15
    linear 10.0 xpos -0.1 ypos 0.0
show powerflight01
with fade
pg "How are you enjoying this flight, [name]?"
mc "It's awesome, Kara! Let's fly DEEP into the city!"
pg "Hang on tight then, I'm going to fly at SUPER-SPEED!"
show nightsky:
    subpixel True
    zoom 1.5 xpos 0.0 ypos 0.0
    linear 10.0 xpos -0.2 ypos -0.2
show powerflight02:
    subpixel True
    xpos -0.1 ypos 0.0
    linear 10.0 xpos 0.0 ypos 0.05
with dissolve
mc "Err, you're going a bit fast there, Kara... Please slow down!"
pg "Are you scared, [name]?"
mc "NO! I'm a FEARLESS SUPERHERO! But still..."
pg "Alright, I'll slow down. For YOU."
scene powerflight03 with dissolve
mc "What's that building over there?"
pg "I think it's Arkham's Asylum. I'll do a fly-by..."
show arkhamabove:
    subpixel True
    xpos 0.0 ypos -0.15
    linear 10.0 xpos -0.1 ypos 0.0
show powerflight04
with dissolve
play channel1 "sounds/nightsounds.mp3"
mc "What a spooky place..."
window hide
play sound "sounds/skill.mp3"
show locationarkham at poslocation
$ renpy.pause(0.5, hard=True)
pause
$ locarkham = True
pg "Time to head back to the compound, I'm feeling... a bit tired, carrying over 200lbs of MUSCLE on my back!"
jump Main

label PowerLingerie:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy09.mp3"
scene powerlingeriebackground01
show powerlingerie01:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerlingerie01 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
pg "Here's the first outfit. So what do you think?"
mc "Turn round so I can have a better look, Kara."
hide powerlingerie01
show powerlingerie02
with dissolve
pg "Like that?"
mc "Yeah, like that. It's nice, very nice. But I need an even CLOSER look. So let me zoom in with my Super-Eyes."
pg "You don't have Super-Eyes."
mc "Ok, fine. But let me zoom in anyway. By squinting my normal eyes."
window hide
hide powerlingerie02
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerlingerie03:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 at widowfullbackzoombackground
show powerlingerie03 at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "And the back now. The ass... I mean, the back is important too."
window hide
hide powerlingerie03
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerlingerie04:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerlingerie04 at powerfulldown
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Is the ASS to your liking, [name]?"
mc "Ooh yeah. But the babydoll hides it too much."
scene powerlingeriebackground01 blurred:
    zoom 1.5 yoffset -400
show powerlingerie05
with dissolve
pg "I'm surprised you haven't used your Super-Senses to see right through it yet..."
mc "Hey! I'm being PROFESSIONAL here. Readers of the Cockham Planet don't have superpowers..."
scene powerlingeriebackground01 blurred
show powerlingerie06
with dissolve
pg "Alright, Mr Professional. What about the front, what do you have to say about THAT?"
mc "Your tits are huge."
hide powerlingerie06
show powerlingerie07
with dissolve
pg "I'm talking about the lingerie set I'm wearing!"
mc "Ah, sorry, I was distracted. By your HUGE tits. Though I wish they would be even BIGGER."
hide powerlingerie07
show powerlingerie08
with dissolve
pg "I don't. They're quite heavy to carry around as it is."
mc "Oh well, you have Super-Strength so it shouldn't be too much trouble."
hide powerlingerie08
show powerlingerie07
with dissolve
pg "Let's change the subject, please. And my outfit. I'll be back with another one I was thinking of maybe wearing for the photo-session."
window hide
show powerlingerie07 at moveleftoutslow
$ renpy.pause(1.2, hard='True')      

scene powerlingeriebackground01
show powerlingerie11:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerlingerie11 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
pg "And now for something a bit more NAUGHTY!"
mc "Ooh! I wanna see MORE!"
hide powerlingerie11
show powerlingerie12
with dissolve
pg "Like that?"
mc "Oh God, I think you're going to give readers a HEART ATTACK!"
pg "Mmh, that's not good. We need them to finance the compound through these regular photo-sessions."
mc "It was just a figure of speech. Let me squint my eyes again, which is probably what the readers will do too."
window hide
hide powerlingerie12
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerlingerie13:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 at widowfullbackzoombackground
show powerlingerie13 at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "Now we're talking! What about the... you know. Booty?"
pg "My ass you mean?"
window hide
hide powerlingerie13
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerlingerie14:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerlingerie14 at powerfulldown
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Is it BETTER than the last one?"
mc "Definitely. I don't even need to use Super-Senses to see your fine glutes."
scene powerlingeriebackground01 blurred:
    zoom 1.5 yoffset -530
show powerlingerie15
with dissolve
pg "You don't think it's TOO naughty for the Cockham Planet readers?"
mc "If you show your tits like that, it might be."
hide powerlingerie15
show powerlingerie16
with dissolve
pg "I'm showing them to YOU. Exclusively. You have a problem with that?"
mc "Not at all. Not at all."
scene powerlingerie21 with dissolve
pg "I can see that. You're sporting a massive hardon in front of your landlady's daughter..."
mc "Well, you did show me your tits, so you're responsible."
scene powerlingerie22 with dissolve
pg "So I'm responsible for that great big drooling tentpole?"
play sound "sounds/boymoan.mp3"
pg "What's the matter? You can't take a little bit of TEASING?"
scene powerlingerie23 with dissolve
play sound "sounds/lick02.mp3"
pg "I think you should learn to control your libido, [name]..."
play sound "sounds/boymoan02.mp3"
mc "Are you... going to blow me?"
scene powerlingerie24 with dissolve
pg "No. That would make you cum TOO EASILY... Like right now, you're already spurting filthy pre-cum all over the place..."
mc "So what are you going to do, Kara? I NEED some relief!"
scene powerlingerie25 with dissolve
pg "I'll provide relief. with my FEET!"
scene powerlingerie26 with dissolve
pg "Look at you. I simply wanted your opinion about which lingerie set I should wear and you ended up sporting a great big erection right in front of your landlady's daughter!"
play channel1 "sounds/wank.mp3"
window hide

label PowerFootSlowFuck:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootjobslowvideo behind powerfootjobfastvideo
show powerfootjobslowvideo behind powerfootsceneslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsceneslowvideo
hide powerfootjobfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerfoottalkfast = False
if powerfoottalkslow == False:
    pg "You're just such a DIRTY landboy!"
    $ powerfoottalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootpovslow()
screen powerfootpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFastFuck")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootFaceSlow")

label PowerFootFastFuck:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootjobfastvideo behind powerfootjobslowvideo
show powerfootjobfastvideo behind powerfootscenefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootjobslowvideo
hide powerfootscenefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerfoottalkslow = False
if powerfoottalkfast == False:
    pg "You have no self-control. As soon as you see a scantily-clad woman, you get HARD as a rock. Even if it's your landlady's DAUGHTER!"
    $ powerfoottalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootpovfast()
screen powerfootpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFaceFast")

label PowerFootFaceSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootsceneslowvideo behind powerfootjobslowvideo
show powerfootsceneslowvideo behind powerfootscenefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootjobslowvideo
hide powerfootscenefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerfoottalkfast = False
if powerfoottalkslow == False:
    pg "You're just such a DIRTY landboy!"
    $ powerfoottalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerfootsceneslow()
screen powerfootsceneslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFaceFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSlowFuck")

label PowerFootFaceFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerfootscenefastvideo behind powerfootjobfastvideo
show powerfootscenefastvideo behind powerfootsceneslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsceneslowvideo
hide powerfootjobfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerfoottalkslow = False
if powerfoottalkfast == False:
    pg "You have no self-control. As soon as you see a scantily-clad woman, you get HARD as a rock. Even if it's your landlady's DAUGHTER!"
    $ powerfoottalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show pov:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerfootscenefast()
screen powerfootscenefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootFaceSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootFastFuck")

label PowerFootFuckEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
pg "Such a filthy boy... I bet you're churning up a MONSTERLOAD for your landlady's daughter, aren't you?"
mc "Oh my God, Kara, you're teasing me so much..."
scene powerlingeriecum01 with dissolve
hide powerfootjobslowvideo
hide powerfootjobfastvideo
hide powerfootsceneslowvideo
hide powerfootscenefastvideo
stop channel1
stop channel2
play channel1 "sounds/boyorgasm01.mp3"
mc "... I NEED TO COME, AAAAHHHH!"
window hide
with fastflash
pg "Oooh, I can see that!"
scene powerlingeriecum02 with dissolve
pg "Come on, [name], BLAST IT OUT!"
window hide
with fastflash
pg "I want you to REACH THE CEILING WITH YOUR NEXT SHOT!"
if inventorylustring:
    play sound "sounds/magic.mp3"
    scene powerlingeriecum03a with dissolve    
    mc "RHAAAA! MAXIMUM CUMSHOT POWER!"
    window hide
    with hpunch
    play sound "sounds/splat.ogg"
    pg "Oh my god, your cumshots are sssooo POWERFUL!"
    window hide 
    with fastflash
    play sound "sounds/splat.ogg"
    mc "Your feet... I can't stop CU-UUU-MMMING!"
    scene powerlingeriecum04
    pg "You're cumming sssooo MUCH, [name]! Does your landlady's daughter excite you THAT MUCH?"
    window hide
    with fastflash
    stop channel1
    play sound "sounds/boymoan03.mp3"
    mc "Uuuh...Y...YES! AAAAH!"
    stop sound
    scene powerlingeriecum05 with dissolve
    play sound "sounds/panting.mp3"
    if age >= 20:
        pg "That is so FILTHY! You've CAKED my ceiling with your spunk!"
    if age >= 18 and age <= 19:
        pg "That is so FILTHY! You've CAKED my ceiling with your teenage spunk!"
    scene powerlingeriecum06 with dissolve
    pg "Because of you and your great big fat MONSTERLOADS, I'm gonna end up sleeping in SPUNK-COVERED BEDSHEETS!"
    mc "You asked me to reach the ceiling!"
    play sound "sounds/lick03.mp3"
    pg "That's IRRELEVANT! * slurp * "
    stop sound

if inventorylustring == False:
    scene powerlingeriecum03b with dissolve
    mc "RHAAAA! I'm TRYING!"
    window hide
    with hpunch
    pg "You're ALMOST reaching the ceiling. But not quite..."
    window hide 
    with fastflash
    play sound "sounds/boymoan05.mp3"
    mc "But I'm cumming as HARD as I can! RHAAA!"
    scene powerlingeriecum04b with dissolve
    pg "You ARE cumming hard, just not HARD enough! Doesn't your landlady's daughter excite you ENOUGH?"
    scene powerlingeriecum05 with dissolve
    play sound "sounds/panting.mp3"
    mc "Uuuh...Y...YES! You do!"
    scene powerlingeriecum06 with dissolve
    pg "Because of you and your great big fat LOADS, I'm gonna end up sleeping in SPUNK-COVERED BEDSHEETS!"
    mc "You asked me to cum a lot!"
    play sound "sounds/lick03.mp3"
    pg "And you did... But not ENOUGH! You'll need to UP YOUR GAME if you want MORE! * wink *"

scene powerlingeriecum07:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
pg "You've been a very NAUGHTY boy, you know that?"
mc "You're the one who teased me, Kara! And I'm STILL hard, can we...?"
scene powerlingeriecum08 with dissolve
pg "...FUCK? No, I'm not ready for that... You'll have to WAIT and learn to CONTROL your libido..."
pg "Now go back to your room and do whatever it is you need to do to get it down..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop music
jump Main

label PowergirlSupergirl:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ seensuperpowergirl = True
scene powersuper01 with fade
play music "sounds/sexy07.mp3"
mc "Well, hello there ladies, what have we got going here? I think I might join!"
scene powersuper02 with dissolve
pg "This is a girls night ONLY! You're not invited, [name]."
mc "What? But I..."
sg "I'm on assignment with Powergirl, not YOU today..."
scene powersuper03 with dissolve
play sound "sounds/kiss.mp3"
pg "And after our tough day fighting crime, we deserve some relaxing time together, don't you agree, [name]?"
scene powersuper04 with dissolve
mc "Yeah, sure, but I've been fighting crime too! I deserve something too!"
pg "Don't interrupt us! You can watch, but you'd better shut up..."
scene powersuper05 with dissolve
play sound "sounds/kiss.mp3"
sg "Mmh..."
mc "* God, this is so Super-Sexy *"
scene powersuper06 with dissolve
mc "Pretty pl..."
pg "I said NO, [name]! Just enjoy the show. You're lucky enough to be watching it..."
window hide

label PowerSuperSlow:
hide nexticon
hide faster
hide slower
hide sideicon
hide front
show powersuperslowvideo behind powersuperfastvideo
show powersuperslowvideo behind powersuperfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powersuperfrontslowvideo
hide powersuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powersupertalkfast = False
if powersupertalkslow == False:
    sg "Mmh, Kara, just like that!"
    $ powersupertalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powersuperslow()
screen powersuperslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlow")

label PowerSuperFast:
hide nexticon
hide faster
hide slower
hide sideicon
hide front
show powersuperfastvideo behind powersuperslowvideo
show powersuperfastvideo behind powersuperfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powersuperslowvideo
hide powersuperfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powersupertalkslow = False
if powersupertalkfast == False:
    pg "Oooh! UUUH, it feels so good rubbing our pussies together!"
    $ powersupertalkfast = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powersuperfast()
screen powersuperfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFast")

label PowerSuperFrontSlow:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
show powersuperfrontslowvideo behind powersuperslowvideo
show powersuperfrontslowvideo behind powersuperfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powersuperslowvideo
hide powersuperfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powersupertalkfast = False
if powersupertalkslow == False:
    sg "Mmh, Kara, just like that!"
    $ powersupertalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powersuperfrontslow()
screen powersuperfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperSlow")

label PowerSuperFrontFast:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
show powersuperfrontfastvideo behind powersuperfastvideo
show powersuperfrontfastvideo behind powersuperfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powersuperfrontslowvideo
hide powersuperfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powersupertalkslow = False
if powersupertalkfast == False:
    pg "Oooh! UUUH, it feels so good rubbing our pussies together!"
    $ powersupertalkfast = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show sideicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powersuperfrontfast()
screen powersuperfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerSuperFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerSuperEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerSuperFast")

label PowerSuperEnd:
hide nexticon
hide cum
hide faster
hide slower
hide sideicon
hide front
pg "[name] is being a naughty boy, he's rubbing himself while he's admiring the show..."
sg "A NAUGHTY, DIRTY boy! Knowing that he's getting hard watching us makes me want to cum... Even if boys' thingies are DISGUSTING."
scene powersupercum01 with dissolve
pg "Then let me help you reach that climax, Linda!"
play sound "sounds/moan05.mp3"
scene powersupercum02 with dissolve
play channel1 "sounds/moan02.mp3"
sg "... AAAAH!"
play sound "sounds/splooge02.mp3"
window hide
with hpunch
pg "UUUUH, come for me Supergirl!"
scene powersupercum03 with dissolve
stop channel1
play sound "sounds/panting.mp3"
pg "Mmmh, she squirted so much, it must have been REAL GOOD..."
scene powersupercum04 with dissolve
sg "Oooh... This is the BEST orgasm I ever had..."
scene powersupercum05 with dissolve
sg "But... You're all DIRTY with my juices, Kara. I need to clean up my mess.."
mc "I'll help you!"
pg "No you WON'T! I want her feminine touch and not your ROUGH hands and tongue on my breasts..."
play channel1 "sounds/lick01.ogg"
scene powersuperbreast
$ renpy.pause(1.0, hard='True') 
pause
stop channel1
pg "I think I'm all clean... Now it 's YOUR turn, Linda."
play channel1 "sounds/lick03.mp3"
scene powersuperpussy
$ renpy.pause(1.0, hard='True') 
pause
stop channel1
play sound "sounds/moan05.mp3"
scene powersuper10 with dissolve
sg "Oh my God, you lick pussy sssoo well! Where did you learn that?"
pg "It seems you're not the only one with some SUPER-SEX superpowers, [name]!"
mc "I'm the only one with a 15-inch long pussy-pleaser!"
scene powersuper06 with dissolve
pg "Yeah, I think we all know by now, you keep telling us."
sg "It's getting late and we need to take a shower TOGETHER before heading to bed. So off you go, [name]. I'll see you tomorrow morning for OUR pairing."
mc "I can't wait for THAT!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label PowerRoomHot:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy09.mp3"
scene powerlingeriebackground01
show powerhot01:
    zoom 1.0 xoffset -1000 yoffset 0
with fade
show powerhot01 at moveleftinslow
$ renpy.pause(0.8, hard='True')      
mc "Wow, this set is really HOT, Kara!"
window hide
hide powerhot01
hide powerlingeriebackground01
show powerlingeriebackground01:
    zoom 1.7 xoffset -100 yoffset 0
show powerhot02:
    zoom 1.0 xoffset -100 yoffset 0   
show powerlingeriebackground01 at powerfulldownbackground
show powerhot02 at powerfulldown02
with dissolve
$ renpy.pause(5.0, hard='True')
pause
pg "Really, you like it? You're not just saying that to get inside my panties?"
mc "I mean it. AND I want to get into your panties."
scene powerlingeriebackground01 blurred
show powerhot03a
with dissolve
pg "Does it showcase my MUSCLES well enough?"
mc "I can see your abs CLEARLY."
window hide
hide powerhot03a
show powerlingeriebackground01:
    zoom 1.8 xoffset -100 yoffset 0
show powerhot03b:
    zoom 1.0 xoffset -200 yoffset -1080    
show powerlingeriebackground01 blurred at widowfullbackzoombackground
show powerhot03b at powerfullup
with dissolve
$ renpy.pause(5.0, hard='True')      
mc "And now I can see them TENSING and your biceps BULGING!"
scene powerlowbackground
show powerhot04
with dissolve
pg "And is YOUR muscle tensing [name]? * wink *"
mc "It's tensing, it's tensing fast and HARD!"
hide powerhot04
show powerhot05
with dissolve
pg "So you're telling me you're getting a great big hardon from looking at your landgirl posing in sexy lingerie?"
mc "Well, err..."
hide powerhot05
show powerhot06
with dissolve
pg "Pull it out then, I want to see how HARD I make you. And it better be TITANIUM-HARD!"
mc "I'll show you, Kara, I'll show you, I'll get totally TITANIUM-HARD for you!"
hide powerhot06
show powerhot07
with dissolve
pg "And if you ARE as HARD as I want you to be, maybe I'll take my bra off for you..."
scene powerhot08 with dissolve
pg "I'll give you a sneak peek... Cos you're such a naughty boy."
scene powerhot09 with dissolve
play sound "sounds/wow.mp3"
pg "Wow, you really are SUPER-HARD for me..."
mc "You've got to do something about it, I don't know how long I can..."
scene powerhot10:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "... You poor thing, you need some relief, don't you? You'd love to stick that big fat pile-driver right up my wet pussy, wouldn't you?"
mc "Yes, YES, I NEED TO! I beg you, Kara!"
scene powerhot11 with dissolve
play sound "sounds/kiss.mp3"
pg "Just kiss me first, silly boy, try and make this WORTH it for me too..."
scene powerhot12 with dissolve
play sound "sounds/kiss.mp3"
pg "That's it, with your tongue, I LOVE French-kissing... While I grind my butt on your ROCK-HARD shaft..."
scene powerhot13 with dissolve
play sound "sounds/boymoan02.mp3"
mc "Please, Kara, let me put it inside you..."
scene powerhot14 with dissolve
pg "Not yet cowboy, what would be the fun in that? I want to take it SLOWLY. Meaning, I'll use my lovely feet first..."
play channel1 "sounds/wetmassage.mp3"

label PowerFootHotSlow:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootslowvideo behind powerfootfastvideo
show powerfootslowvideo behind powerfootsideslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootfastvideo
hide powerfootsideslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerhottalkfast = False
if powerhottalkslow == False:
    pg "I'm in control now, [name]. In control of YOUR horny [age]yo MONSTERCOCK!"
    $ powerhottalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powerfootslow()
screen powerfootslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootHotFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSideSlow")

label PowerFootHotFast:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootfastvideo behind powerfootslowvideo
show powerfootfastvideo behind powerfootsidefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootslowvideo
hide powerfootsidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerhottalkslow = False
if powerhottalkfast == False:
    pg "You need some sweet relief, don't you? Let my feet take you over the edge, give me a truly SUPERHERO load of sweet young cum!"
    $ powerhottalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen powerfootfast()
screen powerfootfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootHotSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootHotEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootSideFast")

label PowerFootSideSlow:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootsideslowvideo behind powerfootslowvideo
show powerfootsideslowvideo behind powerfootsidefastvideo
$ renpy.pause(1.0, hard='True')      
hide powerfootslowvideo
hide powerfootsidefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerhottalkfast = False
if powerhottalkslow == False:
    pg "I'm in control now, [name]. In control of YOUR horny [age]yo MONSTERCOCK!"
    $ powerhottalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerfootsideslow()
screen powerfootsideslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootSideFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootHotSlow")

label PowerFootSideFast:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
show powerfootsidefastvideo behind powerfootfastvideo
show powerfootsidefastvideo behind powerfootsideslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerfootsideslowvideo
hide powerfootfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerhottalkslow = False
if powerhottalkfast == False:
    pg "You need some sweet relief, don't you? Let my feet take you over the edge, give me a truly SUPERHERO load of sweet young cum!"
    $ powerhottalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerfootsidefast()
screen powerfootsidefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFootSideSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFootHotEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFootHotFast")

label PowerFootHotEnd:
hide cum
hide faster
hide slower
hide sideicon
hide sceneicon
pg "Are you going to spew that filthy load yet? I think you REALLY need to, don't you?"
mc "Oh Kara, I'm gonna cum, gonna cum so much for you!"
scene powerhotfootcum01 with dissolve
mc "FUCK, here it comes, AAAH!"
stop channel2
play channel2 "v031/boyorgasm02.mp3"
window hide
with hpunch
pg "Mmmh, yeah, I love seeing that great big fat donkey-cock CONVULSING with pleasure!"
scene powerhotfootcum02 with dissolve
pg "Look at all that yummy spunk, you're really giving your naughty landgirl a BIG load, aren't you?"
window hide
with fastflash
mc "I am Kara, just for YOOOOOUUUU, AAAAH!"
scene powerhotfootcum03 with dissolve
pg "But it's not enough, I want MORE, give me MORE!"
window hide
with hpunch
mc "Your feet are DRAINING me, RHAAA!"
scene powerhotfootcum04 with dissolve
pg "Give me a few more POWERFUL SHOTS, [name]! I know you can do it! Do it for your LANDLADY'S DAUGHTER!"
window hide
with fastflash
pg "MORE!"
scene powerhotfootcum03 with dissolve
pg "That's it, let it ALL out, [name]..."
window hide
with hpunch
pg "You're such a good boy, pumping all that sweet cum just for me..."
stop channel2
stop channel1
scene powerhotfootcum05 with dissolve
play sound "sounds/panting.mp3"
pg "Now, your giant cock had better not go soft on me..."
scene powerhotfootcum06 with dissolve
play sound "sounds/slurp.mp3"
pg "Cos I have MUCH MORE in store for it..."
scene powerhotfootcum07 with dissolve
pg "But I should really take my panties off if you plan to get that rod inside me, right?"
mc "Oh God, Kara..."
scene powerhotfootcum08 with dissolve
if age >= 20:
    pg "You're still so HARD for me! My feet didn't pump enough cream out of your giant cum factories after all..."
if age >= 18 and age <= 19:
    pg "You're still so HARD for me! My feet didn't pump enough cream out of your giant teenage cum factories after all..."
scene powerhotfootcum09 with dissolve
play sound "sounds/lick03.mp3"
pg "Maybe I should help you replenish them to FULL CAPACITY. With MY cream! Hi hi!"
scene powerhotfootcum10 with dissolve
play sound "sounds/slurp.mp3"
pg "That's it, suck up that milk, it will make you STRONG [name]! * giggles*"
scene powerhotfootcum11 with dissolve
pg "So are you ready for another round of TEASING and CUMMING, [name]?"
mc "As long as it involved your crotch teasing my pussy and my cock cumming INSIDE you!"
scene powerhotfootcum12 with dissolve
pg "You've got it half-right, naughty landboy! I'll show you..."
window hide
play channel1 "sounds/wank.mp3"

label PowerRideHotSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerrideslowvideo behind powerridefastvideo
show powerrideslowvideo behind powerridepovslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerridefastvideo
hide powerridepovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerridetalkfast = False
if powerridetalkslow == False:
    mc "You're rubbing your clit on my shaft Kara, Oh God..."
    pg "That's the teasing idea, [name]!"
    $ powerridetalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerrideslow()
screen powerrideslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideHotFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRidePOVSlow")

label PowerRideHotFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridefastvideo behind powerrideslowvideo
show powerridefastvideo behind powerridepovfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerrideslowvideo
hide powerridepovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerridetalkslow = False
if powerridetalkfast == False:
    if age >= 20:
        pg "I should really do it faster now, cos your giant dong just NEEDS to come, doesn't it?"
    if age >= 18 and age <= 19:
        pg "I should really do it faster now, cos your giant teenage dong just NEEDS to come, doesn't it?"
    $ powerridetalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerridefast()
screen powerridefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideHotSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerRideHotEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRidePOVFast")

label PowerRidePOVSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridepovslowvideo behind powerrideslowvideo
show powerridepovslowvideo behind powerridepovfastvideo
$ renpy.pause(1.0, hard='True')      
hide powerrideslowvideo
hide powerridepovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ powerridetalkfast = False
if powerridetalkslow == False:
    mc "You're rubbing your clit on my shaft Kara, Oh God..."
    pg "That's the teasing idea, [name]!"
    $ powerridetalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerridepovslow()
screen powerridepovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRidePOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideHotSlow")

label PowerRidePOVFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show powerridepovfastvideo behind powerridefastvideo
show powerridepovfastvideo behind powerridepovslowvideo
$ renpy.pause(1.0, hard='True') 
hide powerridepovslowvideo
hide powerridefastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ powerridetalkslow = False
if powerridetalkfast == False:
    if age >= 20:
        pg "I should really do it faster now, cos your giant dong just NEEDS to come, doesn't it?"
    if age >= 18 and age <= 19:
        pg "I should really do it faster now, cos your giant teenage dong just NEEDS to come, doesn't it?"
    $ powerridetalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powerridepovfast()
screen powerridepovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRidePOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerRideHotEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideHotFast")

label PowerRideHotEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
pg "Looks like my teasing is going to push you over the edge. AGAIN!"
scene powerridecum01 with dissolve
stop channel1
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "YES IT IS, AAAH!"
window hide
with fastflash
pg "Mmmh, I love it when you BLAST so POWERFULLY for me!"
scene powerridecum02 with dissolve
play sound "sounds/moan02.mp3"
pg "That's it, cover my tits in your warm cream!"
window hide
with hpunch
pg "Ooh, you're CONVULSING, aren't you? Convulsing with pleasure for your teasing landgirl!"
scene powerridecum03 with dissolve
mc "OOOOH, AAAH!"
window hide
with fastflash
pg "You just want to come and come and never stop, don't you?"
scene powerridecum04 with dissolve
mc "Oh God, Kara..."
window hide
with hpunch
pg "That great big [age]yo horsecock is just aching to empty its nasty nut, isn't it?"
scene powerridecum05 with dissolve
pg "Come on, I know you have a few shots left in those giant cum boulders of yours!"
window hide
with fastflash
mc "Ggg... I... I can't anymore..."
scene powerridecum06 with dissolve
stop channel2
stop channel1
play sound "sounds/panting.mp3"
pg "You're not tired, are you [name]? Cos you still haven't put your massive 18-incher up my fuckhole..."
mc "Oh God..."
scene powerridecum07 with dissolve
if powerfuckfirst:
    pg "Look at you, you're STILL HARD just thinking about sticking your huge pud up my hungry hole... Such a dirty boy..."
    scene powerridecum08 with dissolve
    pg "Now it's time for me to ride this wild beast and REALLY tame it like I did last time, [name]!"
if powerfuckfirst == False:
    pg "Yeah, it's time for you to show me how you FUCK a girl! You've PUMPED your monster schlong up everyone else's horny pussy, I know that..."
    scene powerridecum06 with dissolve
    pg "Even my mother's pussy, cos you're such a dirty boy! And she's such a cock-hungry size queen."
    mc "I..."
    $ powerfuckfirst = True
    scene powerridecum08 with dissolve
    pg "But I don't care. Now it's MY turn to ride this wild beast that's been destroying all these hungry holes behind my back!"
scene powerridecum08 with dissolve
play sound "sounds/slurp.mp3"
pg "But first, I'll clean up the aftermath of your second MONSTER LOAD..."
scene powerridecum09 with dissolve
mc "Yeah, fuck, that's keeping me ROCK-HARD for you, Kara!"
pg "I want to check this myself. Hold me in your muscular arms, [name]..."
scene powerridecum10 with dissolve
pg "Mmh... I can FEEL its hardness, but... Can it STAY the course? If I rub my hungry snatch all over it?"
mc "I... err."
play channel1 "sounds/boymoan02.mp3"
play channel2 "sounds/wetmassage.mp3"
window hide

label PowerDickSlow: 
hide nexticon
hide faster
hide slower
show powerdickslowvideo behind powerdickfastvideo
pause 1.0
hide powerdickfastvideo with dissolve
if powerdicktold == False:
    pg "Yeah, it does feel quite HARD, doesn't it?"
    window hide
    $ powerdicktold = True
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen powerdickslow()
screen powerdickslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerDickFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerDickEnd")

label PowerDickFast:
show powerdickfastvideo behind powerdickslowvideo
hide nexticon
hide faster
hide slower
pg "But what if I grind my ass on it a bit HARDER and FASTER? Will it hold up?"
mc "I..."
hide powerdickslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen powerdickfast()
screen powerdickfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerDickSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerDickEnd")

label PowerDickEnd:    
hide nexticon
hide slower
hide faster
pg "Well done [name]... You stayed ROCK-HARD for Powergirl. I hope it was good for you!"
scene powerdickcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
pg "Ooh, it WAS good for you, wasn't it?"
window hide
with fastflash
play sound "sounds/wow.mp3"
pg "You can't help but spurt some great big globs of yummy spunk from me grinding on your fat [age]yo donkey-dick!"
stop sound
play sound "sounds/boymoan.mp3"
$ renpy.pause(0.5, hard='True')
scene powerdickcum02 with dissolve
stop channel1
play sound "sounds/boymoan02.mp3"
pg "Are you done wih those  pre-orgasmic spurts? Mmmh, now you're going to be ROCK-HARD for me for a LONG TIME!"
pg "It's just what I wan..."
scene powerprefuck01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with dissolve
pg "...Ooh, look at you, you're so HORNY, you've decided to MANHANDLE your poor landlady's daughter?"
mc "That's right, I can't take it any more, you've teased me too much Kara!"
scene powerprefuck02 with dissolve
pg "Are you going to REALLY give it to me? To really POUND my poor little pussy to total oblivion with your massive cunt-splitter?"
play sound "sounds/thud.mp3"
scene powerprefuck03 with dissolve
mc "Feel how fucking heavy and hard my cock feels! This is going to SPLIT you in two!"
scene powerprefuck02 with dissolve
pg "Do it again, I NEED to feel its POWER!"
window hide
play music ["sounds/thud.mp3", "<silence .75>"]
scene powercockslap
pause
pg "Now SHOW ME, DRILL MY HOLE, you horse-hung STUD!"
stop music

label PowerFuckSlow:
$ powerharder = False
window hide
show powershortslowvideo behind powershortfastvideo
show powershortslowvideo behind powershortpovslowvideo
show powershortslowvideo behind powerhardslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powershortfastvideo
hide powershortpovslowvideo
hide powerhardslowvideo
hide nexticon
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
call screen powershortslow()
screen powershortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckPOVSlow")

label PowerFuckFast:
$ powerharder = False
window hide
show powershortfastvideo behind powershortslowvideo
show powershortfastvideo behind powershortpovfastvideo
show powershortfastvideo behind powerhardfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powershortslowvideo
hide powershortpovfastvideo
hide powerhardfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powershortfast()
screen powershortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckPOVFast")

label PowerFuckPOVSlow:
$ powerharder = False
window hide
show powershortpovslowvideo behind powershortslowvideo
show powershortpovslowvideo behind powershortpovfastvideo
show powershortpovslowvideo behind powerhardpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powershortslowvideo
hide powershortpovfastvideo
hide powerhardpovslowvideo
hide nexticon
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
show sceneicon:
     xpos 50 ypos 500     
call screen powershortpovslow()
screen powershortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckSlow")

label PowerFuckPOVFast:
$ powerharder = False
window hide
show powershortpovfastvideo behind powershortpovslowvideo
show powershortpovfastvideo behind powershortfastvideo
show powershortpovfastvideo behind powerhardpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powershortpovslowvideo
hide powershortfastvideo
hide powerhardpovfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powershortpovfast()
screen powershortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("PowerHardPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerFuckFast")

label PowerHardSlow:
if powerharder == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharder = True        
window hide
show powerhardslowvideo behind powerhardfastvideo
show powerhardslowvideo behind powerhardpovslowvideo
show powerhardslowvideo behind powershortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powerhardfastvideo
hide powerhardpovslowvideo
hide powershortslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerhardlow()
screen powerhardlow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEnd")

label PowerHardFast:
if powerharder == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharder = True        
window hide
show powerhardfastvideo behind powerhardslowvideo
show powerhardfastvideo behind powerhardpovfastvideo
show powerhardfastvideo behind powershortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen powerhardfast()
screen powerhardfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEnd")

label PowerHardPOVSlow:
if powerharder == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharder = True        
window hide
show powerhardpovslowvideo behind powerhardslowvideo
show powerhardpovslowvideo behind powerhardpovfastvideo
show powerhardpovslowvideo behind powershortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortpovslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerhardpovslow()
screen powerhardpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEnd")

label PowerHardPOVFast:
if powerharder == False:
    mc "Are you ready to take it HARDER and DEEPER Kara?"
    pg "YES! GIVE ME ALL YOU'VE GOT!"
    $ powerharder = True        
window hide
show powerhardpovfastvideo behind powerhardpovslowvideo
show powerhardpovfastvideo behind powerhardfastvideo
show powerhardpovfastvideo behind powershortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide powerhardpovslowvideo
hide powerhardfastvideo
hide powershortpovfastvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show nexticon:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powerhardpovfast()
screen powerhardpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerHardPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("PowerFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerFuckEnd")

label PowerFuckEnd:
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
pg "Now I don't want you to come just yet, so pull out your donkey-dick, I'm gonna RIDE you like a wild bronco!"
mc "I'm so close though, so, so very close..."
pg "PULL OUT GODAMMIT!"
mc "Oh God, too late, I..."
play sound "sounds/boymoan05.mp3"
show powerpullcumend behind powerpullanimvideo
hide powerhardfastvideo
hide powershortpovfastvideo
hide powerhardslowvideo
hide powerhardpovfastvideo
hide powershortpovslowvideo
hide powerhardpovslowvideo
hide powershortslowvideo
hide powershortpovfastvideo
hide powershortfastvideo
show powerpullanimvideo
with fastdissolve
$ renpy.pause(1.33, hard='True')
scene powerpull01 with dissolve
stop channel1
play sound "sounds/boymoan02.mp3"
pg "That's just... NASTY! You just blurped a great big wad of cum on my tummy! My pussy was just sooo enticing, wasn't it?"
mc "Y... yes, I just couldn't hold off... Sorry, Kara..."
scene powerpull02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
pg "Now you're going to have to make it up to me, I'm going to RIDE YOU TILL YOU SPEW A GIANT BOYLOAD!"
mc "Uh oh..."
scene powerfuckpreride01 with dissolve
pg "Just keep that great big [age]yo whopper steady..."
scene powerfuckpreride02 with dissolve
play sound "sounds/moan04.ogg"
pg "It's so BIG! AAAH!!!"
mc "That's just my helmet Kara. You've got 15 more inches to go."
scene powerfuckpreride03 with dissolve
pg "You think I'm scared? Powergirl is NEVER scared, I'll prove it to you!"

label PowerCowgirlSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlslowvideo behind powercowgirlfastvideo
show powercowgirlslowvideo behind powercowgirlfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powercowgirlfastvideo
hide powercowgirlfrontslowvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkfast = False
if powercowgirltalkslow == False:
    mc "That's it, you've getting the hang of it, nice and slow..."
    $ powercowgirltalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powercowgirlslow()
screen powercowgirlslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerCowgirlFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideFrontSlow")

label PowerCowgirlFast:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfastvideo behind powercowgirlslowvideo
show powercowgirlfastvideo behind powercowgirlfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powercowgirlslowvideo
hide powercowgirlfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkslow = False
if powercowgirltalkfast == False:
    mc "Damn Kara, you're really riding my dong now!"
    if age >= 20:
        pg "* puff * I told... you... Powergirl can take it... All your FAT INCHES!"
    if age >= 18 and age <= 19:
        pg "* puff * I told... you... Powergirl can take it... All your FAT TEENAGE INCHES!"
    $ powercowgirltalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen powercowgirlfast()
screen powercowgirlfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerCowgirlSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerCowgirlEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideFrontFast")

label PowerRideFrontSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfrontslowvideo behind powercowgirlslowvideo
show powercowgirlfrontslowvideo behind powercowgirlfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide powercowgirlslowvideo
hide powercowgirlfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkfast = False
if powercowgirltalkslow == False:
    mc "That's it, you've getting the hang of it, nice and slow..."
    $ powercowgirltalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen powercowgirlfrontslow()
screen powercowgirlfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerRideFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerCowgirlSlow")

label PowerRideFrontFast:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show powercowgirlfrontfastvideo behind powercowgirlfastvideo
show powercowgirlfrontfastvideo behind powercowgirlfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide powercowgirlfrontslowvideo
hide powercowgirlfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex04.mp3"
$ powercowgirltalkslow = False
if powercowgirltalkfast == False:
    mc "Damn Kara, you're really riding my dong now!"
    if age >= 20:
        pg "* puff * I told... you... Powergirl can take it... All your FAT INCHES!"
    if age >= 18 and age <= 19:
        pg "* puff * I told... you... Powergirl can take it... All your FAT TEENAGE INCHES!"
    $ powercowgirltalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen powercowgirlfrontfast()
screen powercowgirlfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("PowerRideFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("PowerCowgirlEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("PowerCowgirlFast")

label PowerCowgirlEnd:
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
pg "I want you to COME now [name], the BIGGEST LOAD OF CUM YOU CAN MUSTER FOR ME!"
mc "But... I..."
scene powerridefuckcum01 with dissolve
pg "CUM NOW FOR POWERGIRL!"
play sound "sounds/splooge02.mp3"
stop channel2
window hide
with hpunch
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAH!"
scene powerridefuckcum02 with dissolve
play sound "sounds/splooge01.mp3"
pg "That's it, just KEEP PUMPING THAT SPUNK INSIDE ME!"
window hide
with fastflash
mc "My balls... they're EXPLODING, RHAAA!"
scene powerridefuckcum03 with dissolve
play sound "sounds/womancum01.mp3"
pg "Let me make them BURST even more then!"
window hide
with hpunch
mc "AAAAH, this is sssooo GOOOOOD!"
scene powerridefuckcum04 with dissolve
play sound "sounds/splooge03.mp3"
pg "Powergirl's pussy is just the BEST pussy, isn't it?"
window hide
with fastflash
mc "Y... YES, UUUUH, BLASTING SOME MORE!"
scene powerridefuckcum03 with vpunch
play sound "sounds/splooge01.mp3"
pg "Good, cos I want you to COME some more!..."
scene powerridefuckcum04 with dissolve
play sound "sounds/splooge03.mp3"
pg "... To TOTALLY EMPTY YOUR BALLS FOR ME!"
scene powerridefuckcum03 with vpunch
play sound "sounds/splooge01.mp3"
pg "KEEP PUMPING YOUR SEED UNTIL I TELL YOU STOP!"
scene powerridefuckcum05 with dissolve
mc "OOOOH, I'm..."
window hide
with hpunch
pg "...not yet giving up on me, IS THAT CLEAR?"
scene powerridefuckcum06 with dissolve
pg "I can feel your cream sloshing inside me [name], just KEEP IT UP!"
window hide
with fastflash
mc "AAAAH! I can't... I'm..."
scene powerridefuckcum07 with dissolve
stop channel2
play sound "sounds/splooge01.mp3"
pg "... DRAINED by Powergirl!"
scene powerridefuckcum08 with dissolve
play sound "sounds/panting.mp3"
pg "Well, look at you. You look like a tired superhero. I suppose after that MANY loads, I can let you go back to your room."
play sound "sounds/panting.mp3"
mc "Ggg... Thanks Kara."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
