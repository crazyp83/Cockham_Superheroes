label MayorsHome:
if questhulk and spokemilfshehulk and spokemayorshehulk == False and questhulkcompleted == False:
    jump HulkQuestMayor01 

if mission07win and mission07mayorpresent == False:
    $ mission07mayorpresent = True
    scene mayorsoffice01 with fade
    show mayor01 with dissolve
    mk "Ah, I recognize you now. You're wearing your thong with the super-hero sign on it. [hero], is it not?"
    mc "That's right Mr Mayor."
    hide mayor01
    show mayor02
    with fastdissolve    
    mk "I would like to offer you a present, in recognition of your work saving this city from its mayor's demise."
    if samuraisword:
        mk "A rare piece of Kryptonite I borrowed from the Museum of Extraterrestrial Minerals and forgot to return. And now it is yours."
        window hide
        $ inventorykryptonite = True
        play sound "sounds/achievement.mp3"
        show acquiredkryptonite at poslocation
        $ renpy.pause(0.5, hard='True')
        pause
        mc "Fuck yeah!"
        hide mayor02
        show mayor01
        with fastdissolve
        mk "I trust you will make good use of it, ie: NOT for some silly pranks on Superman."
        mc "That... never crossed my mind, Mister Mayor..."
        jump Main    
    if inventorykryptonite:        
        mk "An exquisite samurai sword that was handed to me by my great-granduncle after the War. And now it is yours."
        window hide
        $ samuraisword = True
        play sound "sounds/achievement.mp3"
        show acquiredsamurai at poslocation
        $ renpy.pause(0.5, hard='True')
        pause
        mc "Fuck yeah!"
        hide mayor02
        show mayor01
        with fastdissolve
        mk "It has a a bit of blood on it, you might want to give it a swipe."
        jump Main
   
if mission03 and mission03end == False and seentriad == False:
    jump Mission03Office 
if mission03 and mission03end == False and seentriad:
    jump Mission03Officeb 
if mission03end and talkmission03mayor == False:
    jump PostMissionOffice
if mission03end and talkmission03mayor:
    jump MayorsOffice

label HulkQuestMayor01:
scene mayorsoffice01 with fade
show mayor01 with dissolve
mk "And what can I do for you, [hero]?"
mc "You can free She-Hulk, that's what!"
hide mayor01
show mayor03
with fastdissolve
mk "That is out of the question! She has caused enough damage to the city!"
label HulkMayorDialogues:
menu:
    "What if I punched your fucking face in until you complied? (+1 Super-Villain)" if evilness >= 13 and mayorevil == False:
        $ mayorevil = True
        hide mayor03
        show mayor02
        with fastdissolve
        mk "What? Are you threatening me? I will have the Cockham League of Justice dissolved!"
        mc "Ok, ok, I'll take it back. For NOW."
        call Evil from _call_Evil_20
        hide mayor02
        show mayor03
        with fastdissolve        
        mc "* But one day, when I'm a REAL SUPER-VILLAIN, I'll be back... *"
        jump HulkMayorDialogues
    "What if I managed to calm her down somehow?":
        $ spokemayorshehulk = True
        hide mayor03
        show mayor01
        with fastdissolve
        mk "Good luck with that. She's BERSERK! But I will grant her freedom if you succeed..."
        mc "Alright! Just have to find a way to make her more compliant now..."
        jump Main
        
