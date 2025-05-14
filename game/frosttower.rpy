label FrostTower:
scene frostofficebackground
show officefrost03
with fade
if  mission07win and spokefrostmission07 == False:
    $ spokefrostmission07 = True
    if laradagger:
        ef "How dare you show your face in here! After you betrayed your landlord and let Lara Crotch get away with the dagger of Ra's-Al-Ghul!"
        mc "The dagger is better destroyed than in your EVIL hands!"
        hide officefrost03
        show officefrost05
        with fastdissolve 
        ef "Get out of my office before I decide to raise your rent to ASTRONOMICAL LEVELS!"
    if emmadagger:
        ef "Ah, my EVIL side-kick and landboy!"
        mc "I prefer to see our relationship as a crime family business."
        hide officefrost03
        show officefrost02
        with fastdissolve 
        ef "I still haven't figured out how to get that dagger to work, but once I do, Cockham WILL BE MINE!"
        mc "You mean OURS, right?"
        hide officefrost02
        show officefrost04
        with fastdissolve
        if evilness >= 15:
            ef "Sure, that's what I meant. In the meantime, I'm horny for some NASTY SEX!"
            mc "Alright!"
            $ evilfrostsex = True
            jump FrostFuckBedroom
        if evilness <= 14:
            ef "Sure, that's what I meant."
    jump Main

if mission06end and hulkharem and hulkescapedfrosttold == False:
    ef "She-Hulk has escaped!"
    mc "Oh damn, that's terrible."
    hide officefrost03
    show officefrost05
    with fastdissolve 
    ef "Your casual answer tells me YOU had something to do with it!"
    mc "Not true! She was out of control anyway, remember?"
    hide officefrost05
    show officefrost01
    with fastdissolve 
    ef "I suppose she was. God only knows where she is now. Hopefully, far far away from Cockham."
    mc "Hopefully..."
    hide officefrost01
    show officefrost04
    with fastdissolve     
    ef "Now go away, I'm very busy. Having to deal with this unforeseen circumstance."
    $ hulkescapedfrosttold = True
    jump Main
        
if  mission06 and mission06end == False and mission06day >= 4 and mission06evil:
    ef "How dare you show your loser face in here!"
    mc "Err... What did I do?"
    hide officefrost03
    show officefrost05
    with fastdissolve 
    ef "You FAILED your mission. You had THREE days and you managed to SCREW IT UP ANYWAY!"
    play sound "sounds/losing.mp3"
    show missionicon06 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission06fail = True
    $ mission06end = True
    hide officefrost05
    show officefrost04
    with fastdissolve 
    ef "Now I need to think about my next move with that failure hanging in the balance. So be gone!"
    jump Main

if  mission06 and mission06end == False and mission06evil:
    ef "Ah, my tenant... I hope you come with GOOD news!"
    mc "Not yet, but I'm working on it."
    hide officefrost03
    show officefrost05
    with fastdissolve 
    ef "That's NOT good news! Go away and come back when you have SUCCEEDED!"
    jump Main

if mission06end and mission06win and mission06evil and toldmission06evil == False:
    ef "Ah, my tenant... I hope you come with GOOD news!"
    mc "I sure do. I have stolen that gold that Stallion stole from some other people. Basically, he doesn't have any gold anymore."
    hide officefrost03
    show officefrost01
    with fastdissolve    
    ef "While you have plenty to share with your landlord I presume!"
    mc "Err... About that. Catwoman then stole the gold that I stole from the Stallion that he stole fr..."
    hide officefrost01
    show officefrost05
    with fastdissolve        
    ef "Oh, do SHUT UP! I got it. You're a USELESS THIEF!"
    mc "But a good SEX Super-Villain though, right?"
    call Evil from _call_Evil_2
    hide officefrost05
    show officefrost04
    with fastdissolve        
    ef "* sigh * I suppose so... But be gone, I need to think about my next move. And your massive horsecock staring me in the face ain't helping."
    $ toldmission06evil = True
    jump Main

if mission05end and quest06end and mission06 == False and frostfucked and evilness >= 13:
    ef "Ah, my tenant... Now that you've vowed fealty to your LANDLORD, she has a mission for you."
    mc "I'm getting confused with genders here."
    hide officefrost03
    show officefrost05
    with fastdissolve    
    ef "Just LISTEN! To impose MY, I mean OUR, reign over Cockham, we must get rid of some \"challengers\", shall we say."
    mc "That's cunning."
    hide officefrost05
    show officefrost02
    with fastdissolve  
    ef "And since I have some little spies embedded within the CCPD, I know the code to the Stallion's safe, where he hides his GOLD. They coaxed it out of some thug they arrested."
    ef "Without his gold, the Stallion will be OUT OF BUSINESS, and the Narrows will fall into my, I mean OUR, hands! You must steal this gold, but there is a time-limit, he changes the code every three days."
    window hide
    play sound "sounds/achievement.mp3"
    $ mission06evil = True
    $ mission06 = True
    show missionicon06 at poslocation
    $ renpy.pause(0.5, hard=True)
    show textmission06 at posmissiontext
    pause                        
    mc "So basically, I am to be engaged in high-end robbery. But I'm not a thief, I don't even know how to open a vault even WITH a code."
    hide officefrost02
    show officefrost01
    with fastdissolve  
    ef "It is your destiny to find a way into that vault. The Villain Side counts on you."
    hide officefrost01 with moveoutleft
    mc "I need to find Catwoman. But who could possibly know her whereabouts?..."
    jump Main

if frostfucked == False and quest06end and toldemmalevel02:
    ef "Well, if it isn't Mr Superhero-with-a-big-cock... Who also happens to be my tenant."
    mc "It is indeed..."
    hide officefrost03
    show officefrost05
    with fastdissolve    
    ef "I heard that you FUCKED every single Superheroine out there. And yet, you still haven't fucked ME, the MOST BEAUTIFUL WOMAN IN THE WORLD!"
    mc "That is clearly an oversight on my part. Or on the dev's part I should say."
    hide officefrost05
    show officefrost04
    with fastdissolve  
    ef "Well, this oversight needs to be corrected. NOW! Follow me..."
    mc "Alright! SEXY FUN TIMES WITH A SEXY SUPER-VILLAINESS, HERE I COME!"
    jump FrostFuckBedroom
if frostfucked and quest06end and toldemmalevel02:
    ef "Well, if it isn't Mr Superhero-with-a-big-cock... Who also happens to be my tenant."
    mc "It is indeed..."
    hide officefrost03
    show officefrost02
    with fastdissolve
    jump FrostTowersDialogues
if frosttoldmc == False and frostfirstvisit:
    ef "You came back..."
    mc "Sure I did. To check on you. You can never be too cautious with Super-Villains."
    jump FrostTruth
if frosttoldmc:
    ef "My tenant. What a nice surprise... Although I had foreseen you coming today..."
    hide officefrost03
    show officefrost02
    with fastdissolve
    jump FrostTowersDialogues
ef "[hero]... Another visit. Unannounced this time I might add..."
mc "Your secretary let me through."
if widowpicked:
    ef "What do you want, I'm a very busy BUSINESS woman."
if frostpicked:
    ef "I did tell her to let YOU through indeed... [name]."
