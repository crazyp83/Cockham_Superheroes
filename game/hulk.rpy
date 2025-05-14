label HulkCompound:
play music "sounds/underworld.mp3"
if mclevel02 and hulkharem:
    scene hulknewmeet with fade
    menu:
        "Jacuzzi Sex":
            mc "Ah, there you are, smiling and ready for a HOT jacuzzi session with your HAREM MASTER!"
            hu "Oooh, I can't wait, [name]!"
            jump HulkJacuzziSex
        "Gym session":
            mc "Ah, there you are, smiling and ready for a gym session!"
            hu "Oooh, I can't wait, [name]!"
            jump HulkGym
if seenhulk01 == False:
    scene hulkcompound00 with fade
    mc "This place doesn't look familiar, I think I'm lost. Damn, this compound is just too big..."
    jump SheHulkFirst
if seenhulk01 and inventorysedative == False:
    scene hulkcompound00 with fade
    mc "Let's visit the SHE-HULK again, just to check on her..."
    scene hulkcompound06 with dissolve    
    play sound "sounds/hulkgrowl.mp3"
    $ renpy.pause(1.0, hard=True)
    mc "It appears she is still as angry as ever... No need to hang around until I find a way to free her. I should probably check my quest hints."
    mc "By clicking on the small down arrow at the bottom of the quest screen to get to the next page, since it's the fourth quest already."
    jump Main
if seenhulk01 and inventorysedative and questhulkcompleted == False:
    scene hulkcompound00 with fade
    mc "Let's visit the SHE-HULK again..."
    jump FreeHulk
if seenhulk01 and inventorysedative and questhulkcompleted:
    scene hulkprefuck20 with fade
    mc "Time for some HO-HO-HOT SEX, She-Hulk! My dong is HARD and READY TO PLEASE!"
    $ hulksexneed = 0
    menu:
        "See scene":
            hu "Let me get on my knees, so I can suck on your great big non-green whopper then!"
            jump HulkSexAgain
        "Skip scene":
            scene hulkprefuck20 with dissolve
            mc "There, I did my dirty deed, and now I can go."
            jump Main

label SheHulkFirst:
$ seenhulk01 = True
play sound "sounds/hulkgrowl.mp3"
$ renpy.pause(1.0, hard=True)
mc "What's that noise? It's coming from over there, let's have a closer look."
scene hulkcompound01 with dissolve
mc "Hang on, what is She-Hulk doing down here??? NAKED to boot."
scene hulkcompound02 with dissolve
play channel1 "sounds/wank.mp3"
mc "And Batman??? The dirty pervert is having a wank!"
scene hulkcompound03 with dissolve
stop channel1
play sound "sounds/boymoan02.mp3"
bm "Uh? Why are you here? Go away, dammit, I'm busy! AAAH!"
mc "You're jerking off to... She-Hulk??? That's disgusting!"
scene hulkcompound04 with dissolve
stop sound
bm "No I was not! I... had an itch or something. My costume gets quite stuffy, so shut up!"
mc "I'm going to report you to Captain MILF!"
bm "Oh yeah? AH AH AH! Nothing will come of it! I bankroll this League, remember? Without me, you guys are BROKE!"
scene hulkcompound05 with dissolve
mc "And why is She-Hulk tied up like that, that's just PLAIN WRONG!"
scene hulkcompound06 with dissolve
play sound "sounds/hulkgrowl.mp3"
bm "Cos she's NUTS, that's why!"
mc "Does Captain MILF know about this?"
scene hulkcompound04 with dissolve
bm "Well, why don't you ask her? * snickers * Now if you'll excuse me, I'm a busy man, I need to go and fight some CRIME!"
window hide
play sound "sounds/skill.mp3"
$ questhulk = True
show questshehulk at poslocation
$ renpy.pause(0.5, hard=True)
show questhulktext at posmissiontext
pause
mc "You're a sick little man, Batman."
bm "Oooh, says the guy who IMPREGNATED Wonder Woman while she was bound and naked!"
stop music
jump Main

label FreeHulk:
scene hulkprefuck01 with fade
mc "Ah there she is. Damn she's TALL!"
scene hulkprefuck02 with dissolve
mc "I should probably inject the sedative on her butt. That's usually where doctors stick syringes."
scene hulkprefuck03 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "Uh oh, she doesn't like the sound of it."
call screen usepower("useagility", "HulkNoAgility", "HulkAgility") with dissolve