label Mission03:
scene mayorsoffice01 with fade
show mayor01 with dissolve
mk "Captain MILF and... What's his name again?"
mc "[hero]. My name is [hero]."
play sound "sounds/skill.mp3"
window hide
show locationmayors at poslocation
$ renpy.pause(0.5, hard=True)
pause
$ locmayors = True
hide mayor01
show mayor02
with fastdissolve
mk "Well, I'm glad you could come on such short notice."
mk "My daughter, she's been... She has a..."
cm "What is it, Mister Mayor?"
hide mayor02
show mayor03
with fastdissolve
mk "She has a CHASTITY DEVICE ON HER!"
mc "Well, maybe she decided to become less promiscuous. I heard things about her..."
mk "NO, SOMEONE PUT IT ON HER!"
cm "It's best if you show us, Mister Mayor."
hide mayor03
show mayor04
with fastdissolve
mk "I can't go in there, my poor daughter... with this... THING on her. You go, she's in the living room next door. And I count on your TOTAL DISCRETION."
scene catherine01 with dissolve
cm "Hello Catherine, I'm Captain MILF and this is [hero]. We are here to find out what happened to you."
mc "Yeah, what do you remember for starters?"
scene catherine02 with dissolve
ck "I woke up this morning with this... belt on me. It looks like a chastity device but I don't have the key."
mc "Oh well, I'll just use my SUPER-STRENGTH to tear it right off you and you'll be good to go, don't worry."
scene catherine03 with dissolve
ck "I think it's booby-trapped. I heard a buzzing noise when I tried to remove it."
cm "Coud you please show it to us so we can see what we can do."
scene catherine04 with dissolve
ck "See this red thing? It started flashing."
scene catherine05 with dissolve
mc "Let's have a closer look then... Yeah, I see it fits very snugly. Whoever put this on you knew precisely your size..."
cm "What does it say on that red thing?"
scene catherine06 with dissolve
mc "Nothing much, just that it's locked. And it looks like it has something inside of it."
cm "Probably the gunpowder I can smell. This thing is definitely booby-trapped."
scene catherine07 with dissolve
mc "Let's see what happens if I try to..."
cm "Be careful [name], we wouldn't want this thing to blow up."
scene catherine08 with dissolve
mc "Blowing up such a fine ass would indeed be a crime."
ck "This is so embarrassing..."
play sound "sounds/buzz.mp3"
mc "Ah, I hear that buzzing sound."
cm "Then stop pulling, we must find another way."
scene catherine09 with dissolve
ck "So what are you going to do?"
mc "I'll find the culprits, I promise you, Catherine."
window hide
play sound "sounds/achievement.mp3"
$ mission03 = True
show missionicon03 at poslocation
$ renpy.pause(0.5, hard=True)
show textmission03 at posmissiontext
pause
cm "Stay strong, Catherine."
scene catherine03 with dissolve
ck "Easy for you to say... I can't... even take a shower with that thing on."
scene mayorsoffice01
show mayorsofficehonoka01
show mayor01
with dissolve
mk "So, did you manage to remove it?"
cm "I'm afraid not, it's too dangerous since it's booby-trapped. Did you receive a note recently?"
hide mayor01
show mayor02
with fastdissolve
mk "As a matter of fact, yes, I did. I found an anonymous letter on my desk this morning simply stating \"Don't do it\"."
hide mayor02
show mayor03
with fastdissolve
mk "I don't even understand what it might refer to!"
mc "Who's the girl behind you, Mister Mayor?"
hide mayor03
show mayor04
with fastdissolve
mk "Oh, that's just the maid. She comes in every day to clean my office, don't mind her."
cm "Mister Mayor, someone is clearly blackmailing you. The League of Justice will get to the bottom of this."
cm "And about our subvention..."
hide mayor04
show mayor02
with fastdissolve
mk "Yeah, yeah, I know. You resolve this case in complete discretion and you'll get your money, Captain MILF. Now I need to go to Town Hall, I'll trust you will find the culprits within the next four days."
mc "Oooh, four days? that's one extra day than what I thought, considering this is a MISSION."
cm "Sure thing, Mister Mayor."
scene compoundhall01d
show compoundmilf02
with fade
cm "So, what do you make of it, [name]?"
mc "Who would want to blackmail the Mayor?"
hide compoundmilf02
show compoundmilf06
with fastdissolve
cm "That is THE question. So many potential enemies spring to mind. Barbara Keen, The Mafia, The Chinese Triad. Even the Joker, just to spread chaos in Cockham...."
mc "Mmmh, where to begin?..."
hide compoundmilf06
show compoundmilf01
with fastdissolve
cm "That is for YOU to find out. But I would consider Barbara Keen to be a prime suspect considering her romantic past with the Mayor."
$ locsirens = True
window hide
play sound "sounds/skill.mp3"
show locationsirens at poslocation
$ renpy.pause(0.5, hard=True)
cm "In any case, I'm leaving you in charge of the investigation, I have too much paperwork to finish..."
mc "Roger that, Captain MILF."
jump Main