hide officefrost03
show officefrost02
with fastdissolve
$ frostfirstvisit = True
ef "And what is the purpose of your visit? Alone, I might add..."
label FrostTowersDialogues:
menu:
    "...And my big cock is very big right now!" if frostfucked:
        hide officefrost02
        show officefrost05
        with fastdissolve
        ef "Which means you came to FUCK THE MOST BEAUTIFUL WOMAN IN THE WORLD AGAIN?!"
        mc "Your mind reading abilities are beyond doubt."
        hide officefrost05
        show officefrost04
        with fastdissolve  
        ef "Good. Follow me then... To the FUCK LAIR!"
        jump FrostFuckBedroom
    "I have retrieved the Jewel of Mind Control, my, err, landlord." if toldemmajewel == False and quest06end:
        $ toldemmajewel = True
        if evilness >= 13:
            hide officefrost02
            show officefrost04
            with fastdissolve
            ef "Excellent. Give it to me, this jewel will allow us to rule Co..."
            mc "I don't have it. Lara Crotch kept it."
            hide officefrost04
            show officefrost01
            with fastdissolve
            ef "Why did you let her take it! Are you evil or are you a wimpy good boy?"
            mc "I insisted but... she just refused! But I'll get it, I promise!"
            hide officefrost01
            show officefrost05
            with fastdissolve
            ef "You had better, young man. I will not tolerate your FAILURES any longer! Be gone!"
            jump Main
        if evilness <= 12:
            hide officefrost02
            show officefrost03
            with fastdissolve
            ef "Give it to me then! GIVE IT TO ME!"
            play sound "sounds/radiation02.mp3"
            mc "I... would... if I had it."
            hide officefrost03
            show officefrost05
            with fastdissolve
            stop sound
            ef "Pff! You're USELESS. Get out of my sight!"
            jump Main
    "I have now reached Superhero level 2, White Queen!" if toldemmalevel02 == False and mclevel02:
        $ toldemmalevel02 = True
        if evilness >= 13:
            hide officefrost02
            show officefrost04
            with fastdissolve
            ef "Excellent. I can now plan the next stage of our conquest of the power levers of Cockham City."
            mc "That sounds ominous."
            hide officefrost04
            show officefrost01
            with fastdissolve
            ef "It certainly will be something to BEHOLD. Until then, maintain your evilness level. Or even better yet, INCREASE IT!"
            mc "As you wish, err... landlord."
            jump Main
        if evilness <= 12:
            ef "And I should care because?..."
            mc "Well, I am now a FORMIDABLE adversary."
            hide officefrost02
            show officefrost05
            with fastdissolve
            ef "Pff! You don't scare me, [hero]. I have vanquished far greater foes... Now begone until you realize what you NEED TO DO."
            jump Main
    "I heard you bought the research Division of Vayne Enterprises" if lpspeakef01:
        hide officefrost02
        show officefrost01
        with fastdissolve
        voice "frost/tower01"
        ef "I did indeed. I will make this research division GREAT AGAIN!"
        mc "I might have heard that line before. Even if it is 1977."
        hide officefrost01
        show officefrost02
        with fastdissolve
        jump FrostTowersDialogues
    "What exactly is your BUSINESS?":
        hide officefrost02
        show officefrost04
        with fastdissolve
        voice "frost/tower02"
        ef "None of YOUR business."
        mc "Ah. touché."
        hide officefrost04
        show officefrost02
        with fastdissolve
        jump FrostTowersDialogues
    "So, which side are you on, REALLY?":
        hide officefrost02
        show officefrost03
        with fastdissolve
        voice "frost/tower03"
        ef "The right side."
        mc "Err, is that the good side or the evil side?"
        hide officefrost03
        show officefrost05
        with fastdissolve
        voice "frost/tower04"
        ef "It's the right side. As I said..."
        hide officefrost05
        show officefrost02
        with fastdissolve
        mc "I'm still confused..."
        jump FrostTowersDialogues
    "Landlord, I am ready to train with you." if frosttoldmc and frosttrainedresistance == False:
        hide officefrost02
        show officefrost03
        with fastdissolve
        if evilness <= 9:
            ef "And why would I train a Super-Hero who clearly hasn't chosen the RIGHT SIDE?"
            mc "Err, cos I'm your landboy? And you get half my rent."
            hide officefrost03
            show officefrost05
            with fastdissolve            
            ef "And you refuse to JOIN ME on the OTHER SIDE! SO get lost!"
            mc "Gee, landlord-tenant drama right there..."
            jump Main
        if frostchosegood:
            ef "And why would I train a Super-Hero who REFUSES to join me?"
            if evilness >= 13:
                mc "I made a mistake, but now I'll become a Super-Villain, I swear!"
                hide officefrost03
                show officefrost04
                with fastdissolve 
                ef "I'll give you the benefit of the doubt. I will teach you Super-Resistance. So you can resist Captain MILF if she tries to lead you back into the fold..."
                mc "Alright!"
                hide officefrost04
                show officefrost03
                with fastdissolve
                ef "Follow me, my landboy."
                jump FrostResistanceTraining
        if evilness >= 10 and evilness <= 12:
            ef "And why would I train a Super-Hero who clearly can't choose what side to be on?"
            mc "Well, I've been hesitating, that's true, and I like to stay neutral, but now I've seen the light and I'll become a Super-Villain, I swear!"
            hide officefrost03
            show officefrost04
            with fastdissolve 
            ef "I'll give you the benefit of the doubt. I will teach you Super-Resistance. So you can resist Captain MILF if she tries to lead you back into the fold..."
            mc "Alright!"
            hide officefrost04
            show officefrost03
            with fastdissolve
            ef "Follow me, [name]."
            jump FrostResistanceTraining               
        ef "Good. I will teach you Super-Resistance. So you can resist Captain MILF if she tries to lead you back into the fold..."
        if mcresistance == 0:
            mc "Oh, great, I don't have any of that stuff..."
        if mcresistance == 1:
            mc "I already have some Super-Resistance actually. Level 1 to be more precise."
            ef "Then you will reach level 2..."
            mc "Oooh! Level 2? I'm in!"
        hide officefrost03
        show officefrost04
        with fastdissolve
        ef "Follow me, [name]."
        jump FrostResistanceTraining
    "Landlord, I am ready to train with you some more." if frosttrainedcontrol == False and frosttrainedresistance and questhulkcompleted:
        hide officefrost02
        show officefrost03
        with fastdissolve
        if evilness <= 9:
            hide officefrost03
            show officefrost05
            with fastdissolve            
            ef "You're STILL on the Hero route. Come back when you're DEDICATED to the Super-Villain route!"
            mc "I'm a free boy, I do what I want WHEN I want!"
            jump Main
        if evilness >= 10 and evilness <= 12:
            hide officefrost03
            show officefrost05
            with fastdissolve            
            ef "You're STILL on the Neutral path. The one for WIMPS who can't make up their minds! Come back when you're DEDICATED to the Super-Villain route!"
            mc "I'm a free boy, I do what I want WHEN I want!"
            jump Main
        ef "Good. I will teach you Mind Control. So you can control other weak superheroes and bring them to the VILLAIN SIDE."
        mc "That sounded pretty ominous."
        if hulkescaped == False:
            hide officefrost03
            show officefrost04
            with fastdissolve
            ef "But I need a test subject for that. You need to let She-Hulk ESCAPE. I will easily find her, considering the amount of havoc she usually wreck, and bring her back here."
            mc "Oh, so I have to stop fucking her for a week or so?"
            hide officefrost04
            show officefrost02
            with fastdissolve
            ef "That is correct. And it is what I said. Come back once She-Hulk has escaped. And you will master the Villain Art of MIND CONTROL. At least level 1 that is."
            jump Main
        if hulkescaped:
            hide officefrost03
            show officefrost04
            with fastdissolve
            ef "And I have a test suject for you to practice on, since you very naughtily let She-Hulk escape. I easily captured her through my Mind Control abilities."
            mc "I did that?"
            hide officefrost04
            show officefrost02
            with fastdissolve
            ef "Follow me, [name]."
            jump FrostControlTraining
    "How about we continue where we left off last time?":
        if widowpicked:
            hide officefrost02
            show officefrost04
            with fastdissolve
            voice "frost/tower05"
            ef "If I remember correctly, you mistakingly believe I'm NOT the most beautiful woman in the world! So get LOST!"
            mc "Ah yeah, that's correct, I did pick the Black Widow. But that was a ruse."
            hide officefrost04
            show officefrost05
            with fastdissolve
            voice "frost/tower06"
            ef "You think I'm going to fall for THAT?"
            mc "Err..."
            hide officefrost05
            show officefrost02
            with fastdissolve
            jump FrostTowersDialogues
        if frostpicked:
            hide officefrost02
            show officefrost04
            with fastdissolve
            voice "frost/tower07"
            ef "I don't need anything more from you. You recognized that I AM the most beautiful woman in the world, and that is all I wanted."
            mc "Yeah, but what about a reward for that?"
            hide officefrost04
            show officefrost05
            with fastdissolve
            voice "frost/tower08"
            ef "You only admitted the OBVIOUS! You want a fucking medal for that?"
            mc "Err..."
            hide officefrost05
            show officefrost02
            with fastdissolve
            jump FrostTowersDialogues
    "I'm horny. Are you horny? Cos I could use your pussy to relieve my horniness." if frostfucked:
        hide officefrost02
        show officefrost03
        with fastdissolve
        ef "Well, well, well. I'm guessing you didn't use Super-Seduction to come out with THAT LAME ASS line."
        mc "I didn't indeed. Made it up all by myself without using any superpowers."
        hide officefrost03
        show officefrost01
        with fastdissolve
        ef "Well, you're in luck because it so happens that I'm not too busy today... And that I'm VERY HORNY TOO! So follow me to my fuck lair..."
        jump FrostFuckBedroom
    "I'm done here.":
        hide officefrost02
        show officefrost03
        with fastdissolve
        voice "frost/tower09"
        ef "Good, since I am VERY BUSY."
        jump Main