label HulkNoAgility:
scene hulknoagility01 with dissolve
play sound "sounds/punch.mp3"
hu "GRRRR!"
scene hulknoagility02 with dissolve
mc "Damn! I think I'll come back another time. When she's less angry and I'm more Super-Agile..."
jump Main

label HulkAgility:
scene hulkprefuck04 with dissolve
mc "Phew, that was a close call. I wouldn't have liked to be on the receiving end of a mighty punch from HER."
scene hulkprefuck05 with dissolve
mc "Now, she doesn't seem to be able to turn around, so I'll just stick this right...."
scene hulkprefuck06 with dissolve
mc "...here!"
scene hulkprefuck07 with dissolve
mc "It seems to be having an effect..."
scene hulkprefuck08 with dissolve
hu "Wh... Who are you?"
mc "I'm [hero], the NEW SUPER-HERO from the League. And I'm here to free you. Bur first, you need to tell me why you are so angry all the time."
hu "I... Men are afraid of me! They won't get near me, they think I'm a freak... It makes me sad and... angry."
scene hulkprefuck09 with dissolve
mc "I see. You're sexually frustrated. Well, fear not, cos I have exactly what you need."
stop music
scene hulkprefuck10 with dissolve
play sound "sounds/intromusic.mp3"
mc "A SUPER-COCK!"
hu "Oh! It's so beautiful!"
scene hulkprefuck10 with dissolve
mc "So, promise that if I free you, you won't attack me and if I satisfy your sexual needs, say, once a week, you'll remain calm and you won't destroy half the city."
scene hulkprefuck11 with dissolve
hu "YES, I PROMISE! Just please fuck me with that giant cock NOW! And also take those magnetic cuffs off me!"
scene hulkprefuck12 with dissolve
mc "Sure, that was the plan. I saw the switch of the magnetic coil that is trapping you on my way in. I'll go switch it off. And then, SWEE-EEET LOVE with a giant muscle big-titted babe!"
hu "Mnmh, you really know how to talk to women, [hero]."
scene hulkprefuck13 with dissolve
hu "Finally, I can take these horrible coilcuffs off me!"
menu:
    "Watch sex scene":
        jump HulkSex
    "Skip sex scene cos I'm a frail individual who can't take monster muscle female-on man sex":
        jump HulkNoSex

label HulkSex:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop sound
scene hulkpreblow01 with dissolve
play music "sounds/sexy07.mp3"
mc "Err, How tall are you She-Hulk?"
hu "I've grown to... 6ft10. Let me get on my knees to your level."
label HulkSexAgain:
scene hulkpreblow02 with dissolve
hu "Wow! I'm just eye level with your great big monster schlong!"
if questhulkcompleted:
    mc "All the better to suck m..."
if questhulkcompleted == False:
    mc "Then I guess we'll start with a blowj..."

play channel1 "sounds/boymoan02.mp3"
label HulkPreBlowSlow: 
window hide
hide cum
hide faster
hide slower
show hulkpreblowslowvideo behind hulkpreblowfastvideo
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/blow01.mp3"
hide hulkpreblowfastvideo with dissolve
mc "Oh Fuck! You're gobbling me up so good!"
show nexticon:
     xpos 1750 ypos 1020        
show faster:
     xpos 1700 ypos 500     

call screen hulkpreblowslow()
screen hulkpreblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkPreBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowSlowa")

label HulkPreBlowFast:
show hulkpreblowfastvideo behind hulkpreblowslowvideo
window hide
hide cum
hide faster
hide slower
$ renpy.pause(1.0, hard='True')
mc "Yeah, now slide your throat down my horsedick FASTER!"
window hide
hide hulkpreblowslowvideo with dissolve
show nexticon:
     xpos 1750 ypos 1020        
show slower:
     xpos 50 ypos 500     

call screen hulkpreblowfast()
screen hulkpreblowfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkPreBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowSlowa")

label HulkBlowSlowa:
hide nexticon
hide hulkpreblowslowvideo
hide hulkpreblowfastvideo
scene hulkpreblow03

