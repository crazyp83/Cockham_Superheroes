label IvyLair:
if quest05 and quest05end == False and foundflower == False:
    jump IvyQuest05a
if quest05 and quest05end == False and foundflower and floweranalyzed == False:
    jump IvyQuest05b
if quest05 and quest05end == False and foundflower and floweranalyzed:
    jump IvyQuest05c

scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
show ivy03 with dissolve
pi "You again? Pff..."
label IvyDialogues:
show ivy03:
    breathe
menu:
    "Oh, so you're back to having small-ish tits I see." if quest05end and toldtitsivy == False and ivyharem == False:
        hide ivy03
        show ivy04
        with fastdissolve
        pi "I had to FEED my plants and they were HUNGRY! And now they're HUNGRY again! For MEAT!"
        mc "Uh oh, are you talking about... MY meat?"
        window hide
        play sound "v03/rumble.mp3"
        hide ivy04
        show ivy06
        with fastdissolve
        hide ivy06
        show ivy07
        with fastdissolve
        hide ivy07
        show ivy08
        with fastdissolve
        pi "I wasn't, but now that you mention it, you DO have plenty of meat to FEED them!"
        mc "I'm out of here, you're nuts! I'll come back when you've calmed down!" 
        $ toldtitsivy  = True
        jump Main
    "Oh, so you're back to having small-ish tits I see." if quest05end and toldtitsivy == False and ivyharem:
        hide ivy03
        show ivy04
        with fastdissolve
        pi "I had to FEED my plants and they were HUNGRY! So they're back to normal, because you are EVIL and you wouldn't let me keep my huge tits!"
        mc "They're still reasonably sized. And I'm HORNY! So it's time for you to fulfill your DUTY as a SLAVE in my SUPER-VILLAIN HAREM!" 
        hide ivy04
        show ivy02
        with fastdissolve
        pi "Wh... What? You want to FUCK ME?"
        mc "Correctamundo!"
        $ toldtitsivy  = True
        jump IvyHaremSex
    "I have a proposition for you. Me, your Harem MASTER, you my SLAVE!" if quest05end and toldtitsivy and ivyharem == False and evilness <= 5 and mcmind >= 1:
        hide ivy03
        show ivy01
        with fastdissolve
        pi "And why the hell would I agree to this?"
        mc "Because I'm a SUPERHERO and you will SUBMIT to my WILL!" 
        hide ivy01
        show ivy03
        with fastdissolve
        pi "Dream on!"
        call screen usepower("usemind", "IvyHaremFail", "IvyHaremWin") with dissolve  
        label IvyHaremFail:
        pi "Oh my God, that was such a LAME attempt! What a LOSER!"
        mc "Err, ok, I might have to work on my mind control thingie, but I'll be BACK!"
        jump Main        
        label IvyHaremWin:
        $ usedmind += 1
        play sound "v031/radiation01.mp3"
        hide ivy03
        show ivy04
        with fastdissolve
        $ ivyharem = True
        pi "Yes MASTER, I will be a GOOD girl and become part of your GOOD Harem as your SEX SLAVE!"
        window hide
        play sound "sounds/achievement.mp3"
        show haremgirlivy at posharem
        $ renpy.pause(0.5, hard='True')
        show haremgirltext at posharemtext
        pause
        mc "Now that's better, let's seal the deal with some HO-O-OT SEX!"
        jump IvyHaremSex    
    "It's ME-EE! YOUR Harem MASTER!" if quest05end and toldtitsivy and ivyharem:
        hide ivy03
        show ivy04
        with fastdissolve
        pi "Yeah, so?"
        mc "I'm HORNY! So it's time for you to fulfill your DUTY as a SLAVE in my HAREM!" 
        hide ivy04
        show ivy02
        with fastdissolve
        pi "Wh... What? You want to FUCK ME SENSELESS AGAIN?"
        mc "Correctamundo!"
        jump IvyHaremSex
    "I have my eyes on you, Poison Ivy!" if evilness <= 12:
        window hide
        play sound "v03/rumble.mp3"
        hide ivy03
        show ivy06
        with fastdissolve
        hide ivy06
        show ivy07
        with fastdissolve
        hide ivy07
        show ivy08
        with fastdissolve
        pi "Good, cos I have my PLANTS on you!"
        mc "OK, you know what? I think I'll come back another time. When I'm STRONGER."
        hide ivy08
        show ivy01
        with fastdissolve
        pi "GOOD IDEA!"
        jump Main
    "Join my harem of Sexy Super-Villainesses and feel the POWER of my Super-Cock!" if evilness >= 13 and ivyharem == False:
        hide ivy03
        show ivy02
        with fastdissolve
        pi "Wow, you're some piece of work. You think I care?"
        mc "Well, you know, it's as STURDY as an OAK TRUNK and err..."
        hide ivy02
        show ivy03
        with fastdissolve
        pi "Oak trunks aren't that sturdy, because they are not flexible and can get uprooted by STRONG WINDS!"
        mc "Ah... I'll come back when I have some more convincing arguments then."
        hide ivy03
        show ivy01
        with fastdissolve
        pi "GOOD IDEA!"
        jump Main
    "Join my harem of Sexy Super-Villainesses and feel the POWER of my Super-Cock!" if evilness >= 15 and toldtitsivy and ivyharem == False and mcmind >= 1:
        hide ivy03
        show ivy02
        with fastdissolve
        pi "Wow, you're some piece of work. You think I care?"
        call screen usepower("usemind", "IvyHaremFailb", "IvyHaremWinb") with dissolve  
        label IvyHaremFailb:
        pi "Oh my God, that was such a LAME attempt! What a LOSER!"
        mc "Err, ok, I might have to work on my mind control thingie, but I'll be BACK!"
        jump Main        
        label IvyHaremWinb:
        $ usedmind += 1
        play sound "v031/radiation01.mp3"
        hide ivy03
        show ivy04
        with fastdissolve
        $ ivyharem = True
        pi "Yes MASTER, I will be a GOOD girl and become part of your EVIL Harem as your SEX SLAVE!"
        window hide
        play sound "sounds/achievement.mp3"
        show haremgirlivy at posharem
        $ renpy.pause(0.5, hard='True')
        show haremgirltext at posharemtext
        pause        
        mc "Now that's better, let's seal the deal with some HO-O-OT SEX!"
        jump IvyHaremSex    
    "I was passing by and decided to check on you." if sawivyregrow == False:
        $ sawivyregrow = True
        hide ivy03
        show ivy01
        with fastdissolve
        pi "I'm still here as you can see. You know why? Cos this is MY PLACE!"
        mc "Sure, but one of your vines is MINE now!"
        window hide
        play sound "v03/rumble.mp3"
        hide ivy01
        show ivy06
        with fastdissolve
        hide ivy06
        show ivy07
        with fastdissolve
        hide ivy07
        show ivy08
        with fastdissolve
        pi "Yeah, so?"
        mc "Ah shit, you grew ANOTHER one?"
        hide ivy08
        show ivy08b
        with fastdissolve
        pi "That's right. Plants GROW and I CONTROL their growth! Now get outta here!"
        mc "Fine, fine, I'll come back when you're... less angry at me."
        pi "GOOD IDEA!"
        jump Main        
    "I don't know why I'm here cos I have nothing to say.":
        hide ivy03
        show ivy01
        with fastdissolve
        pi "Stop wasting my time! And yours."
        jump Main

label IvyQuest05a:
scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
if mcsenses >= 1:
    mc "Mmmh, she's not around, yet something seems different, my Super-Senses tell me..."
if mcsenses == 0:
    mc "Mmmh, she's not around, yet something seems different..."
scene ivycompoundflowers:
    subpixel True
    xpos 0.0
    linear 2.0 xpos -0.1
with dissolve
mc "Still, I have a mighty manly quest, and that quest is to pick up some flowers..."
window hide
$ foundflower = True
play sound "sounds/skill.mp3"
show questivyprogress01 at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "And here they are, your days as a boob-thief are numbered, Poison Ivy! Now let's get out of here."
scene ivycompound01 with dissolve
show ivybig01 with moveinright
show ivybig01 at center:
    breathe