label FrostTruth:
play music "sounds/truth.mp3"
$ frosttoldmc = True
hide officefrost03
show officefrost01
with fastdissolve
voice "frost/tower10"
ef "[hero]. There is something you need to know."
mc "Go on, I'm all ears. What is it?"
voice "frost/tower11"
ef "You are now old enough to learn the TRUTH."
mc "What truth?"
hide officefrost01
show officefrost03
with fastdissolve
voice "frost/tower12"
ef "You do not yet realize your importance. You have only begun to discover your superpowers."
mc "Yeah, sure, it's only the start of the game."
hide officefrost03
show officefrost04
with fastdissolve
voice "frost/tower13"
ef "Join me and I will complete your training. With our combined strength, we can end this destructive conflict and bring order to Cockham."
mc "I will never join you!"
voice "frost/tower14a"
ef "If you only knew the power of the villain side. Captain MILF never told you what happened to your landlord."
mc "Why would she?"
window hide
pause
hide officefrost04
show officefrost01
with fastdissolve
voice "frost/tower15a"
ef "[name]... I am your landlord."
mc "I'm pretty sure Captain Milf is the one I pay my rent to."
hide officefrost01
show officefrost02
with fastdissolve
voice "frost/tower16"
ef " * sigh * It was a long time ago, just over [age] years to be precise. I was fighting Captain MILF on a different astral plane. I morphed into a diamond titan..."
hide officefrost02
show officefrost01
with fastdissolve
voice "frost/tower17a"
ef "In the throes of battle, I... impregnated her. Naturally, we bought a house together nine months later. I AM YOUR LANDLORD."
mc "No. No. That's not true! That's impossible! This is an adult VN and all landlords are DEAD or have conveniently and permanently left the house years ago!"
hide officefrost01
show officefrost05
with fastdissolve
voice "frost/tower18"
ef "Search your feelings. You know it to be true."
mc "No! No! No!"
hide officefrost05
show officefrost03
with fastdissolve
voice "frost/tower19a"
ef "Join me, and together we can rule Cockham as landlord and tenant. Come with me. It is the only way."
menu:
    "I...feel strangely attracted to you... (+1 Super-Villain)":
        call Evil from _call_Evil_3
        $ frostchoseevil = True
        voice "frost/tower20a"
        ef "I had foreseen it. It is your Destiny, my dear landboy."
        mc "I have a question, err... landlord. When you titfucked me in the intro, was that... homosexual landlord-landboy sex, then?"
        hide officefrost03
        show officefrost04
        with fastdissolve
        voice "frost/tower21"
        ef " * sigh * Go back home and think hard about your DESTINY."
        mc "Alright. I'll try and do that..."
        jump Main        
    "I... must resist. I WILL NEVER JOIN YOU! (+1 Super-Hero)":
        call Good from _call_Good_2
        $ frostchosegood = True
        hide officefrost03
        show officefrost04
        with fastdissolve
        voice "frost/tower22a"
        ef "I had not foreseen this. Your destiny is a blur... Leave before I decide to exact my vengeance upon you. Landboy."
        jump Main

label FrostResistanceTraining:
$ frosttrainedresistance = True
play music "sounds/underworld.mp3"
scene frosttrain01 with dissolve
ef "Now [name], get naked. I would not want to burn or freeze your thong."
mc "Naked? Is that really necessary?"
ef "Yes it is. Trust me. You know you can trust your landlord, right?"
mc "I guess so..."
scene frosttrain02 with dissolve
if age >= 20:
    ef "I see that your giant dangling boyhood is stil as MASSIVE as I remember..."
if age >= 18 and age <= 19:
    ef "I see that your giant teenage dangling boyhood is stil as MASSIVE as I remember..."
scene frosttrain03 with dissolve
ef "I'm wondering... What part of your body needs the most to become Super-Resistant? In other words, what is the most IMPORTANT part of your body?"
scene frosttrain04 with dissolve
mc "Well, I don't like to brag or anything, but obviously, my superior Alpha-Cock is the most imp..."
scene frosttrain05 with dissolve
play sound "sounds/magic.mp3"
ef "Then I'll freeze your cock!"
mc "Why the hell are you doing that? It fucking HURTS! My cock, MY COCK, it's gonna fall off!"
scene frosttrain06 with dissolve
ef "Not if you increase your blood pressure and make it HEAT UP with EXTREME VIGOR!"
mc "And how the fuck do I do that?"
scene frosttrain07 with dissolve
ef "You must TENSE all your muscles and PUMP THE BLOOD FROM YOUR HEART INTO YOUR GROIN!"
play sound "sounds/mangrunt01.mp3"
mc "AAAAH!!!"
scene frosttrain08 with dissolve
mc "AAAH, fuck, I'm getting there!"
ef "Keep going, keep PUMPING THAT BLOOD!"
scene frosttrain09 with dissolve
play sound "sounds/brokenglass.mp3"
mc "FUCK YEAH! I've Super-Resisted your vicious freezing attack! And now I'm ROCK-HARD TOO!"
ef "I can see that... It seems to be SCALDING HOT."
scene frosttrain10 with dissolve
play music "sounds/thunder.mp3"
ef "I wonder how HOT it can get!"
mc "Oh no, no no no, please!"
scene frosttrain11 with dissolve
play sound "sounds/magic.mp3"
mc "FUCK ME! She's got lightning bolts coming out of her eyes!"
scene frosttrain12 with dissolve
stop music
play sound "sounds/magic.mp3"
ef "And you'd better do something about it, boy, or your cock will MELT like butter!"
mc "My precious dong, it's red-hot, but not the kind of hotness I like!!!"
scene frosttrain13 with dissolve
ef "Let the heat escape, by chasing it away with MORE BLOOD AND HEAT!"
play sound "sounds/mangrunt01.mp3"
mc "Right, I need to concentrate..."
window hide
with hpunch
mc "LET THE HEAT FLOW!"
scene frosttrain14 with dissolve
play sound "sounds/boymoan04.mp3"
mc "AAAAH!!! Get off me, RED-HOT EMBERS!"
ef "Well done, they are turning blue, meaning you have Super-resisted the extreme heat from my lightning bolts..."
scene frosttrain15 with dissolve
call ResistancePlus from _call_ResistancePlus
mc "I did it, I've acquired Super-Resistance! Now I can defeat all my ENEMIES!!!"
ef "Let's not push it. Some enemies perhaps, but POWERFUL ones will take MORE training to defeat..."
mc "You've destroyed my hopes and dreams of an early game victory... And I'm getting soft."
scene frosttrain02 with dissolve
ef "Now pledge allegiance to ME, [hero]! Pledge allegiance to the VILLAIN SIDE!"
menu:
    "Of course, my landlord. (+ 1 Super-Villain)":
        scene frosttrainend01 with dissolve
        call Evil from _call_Evil_4
        ef "Together, we shall RULE COCKHAM!"
        mc "Err, when?"
        ef "Probably, like, in v0.9 or later."
        mc "What a bummer. That's like years away."
        ef "If the dev was called ICSTOR or L\&P, yes, but he's not."
        jump Main
    "I changed my mind, I don't want to join the Villain Side. (+ 1 Super-Hero)":
        scene frosttrain02 with dissolve
        call Good from _call_Good_3
        ef "I will make you pay for your DECEIT!"
        scene frosttrainend02 with dissolve
        play sound "sounds/punch.mp3"
        mc "AAAH! I'm flying backwards!"
        scene frosttrainend03 with dissolve
        mc "Finally, I'm not flying backwards anymore thanks to that wall. By the way, thanks for the free training..."
        ef "I wil NEVER train you again!"
        $ frostnevertrain = True
        jump Main
        
