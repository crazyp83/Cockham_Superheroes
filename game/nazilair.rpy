label NaziCompound:
scene nazicompoundempty with fade
mc "I guess the nazi compound is empty. I was hoping Colonel Stroheim would have returned, but he didn't."
if inventorywhip == False:
    mc "Maybe I could look around and see if I find any interesting item to add to my inventory."
    scene naziwhip with dissolve
    mc "The Valkyrie's whip. Powergirl forgot to take it back to the compound. So now it's MINE!"
    window hide
    $ inventorywhip = True
    play sound "sounds/achievement.mp3"
    show acquiredwhip at poslocation
    $ renpy.pause(0.5, hard='True')
    pause
    mc "Time to go back to the compound..."    
jump Main

label StroheimWonder:
$ seenstroheimwonder = True
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene special01 with fade
play music "sounds/alarm.mp3"
mc "Uh oh, this is the \"Super-Hero in Super-Grave Danger\" alarm! I need to get to the hall pronto to find out what's happening!"
scene league09 with fade
play music "sounds/suspense.mp3"
cm "Are we all here?"
bw "No, Lara Crotch is away. And Batman hasn't shown up yet."
scene league03 with dissolve
pg "Neither has Wonder Woman! Did something bad happen to any of them?"
bw "I hope it's Batman."
scene league01 with dissolve
cm "Listen up, Wonder Woman was captured by Colonel Stroheim during the night. So let's hurry! Superman, carry me and Audit Girl, Powergirl, you take [hero] and the Black Widow!"
mc "Are you absolutely certain Powergirl can carry TWO people?"
scene league03 with dissolve
pg "You are such a coward! Wonder Woman is in super-grave danger and the only thing you worry about is whether you will fall to your death!"
mc "Well, I mean..."
scene league02 with dissolve
bw "Let's GO! We need to save Wonder Woman from the clutches of these nazis and I trust Powergirl!"

play music "sounds/coldwind.mp3"
show greysky:
    subpixel True
    xpos 0.0 ypos 0.0
    linear 10.0 xpos -0.3 ypos -0.2
show stroheimheroes01:
    subpixel True
    xpos -0.1 ypos 0.0
    linear 10.0 xpos 0.0 ypos 0.05
show stroheimheroes02:
    subpixel True
    xpos 0.05 ypos 0.05
    linear 10.0 xpos 0.0 ypos 0.0
with fade
mc "Oh Lord, please get us there safe..."
scene special02 with fade
cm "There's the neo-nazi compound."
window hide
play sound "sounds/skill.mp3"
show locationnazi at poslocation
$ renpy.pause(0.5, hard=True)
pause
$ locnazi = True
mc "Gee, that's discreet! Why wasn't I told about the location of this place earlier???"
cm "Colonel Stroheim has been keeping pretty quiet lately, so I didn't think this was a location you needed to know about. Let's sneak inside."
stop music
scene stroheim00 with fade
play channel1 "sounds/infiltrate.mp3"
cm "What do you see, [name]?"
mc "I see... some kind of portal and... Wonder Woman is BOUND and NAKED!"
scene stroheim01 with dissolve
na "Ha ha, you are tied up to my devious machine and you are at my MERCY now, Wonder Woman! My genius nazi plan is bound to work. BOUND, get it?"
ww "No, I don't get it, is that supposed to be funny?"
scene stroheim02 with dissolve
na "How dare you! German humor is das BEST humor in ze vorld!"
scene stroheim03 with dissolve
na "Engage ze DEVIOUS MACHINE! That vill teach her some manners!"
ig "Ja wohl, Herr Colonel!"
scene stroheim04 with dissolve
ww "Great girdle of Aphrodite! This... thing is IMMENSE!"
scene stroheim05 with dissolve
play music "sounds/womansex01.mp3"
na "HA HA, that's right, you'd better open up real WIDE, Wonder Woman!"
stop music
scene stroheim06 with dissolve
cm "They are raping her with a giant dildo!"
mc "Yeah sure, but let's wait a bit and see, she's not in any imminent danger after all..."
scene stroheim07 with dissolve
pg "You just want to watch the show, admit it!"
mc "No! Err, I'm just..."
scene stroheim08 with dissolve
sm "I cannot wait and let this pervert act be inflicted upon Wonder Woman! I'm going in!"
cm "Superman, wait!"
scene stroheim09 with dissolve
pg "Too late. The doofus went in."
na "HA! Superman, I vas expecting you! Fire... the KRYPTONITE bullets!"
play sound "sounds/gunfire.mp3"
scene stroheim10 with dissolve
sm "What? Hang on, this isn't fair! I didn't even have time to use my Super-Laser-Eyes!"
na "German bullets are the BEST bullets in ze vorld!"
scene stroheim11 with dissolve
sm "AAAH, I'm losing all my super-powers! HELP!"
cm "And now we've lost Superman... * sigh*"
scene stroheim12 with dissolve
mc "But we are all immune to kryptonite apart from him, right?"
pg "Err. I don't like it. It makes me lose my Super-Flight ability."
cm "And I lose at least one level in Super-Strength in the presence of this vile rock!"
mc "Gee, leave it to ME, the REAL superhero, hey?"
bw "And ME! Kryptonite doesn't affect the Black Widow at all!"
scene stroheim13 with dissolve
na "Is that all you can do, Cockham League of Injustice? HA HA! Begin phase ZWEI of my devious nazi plan!"
na "Impregnate her with our beloved Führer's superior Aryan seed that is cryogenically stored is ze machine's tank!"
scene stroheim14 with dissolve
ig "With ze fertility drug I injected her, she vill become pregnant with nazi babies with abzolut zertainty, Herr Colonel!"
scene stroheim15 with dissolve
fr "She is zo lucky to be receiving our Führer's mighty nazi cream!"
na "Ach, mein dear Frieda. I'll give you some neo-nazi ball-batter when this is over, LOTS of it, HA HA! *wink*"
scene stroheim16 with dissolve
fr "Oooh, Colonel Stroheim, that is zo naughty of you!"
scene stroheim17 with dissolve
na "And I will make sure to pound that superior Aryan ass of yours to TOTAL OBLIVION, mein big-titted valkyrie!"
fr "Mein Gott, Colonel, you are getting sehr HORNY! I can't wait to feel your bratwurst DEEP inside my muschi!"
scene stroheim18 with dissolve
mc "Now this is going too far! It's, like, almost NTR or something. I did nazi this coming."
pg "We MUST intervene before they knock her up with Hitler's frozen sperm!"
cm "There are quite a few of them, and the henchmen have Kryptonite machine guns... We need a STRATEGY."
scene stroheim19 with dissolve
ag "I could use my Super-Healing and revive Superman... While the rest of you... do the fighting."
pg "Great idea, Audit Girl! I'll square off with the SS-Valkyrie who thinks she's so hot..."
scene stroheim20 with dissolve
bw "I want to deal with that masked nazi nurse... I HATE her for some reason!"
cm "So I'll take on Colonel Stroheim. [name], you need to first neutralize one of the henchmen, that will be the signal."
scene stroheim12 with dissolve
menu: 
    "I'll use my Super-Agility and neutralize the closest henchman." if mcagility >= 1:
        jump StroheimAgility
    "I'll use my Super-Strength and make the henchman on the overlook fall.":
        jump StroheimStrength

