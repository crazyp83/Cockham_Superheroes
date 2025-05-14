label CockhamPlanet:
scene cockhamplanet01 with fade
show loiseyeblink with dissolve
if lpspeak01 == False:
    lp "[hero]! I'm so glad to see you here at the Cockham Planet offices."
if lpspeak01:
    lp "[hero]! What can I do for you? Clark isn't around fortunately..."
if mclevel02 and seendanishoot == False:
    lp "[hero]! I'm so glad to see you here at the Cockham Planet offices."
    mc "Why is that? Another photoshoot with ME?"
    hide loiseyeblink
    show lois02 at centerleft
    with fastdissolve
    lp "No, not WITH you. But WITH your help. As a REAL man. Which I find hard to find in this office."
    mc "Alright, what's this about?"
    hide lois02
    show lois04
    with fastdissolve
    lp "I am shooting for Hustler's \"Sexy Cop\" centerfold. And Sergeant Dani offered to be this year's vixen."
    mc "Great! So, what do I get to do? FUCK HER in front of the camera, is that it?"
    hide lois04
    show lois05
    with fastdissolve
    lp "Not at all. It's a solo shoot. You get to watch and let us know if it's titillating enough to MEN. And boys in your case. Please follow me..."
    jump DaniPhotoshoot
if seendanishoot and seensupermanshoot == False:
    lp "[hero]! I'm so glad to see you here at the Cockham Planet offices. Superman has just arrived."
    mc "Err, so I should leave then?"
    hide loiseyeblink
    show lois02 at centerleft
    with fastdissolve
    lp "Not at all. I'm shooting a new edition of our superheroes calendar, and it's called \"Working together to save Cockham\". So it requires TWO souperheroes."
    mc "I see. It's just that he's kind of angry at me all the time."
    hide lois02
    show lois03
    with fastdissolve
    lp "I will make sure to calm him down with my soothing voice, don't worry."
    menu:
        "Fine, I'll do it.":
            hide lois03
            show lois05 at centerleft
            with fastdissolve
            lp "Great! I have a SPECIAL costume for you too... Follow me."
            jump SupermanPhotoshoot
        "I don't like this. I'll give it a pass.":
            hide lois03
            show lois01 at centerleft
            with fastdissolve
            lp "Umpf... How disappointing of you..."
            jump Main

label LoisPlanetDialogues:
menu:
    "Why, what's going on?" if lpspeak01 == False:
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        $ lpspeak01 = True
        lp "Well, you're here for the photoshoot session I booked for you, right?"
        mc "Oh yeah, that thing. Ok, let's do it."
        hide lois02
        show lois05 at centerleft
        with fastdissolve
        lp "Follow me to our photo studio, everything has been set up."
        jump LoisPhotoshoot01
    "I was in the area, so I thought I'd drop by." if lpspeak01 and lpspeak02 == False:
        $ lpspeak02 = True
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "Drop by for what? * wink *"
        mc "Well, you *KNOW*."
        hide lois02
        show lois04
        with fastdissolve
        lp "Then maybe I should give you my *PRIVATE* address. But there are too many people around here and reporters like eavesdropping on conversations."
        if mcsenses >= 1: 
            mc "Alright, you can just whisper it and I'll use my Super-Hearing to hear you!"
            hide lois04
            show lois03 at centerleft
            with fastdissolve
            lp "What a SUPERHERO you are!"
        if mcsenses == 0: 
            mc "Alright, I'll lean closer and you just whisper it in my ear."
            hide lois04
            show lois03 at centerleft
            with fastdissolve
        lp "So it's..."
        window hide
        play sound "sounds/skill.mp3"
        show locationlois at poslocation
        $ renpy.pause(0.5, hard=True)
        $ loclois = True
        lp "Maybe you can visit me in the evenings when I'm around. Which I won't be in this version of the game by the way."
        mc "Ah. I see. I'll have to wait then."
        hide lois03
        show lois05 at centerleft
        with fastdissolve
        lp "And you'd better leave now. People are already looking at us in a weird way..."
        jump Main
    "What's the latest news on Harley Quiff?" if lpspeakhq01 == False:
        $ lpspeakhq01 = True
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "The last article I wrote about her was when Dr. Weakheart was found dead in his bed. In a puddle of her own cuntjuices."
        mc "Interesting. Where did he live exactly?"
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "In the borough of Porkher Row."
        mc "Interesting..."
        hide lois03
        show lois05 at centerleft
        with fastdissolve
        lp "Now if you'll excuse me, I'm rather busy. We're onto some BIG story. Come back anytime though, [hero]!"
        jump Main
    "What's the latest news on the Joker?" if lpspeakjo01 == False:
        $ lpspeakjo01 = True
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "His last crime spree involved a couple of bank robberies in the Diamond District. Since then, he has disappeared from the radars."
        mc "Probably sipping cocktails on the beach in the Bahamas."
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "When he's out of money, he'll come back to Cockham. And go on a CRIMINAL SPREE."
        hide lois03
        show lois05 at centerleft
        with fastdissolve
        lp "Now if you'll excuse me, I'm rather busy. We're onto some BIG story. Come back anytime though, [hero]!"
        jump Main
    "What's the latest news on Sexy Luthor?" if mission02end and lpspeaksl01 == False:
        $ lpspeaksl01 = True
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "She escaped again. Despite the CCPD acquiring a very expensive new type of cell. Complete waste of taxpayers money. I wrote a lengthy article denouncing it."
        mc "Err... Did you mention me in this article of yours?"
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "No, why? Should I have? I think YOU have something to do with what happened, right?"
        mc "No, no, nothing. I plead the fifth. I have nothing to say to the press! I'm out of here! See you!"        
        jump Main
    "What's the latest news on Colonel Stroheim?" if quest07end == False:
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "I was hoping YOU would give me news on him. After having interrogated his two Valkyries. Which I know from a reliable source are being kept under close guard in the League's Compound..."
        mc "Err, I deny everything! I wasn't there, I didn't do nothing, goodbye!"
        jump Main
    "What's the latest news on Barbara Keen?":
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "She's organizing a MAJOR elite social gathering at her nightclub. I hear she's hiring young waitresses... AND waiters."
        mc "I see. I might have to infiltrate that gatehring then."
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "I certainly will..."
        hide lois03
        show lois05 at centerleft
        with fastdissolve
        lp "Now if you'll excuse me, I'm rather busy. We're onto some BIG story. Come back anytime though, [hero]!"
        jump Main
    "What's the latest news on Emma Frost?" if lpspeakef01 == False:
        $ lpspeakef01 = True
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "You don't know? It's on all the newspapers front pages. Frost International has acquired the whole research division of Vayne Enterprises."
        mc "That means Arkham's asylum too then..."
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "Precisely. You're starting to catch on on all the underdealings going on in this town..."
        hide lois03
        show lois05 at centerleft
        with fastdissolve
        lp "Now if you'll excuse me, I'm rather busy. We're onto some BIG story. Come back anytime though, [hero]!"
        jump Main
    "What's the latest news on Catwoman?" if mission06 and mission06end == False and lpspeakcw01 == False:
        hide loiseyeblink
        show lois02 at centerleft
        with fastdissolve
        lp "There's been a recent spike in jewelry theft in the Diamond district. And I acquired an amateur photograph of Catwoman entering her lair, to which I managed to assign an address."
        mc "Oooh, Can I have it?"
        hide lois02
        show lois03 at centerleft
        with fastdissolve
        lp "A true journalist never reveals his sources."
        mc "And a little cock-slave like you are?..."
        hide lois03
        show lois04 at centerleft
        with fastdissolve
        if loisevil == False:
            lp "I'm NOT your cock slave. Yet. But I'd like to be... * wink *"
            mc "I see. I must first visit you in your flat and turn you into one. Then I'll come back here and ask you again for Catwoman's whereabouts..."
            hide lois04
            show lois05 at centerleft
            with fastdissolve
            lp "You're getting the hang of this game. Now I need to get back to my desk, Clark is watching..."
            jump Main
        $ lpspeakcw01 = True
        lp "Uhm... I suppose I could make an exception in YOUR case. As long as you don't let Clark Kunt know anything about our sexcapades!"
        if seensupermanshoot:
            mc "Of course. How could he possibly know? There is no way he could possibly know you are my little cock-slave. None whatsoever."
            hide lois04
            show lois05 at centerleft
            with fastdissolve
            lp "Here's the address. Try and get her to accept an interview with me if you can... I need to get back to my desk, Clark is watching..."
        if seensupermanshoot == False:
            mc "My lips are sealed. As long as yours are wide open when I pummel my di...."
            hide lois04
            show lois05 at centerleft
            with fastdissolve
            lp "Alright, alright, here's the address. Try and get her to accept an interview with me if you can... I need to get back to my desk, Clark is watching..."
        $ preloccatcave = True
        jump Main
    "Nothing actually. I'm all good.":
        hide loiseyeblink
        show lois04 at centerleft
        with fastdissolve
        lp "So you just came here for no reason at all?"
        mc "I was just being nosey. Can I get a job here?"
        hide lois04
        show lois05 at centerleft
        with fastdissolve
        lp "NO, you can't. Now if you'll excuse me, I'm rather busy. We're onto some BIG story. But come back anytime though, [hero]!"
        jump Main
    