label FrostControlTraining:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/underworld.mp3"
$ frosttrainedcontrol = True
scene frostcontrol01 with fade
ef "There she is. I have created an astral projection around her. She cannot see you, she is totally oblivious to her surroundings right now."
mc "Oh good, cos she's super-strong and can go berserk pretty easily."
scene frostcontrol02 with dissolve
ef "Indeed. Which is why you will have to face your own worst fears once I remove her projection. In order to control her, you must first learn to control your OWN MIND!"
mc "Err... And how do I do that?"
scene frostcontrol03 with dissolve
ef "You will feel the pain and torment inside your head. I will mentally guide you."
mc "Thanks God for that, it doesn't sound very ni..."
scene frostcontrol02 with dissolve
ef "But I'll also make sure to be several feet behind you when your training starts. I don't want any blood stains on my costume."
mc "Ah. So you're mentally predicting she's gonna beat me to a pulp then?"
scene frostcontrol03 with dissolve
ef "If she attacks you, use both your Super-Strength AND Mind Control to TAME HER!"
scene frostcontrol04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
ef "Are you ready?"
scene frostcontrol05 with dissolve
mc "Yeah. Hang on. Control my mind, use Super-Strength, control her mind. Yep, ready now!"
ef "NOW!"
scene frostcontrol06 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "Uh- oh..."
call screen usepower("usestrength", "FrostHulkNoStrength", "FrostHulkStrength") with dissolve
label FrostHulkNoStrength:
scene frostcontrol07 with dissolve
play sound "sounds/punch.mp3"
mc "FU-UUUCK! She head-butted me!"
hu "AAAARRHH!"
jump FrostControlTraining02
label FrostHulkStrength:
scene frostcontrol07 with dissolve
play sound "sounds/punch.mp3"
mc "FU-UUUCK! That did nothing against her superior strength, she still head-butted me!"
hu "AAAARRHH!"
label FrostControlTraining02:
scene frostcontrol08 with dissolve
play sound "sounds/punch.mp3"
mc "Put the shield back on please, Landlord! She's gonna tear me apart!"
play sound "sounds/hulkgrowl.mp3"
ef "* grunt * Fine, but for ONLY THIS ONCE TIME!"
scene frostcontrol09 with dissolve
play sound "sounds/panting.mp3"
mc "I don't want to do this, I can't, this is too hard!"
ef "Go back in there, you wimp! I will not tolerate your cowardice!"
mc "Gee, maybe I should have stayed neutral. I would be less bloodied."
scene frostcontrol10 with dissolve
mc "I have an idea. As usual with all my great ideas, it involves my ALPHA-COCK!"
ef "Whatever it takes, although I would prefer for your dick to remain intact. As your landlord, I am very proud of your tenant dong."
scene frostcontrol11 with dissolve
if age >= 20:
    mc "I will mesmerize her with the Super-Studliness of my ungodly phallus."
if age >= 18 and age <= 19:
    mc "I will mesmerize her with the Super-Studliness of my ungodly teenage phallus."
ef "Not as beautiful as I am, but I get where you're going."
mc "And then, I will be able to control her mind. With my COCK!"
scene frostcontrol02 with dissolve
ef "Interesting theory. It sure worked with Captain MILF when I turned into a monstrously-hung titan [age] years ago."
scene frostcontrol12 with dissolve
mc "And now, let's see how you react to THIS Super-Cock, She-Hulk!"
play sound "sounds/hulkgrowl.mp3"
mc "Oh, you're growling? You'll be MOANING soon when I'm CONTROLLING your mind! Remove the barrier Emma, I AM READY!"
scene frostcontrol13 with dissolve
hu "GRRRLLLL! RH????...."
mc "Yeah, yeah, that's right, now you're already subdued, aren't you?"
ef "Project your tormented mind onto hers to CONTROL her now, [hero]!"
mc "Alright..."
scene frostcontrol14 with dissolve
play channel1 "sounds/radiation02.mp3"
mc "AAAAH, it's... painful! MUST... FIGHT... THE PAIN!"
ef "And the torment. Don't forget the torment. Project all your dark feelings inside her mind, may the villain Force be with you!"
scene frostcontrol15 with dissolve
play sound "sounds/effort01.mp3"
mc "She's holding me tight... I need to resist while she's still confused about my cock!"
call screen usepower("usestrength", "FrostHulkNoStrength02", "FrostHulkStrength02") with dissolve
label FrostHulkNoStrength02:
mc "I can't NOT USE my Super-Strength right now or I die and it's game over!"
label FrostHulkStrength02:
$ usedstrength += 1
scene frostcontrol16 with dissolve
mc "And now... Transfer my TORMENT INTO HER MIND!"
stop channel1
play sound "sounds/magic.mp3"
call ControlPlus from _call_ControlPlus
mc "It's working! I'm a Super-Villain mind controller!"
scene frostcontrol17 with dissolve
mc "And now PRAISE MY COCK, She-Hulk!"
hu "AAARH! Ssso BIG, Master!"
mc "Damn right it's big. And so are my balls and they demand some WORSHIP from your tongue!"
play channel2 "sounds/lick01.ogg"
scene frostcontrol18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
$ renpy.pause(2.0, hard='True')
ef "What the hell do you think you're doing?"
play sound "sounds/boymoan02.mp3"
mc "Errr, AAAAH! I'm getting my balls licked by She-Hulk, why do you ask?"
scene frostcontrol19 with dissolve
play sound "sounds/boymoan03.mp3"
mc "Oh God, she's sticking a finger up my arse, I didn't ask her to do that!"
ef "She's feeding on your emotions. POSITIVE emotions. You'd better get rid of them quickly, [name]!"
scene frostcontrol20 with dissolve
stop channel2
play sound "sounds/lick03.mp3"
mc "Uuuuh, she's going to make me..."
scene frostcontrol21 with dissolve
play channel2 "sounds/boyorgasm01.mp3"
mc "....COME, AAAAHHHHH!"
window hide
with fastflash
ef "That's TOO MUCH positive emotions!"
scene frostcontrol22 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "FUUU-UUUCK, she's grabbing my nuts!"
window hide
with hpunch
ef "I told you to be VILLAINOUS when you use Mind Control!"
scene frostcontrol23 with dissolve
mc "That's it, you cum-hungry whore, I'm gonna blow my wads directly onto your filthy green breasts, like a villain would do!"
window hide
with fastflash
ef "That's more like it!"
scene frostcontrol24 with dissolve
mc "RHAA, thake that, She-Hulk!"
window hide
with hpunch
if age >= 20:
    ef "You're taming her again, thanks to your endless supply of virile scum!"
if age >= 18 and age <= 19:
    ef "You're taming her again, thanks to your endless supply of virile teenage scum!"
hu "UUUUH..."
scene frostcontrol25 with dissolve
stop channel2
play sound "sounds/panting.mp3"
mc "Phew! I almost got my nuts squashed into pancakes by her..."
ef "That's because you used Mind Control to get your rocks off instead of using it to make your mind slave do EVIL things!"
scene frostcontrol26 with dissolve
mc "ALright, I get it now. I'm on the Super-Villain path and I should stick to it."
scene frostcontrol27 with dissolve
ef "Exactly. And with our combined forces, we shall RULE COCKHAM TOGETHER!"
mc "And then do what exactly?"
scene frostcontrol03 with dissolve
ef "Just go back to your compound, you clearly need more TRAINING before you are READY. Also, please reach Level 2 soon, you're too weak an assistant as it stands."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label FrostFuckBedroom:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene frostfuck01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
if frostfucked:
    ef "You know the drill. Get into those \"easy-fuck-access\" shorts and I'll get ready for our FUCK SESSION."
    mc "Err, alright."
if frostfucked == False:
    ef "This is my fuck lair. It's where I FUCK my STUDS. And you're the BIGGEST of them all."
    mc "Damn right, these pindicks have nothing on me!"
    ef "I left some special shorts for you to wear. Put them on while I change into my FUCK OUTFIT..."
    mc "Err, alright."

scene frostfuck02 with dissolve
if frostfucked:
    mc "Right, I'm ready. Ah, here she comes..."
if frostfucked == False:
    mc "These shorts are indeed \"special\". My cock is totally hanging out. I guess it's for easy access. Ah, here she comes..."
play music "sounds/sexy02.mp3" volume 0.75
window hide
show frostfuck03 blurred:
    zoom 1.1 xoffset 0 yoffset -1000
show frostfuck04:
    xoffset -50 yoffset -1080    
show frostfuck03 blurred at scarlettfullzoombackground
show frostfuck04 at scarlettfullzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause        
ef "So, how do like my FUCK OUTFIT, [hero]?"
mc "It's telling my cock: get HARD and READY!"
window hide
hide frostfuck04
show frostfuck03 blurred:
    zoom 1.1 xoffset 0 yoffset 0
show frostfuck05:
    xoffset 50 yoffset 0    