label Mission03Office:
play music "sounds/covertmusic.mp3"
scene mayorsoffice01
show mayorsofficehonoka01
with fade
mc "Oh, the maid is here. Maybe she saw something... I should interrogate her."
window hide
scene honokafullback blurred:
    zoom 1.0 xoffset 0 yoffset -920
show honokafull:
    zoom 1.0 xoffset 200 yoffset -1080    
show honokafullback blurred at honokafullbackzoombackground
show honokafull at honokafullup
$ renpy.pause(6.0, hard='True')
mc "* Mmh, she's a nice piece of maiden crumpet... *"
scene mayorsofficehonokaback
show honoka01
with dissolve
ho "Yes, sir?"
mc "Did you see anything unusual the other night? Like someone getting into Catherine's bedroom?"
hide honoka01
show honoka02
with fastdissolve
ho "What? Oh, no... I'm just the maid, I work during the day."
mc "What's your name please? I need to write it down for my investigation."
hide honoka02
show honoka03
with fastdissolve
ho "Investigation?... My name is... Honoka, sir."
mc "How long have you been working here, Honoka? And who hired you?"
hide honoka03
show honoka01
with fastdissolve
ho "Well, umh, Mister Mayor hired me. From the orphanage, to give me a chance at a better life..."
mc "Interesting. Is he abusing you by any chance? Did you try and get back at him for that?"
hide honoka01
show honoka02
with fastdissolve
ho "Abusing? Me? No, I..."
hide honoka02
show honokafrisk01
with dissolve
ho "What are you doing?"
mc "I just need to frisk you down real quick, you know, part of the investigation..."
hide honokafrisk01
show honokafrisk02
with dissolve
ho "O...kay... What are you looking for, sir?"
mc "Call me [name]. I'm a superhero but we can make do without the official titles. For the while being."
hide honokafrisk02
show honokafrisk03
with dissolve
ho "I have nothing to hide, sir!"
mc "And what's that?"
ho "It's... nothing. I've had that tattoo since I was a little girl, sir..."
mc "I see... It looks kind of new though..."
scene honokafullback blurred:
    zoom 1.0 xoffset 0 yoffset -520
show honokafrisk04
with dissolve
ho "Are we done, sir? Please, I need to get back to work!"
mc "Not quite yet, there is still one place I need to check..."
scene honokafrisk05back
show honokafrisk05
with dissolve
ho "But... What are you doing?"
mc "Just checking your cavities. For hidden suspicious items."
ho "Please, sir... * sob *"
mc "Alright, I'll let you go. For NOW. But you're still on my list of suspects."
scene mayorsofficehonokaback
show honokafrisk01
with dissolve
ho "But why? I'm just a maid, I haven't done anything wrong!"
mc "We'll see about that... Maids are notoriously naughty. VERY naughty."
$ seenhonokatattoo = True
stop music
jump Main