label StroheimAgility:
scene stroheim21 with dissolve
hm01 "Was ist das? ALA..."
play sound "sounds/bonecrack.mp3"
scene stroheim22 with dissolve
mc "You won't be screaming with a broken neck, damn nazi henchman!"
$ usedagility += 1
scene stroheim23 with dissolve
mc "I killed him. That's right people, this is not the fucking A-team. Henchmen can actually die. But nobody ever cares about them so let's move on."
jump StroheimNext

label StroheimStrength:
scene stroheim40 with fade
mc "Now get ready for a SHAKEDOWN from my Super-Muscles, damn nazi henchman!"
play sound "sounds/metalscreech.mp3"
scene stroheim41 with dissolve
hm02 "Was ist das? ALARM! I vill fall to mein death!"
scene stroheim42
show wilhelmfalling at henchmandown01
with dissolve
play sound "sounds/wilhelmscream.mp3"
show wilhelmfalling at henchmandown02
$ renpy.pause(2.0, hard='True')
play sound "sounds/splat.ogg"
scene stroheim43 with dissolve
mc "He's dead. That's right people, this is not the fucking A-team. Henchmen can actually die. But nobody ever cares about them so let's move on."
$ usedstrength += 1

label StroheimNext:
scene stroheimnext01 with dissolve
stop channel1
play sound "sounds/powergirl.mp3"
mc "Captain MILF got rid of the other henchman. And now the Battle has begun. My Bulge must join the fray."
$ usedcombat += 1
menu:
    "Help Powergirl":
        mc "As I rush to join Powergirl, I will first watch how Captain MILF deals with this super-evil neo-nazi Colonel!"
        stop sound
        play channel1 "sounds/battlemusic.mp3"
        scene milfstroheim01 with dissolve
        cm "Take this, Colonel Stroheim!"
        scene milfstroheim02 with dissolve
        cm "This is... strangely Super-Heavy..."
        na "Can you feel the KRYPTONITE in the air, Captain MILF? HA HA HA!"
        scene milfstroheim03 with dissolve
        na "MISSED! You'll NEVER catch me, Captain MILF! And Wonder Woman is getting impregnated as we speak! HA HA!"
        mc "I must hurry and turn the tide with my mighty SUPERPOWERS!"
        jump StroheimPowergirl
    "Help the Black Widow":
        mc "As I rush to join the Black Widow, I will first watch how Captain MILF deals with this super-evil neo-nazi Colonel!"
        stop sound
        play channel1 "sounds/battlemusic.mp3"
        scene milfstroheim01 with dissolve
        cm "Take this, Colonel Stroheim!"
        scene milfstroheim02 with dissolve
        cm "This is...strangely super-heavy..."
        na "Can you feel the KRYPTONITE in the air, Captain MILF? HA HA HA!"
        scene milfstroheim03 with dissolve
        na "MISSED! You'll NEVER catch me, Captain MILF! And Wonder Woman is getting impregnated as we speak! HA HA!"
        mc "I must hurry and turn the tide with my mighty SUPERPOWERS!"
        jump StroheimBlackWidow

label StroheimPowergirl:
scene stroheimpowergirl01 with dissolve
fr "You vill feel the power of my nazi whip!"
mc "She hasn't seen me sneaking up behind her. This is gonna be a piece of cake!"
scene stroheimpowergirl02 with dissolve
pg "[name], what are you doing here?!"
mc "Oh shit, Powergirl didn't see me coming either!"
scene stroheimpowergirl03 with dissolve
play sound "sounds/punch.mp3"
pg "You IDIOT! You bumped into me!"
fr "Having some coordination troubles, SUPER-ZEROES?"
scene stroheimpowergirl04 with dissolve
mc "I'm back on my feet and ready to POUNCE again!"
pg "Let me deal with her!"
mc "* I must do something or Kara will get her lovely baby skin brutally whipped... *"
scene stroheimpowergirl05 with dissolve
play sound "sounds/punch.mp3"
fr "AAh, was ist das? I'm losing my grip on my zuper-whip!"
mc "There, I destabilized her just enough for Powergirl to strike the FINAL BLOW! Right between her giant nazi tiddies..."
scene stroheimpowergirl06 with dissolve
fr "ACH!"
pg "You cannot escape me, surrender, evil Frieda!"
mc "Now that I AM victorious, let's see how the others are doing..."
scene stroheimpowergirl07 with dissolve
mc "The Black Widow defeated the nazi nurse, and Audit Girl is tending to Superman. But Captain MILF still hasn't caught Colonel Stroheim... That's cos he's the end boss of this level, they're always tougher."
$ helpedpowergirl = True
jump StroheimAudit

label StroheimBlackWidow:
scene stroheimwidow01 with dissolve
mc "[hero] to the rescue, Black Widow! RHAAA!"
scene stroheimwidow02 with dissolve
bw "Not like that! What the hell are you doing, [name]?"
scene stroheimwidow03 with dissolve
play sound "sounds/punch.mp3"
bw "I told you so..."
scene stroheimwidow04 with dissolve
bw "Let the Black Widow deal with her!"
mc "I'm not down, my bulge is intact!"
scene stroheimwidow05 with dissolve
mc "If I don't intervene, this SS nurse will inject the Black Widow with a nazi poison!"
scene stroheimwidow06 with dissolve
play sound "sounds/punch.mp3"
mc "There, I grabbed her wrist!"
bw "While I taught her a lesson or two in SUPER-COMBAT!"
scene stroheimwidow07 with dissolve
ig "Please, I'm only a nurse! I vas just obeying orders!"
bw "You're not fooling me, vile super-villain SS Ingrid!"
mc "Let's see how the others are doing..."
scene stroheimwidow08 with dissolve
mc "Powergirl defeated the big-titted valkyrie, and Audit Girl is tending to Superman. But Captain MILF still hasn't caught Colonel Stroheim... That's cos he's the end boss of this level, they're always tougher."
$ helpedwidow = True
jump StroheimAudit