label LoisPhotoshoot01:
scene photopreshoot01 with fade
lp "This is our photo studio. Used mainly for shooting superheroes like yourself for our Special Superheroes Calendar Edition..."
mc "Which edition will I be featuring in?"
scene photopreshoot02 with dissolve
lp "Well, in your case, the \"Superheroes studmuffins Limited Edition\"..."
mc "I see... Mainly aimed at a female audience I gather?"
lp "That's right, half of our readership are women. So just act natural and don't be shy, our readers want some nice sexy but not too raunchy pics, you understand?"
mc "I get it. Where should I go to pose?"
scene photoshoot01 with dissolve
lp "Just over there on the stage in front of the white screen. I'll add a superhero-themed background later in post-editing."
scene photoshoot02 with dissolve
mc "Like here? Am I in the frame?"
lp "Don't worry, I'll move around to take pics from different angles."
scene photoshoot03 with dissolve
lp "Smile for your female fans, [hero]!"
play sound "sounds/flash.mp3"
scene photoshoot03 with fastflash
if age >= 20:
    lp "Perfect! Now flex those huge muscles for me..."
if age >= 18 and age <= 19:
    lp "Perfect! Now flex those huge teenage muscles for me..."
scene photoshoot04 with dissolve
mc "Like that?"
play sound "sounds/flash.mp3"
scene photoshoot04 with fastflash
lp "Damn boy, you are RIPPED! Now flex those biceps..."
scene photoshoot05 with dissolve
lp "These are the biggest boulders I ever shot..."
play sound "sounds/flash.mp3"
scene photoshoot05 with fastflash
lp "They seem to be rippling with POWER... Next, do a superhero pose with your fist up in the air."
scene photoshoot06 with dissolve
lp "Like you've just defeated the worst super-villain in Cockham City."
play sound "sounds/flash.mp3"
scene photoshoot06 with fastflash
lp "Keep that pose a bit longer..."
scene photoshoot07 with dissolve
lp "Nice..."
play sound "sounds/flash.mp3"
scene photoshoot07 with fastflash
lp "Just a few more pics..."
scene photoshoot08 with dissolve
mc "Your camera seems to be aimed rather... below the belt, Ms Pane."
scene photoshoot09 with dissolve
lp "What? Oh, I'm sorry, I was just..."
scene photoshoot10 with dissolve
mc "...Taking pictures of my dangling boyhood?"
lp "Well, I mean, it's just sssooo BIG!"
scene photoshoot11 with dissolve
mc "Well, let me help you if you're interested in a VERY \Special Edition\"..."
lp "What are you doing [hero]? I..."
scene photoshoot12 with dissolve
if age >= 20:
    lp "Oh My God, that's the biggest monster love muscle I've ever seen!"