show frostfuck03 blurred at scarlettfulldownzoombackground
show frostfuck05 at scarlettfulldownzoom
with dissolve
$ renpy.pause(6.0, hard='True')
pause
ef "And is it? Are you getting HARD and READY for me, [name]?"
mc "I sure am! It just takes a little while to fill up with blood, cos it needs a GALLON of it!"
scene frostfuck06 with dissolve
ef " A gallon of blood? Now let's see this [age]yo MONSTERCOCK up close and personal then..."
scene frostfuck07 with dissolve
ef "Doesn't look very hard... Maybe it needs my warm mouth to speed things up... Bring that dong over here..."
scene frostfuck08 with dissolve
ef "Now that's better, I can feel it ENGORGING."
mc "Ooh yeah! Fuck, that's a warm, WIDE mouth!"
scene frostfuck09 with dissolve
ef "It can get even WIDER and WARMER... If you FUCK MY MOUTH WITH IT!"
play channel1 "v032/blow03.mp3"

label FrostBedSuckSlow:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckslowvideo behind frostbedsuckfastvideo
show frostbedsuckslowvideo behind frostbedsuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckfastvideo
hide frostbedsuckpovslowvideo
with dissolve
play channel1 "v032/blow03.mp3"
$ frostbedsuckfast = False
if frostbedsuckslow == False:
    mc "Damn, your mouth was really made for sucking HUGE COCKS!"
    $ frostbedsuckslow = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen frostbedsuckslow()
screen frostbedsuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostBedSuckFrontSlow")

label FrostBedSuckFast:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckfastvideo behind frostbedsuckslowvideo
show frostbedsuckfastvideo behind frostbedsuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckslowvideo
hide frostbedsuckpovfastvideo
with dissolve
play channel1 "sounds/blow02.mp3"
$ frostbedsuckslow = False
if frostbedsuckfast == False:
    mc "Let me pump my shaft in that warm throat even FASTER!"
    $ frostbedsuckfast = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen frostbedsuckfast()
screen frostbedsuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostBedSuckFrontFast")

label FrostBedSuckFrontSlow:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckpovslowvideo behind frostbedsuckslowvideo
show frostbedsuckpovslowvideo behind frostbedsuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckslowvideo
hide frostbedsuckpovfastvideo
with dissolve
play channel1 "v032/blow03.mp3"
$ frostbedsuckfast = False
if frostbedsuckslow == False:
    mc "Damn, your mouth was really made for sucking HUGE COCKS!"
    $ frostbedsuckslow = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen frostbedsuckpovslow()
screen frostbedsuckpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckSlow")

label FrostBedSuckFrontFast:
window hide
hide nexticon
hide slower
hide faster
hide pov
hide front
show frostbedsuckpovfastvideo behind frostbedsuckfastvideo
show frostbedsuckpovfastvideo behind frostbedsuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide frostbedsuckfastvideo
hide frostbedsuckpovslowvideo
with dissolve
play channel1 "sounds/blow02.mp3"
$ frostbedsuckslow = False
if frostbedsuckfast == False:
    mc "Let me pump my shaft in that warm throat even FASTER!"
    $ frostbedsuckfast = True
window hide
pause
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show front:
     xpos 1700 ypos 500     
call screen frostbedsuckpovfast()
screen frostbedsuckpovfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostBedSuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostBedSuckFast")

label FrostBedSuckEnd:
hide nexticon
hide slower
hide faster
hide pov
hide front

stop channel1
scene frostpostsuck01 with dissolve
play sound "sounds/lick01.ogg"
ef "Let me clean up your godly boyhood..."
mc "Be my guest. I think you missed a spot."
scene frostpostsuck02 with dissolve
play sound "sounds/lick02.mp3"
ef "There?"
mc "Yeah, oooh, that's better..."
scene frostpostsuck03 with dissolve
stop sound
ef "Time for the main dish. MY PUSSY!"
mc "And I am HUNGRY!"
scene frostpostsuck04 with dissolve
if widowpicked and frostfucked == False:
    ef "Do you NOW recognize my superior beauty? Compared to that filthy whore Natasha?"
    mc "Oh man, totally!"
if (frostpicked and frostfucked == False) or frostfucked:
    ef "The most beautiful woman in the world is YOURS today... For a short while."
    mc "Good enough for me!"
scene frostpostsuck05 with dissolve
ef "You will have to take your time of course. And don't you DARE cum before I DO!"
mc "I would never entertain such a preposterous proposition."
if age >= 20:
    ef "Good, now come and make me WET. Make me DESIRE you. You and your giant BOYMEAT!"
if age >= 18 and age <= 19:
    ef "Good, now come and make me WET. Make me DESIRE you. You and your giant TEENAGE BOYMEAT!"
scene frostpostsuck06 with dissolve
play sound "sounds/moan02.mp3"
ef "Mmh, I like my boys MUSCULAR and HUNG! And you are th..."
scene frostpostsuck07 with dissolve
play sound "sounds/kiss.mp3"
ef "* kiss * You know how to NOT TALK to a woman..."
scene frostpostsuck08 with dissolve
mc "Let's get this pussy nice and wet for a MASSIVE INSERTION!"
play sound "sounds/moan02.mp3"
ef "Oooh..."                                  

label FrostRoomFuckSlow:
hide cum
hide faster
hide slower
show frostbedfuckslowvideo behind frostbedfuckfastvideo
$ renpy.pause(1.0, hard=True)
hide frostbedfuckfastvideo with dissolve
play channel1 "sounds/womansex03.mp3"
ef "I've never been stretched like this before in my life, you're a SEX GOD!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500
call screen frostbefuckslow()
screen frostbefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(110, 60)        
        action Jump ("FrostRoomFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostRoomFuckEnd")

label FrostRoomFuckFast:
hide cum
hide faster
hide slower
ef "Fuck me FASTER, I NEED to CUM!"
show frostbedfuckfastvideo behind frostbedfuckslowvideo
$ renpy.pause(1.0, hard=True)
play channel1 "sounds/womansex04.mp3"
hide frostbedfuckslowvideo with dissolve
show cum:
    xpos 1750 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen frostbefuckfast()
screen frostbefuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("FrostRoomFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostRoomFuckEnd")

label FrostRoomFuckEnd:
hide cum
hide slower
hide faster
ef "Oh, I'm cumming, just right there, just right... THERE... AAAH!"
play sound "v032/womancum04.mp3"
scene frostfuckcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "So am I!"
window hide
with fastflash
ef "Yes, give me your YOUNG CUM!"
scene frostfuckcum02 with dissolve
play sound "sounds/womancum01.mp3"
ef "AAAH, so DEEP!"
window hide
with hpunch
mc "Fuck yeah, take that, CUM-SLUT!"
scene frostfuckcum03 with dissolve
play sound "sounds/womancum02.mp3"
ef "You're insulting me but I don't care, I just LOVE the feel of your massive shots filling me up!"
window hide
with fastflash
mc "There's more for YOU, as DEEP as I can go! EIGHTEEN INCHES DEEP!"
scene frostfuckcum04 with dissolve
play sound "v032/womancum03.mp3"
ef "AAAH!"
window hide
with hpunch
ef "There's so much sweet cum sloshing inside my belly!"
scene frostfuckcum05 with dissolve
mc "That's right! I'm gonna make you pregnant and you're going to be MINE!"
window hide
with fastflash
play sound "v032/womancum04.mp3"
ef "Dear Lord, you're a CUM-MACHINE! AAAH!"
scene frostfuckcum06 with dissolve
ef "gggg....So...Gggg-oood!"
window hide
with fastflash
mc "Here's the last of my monster load, RHAAA!"
stop channel2
stop channel1
scene frostfuckcum07 with dissolve
play sound "sounds/panting.mp3"
if frostfucked:
    mc "Wow, I totally impregnated you. Again."
    ef "And I totally will take an abortion pill to stop my pregnancy. Again."
    mc "DAMN IT!"
    if evilfrostsex:
        scene frostpreanal01 with dissolve
        ef "But since you've been such a VILLAINOUS Super-hero, I'm offering you my ASS as a SEX REWARD!"
        mc "Alright!"
        play sound "sounds/slurp.mp3"
        ef "After I finish cleaning myself up. I don't like being dirty at all."
        jump EmmaSexAss
    if hulkescaped and hulkescapedfrost == False:
        menu:
            "Stay with her and help SHe-Hulk escape (+1 Hero)":
                jump HulkEscape
            "Go back home":
                pass
    ef "Now go back to your compound, I need to get cleaned up. STUD LANDBOY."    