label HulkBlowSlow:
$ hulkblowtalkfast = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowslowvideo behind hulkblowpovslowvideo
show hulkblowslowvideo behind hulkblowfastvideo
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/blow02.mp3"
hide hulkblowpovslowvideo
hide hulkblowfastvideo
with dissolve
if hulkblowtalkslow == False:
    mc "Let me help you, I want to PUMMEL your throat!"
    $ hulkblowtalkslow = True
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkblowslow()
screen hulkblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkBlowPOVSlow")

label HulkBlowFast:
$ hulkblowtalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowfastvideo behind hulkblowpovfastvideo
show hulkblowfastvideo behind hulkblowslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowpovfastvideo
hide hulkblowslowvideo
with dissolve
if hulkblowtalkfast == False:
    mc "Oh Yeah, that's great... I'm so hard for you, hot She-Hulk!"
    $ hulkblowtalkfast = True
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkblowfast()
screen hulkblowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkBlowPOVFast")

label HulkBlowPOVSlow:
$ hulkblowtalkfast = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowpovslowvideo behind hulkblowslowvideo
show hulkblowpovslowvideo behind hulkblowpovfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowslowvideo
hide hulkblowpovfastvideo
with dissolve
if hulkblowtalkslow == False:
    mc "Let me help you, I want to PUMMEL your throat!"
    $ hulkblowtalkslow = True
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkblowpovslow()
screen hulkblowpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkBlowSlow")

label HulkBlowPOVFast:
$ hulkblowtalkslow = False
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
show hulkblowpovfastvideo behind hulkblowfastvideo
show hulkblowpovfastvideo behind hulkblowpovslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkblowfastvideo
hide hulkblowpovslowvideo
with dissolve
window hide
if hulkblowtalkfast == False:
    mc "Oh Yeah, that's great... I'm so hard for you, hot She-Hulk!"
    $ hulkblowtalkfast = True
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkblowpovfast()
screen hulkblowpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkBlowPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkBlowEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkBlowFast")

label HulkBlowEnd:
window hide
hide cum
hide faster
hide slower
hide pov
hide sceneicon
mc "I'm getting close... Your sucking skills are just too much to..."
hide hulkblowfastvideo
hide hulkblowpovslowvideo
hide hulkblowslowvideo
hide hulkblowpovfastvideo
scene hulkblowcum01
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAAH, you're making me spill my sauce!"
window hide 
with fastflash
hu "GGllll..."
scene hulkblowcum02 with dissolve
mc "RHAAA! Take my spunk DEEP down your throat!"
window hide
with hpunch
mc "So damn GOOO-OOOOD!!!!"
scene hulkblowcum03 with dissolve
stop channel2
mc "AAAH, still NUTTING BIG TIME!!!"
window hide
with fastflash
hu "Cover my face with your SUPER-SPUNK!"
stop channel1
scene hulkblowcum04 with dissolve
play sound "sounds/panting.mp3"
hu "You're FILTHY! You just come and come, like a SEX MACHINE!"
mc "You're the one who made me blow SUPER-HARD, She-Hulk."
scene hulkblowcum05 with dissolve
hu "Now I want this MONSTERCOCK up my pussy! Get on the floor!"
mc "Uh oh..."
scene hulkprefuck14 with dissolve
hu "Let me stick this fuckstick where it belongs..."
scene hulkprefuck15 with dissolve
hu "Mmh, right there, it just fits perfectly..."

label HulkFuckSlow:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckslowvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex06.mp3"
hu "UHH OOOH, I needed a HUGE cock so bad!"
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen hulkfuckslow()
screen hulkfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkFuckHardSlow")

label HulkFuckFast:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckfastvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex06.mp3"
if age >= 20:
    hu "This MASSIVE HORSEDICK is sssooo good! AAAH!"
if age >= 18 and age <= 19:
    hu "This MASSIVE TEENAGE HORSEDICK is sssooo good! AAAH!"
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen hulkfuckfast()
screen hulkfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkFuckHardFast")

label HulkFuckHardSlow:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckharderslowvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex05.mp3"
hu "I want it HARDER and DEEPER!"
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen hulkfuckharderslow()
screen hulkfuckharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkFuckSlow")