if age >= 18 and age <= 19:
    lp "Oh My God, that's the biggest monster teenage love muscle I've ever seen!"
mc "Go ahead and take pictures of it..."
scene photoshoot13 with dissolve
lp "Okay, but just for my *personal* collection..."
play sound "sounds/flash.mp3"
scene photoshoot13 with fastflash
lp "It seems to be GROWING [hero]! I'm not sure if I should... Can I... touch it?"
mc "Sure, you need to FEEL its power to get a REAL-LIFE viewpoint for your article, right?"
lp "Yes, that's exactly why I'm doing this... [hero]."
scene photoshoot14 with dissolve
lp "It's so HEAVY... It weighs like several pounds of flesh."
mc "And it's not even half-hard Ms Pane..."
lp "I can feel it growing some more... It's so BEAUTIFUL up close..."
scene photoshoot15 with dissolve
play sound "sounds/lick01.ogg"
lp "I just wanna lick it..."
scene photoshoot16 with dissolve
play sound "sounds/slurp.mp3"
lp "And suck out the abundant precum flowing from its tip..."
scene photoshoot17 with dissolve
lp "And kiss it and worship it..."
play sound "sounds/kiss.mp3"
scene photoshoot18 with dissolve
play sound "sounds/lick02.mp3"
lp "And suck your tasty balls and make them churn an extra-big load for me..."
scene photoshoot19 with dissolve
stop sound
lp "You're going to do that for me [hero]? Deliver the BIGGEST superhero load of cum ever?"
scene photoshoot20 with dissolve
lp "And cover my titties in an inch-thick layer of it? Pleasure yourself for me please!"
scene photoshoot21 with dissolve
mc "Oh fuck, yeah, I'll do it Lois! I'm so fucking hard for you right now!"
scene photoshoot22 with dissolve
lp "I can see that, your cock is just... ENORMOUS! And your balls look so.. FULL!"
play channel2 "sounds/wank.mp3"
scene photoshoot23 with dissolve
lp "I'm gonna take MANY picture of you jerking off your mammoth love sword!"
play sound "sounds/flash.mp3"
scene photoshoot23 with fastflash
lp "Go on, show me how you pleasure such a huge piece of boymeat!"
window hide
show photowankslow
with dissolve
pause
if age >= 20:
    lp "Yeah, jerk that fat superhero dong!"
if age >= 18 or age <= 19:
    lp "Yeah, jerk that fat teenage superhero dong!"
window hide
pause
hide photowankslow
show photowankfast
lp "God, I can't stop watching you pump that fat shaft... It's so... arousing!"
if age >= 20:
    mc "That's right, just watch me bring this fat fifteen-incher to a mighty eruption of cum!"
if age == 18 or age == 19:
    mc "That's right, just watch me bring this fat teenage fifteen-incher to a mighty eruption of cum!"
stop channel2
scene photoshootcum01 with dissolve
play sound "sounds/boymoan.mp3"
mc "AAAH!"
lp "Oh my God, that plume of spunk is GIGANTIC!"
scene photoshootcum02 with dissolve
play sound "sounds/splooge01.mp3"
lp "You're COVERING me in your warm seed... I LOVE IT, MORE, MORE!"
window hide
with fastflash
mc "Hang on, there's MORE, AAAH!"
scene photoshootcum03 with dissolve
lp "Still MORE cum for me? You are a true SUPERHERO CUM MACHINE!"
window hide
with fastflash
mc "Damn, can't stop CU-UU-MING!"
scene photoshootcum04 with dissolve
play sound "sounds/panting.mp3"
lp "I've never been so completely DRENCHED in anything, let alone a boy's red-hot seed... mmmh..."
mc "Come and suck out the afterdregs..."
scene photoshootcum05 with dissolve
play sound "sounds/slurp.mp3"
lp "Yes sir, it's sssoo tasty... Yummy!"
play sound "sounds/scratch.mp3"
scene photoshootcum06 with dissolve
lp "Shit, Clark? What are you doing here?"
mc "Err, Supe... I mean, wassup, Kunt?"
scene photoshootcum07 with dissolve
cl "How could you do this to me Lois?"
scene photoshootcum08 with dissolve
lp "I'm sorry Clark but [hero]'s cock was just... so enticing. And HE'S the one who showed it to me!"
menu:
    "Hey! YOU'RE the one who was taking shots of it! (no change)":
        scene photoshootcum09 with dissolve
        lp "I... I admit it. But I WAS WRONG!"
        lp "Please forgive me Clark. We could... go on a date tomorrow night?"
        scene photoshootcum12 with dissolve
        cl "I... forgive you. I'll try and pretend this never happened. *sigh*"
        scene photoshootcum13 with dissolve
        mc "Right, well, my photoshoot job is done here so... I 'll leave you two lovebirds to it then..."
        cl "You'd better not cross my path again. Alone."
        jump Main        
    "Well, she ain't getting any dick from you right? So it's YOUR fault really, Clark. (+1 Super-Villain)":
        $ choseevilphoto = True
        call Evil from _call_Evil_5
        pause
        lp "Yeah, I mean, you know how long I've been waiting Clark? MONTHS if not YEARS! And we've never even been to third base... *sigh*"
        scene photoshootcum12 with dissolve
        cl "It's because... I LOVE YOU and I RESPECT YOU TOO MUCH!"
        mc "OR... you have a tiny one and you're ashamed of it. Which one do you think it is, Ms Pane?"
        scene photoshootcum09 with dissolve
        lp "Just... get out of here please, you're making the situation WORSE!"
        cl "Hang on a minute. Could I please have a word with you in private first, [hero]?"
        scene photoshootcum13 with dissolve
        mc "Err, not really, I'm in a hurry and..."
        lp "I'll get cleaned up and leave you two to sort out your differences."
        mc "Wait! Err, he's like... real angry I think."
        lp "You're a superhero. Deal with it."
        scene photoshootcum10 with dissolve
        cl "You know, normally I am a composed superhero and I would never hurt a fellow companion of the Cockham League of Justice..."
        mc "Oh well, everything's fine then, let's just leave it at th..."
        cl "BUT, I'll make an exception in THIS CASE."
        scene photoshootcum11 with dissolve
        play sound "sounds/punch.mp3"
        scene photoshootcum11 with hpunch  
        cl "Now you know how it feels to receive a punch from a Level 3 Super-Strength superhero!"
        if mcresistance >= 1:
            call screen usepower("useresistance", "PhotoNoResistance", "PhotoResistance") with dissolve
        label PhotoNoResistance:
        scene photoshootcum12 with dissolve
        mc "Fuck it hurts... Even though I'm a superhero."
        cl "Now go back to the compound and ponder on what you've done!"
        jump Main        
        label PhotoResistance:
        scene photoshootcum12 with dissolve
        mc "Fuck it hurts... Even though I used my Super-Resistance."
        cl "You didn't read the description of that Level ONE superpower apparently. It provides resistance to HEAT and COLD. NOT to MY punches!"
        cl "Now go back to the compound and ponder on what you've done!"
        jump Main        
        