pi "You were saying? My days are what?"
mc "Why do you have huge tits suddenly? I KNEW IT, you've been STEALING titflesh across town, admit it!"
hide ivybig01
show ivybig02
with fastdissolve
pi "My plants NEED milk to grow even BIGGER and HEALTHIER! I am their nourishing MOTHER, like MOTHER NATURE!"
mc "You feed titmilk to your plants? That's fucking weird. Why don't you grow Bostiboobicus Giganti instead? They're known for their plant milk."
hide ivybig02
show ivybig01
with fastdissolve
show ivybig01 at center:
    breathe
pi "This plant only exists on a remote island and cannot grow in Cockham's climate. My MILK is much BETTER anyway! So get out of my way!"
mc "While I quite like your massively-enhanced bosom, I have a QUEST! And that quest is to STOP YOU from stealing boobflesh from innocent wives and mothers!"
hide ivybig01
show ivybig05
with fastdissolve
pi "WRONG decision!"
window hide
play sound "v03/rumble.mp3"
hide ivybig05
show ivybig06
with fastdissolve
hide ivybig06
show ivybig07
with fastdissolve
hide ivybig07
show ivybig08
with fastdissolve
pi "Prepare to fight! And DIE!"
stop music
play music "v03/fightmusic.mp3"
scene ivyfight01a with dissolve
mc "I'm ready, Poison Ivy! And I'll defeat you, just like last time!"
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
scene ivyfight02a with dissolve
mc "* She's coming on fast, I need to use my SUPERPOWERS QUICK! *"
call screen usepower("useagility", "IvyNoAgility", "IvyAgility") with dissolve

label IvyNoAgility:
scene ivyfight04a with dissolve
play sound "sounds/punch.mp3"
mc "* I clearly wasn't QUICK ENOUGH! *"
jump IvyAgilityNext

label IvyAgility:
scene ivyfight03a with dissolve
play sound "sounds/whoosh.mp3"
mc "* Damn, she's SUPER-FAST! *"
scene ivyfight04a with dissolve
play sound "sounds/punch.mp3"
if mcagility == 1:
    mc "* And I'm not FAST ENOUGH! *"
if mcagility >= 2:
    mc "* And I'm not FAST ENOUGH! Even with Level 2 Super-Agility! *"
label IvyAgilityNext:
scene ivyfight05a with dissolve
stop music
pi "Pff, that was too easy. Your cock might be massive, but it's USELESS against me!"
mc "Err, how about we make it best of three?"
scene ivyfight06a with dissolve
play sound "sounds/bonecrack.mp3"
pi "Feed on his MEAT, my carnivorous familiars!"
mc "AAAAH, not my sensitive cock!"
scene ivyfight07a with dissolve
pi "And now for your final gasp of air... Enjoy the view!"
play sound "sounds/panting.mp3"
mc "Uuuuh..."
scene ivyfight08a with dissolve
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play sound "v03/rumble.mp3"
pi "Mmmh, now that he's passed out, let's have some FUN with his MASSIVE DONG! You can leave, my familiars..."
play music "sounds/sexy07.mp3"
scene ivyfight09a with dissolve
pi "Let's have a peak, he clearly won't mind, HA HA HA!"
scene ivyfight08 with dissolve
pi "Even soft, it's really BIG. And to think he's only [age]... Let's get some STEEL in it!"
scene ivyfight09 with dissolve
pi "That's better, now the REAL fun can begin!"
scene ivypretwerk01 with dissolve
pi "Mmmh, his balls are so MASSIVE. I'm gonna get a lot of seedjuice out of them!"
scene ivypretwerk02 with dissolve
pi "He deserves a scent of my moist snatch. That might even revive him a little bit!"

label IvyTwerkSlow:
window hide
$ ivytwerkfast = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkslowvideo behind ivytwerkfrontslowvideo
show ivytwerkslowvideo behind ivytwerkfastvideo
show ivytwerkslowvideo behind ivytwerkbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytwerkbackground
hide ivytwerkfrontslowvideo
hide ivytwerkfastvideo
if ivytwerkslow == False:
    $ ivytwerkslow = True
    pi "It's so much fun to twerk my ass on an unconscious superhero's face!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
call screen ivytwerkslow()
screen ivytwerkslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontSlow")

label IvyTwerkFrontSlow:
$ ivytwerkfast = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkbackground behind ivytwerkslowvideo
show ivytwerkbackground behind ivytwerkfrontfastvideo
show ivytwerkfrontslowvideo behind ivytwerkslowvideo
show ivytwerkfrontslowvideo behind ivytwerkfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytwerkslowvideo
hide ivytwerkfrontfastvideo
if ivytwerkslow == False:
    $ ivytwerkslow = True
    pi "It's so much fun to twerk my ass on an unconscious superhero's face!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivytwerkfrontslow()
screen ivytwerkfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyTwerkFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkSlow")

label IvyTwerkFast:
window hide
$ ivytwerkslow = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkfastvideo behind ivytwerkslowvideo
show ivytwerkfastvideo behind ivytwerkfrontfastvideo
show ivytwerkfastvideo behind ivytwerkbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytwerkbackground
hide ivytwerkslowvideo
hide ivytwerkfrontfastvideo
if ivytwerkfast == False:
    $ ivytwerkfast = True
    pi "When he wakes up, he'll have the smell of my snatch all over his face, hee hee!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen ivytwerkfast()
screen ivytwerkfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumTrans")

label IvyTwerkFrontFast:
window hide
$ ivytwerkslow = False
hide nexticon
hide faster
hide slower
hide sceneicon
hide front
show ivytwerkbackground behind ivytwerkfrontslowvideo
show ivytwerkbackground behind ivytwerkfastvideo
show ivytwerkfrontfastvideo behind ivytwerkfrontslowvideo
show ivytwerkfrontfastvideo behind ivytwerkfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytwerkfrontslowvideo
hide ivytwerkfastvideo
if ivytwerkfast == False:
    $ ivytwerkfast = True
    pi "When he wakes up, he'll have the smell of my snatch all over his face, hee hee!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen ivytwerkfrontfast()
screen ivytwerkfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTwerkFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumTrans")

label IvyHumTrans:
hide front
hide nexticon
hide nexticon
hide faster
hide slower
hide sceneicon
scene ivyposttwerk01 with dissolve
stop channel1
pi "Let's do something else... Something that's more appropriate considering he's unconscious yet sporting a GIANT HARDON! And I want him to SPURT his SEED!"

label IvyHumSlow:
window hide
$ ivyhumfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumslowvideo behind ivyhumsideslowvideo
show ivyhumslowvideo behind ivyhumfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyhumsideslowvideo
hide ivyhumfastvideo
if ivyhumslow == False:
    $ ivyhumslow = True
    pi "Now what happens if I caress your giant dick while you're passed out I wonder?"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
call screen ivyhumslow()
screen ivyhumslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideSlow")

label IvyHumSideSlow:
$ ivyhumfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumsideslowvideo behind ivyhumslowvideo
show ivyhumsideslowvideo behind ivyhumsidefastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyhumslowvideo
hide ivyhumsidefastvideo
if ivyhumslow == False:
    $ ivyhumslow = True
    pi "Now what happens if I caress your giant dick while you're passed out I wonder?"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivyhumsideslow()
screen ivyhumsideslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHumSideFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSlow")

label IvyHumFast:
window hide
$ ivyhumslow = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumfastvideo behind ivyhumslowvideo
show ivyhumfastvideo behind ivyhumsidefastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyhumslowvideo
hide ivyhumsidefastvideo
if ivyhumfast == False:
    $ ivyhumfast = True
    pi "Maybe I should increase the pace of my snatch rubbing against your nose to trigger a response... A CUM response!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivyhumfast()