label HulkFuckHardFast:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
scene hulkfuckharderfastvideo with dissolve
$ renpy.pause(1.0, hard='True')
play channel2 "sounds/womansex05.mp3"
window hide
if age >= 20:
    hu "Your MONSTERCOCK is drilling me so DEEP!!!"
if age >= 18 and age <= 19:
    hu "Your TEENAGE MONSTERCOCK is drilling me so DEEP!!!"
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen hulkfuckharderfast()
screen hulkfuckharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkFuckHardSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("HulkFuckFast")

label HulkFuckEnd:
window hide
hide cum
hide faster
hide slower
hide harder
hide softer
hu "I want you to BLAST inside my snatch! NOW!"
window hide
$ renpy.pause(1.0, hard='True')
scene hulkfuckcum01 with dissolve
stop channel2
play channel2 "sounds/splooge01.mp3"
play channel1 "sounds/boyorgasm01.mp3"
mc "Yeah, AAAAH, FUCK!"
window hide
with hpunch
hu "Give me MORE SPUNK [hero]!"
scene hulkfuckcum02 with dissolve
hu "You're FILLING ME UP! I've never been filled so much in my life!"
window hide
with hpunch
mc "Take my SUPER-SPUNK, SHE-HULK!"
play sound "sounds/moan05.mp3"
hu "Pull out and dump the rest on me, [hero]!"
scene hulkfuckcum03 with dissolve
stop channel2
play sound "sounds/splooge03.mp3"
hu "Cover my body in your scalding scum!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "FUCK YEAH! RHAAA!"
scene hulkfuckcum04 with dissolve
stop channel1
play sound "sounds/moan01.mp3"
hu "Mmmh, that was so nice of you... I really needed that."
mc "Happy to oblige."
scene hulkfuckcum05 with dissolve
hu "I hope you still have some cream left in your bull-balls. There's another hole that NEEDS to be filled!"
mc "I'm still ROCK-HARD for you, She-Hulk, don't you worry! Let me demonstrate my POWER!"
scene hulkfuckcum06 with dissolve
hu "Oooh, you're lifting me up with such ease!"
scene hulkfuckcum07 with dissolve
mc "That's cos I'm SUPER-STRONG, on top of being SUPER-HUNG!"
hu "Please FUCK me HARD in the ass! I NEED your young GIANT cock in there!!!"
scene hulkanalprefuck01 with dissolve
if age >= 20:
    hu "Don't hold back, I want ALL 15 inches of prime fuckmeat!"
if age >= 18 and age <= 19:
    hu "Don't hold back, I want ALL 15 inches of prime teen fuckmeat!"
scene hulkanalprefuck02 with dissolve
mc "Don't worry, I'll definitely make them fit, even if I have to FORCE them in."

label HulkAnalFuckSlow:
$ hulkanalfasttalk = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckslowvideo behind hulkanalfuckfastvideo
show hulkanalfuckslowvideo behind hulkanalfuckbackslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
if hulkanalslowtalk == False:
    if age >= 20:
        hu "Mmmh, just like that... Your giant cock... in my ass..."
    if age >= 18 and age <= 19:
        hu "Mmmh, just like that... Your giant teenage cock... in my ass..."
    $ hulkanalslowtalk = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen hulkanalfuckslow()
screen hulkanalfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkAnalFuckFrontSlow")

label HulkAnalFuckFast:
$ hulkanalslowtalk = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckfastvideo behind hulkanalfuckslowvideo
show hulkanalfuckfastvideo behind hulkanalfuckbackfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckslowvideo
hide hulkanalfuckbackfastvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
if hulkanalfasttalk == False:
    mc "That ass needs to be pounded HARDER and FASTER!"
    $ hulkanalfasttalk = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show assview:
     xpos 1700 ypos 500     
call screen hulkanalfuckfast()
screen hulkanalfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkAnalFuckFrontFast")

label HulkAnalFuckFrontSlow:
$ hulkanalfasttalk = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckbackslowvideo behind hulkanalfuckslowvideo
show hulkanalfuckbackslowvideo behind hulkanalfuckbackfastvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckslowvideo
hide hulkanalfuckbackfastvideo
with dissolve
play channel1 "sounds/womansex01.mp3"
if hulkanalslowtalk == False:
    if age >= 20:
        hu "Mmmh, just like that... Your giant cock... in my ass..."
    if age >= 18 and age <= 19:
        hu "Mmmh, just like that... Your giant teenage cock... in my ass..."
    $ hulkanalslowtalk = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkanalfuckbackslow()