label DaniPhotoshoot:
$ seendanishoot = True
scene danipreshoot01 with fade
lp "Since you work in liaison with the CCPD, you two must have met before, right?"
mc "Err, vaguely, I might have seen her around at one stage but..."
scene danipreshoot02 with dissolve
if mission02win:
    da "We did a MISSION together. Which ended in almost complete success thanks to my quick thinking."
if mission02fail:
    da "We did a MISSION together. Which ended in complete disaster."
lp "Really? You'll have to tell me MORE about this mission of yours. After the photoshoot."
scene danipreshoot03 with dissolve
lp "So let's get started, Sergeant Dani, just be natural, I'll take the photos and make sure I take them from the BEST angles... And take the props I prepared for you."
play music "sounds/sexy13.mp3"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene danishoot01 with dissolve
da "Like this?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Perfect! Keep going."
scene danishoot02 with dissolve
lp "Turn around and keep holding your baton."
window hide
with fastflash
play sound "sounds/flash.mp3"
mc "This is getting steamy..."
scene danishoot03 with dissolve
lp "That's it, look like you're about to arrest a dangerous criminal."
scene danishoot04:
    xpos 0.0 ypos 0.0
    ease 6.0 ypos -1.3 xpos 0.0
with dissolve
$ renpy.pause(2.0, hard='True')
pause
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "You might as well take your skirt off."
scene danishoot05 with dissolve
mc "Damn, I'd like to get arrested RIGHT NOW!"
scene danishoot06 with dissolve
lp "Can you lift up your blouse? This calendar is for the Hustler Supplement of our weekend edition, the readers want to see some FLESH."
scene danishoot07 with dissolve
mc "Mamma Mia!"
window hide
with fastflash
play sound "sounds/flash.mp3"
da "I have an idea of what to do with my baton."
scene danishoot08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
lp "I like your improvisation style Sergeant Dani!"
scene danishoot09 with dissolve
mc "So do I..."
scene danishoot10 with dissolve
da "This is making me quite horny actually..."
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Then take off your panties and play with your pussy, Sergeant Dani."
scene danishoot11 with dissolve
lp "That's perfect, nicely trimmed and very APPETIZING!"
scene danishoot12 with dissolve
play sound "sounds/moan02.mp3"
da "Uh..."
scene danishoot13 with dissolve
mc "Can I make a suggestion? Stick your fing..."
scene danishoot14 with dissolve
play sound "sounds/moan05.mp3"
window hide
with fastflash
play sound "sounds/flash.mp3"
mc "Ah, okay, you didn't need my suggestion."
scene danishoot13 with fastdissolve
play sound "sounds/moan03.mp3"
$ renpy.pause(0.5, hard='True')
scene danishoot14 with fastdissolve
play sound "sounds/moan05.mp3"
$ renpy.pause(0.5, hard='True')
da "Aaaah..."
scene danishoot15 with dissolve
stop sound
da "I almost came..."
scene danishoot16 with dissolve
da "Maybe with the help of my baton..."
scene danishoot17 with dissolve
mc "Or MY baton perhaps?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "Please [hero], this is meant to be a solo shoot only."
scene danishoot18 with dissolve
play sound "sounds/moan04.ogg"
da "Mmmh... Oooh..."
show daniwankslowvideo with dissolve
play channel1 "sounds/moan02.mp3"
show faster:
    xpos 1700 ypos 500    
call screen daniwankslow()
screen daniwankslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniWankFast")

label DaniWankFast:
hide faster
show daniwankfastvideo behind daniwankslowvideo
lp "Frig yourself off, I want to see some pussy juices squirting eveywhere!"
$ renpy.pause(2.0, hard='True')
hide daniwankslowvideo
with fastdissolve
show nexticon:
    xpos 1750 ypos 1020    
call screen daniwankfast()
screen daniwankfast():
    modal True
    button:
        xpos 1750
        ypos 1020
        xysize(180, 60)        
        action Jump ("DaniWankEnd")