label StroheimAudit:
scene auditstroheim01 with dissolve
ag "Oh my God, he doesn't have a pulse!"
ag "Hang on, I forgot he's from Krypton, this is actually normal."
scene auditstroheim02 with dissolve
play sound "sounds/healing.mp3"
ag "By the Claws of Wolverine, let the healing begin!" 
scene auditstroheim03 with dissolve
stop sound
sm "Thank you, Audit Girl..."
ag "Yippee, I SAVED Superman!"
sm "But I still can't fight, I'm too weak..."
ag "The others are doing the fighting and we are winning! Soon, Wonder Woman will be freed!"
scene stroheimend01 with dissolve
stop channel1 fadeout 2.0
na "Too late! My genius plan has been set in motion and NOTHING CAN STOP IT! HA HA! And I'm escaping through my evil nazi space portal!"
play sound "sounds/evillaugh.mp3"
mc "Damn you Colonel Stroheim, what have you done to Wonder Woman?"
scene stroheimend02 with dissolve
na "When she returns to her time, proto-nazi babies will soon start ruling the world. Our Führer's 1000-year Reich vill have begun! HEIL HITLER!"
stop sound
scene stroheimend03 with dissolve
mc "Man, this is fucked up, even for a silly nazi."
scene stroheimend04 with dissolve
cm "Oh dear me, what are we going to do? Poor Princess Diana..."
mc "There might be a way out of this. I need to drown Hitler's seed with my own superior ALPHA-SPUNK!"
scene stroheimend05 with dissolve
cm "What??? This is just..."
bw "...about the only way to stop her from getting pregnant with nazi babies and tearing the timeline of our universe apart! Do it, [hero]!"
scene stroheimend03 with dissolve
ww "I'm just a sperm receptacle, like a good housewife... * sob *"
scene stroheimend06 with dissolve
mc "And SPERM you shall receive. LOTS OF IT!"
cm "I can't believe I'm letting my own tenant impregnate Wonder Woman..."
scene stroheimend07 with dissolve
pg "I don't think I want to see that. Let's clean up around here and find some clues while [name] does his dirty deed..."
scene stroheimend08 with dissolve
mc "Hey, I'm SAVING the timeline of the universe here!"
ww "Don't listen to her. I am ready... and submissively willing to receive your virile offering."
scene wonderstroheimprefuck01 with dissolve
play channel1 "sounds/sexy06.mp3"
mc "Now that's what I like to hear! My cum-missile will ravish your uterus until it swells with my baby-making load!"
cm "Please go slowly at first. She's a virgin, she never had a cock inside her, and yours is even bigger than the nazi dildo they used to rape her..."
scene wonderstroheimprefuck02 with dissolve
play sound "sounds/moan05.mp3"
if age >= 20:
    mc "That's just a few inches of my ALPHA-DONG... Get ready for MANY MORE of them!"
if age >= 18 and age <= 19:
    mc "That's just a few inches of my teenage ALPHA-DONG... Get ready for MANY MORE of them!"
ww "My virginity... * sob * The purity of my race... But I can't fight you, my womb is yours to dispose of as you wish!"
window hide
label WonderSlowFuck:
hide cum
hide faster
hide slower
hide harder
hide softer
show wonderstroheimfuckslowvideo behind wonderstroheimfuckfastvideo
show wonderstroheimfuckslowvideo behind wonderstroheimhardslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderstroheimfuckfastvideo
hide wonderstroheimhardslowvideo
with dissolve
stop channel2
play channel2 "sounds/womansex06.mp3"
$ wondertalkfast = False
pause
show faster:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen wonderpovslow()
screen wonderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderFastFuck")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderPoundSlow")

label WonderFastFuck:
hide cum
hide faster
hide slower
hide harder
hide softer
if wondertalkfast == False:
    ww "I have failed in my duty as a woman, my womb deserves a solid pounding!"
    $ wondertalkfast = True
show wonderstroheimfuckfastvideo behind wonderstroheimfuckslowvideo
show wonderstroheimfuckfastvideo behind wonderstroheimhardfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderstroheimfuckslowvideo
hide wonderstroheimhardfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex06.mp3"
pause
window hide
show slower:
     xpos 1700 ypos 500     
show harder:
     xpos 50 ypos 500     
call screen wonderpovfast()
screen wonderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderSlowFuck")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderPoundFast")

label WonderPoundSlow:
hide cum
hide faster
hide slower
hide harder
hide softer
if wonderpoundtalk == False:
    mc "Now who's going to be your daddy, hey?"
    ww "You're my daddy, [name]. FUCK ME HARDER DADDY!"
    $ wonderpoundtalk = True
show wonderstroheimhardslowvideo behind wonderstroheimfuckslowvideo
show wonderstroheimhardslowvideo behind wonderstroheimhardfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderstroheimfuckslowvideo
hide wonderstroheimhardfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex03.mp3"
$ wondertalkfast = False
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show softer:
     xpos 50 ypos 500     
call screen wonderpoundslow()
screen wonderpoundslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderPoundFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderImpregEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderSlowFuck")

label WonderPoundFast:
hide cum
hide faster
hide slower
hide harder
hide softer
if wondertalkfast == False:
    ww "I have failed in my duty as a woman, my womb deserves a solid pounding!"
    $ wondertalkfast = True
if wonderpoundtalk == False:
    mc "Now who's going to be your daddy, hey?"
    ww "You're my daddy, [name]. FUCK ME HARDER DADDY!"
    $ wonderpoundtalk = True
show wonderstroheimhardfastvideo behind wonderstroheimhardslowvideo
show wonderstroheimhardfastvideo behind wonderstroheimfuckfastvideo
$ renpy.pause(1.0, hard='True') 
hide wonderstroheimhardslowvideo
hide wonderstroheimfuckfastvideo
with dissolve
stop channel2
play channel2 "sounds/womansex03.mp3"
pause
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderpoundfast()
screen wonderpoundfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderPoundSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderImpregEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderFastFuck")

label WonderImpregEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
mc "That's it, I can feel my balls churning up a..."
stop channel2
scene wonderstroheimcum01 with dissolve
play channel2 "sounds/splooge02.mp3"
play sound "sounds/boymoan05.mp3"
mc "...MONSTERLOAD! AAAH!"
window hide
with fastflash
ww "AAH, I can feel my womb being WHITEWASHED with your seed!"
play sound "sounds/moan06.ogg"
scene wonderstroheimcum02 with hpunch
mc "Damn right, Adolf's spermies won't stand a chance, RHAAA!"
window hide
with fastflash
cm "I hope this works, give her all you've got, sweetie pie!"
scene wonderstroheimcum03 with dissolve
mc "I am, Captain MILF, I am! FILLING HER UP BIG TIME!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
ww "AAAH, my uterus is SWELLLING!"
scene wonderstroheimcum04 with dissolve
ww "Gggg... I'm just a walking womb... My sole duty as a woman is to carry babies... * sob *"
window hide
with fastflash
cm "Err, okay, I think that's enough [name], she's about to BURST!"
stop channel1
stop channel2
scene wonderstroheimcum05 with dissolve
play sound "sounds/moan03.mp3"
mc "That's it. I'm pretty sure I just saved the timeline of our universe."
cm "Hopefully, not TOO much or you'll end up creating an alternate world filled with horse-hung muscle shota boys..."
mc "Mmmh..."
scene stroheimend10 with dissolve
pg "I've tied up the Valkyrie and the SS nurse. And I found some classified top secret nazi documents in some totally unsecured boxes lying around."
fr "They belong to Colonel Stroheim! He took them home after the War!"
ig "This is a VITCH-HUNT!"
scene stroheimend11 with dissolve
mc "What about the... big-titted henchwomen? Do they need any nazi sperm to be drowned out perhaps?"
cm "No they don't! But we'll take them back to the compound for interrogation. We need to find out what is Colonel Stroheim's next move."
scene stroheimend12 with dissolve
mc "Interesting. I volunteer to interrogate them. I have mastered the technique using a big fat truncheon and..."
cm "Enough, [name]! You've had your share of pussy for the day, don't press your luck. I will interrogate the prisoners, I'm the LEAGUE CAPTAIN."
mc "Sorry, my landlady. I mean, Captain MILF."
show screen calendar
show screen statscreenicon
show screen questscreenicon
$ d10locday = renpy.random.randint(1,10)
$ d10locnight = renpy.random.randint(1,10)
$ d10locnightpoolmilf = renpy.random.randint(1,2)
$ d10locnightpgroom = renpy.random.randint(1,2)
jump Main

