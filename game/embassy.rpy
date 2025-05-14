label SovietEmbassy:
if seenembassy:
    jump SovietEmbassySeen
if seenembassy == False:
    jump SovietEmbassyNext

label SovietEmbassySeen:
scene embassy05 with dissolve
mc "So. A tall wall, a Super-Hero with Super-Agility, that should do the trick."
scene embassy06a with dissolve
mc "Piece of cake!"
scene embassy06c with dissolve
play music "sounds/alarm.mp3"
mc "Uh oh, looks like they upgraded their alarm system since my last visit! Let's get out of here before they start shooting at me!"
scene embassy05 with dissolve
stop music
mc "I'm gonna need to find another way of getting inside this embassy. In another update..."
jump Main

label SovietEmbassyNext:
play music "sounds/nightsounds.mp3"
$ period = 1
scene preride01 with fade
mc "She should be coming out of that garage over there that you guys can't see anytime now..."
scene preride02 with dissolve
play sound "v042/carengine.mp3"
mc "And there she is! I recognize her green Dodge!"
scene ride01 with dissolve
stop sound
mc "I have to follow her, I've got to hail a cab pronto!"
scene ride02 with dissolve
cd "Yes, my friend? Where would you like to..."
mc "Just follow that green Dodge!"
play music "v042/carchase.mp3"
scene ride03 with dissolve
mc "We're going to lose her, drive faster!"
cd "That is bery, bery wrong!"
scene ride04 with dissolve
mc "Just do it! I'll give you a generous tip at the end!"
play sound "v042/screeching.mp3"
cd "Oooh, I don't like that, not one bit, my friend!"
scene ride05 with dissolve
mc "There, she turned into that street, stay at a safe distance but don't lose her!"
scene embassy01 with fade
mc "She's stopping right in front of this huge building..."
cd "That is the Soviet embassy, my friend."
mc "Okay, just drive by the entrance real slow..."
scene embassy02 with dissolve
stop music
play music "sounds/nightsounds.mp3"
mc "She's being let through like she knows the guards. Very suspicious. Let me off over there, please."
scene embassy03 with dissolve
cd "That will be forty-seven dollars, my friend. Plus your generous tip, thank you bery, bery much."
mc "Err, I don't have any money actually, just bill the Cockham League of Justice will you?"
cd "That is bery, bery bad of you, my friend, I wish to complain in the most vehement manner!"
mc "This is a super-important MISSION to save the world, you hear me? So don't interfere with Cockham League business!"
scene embassy04 with dissolve
cd "I will never take another superhero in my cab! Bery, bery bad customers!"
mc "* It sure would make things easier if there was actual money in this damn game... Although players would instantly cheat it in the console. *"
scene embassy05 with dissolve
mc "So. A tall wall, a Super-Hero with Super-Agility, that should do the trick."
call screen usepower("useagility", "SovietwallNoAgility", "SovietwallAgility") with dissolve

label SovietwallNoAgility:
scene embassy06a with dissolve
play sound "sounds/mangrunt01.mp3"
mc "Damn it, I can't even reach the top of that wall. Let's start over again... Until the payer manages to hit the correct button."
scene embassy05 with dissolve
stop sound
mc "Come on, it can't be THAT hard!"
call screen usepower("useagility", "SovietwallNoAgility", "SovietwallAgility") with dissolve

label SovietwallAgility:
$ seenembassy = True
scene embassy06b with dissolve
$ usedagility += 1
mc "Piece of cake!"
scene embassy07 with dissolve
mc "Got you! Just in time, she's entering this building with another chick... Better follow them inside."
scene embassy08 with dissolve
stop music
mc "This place is creepy and I just missed them! They took the elevator, I'll check which floor they g..."
scene embassy09 with dissolve
play music "v042/russianballet.mp3"
mc "What the hell...?"
scene embassy10 with dissolve
mc "Where did these two... come from?"
scene embassy11 with dissolve
mc "Hello? Who are you? Just let me through and go and practice ballet somewhere else, ladies!"
scene embassy12 with dissolve
mc "I'm losing patience here, robot-woman! Just GET OUT OF MY WAY!"
scene embassy13 with dissolve
mc "Hey, stop this! These are NOT just dancing robots, they're KILLER-ROBOTS!"
scene embassy14 with dissolve
mc "* Her armhold is... super-strong! I can't... breathe... *"

$ img_l = []
$ l2_l = []
if mcstrength >= 2:
    $ img_l.append("usestrength")
    $ l2_l.append("BallerinaStrength")
if mcmind >= 1:
    $ img_l.append("usemind")
    $ l2_l.append("BallerinaStrength")
if img_l:
    call screen usepower(img_l, "BallerinaNoStrength", l2_l) with dissolve