screen ivyhumfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumEnd")

label IvyHumSideFast:
window hide
$ ivyhumslow = False
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
show ivyhumsidefastvideo behind ivyhumsideslowvideo
show ivyhumsidefastvideo behind ivyhumfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyhumsideslowvideo
hide ivyhumfastvideo
if ivyhumfast == False:
    $ ivyhumfast = True
    pi "Maybe I should increase the pace of my snatch rubbing against your nose to trigger a response... A CUM response!"
window hide
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivyhumsidefast()
screen ivyhumsidefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumSideSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHumFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyHumEnd")

label IvyHumEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide sideicon
pi "Mmmh, yeah, I can feel your spermtub BEGGGING for release!"
scene ivyhumcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
pi "There you go, spurting while you're unconscious, that's just so NASTY!"
scene ivyhumcum02 with dissolve
pi "Oooh! And now, you're REALLY disgorging THICK jets of cum, aren't you?"
window hide
with fastflash
if age >= 20:
    pi "Yeah, keep going, EMPTY THOSE FAT BALLS!"
if age >= 18 and age <= 19:
    pi "Yeah, keep going, EMPTY THOSE FAT TEENAGE BALLS!"
scene ivyhumcum03 with dissolve
pi "Naughty boy! You're nutting over my thick asscheeks!"
window hide
with hpunch
mc "Ggggg..."
scene ivyhumcum04 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
pi "Oh look, you're waking up, just while you're PUMPING YOUR SEED ALL OVER YOUR FACE, HA HA HA!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "What the...?"
scene ivyhumcum05 with dissolve
play sound "sounds/splat.ogg"
pi "I should really add my own juices to your face to MARK MY TERRITORY!"
mc "Yuck!"
scene ivyhumcum06 with dissolve
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
pi "Now listen loser, I'll let you go cos it was so much fun seeing you in PAIN, but don't ever come back, you're not strong enough to beat me clearly!"
mc "Tha... Thanks for not killing me I guess."
jump Main

label IvyQuest05b:
scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
mc "Mmh, no one's around. This quest ain't progressing. Maybe I forgot about bringing the flowers to Arkham for analysis..."
jump Main

label IvyQuest05c:
scene ivycompound01 with fade
play music "v03/ivymusic.mp3"
show ivybig01 with moveinright
show ivybig01 at center:
    breathe
pi "You're back? You didn't get humiliated enough?"
mc "Err, no, I did get humiliated enough, but now I want my REVENGE!"
hide ivybig01
show ivybig05
with fastdissolve
pi "How FOOLISH of you!"
window hide
play sound "v03/rumble.mp3"
hide ivybig05
show ivybig06
with fastdissolve
hide ivybig06
show ivybig07
with fastdissolve
hide ivybig07
show ivybig08
with fastdissolve
pi "Prepare to fight! And this time, to DIE!"

play music "sounds/battlemusic.mp3"
scene duelmczoom:
    zoom 0.5
with dissolve
mc "I'm ready to fight, but not to DIE!"
window hide
show duelmczoom at duelmc
pause 4
scene duelpizoom:
    zoom 0.5
with dissolve
pi "Too bad for you..."
window hide
show duelpizoom at duelpi
pause 4
if samuraisword:
    mc "And I have a little surprise for you this time, Poison Ivy..."
    scene ivyfight10 with dissolve
    mc "My Samurai sword!"
    scene ivyfight11 with dissolve
    pi "Pff, your rusty weapon doesn't scare me!"    
    scene ivyfight12 with dissolve
    play sound "sounds/whoosh.mp3"
    mc "It should!"
    pi "NOOOOO, my precious vine! I'll make you PAY FOR THIS!"
    scene ivyfight13 with dissolve
    mc "I haven't finished..."
    scene ivyfight14 with dissolve
    play sound "sounds/whoosh.mp3"
    mc "Now I have!"
    pi "AAAAH, you're EVIL! My familiars, I will AVENGE YOU ONE DAY, I SWEAR!"
    stop music
    jump IvyFightWin

scene ivyfight01 with dissolve
play sound "sounds/fight.mp3"
window hide
show fightsign:
    xpos 0.42
    ypos 0.45    
$ renpy.pause(1, hard=True)
mc "* This time, I'll use my SUPER-COMBAT SUPERPOWER! *"
call screen usepower("usecombat", "IvyNoCombat", "IvyCombat") with dissolve

label IvyNoCombat:
scene ivyfight03 with dissolve
play sound "sounds/whoosh.mp3"
pi "Missed! And now, for my counter-attack..."
scene ivyfight04 with dissolve
play sound "sounds/punch.mp3"
mc "AAAAH!"
stop music
scene ivyfight05 with dissolve
pi "This time, I'll make sure it's your final gasp of air... Enjoy the view! While you CAN!"
play sound "sounds/bonecrack.mp3"
mc "Uuuuh..."
scene blackscreen with fade
"GAME OVER"
return
    
label IvyCombat:
scene ivyfight02 with dissolve
play sound "sounds/punch.mp3"
mc "Take that, Poison Ivy!"
scene ivyfight21 with dissolve
play sound "v03/rumble.mp3"
pi "You should do better than that, FAMLIARS, STRIKE!"
play sound "sounds/punch.mp3"
mc "Not this time, I came PREPARED!"
scene ivyfight22 with dissolve
mc "Get ready for a smackdown, Poison Ivy!"
pi "Help me, my Preciouses, HELP YOUR MISTRESS!"
scene ivyfight23 with dissolve
play sound "sounds/punch.mp3"
mc "Too late for that, you should have yielded before the fight began! You can't defeat a SEX SUPERHERO that easily!"
pi "AAAH, you're such an ANIMAL!"
scene ivyfight24 with dissolve
mc "Now let's get rid on these nuisance plants with my Super-Strength!"
pi "NOOOO! * cough * Leave my precious vines alone!"
scene ivyfight25 with dissolve
play sound "sounds/mangrunt01.mp3"
mc "I don't think so..."
play sound "sounds/bonecrack.mp3"
pi "I will avenge you, my familiars, I swear!"

label IvyFightWin:
stop music
scene ivyfight15 with dissolve
mc "Perhaps, but not today. In the meantime..."
scene ivyprefuck01 with dissolve
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy14.mp3"
mc "...you've lost the fight, and I have vanquished you Poison Ivy! So now, you'll do as you're told!"
pi "N...NO! NEVER!"
scene ivyprefuck02 with dissolve
mc "In that case, I'll have some sexy fun with you until you SUBMIT! So let me get those panties off you, you won't need them."
pi "You don't scare me! Your cock is... quite big indeed, but..."
scene ivyprefuck03 with dissolve
mc "The more you resist, the more PAINFUL it will be, Poison Ivy."
pi "You're just... a BEAST! Just get on with it, you filthy boy!"
scene ivyprefuck04 with dissolve
if age >= 20:
    mc "Now, these nice huge titties are just about the right size for my SUPERHERO MEGA-DONG!"
if age >= 18 and age <= 19:
    mc "Now, these nice huge titties are just about the right size for my SUPERHERO TEENAGE MEGA-DONG!"
play sound "sounds/moan01.mp3"
pi "My milkbags are too sensitive for a rough titfuck, they are the nourishing fertilizer for my plants!"
mc "Not anymore, they're just huge mounds of titflesh for my horny love muscle!"

play channel2 "sounds/wetmassage.mp3"
label IvyTitSlow:
window hide
$ ivytitfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitslowvideo behind ivytitfrontslowvideo
show ivytitslowvideo behind ivytitfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytitfrontslowvideo
hide ivytitfastvideo
if ivytitslow == False:
    $ ivytitslow = True
    mc "Yeah, I LOVE your ample titflesh rubbing against my shaft..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
call screen ivytitslow()
screen ivytitslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontSlow")