label DaniWankEnd:
hide nexticon
scene danishoot20 with dissolve
stop channel1
play sound "sounds/womancum02.mp3"
da "AHHH, I'm coming!!!"
scene danishoot21 with dissolve
play sound "sounds/moan06.ogg"
mc "Damn, she's squirting big time!"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "That's the centerfold pic right there!"
scene danishoot22 with dissolve
play sound "sounds/moan04.ogg"
mc "Do I get a free copy of that issue?"
window hide
with fastflash
play sound "sounds/flash.mp3"
lp "No, you'll have to pay for it, like everyone else."         
scene danishoot23 with dissolve
mc "That's not fair, I don't have any money."
play sound "sounds/lick01.ogg"
lp "That's a wrap, thank you Sergeant Dani."                           
stop music
scene danipostshoot01 with dissolve
stop sound
lp "Well, I need to interrogate, I mean interview Sergeant Dani now about this \"mission\" you did together, so if you'll excuse us..."
mc "What? I get to leave?"
scene danipostshoot02 with dissolve
lp "Yes, we wouldn't want Clark Kunt barging in on us right now, would we?"
mc "Err, yeah, I get your point..."
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label SupermanPhotoshoot:
$ seensupermanshoot = True
scene supermanshoot00 with fade
lp "[hero], why don't you go and pick the costume I left for you in the backroom and put it on?"
mc "Will do, Ms Pane. I hope it has an XXL large pouch at the front."
lp "Oh, I made SURE of that! * wink *"
scene supermanshoot01 with dissolve
lp "While [hero] is changing, let's start off this photoshoot with you, Superman!"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "Smile!"
scene supermanshoot02 with dissolve
lp "Now pretend you're about to LIFT OFF!"
window hide
play sound "sounds/flash.mp3"
with fastflash
sm "I have a cape so I'm a REAL Superhero!"
scene supermanshoot03 with dissolve
lp "I didn't know the cape had anything to do with it."
sm "It's super-important!"
scene supermanshoot04 with dissolve
lp "Ah, I see [hero] is ready, let me do a few pictures with him alone then."
sm "But.."
mc "Come on man, it's MY turn!"
scene supermanshoot05 with dissolve
mc "I'll do a pose like I'm about to BANG on the ground and make my enemies TREMBLE WITH FEAR!"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "Ooh, you're such a STRONG superhero!"
sm "I'm stronger than him. Super-Strength level 3. He's only Level 2."
scene supermanshoot06 with dissolve
mc "How about these SUPER-MUSCLES?"
window hide
play sound "sounds/flash.mp3"
with fastflash
lp "My God, they're so BIG!"
sm "Pff, you don't need ridiculously huge muscles to have Super-Strength!"
scene supermanshoot07 with dissolve
lp "Why don't you join [hero] now, Superman? I'd like to have you BOTH in the same frame..."
sm "Umpf, I don't know if this is a good idea..."
mc "What, are you scared that you'll look PUNY next to me, Superman?"
sm "Absolutely NOT! A TRUE Superhero does not concern himself with such petty considerations. I'll stand next to you and PROVE it!"
scene supermanshoot08 with dissolve
sm "There, see? Nothing scares SUPERMAN!"
lp "Your tiny bulge reminds me of someone. A colleague of mine who otherwise wears glasses and therefore doesn't look like you at all..."
scene supermanshoot08 with dissolve
sm "Is he... someone nice that you like?"
lp "Sure... except for..."
mc "The fact that he doesn't have a dick?"
scene supermanshoot10 with dissolve
lp "I don't even know... I... never saw it."
mc "Probably best, you might be VERY disappointed."
sm "Hey!"
lp "Err, let's get back to the photoshoot shall we? Pose like you are both fighting some Super-Villain TOGETHER!"
scene supermanshoot11 with dissolve
sm "Take that Sexy Luthor!"
window hide
play sound "sounds/flash.mp3"
with fastflash
mc "Oh, she took something from me alright! My MASSIVE cock! That's how I, err..."
scene supermanshoot12 with dissolve
sm "What? You...?"
mc "Well, yeah, I mean, she Super-Seduced me, so I had no choice! But thanks to my Super-Studliness, I wasn't defeated by her super-tight pussy."
scene supermanshoot09 with dissolve
sm "She never Super-Seduced me... * sigh *"
window hide
play sound "sounds/flash.mp3"
with fastflash
mc "Why would she? You can't give it to her good like me."
scene supermanshoot13 with dissolve
lp "She could do... stuff TO him though."
window hide
play sound "sounds/flash.mp3"
with fastflash
sm "What... are you saying?"
scene supermanshoot12 with dissolve
mc "Oh yeah, I hadn't thought of that. She could wear a strap-on dildo and give it to YOU good. You might even enjoy it. Like losing your virginity."
sm "You... You think so?"
scene supermanshoot14 with dissolve
lp "I have a strap-on in my office. Don't ask me why, but I'll go and get it and we can show Superman how great SEX is really like!"
sm "But... I never said yes!"
lp "Oh come on, you clearly NEED some, don't pretend you don't... And I owe you for saving my life during that earthquake last year. Let me show you my appreciation... MY WAY."
sm "I... I suppose we could try... something...."
scene supermanshoot15 with dissolve
mc "Alright, it's a deal then. You take Superman up the ass while I take YOU up the ass!"
sm "What? How dare you treat Lois Pane like a cheap whore like that! And you might hurt her, your cock is just... TOO BIG!"
lp "Don't worry about me, Superman. I... do enjoy being treated like that... I'll be back in a moment, my sexy superheroes!"
scene supermanshoot16 with dissolve
sm "I... didn't know that she... liked that... But why?"
mc "Different women have different sex kinks, buddy. That's just the way the SEX world is. Trust me, I know everything about what women WANT."
mc "You might learn a few things from watching ME perform. Call it sexual education for dickless superheroes."
play music "sounds/sexy09.mp3"
scene supermanshoot17 with dissolve
lp "Here I am. Now you two, off with those tight bodysuits! * wink *"
mc "Ooh yeah! I was getting hard already anyway!"
scene supermanshoot18:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
sm "I... I'm still not sure this is a goo...."
lp "Just get on all fours, Superman! I ORDER YOU!"
sm "Err, right Ms Pane..."
menu:
    "Ooh, that sounds kinda hot! (watch scene)":
        jump SupermanFuckSee
    "I cannot bear watching my childhood hero getting butt-fucked by a dildo and covered in spunk. (skip scene)":
        jump SupermanFuckNoSee