label Mission03Officeb:
play music "sounds/covertmusic.mp3"
scene mayorsoffice01
show mayorsofficehonoka01
with fade
mc "Honoka is here. Time to confront the little Triad hussy..."
scene mayorsofficehonokaback
show honoka01
with dissolve
ho "Yes, sir?"
mc "That's it, I KNOW it's YOU! That tattoo you have, it's a Chinese Triad tattoo, admit it!"
hide honoka01
show honoka02
with fastdissolve
ho "Well, err... Please sir, it's not my fault! I HAD to do it!"
mc "Now tell me where the key is!"
hide honoka02
show honoka03
with fastdissolve
ho "I can't sir, I can't tell you, I'm sorry! It's too DANGEROUS! For YOU too!"
mc "Dangerous? Danger is my middle name! Now get undressed, I'm doing a FULL CAVITY SEARCH this time!"
stop music
$ renpy.start_predict("v02/honokalick.webm")
play music "sounds/sexy06.mp3"
scene honokaprelick01 with fade
mc "Are you hiding it in your pussy? Or your ass? Seems to be a favorite hiding place for keys these days..."
ho "No sir, I swear!"
mc "I don't believe you, I'm gonna have to lick that pussy of yours until you squirt it out!"
scene honokalickvideo with dissolve
play channel2 "sounds/womansex05.mp3"
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
stop channel2
play sound "sounds/womancum01.mp3"
ho "AAAH, you've made me squirt!"
window hide
with fastflash
mc " * Bingo! Now where is that key? *"
$ renpy.stop_predict("v02/honokalick.webm")
scene honokalickcum02 with dissolve
play sound "sounds/moan05.mp3"
mc "Come on, squirt it out and stop plastering my face in your juices!"
window hide
with fastflash
ho "But sir, the key is not in my pussy, AAAH!"
scene honokalickcum03 with dissolve
mc "Alright, then there is but only one option left..."
ho "It's not in my ass either, please, sir!"
mc "In that case, I'll FUCK YOU INTO SUBMISSION!"
call screen usepower("usestud", "HonokaNoSeduction", "HonokaSeduction") with dissolve
label HonokaNoSeduction:
mc "Some smart-ass player tried to see what happens if I don't use my Super-Studliness superpower but I am OVERRULING him!"
mc "I'm a fucking STUD and this is not an NTR game for SISSIES! FUCK YEAH!"
label HonokaSeduction:
scene honokaprefuck01 with dissolve
mc "Are you ready for it Honoka? Or would you rather talk NOW?"
ho "Oooh, please fuck me first. I can't think right now."
scene honokaprefuck02 with dissolve
play sound "sounds/moan01.mp3"
mc "I bet you're doing a ahegao face right now. Which means you're enjoying it, aren't you?"
ho "Yes... YES SIR! FUCK ME! FUCK MY TIGHT LITTLE ASIAN PUSSY WITH YOUR WHITE MONSTER BOYCOCK!"
mc "Alright, here we go..."
label HonokaSlowFuck:
$ honokaharder = False
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
call screen honokafuckslow()
screen honokafuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFastFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceSlow")

label HonokaFastFuck:
if honokaharder == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharder = True
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
call screen honokafuckfast()
screen honokafuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceFast")

label HonokaFaceSlow:
$ honokaharder = False
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
call screen honokafacefuckslow()
screen honokafacefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaSlowFuck")

label HonokaFaceFast:
if honokaharder == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharder = True
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
call screen honokafacefuckfast()
screen honokafacefuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFastFuck")

label HonokaFuckEnd:
mc "I'm gonna fill you up with so much cum, you won't have any choice but to tell me where that key is!"
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
ho "Please pull out sir, I'll tell you where the key is, I promise!"
mc "That's a good girl, I'll cover your back in my cum then..."
stop channel1
scene honokafuckcum04 with dissolve
mc "Fuck, THAR SHE BLOWS! AAAH!"
window hide
with fastflash
ho "Sir, you will make a BIG mess and I will have to clean it up!"
mc "Tell me where the key is and I'll stop!"
window hide
with fastflash
ho "I have it, I have it, I'll give it to you, sir!"
scene honokafuckcum05 with dissolve
play sound "sounds/moan02.mp3"
ho "I'm CAKED in your scalding boycum, sir..."
mc "Yep, you've been SUPER-STUDDED! Now hand over the key, Honoka..."
stop music
scene honokafuckcum06 with dissolve
ho "Here it is. Please sir, I beg you, don't tell the Mayor it was me, I was FORCED to do it by Ada Wang! She kidnapped my family!"
mc "That's a convenient excuse... Let me think."
menu:
    "Fine, I don't want your family to get hurt because of me. (+1 Super-Hero)":
        scene honokafuckcum08 with dissolve
        call Good from _call_Good_15
        ho "Oh, thank you, kind hero, sir!"
        mc "SUPER-hero if you please."
        $ chosehonokagood = True
    "Na, I don't buy it. (+1 Super-Villain)":
        scene honokafuckcum07 with dissolve
        call Evil from _call_Evil_21
        ho "No... I'm going to lose my job... I'll be homeless and penniless.!"
        mc "Welcome to the club, I don't have money either and I'm not even a landlord."