screen hulkanalfuckbackslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckSlow")

label HulkAnalFuckFrontFast:
$ hulkanalslowtalk = False
window hide
hide cum
hide slower
hide faster
hide sceneicon
hide assview
show hulkanalfuckbackfastvideo behind hulkanalfuckfastvideo
show hulkanalfuckbackfastvideo behind hulkanalfuckbackslowvideo
$ renpy.pause(1.0, hard='True')
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
with dissolve
play channel1 "sounds/womansex04.mp3"
if hulkanalfasttalk == False:
    mc "That ass needs to be pounded HARDER and FASTER!"
    $ hulkanalfasttalk = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen hulkanalfuckbackfast()
screen hulkanalfuckbackfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkAnalFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkAnalFuckFast")

label HulkAnalFuckEnd:
hide cum
hide assview
hide faster
hide slower
hide sceneicon
window hide
hu "* Puff * I... can't take it anymore, you're PULVERIZING my ass... Please fill it up NOW!"
hide hulkanalfuckbackfastvideo
hide hulkanalfuckfastvideo
hide hulkanalfuckbackslowvideo
hide hulkanalfuckbackslowvideo
scene hulkanalcum01
stop channel1
play channel1 "sounds/splooge01.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "There you go, my third MEGA-LOAD of the day! RHAAA!"
window hide 
with hpunch
hu "You're such a STALLION! You're cumming so much AGAIN!"
scene hulkanalcum02 with dissolve
play sound "sounds/moan05.mp3"
hu "Yes, Yes, I'm cumming too! Your spunk in my ass is making me EXPLODE!"
window hide
with fastflash
mc "CUM with me, She-HULK! RHAAA!"
scene hulkanalcum03 with dissolve
play sound "sounds/boymoan05.mp3"
mc "Take more, take ALL OF MY CUM, AAAH!"
window hide
with hpunch
play sound "sounds/moan04.ogg"
hu "AAAHHH! My ass is already full to the brim!"
scene hulkanalcum04 with dissolve
play sound "sounds/moan04.ogg"
stop channel1
stop channel2
hu "Mmmh, are you alright back there?"
play sound "sounds/panting.mp3"
mc "Rhhhhooo...."
hu "You poor thing, She-Hulk totally DRAINED your bull-balls. And now you're out of commission and need to go back to your bedroom..."
$ questhulkcompleted = True
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label HulkNoSex:
scene hulkprefuck20 with dissolve
$ questhulkcompleted = True
mc "There, I ravaged your holes, even though there are no witnesses to the sexual carnage, and now you are sexually satisfied for a whole week!"
mc "However, I will still need to come back here to fuck you behind closed screens on a regular basis if you are to remain calm and docile. GOT IT, PLAYER?"
jump Main

label HulkGym:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
scene hulkgym01 with fade
mc "* Nice outfit. Totally hugs her muscled booty... *"
scene hulkgym02 with dissolve
if hulkseengym == False:
    hu "What's this ring over there?"
    mc "That's the fighting ring. Considering your... anger, we'll do some other training before you're allowed to go there."
    hu "What do you want me to do then?"
if hulkseengym:
    hu "What do you want me to do today?"
menu:
    "Punching Bag Training":
        mc "Let's see how you deal with that punching bag..."
        jump HulkPunchingBag    
    "Strength Training":
        mc "Let's see how strong you TRULY are..."
        jump HulkStrengthGym

label HulkPunchingBag:
scene hulkgym16 with dissolve
mc "First, you should do some exercise to get yourself ready. Wrap your legs around the punching bag and do some ab crunches."
scene hulkgym17 with dissolve
hu "Like this?"
mc "Yeah, just like that. I'll watch from afar. And from above too."
window hide
play music "sounds/gymmusic.mp3"

label HulkGymLiftSide:
hide topicon
hide sideicon
hide nexticon
show hulkgymliftsidevideo behind hulkgymlifttopvideo
$ renpy.pause(1.0, hard='True')
hide hulkgymlifttopvideo
with dissolve
mc "* Damn, she makes it look so easy. *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    