label SupermanFuckSee:        
scene supermanshoot19 with dissolve
mc "Oh man, she's going to totally OWN YOUR ASS!"
sm "Don't say that please!"
mc "And I'm going to totally own HER ass!"
sm "That's even worse..."
scene supermanshoot20 with dissolve
mc "Wow, you look like a Ken doll! If they ever make a Barbie movie, you should be the main actor!"
lp "And I'll be \"Strap-on Barbie\" for you!"
scene supermanshoot21 with dissolve
lp "So, Superman, are you ready to take on my HUGE cock?"
sm "I..."
scene supermanshoot22 with dissolve
lp "Your backdoor looks really enticing, you're making me so HARD for you, Superman!"
mc "Why do you even have an asshole? I thought you never ate."
sm "Err..."
scene supermanshoot23 with dissolve
mc "Slap that dildo on his buttcheeks, Lois!"
lp "You think so? Let's try..."
scene supermanshoot24 with dissolve
play sound "sounds/slap.mp3"
play channel1 "sounds/boymoan02.mp3"
lp "Do you like that, Superman? Me slapping my MASSIVE dildo on your filthy ass?"
sm "I... I think so..."
window hide
play channel2 [ "sounds/slap.mp3", "<silence .7>" ]
scene loisrackdildo
pause
stop music
mc "Superman is clearly into it... If he had a dick, he'd be drooling pre-cum right now!"
scene supermanshoot25 with dissolve
stop channel2
lp "Now let's see how well this dildo fits into that lovely hole..."
sm "Please be careful, I've never..."
window hide
stop channel1
show supershootanim01video
play sound "sounds/boymoan03.mp3"
$ renpy.pause(1.36, hard='True')
scene supermanshoot25b
sm "...AAAH!"
scene supermanshoot26 with dissolve
lp "Enjoying it, Superman?"
sm "I... I do, yes."
scene supermanshoot27 with dissolve
if age >= 20:
    mc "And now it's MY turn to see how well my giant cock fits into YOUR lovely hole, Lois..."
if age >= 18 and age <= 19:
    mc "And now it's MY turn to see how well my giant teenage cock fits into YOUR lovely hole, Lois..."
window hide
show supershootanim02video
$ renpy.pause(1.40, hard='True')
play sound "sounds/moan01.mp3"
scene supermanshoot27b
lp "OOOOH! Let me get used to that GIRTH!"
scene supermanshoot28 with dissolve
mc "No time to waste here, let's FUCK!"

play channel2 "sounds/boymoan02.mp3"

label StrapFuckSlow:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckslowvideo behind strapfuckfastvideo
show strapfuckslowvideo behind strapfuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckfastvideo
hide strapfuckpovslowvideo
with dissolve
play channel1 "v031/womansex07.mp3"
$ strapfuckfast = False
if strapfuckslow == False:
    lp "You're a Barbie boy, in a Barbie world, strap-on plastic, it's fantastic!"
    $ strapfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen strapfuckslow()
screen strapfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("StrapFuckFrontSlow")

label StrapFuckFast:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckfastvideo behind strapfuckslowvideo
show strapfuckfastvideo behind strapfuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckslowvideo
hide strapfuckpovfastvideo
with dissolve
play channel1 "v031/womansex08.mp3"
$ strapfuckslow = False
if strapfuckfast == False:
    mc "Fuck, get ready for a MASSIVE ANAL POUNDING. BOTH OF YOU!"
    $ strapfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show pov:
     xpos 1700 ypos 500     
call screen strapfuckfast()
screen strapfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("StrapFuckFrontFast")

label StrapFuckFrontSlow:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckpovslowvideo behind strapfuckslowvideo
show strapfuckpovslowvideo behind strapfuckpovfastvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckslowvideo
hide strapfuckpovfastvideo
with dissolve
play channel1 "v031/womansex07.mp3"
$ strapfuckfast = False
if strapfuckslow == False:
    lp "You're a Barbie boy, in a Barbie world, strap-on plastic, it's fantastic!"
    $ strapfuckslow = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen strapfuckpovslow()
screen strapfuckpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFrontFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckSlow")

label StrapFuckFrontFast:
window hide
hide cum
hide slower
hide faster
hide pov
hide sceneicon
show strapfuckpovfastvideo behind strapfuckfastvideo
show strapfuckpovfastvideo behind strapfuckpovslowvideo
$ renpy.pause(1.0, hard='True')
hide strapfuckfastvideo
hide strapfuckpovslowvideo
with dissolve
play channel1 "v031/womansex08.mp3"
$ strapfuckslow = False
if strapfuckfast == False:
    mc "Fuck, get ready for a MASSIVE ANAL POUNDING. BOTH OF YOU!"
    $ strapfuckfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
show sceneicon:
     xpos 1700 ypos 500     
call screen strapfuckpovfast()
screen strapfuckpovfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("StrapFuckEnd")
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("StrapFuckFast")

label StrapFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide front
mc "This is so HAWT, it's making want to..."
stop channel1
scene supershootcum01 with dissolve
play channel1 "v031/boyorgasm02.mp3"
mc "...blast! RHAAAA!"
window hide
with fastflash
play sound "v032/womancum03.mp3"
lp "AAAH, I can feel it, right in my guts!"
scene supershootcum02 with dissolve
play sound "v032/womancum04.mp3"
lp "SSSSOOO DEEP!"
window hide
with hpunch
sm "TOO DEEP for me, please Lois, take it out!"
scene supershootcum03 with dissolve
mc "No! Keep it in in his pussy ass, while I pump my load inside yours, AAAH!"
window hide
with fastflash
play sound "sounds/splooge02.mp3"
lp "Yes, MASTER!"
scene supershootcum04 with dissolve
stop channel1
play sound "sounds/boymoan03.mp3"
mc "Take those fat wads, still NU-UUU-TTTIIINNNG!"
window hide
with hpunch
play channel1 "sounds/boyorgasm01.mp3"
if age >= 20:
    lp "Can you see that, Superman? Can you see how much spunk is ERUPTING from this SUPERSTUD'S STALLION COCK?"
if age >= 18 and age <= 19:
    lp "Can you see that, Superman? Can you see how much spunk is ERUPTING from this SUPERSTUD'S TEENAGE STALLION COCK?"