$ mission03win = True
$ mission03end = True
scene catherine02 with fade
mc "I have the key to your chastity device, Catherine!"
scene catherine03 with dissolve
ck "Really? I'm so relieved! Please take this damn thing off NOW!"
scene catherine05 with dissolve
mc "Sure, sure, I'll do that right away. Where is the key? Oh, there it is. Right away, right away, not admiring your ass at all, just doing my job..."
scene catherinepost01 with dissolve
play sound "sounds/click.mp3"
mc "There, it's off, and thanks to me, you'll be able to go to cocaine-fuelled 70s parties again!"
window hide
play sound "sounds/winning.mp3"
show missionicon03 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
scene catherinepost02 with dissolve
play sound "sounds/kiss.mp3"
ck "How about a party right here with me. Right NOW!"
mc "And what do you have in mind?..."
ck "I need to take a shower. Why don't you join me?"
scene catherinepost03 with dissolve
mc "Fuck Yeah!"
ck "Carry me there in your strong arms... HERO."
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play channel1 "sounds/sexy05.mp3"
scene catherineshower01 with fade
ck "Don't be shy, get out of your thong... Your cock looks like it's STRAINING to come out!"
scene catherineshower02:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
ck "I'm getting in. Join me when you're ready."
scene catherineshower03 with dissolve
play channel2 "sounds/shower.mp3"
mc " * Damn, what a THICC ass... I'm getting ROCKHARD right now! * "
scene catherineshower04 with dissolve
mc "Is the water hot yet? I only take HOT showers."
ck "It's perfect. And once you join me, I'm sure it will get HOTTER!"
scene catherineshower05 with dissolve
ck "Finally, I can clean myself. Clean yourself too, I don't want to get TOO messy with you..." 
scene catherineshower06 with dissolve
stop channel2
ck "And now... Let's get STEAMY! With that MONSTERCOCK of yours! How big is it exactly?"
if age >= 20:
    mc "Fifteen inches of boymeat for you, Catherine!"
if age >= 18 and age <= 19:
    mc "Fifteen inches of teenage boymeat for you, Catherine!"
ck "Damn, that's ssso BIG! Come closer, [name]..."
scene catherineshower07 with dissolve
play sound "sounds/lick01.ogg"
ck "Mmh, just like that... Lick me clean, [name]!"
scene catherineshower08a with dissolve
mc "How about I rub my shaft against your dirty pussy to make it cleaner..."
window hide
scene catherineshowerdick
pause
if age >= 20:
    ck "Oh FUCK! Your cock is so MASSIVE! I bet you have TONS of virile sperm to unleash, don't you?"
if age >= 18 and age <= 19:
    ck "Oh FUCK! Your cock is so MASSIVE! I bet you have TONS of virile teenage sperm to unleash, don't you?"