call screen hulkgymliftside()
screen hulkgymliftside():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftTop")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEnd")

label HulkGymLiftTop:
hide topicon
hide sideicon
hide nexticon
show hulkgymlifttopvideo behind hulkgymliftsidevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymliftsidevideo
with dissolve
mc "* Even better view even though I'm not actually there. *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymlifttop()
screen hulkgymlifttop():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftSide")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEnd")


label HulkGymLiftEnd:
hide topicon
hide sideicon
hide nexticon
mc "Now that she's getting all sweaty, I should use my Super-Senses and see her doing it in the nude... Ain't even gonna ask for permission from the player."

label HulkGymLiftSideNude:
hide topicon
hide sideicon
hide nexticon
show hulkgymliftsidenudevideo behind hulkgymlifttopnudevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymlifttopnudevideo
with dissolve
mc "* Now we're talking. Naked She-Hulk... *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymliftsidenude()
screen hulkgymliftsidenude():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftTopNude")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndNude")

label HulkGymLiftTopNude:
hide topicon
hide sideicon
hide nexticon
show hulkgymlifttopnudevideo behind hulkgymliftsidenudevideo
$ renpy.pause(1.0, hard='True')
hide hulkgymliftsidenudevideo
with dissolve
mc "* Look at those abs flexing so HARD! *"
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show topicon:
     xpos 1650 ypos 500    
call screen hulkgymlifttopnude()
screen hulkgymlifttopnude():
    modal True
    button:
        xpos 1650
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkGymLiftSideNude")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkGymLiftEndNude")

label HulkGymLiftEndNude:
stop music
scene hulkgym18 with dissolve
mc "I think you've trained enough, you can come down now."
scene hulkgym19 with dissolve
play sound "sounds/femalegrunt01.mp3"
hu "I liked this exercise, it's making my muscles SWELL UP!"
mc "I see that. Just stand behind the punching bag and wait for me to begin the PROPER training."
scene hulkgym03 with dissolve
mc "Okay, are you ready?"
hu "Ready for what?"
scene hulkgym04 with dissolve
play sound "sounds/punch.mp3"
mc "Well, for THAT!"
hu "What was that for?"
scene hulkgym03 with dissolve
mc "I see. Not enough for you?"
scene hulkgym05 with dissolve
play sound "sounds/punch.mp3"
mc "Then take this!"
scene hulkgym06 with dissolve
hu "I still don't get it. What are you trying to do exactly?"
mc "Push it back as hard as you can, I'll show you!"
scene hulkgym07 with dissolve
play sound "sounds/whoosh.mp3"
hu "Like this?"
scene hulkgym08 with dissolve
play sound "sounds/punch.mp3"
mc "Hey!"
scene hulkgym09 with dissolve
play sound "v032/ouch.mp3"
hu "What happened, are you alright? Why didn't you simply stop the punching bag?"
scene hulkgym10 with dissolve
mc "You... kind of hit it too hard. Let's do some stretching to get you more supple."
scene hulkgym11 with dissolve
hu "You're the one who told me to hit it hard, remember?"
mc "Yeah, sure, but I didn't expect you to be that strong... Now bend your body to the side..."
scene hulkgym12 with dissolve
hu "Like this?"
mc "Almost perfect. I'll give you a slight nudge..."
scene hulkgym13 with dissolve
mc "Right here..."
scene hulkgym14 with dissolve
play sound "sounds/punch.mp3"
hu "Don't touch my tits when I'm stretching, it makes me ANGRY!"
scene hulkgym15 with dissolve
play sound "v032/ouch.mp3"
mc "I.... I think I need to find a steak to put on my jaw. Thanks God we have a huge supply of them in the kitchen..."
hu "So it's over? It's YOUR fault! I'll do some stretching ON MY OWN while you nurse that well-deserved injury!"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
jump Main