label InterrogationRoom:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/underworld.mp3"
scene interrogation01 with fade
mc "Well, well, well. If it isn't my two favorite nazi girls. Tied up like hogs."
scene interrogation02 with dissolve
ig "Vat do you want? I have nothing to say to YOU!"
mc "We'll see about that..."
ig "You can torture me as much as you like, I von't say a vord!"       
scene interrogation03 with dissolve
mc "Who said I was going to torture you? I just want to have a feel of those nice funbags of yours... And play with your uptight German pussy."
ig "You're just a PERVERT!"

call screen usepower("useseduction", "NaziNoSeduction", "NaziSeduction") with dissolve

label NaziNoSeduction:
scene interrogation04 with dissolve
play sound "sounds/lick01.ogg"
mc "* lick * Yeah, maybe. But I don't think you are as frigid as you make it out to be."
scene interrogation04b with dissolve
play sound "sounds/punch.mp3"
mc "Ouch! Damn, apparently you ARE as frigid as you look..."
scene interrogation05b with dissolve
mc "I need to press that godamn Super-Seduction button correctly next time or I'll never manage to move forward with this quest!"
jump Main

label NaziSeduction:
$ pressednazisseduction = True
$ usedseduction += 1
scene interrogation04 with dissolve
play sound "sounds/lick01.ogg"
mc "* lick * Yeah, maybe. But I don't think you are as frigid as you make it out to be."
ig "V... Vat are you doing?"
fr "Don't let zis disgusting American Schwein get to you! BE FRIGID, INGRID!"
scene interrogation05 with dissolve
play sound "sounds/moan02.mp3"
ig "N...Nein! I am zo sensitive down there...."
mc "I can see that, you're all wet..."
scene interrogation06 with dissolve
mc "Those big babies must be aching to release their warm milk..."
play sound "sounds/moan01.mp3"
ig "I must... resist!"
scene interrogation07 with dissolve
play sound "sounds/womancum02.mp3"
ig "AAAH! Das ist zo GUT!"
scene interrogation08 with dissolve
mc "Well, that was fast, I must be making you very HORNY..."
ig "NEIN! I vas... just... I needed..."
mc "Say no more and get some rest."
scene interrogation09 with dissolve
mc "Now it's your turn, Frieda. You must be horny too, your nipples are all hard..."
fr "No they're not! It's just...cold in here."
scene interrogation10 with dissolve
mc "Well, allow me to warm them up then. We wouldn't want our guests to catch a nipple cold."
fr "Filthy Schwein! Don't touch me, you are from an inferior race!"
scene interrogation11 with dissolve
mc "Don't say that, it's kind of offensive, and give me a kiss..."
fr "Never! My lips are reserved for Colonel Stroheim! He's a nice man from the SUPERIOR race!"
scene interrogation12 with dissolve
mc "Maybe I asked too nicely... You're going to change your tune, Frieda. Once you meet..."
scene interrogation13 with dissolve
mc "...My giant boyhood..."
fr "Wat is zis thing? It's..."
scene interrogation14 with dissolve
play sound "sounds/gasp.mp3"
mc "...HUGE, right?"
fr "Mein Gott! It's zo much bigger than Colonel Stroheim's bratwurst!"
scene interrogation15 with dissolve
mc "That's right. It's much more POWERFUL too. I'll show you..."
window hide
scene friedatits with fastdissolve
play channel2 [ "sounds/slap.mp3", "<silence .75>" ]
$ renpy.pause(2.0, hard='True')
fr "You are BRUISING mein chest... But it's a gut pain... I like it... I am supposed to be SADISTIC, wat is happening?..."
pause
if age >= 20:
    mc "You're just falling for my SUPER-COCK. It's a perfectly natural reaction."
if age >= 18 and age <= 19:
    mc "You're just falling for my TEEN SUPER-COCK. It's a perfectly natural reaction."
stop channel2
scene interrogation19 with dissolve
mc "Shut up, I'm not done proving my COCK SUPERIORITY to you..."
stop music
play music "sounds/sexy02.mp3"
scene interrogation20 with dissolve
play channel1 "sounds/moan02.mp3"
fr "Wat are you doing????"
mc "Just using my cock as a pussy crank. You'll see..."

label FriedaLiftSlow:
window hide
show friedaliftslowvideo behind friedaliftfastvideo
pause 1.0
hide friedaliftfastvideo
hide faster
hide slower
with dissolve
fr "I can't believe this is possible!"
mc "You'd better believe it..."
show faster:
     xpos 1700 ypos 500
call screen friedaliftslow()
screen friedaliftslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaLiftFast")

label FriedaLiftFast:
window hide
show friedaliftfastvideo behind friedaliftslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedaliftslowvideo
hide faster
hide slower
with dissolve
mc "See? My tireless [age]yo donkey-dick can do this all day..."
fr "Mein Gott, AAAH!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
call screen friedaliftfast()
screen friedaliftfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaLiftSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaLiftEnd")

label FriedaLiftEnd:
fr "Mein pussy is getting zo wet..."
scene interrogation21 with dissolve
stop channel1
play sound "sounds/mangrunt01.mp3"
mc "Houston, we have LIFT OFF!"
play sound "sounds/moan04.ogg"
fr "AAAH, you're such a young STALLION!"
scene interrogation22 with dissolve
mc "That's right, so you'd better show your appreciation for this SUPER-COCK!"
scene interrogation21 with dissolve
fr "But you're not Aryan, I can't let y..."
scene interrogation22 with dissolve
mc "What did you say? This SUPERIOR COCK isn't good enough for you?"
fr "Nein, nein! It's gut, I..."
scene interrogation23 with dissolve
play sound "sounds/womancum02.mp3"
mc "No more superior cock for you! Until you tell me EVERYTHING!"
scene interrogation24 with dissolve
fr "Untie me and I will talk. If you prove to me you are from the Superior race..."
mc "Alright, let's see now..."
scene interrogation25 with dissolve
mc "What is Colonel Stroheim up to? Where did he go?"
ig "Don't talk! We vowed allegiance to our Führer! Heil Hitler!"
scene interrogation26 with dissolve
fr "But maybe he's an Aryan, Ingrid. One of ours. If he shows us his Race Papieren..."
mc "I don't have any \"papers\". But I am from the Superior Race. The race of SUPER-HEROES! And I'll PROVE it to you on your little friend!"
scene interrogation27 with dissolve
mc "Your turn to feel the POWER of my mighty pillar!"
ig "W...Wat?"
scene interrogation28 with dissolve
mc "Can you feel the HEAT radiating from its massive girth yet?"
ig "I... Yes, I suppose it is sehr HOT!"
scene interrogation29 with dissolve
mc "Let me place it between your thighs..."
mc "And..."
play channel1 "sounds/moan02.mp3"
play channel2 "sounds/wetmassage.mp3"

label IngridLiftSlow:
window hide
show ingridliftslowvideo behind ingridliftfastvideo
pause 1.0
hide ingridliftfastvideo
hide faster
hide slower
with dissolve
mc "Does it feel like a SUPERIOR COCK to you yet?"
ig "I... Nein, I must resist!" 
show faster:
     xpos 1700 ypos 500
call screen ingridliftslow()
screen ingridliftslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridLiftFast")