scene catherineshower08c with dissolve
play sound "sounds/boymoan03.mp3"
mc "AAAH! Look what you've made me do with your sexy talk!"
window hide
with fastflash
ck  "You're cumming already?"
scene catherineshower08a with dissolve
ck "You've got more for me, STUD?"
scene catherineshower08c
show catherineshower08d
with dissolve
play sound "sounds/boymoan02.mp3"
mc "AH, FUCK!"
window hide
with fastflash
ck "Mmmh, yeah, pump that cream, [name], all over the place!"
scene catherineshower08a with dissolve
ck "Keep blasting, I want to see how POWERFUL your superhero monstercock is!"
scene catherineshower08c with dissolve
play sound "sounds/boymoan03.mp3"
mc "Damn it, RHAAAA!"
window hide
with fastflash
ck "Oooh, still more for ME?"
scene catherineshower08c
show catherineshower08d
with fastdissolve
play sound "sounds/boymoan.mp3"
ck "Now I wonder if you'll even have some left for my PUSSY..."
scene catherineshower08b with dissolve
mc "That was just a small appetizer. I'll show you how truly POWERFUL my cock is NOW!"
ck "You're still HARD? YES, show me how POWERFUL it is please!"
scene catherineshower09 with dissolve
ck "What? You're LIFTING ME UP ON YOUR SUPERHERO DONG???"
scene catherineshower10 with dissolve
mc "That's right, Catherine, and now I'm ready to IMPALE you on it!"
ck "You're going to fuck me MERCILESSLY? Using your POWERFUL MUSCLECOCK?"
scene catherineshower11 with dissolve
mc "You got that right!"
ck "THEN POUND IT INTO ME, I WANT TO FEEL IT TOTALLY FILLING ME UP!"
window hide

label CatherineShowerSlow:  
hide cum
hide faster
hide slower
stop music
play music "sounds/womansex03.mp3"
show catherineshowerslowvideo behind catherineshowerfastvideo
$ renpy.pause(1.0, hard='True')
hide catherineshowerfastvideo
with dissolve
if catherineshowertold01 == False:
    mc "I'll fuck you slowly at first... So you get used to my MASSIVE size..."
    window hide
    $ catherineshowertold01 = True
show faster:
     xpos 1700 ypos 500     

call screen catherineshowerslow()
screen catherineshowerslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CatherineShowerFast")

label CatherineShowerFast:
hide cum
hide faster
hide slower
mc "And now get ready for some HEAVY POUNDING!"
window hide
show catherineshowerfastvideo behind catherineshowerslowvideo
$ renpy.pause(1.0, hard='True')
hide catherineshowerslowvideo
with dissolve
ck "Oh God, yes, YES, DO IT!"
stop music
play music "sounds/womansex04.mp3"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen catherineshowerfast()
screen catherineshowerfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("CatherineShowerSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CatherineShowerEnd")

label CatherineShowerEnd:
hide cum
hide faster
hide slower
ck "Please CUM! My pussy... It's getting numb. You're STRETCHING it so much..."
mc "Hang on, just a few more fifteen-inch stabs and..."
stop music
scene catherineshowercum01 with dissolve
hide catherineshowerfastvideo
hide catherineshowerslowvideo
play music "sounds/splooge02.mp3"
play channel1 "sounds/boyorgasm01.mp3"
mc "...AAAAH, here it COMES!"
window hide
with fastflash
ck "What? But... You just came TONS and you're spewing ANOTHER MEGA-LOAD???"
scene catherineshowercum02 with dissolve
mc "You'd better believe it! RHAAA!"
play sound "sounds/womancum01.mp3"
window hide
with fastflash
ck "You cum factories must have been so BLOATED!"
scene catherineshowercum03 with dissolve
mc "You got that right! Take some more OUNCES of my virile cum!"
window hide
with fastflash
ck "Pull out, my womb is gonna EXPLODE!"
scene catherineshowercum04 with dissolve
ck "AAAH, my stomach... It's distending like it's gonna BURST!"
window hide
with fastflash
mc "I'm TRYING to pull out but I'm STUCK!"
window hide
with fastflash
ck "FORCE IT OUT, I beg you!"
scene catherineshowercum05 with dissolve
stop music
stop channel1
play sound "sounds/splooge01.mp3"
play music "sounds/boymoan02.mp3"
mc "Ah, finally! And now I can liberally DOUSE your shower room!"
stop music
window hide
with fastflash
play sound "sounds/moan01.mp3"
ck "Oh my God, your baby-batter is CASCADING out of my pussy... Ooooh!"
scene catherineshowercum06 with dissolve
mc "Your pussy must have been cleaned up pretty good by now, I think we should probably call it a day. And call Honoka to clean up the shower room."
ck "Ooh... My poor pussy..."                                                                                         
show screen calendar
show screen statscreenicon
show screen questscreenicon