if frostfucked == False:
    $ frostfucked = True
    mc "Wow, I totally impregnated you."
    ef "Good thing I have abortion pills..."
    mc "Abortion pills? What the hell is that?"
    ef "A recently developed drug that allows women to CONTROL their bodies. A bit like MIND CONTROL, but for fetuses."
    mc "Damn, so I didn't impregnate you then?"
    if evilfrostsex:
        scene frostpreanal01 with dissolve
        ef "Certainly not. But since you've been such a VILLAINOUS Super-hero, I'm offering you my ASS as a SEX REWARD!"
        mc "Alright!"
        play sound "sounds/slurp.mp3"
        ef "After I finish cleaning myself up. I don't like being dirty at all."
        jump EmmaSexAss
    ef "Certainly not! Now go back to your compound, I need to get cleaned up. STUD LANDBOY."
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label EmmaSexAss:
play music "sounds/sexy13.mp3" volume 0.5
scene frostpreanal02 with dissolve
ef "First, I want you to show me how NASTY you can be, boy! By giving me a RIMJOB!"
mc "I've done it before and I'll gladly do it again. If ANAL SEX follows, obviously."
scene frostpreanal03 with dissolve
ef "It will, it will... But my rosebud needs some prepping for your mighty pecker."
mc "Alright then..."
scene frostpreanal04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "It does look... appetizing."
ef "Of course it is, I keep it squeaky clean!"
scene frostpreanal05 with dissolve
play sound "sounds/lick01.ogg"
ef "Mmh, yeah. Stick that tongue in there and WIGGLE IT!"
window hide
play channel1 "sounds/lick02.mp3"
show frostrimjobvideo
$ renpy.pause(1.0, hard='True')
pause
stop channel1
scene frostpreanal06 with dissolve
play sound "sounds/moan02.mp3"
ef "Mmmh, you did very well, my young trainee..."
scene frostpreanal07 with dissolve
mc "Then it's time to move on to the MAIN COURSE. My [age]yo SUPER-COCK in your SUPER-TIGHT ASS!"
scene frostpreanal08 with dissolve
mc "First, let's stick the head in..."
play sound "sounds/moan01.mp3"
ef "Slowly please..."
mc "And the rest should follow..."
scene frostpreanal09 with dissolve
mc "...Like so..."
play sound "sounds/moan04.ogg"
ef "AAAH!"
scene frostpreanal10 with dissolve
mc "And now we're ready for ANAL DESTRUCTION!"
ef "Oh Lord, why did I acce..."

label FrostAnalSlow:
$ frostanalfast = False
window hide
show frostanalslowvideo behind frostanalfastvideo
show frostanalslowvideo behind frostanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide frostanalfastvideo
hide frostanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalslow == False:
    $ frostanalslow = True
    ef "You're filling me up so MUCH!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen frostanalslow()
screen frostanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalBackSlow")

label FrostAnalFast:
$ frostanalslow = False
window hide
show frostanalfastvideo behind frostanalslowvideo
show frostanalfastvideo behind frostanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide frostanalbackfastvideo
hide frostanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalfast == False:
    $ frostanalfast = True    
    ef "Oh God, you're gonna ass-fuck me even FASTER? AAAH!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen frostanalfast()
screen frostanalfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalBackFast")

label FrostAnalBackSlow:
$ frostanalfast = False
window hide
show frostanalbackslowvideo behind frostanalslowvideo
show frostanalbackslowvideo behind frostanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide frostanalbackfastvideo
hide frostanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if frostanalslow == False:
    $ frostanalslow = True
    ef "You're filling me up so MUCH!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen frostanalbackfuckslow()
screen frostanalbackfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalBackFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalSlow")

label FrostAnalBackFast:
$ frostanalslow = False
window hide
show frostanalbackfastvideo behind frostanalfastvideo
show frostanalbackfastvideo behind frostanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide frostanalfastvideo
hide frostanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
if frostanalfast == False:
    $ frostanalfast = True    
    ef "Oh God, you're gonna ass-fuck me even FASTER? AAAH!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen frostanalbackfuckfast()