label IngridLiftFast:
window hide
show ingridliftfastvideo behind ingridliftslowvideo
pause 1.0
hide ingridliftslowvideo
hide faster
hide slower
with dissolve
mc "How about if I lift your whole body up even faster? Can you feel its sheer SUPER-POWER now?"
ig "AAAH! You are a sehr big POWERFUL boy, JA!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
call screen ingridliftfast()
screen ingridliftfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridLiftSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridLiftEnd")

label IngridLiftEnd:
hide nexticon
hide faster
hide slower
mc "Let me emphasize how STRONG it is right now..."
scene interrogation30 with dissolve
stop channel1
stop channel2
play sound "v032/womancum04.mp3"
mc "There! Did you feel that?"
ig "JA, JA, I DID!"
scene interrogation31 with dissolve
fr "He is zo STRONG! Stronger than the Aryan boys I met back in Bavaria vhen I was a horny teenager!"
ig "I know, zis is so embarassing for our superior race..."
scene interrogation32 with dissolve
mc "Next round. My cock versus your Nazi ass!"
ig "NEIN! You are crazy, it vill never fit!"
scene interrogation33 with dissolve
play sound "sounds/moan05.mp3"
mc "I don't see any fitting issues so far..."
ig "AAAH! It feels like I am being IMPALED on your Lieb-Sword!"
play channel1 "sounds/moan03.mp3"

label IngridAnalFuckSlow:
$ ingridanalfuckfast = False
window hide
show ingridanalslowvideo behind ingridanalfastvideo
show ingridanalslowvideo behind ingridanalcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ingridanalfastvideo
hide ingridanalcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckslow == False:
    $ ingridanalfuckslow = True
    ig "Your ding-dong... It is zo fucking BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ingridanalfuckslow()
screen ingridanalfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckPOVSlow")

label IngridAnalFuckFast:
$ ingridanalfuckslow = False
window hide
show ingridanalfastvideo behind ingridanalslowvideo
show ingridanalfastvideo behind ingridanalcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ingridanalcloserfastvideo
hide ingridanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckfast == False:
    $ ingridanalfuckfast = True    
    if age >= 20:
        ig "Mein Gott! Zat giant horsedick is stretching mein ass wider than the Siegfried line!"
    if age >= 18 and age <= 19:
        ig "Mein Gott! Zat giant teen horsedick is stretching mein ass wider than the Siegfried line!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ingridanalfuckfast()
screen ingridanalfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckPOVFast")

label IngridAnalFuckPOVSlow:
$ ingridanalfuckfast = False
window hide
show ingridanalcloserslowvideo behind ingridanalslowvideo
show ingridanalcloserslowvideo behind ingridanalcloserfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide ingridanalcloserfastvideo
hide ingridanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ingridanalfuckslow == False:
    $ ingridanalfuckslow = True
    ig "Your ding-dong... It is zo fucking BIG!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ingridanalcloserfuckslow()
screen ingridanalcloserfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckSlow")

label IngridAnalFuckPOVFast:
$ ingridanalfuckslow = False
window hide
show ingridanalcloserfastvideo behind ingridanalfastvideo
show ingridanalcloserfastvideo behind ingridanalcloserslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide ingridanalfastvideo
hide ingridanalcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
if ingridanalfuckfast == False:
    $ ingridanalfuckfast = True    
    if age >= 20:
        ig "Mein Gott! Zat giant horsedick is stretching mein ass wider than the Siegfried line!"
    if age >= 18 and age <= 19:
        ig "Mein Gott! Zat giant teen horsedick is stretching mein ass wider than the Siegfried line!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ingridanalcloserfuckfast()