$ period = 1
scene compoundhall01n
show compoundmilf01
with fade
cm "I got a call from the Mayor saying you successfully completed your mission. Well done, [name]!"
mc "Piece of cake for a SUPERHERO like me!"
hide compoundmilf01
show compoundmilf02
with fastdissolve
cm "The next missions might be trickier, so don't get overly confident, my sweet tenant..."
mc "I feel like I need to RAISE my Superpowers level..."
hide compoundmilf02
show compoundmilf05
with fastdissolve
cm "You sure do to get ready for the dangers that lie ahead. Eventually, various superheroes will help you."
mc "What about you, what will you help me for?"
hide compoundmilf05
show compoundmilf07
with fastdissolve
cm "Well. Possibly, I could help you raise your Super-Seduction... But it's a tough one, it might involve..."
mc "Sex? Sweet landlady-tenant sex?"
hide compoundmilf07
show compoundmilf04
with fastdissolve
cm "You seem awfully eager for that..."
mc "Damn right, Carol, you're smoking hot!"
hide compoundmilf04
show compoundmilf01
with fastdissolve
cm "I guess we could start off with something that doesn't involve your giant cock... Let me know when you're ready to be taught Super-Seduction LEVEL 2!"
jump MCRoomNight

label PostMissionOffice:
$ talkmission03mayor = True
scene mayorsoffice01 with fade
show mayor01 with dissolve
if mission03fail:
    mk "And what the hell are you doing here? Because of you, my daughter is STILL in a devious chastity device!"
    mc "I was coming round to check on her actually..."
    hide mayor01
    show mayor02
    with fastdissolve
    mk "Well, you can turn round and go back where you came from! You're not welcome here anymore!"
    jump Main
if mission03win:
    mk "Ah, what's-his-name-superhero-with-an-abnormally-huge-cock, glad to see you here!"
    mc "[hero], Mister Mayor, it's [hero]..."
    hide mayor01
    show mayor02
    with fastdissolve
    mk "Well, [hero], I want to extend my gratitude to you for saving my daughter from a life devoid of social scandals."
    mc "You're welcome. And?..."
    mk "And what?"
    mc "And my reward IS..."
    hide mayor02
    show mayor03
    with fastdissolve
    mk "Well, my immense gratitude! And hers too!"
    mc "Your immense gratitude which materializes INTO..."
    hide mayor03
    show mayor01
    with fastdissolve
    mk "Ah, I see where you're going at, young man. You need to fill up your inventory, is that right?"
    mc "Yes, SO..."
    hide mayor01
    show mayor02
    with fastdissolve
    mk "So you get to choose amongst these two formidable taxpayer-funded gifts."
    menu:
        "A Samurai Sword":
            jump MayorGift01
        "A piece of Kryptonite":
            jump MayorGift02
            
label MayorGift01:
mk "That's an exquisite samurai sword that was handed to me by my great-granduncle after the War. And now it is yours."
window hide
$ samuraisword = True
play sound "sounds/achievement.mp3"
show acquiredsamurai at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Fuck yeah!"
hide mayor02
show mayor01
with fastdissolve
mk "It has a a bit of blood on it, you might want to give it a swipe."
jump Main

label MayorGift02:
mk "That's a rare piece of Kryptonite I borrowed from the Museum of Extraterrestrial Minerals and forgot to return. And now it is yours."
window hide
$ inventorykryptonite = True
play sound "sounds/achievement.mp3"
show acquiredkryptonite at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Fuck yeah!"
hide mayor02
show mayor01
with fastdissolve
mk "I trust you will make good use of it, ie: NOT for some silly pranks on Superman."
mc "That... never crossed my mind, Mister Mayor..."
jump Main
    