label BallerinaNoStrength:
scene embassy15 with dissolve
play sound "sounds/bonecrack.mp3"
mc "I'm being squeezed to DEATH here! AAAHHhhhh...."
if selected_power == "usemind":
    mc "I can't mind-control robots, this was a BAD CHOICE! And now I'm being squeezed to DEATH! AAAHHhhhh...."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label BallerinaStrength:
if selected_power == "usemind":
    scene embassy15 with dissolve
    mc "I can't mind-control robots, this was a BAD CHOICE! And now I'm being squeezed to DEATH! AAAHHhhhh...."
    window hide
    show gameovericon:
        xpos 600 ypos 400
    pause
    return
scene embassy16 with dissolve
$ usedstrength += 1
play sound "sounds/mangrunt01.mp3"
mc "SUPER-STRENGTH IN ACTION!"
scene embassy17 with dissolve
mc "Oh, you want to fight, hey? Well, I'm prepared to take on BOTH OF YOU METAL FREAKS!"
call screen usepower("usecombat", "BallerinaNoCombat", "BallerinaCombat") with dissolve

label BallerinaNoCombat:
scene embassy21 with dissolve
play sound "sounds/punch.mp3"
mc "...Yikes!"
jump BallerinaCombatEnd

label BallerinaCombat:
$ usedcombat += 1
scene embassy18 with dissolve
play sound "sounds/punch.mp3"
mc "You want some of that? Then eat my shoe!"
scene embassy19 with dissolve
mc "Oh, no you won't hit my soft baby skin face!"
scene embassy20 with dissolve
mc "Now, yield, big-titted ballerina Soviet robot! I have the upper h..."
scene embassy21 with dissolve
play sound "sounds/punch.mp3"
mc "...Yikes!"
label BallerinaCombatEnd:
hide screen statscreenicon
hide screen questscreenicon
hide screen calendar
scene embassy22 with dissolve
stop music
play music "sounds/sexy02.mp3"
mc "Uh oh... I'm in deep trouble now..."
scene embassy23 with dissolve
mc "Just let me go, I promise I won't come back ever again!"
scene embassy24 with dissolve
mc "Oh God, she even has a realistic pussy, now I'm getting an erection..."
scene embassy25 with dissolve
mc "I see, you girls want to have some fun with my SUPERHERO COCK, hey? Then be my guest, I'll DESTROY your pussies and I'll finally be able to get through!"
scene embassy26 with dissolve
play sound "sounds/kiss.mp3"
mc "* Damn, I'm kissing a mouthless metal robot. Feels pretty good actually... *"
scene embassy27 with dissolve
if age >= 20:
    mc "Yeah, play with my massive balls, I'm gonna cover your tits in an inch-thick layer of my cream!"
if age >= 18 and age <= 19:
    mc "Yeah, play with my massive balls, I'm gonna cover your tits in an inch-thick layer of my teenage cream!"
scene embassy28 with dissolve
mc "Now hang on ladies, this is getting a bit TOO femdom-y to my lik..."
scene embassy29 with dissolve
mc "* She's pinning my throat with her metal arse! *"
scene embassy30 with dissolve
mc "* While the other sex-crazed ballerina is about to ride my dong mercilessly! *"
mc "* I think they're not just killer robots, they're SEX KILLER ROBOTS! * Gonna have to... survive this! *"
play channel2 "sounds/boymoan02.mp3"

label RobotAssFuckSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckslowvideo behind robotassfuckfastvideo
show robotassfuckslowvideo behind robotassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckfastvideo
hide robotassfuckfrontslowvideo
with dissolve
play channel1 "sounds/wank.mp3"
mc "* Oh Fuck, she can take ssso many inches of my shaft inside her arse, it's amazing! *"
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen robotassfuckslow()
screen robotassfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("RobotAssFuckFrontSlow")

label RobotAssFuckFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfastvideo behind robotassfuckslowvideo
show robotassfuckfastvideo behind robotassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckslowvideo
hide robotassfuckfrontfastvideo
with dissolve
play channel1 "sounds/wetmassage.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen robotassfuckfast()
screen robotassfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("RobotAssFuckFrontFast")

label RobotAssFuckFrontSlow:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfrontslowvideo behind robotassfuckslowvideo
show robotassfuckfrontslowvideo behind robotassfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckslowvideo
hide robotassfuckfrontfastvideo
with dissolve
play channel1 "sounds/wank.mp3"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen robotassfuckfrontslow()
screen robotassfuckfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckSlow")