screen ingridanalcloserfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("IngridAnalFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("IngridAnalFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("IngridAnalFuckFast")

label IngridAnalFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
mc "It's time for me to fill up that dirty hole with my SUPERIOR SPUNK!"
fr "If he totally fills you up, then he IS from the Superior Race!"
scene ingridanalcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "v031/boyorgasm02.mp3"
mc "That's it, take THAT, you nazi-whore!"
window hide
with hpunch
ig "AAAH! He's so BRUTAL!"
scene ingridanalcum02 with dissolve
mc "I thought you girls like BRUTAL stuff! You want some more, here's some MOAAAAR!"
window hide
with fastflash
mc "DEEPER INSIDE YOUR BACKDOOR, RHAA!"
scene ingridanalcum03 with dissolve
mc "I'll give you a CUM ENEMA, AAAH!"
window hide
with vpunch
play sound "sounds/womancum02.mp3"
ig "Zo much nutzauce! I'm cumming too!"
scene ingridanalcum04 with dissolve
stop channel1
play sound "sounds/splat.ogg"
mc "Now for the GRAND CUM FINALE!!!!"
window hide
with fastflash
fr "You're LEAKING spunk from dein ass, Ingrid! He IS from the Superior Race!"
scene ingridanalcum05 with dissolve
stop channel2
play sound "sounds/boymoan03.mp3"
mc "There. I totally covered you in my HOT SEED."
play sound "sounds/moan02.mp3"
ig "Uuuhhh, I feel zo dirty... And zo GUT!"
scene ingridanalcum06 with dissolve
fr "I hope you kept some cream for MICH!"
mc "Ooh yeah, a SEX SUPERHERO like me ain't done with just one little load. Come over here and I'll show you..."
scene interrogation40 with dissolve
play sound "sounds/lick01.ogg"
ig "Zo tasty..."
mc "Come closer, Frieda. I want to..."
scene interrogation41 with dissolve
play sound "sounds/kiss.mp3"
mc "...kiss YOU!"
fr "Mmmh... Zuch a good kisser...."
mc "Now get down on your knees...."
scene interrogation42 with dissolve
if age >= 20:
    mc "...And worship my MASSIVE HORSECOCK!"
if age >= 18 and age <= 19:
    mc "...And worship my MASSIVE TEEN HORSECOCK!"
play sound "sounds/kiss.mp3"
fr "I vill, I vill! * kisses *"
mc "And you, Ingrid, clean the tip from my overflowing cum-cannon!"
ig "Ja wohl!"
scene interrogation43 with dissolve
play sound "sounds/slurp.mp3"
mc "That's good, my little nazi cock-sluts. Yeah, sehr good."
scene interrogation44 with dissolve
play sound "sounds/lick02.mp3"
mc "Keep going, suck that dong... Make me COME AGAIN!"

stop channel1
play channel1 "v032/blow03.mp3"

label SSBlowjobSlow:
$ ssblowjobfast = False
window hide
show ssblowjobslowvideo behind ssblowjobfastvideo
show ssblowjobslowvideo behind ssblowjobcloserslowvideo
pause 1.0
hide ssblowjobfastvideo
hide ssblowjobcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobslow == False:
    $ ssblowjobslow = True
    mc "My shaft just LOVES the attention you're giving it, my little nazi cock-whores..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ssblowjobfuckslow()
screen ssblowjobfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobCloserSlow")

label SSBlowjobFast:
$ ssblowjobslow = False
window hide
show ssblowjobfastvideo behind ssblowjobslowvideo
show ssblowjobfastvideo behind ssblowjobcloserfastvideo
pause 1.0
hide ssblowjobcloserfastvideo
hide ssblowjobslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobfast == False:
    $ ssblowjobfast = True
    play sound "sounds/boymoan02.mp3"
    mc "Oh yeah, it's even better like that... Mmmh..."    
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show closer:
     xpos 50 ypos 500    
call screen ssblowjobfuckfast()
screen ssblowjobfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobCloserFast")

label SSBlowjobCloserSlow:
$ ssblowjobfast = False
window hide
show ssblowjobcloserslowvideo behind ssblowjobslowvideo
show ssblowjobcloserslowvideo behind ssblowjobcloserfastvideo
pause 1.0
hide ssblowjobcloserfastvideo
hide ssblowjobslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
with dissolve
if ssblowjobslow == False:
    $ ssblowjobslow = True
    mc "My shaft just LOVES the attention you're giving it, my little nazi cock-whores..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ssblowjobcloserfuckslow()
screen ssblowjobcloserfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobCloserFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobSlow")

label SSBlowjobCloserFast:
$ ssblowjobslow = False
window hide
show ssblowjobcloserfastvideo behind ssblowjobfastvideo
show ssblowjobcloserfastvideo behind ssblowjobcloserslowvideo
pause 1.0
hide ssblowjobfastvideo
hide ssblowjobcloserslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide closer
if ssblowjobfast == False:
    $ ssblowjobfast = True
    play sound "sounds/boymoan02.mp3"
    mc "Oh yeah, it's even better like that... Mmmh..."    
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen ssblowjobcloserfuckfast()
screen ssblowjobcloserfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SSBlowjobCloserSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("SSBlowjobEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SSBlowjobFast")

label SSBlowjobEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide closer
mc "You want me to come? You want another GIANT LOAD of BOYCREAM?"
fr "Ja, JA! Bitte, give us your young cum!"
scene ssblowjobcum01 with dissolve
stop sound
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "HERE YOU GO, MY LITTLE NAZI CUM-WHORES, AAAH!"
window hide
with fastflash
play sound "sounds/splooge01.mp3"
ig "Mmmggg...."
scene ssblowjobcum02 with dissolve
play sound "sounds/slurp.mp3"
mc "MAJOR CUM RELEASE AHEAD!"
window hide
with hpunch
mc "Fuck yeah! Suck that hot spunk!"
scene ssblowjobcum03 with dissolve
play sound "sounds/lick01.ogg"
fr "You're... * slurp * cumming zzzooo much!"
window hide
with fastflash
mc "Damn right I am, RHAAA!"
scene ssblowjobcum04 with dissolve
play sound "sounds/splat.ogg"
ig "* gargle * He is filling... Mein mouth!"
window hide
with fastflash
if age >= 20:
    mc "...with a MASSIVE dose of my unending supply of jizz!"
if age >= 18 and age <= 19:
    mc "...with a MASSIVE dose of my unending supply of teenage jizz!"
scene ssblowjobcum05 with dissolve
stop channel1
play sound "v031/cough.mp3"
ig "I can't... swallow all zis cream... schnell enough...."
play sound "sounds/lick03.mp3"
fr "Let me lick your mighty cum-cannon clean..."
mc "Yeah, go ahead. Then clean your little friend's face and chest, I made a big cum mess over there..."
scene ssblowjobcum06 with dissolve
play sound "sounds/lick02.mp3"
ig "Oooh, Frieda..."
mc "Yeah, that's hot, keep going..."
scene ssblowjobcum07 with dissolve
play sound "sounds/lick01.ogg"
fr "I just love the taste of that young spunk.... It smells zo VIRILE!"
ig "I know... But... We must not tell him anything..."
scene ssblowjobcum08 with dissolve
mc "I see, you girls need some more CUM PERSUASION! Well, I'm STILL HARD so you'll get what you want!"
ig "Was? How can he still have a hardon after theze zwei MASSIVE RELEASES???"
scene ssblowjobcum09 with dissolve
play sound "sounds/gasp.mp3"
mc "And it's YOUR turn to feel the POWER of my mighty ROD OF PLEASURE, Frieda!"
ig "I...can't fight him anymore. Zorry, Frieda..."
scene ssblowjobcum10 with dissolve
mc "I'm gonna fucking tear your womb apart if you don't talk soon..."
fr "I... Go on, FUCK MICH! I DON'T CARE!"
scene ssblowjobcum11 with dissolve
play sound "sounds/womancum02.mp3"
mc "Cumming already? But that's just the tip..."
ig "There's way over ein foot of MEGACOCK still outzide Frieda!"
mc "That's right, so get ready for a HEAVY POUNDING!"    

label FriedaFuckSlow:
$ friedafuckharder = False
$ friedafuckfast = False
if friedafuckslow == False:
    $ friedafuckslow = True
    ig "Just take it like I did! For the glory of our Führer!"
window hide
show friedafuckslowvideo behind friedafuckfastvideo
show friedafuckslowvideo behind friedafuckpovslowvideo
show friedafuckslowvideo behind friedafuckharderslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide friedafuckfastvideo
hide friedafuckpovslowvideo
hide friedafuckharderslowvideo
hide cum
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
call screen friedafuckslow()
screen friedafuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVSlow")

label FriedaFuckFast:
$ friedafuckharder = False
$ friedafuckslow = False
if friedafuckfast == False:
    $ friedafuckfast = True
    fr "Is that all you have? You'll never get what you what with suck WEAK pounding!"
    mc "Oh, you're taunting me now? I'm gonna fuck you FASTER then!"
window hide
show friedafuckfastvideo behind friedafuckslowvideo
show friedafuckfastvideo behind friedafuckpovfastvideo
show friedafuckfastvideo behind friedafuckharderfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedafuckslowvideo
hide friedafuckpovfastvideo
hide friedafuckharderfastvideo
hide cum
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
call screen friedafuckfast()
screen friedafuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVFast")

label FriedaFuckPOVSlow:
$ friedafuckharder = False
$ friedafuckfast = False
if friedafuckslow == False:
    $ friedafuckslow = True
    ig "Just take it like I did! For the glory of our Führer!"
window hide
show friedafuckpovslowvideo behind friedafuckslowvideo
show friedafuckpovslowvideo behind friedafuckpovfastvideo
show friedafuckpovslowvideo behind friedafuckharderpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide friedafuckslowvideo
hide friedafuckpovfastvideo
hide friedafuckharderpovslowvideo
hide cum
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
call screen friedafuckpovslow()
screen friedafuckpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckSlow")

label FriedaFuckPOVFast:
$ friedafuckharder = False
$ friedafuckharder = False
$ friedafuckslow = False
if friedafuckfast == False:
    $ friedafuckfast = True
    fr "Is that all you have? You'll never get what you what with suck WEAK pounding!"
    mc "Oh, you're taunting me now? I'm gonna fuck you FASTER then!"
window hide
show friedafuckpovfastvideo behind friedafuckpovslowvideo
show friedafuckpovfastvideo behind friedafuckfastvideo
show friedafuckpovfastvideo behind friedafuckharderpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide friedafuckpovslowvideo
hide friedafuckfastvideo
hide friedafuckharderpovfastvideo
hide cum
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
call screen friedafuckpovfast()
screen friedafuckpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckFast")

label FriedaFuckHarderSlow:
if friedafuckharder == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharder = True        
window hide
show friedafuckharderslowvideo behind friedafuckharderfastvideo
show friedafuckharderslowvideo behind friedafuckharderpovslowvideo
show friedafuckharderslowvideo behind friedafuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide friedafuckharderfastvideo
hide friedafuckharderpovslowvideo
hide friedafuckslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen friedafuckharderslow()
screen friedafuckharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEnd")

label FriedaFuckHarderFast:
if friedafuckharder == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharder = True        
window hide
show friedafuckharderfastvideo behind friedafuckharderslowvideo
show friedafuckharderfastvideo behind friedafuckharderpovfastvideo
show friedafuckharderfastvideo behind friedafuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/pounding.ogg"
hide friedafuckharderslowvideo
hide friedafuckharderpovfastvideo
hide friedafuckfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen friedafuckharderfast()
screen friedafuckharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEnd")

label FriedaFuckHarderPOVSlow:
if friedafuckharder == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharder = True        
window hide
show friedafuckharderpovslowvideo behind friedafuckharderslowvideo
show friedafuckharderpovslowvideo behind friedafuckharderpovfastvideo
show friedafuckharderpovslowvideo behind friedafuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide friedafuckharderslowvideo
hide friedafuckharderpovfastvideo
hide friedafuckpovslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen friedafuckharderpovslow()
screen friedafuckharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEnd")

label FriedaFuckHarderPOVFast:
if friedafuckharder == False:
    fr "You can't do better than that? You're definitely from an INFERIOR race then!"
    mc "That's it, I've had enough! I'm gonna POUND YOU HARDER UNTIL YOU SUBMIT!"
    $ friedafuckharder = True        
window hide
show friedafuckharderpovfastvideo behind friedafuckharderpovslowvideo
show friedafuckharderpovfastvideo behind friedafuckharderfastvideo
show friedafuckharderpovfastvideo behind friedafuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/pounding.ogg"
hide friedafuckharderpovslowvideo
hide friedafuckharderfastvideo
hide friedafuckpovfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen friedafuckharderpovfast()
screen friedafuckharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FriedaFuckHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("FriedaFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FriedaFuckHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FriedaFuckEnd")

label FriedaFuckEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon    
mc "Are you ready to spill the beans? Cos I'm ready to spill MY SEED!"
ig "Hold tight, Frieda!"
scene friedafuckcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/boymoan05.mp3"
fr "Nein! He's cumming..."    
window hide
with fastflash
play sound "sounds/moan05.mp3"
mc "That's right, and that's just the START!"
scene friedafuckcum02 with dissolve
mc "RHAAA! I won't stop until you're BLOATED with my spunk!"
window hide
with hpunch
mc "Talk, or I'll WRECK your womb with a mighty CUMPLOSION!"
scene friedafuckcum03 with dissolve
play sound "sounds/moan04.ogg"
fr "AAAh! I vill talk, I vill talk! Colonel Stroheim vent back in time. To... Berlin, 1945. AAAH!"
window hide
with hpunch
ig "The day after our Führer had a tragic gun-related inzident. Leave her alone now!"
scene friedafuckcum04 with dissolve
play sound "sounds/boymoan03.mp3"
mc "Tell me MORE! Or the next shot will DESTROY your womb! I want to know EVERYTHING!"
window hide
with fastflash
play sound "sounds/moan05.mp3"
fr "UUUH! He is gathering his burnt remains to clone him back to LIFE!"
mc "Then, there is no past time to waste! I must STOP him before it was too late! Tell me how to get there!"
window hide
with hpunch
play sound "sounds/moan06.ogg"
ig "I can take you there, I know how to program ze portal command module! Let her go!"
scene friedafuckcum05 with dissolve
stop channel1
play sound "sounds/moan02.mp3"
play sound "sounds/splooge01.mp3"
mc "Alright, for THIS time, I will spare your womb... And I'll fetch Wonder Woman while you girls clean yourselves up. Of all the Super-heroes, she's the one who deserves to put an END to this neo-nazi madness!"
play sound "sounds/moan02.mp3"
fr "Vat have ve done? Ve have betrayed Colonel Stroheim!"
ig "And our future cloned Führer..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
stop music

label PreBerlin:
$ period += 1
play channel1 "sounds/suspense.mp3"
scene preberlin01 with fade
ww "Show us how to get to Colonel Stroheim or you will feel the wrath of Wonder Woman!"
ig "The command module is over zhere."
scene preberlin02 with dissolve
ig "I vill program it for Berlin, May the 1st, 1945."
mc "You'd better not trick us. I'm watching you."
scene preberlin03 with dissolve
ww "I don't trust them. Send them ahead into the portal. If it's a trick, they'll try and escape and not go through it."
mc "You have wonderful ideas, Princess Diana of...err..." 
ww "THEMYSCIRA!"
scene preberlin04 with dissolve
mc "You go first, Valkyrie Frieda. Then the SS nurse. Quietly, I'm watching you. There is no escape."
ww "What is this jar you're carrying?"
scene preberlin05 with dissolve
mc "It contains Hitler's intact testicle which I somehow acquired. Something tells me it might be very valuable on this dangero..."
scene preberlin06 with dissolve
play sound "sounds/whoosh.mp3"
ig "I'll take that with me on my vay, danke schön, dumbass!"
mc "Hey! Damn it! You can't even trust Nazis not to be dishonest thieves!"
scene preberlin07 with dissolve
ww "Even by my standards, you are so naive, young hero. Let's follow them, we need to catch them before they hand over this artefact to Colonel Stroheim!"
mc "Alright, I'm ready to KICK SOME NAZI BUTTS!"

label BerlinStart:
play channel1 "v051/bombers.mp3"
scene war01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with fade
mc "What the? This is REALLY Berlin, 1945!!!"
ww "Be careful, I Super-Sense a lot of Evil around here..."
scene war02 with dissolve
play sound "sounds/slap.mp3"
ww "Watch out! It's that SS nurse throwing poisonous darts at us! But my shield protected me from her sneaky attack!"
mc "Err... It didn't protect ME I'm afraid..."
scene war03 with dissolve
play sound "sounds/panting.mp3"
mc "I don't feel good. Not good at all..."
ww "[hero]! Try and FIGHT the poison! I'm going to chase after these pesky nazis!"
if mcresistance == 0:
    scene war05 with dissolve
    mc "Feeling worse and worse..."
    jump BerlinNoResistance

scene war04 with dissolve
play sound "sounds/effort01.mp3"
mc "I'll use my Super-Resistance to FIGHT FOR MY LIFE!"
call screen usepower("useresistance", "BerlinNoResistance", "BerlinResistance") with dissolve

label BerlinNoResistance:
scene war05 with dissolve
"The nazi poison slowly seeps into your blood stream and..."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return    

label BerlinResistance:
if mcresistance == 0 or usedresistance == 0:
    scene war05 with dissolve
    mc "Feeling worse and worse... My Super-Resistance is just not HIGH enough. I should have trained with Captain MILF in the pool... Or picked it as a Super-Power when leveling up..."
    window hide
    show gameovericon:
        xpos 600 ypos 400
    pause
    return        

if mcresistance >= 1 and usedresistance >= 1:
    $ usedresistance += 1
    play channel2 "sounds/wwomanmusic01.mp3"
    scene war06 with dissolve
    fr "Fire at VILL! EXTERMINATE THEM!"
    play sound "sounds/gunfire.mp3"
    mc "I'm... starting to feel better. But I can't help Wonder Woman just yet... I hope she manages it on her own for now."
    scene war07 with dissolve
    play sound "sounds/knifecut.mp3"
    mc "Clearly, she can handle these nazi thugs all by herself. She's Wonder Woman after all!"
    scene war08 with dissolve
    play sound "sounds/gunfire.mp3"
    mc "I wouldn't like to be that nazi henchman. Things are looking bleak for him right now..."
    scene war09 with dissolve
    hm02 "ALARM! She's too fast for mich!"
    play sound "sounds/wilhelmscream.mp3"
    mc "You can scream all you like buddy, you're done for! Wonder Woman for the kill again!"
    
scene war10 with dissolve
stop channel2
ww "Are you feeling better now?"
mc "Yes, thank you. Boy, this place is crawling with nazis. CRAWLING, get it?"
ww "No, I don't get it. Was that supposed to be funny?"
mc "A bit."
ww "Stop wasting time, and let's follow those SS Valkyries who took the jar that you weren't supposed to bring here in the first place!"
scene war11 with dissolve
mc "I see a nazi soldier over there!"
ww "I saw him too. I have Super-Vision."
scene war12 with dissolve
play sound "sounds/whoosh.mp3"
mc "What are you doing, throwing your shield at him!"
scene war13 with dissolve
play sound "sounds/knifecut.mp3"
mc "Ah, I see, you actually AIMED your shield at him. My bad."
scene war14 with dissolve
play sound "sounds/panting.mp3"
mc "The Nazi regime is on its last legs. LAST LEG, g..."
ww "Oh, shut up! I'm not in the mood for your silly puns!"
mc "Ah, but you admit it was a joke and that you got it at least."
ww "Let me pick up my shield and let's continue. I saw them entering that building over there."

label BerlinEnd:
play channel1 "sounds/underworld.mp3"
scene berlin01 with fade
mc "Colonel Stroheim! There he is! Let's END this!"
scene berlin02 with dissolve
play sound "v031/radiation01.mp3"
na "Too late! With the intact BALL of our Führer that you so kindly gave me, my resurrection experiment is ON A ROLL, HA HA! ON A ROLL, get it?"
ww "Is he saying that because a ball rolls? That's quite clever."
play sound "sounds/buzz.mp3"
na "Until I got my hands on that testicle, all my cloning attempts had failed. But not this time, thanks to you, HA HA HA!"
mc "You dastardly Super-Villain! And nazi to boot."
show pg13:
    xpos 100 ypos 600
with fastdissolve
    
menu:
    "Watch the program. I'm ready for a laugh.":
        pass
    "Jump to the end. I don't want to see Adolf's pee-pee.":
        stop channel1 fadeout 1.0
        jump BerlinEnd02

scene berlin03 with dissolve
play sound "sounds/splat.ogg"
na "Behold, our Führer is coming back to life! To lead us into his 1000-year Reich again! Heil Hitler!"
ah "Vat the fuck? Vy am I naked? And who are you people? "
scene berlin04 with dissolve
na "Mein Führer, I am Colonel Str..."
scene berlin05 with dissolve
ah "Hang on, am I seeing this right? I have two balls??? You count two balls, right? Tell me you count two balls!"
na "Korrect, Mein Führer, I have found your...err... zecond ball and you are now ready to lead your Reich again and rid the world of the Jewish filth!"
scene berlin06 with dissolve
ah "I don't give a sheisse about the var anymore, you idioten! I have TWO BALLS now, you hear me? \n ZWEI FUCKING BEAUTIFUL BALLS!"
na "But... Mein Führer... The Jews... You still hate them, right?"
scene berlin07 with dissolve
ah "Ach, nein! I vas only angry because I thought the rabbi had cut my ball off by mistake during my circumcision when I vas a kid, but clearly, I vas wrong!"
scene berlin08 with dissolve
ah "Now, I can proudly tell the Vorld that I AM JEWISH! A Jew with two big, fat balls! SHALOM!"
mc "Well, that's a twist I didn't expect."
scene berlin09 with dissolve
ah "Mein ball. Mein lovely ball..."
na "I... can't live on with the knowledge that I turned our Führer into a..."
scene berlin10 with dissolve
na "...Auf Wiedersehen, cruel world!"
play sound "sounds/gun.mp3"
window hide
with fastflash
fr "NEEEEIIIINN!"
stop sound
scene berlin11 with dissolve
ah "Did this idioten just kill himself? Pfff, what a LOSER!"
scene berlin12 with dissolve
ah "Well, he-llo la-dies... Vat? You've never seen a circumcized Jewish dick before?"
fr "AAAAH! He's a Jew, a horrible Jew! Meine eyes, MEINE EYES!"
ah "Hey! That's totally antisemitic! Fucking nazis..."
scene berlin13 with dissolve
ww "What are we going to do with him? We can't leave him here. He's supposed to be dead."
mc "You're right, this would tear the timeline of the universe apart, and that's a really bad thing apparently."
mc "We have no choice but to take him back with us. BACK TO THE FUTURE!"
play channel1 "v051/backtothefuture.mp3"
ww "Get him to put a robe on at least. I know how prudish the people of 1977 are."
scene berlin14:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
ah "So tell me more about that future of yours, meine friends. Vill I have my own jet-pack? Or at least a flying skateboard?"
mc "Not until 2015 according to..."
ah "But us Jews still rule the world, right? Did vee build space lasers yet?"
stop channel1 fadeout 1.0
mc "Err..."

label BerlinEnd02:
stop sound
scene compoundhall01n with fade
show compoundmilf02 at right with moveinright
cm "Ah, there you are! I was getting worried about you two!"
window hide
show hitler01 at left with moveinleft
ah "Well, hello there, big-titted lady!"
hide compoundmilf02
show compoundmilf03 at right
with fastdissolve
cm "Is that... who I think it is???"
mc "Err, yes. His clone. Who isn't legally responsible for the atrocities committed by his predecessor. So no need to get offended, players, okay?"
hide hitler01
show hitler02 at left
with fastdissolve
ah "Adon Hitlerovich. At your zervice."
hide compoundmilf03
show compoundmilf06 at right
with fastdissolve
cm "What the hell is he babbling about?"
hide hitler02
show hitler01 at left
with fastdissolve
mc "Long story short, Hitler was a Jew all along. With a ball missing, but now he's got two, so..."
hide hitler01
show hitler03 at left
with fastdissolve
ah "Zo I feel like a NEW MAN. An übermensch even!"
hide compoundmilf06
show compoundmilf05 at right
with fastdissolve
cm "And what am I supposed to do with him? He can't stay here!"
mc "We'll shave his moustache, put a kippa on his head and drop him in the Jewish quarter of Cockham. Problem solved."
ah "I'll open a hot zoup kitchen! Two dollars extra for the bread!"
hide compoundmilf05
show compoundmilf02 at right
with fastdissolve
cm "And what about Colonel Stroheim?"
mc "He killed himself when he found out Hitler was a Jew, so we're rid of him for good, Captain MILF!"
play sound "sounds/winning.mp3"
show quest07icon at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
$ quest07end = True
pause
hide hitler03
hide quest07icon
hide winicon
show hitler01 at left
with fastdissolve
ah "So you're a MILF? Sehr interesting. Do you have some Jew in you? Vould you like some?"
hide compoundmilf02
show compoundmilf06 at right
with fastdissolve
cm "* sigh *. Get him out of here."
jump Main