scene supershootcum05 with dissolve
play sound "sounds/moan01.mp3"
lp "Oooh yeah, cover Superman in your hot sauce, make him BEG FOR MORE!"
window hide
with fastflash
mc "Sure Lois, here I CO-O-MMME!"
stop channel2
scene supershootcum06 with dissolve
play sound "sounds/splat.ogg"
sm "This is so humiliating...."
window hide
with fastflash
lp "What are you complaining about? I thought you liked it. I definitely heard you moan a lot."
scene supershootcum07 with dissolve
play sound "sounds/splat.ogg"
sm "I... might have, but..."
window hide
with fastflash
lp "You deserve a good spanking for LYING!"
scene supershootcum08 with dissolve
play sound "sounds/slap.mp3"
lp "Admit that you LIKE this and that you DESERVE this!"
window hide
with hpunch
sm "I... Please stop, it's... nice but not very nice..."
scene supershootcum09 with dissolve
lp "I didn't hear you well enough! Say it out LOUD!"
scene supershootcum10 with dissolve
play sound "sounds/slap.mp3"
sm "Alright, I DO, Lois, I deserve it!"
lp "You sure as hell do, you dickless superhero!"
stop channel1
scene supershootcum11 with dissolve
play sound "sounds/slurp.mp3"
lp "Let me clean you of all this tasty virile seed..."
scene supershootcum12 with dissolve
play sound "sounds/slap.mp3"
mc "Hey, maybe HE wants to have a taste..."
scene supershootcum11 with dissolve
play sound "sounds/slurp.mp3"
lp "I want it all for ME!"
scene supershootcum12 with dissolve
play sound "sounds/slap.mp3"
mc "Well, hurry up Lois, cos I'm STILL HARD as you can feel from my fat rod slapping your backside!"
lp "Of course Master. Superman, get back on your feet, I wil let you have a taste. From somewhere I can't reach. My little overfilled rosebud!"
scene supermanshoot30:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
play sound "sounds/kiss.mp3"
lp "While I kiss [hero] and show my total devotion to his Super-Studliness!"
scene supermanshoot31 with dissolve
sm "But, I... never..."
lp "Just stick your tongue in there and slurp up all of [hero]'s manly juices. Including what's dripping OUT of my hole... DO IT NOW!"
scene supermanshoot32 with dissolve
play sound "sounds/lick03.mp3"
sm "If this please you, Lois..."
play sound "sounds/lick02.mp3"
lp "Mmmh, twirl that tongue DEEPER..."
scene supermanshoot33 with dissolve
play sound "sounds/slurp.mp3"
lp "Yes, that's it, you're hitting the right spot, AAAH!"
play sound "sounds/moan03.mp3"
scene supermanshoot34 with dissolve
play sound "sounds/kiss.mp3"
lp "You did well, Superman..."
scene supermanshoot35 with dissolve
stop sound
if age >= 20:
    lp "Now, gently take my strapon off. I want to get FUCKED by a REAL cock! A HUGE, MASSIVE, DONKEY-DICK!"
if age <= 19:
    lp "Now, gently take my strapon off. I want to get FUCKED by a REAL cock! A HUGE, MASSIVE, YOUNG DONKEY-DICK!"
scene supermanshoot36 with dissolve
play sound "sounds/wow.mp3"
lp "Just look at it, Superman! It's so GIGANTIC!"
sm "I wish I had a cock now..."
mc "Why don't you have a quick taste first Lois?"
scene supermanshoot37 with dissolve
play sound "sounds/lick01.ogg"
lp "It's just DEE-LI-CIOUS!"
scene supermanshoot38 with dissolve
lp "Best shaft I've EVER tasted!"
window hide
show loissuperlick
play channel2 "sounds/lick01.ogg"
pause
mc "Now that I'm SUPER-HARD, let's show Superman how to Super-Please a woman!"
stop channel2
scene supermanshoot39 with dissolve
lp "Mmmh, look at this thing! It's DROOLING pre-cum everywhere... He must be so HORNY!"
sm "Please stop doing that Lois, it's... all sticky..."
if age >= 20:
    lp "I'm just having a little bit of fun. Just to show you how WIDE I'm going to have to open my legs to let this monstercock slide into my tight little fuckhole..."
if age >= 18 and age <= 19:
    lp "I'm just having a little bit of fun. Just to show you how WIDE I'm going to have to open my legs to let this teenage monstercock slide into my tight little fuckhole..."
scene supermanshoot40 with dissolve
play sound "sounds/moan02.mp3"
mc "Now watch closely, this is how a Super-Stud like me gets all the girls..."
scene supermanshoot41 with dissolve
lp "I'm already dripping wet just by looking at his beautiful piece of boymeat!"
sm "Please don't say that, Lois..."
lp "But it's TRUE! FUCK ME, YOU MONSTER-DICKED YOUNG STALLION!"

label LoisSuperShortSlow:
$ loissuperharder = False
window hide
show loissupershortslowvideo behind loissupershortfastvideo
show loissupershortslowvideo behind loissupershortpovslowvideo
show loissupershortslowvideo behind loissuperfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissupershortfastvideo
hide loissupershortpovslowvideo
hide loissuperfuckslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
$ loissuperfuckfast = False
if loissuperfuckslow == False:
    lp "You're fucking me sssoo good!"
    $ loissuperfuckslow = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen loissupershortslow()
screen loissupershortslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVSlow")

label LoisSuperShortFast:
$ loissuperharder = False
window hide
show loissupershortfastvideo behind loissupershortslowvideo
show loissupershortfastvideo behind loissupershortpovfastvideo
show loissupershortfastvideo behind loissuperfuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissupershortslowvideo
hide loissupershortpovfastvideo
hide loissuperfuckfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
$ loissuperfuckslow = False
if loissuperfuckfast == False:
    lp "He's stretching my cunt so much! If only Clark Kunt had a huge cock like that..."
    $ loissuperfuckfast = True
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen loissupershortfast()
screen loissupershortfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVFast")

label LoisSuperShortPOVSlow:
$ loissuperharder = False
window hide
show loissupershortpovslowvideo behind loissupershortslowvideo
show loissupershortpovslowvideo behind loissupershortpovfastvideo
show loissupershortpovslowvideo behind loissuperfuckpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissupershortslowvideo
hide loissupershortpovfastvideo
hide loissuperfuckpovslowvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
$ loissuperfuckfast = False
if loissuperfuckslow == False:
    lp "You're fucking me sssoo good!"
    $ loissuperfuckslow = True
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loissupershortpovslow()
screen loissupershortpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortSlow")