label RobotAssFuckFrontFast:
window hide
hide cum
hide slower
hide faster
hide front
hide assview
show robotassfuckfrontfastvideo behind robotassfuckfastvideo
show robotassfuckfrontfastvideo behind robotassfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
hide robotassfuckfastvideo
hide robotassfuckfrontslowvideo
with dissolve
play channel1 "sounds/wetmassage.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen robotassfuckfrontfast()
screen robotassfuckfrontfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("RobotAssFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("RobotAssFuckFast")

label RobotAssFuckEnd:
hide cum
hide assview
hide faster
hide slower
hide front
mc "* I'm starting to get dizzy... And my balls DEMAND release at the same time! *"
scene robotcum01 with dissolve
stop channel2
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "FU-UUUUCK!"
window hide
with fastflash
mc "I'm CUMMMING, AAAAH!"
scene robotcum02 with dissolve
mc "* Nooo! She's CRUSHING my pelvis! *"
window hide
with hpunch
mc "* Must... FIGHT IT! *"
call screen usepower("usestud", "RobotNoStud", "RobotStud") with dissolve

label RobotNoStud:
scene robotcum03b with dissolve
stop channel1
mc " * Can't... Breathe... Pelvis... crushed! I'm gonna die!!! *"
play sound "sounds/bonecrack.mp3"
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label RobotStud:
scene robotcum03a with dissolve
play channel2 "sounds/splooge02.mp3"
mc "By FLOODING her insides, RHAAA!"
window hide
with fastflash
play sound "sounds/boymoan03.mp3"
mc "Take that!"
scene robotcum04 with dissolve
play sound "sounds/effort01.mp3"
mc "GGGG... Gotta cum some MORE!"
window hide 
with hpunch
mc "Gotta BLAST it out... And keep that other robot from choking me!"
scene robotcum05 with dissolve
stop channel2
stop channel1
play channel4 "sounds/boymoan05.mp3"
play sound "sounds/splooge03.mp3"
mc "...NOW! RHAAAA!"
window hide
with vpunch
mc "FUCK, YEAH, AAAAH!"
stop channel4
scene robotcum06 with dissolve
play sound "sounds/glitch.mp3"
mc "That's it, next robot to SUBDUE with my mighty PILLAR!"
scene robotcum07 with dissolve
mc "And my mighty MUSCLES! What are you gonna do? Who's your daddy now?"
scene robotcum08 with dissolve
play sound "sounds/bonecrack.mp3"
mc "Since you don't seem to get the message and I don't have all day, I'm gonna get rid of you ONCE and FOR ALL!"
scene robotcum09 with dissolve
stop music
play sound "sounds/glitch.mp3"
mc "Finally, the coast is clear. I'm not even gonna bother putting my thong back on, I need to save the Black Widow from the clutches of these sex-crazed commies!"
scene natalya01 with fade
play music "sounds/coolmusic.mp3"
mc "Finally, here's the Black Widow. She seems alright, let's get her back to the compound..."
scene natalya02 with dissolve
bw "What are you doing here, [hero]???"
nt "And how did you get past my atomic-powered ballerinas?"
scene natalya03 with dissolve
mc "Oh, these two robots? I fucked them to DEATH, that's how!"
nt "You're just a filthy capitalist PIG! Look at you, walking around with a massive hardon, no wonder your country is so DEPRAVED!"
scene natalya04 with dissolve
mc "Are you going to let her insult me and Cockham like that, Natasha?"
bw "I don't do politics. She's just a friend. I can have whoever I want as a friend! So leave me alone and stop following me!"
mc "I'm going to have to report this to Captain MILF. She won't be happy. Especially since you insulted her the other day."
bw "Whatever. I do my job. You guys stay out of my PRIVATE LIFE! Or I QUIT! And you won't find a superheroine with Super-Combat skills like me anytime soon!"
scene natalya05 with dissolve
nt "And stop waving that... DISGUSTING THING in front of me! Get out of my embassy, you dirty American boy!"
mc "Fine, I'll pick up my thong on the  way out, no need to escort me out of the building... Or I might end up fucking some more Russian robots to DEATH!"
show screen statscreenicon
show screen questscreenicon
show screen calendar
scene compoundhall01n
show compoundmilf01
with fade
cm "So, did you manage to find out what is going on with the Black Widow?"
mc "Yes, she's being brainwashed by the Soviets."
hide compoundmilf01
show compoundmilf05
with fastdissolve
cm "Oh, Dear me. There was always the possibility she was a sleeper agent when I recruited her. She must be DE-PROGRAMMED before it's too late!"
mc "Alright, how do I do that? She won't even talk to me anymore."
hide compoundmilf05
show compoundmilf02
with fastdissolve
cm "It's YOUR mission. An IMPORTANT mission. So it's YOUR responsibility to figure out a way to de-program her."
hide compoundmilf02
show compoundmilf06
with fastdissolve
cm "Some kind of Mind-Control device would be useful. I wonder who could have such a thing... You'd better get going, young hero. It's getting late and you need all your wit to succeed!"
jump Main