screen frostanalbackfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostAnalBackSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("FrostAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("FrostAnalFast")

label FrostAnalEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
ef "Come on, I can't take much more of this, BLOW YOUR NUTSAUCE IN MY ASS!"
mc "I could be Super-Villain and carry on but since you're my landlord, I'll..."
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge02.mp3"
scene frostanalcum01 with dissolve
mc "...give you what you want, RHAAA!!!"
window hide
with fastflash
ef "YES, FINALLY!"
scene frostanalcum02 with dissolve
mc "You want nutsauce? I'll give you NUTSAUCE, AAAH!"
window hide
with hpunch
mc "RIGHT UP YOUR INTESTINES!"
scene frostanalcum03 with dissolve
play sound "sounds/womancum01.mp3"
ef "AAAH, you're so fucking DEEP!!!!"
window hide
with fastflash
if age >= 20:
    mc "Eighteen inches of MEGACOCK DEEP!!!!"
if age >= 18 and age <= 19:
    mc "Eighteen inches of TEEN MEGACOCK DEEP!!!!"
scene frostanalcum04:
    subpixel True
    zoom 1
    ease 8 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan02.mp3"
ef "I'm so full... so fulll... Uuuuh..."
window hide
with vpunch
mc "Oooh god, cumming so MUCH!!!!"
scene frostanalcum05 with dissolve
mc "Hold on, I've got a few more MONSTERSHOTS TO UNLOAD! GGGUUUU!!!!"
window hide
with fastflash
ef "I can't...take it anymore... Please stop pummeling my poor ass!"
window hide
with fastflash
mc "Just a few more... There..."
stop channel1
stop channel2
scene frostanalcum06:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1        
with dissolve
play sound "sounds/moan02.mp3"
ef "Uuh... there's so much cum pouring out of my gaping ass..."
mc "Yeah, I ain't doing a rimjob anymore, that's for sure..."
stop sound
stop music
if hulkescaped and hulkescapedfrost == False:
    menu:
        "Stay with her and help She-Hulk escape (+1 Hero)":
            jump HulkEscape
        "Go back home":
            pass
ef "Now go back to your compound, I need to get cleaned up. STUD LANDBOY."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label HulkEscape:
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
scene hulkpreescape01 with fade
pause
scene hulkpreescape02 with dissolve
mc "I was only half-sleeping. And she's still fast asleep. Time to find She-Hulk and make her leave this dreadful place!"
scene hulkescape01 with fade
mc "Are there she is. How I am going to get her out of her mental cage?"
if mcmind >= 1:
    mc "I know, I'll use my Super-Mind Control abilities to lure her out!"
if mcmind == 0:
    mc "Without any Mind Control Super-Powers, it's hopeless. I should go home and loo for a way of acquiring Mind Control..."
    jump Main
    
label HulkEscapeConcentrate:
scene hulkescape02 with dissolve
mc "Need to concentrate..."
call screen usepower("usemind", "HulkNoEscapeMind", "HulkEscapeMind") with dissolve

label HulkNoEscapeMind:
scene hulkescape03 with dissolve
mc "Ah, it didn't work. The player ain't playing along. Never mind, I can do this all day, let's start again!"
jump HulkEscapeConcentrate

label HulkEscapeMind:
$ usedmind += 1
scene hulkescape04 with dissolve
mc "She seems to be responding a bit. Come closer... Touch the screen, see what's on the other side..."
scene hulkescape05 with dissolve
mc "Curiosity got the best of her, But now she seems confused..."
scene hulkescape06 with dissolve
play sound "sounds/hulkgrowl.mp3"
mc "...And ANGRY! Shit!"
scene hulkescape07 with dissolve
mc "Hey, let me go She-Hulk, it's ME!"
hu "Me horny! I haven't had sex in so long!"
scene hulkescape08 with dissolve
hu "My pussy is leaking... I want COCK! HUGE COCK to fit inside PUSSY!"
scene hulkescape09 with dissolve
mc "Ah, well, why didn't you say so? I have just what you need, but you have to stop choking me and let me down..."
mc "I even brought you a pair of pajama shorts so we could escape without being noticed. Too much."
scene hulkescape10 with dissolve
mc "The coast is clear, let's get outta here and back to the compound! For some SWEE-EE-EET SEX!"
$ hulkescapedfrost = True
if hulkfrostescapehero == False:
    $ hulkfrostescapehero = True
    call Good from _call_Good_4
$ period += 1
scene hulkjacuzzi01 with dissolve
mc "There you go, I think you might need to take a nice relaxing jacuzzi bath and freshen up a bit..."
hu "But ME HORNY!"
mc "Yeah, I got that... Let me get inside the jacuzzi and show you where we'll be DOING IT!"
jump HulkJacuzziSex02

label HulkJacuzziSex:
scene hulkjacuzzi01 with dissolve
hu "You want me to get cleaned? So you can FUCK ME again?"
mc "That's the idea. Keep you sexually satisfied. And keeping myself sexually satisfied in the process."    

label HulkJacuzziSex02:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy10.mp3"
scene hulkjacuzzi02 with dissolve
mc "The water is warm and I'm getting hotter by the minute..."
scene hulkjacuzzi03 with dissolve
hu "BIG COCK... NEED TO SEE IT!"
mc "Well come and get it then, She-Hulk..."
scene hulkjacuzzi04 with dissolve
hu "Me can't wait."
play sound "sounds/ripping.mp3"
mc "Yet another speedo to the garbage chute..."
scene hulkjacuzzi05 with dissolve
play sound "sounds/wow.mp3"
if hulkjacuzzifucked == False:
    hu "It's even BIGGER than I remember it!"
    mc "Yep, grew bigger in the meantime. Superhero Level TWO now! And Cock Size level two TOO!"
if hulkjacuzzifucked:
    hu "So, so BIG!"
    mc "That's right, Superhero Level TWO and Cock Size level two TOO!"
scene hulkjacuzzi06 with dissolve
play sound "sounds/lick01.ogg"
mc "Fuck yeah..."
scene hulkjacuzzi07 with dissolve
hu "ME gonna make you blow your NUT with my MOUTH in no time!"
mc "Oh, be my gu..."
stop channel1
play channel1 "sounds/blow02.mp3"

label HulkJacuzziBlowSlow:
$ hulkjacuzziblowfast = False
$ hulkjacuzziblowharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide nexticon
if hulkjacuzziblowslow == False and hulkjacuzzistart:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslow = True
window hide
show hulkjacuzziblowslowvideo behind hulkjacuzziblowfastvideo
show hulkjacuzziblowslowvideo behind hulkjacuzziblowslowpovvideo
show hulkjacuzziblowslowvideo behind hulkjacuzziblowharderslowvideo
pause 1.0
hide hulkjacuzziblowfastvideo
hide hulkjacuzziblowslowpovvideo
hide hulkjacuzziblowharderslowvideo
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if hulkjacuzziblowslow == False and hulkjacuzzistart == False:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslow = True
    $ hulkjacuzzistart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowslow()
screen hulkjacuzziblowslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVSlow")

label HulkJacuzziBlowFast:
$ hulkjacuzziblowslow = False
$ hulkjacuzziblowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzziblowfast == False:
    mc "Go on, get that cock nice and wet..."
    $ hulkjacuzziblowfast = True
show hulkjacuzziblowfastvideo behind hulkjacuzziblowslowvideo
show hulkjacuzziblowfastvideo behind hulkjacuzziblowfastpovvideo
show hulkjacuzziblowfastvideo behind hulkjacuzziblowharderfastvideo
pause 1.0
hide hulkjacuzziblowslowvideo
hide hulkjacuzziblowfastpovvideo
hide hulkjacuzziblowharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzziblowfast()
screen hulkjacuzziblowfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVFast")

label HulkJacuzziBlowPOVSlow:
$ hulkjacuzziblowfast = False
$ hulkjacuzziblowharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide nexticon
if hulkjacuzziblowslow == False:
    mc "Damn, those strong lips around my knob..."
    $ hulkjacuzziblowslow = True
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowslowvideo
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowfastpovvideo
show hulkjacuzziblowslowpovvideo behind hulkjacuzziblowharderpovslowvideo
pause 1.0
hide hulkjacuzziblowslowvideo
hide hulkjacuzziblowfastpovvideo
hide hulkjacuzziblowharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowslowpov()
screen hulkjacuzziblowslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowSlow")

label HulkJacuzziBlowPOVFast:
$ hulkjacuzziblowslow = False
$ hulkjacuzziblowharder = False
hide nexticon
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzziblowfast == False:
    mc "Go on, get that cock nice and wet..."
    $ hulkjacuzziblowfast = True
window hide
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowslowpovvideo
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowfastvideo
show hulkjacuzziblowfastpovvideo behind hulkjacuzziblowharderpovfastvideo
pause 1.0
hide hulkjacuzziblowslowpovvideo
hide hulkjacuzziblowfastvideo
hide hulkjacuzziblowharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzziblowfastpov()
screen hulkjacuzziblowfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowFast")

label HulkJacuzziBlowHarderSlow:
if hulkjacuzziblowharder == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharder = True        
window hide
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowharderfastvideo
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowharderpovslowvideo
show hulkjacuzziblowharderslowvideo behind hulkjacuzziblowslowvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderfastvideo
hide hulkjacuzziblowharderpovslowvideo
hide hulkjacuzziblowslowvideo
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
call screen hulkjacuzziblowharderslow()
screen hulkjacuzziblowharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCum")

label HulkJacuzziBlowHarderFast:
if hulkjacuzziblowharder == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharder = True        
window hide
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowharderslowvideo
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowharderpovfastvideo
show hulkjacuzziblowharderfastvideo behind hulkjacuzziblowfastvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderslowvideo
hide hulkjacuzziblowharderpovfastvideo
hide hulkjacuzziblowfastvideo
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
call screen hulkjacuzziblowharderfast()
screen hulkjacuzziblowharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCum")

label HulkJacuzziBlowHarderPOVSlow:
if hulkjacuzziblowharder == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharder = True        
window hide
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowharderslowvideo
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowharderpovfastvideo
show hulkjacuzziblowharderpovslowvideo behind hulkjacuzziblowslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderslowvideo
hide hulkjacuzziblowharderpovfastvideo
hide hulkjacuzziblowslowpovvideo
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
call screen hulkjacuzziblowharderpovslow()
screen hulkjacuzziblowharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCum")

label HulkJacuzziBlowHarderPOVFast:
if hulkjacuzziblowharder == False:
    mc "Can you... Get it DEEPER in your mouth please, She-Hulk?"
    hu "Mmmmggg. Y....Yes..."
    $ hulkjacuzziblowharder = True        
window hide
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowharderpovslowvideo
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowharderfastvideo
show hulkjacuzziblowharderpovfastvideo behind hulkjacuzziblowfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/blow01.mp3"
hide hulkjacuzziblowharderpovslowvideo
hide hulkjacuzziblowharderfastvideo
hide hulkjacuzziblowfastpovvideo
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
call screen hulkjacuzziblowharderpovfast()
screen hulkjacuzziblowharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziBlowHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziBlowCum")

label HulkJacuzziBlowCum:
hide faster
hide slower
hide pov
hide sceneicon
hide nexticon
mc "Oh, it's sso good, I..."
scene hulkjacuzzi08 with dissolve
stop channel1
play sound "sounds/lick01.ogg"
hu "I don't want you to cum just yet!"
window hide
with hpunch
mc "Oh God, but..."
scene hulkjacuzzi09 with dissolve
play sound "sounds/slurp.mp3"
mc "Aaaah... I'm leaking pre-cum like crazy..."
hu "Then it's time for you to FUCK ME!"
scene hulkjacuzzi10 with dissolve
mc "You don't need to ask me twice! I'm gonna POUND you missionary-style, cos that is my MISSION!"
scene hulkjacuzzi11 with dissolve
play sound "sounds/wow.mp3"
if hulkjacuzzifucked == False:
    hu "I've never been manhadled before! I usually just crush anyone that gets near me..."
    mc "There's a first for everything, even for She-Hulk! Now turn around, I want to play with that sweet pussy a bit!"
if hulkjacuzzifucked:
    hu "You're MAN-handling me again! This is making me feel so HORNY!"
    mc "Then we're BOTH horny as hell! Now turn around, I want to play with that sweet pussy a bit!"
scene hulkjacuzzi12 with dissolve
play sound "sounds/moan02.mp3"
hu "Oooh! Your fingers..."
if age >= 20:
    mc "Yeah, get nice and wet for me... I can't wait to plunge my giant shaft inside that nice DEEP pussy of yours!"
if age >= 18 and age <=19:
    mc "Yeah, get nice and wet for me...I can't wait to plunge my giant teen shaft inside that nice DEEP pussy of yours!"
scene hulkjacuzzi13 with dissolve
mc "Enough foreplay, time for the MAIN PLAY!"
hu "Huuu! Fuck me please!"
scene hulkjacuzzi14 with dissolve
mc "That's what I'm about to do!"
hu "Your cock is so BIG! Even for me..."
play channel1 "sounds/womansex05.mp3"

label HulkJacuzziFuckSlow:
$ hulkjacuzzifuckfast = False
$ hulkjacuzzifuckharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if hulkjacuzzifuckslow == False and hulkjacuzzifuckstart:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslow = True
window hide
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckfastvideo
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckslowpovvideo
show hulkjacuzzifuckslowvideo behind hulkjacuzzifuckharderslowvideo
pause 1.0
hide hulkjacuzzifuckfastvideo
hide hulkjacuzzifuckslowpovvideo
hide hulkjacuzzifuckharderslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if hulkjacuzzifuckslow == False and hulkjacuzzifuckstart == False:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslow = True
    $ hulkjacuzzifuckstart = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckslow()
screen hulkjacuzzifuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVSlow")

label HulkJacuzziFuckFast:
$ hulkjacuzzifuckharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzzifuckfast == False:
    hu "Just like that, but faster please!"
    $ hulkjacuzzifuckfast = True
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckslowvideo
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckfastpovvideo
show hulkjacuzzifuckfastvideo behind hulkjacuzzifuckharderfastvideo
pause 1.0
hide hulkjacuzzifuckslowvideo
hide hulkjacuzzifuckfastpovvideo
hide hulkjacuzzifuckharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckfast()
screen hulkjacuzzifuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVFast")

label HulkJacuzziFuckPOVSlow:
$ hulkjacuzzifuckharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if hulkjacuzzifuckslow == False:
    mc "Oh fuck, this feels so GOOD!"
    hu "AAAH! It feels AMAZING to me!"
    $ hulkjacuzzifuckslow = True
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckslowvideo
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckfastpovvideo
show hulkjacuzzifuckslowpovvideo behind hulkjacuzzifuckharderpovslowvideo
pause 1.0
hide hulkjacuzzifuckslowvideo
hide hulkjacuzzifuckfastpovvideo
hide hulkjacuzzifuckharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckslowpov()
screen hulkjacuzzifuckslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckSlow")

label HulkJacuzziFuckPOVFast:
$ hulkjacuzzifuckharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if hulkjacuzzifuckfast == False:
    hu "Just like that, but faster please!"
    $ hulkjacuzzifuckfast = True
window hide
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckslowpovvideo
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckfastvideo
show hulkjacuzzifuckfastpovvideo behind hulkjacuzzifuckharderpovfastvideo
pause 1.0
hide hulkjacuzzifuckslowpovvideo
hide hulkjacuzzifuckfastvideo
hide hulkjacuzzifuckharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen hulkjacuzzifuckfastpov()
screen hulkjacuzzifuckfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckFast")

label HulkJacuzziFuckHarderSlow:
if hulkjacuzzifuckharder == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharder = True        
window hide
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckharderfastvideo
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckharderpovslowvideo
show hulkjacuzzifuckharderslowvideo behind hulkjacuzzifuckslowvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderfastvideo
hide hulkjacuzzifuckharderpovslowvideo
hide hulkjacuzzifuckslowvideo
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
call screen hulkjacuzzifuckharderslow()
screen hulkjacuzzifuckharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCum")

label HulkJacuzziFuckHarderFast:
if hulkjacuzzifuckharder == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharder = True        
window hide
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckharderslowvideo
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckharderpovfastvideo
show hulkjacuzzifuckharderfastvideo behind hulkjacuzzifuckfastvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderslowvideo
hide hulkjacuzzifuckharderpovfastvideo
hide hulkjacuzzifuckfastvideo
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
call screen hulkjacuzzifuckharderfast()
screen hulkjacuzzifuckharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCum")

label HulkJacuzziFuckHarderPOVSlow:
if hulkjacuzzifuckharder == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharder = True        
window hide
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckharderslowvideo
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckharderpovfastvideo
show hulkjacuzzifuckharderpovslowvideo behind hulkjacuzzifuckslowpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderslowvideo
hide hulkjacuzzifuckharderpovfastvideo
hide hulkjacuzzifuckslowpovvideo
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
call screen hulkjacuzzifuckharderpovslow()
screen hulkjacuzzifuckharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCum")

label HulkJacuzziFuckHarderPOVFast:
if hulkjacuzzifuckharder == False:
    mc "Now I'm gonna POUND YOU DEEPER!"
    if age >= 20:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-INCHES!"
    if age >= 18 and age <= 19:
        hu "YES! DO IT! Give me all you've got, all EIGHTEEN MEGA-TEENAGE INCHES!"
    $ hulkjacuzzifuckharder = True        
window hide
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckharderpovslowvideo
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckharderfastvideo
show hulkjacuzzifuckharderpovfastvideo behind hulkjacuzzifuckfastpovvideo
pause 1.0
stop channel1
play channel1 "v031/womansex08.mp3"
hide hulkjacuzzifuckharderpovslowvideo
hide hulkjacuzzifuckharderfastvideo
hide hulkjacuzzifuckfastpovvideo
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
call screen hulkjacuzzifuckharderpovfast()
screen hulkjacuzzifuckharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("HulkJacuzziFuckHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("HulkJacuzziFuckCum")

label HulkJacuzziFuckCum:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
mc "I don't think I can last much longer without..."
stop channel1
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge02.mp3"
scene hulkjacuzzicum01 with dissolve
mc "...BLOWING MY NUT! AAAH!"
window hide
with hpunch
hu "Do it, me want your cum, LOTS of it!"
scene hulkjacuzzicum02 with dissolve
mc "Here it comes! RHAAA!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
hu "I'm feeling it! Feeling every MONSTER SHOT OF YOUR CREAM!!!"
scene hulkjacuzzicum03 with dissolve
mc "Well, get ready for MORE!!!"
window hide
with vpunch
play sound "sounds/moan06.ogg"
hu "ME WANT MORE! MUCH MORE!"
scene hulkjacuzzicum04 with dissolve
play sound "sounds/moan03.mp3"
mc "I'm delivering my baby-making ball-batter directly into your womb!"
window hide
with fastflash
if hulkjacuzzifucked == False:
    hu "You want me to get PREGNANT? AAAH!"
if hulkjacuzzifucked:
    hu "MY EGGS ARE GETTING DROWNED IN YOUR SPERMS!"
scene hulkjacuzzicum05 with dissolve
mc "Damn right, you're in MY HAREM now She-Hulk! AAAH!"
window hide
with hpunch
hu "AAAAH! YOU SO DEEEEEPPP! TOO MUCH CUM!"
window hide
with fastflash
mc "I should probably pull out, I think you've got enough of my spunk to make one hundred babies..."
scene hulkjacuzzicum06 with dissolve
stop channel2
mc "So I can give you the rest of my load, AAAH!"
window hide
with fastflash
hu "STILL SO MUCH? SUCH A STUD FOR ME!!!"
scene hulkjacuzzicum07 with dissolve
if hulkjacuzzifucked == False:
    mc "Damn right, your STUDMASTER NOW, RHAAA!"
if hulkjacuzzifucked:
    mc "For you, your STUDMASTER always comes that much!"
window hide
with fastflash
if hulkjacuzzifucked == False:
    hu "YES, ME WANT TO BE YOUR HAREM SEX SLAVE!"
if hulkjacuzzifucked:
    hu "That's why ME LOVES BEING YOUR HAREM SLAVE!"
scene hulkjacuzzicum08 with dissolve
stop channel1
if hulkjacuzzifucked == False:
    mc "It shall be done!"
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlhulk at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ hulkharem = True
    mc "A great addition to MY harem!"
    hu "Me agree!"
    $ hulkjacuzzifucked = True
stop music
play sound "sounds/panting.mp3"
mc "Phew! That was a MEGA-ORGASM FROM YOURS TRULY..."
if age >= 20:
    hu "You such a STALLION!"
if age >= 18 and age <= 19:
    hu "You such a TEENAGE STALLION!"
"She-Hulk will now be available for repeat sex on the compound roster with Lara's room icon during the day."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main