label LoisSuperShortPOVFast:
$ loissuperharder = False
window hide
show loissupershortpovfastvideo behind loissupershortpovslowvideo
show loissupershortpovfastvideo behind loissupershortfastvideo
show loissupershortpovfastvideo behind loissuperfuckpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissupershortpovslowvideo
hide loissupershortfastvideo
hide loissuperfuckpovfastvideo
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
$ loissuperfuckslow = False
if loissuperfuckfast == False:
    lp "He's stretching my cunt so much! If only Clark Kunt had a huge cock like that..."
    $ loissuperfuckfast = True
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen loissupershortpovfast()
screen loissupershortpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperShortPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperShortFast")

label LoisSuperFuckSlow:
if loissuperharder == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharder = True        
window hide
show loissuperfuckslowvideo behind loissuperfuckfastvideo
show loissuperfuckslowvideo behind loissuperfuckpovslowvideo
show loissuperfuckslowvideo behind loissupershortslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissuperfuckfastvideo
hide loissuperfuckpovslowvideo
hide loissupershortslowvideo
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
call screen loissuperfuck()
screen loissuperfuck():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperShortSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEnd")

label LoisSuperFuckFast:
if loissuperharder == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharder = True        
window hide
show loissuperfuckfastvideo behind loissuperfuckslowvideo
show loissuperfuckfastvideo behind loissuperfuckpovfastvideo
show loissuperfuckfastvideo behind loissupershortfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissuperfuckslowvideo
hide loissuperfuckpovfastvideo
hide loissupershortfastvideo
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
call screen loissuperfuckfast()
screen loissuperfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperShortFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEnd")

label LoisSuperFuckPOVSlow:
if loissuperharder == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharder = True        
window hide
show loissuperfuckpovslowvideo behind loissuperfuckslowvideo
show loissuperfuckpovslowvideo behind loissuperfuckpovfastvideo
show loissuperfuckpovslowvideo behind loissupershortpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide loissuperfuckslowvideo
hide loissuperfuckpovfastvideo
hide loissupershortpovslowvideo
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
call screen loissuperfuckpovslow()
screen loissuperfuckpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEnd")

label LoisSuperFuckPOVFast:
if loissuperharder == False:
    lp "I want you to fuck me HARDER! And DEEPER TOO!"
    sm "You look totally full to breaking point alread..."
    lp "SHUT THE FUCK UP SUPERMAN! I NEED THIS GIANT COCK TO POUND ME HARDER NOW!"
    $ loissuperharder = True        
window hide
show loissuperfuckpovfastvideo behind loissuperfuckpovslowvideo
show loissuperfuckpovfastvideo behind loissuperfuckfastvideo
show loissuperfuckpovfastvideo behind loissupershortpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide loissuperfuckpovslowvideo
hide loissuperfuckfastvideo
hide loissupershortpovfastvideo
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
call screen loissuperfuckpovfast()
screen loissuperfuckpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LoisSuperFuckPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("LoisSuperShortPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LoisSuperFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LoisSuperFuckCumEnd")

label LoisSuperFuckCumEnd:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
mc "I'm gonna pump you full of cum soon, Lois!"
lp "Do it, STUD! Fill me up till I'm bloated with your hot spunk and I BELONG TO YOU!"
stop channel1
scene loissupercum01 with dissolve
play channel1 "sounds/boyorgasm01.mp3"
play channel1 "sounds/splooge01.mp3"
mc "HERE I GO! AAAH!"
window hide
with hpunch
mc "Have a good look, Superman, while I BREED Lois Pane!"
scene loissupercum02 with dissolve
sm "This is... horrible, she seems to be in such pain!"
window hide
with fastflash
play sound "sounds/moan04.ogg"
lp "No I'm not, I'm CU....MMMMIIIING! AAAH!"
scene loissupercum03 with dissolve
mc "Looks like my huge dick is stuck in there, gonna need your help a little..."
window hide
with hpunch
lp "I've never been pumped so FULL of warm nutsauce in my life, this is so GOO-OOD!"
scene loissupercum04 with dissolve
mc "You're gonna need to pull harder... I'm still blowing and Lois is getting bloated real quick!"
window hide
with fastflash
sm "I... I'm trying..."
scene loissupercum05 with dissolve
stop channel1
play sound "v041/plop.mp3"
mc "AAAH, that's better, FUCK!"
window hide
with hpunch
sm "Yuck, you're still blasting this weird white stuff!"
scene loissupercum06 with dissolve
play sound "sounds/moan02.mp3"
lp "Cover my body in it, I LOVE IT, I CRAVE YOUR YOUNG SPUNK!"
window hide
with fastflash
mc "Will do, Lois! Oh Fuck, I'm in HEAVENS, AAAH!"
scene loissupercum07 with dissolve
stop channel2
play sound "sounds/panting.mp3"
mc "Damn it... I came so much..."
lp "Mmmh, look at that huge dollop of sperm dangling from his engorged tip, there's more cum in that single drop than a normal man could produce in a week!"
scene loissupercum08 with dissolve
play sound "sounds/slurp.mp3"
lp "And he's TOTALLY covered me with OUNCES of his sweet young semen... It's so tasty..."
sm "Is it?..."
play sound "sounds/lick02.mp3"
lp "Ooh yeah, you want to taste it too, Superman?"
sm "I..."
scene loissupercum09 with dissolve
lp "Go on, have a lick, it might give you enough testosterone to grow you a dicklet one day..."
play sound "sounds/lick01.ogg"
mc "I doubt it but it's worth a try..."
label SupermanFuckNoSee:
scene loissupercum10 with dissolve
mc "This is how you get the girls, Superman, got it?"
if seensupermanshoot:
    sm "I suppose so... Thank you for showing me. AGAIN. * sigh *"
if loisharem == False:
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirllois at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ loisharem = True
    mc "And now Lois is in MY harem."
    lp "For SEX, I'll always be YOURS and READY to PLEASE YOU, [name]!"

stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main