label HulkStrengthGym:
scene hulkgym20 with dissolve
mc "This is Superman's own Kryptonium kettlebell. Not to be confused with Kryptonite, which the weakling wouldn't be able to lift at all."
scene hulkgym21 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "Even I can barely move it and I'm Super-Strong. Level 2 to be more precise."
hu "Level 2?"
scene hulkgym22 with dissolve
play sound "sounds/panting.mp3"
mc "Yeah, on a scale that goes to 3 apparently. Now let's see how you fare with it. Try and pick it up."
scene hulkgym23 with dissolve
mc "It weighs 100 tons."
hu "Is that a lot?"
mc "Err, YEAH! It's the heaviest thing you'll find in this gym, so be careful with it, don't drop it or anything."
scene hulkgym24 with dissolve
hu "Oh, I thought it would be heavier that that."
mc "What do you mean?"
scene hulkgym25 with dissolve
hu "Well, it's like, super-light really."
mc "You're kidding me, right?"
scene hulkgym26 with dissolve
hu "No. Look, I can lift it easily with just one arm."
mc "What the????"
scene hulkgym27 with dissolve
hu "I bet I could even crush it in my hand."
play sound "sounds/femalegrunt01.mp3"
mc "I doubt that. Kryptonium is unbreakable."
scene hulkgym28 with dissolve
play sound "sounds/bonecrack.mp3"
hu "SHe-Hulk can BREAK anything she wants!"
mc "Err, yeah, I see that."
scene hulkgym29 with dissolve
mc "Uh oh, you droppped it now..."
scene hulkgym30 with dissolve
play sound "v06/thump.mp3" volume 2.0
mc "The whole building is SHAKING!!!"
scene hulkgym10 with dissolve
mc "Damn, you almost BROKE THE FLOOR, you've got to be more careful."
scene hulkgym31 with dissolve
hu "But I feel so GOOD! I think my muscles are..."
scene hulkgym32:
    subpixel True
    zoom 1 xpos -0.03 ypos -0.03
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/womangroan.mp3"
hu "...growing!"
mc "Damn!"
scene hulkgym33a:
    subpixel True
    zoom 0.5
    ease 8.0 zoom 1.0 xpos -0.3 ypos -0.2    
$ renpy.pause(4.0, hard='True') 
with dissolve
mc "Yeah, those biceps are definitely BIGGER and even more MENACING!"
scene hulkgym33b with dissolve
mc "* And they look even better with Super-Senses activated, he he... *"
mc "That's it, I want to compare our muscled bodies, let's pose in front of the mirror, She-Hulk!"
hu "Alright, but you might not appreciate the DIFFERENCE between us two, I'm warning you!"
scene hulkgym34 with dissolve
mc "* Damn, she's right, she's twice as big as I am... I feel like a weakling next to her... *"
scene hulkgym35 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "Okay, you're asking for it, MAXIMUM MUSCLE FLEX!!!"
hu "Not bad, [name], but you still have a long way to go to reach MY size."
scene hulkgym36 with dissolve
mc "When I level up to Super-Hero Level 03, you'll see!"
hu "Maybe, but right now, my muscles feel like they're on level TEN at least!"
scene hulkgym37:
    subpixel True
    zoom 1 xpos -0.03 ypos -0.03
    ease 10 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
hu "I mean, just look at my arms. Aren't they just ENORMOUS? Doesn't it make you want to KISS THEM?"
mc "I..."
scene hulkgym38:
    zoom 0.5
with dissolve
play sound "sounds/kiss.mp3"
mc "Yes, I just NEED to kiss those MASSIVE muscles!"
scene hulkgym38:
    subpixel True
    zoom 0.5
    ease 8.0 zoom 1.0 xpos -0.4 ypos -0.4 
with fastdissolve
play sound "sounds/kiss.mp3"
$ renpy.pause(4.0, hard='True') 
play sound "sounds/kiss.mp3"
hu "Go ahead... And LICK them too."
scene hulkgym39 with dissolve
hu "Keep going, there's some MUSCLE SWEAT that needs to be LICKED UP!"
play sound "sounds/lick02.mp3"
scene hulkgym40 with dissolve
hu "You like doing this don't you? Even though you're my harem Master..."
play sound "sounds/lick03.mp3"
mc "I... err..."
scene hulkgym41 with dissolve
hu "It looks like worshipping my muscles is making you horny, [name]..."
mc "Err... No! I mean, yes. I guess."
hu "You'd better leave. What if somebody sees you like that in the gym? Your reputation would take a big blow..."
mc "I guess you're right... I'd better leave, there are no more renders to this scene anyway."
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
jump Main    