label MayorsOffice:
if mclevel02 == False:
    scene mayorsoffice01
    show mayorsofficehonoka01
    with fade
    mc "Well, well, well. Honoka is here. Still working at cleaning the Mayor's apparently filthy desk."
    menu:
        "Talk to her (+ SEX)":
            jump HonokaSexAgain
        "Leave":
            mc "I'll quietly move away and go back to the comfort of my compound bedroom..."
            jump Main
if mclevel02:
    scene mayorsoffice01 with fade
    mc "Uhm, nobody's around. Which is strange cos I was expecting Honoka to be strutting around in her sexy French maid outfit as per usual."
    mc "Must be that leveling up business that made this scene disappear. Better go back to the compound."
jump Main
 
label HonokaSexAgain:
if chosehonokagood and spokehonoka == False:
    $ spokehonoka = True
    scene mayorsofficehonokaback
    show honoka01
    with dissolve
    mc "So, you still have your old job then? Thanks to my superhero KINDNESS."
    ho "Oh yes, thanks to YOU! Thank you sssoo MUCH, [hero]!"
    mc "Do I get a reward then?"
    hide honoka01
    show honoka02
    with fastdissolve
    ho "Well, I guess I haven't finished cleaning the desk. So we might as well make it absolutely FILTHY!"
    mc "Yeah, filthy with my CUM!"
    hide honoka02
    show honoka03
    with fastdissolve
    ho "Hopefully, the Mayor won't come home for another couple of hours..."
    jump HonokaSexAgain02
if chosehonokagood == False and spokehonoka == False:
    $ spokehonoka = True
    scene mayorsofficehonokaback
    show honoka01
    with dissolve
    mc "How come you still have your job here? Are you up to some more mischief?"
    hide honoka01
    show honoka02
    with fastdissolve
    ho "No... The Mayor... He was VERY kind to me and decided to keep me. Despite what YOU said to him!"
    mc "So be it. But you know what this means then?"
    hide honoka02
    show honoka01
    with fastdissolve
    ho "That you failed?"
    mc "No! It means \"get undressed and stick your ass on that desk\", I'm gonna lick your pussy and make you squirt!"    
    hide honoka01
    show honoka03
    with fastdissolve
    ho "Well, I guess I haven't finished cleaning the desk. So we might as well make it absolutely FILTHY!"
    mc "Yeah, filthy with my CUM!"
    hide honoka02
    show honoka03
    with fastdissolve
    ho "Hopefully, the Mayor won't come home for another couple of hours..."
    jump HonokaSexAgain02    
if spokehonoka:
    scene mayorsofficehonokaback
    show honoka01
    with dissolve
    mc "You know why I'm here Honoka?"
    hide honoka01
    show honoka03
    with fastdissolve
    ho "Err, I can guess. TO give it to me HARD and ROUGH?"
    mc "Bingo! Now get naked and spread those legs on the desk for me..."
    jump HonokaSexAgain02
    
label HonokaSexAgain02:
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
label HonokaSlowFuckb:
$ honokaharder = False
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
call screen honokafuckslowb()
screen honokafuckslowb():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFastFuckb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndb")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceSlowb")

label HonokaFastFuckb:
if honokaharder == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharder = True
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
call screen honokafuckfastb()
screen honokafuckfastb():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaSlowFuckb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndb")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFaceFastb")

label HonokaFaceSlowb:
$ honokaharder = False
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
call screen honokafacefuckslowb()
screen honokafacefuckslowb():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceFastb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndb")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaSlowFuckb")

label HonokaFaceFastb:
if honokaharder == False:
    ho "Please sir... AAAH! My pussy... I want to be fucked HARDER!"
    $ honokaharder = True
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
call screen honokafacefuckfastb()
screen honokafacefuckfastb():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HonokaFaceSlowb")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HonokaFuckEndb")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HonokaFastFuckb")

label HonokaFuckEndb:
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
jump Main