label IvyTitFrontSlow:
$ ivytitfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfrontslowvideo behind ivytitslowvideo
show ivytitfrontslowvideo behind ivytitfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivytitslowvideo
hide ivytitfrontfastvideo
if ivytitslow == False:
    $ ivytitslow = True
    mc "Yeah, I LOVE your ample titflesh rubbing against my shaft..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivytitfrontslow()
screen ivytitfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyTitFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitSlow")

label IvyTitFast:
$ ivytitslow = False
if ivytitfast == False:
    $ ivytitfast = True
    mc "Now I'm gonna pummel my giant cock between those soft pillows even FASTER!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfastvideo behind ivytitslowvideo
show ivytitfastvideo behind ivytitfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytitslowvideo
hide ivytitfrontfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivytitfast()
screen ivytitfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyTitCum")

label IvyTitFrontFast:
window hide
$ ivytitslow = False
if ivytitfast == False:
    $ ivytitfast = True
    mc "Now I'm gonna pummel my giant cock between those soft pillows even FASTER!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide front
show ivytitfrontfastvideo behind ivytitfrontslowvideo
show ivytitfrontfastvideo behind ivytitfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivytitfrontslowvideo
hide ivytitfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen ivytitfrontfast()
screen ivytitfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyTitFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("IvyTitCum")

label IvyTitCum:
hide cum
hide faster
hide slower
hide sceneicon
hide front
mc "Fuck yeah, I feel it coming..."    
pi "Just spew your vile load already and be gone!"
scene ivytitcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
mc "I'll come but... RHAAA!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
mc "I doubt I'll be gone after this, AAAH!"
scene ivytitcum02 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "I've got a HUGE SUPPLY of young spunk for you, Poison Ivy, YEAH!"
window hide
with fastflash
pi "Just EMPTY your fat sack, do your worst, you vile creature!"
scene ivytitcum03 with dissolve
mc "Oh yeah, you want some MORE? HERE'S SOME MOOOAAAARRRR!"
window hide
with hpunch
pi "Your filthy scum is flying EVERYWHERE!"
scene ivytitcum04 with dissolve
mc "More importantly, it's covering your ample bosom, RHAAA!"
window hide
with fastflash
pi "You're not done yet?"
scene ivytitcum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Phew, I am now. For THIS LOAD."
pi "Wh... What? You can't be serious?"
scene ivytitcum06 with dissolve
mc "I'm still hard and you still haven't told me where the antidote is. You leave me no choice but to FUCK YOU MERCILESSLY!"
scene ivytitcum07:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(1.0, hard='True')
mc "So get ready for some SERIOUS POUNDING!"
scene ivytitcum08 with dissolve
pi "I won't tell you, even if you..."
scene ivytitcum09 with dissolve
play sound "sounds/moan04.ogg"
pi "...AAAH!"
mc "You were saying? It's rude to talk with your pussy full..."
pi "I'll resist, my vaginal muscles will REJECT your pile-driving non-vegan meat!"
mc "We'll see about that! I'll begin the ploughing!"

label IvyFuckSoft:
window hide
$ ivyharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfucksoftvideo behind ivyfuckhardslowvideo
show ivyfucksoftvideo behind ivyfucksoftsidevideo
show ivyfucksoftvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ivyfuckbackground
hide ivyfuckhardslowvideo
hide ivyfucksoftsidevideo
mc "I'm gonna re-arrange your pussy in the shape of my MEGACOCK, Poison Ivy!"
window hide
pause
show harder:
    xpos 1700 ypos 500    
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckshortslow()
screen ivyfuckshortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckSoftSide")

label IvyFuckSoftSide:
$ ivyharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfucksoftvideo
show ivyfuckbackground behind ivyfuckhardsideslowvideo
show ivyfucksoftsidevideo behind ivyfucksoftvideo
show ivyfucksoftsidevideo behind ivyfuckhardsideslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ivyfucksoftvideo
hide ivyfuckhardsideslowvideo
pi "You won't get what you want from... * puff * me, I'm immune to... AAAAH, pain!"
window hide
pause
show harder:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckshortfast()
screen ivyfuckshortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckSoft")

label IvyFuckHardSlow:
if ivyharder == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharder = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckhardslowvideo behind ivyfuckhardvideo
show ivyfuckhardslowvideo behind ivyfucksoftvideo
show ivyfuckhardslowvideo behind ivyfuckhardsideslowvideo
show ivyfuckhardslowvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckbackground
hide ivyfuckhardfastvideo
hide ivyfucksoftvideo
hide ivyfuckhardsideslowvideo
window hide
pause
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckhardslow()
screen ivyfuckhardslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("IvyFuckSoft")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSideSlow")

label IvyFuckHardFast:
if ivyharder == False:
    mc "You're trying to resist but you won't for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharder = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckhardfastvideo behind ivyfuckhardslowvideo
show ivyfuckhardfastvideo behind ivyfuckhardsidefastvideo
show ivyfuckhardfastvideo behind ivyfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckbackground
hide ivyfuckhardslowvideo
hide ivyfuckhardsidefastvideo
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen ivyfuckhardfast()
screen ivyfuckhardfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSideFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyFuckEnd")

label IvyFuckHardSideSlow:
if ivyharder == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharder = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfuckhardslowvideo
show ivyfuckbackground behind ivyfucksoftsidevideo
show ivyfuckbackground behind ivyfuckhardsidefastvideo
show ivyfuckhardsideslowvideo behind ivyfuckhardslowvideo
show ivyfuckhardsideslowvideo behind ivyfucksoftsidevideo
show ivyfuckhardsideslowvideo behind ivyfuckhardsidefastvideo
$ renpy.pause(.1, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckhardslowvideo
hide ivyfucksoftsidevideo
hide ivyfuckhardsidefastvideo
window hide
pause
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckhardsceneiconslow()
screen ivyfuckhardsceneiconslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("IvyFuckSoftSide")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardSlow")

label IvyFuckHardSideFast:
if ivyharder == False:
    mc "You're trying to resist but you won't be for long. I'm gonna POUND YOU HARD AND DEEP!"
    $ ivyharder = True        
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
show ivyfuckbackground behind ivyfuckhardsideslowvideo
show ivyfuckbackground behind ivyfuckhardfastvideo
show ivyfuckhardsidefastvideo behind ivyfuckhardsideslowvideo
show ivyfuckhardsidefastvideo behind ivyfuckhardslowvideo
$ renpy.pause(.1, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ivyfuckhardsideslowvideo
hide ivyfuckhardfastvideo
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen ivyfuckhardsceneiconfast()
screen ivyfuckhardsceneiconfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyFuckHardSideSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyFuckHardFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyFuckEnd")

label IvyFuckEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide sceneicon
hide sideicon
mc "Are you giving up yet, Poison Ivy? Are you yielding to my [age]yo SUPERHERO ALPHA-DONG?"
pi "* Puff * FUCK YOU!"
stop channel1
scene ivyfuckbackground
show ivyfuckcum01
with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "Then I will flood your insides with my ALPHA-SPUNK!"
window hide
with hpunch
pi "Noooo! You BASTARD, PULL OUT!"
scene ivyfuckbackground
show ivyfuckcum02
with dissolve
mc "Pull out? Why would I do that when I'm emptying my balls directly into your WOMB, RHAAAA!"
window hide
with fastflash
stop channel1
play sound "sounds/boymoan05.mp3"
pi "I'll give you the antidote I swear! Just don't make me pregnant!"
scene ivyfuckcum03 with dissolve
mc "AAAH! still pumping! Tell me NOW where it is cos I'm NUTTING BIG TIME!"
window hide
with hpunch
pi "In my boots, now PULL OUT BEFORE IT'S TOO LATE!"
menu:
    "Keep your word and pull out (+1 Super-Hero)":
        call Good from _call_Good_7
        jump IvyCumOut
    "Keep blasting inside her and impregnate her (+1 Super-Villain)" if evilness <= 14:
        call Evil from _call_Evil_7
        jump IvyCumMore
    "Keep blasting inside her and impregnate her (+1 Super-Villain, Ivy becomes SUPER-VILLAIN HAREM GIRL)" if evilness >= 15:
        call Evil from _call_Evil_8
        jump IvyCumMore

label IvyCumOut:
stop channel2
play sound "sounds/boymoan03.mp3"
scene ivyfuckcum04a with dissolve
mc "Still gonna PLASTER your body in my cream though, FU-UUU-UCCCK!"
window hide
with hpunch
play sound "sounds/moan03.mp3"
pi "You filthy boy, I don't want your vile scum on me!"
scene ivyfuckcum04b with dissolve
play sound "sounds/boymoan05.mp3"
mc "You're in luck, I'm cumming so forcefully, it's sailing over your head, AAAH!"
window hide
with fastflash
pi "It's not true, I can feel heavy blasts on my back, LIAR!"
scene ivyfuckcum04c with dissolve
play sound "sounds/boymoan03.mp3"
mc "Here's the last of it anyway, phew!"
window hide
with fastflash
pi "Human sperm is just DISGUSTING!"
scene ivyfuckcum05a with dissolve
stop sound
mc "Yeah, well, I don't spurt pollen, sorry... Now where's that godamn primer antidote? Ah, yes I remember."
jump IvyPostFuck01

label IvyCumMore:
play sound "sounds/boymoan03.mp3"
scene ivyfuckcum03b with dissolve
mc "I lied bitch, take that! RHAAA!"
window hide
with fastflash
pi "NOOOO, you're BLASTING insde me!"
scene ivyfuckcum03c with dissolve
play sound "sounds/boymoan05.mp3"
mc "I've got some more for you, whether you like or not, RHAAA!"
window hide
with hpunch
pi "ASSHOLE! * sob*"
scene ivyfuckcum03b with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "And even MORE to come! I'm seeding you, you should like that being a plant person and all that, no?"
scene ivyfuckcum03c with dissolve
$ renpy.pause(.5, hard='True')
window hide
with hpunch
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03b with dissolve
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03c with dissolve
$ renpy.pause(.5, hard='True')
scene ivyfuckcum03b with dissolve
mc "FFUUUCCK, I totally impregnated you now, AAAH! You're MY bitch now, you hear me?"
stop channel1
stop channel2
pi "Y... Yes... * sob *"
if evilness >= 15:
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlivy at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ ivyharem = True
scene ivyfuckcum05b with dissolve
mc "Phew, that was intense... Now where's that godamn primer antidote? Ah, yes I remember."

label IvyPostFuck01:
stop music
scene ivypostfuck01 with dissolve
mc "Now let's see those boots..."
window hide
play sound "sounds/skill.mp3"
show questivyprogress03 at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Time to go back to the CCPD and tell everyone I'm da man! DA SUPER-MAN even!"

scene sophiaoffice10 with fade
cs01 "I hope you come back with good news, [hero]."
mc "I sure do, Captain Sawyer, I soundly defeated Poison Ivy and I now have the antidote!"
scene sophiaoffice16 with dissolve
so "Really? Oh my God, this is the most exciting day of my life, even better than when one of my students went as far as lifting my skirt in the shool corridor! Please give me that antidote!"
cs01 "Please drink only a small amount, we need to make large quantities out of it for the other inflicted women, I'm sure Vayne Industries will oblige."
play music "sounds/sexy04.mp3"
scene sophiaoffice17 with dissolve
mc "And I would suggest you take your top off, you wouldn't want to rip your bra..."
cs01 "* sigh *"
scene sophiaoffice18 with dissolve
play sound "v032/gulp.mp3"
cs01 "That's enough Mrs Porker!"
scene sophiaboobsmall with dissolve
mc "Now let's see if it worked... In real-time."
show sophiaboobgrowvideo
$ renpy.pause(1.0, hard='True')
hide sophiaboobgrowvideo
show sophiaboobbig
play sound "sounds/wow.mp3"
so "Wow!"
show nexticon:
    xpos 1750 ypos 1020    
show slowmoicon:
     xpos 1700 ypos 500     
call screen sophiaslowmo()
screen sophiaslowmo():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBoobsSlowmo")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBoobsEnd")    

label SophiaBoobsSlowmo:
play sound "v032/wowslow.mp3"
hide slowmoicon
hide nexticon
hide sophiaboobbig
show sophiaboobgrowslowvideo
$ renpy.pause(2.97, hard='True')
hide sophiaboobgrowslowvideo
show sophiaboobbig
label SophiaBoobsEnd:
hide nexticon
hide slowmoicon
mc "Wow indeed..."
scene sophiaoffice19 with dissolve
play sound "sounds/moan03.mp3"
so "I just LOVE my new big tits! What about you, Mr [hero]?"
scene sophiaoffice20 with dissolve
mc "I can safely say that I love them too."
so "Oh my God, you've grown BIGGER too, haven't you?"
cs01 "Now this is highly inappropriate, Mrs Porker doesn't need to see your giant menacing phallus, she's a married woman! And a mother might I add."
scene sophiaoffice19 with dissolve
so "Oh but I don't mind, Captain Sawyer! My hubby, he's... I NEED to feel wanted and this boy makes me feel a whole WOMAN again after three years of dev neglect!"
scene sophiaoffice21 with dissolve
cs01 "In that case, I want in. [hero] needs to be punished for this outrageously lewd display. And YOU need to be punished for gulping down too much of the antidote..."
so "But I left some in the vial, I swear!"
scene sophiaoffice22 with dissolve
cs01 "[hero], don't you agree that Mrs Porker has broken the law and deserves a severe punishment?"
mc "I sure do, Captain Sawyer."
if age >= 20:
    cs01 "Do you agree that getting pummeled by your 18-inch superhero cock would constitute an adequate sentence?"
if age >= 18 and age <= 19:
    cs01 "Do you agree that getting pummeled by your 18-inch superhero teenage cock would constitute an adequate sentence?"
mc "Ooh yeah! Perfectly adequate!"
scene sophiaoffice23 with dissolve
cs01 "Then let's get her ready for her sentence!"
play sound "sounds/kiss.mp3"
window hide 
with hpunch
so "Oooh! I'm really going to get PUNISHED this time!"
play sound "sounds/moan01.mp3"
scene sophiaoffice24 with dissolve
mc "Interesting pose..."
cs01 "That way, I can lick her pussy while you take her from the other end."
scene sophiaoffice25 with dissolve
so "Oooh, Captain Sawyer!"
play sound "sounds/slurp.mp3"
mc "I'm gonna have to kneel to fuck her mouth properly then."
scene sophiapreblow01 with dissolve
so "Your cock is just... too MASSIVE, Mr Officer [hero]!"
cs01 "Your sentence includes gagging on a monstercock, Mrs Porker!"
mc "Also, the dev somehow always manages to make it fit."
scene sophiapreblow02 with dissolve
play sound "sounds/moan04.ogg"
mc "See? It fits just fine..."
stop sound
play channel1 "v032/blow03.mp3"

label SophiaBlowSlow:
window hide
$ sophiablowfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowslowvideo behind sophiablowtopslowvideo
show sophiablowslowvideo behind sophiablowfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowtopslowvideo
hide sophiablowfastvideo
if sophiablowslow == False:
    $ sophiablowslow = True       
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show topicon:
     xpos 50 ypos 500     
call screen sophiablowslow()
screen sophiablowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlow")

label SophiaBlowFrontSlow:
$ sophiablowfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowtopslowvideo behind sophiablowslowvideo
show sophiablowtopslowvideo behind sophiablowtopfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowslowvideo
hide sophiablowtopfastvideo
if sophiablowslow == False:
    $ sophiablowslow = True
    mc "I'll go slowly to let your throat get used to the 11-inch girth of my super-sized dong..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiablowtopslow()
screen sophiablowtopslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaBlowFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlow")

label SophiaBlowFast:
$ sophiablowslow = False
if sophiablowfast == False:
    $ sophiablowfast = True
    mc "I think your throat can take some FASTER skull-fucking now!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowfastvideo behind sophiablowslowvideo
show sophiablowfastvideo behind sophiablowtopfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowslowvideo
hide sophiablowtopfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show topicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen sophiablowfast()
screen sophiablowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNext")

label SophiaBlowFrontFast:
window hide
$ sophiablowslow = False
if sophiablowfast == False:
    $ sophiablowfast = True
    mc "I think your throat can take some FASTER skull-fucking now!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide topicon
show sophiablowtopfastvideo behind sophiablowtopslowvideo
show sophiablowtopfastvideo behind sophiablowfastvideo
$ renpy.pause(1.0, hard='True')
hide sophiablowtopslowvideo
hide sophiablowfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show nexticon:
    xpos 1750 ypos 1020    
call screen sophiablowtopfast()
screen sophiablowtopfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaBlowFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaBlowNext")

label SophiaBlowNext:
hide  nexticon
hide faster
hide slower
hide sceneicon
hide topicon    
cs01 "Let's give her mouth and pussy some respite..."
if age >= 20:
    mc "Let me first see how far she can take my fat pole..."
if age >= 18 and age <= 19:
    mc "Let me first see how far she can take my fat teen pole..."
scene sophiaoffice30 with dissolve
stop channel1
play sound "sounds/blow02.mp3"
mc "Damn, almost to the balls!"
window hide 
with hpunch
so "GGGGllll..."
scene sophiaoffice31 with dissolve
stop sound
play sound "v031/cough.mp3"
mc "Well done, you must have taken like, 15 inches or something. God only knows where they went."
cs01 "Now for the next part of your sentence. I authorize [hero] here to fuck you senseless on my desk!"
mc "Alright!"
scene sophiaoffice32 with dissolve
mc "Let's get this show on the road. Since Mrs Porker here is still recovering from barely being able to breathe for the last fifteen minutes, I'll take matters in my own hands."
so "Dear Lord, I'm in for a mighty POUNDING!"
scene sophiaoffice33 with dissolve
play sound "sounds/thud.mp3"
so "Oooh, you're so rough and MANLY, Mr Officer [hero]!"
scene sophiaoffice34 with dissolve
mc "I won't ask if you're ready, cos this is part of your SENTENCE!"
so "Still, please be caref..."

label SophiaDeskSlow:
window hide
$ sophiadeskfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskslowvideo behind sophiadeskpovslowvideo
show sophiadeskslowvideo behind sophiadeskfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sophiadeskpovslowvideo
hide sophiadeskfastvideo
if sophiadeskslow == False:
    $ sophiadeskslow = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <=19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophiadeskslow()
screen sophiadeskslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlow")

label SophiaDeskFrontSlow:
$ sophiadeskfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskpovslowvideo behind sophiadeskslowvideo
show sophiadeskpovslowvideo behind sophiadeskpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex03.mp3"
hide sophiadeskslowvideo
hide sophiadeskpovfastvideo
if sophiadeskslow == False:
    $ sophiadeskslow = True
    if age >= 20:
        so "I've never been fucked by such a YOUNG muscle stud before in my life! And I'm a schoolteacher."
    if age >= 18 and age <=19:
        so "I've never been fucked by such a YOUNG TEENAGE muscle stud before in my life! And I'm a schoolteacher."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophiadeskpovslow()
screen sophiadeskpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaDeskFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlow")

label SophiaDeskFast:
$ sophiadeskslow = False
if sophiadeskfast == False:
    $ sophiadeskfast = True
    mc "Damn, that pussy is just BEGGING to get fucked HARDER!"
    so "AAAH, YES! pound me like the cheap whore that I am, Mr [hero]!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskfastvideo behind sophiadeskslowvideo
show sophiadeskfastvideo behind sophiadeskpovfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sophiadeskslowvideo
hide sophiadeskpovfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophiadeskfast()
screen sophiadeskfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCum")

label SophiaDeskFrontFast:
window hide
$ sophiadeskslow = False
if sophiadeskfast == False:
    $ sophiadeskfast = True
    mc "Damn, that pussy is just BEGGING to get fucked HARDER!"
    so "AAAH, YES! pound me like the cheap whore that I am, Mr [hero]!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophiadeskpovfastvideo behind sophiadeskpovslowvideo
show sophiadeskpovfastvideo behind sophiadeskfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sophiadeskpovslowvideo
hide sophiadeskfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophiadeskpovfast()
screen sophiadeskpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFrontSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaDeskFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaDeskCum")

label SophiaDeskCum:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
cs01 "I think she's begging for your cum, [hero]. Fill her up, turn her slutty pussy into your cum dump!"
mc "Oh fuck, you girls are so nast..."
scene sophiadeskcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play sound "sounds/splooge02.mp3"
mc "...AAAAH!"
window hide
with hpunch
so "My hubby never comes this HARD, OOOOH!"
scene sophiadeskcum02 with dissolve
so "...On the rare occasion when he can get his pindick hard that is, AAAH!"
window hide
with fastflash
cs01 "Keep pumping that fat load deep inside her pussy and shut her up!"
scene sophiadeskcum03 with dissolve
play sound "sounds/moan05.mp3"
mc "Take that Mrs Porker, RHAAA!"
window hide
with hpunch
so "Sssooo much CUM, AAAH!"
scene sophiadeskcum04 with dissolve
play sound "sounds/moan04.ogg"
mc "I've got MORE for your hungry hole!"
window hide
with fastflash
cs01 "Keep going, I want you to empty yourself!"
scene sophiadeskcum03 with dissolve
play sound "sounds/moan05.mp3"
mc "AAAH, yes!"
scene sophiadeskcum04 with dissolve
mc "Here you go!"
scene sophiadeskcum03 with dissolve
so "I beg you, please stop!"
mc "And MORE, RHAAA!"
scene sophiadeskcum04 with dissolve
mc "And MORE, RHAAA!"
with hpunch
cs01 "You did good, she's overfilled with your [age]yo scum..."
scene sophiadeskcum05 with dissolve
stop channel1
play sound "sounds/splooge01.mp3"
so "You've turned my fuckhole inside out... I don't think I will ever be able to feel my hubby's tiny dick ever again. Or any of my pupils' for that matter."
mc "Now, as you may have noticed, I am still HARD, despite the monstrous load I just dumped inside Mrs Porker."
scene sophiadeskcum06 with dissolve
cs01 "So, you expect us to make you blow another giant load before you finally leave us in peace?"
mc "That would be the strict minimum in my books, yes."
scene sophiadeskcum07 with dissolve
if age >= 20:
    cs01 "Just because you're such a fucking STUD doesn't give you the right to just nut your sauce anywhere and anytime you want!"
if age >= 18 and age <= 19:
    cs01 "Just because you're such a fucking TEEN STUD doesn't give you the right to just nut your sauce anywhere and anytime you want!"
mc "It doesn't?"
so "We're gonna tease you so much, you'll be BEGGING for release, Mr Officer [hero]..."
mc "Try me!"
cs01 "Fine, go and sit down on the sofa and wait for us..."
scene sophiadeskcum08 with dissolve
cs01 "I'm gonna hold this monster tight while we slowly lick the whole shaft to a mighty explosion!"
play channel1 "sounds/lick01.ogg"

label SophiaLickSlow:
window hide
$ sophialickfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickslowvideo behind sophialicksceneslowvideo
show sophialickslowvideo behind sophialickfastvideo
$ renpy.pause(1.0, hard='True')
hide sophialicksceneslowvideo
hide sophialickfastvideo
if sophialickslow == False:
    $ sophialickslow = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sophialickslow()
screen sophialickslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlow")

label SophiaLickSceneSlow:
$ sophialickfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialicksceneslowvideo behind sophialickslowvideo
show sophialicksceneslowvideo behind sophialickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sophialickslowvideo
hide sophialickscenefastvideo
if sophialickslow == False:
    $ sophialickslow = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sophialicksceneslow()
screen sophialicksceneslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SophiaLickSceneFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlow")

label SophiaLickFast:
$ sophialickslow = False
if sophialickfast == False:
    $ sophialickfast = True
    mc "That's it, my little cock-hungry whores, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickfastvideo behind sophialickslowvideo
show sophialickfastvideo behind sophialickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sophialickslowvideo
hide sophialickscenefastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophialickfast()
screen sophialickfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCum")

label SophiaLickSceneFast:
window hide
$ sophialickslow = False
if sophialickfast == False:
    $ sophialickfast = True
    mc "That's it, my little cock-hungry whores, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sophialickscenefastvideo behind sophialicksceneslowvideo
show sophialickscenefastvideo behind sophialickfastvideo
$ renpy.pause(1.0, hard='True')
hide sophialicksceneslowvideo
hide sophialickfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sophialickpovfast()
screen sophialickpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickSceneSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SophiaLickFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SophiaLickCum")

label SophiaLickCum:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "Oh God, oh..."
scene sophialickcum01 with dissolve
play sound "sounds/boymoan03.mp3"
so "He's leaking pre-slime like a faucet!"
cs01 "That means he's about to bust his nut."
scene sophialickcum02 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
so "Let my tongue take him over the edge then..."
scene sophialickcum03 with dissolve
mc "AAAH!"
window hide
with hpunch
play sound "sounds/wow.mp3"
so "Oh my God, it's flying so high up!"
scene sophialickcum04 with dissolve
if age >= 20:
    cs01 "Look at that shot, more manly cum in that single shot than a hundred men combined!"
if age >= 18 and age <= 19:
    cs01 "Look at that shot, more manly teenage cum in that single shot than a hundred men combined!"
window hide
with fastflash
so "He had a LOT of cum left!"
scene sophialickcum05 with dissolve
mc "FFF..FFFFFUUUUCCCKK, RHAAA!"
window hide
with hpunch
cs01 "Keep pumping boy, let it RAIN down upon us!"
window hide
with fastflash
so "My face has been BUKKAKED! And so has yours, Captain Sawyer!"
scene sophialickcum06 with dissolve
stop channel1
play sound "sounds/lick03.mp3"
so "Mmmh, it's so thick and chunky."
cs01 "And there's so much of it..."
play sound "sounds/slurp.mp3"
so "* lick * I'm going to have to buy new outfits to fit my bigger tits... Hopefully, that will lead to some of my students feeling up some new fabric."
cs01 "I think it's time for you to get cleaned up and go back to your family, Mrs Porker."
cs01 "And for you to go back to your compound... Now that you have successfully completed this quest."
$ quest05end = True
window hide
play sound "sounds/winning.mp3"
show questicon05 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
mc "Alright, I'm done for anyway."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label IvyHaremSex:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy07.mp3"
scene ivyprefuckharem01 with dissolve
menu:
    "Do her doggy-style":
        jump IvyHaremDoggy
    "Get a titfuck":
        jump IvyHaremTitfuck

label IvyHaremDoggy:
mc "So get into the doggy position, I'm HARD and I don't have all day!"
pi "I'm kind of busy, I need to feed my pl..."
scene ivyprefuckharem02 with dissolve
mc "What part of \"you're in my harem and you will OBEY me\" did you not understand?"
pi "You're such a BRUTAL HAREM MASTER!"
scene ivyprefuckharem03 with dissolve
mc "First, I'll take these panties off, they won't be necessary..."
pi "Just hurry, I'm getting HORNY too! And I need to feed my plants."
scene ivyprefuckharem04 with dissolve
mc "Mmh, yeah, I can see that my little harem slave. You're VERY wet down there. You're really looking forward to getting teared apart by my humongous 18-incher, aren't you?"
if evilness >= 13:
    pi "I... You're just so EVIL!"
if evilness <= 12:
    pi "Y...YES, I know it will feel so GOOD!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "Sure, but you're a super-villainess so you like that, right?"
if evilness <= 12:
    mc "That's right, I'll do you HARD and GOOD!"
scene ivyprefuckharem04 with dissolve
if evilness >= 13:
    pi "No I don't! I like to be evil on my OWN!"
if evilness <= 12:
    pi "I'm so evil, I deserve it, I deserve to be put into my place by my GOOD harem Master!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "You sure? Your wet fuckhole says otherwise. Now take your boots off, I like to fuck \"au naturel\"."
if evilness <= 12:
    pi "That's right, and I can tell that your wet fuckhole is really looking forward to it! Now take your boots off, I like to fuck \"au naturel\"."
scene ivyprefuckharem06 with fastdissolve
if age >= 20:
    pi "Like this? I'm ready for your monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
if age >= 18 and age <= 19:
    pi "Like this? I'm ready for your teenage monster dong, Master! Drill my naughty super-villain hole with it, I beg you!"
mc "That's what I thought... You're horny for my massive weapon and you're going to get it. HARD and DEEP!"

play channel1 "sounds/womansex04.mp3"
label IvyHaremFuckSlow:
$ ivyharemfuckfast = False
window hide
show ivyharemfuckslowvideo behind ivyharemfuckfastvideo
show ivyharemfuckslowvideo behind ivyharemfuckpovslowvideo
pause 1.0
hide ivyharemfuckfastvideo
hide ivyharemfuckpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if ivyharemfuckfirst == False:
    $ ivyharemfuckfirst = True
    mc "I've enlarged your hole so much that first time I banged it, now my shaft just goes in real smoothly!"
    pi "I'm... opening up as wide as I can for you, Master!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen ivyharemfuckslow()
screen ivyharemfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckPOVSlow")

label IvyHaremFuckFast:
window hide
show ivyharemfuckfastvideo behind ivyharemfuckslowvideo
show ivyharemfuckfastvideo behind ivyharemfuckpovfastvideo
pause 1.0
hide ivyharemfuckpovfastvideo
hide ivyharemfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if ivyharemfuckfast == False:
    $ ivyharemfuckfast = True    
    mc "Now I'm really giving to you, cos you're my HAREM BITCH!"
    pi "Oh Master, you're so BRUTAL! But I LOVE IT!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen ivyharemfuckfast()
screen ivyharemfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckPOVFast")

label IvyHaremFuckPOVSlow:
$ ivyharemfuckfast = False
window hide
show ivyharemfuckpovslowvideo behind ivyharemfuckslowvideo
show ivyharemfuckpovslowvideo behind ivyharemfuckpovfastvideo
pause 1.0
hide ivyharemfuckpovfastvideo
hide ivyharemfuckslowvideo
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
call screen ivyharemfuckpovfuckslow()
screen ivyharemfuckpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckSlow")

label IvyHaremFuckPOVFast:
window hide
show ivyharemfuckpovfastvideo behind ivyharemfuckfastvideo
show ivyharemfuckpovfastvideo behind ivyharemfuckpovslowvideo
pause 1.0
hide ivyharemfuckfastvideo
hide ivyharemfuckpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if ivyharemfuckfast == False:
    $ ivyharemfuckfast = True    
    mc "Now I'm really giving to you, cos you're my HAREM BITCH!"
    pi "Oh Master, you're so BRUTAL! But I LOVE IT!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemfuckpovfuckfast()
screen ivyharemfuckpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremFuckFast")

label IvyHaremFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
mc "You did good, Poison Ivy, you're about to make my [age]yo ALPHA-DONG CUM BIG TIME?"
pi "* Puff * Well, get on with it then!"
scene ivyfuckharemcum01 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
play channel2 "sounds/splooge02.mp3"
mc "First, I will flood your insides with my ALPHA-SPUNK! RHAAA!"
window hide
with hpunch
play sound "sounds/moan05.mp3"
pi "Noooo! I can't get pregnant, I need to take care of my plants!"
scene ivyfuckharemcum02 with dissolve
mc "Too late, here comes my baby-making ball-batter, AAAHH!"
window hide
with fastflash
pi "Pull out, pull out you bastard!"
scene ivyfuckharemcum03 with dissolve
stop channel2
mc "Fine, but still gonna PLASTER your body in my cream though, FU-UUU-UCCCK!"
window hide
with hpunch
play sound "sounds/moan03.mp3"
pi "You filthy boy, I can feel your vile scum on me!"
scene ivyfuckharemcum04 with dissolve
mc "I'm your HAREM MASTER, so take these heavy shots to remind you, OOOOH!"
window hide
with vpunch
pi "Please stop spewing your vile load all over me, Master!"
scene ivyfuckharemcum05 with dissolve
mc "You're in luck, here's the last of it, phew!"
window hide
with fastflash
pi "My Master's cum is so... disgusting. But so enthralling at the same time."
scene ivyfuckharemcum06 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "You got that right. And I'll be back to give you MORE. And remind you that you belong to MY Harem now!"
pi "Y.. Yes Master..."
jump IvyHaremEnd

label IvyHaremTitfuck:
mc "I want a nice titfuck between your soft pillows until I blow my nut, you hear me?"
pi "I'm kind of busy, I need to feed my pl..."
scene ivyprefuckharem02 with dissolve
mc "What part of \"you're in my harem and you will OBEY me\" did you not understand?"
pi "You're such a BRUTAL HAREM MASTER!"
scene ivyprefuckharem03 with dissolve
mc "First, I'll take these panties off, they won't be necessary..."
pi "Just hurry, I'm getting HORNY too! And I need to feed my plants."
scene ivyprefuckharem04 with dissolve
mc "Mmh, yeah, I can see that my little harem slave. You're VERY wet down there. You're really looking forward to getting teared apart by my humongous 18-incher, aren't you?"
if evilness >= 13:
    pi "I... You're just so EVIL!"
if evilness <= 12:
    pi "Y...YES, I know it will feel so GOOD!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "Sure, but you're a super-villainess so you like that, right?"
if evilness <= 12:
    mc "That's right, I'll do you HARD and GOOD!"
scene ivyprefuckharem04 with dissolve
if evilness >= 13:
    pi "No I don't! I like to be evil on my OWN!"
if evilness <= 12:
    pi "I'm so evil, I deserve it, I deserve to be put into my place by my GOOD harem Master!"
scene ivyprefuckharem05 with fastdissolve
play sound "sounds/slap.mp3"
if evilness >= 13:
    mc "You sure? Your wet fuckhole says otherwise. Now take your boots off, I like to fuck \"au naturel\"."
if evilness <= 12:
    pi "That's right, and I can tell that your wet fuckhole is really looking forward to it! Now take your boots off, I like to fuck \"au naturel\"."
scene ivypretitfuckharem01 with fastdissolve
mc "Now that's better."
pi "Are you going to lick my pussy first, Master?"
mc "Na. This harem thing is about YOU servicing ME. Not the other way around. So lie on your back!"
scene ivypretitfuckharem02 with fastdissolve
if age >= 20:
    pi "I'm ready for your monster dong, Master! Pound your battering ram between my reasonably-sized pillows, I beg you!"
if age >= 18 and age <= 19:
    pi "I'm ready for your teenage monster dong, Master! Pound your battering ram between my reasonably-sized pillows, I beg you!"
mc "That's what I thought... You just can't wait to get my my massive weapon between your breasts. So get ready for my 18 inches of rock-hard love muscle!"

play channel2 "sounds/wetmassage.mp3"
label IvyHaremTitfuckSlow:
$ ivyharemtitfuckfast = False
window hide
show ivyharemtitfuckslowvideo behind ivyharemtitfuckfastvideo
show ivyharemtitfuckslowvideo behind ivyharemtitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyharemtitfuckfastvideo
hide ivyharemtitfuckfrontslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckslow == False:
    $ ivyharemtitfuckslow = True
    if age >= 20:
        pi "Do you like my tits Master? Do they wrap nicely around your giant ALPHA-DICK?"
    if age >= 18 and age <= 19:
        pi "Do you like my tits Master? Do they wrap nicely around your giant TEEN ALPHA-DICK?"
    mc "Even though your tits are not as MASSIVE than that first time, there's still plenty of boobflesh to rub against my hard pole!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen ivyharemtitfuckslow()
screen ivyharemtitfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckPOVSlow")

label IvyHaremTitfuckFast:
$ ivyharemtitfuckslow = False
window hide
show ivyharemtitfuckfastvideo behind ivyharemtitfuckslowvideo
show ivyharemtitfuckfastvideo behind ivyharemtitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyharemtitfuckfrontfastvideo
hide ivyharemtitfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckfast == False:
    $ ivyharemtitfuckfast = True    
    pi "Go on, pile-drive that throbbing horsecock between my breasts faster, I want to make you CUM, Master!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show front:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfast()
screen ivyharemtitfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckPOVFast")

label IvyHaremTitfuckPOVSlow:
$ ivyharemtitfuckfast = False
window hide
show ivyharemtitfuckfrontslowvideo behind ivyharemtitfuckslowvideo
show ivyharemtitfuckfrontslowvideo behind ivyharemtitfuckfrontfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan04.mp3"
hide ivyharemtitfuckfrontfastvideo
hide ivyharemtitfuckslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
with dissolve
if ivyharemtitfuckslow == False:
    $ ivyharemtitfuckslow = True
    if age >= 20:
        pi "Do you like my tits Master? Do they wrap nicely around your giant ALPHA-DICK?"
    if age >= 18 and age <= 19:
        pi "Do you like my tits Master? Do they wrap nicely around your giant TEEN ALPHA-DICK?"
    mc "Even though your tits are smaller than that first time, there's still plenty of boobflesh to rub against my hard pole!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfrontfuckslow()
screen ivyharemtitfuckfrontfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckSlow")

label IvyHaremTitfuckPOVFast:
$ ivyharemtitfuckslow = False
window hide
show ivyharemtitfuckfrontfastvideo behind ivyharemtitfuckfastvideo
show ivyharemtitfuckfrontfastvideo behind ivyharemtitfuckfrontslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/boymoan02.mp3"
hide ivyharemtitfuckfastvideo
hide ivyharemtitfuckfrontslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide front
if ivyharemtitfuckfast == False:
    $ ivyharemtitfuckfast = True    
    pi "Go on, pile-drive that throbbing horsecock between my breasts faster, I want to make you CUM, Master!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ivyharemtitfuckfrontfuckfast()
screen ivyharemtitfuckfrontfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IvyHaremTitfuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IvyHaremTitfuckFast")

label IvyHaremTitfuckEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide front
mc "Fuck yeah, I feel it coming..."    
pi "Spew that load already and be gone!"
scene ivytitfuckharemcum01 with dissolve
stop channel2
stop channel1
play sound "sounds/boymoan03.mp3"
mc "...anytime... RHAAA!"
window hide
with hpunch
play sound "sounds/boymoan05.mp3"
pi "You're EXPLODING like a cum firehose!"
scene ivytitfuckharemcum02 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "I've got a HUGE SUPPLY of young spunk for you, Poison Ivy, YEAH!"
window hide
with fastflash
pi "Just EMPTY your fat sack, do your worst!"
scene ivytitfuckharemcum03 with dissolve
mc "Oh yeah, you want some MORE? HERE'S SOME MOOOAAAARRRR!"
window hide
with hpunch
pi "Your filthy scum is flying EVERYWHERE!"
scene ivytitfuckharemcum04 with dissolve
mc "More importantly, it's covering your ample bosom, RHAAA!"
window hide
with fastflash
pi "Your huge cumstreaks are so... scalding hot!"
scene ivytitfuckharemcum05 with dissolve
stop channel1
play sound "sounds/panting.mp3"
pi "My Master's cum is so... disgusting. But so enthralling and tasty at the same time."
scene ivytitfuckharemcum06:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "It's NOT disgusting! And I'll be back to give you MORE. And remind you that you belong to MY Harem now!"
pi "Y.. Yes Master..."

label IvyHaremEnd:
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
