label OfficeCCPD:
stop music
play music "sounds/ccpdoffice.mp3"
scene ccpd01
show ccpd01back
with fade

if mission05end and quest06end and mission06 == False and period == 0 and evilness <= 5:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Ah, there you are, just in time for a CRUCIAL MISSION."
    mc "Alright, mission mode is GO!"
    hide sawyereyeblink
    show sawyer05 at centerleft
    with fastdissolve
    cs01 "I DID manage to coax out some valuable intel from those thugs Catwoman... and yourself to some extent, arrested in the Narrows."
    mc "I was the main guy in that scene. I'm the MC."
    hide sawyer05
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "Whatever. The Stallion is hiding his gold in a locked vault. But the CCPD now knows the code to open it."
    cs01 "It is time to put him OUT OF BUSINESS FOR GOOD! Since his gang of thugs are mainly involved in sex crimes, YOU are to be the superhero speaheading this delicate mission."
    window hide
    play sound "sounds/achievement.mp3"
    $ mission06good = True
    $ mission06 = True
    show missionicon06 at poslocation
    $ renpy.pause(0.5, hard=True)
    show textmission06 at posmissiontext
    pause                        
    hide sawyer04
    show sawyereyeblink at centerleft
    with fastdissolve
    cs01 "There is a time-limit however, since the code we acquired will expire in three days..."
    mc "OK, but I'm not a thief, I don't even know how to open a vault even WITH a code."
    hide sawyereyeblink
    show sawyer03 at centerleft
    with fastdissolve
    cs01 "Since you accepted this mission, it is now your SOLE DUTY to find a way inside that vault and put an end to the Stallion's reign of SEX TERROR in the Narrows! DISMISSED."
    hide sawyer03 with moveoutleft
    mc "I need to find Catwoman. But who could possibly know her whereabouts?..."
    jump Main

if quest05 and quest05end == False:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Have you solved that quest I gave you yet?"
    mc "Err, no. No, I haven't yet."
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "Well, hurry up! More and more women are reporting their breasts shrinking! Someone must stop this!"
    mc "I fully agree. Small tits are, like, meh."
    cs01 "And don't come back until you've grown some SERIOUS balls!"
    jump Main
        
if mission01 and mission01end == False and mission01day == 2 and period == 0:
    show sawyerout01 at centerleft with dissolve
    cs02 "Ah, good thing you showed up on time and that I am already in my outdoor outfit. Mrs Porker is here too, so let's go to the crime scene."
    mc "Alright, that's why I'm here!"
    jump Mision01Alley

if mission01 and mission01end == False and mission01day == 2 and period == 1:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Where the hell have you been all day????"
    mc "Well, I thought I was supposed to come in the evening to be honest."
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "You were supposed to turn up DURING THE DAY!"
    mc "Ah, my bad, sorry. Well, let's go anyway. Where's Mrs Porker?"
    hide sawyer04
    show sawyer02 at centerleft
    with fastdissolve
    cs01 "She's gone! She didn't want to wait all day for YOU to show up! Now you've wasted ANOTHER DAY for NOTHING."
    mc "But I still have one more day to complete the mission, right?"
    hide sawyer02
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "Yes. ONLY ONE MORE DAY. SO you'd better show up tomorrow DURING THE DAY."
    mc "Fine, got it."
    cs01 "Now go back home, we're very busy here at the CCPD. Lots of crime going on in this town. THROUGHOUT THE DAY."
    jump Main

if mission01 and mission01end == False and mission01day == 3  and period == 0:
    show sawyerout01 at centerleft with dissolve
    cs02 "Finally, you showed up! Mrs Porker is here too, so let's go to the crime scene NOW. This is your FINAL DAY to complete this mission, may I remind you."
    mc "Alright, that's why I'm here!"
    jump Mision01Alley

if mission01 and mission01end == False and mission01day == 3  and period == 1:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Do you think this is funny?"
    mc "What?"
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "Showing up on the LAST DAY of the mission and in the evening to boot?"
    mc "Well, I was busy. But now I'm here so let's not dwell on the past and..."
    hide sawyer04
    show sawyer02 at centerleft
    with fastdissolve
    cs01 "It's TOO LATE. Mrs Porker is gone. And you have FAILED YOUR FIRST MISSION."
    play sound "sounds/losing.mp3"
    show missionicon01 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission01fail = True
    $ mission01end = True
    cs01 "And it was the EASIEST one too. EPIC FAIL."
    mc "I'm new to this superhero stuff, I need time to... adjust."
    hide sawyer02
    show sawyer03 at centerleft
    with fastdissolve
    cs01 "Go back home. Because of your incompetence, I now have the difficult duty of liaising with the Bureau f95 Mods to clean up YOUR MESS."
    jump Main

if mission01 and mission01end == False and mission01day >= 4:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Do you think this is funny?"
    mc "What?"
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "Showing up on PAST THE LAST DAY of the mission?"
    mc "Is it? How time flies..."
    hide sawyer04
    show sawyer03 at centerleft
    with fastdissolve
    cs01 "Go back home. You FAILED that mission. And because of your incompetence, I now have the difficult duty of liaising with the Bureau f95 Mods to clean up YOUR MESS."
    play sound "sounds/losing.mp3"
    show missionicon01 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission01fail = True
    $ mission01end = True
    jump Main

if mission01 == False and mission01end == False:
    jump Mission01

if mission03end and period == 0 and mission04 == False and mission04end == False:
    jump Mission04 

if mission04 and mission04end == False and seenbeatbarr and period == 1: 
    jump Mission04Next

if mission04 and mission04end and mission04debrief == False and toldmilfmission04 == False:
    $ mission04debrief = True
    show sawyereyeblink at centerleft with dissolve
    cs01 "Well, I must say that I am impressed."
    mc "About what?"
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "You solving this... delicate mission I assigned to you."
    mc "The one about the anal invaders?"
    hide sawyer04
    show sawyer05 at centerleft
    with fastdissolve
    cs01 "Yes, that one. You act like you don't remember..."
    mc "Well, I, err..."
    hide sawyer05
    show sawyer02 at centerleft
    with fastdissolve
    cs01 "Just like Agent Skully... Very strange. Notwithstanding her traumatic anal AND pussy injuries."
    mc "What? What happened to her?"
    hide sawyer02
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "That's what I would have liked to find out from you. She's recovering in hospital right now. Fortunately, no further patients have been admitted. Therefore, I consider this case CLOSED. Unexplainably.."
    play sound "sounds/winning.mp3"
    show missionicon04 at poslocation
    $ renpy.pause(0.5, hard='True')
    show winicon at poswin
    $ mission04win = True
    hide sawyer04
    show sawyereyeblink at centerleft
    with fastdissolve
    mc "Yeah, another mission bites the dust!"
    jump CCPDDialogue

if mission04 and mission04end and mission04debrief == False and toldmilfmission04:
    $ mission04debrief = True
    show sawyereyeblink at centerleft with dissolve
    cs01 "Well, I must say that I am impressed."
    mc "About what?"
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "You solving this... delicate mission I assigned to you."
    mc "The one about the anal invaders? Yeah, I did that. All by myself. Like a TRUE superhero!"
    hide sawyer04
    show sawyer05 at centerleft
    with fastdissolve
    cs01 "Somehow, Agent Skully doesn't recall any of your \"super-heroism\". Care to explain?"
    mc "Err, she must have been knocked out during the mighty battle I fought against, err... the Super-Villain anal invader enemies."
    hide sawyer05
    show sawyer02 at centerleft
    with fastdissolve
    cs01 "And... Can you explain her traumatic anal AND pussy injuries?"
    mc "Her what? I've got nothing to do with THAT, I swear!"
    hide sawyer02
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "I didn't accuse you of anything, [hero]... Anyway, she's recovering in hospital right now. And no further patients have been admitted. Therefore, I consider this case CLOSED. Unexplainably.."
    play sound "sounds/winning.mp3"
    show missionicon04 at poslocation
    $ renpy.pause(0.5, hard='True')
    show winicon at poswin
    $ mission04win = True
    hide sawyer04
    show sawyereyeblink at centerleft
    with fastdissolve
    mc "Yeah, another mission bites the dust!"
    jump CCPDDialogue

if mission04end and period == 0 and quest05 == False and quest05end == False and mclevel02:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Ah, [hero]. I have a QUEST for you."
    mc "That's why I'm here, to solve missions and quests."
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "You remember Mrs Porker?"
    mc "Oh uh, she's been raped again?"
    hide sawyer04
    show sawyer02 at centerleft
    with fastdissolve
    cs01 "Much worse than that. Come to my office, I'll show you."
    jump Quest05Start

if  mission06 and mission06end == False and mission06good and mission06day >= 4:
    show sawyereyeblink at centerleft with dissolve
    cs01 "Another day, and another major FAILURE from the Cockham League of Justice, courtesy of [hero]!"
    mc "Err... What did I do?"
    hide sawyereyeblink
    show sawyer04 at centerleft
    with fastdissolve
    cs01 "What DIDN'T you do is the correct question. And the answer is NOTHING! The Stallion still rules the Narrows and we are back to SQUARE ONE because of your INCOMPETENCE!"
    play sound "sounds/losing.mp3"
    show missionicon06 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    $ mission06fail = True
    $ mission06end = True
    hide sawyer04
    show sawyer03 at centerleft
    with fastdissolve
    cs01 "Now I need to think of a new way to arrest Samson Goldcock without having the District Attorney on my back. You are DISMISSED!"
    jump Main
if  mission06 and mission06end == False and mission06good:
    show sawyereyeblink at centerleft with dissolve
    cs01 "What are you doing here?"
    mc "Paying you a courteous visit, Captain Sawyer. And if you're not too busy, we could have some SAY-AY..."
    hide sawyereyeblink
    show sawyer03
    with fastdissolve 
    cs01 "Get back to WORK! You have a MISSION and you need to FOCUS on it!"
    jump Main
if mission06end and mission06win and mission06good and toldmission06good == False:
    $ toldmission06good = True
    show sawyereyeblink at centerleft with dissolve
    cs01 "Ah, there you are. THe HERO who unthroned the Stallion!"
    call Good from _call_Good_12
    mc "I did it with my SUPER-COCK. Please tell the media about that crucial detail."
    hide sawyereyeblink
    show sawyer04
    with fastdissolve    
    cs01 "Err, maybe not. But good work nonetheless. Now the Stallion has been banned from the Narrows and the CCPD can finally bring LAW and ORDER back to those slums."
    jump Main
    
show sawyereyeblink at centerleft with dissolve
cs01 "[hero]. What brings you here?"
label CCPDDialogue:
menu:
    "I'm ready to go on the beat, Captain Sawyer." if wentbeat and mclevel02:
        cs01 "I'm not though. Come back another time."
        hide sawyereyeblink with moveoutright
        mc "Damn, that was brutal. I guess more new scenes need to be added now that I've reached Level02."
        jump Main
    "I'm ready to go on the beat, Captain Sawyer." if wentbeat and mclevel02 == False:
        if sawyerfootjob == False:
            hide sawyereyeblink
            show sawyer03 at centerleft
            with fastdissolve                
            cs01 "Then follow me to my office, I need to change into my outdoors uniform..."
            jump SawyerBeat
        cs01 "I'll change into my outdoors outfit. Just wait right here..."
        hide sawyereyeblink with moveoutright
        scene ccpd01
        show ccpd01back
        with fade 
        show sawyerout01 at centerleft with dissolve
        cs02 "And where would you like to go? Have a quick look at the map to decide..."
        stop music
        scene cockhammap
        menu:
            "Old Cockham":
                jump CockhamBeat                
            "Barr Town":
                jump BarrBeat
            "Porkher Row":
                jump PorkherBeat
    "Any SEX crime cases for me, Captain Sawyer?":
        hide sawyereyeblink
        show sawyer04 at centerleft
        with fastdissolve
        cs01 "Everything is quiet on the sex crime front."
        mc "Ah. I feel kind of useless."
        hide sawyer04
        show sawyereyeblink at centerleft
        with fastdissolve                
        cs01 "I can understand..."
        if period == 1:
            jump CCPDDialogue
        hide sawyereyeblink
        show sawyer05 at centerleft
        with fastdissolve                
        cs01 "However, I was about to go on the beat. Care to join me?"
        menu:
            "Sure, why not.":
                if sawyerfootjob == False:
                    hide sawyer05
                    show sawyer03 at centerleft
                    with fastdissolve                
                    cs01 "Then follow me to my office, I need to change into my outdoors uniform..."
                    jump SawyerBeat
                cs01 "I'll change into my outdoors outfit. Just wait right here..."
                hide sawyer05 with moveoutright
                scene ccpd01
                show ccpd01back
                with fade 
                show sawyerout01 at centerleft with dissolve
                cs02 "So, are you ready to go on the beat, [hero]?"
                mc "Sure, Captain Sawyer. The Cockham League of Justice will prevail!"
                cs02 "And where shall we go? Have a quick look at the map to decide..."
                stop music
                scene cockhammap
                menu:
                    "Old Cockham":
                        jump CockhamBeat                
                    "Barr Town":
                        jump BarrBeat
                    "Porkher Row":
                        jump PorkherBeat
            "Na, I'm good.":
                hide sawyer05
                show sawyer02 at centerleft
                with fastdissolve                
                cs01 "Fine. Then I'll go alone. Now if you'll excuse me."
                jump Main            
    "What can you tell me about The Stallion?" if mission06win == False:
        hide sawyereyeblink
        show sawyer04 at centerleft
        with fastdissolve
        cs01 "Well. He's known for his sexual prowess. He's got an absolutely GIGANTIC black powercock!"
        mc "I meant in terms of CRIMINAL ACTIVITY."
        hide sawyer04
        show sawyer02 at centerleft
        with fastdissolve                
        cs01 "Ah, sorry. He's an arms dealer for starters but we have never been able to catch him in the act."
        hide sawyer02
        show sawyer05 at centerleft
        with fastdissolve                
        cs01 "And he leads a gang of thugs in the Narrows. They're called the \"Narrows Bros\". Even though some members are girls, like his two closest lieutenants, Jasmine and Africa."
        hide sawyer05
        show sawyereyeblink at centerleft
        with fastdissolve                
        mc "Thanks for the info, Captain."
        jump CCPDDialogue
    "What can you tell me about The Joker?":
        hide sawyereyeblink
        show sawyer04 at centerleft
        with fastdissolve
        cs01 "He's no joke! A complete LUNATIC. Keeps trying to blow up stuff in the city. Fortunately, Batman has foiled his attempts at wreaking chaos. So far."
        mc "Batman? But he's a doofus. Or so I'm told."
        hide sawyer04
        show sawyereyeblink at centerleft
        with fastdissolve                
        cs01 "Maybe you underestimate him then. He's very useful to the CCPD."
        mc " * Damn it. This is almost non-sexual NTR. Almost. *"
        jump CCPDDialogue
    "What can you tell me about Harley Quiff?":
        hide sawyereyeblink
        show sawyer02 at centerleft
        with fastdissolve
        cs01 "She is innocent until proven guilty. And this is all I will say. As ordered by the defamation judge..."
        mc "Those judges can be nasty..."
        hide sawyer02
        show sawyereyeblink at centerleft
        with fastdissolve                
        jump CCPDDialogue
    "What can you tell me about the Mafia?":
        hide sawyereyeblink
        show sawyer02 at centerleft
        with fastdissolve
        cs01 "They have complete control over the borough of \"Little Italy\". Our officers don't even dare go there. Except the Italian ones."
        mc "They must have a weakness."
        hide sawyer02
        show sawyer04 at centerleft
        with fastdissolve                
        cs01 "Well, find it. Cos I'm stumped..."
        hide sawyer04
        show sawyereyeblink at centerleft
        with fastdissolve                
        jump CCPDDialogue
    "What can you tell me about The Chinese Triad?":
        hide sawyereyeblink
        show sawyer04 at centerleft
        with fastdissolve
        cs01 "Ada Wang is their leader. All members of her Triad have a tattoo on their left arm, which she inked herself."
        mc "Interesting. What does the tattoo look like?"
        hide sawyer04
        show sawyereyeblink at centerleft
        with fastdissolve                
        cs01 "I don't know at this stage..."
        jump CCPDDialogue
    "I feel horny. And so does my MONSTER COCK!" if quest05end and mclevel02:
        hide sawyereyeblink
        show sawyer03 at centerleft
        with fastdissolve
        cs01 "Is that so? I suppose I have a bit of time on my hands for a quick romp with a hung super-hero... Follow me to my office."
        mc "Yeah!"
        jump SawyerFuck
    "I feel horny. For a footjob." if sawyerfootjob and mclevel02 == False:
        hide sawyereyeblink
        show sawyer02 at centerleft
        with fastdissolve
        cs01 "Have you been a naughty boy again?"
        mc "Yes. A very naughty boy. Who deserves a punishment!"
        hide sawyer02
        show sawyer03 at centerleft
        with fastdissolve                
        cs01 "Then follow me to my office. Naughty superhero."
        jump SawyerFootjob
    "I'm done.":
        hide sawyereyeblink
        show sawyer02 at centerleft
        with fastdissolve
        cs01 "Good, because I'm VERY busy. With all types of CRIME."
        jump Main

label SawyerBeat:
stop music
scene sophiaoffice08 with dissolve
cs01 "Just sit here, I won't take long."
scene sawyerstrip01 with fade
play music "sounds/sexy03.mp3"
mc "* Oooh, she's getting undressed behind that curtain. Pity I can't see through it properly. *"
if mcsenses >= 1:
    call screen usepower("usesenses", "CopCurtainb", "CopCurtainNakedb") with dissolve
label CopCurtainb:
scene sawyerstrip02 with dissolve
mc "* I can barely see anything but I'm gonna guess she's getting undressed. *"
scene sawyerstrip03 with dissolve
mc "* And now I believe she is changing into her outdoor gear... *"
scene sawyerstrip04 with dissolve
mc "* It's almost as if she's putting on a show for me, except I can't see a damn thing. *"
scene sawyerstrip05 with dissolve
mc "* But I guess I should just wait and stop thinking about it... *"
scene sawyerstrip06 with dissolve
mc "* I think she's almost ready now. Let's act natural... *"
stop music
scene sawyerstripend with dissolve
cs02 "So, are you ready to go on the beat, [hero]?"
mc "Sure, Captain Sawyer. The Cockham League of Justice will prevail!"
cs02 "And where shall we go? Have a quick look at the map to decide..."
scene cockhammap
menu:
    "Old Cockham":
        jump CockhamBeat
    "Barr Town":
        jump BarrBeat
    "Porkher Row":
        jump PorkherBeat

label CopCurtainNakedb:
$ sawyerfootjob = True
scene sawyerstrip02b with dissolve
mc "* That's much better, I can totally see through this ..., it's like it's transparent. I like that Super-Power... *"
scene sawyerstrip03b with dissolve
mc "* Mmh, I'm starting to get a hardon... *"
scene sawyerstrip04b with dissolve
mc "* Ooh yeah, baby, take that bra off while I... adjust my hardening dong... *"
scene sawyerstrip05b with dissolve
mc "* Now we're talking! I'm gonna have a fast wank while she finishes... *"
scene sawyerstrip06b with dissolve
mc "* Just need a few more seco... *"
cs02 "I trust you didn't use your Super-Senses to w..."
stop music
scene sawyerstripendbad with dissolve
cs02 "What the hell! You DID use your Super-Vision you fucking PERVERT!"
scene sawyerprefoot01 with dissolve
mc "Err... Sorry, I couldn't help it... Your body... It's so HOT!"
cs02 "Is that so? Well, we can't go out with your giant cock sticking out like that for all to see. So we won't be going on the beat today."
scene sawyerprefoot02 with dissolve
cs02 "Since... you deserve a PUNISHMENT for the crime of \"Misuse of Superpowers\"!"
mc "Uh oh..."
cs02 "Get on your knees and lick my feet!"
play channel1 "sounds/sexy03.mp3"
scene sawyerprefoot03 with dissolve
play sound "sounds/lick01.ogg"
cs02 "A bit higher now. While I tame that hard BEAST of yours..."
scene sawyerprefoot04 with dissolve
play sound "sounds/lick01.ogg"
cs02 "That's good... You like my fishnet stockings, don't you, naughty boy?"
mc "Yes, Captain Sawyer."
if age >= 20:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant young meat!"
if age >= 18 or age <= 19:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant teeenage meat!"
show sawyerfootslowstart
play channel2 "sounds/wank.mp3"
scene sawyerfootslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
cs02 "Does this feel good on your trembling shaft, [hero]?"
mc "Oh yeah, fuck..."
window hide
pause
cs02 "Remove your hand and let me pump that fat shaft FASTER!"
scene sawyerfootfastvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "God, your feet... These stockings..."
window hide
pause
cs02 "You're gonna cum aren't you? You're gonna unload those bloated balls that are making you lose focus on your duties... Go on, DUMP YOUR YOUNG CREAM!" 
hide sawyerfootslowstart
scene sawyerfootcum01
with dissolve
cs02 "Ooh yeah, you're real close, you're spattering pre-cum all over the pl..."
scene sawyerfootcum02 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAAH!"
window hide
with fastflash
cs02 "That's it, let it all out!"
scene sawyerfootcum03 with dissolve
cs02 "Look at the filthy mess you're making!"
window hide
with fastflash
mc "Ah, it's not my fault, AAAH!"
window hide
with fastflash
cs02 "YES IT IS! This is what happens when you MISUSE YOUR SUPERPOWERS!"
stop channel1
stop channel2
scene sawyerfootcum04 with dissolve
play sound "sounds/panting.mp3"
mc "Aaah... I came too much..."
cs02 "And now you're TIRED and USELESS. So much for that so-called Super-Studliness Captain MILF warned me about. My FEET defeated YOUR superpower!"
scene sawyerfootcum05 with dissolve
cs02 "So let this be a LESSON to you. Now get out of here..."
mc "Just give me a small break and I'll get another erection in no ti..."
cs02 "GET OUT OF MY OFFICE!"
jump Main
    
label SawyerFootjob:
stop music
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene sophiaoffice08 with fade
cs01 "You know the drill. Sit here and wait for me as I change into my PUNISHMENT outfit!"
play channel1 "sounds/sexy03.mp3"
scene sawyerstrip02b with dissolve
mc "She's teasing me... Into being a very naughty boy!"
scene sawyerstrip06b with dissolve
mc "And now she's ready to PUNISH ME!"
scene sawyerstripendbad with dissolve
cs02 "THIS THING... should be INSIDE your thong and not sticking out ROCK-HARD like that! I'm booking you for indecent exposure... And illegal carrying of a LARGE CALIBER WEAPON!"
mc "Uh oh... What's the sentence, Officer?"
cs02 "You are condemned to... getting down on your knees and licking my feet!"
scene sawyerprefoot03 with dissolve
play sound "sounds/lick01.ogg"
cs02 "A bit higher now. While I tame that hard BEAST of yours..."
scene sawyerprefoot04 with dissolve
play sound "sounds/lick01.ogg"
cs02 "That's good... You like my fishnet stockings, don't you, naughty boy?"
mc "Yes, Captain Sawyer."
if age >= 20:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant young meat!"
if age >= 18 and age <= 19:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant teeenage meat!"
show sawyerfootslowstart
play channel2 "sounds/wank.mp3"
scene sawyerfootslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
cs02 "Does this feel good on your trembling shaft, [hero]?"
mc "Oh yeah, fuck..."
window hide
pause
cs02 "Remove your hand and let me pump that fat shaft FASTER!"
scene sawyerfootfastvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "God, your feet... These stockings..."
window hide
pause
cs02 "You're gonna cum aren't you? You're gonna unload those bloated balls that are making you lose focus on your duties... Go on, DUMP YOUR YOUNG CREAM!" 
hide sawyerfootslowstart
scene sawyerfootcum01
with dissolve
cs02 "Ooh yeah, you're real close, you're spattering pre-cum all over the pl..."
scene sawyerfootcum02 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAAH!"
window hide
with fastflash
cs02 "That's it, let it all out!"
scene sawyerfootcum03 with dissolve
cs02 "Look at the filthy mess you're making!"
window hide
with fastflash
mc "Ah, it's not my fault, AAAH!"
window hide
with fastflash
cs02 "YES IT IS! This is what happens when you MISUSE YOUR SUPERPOWERS!"
stop channel1
stop channel2
scene sawyerfootcum04 with dissolve
play sound "sounds/panting.mp3"
mc "Aaah... I came too much..."
cs02 "My FEET have once again defeated YOUR superhero boycock!"
scene sawyerfootcum05 with dissolve
cs02 "So let this be another LESSON for you. Now put your thong back on and GET OUT OF HERE!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label SawyerFuck:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
stop music
play music "sounds/sexy02.mp3"
scene sawyerprelick01 with fade
cs01 "I suppose you want me to help you get a hardon?"
mc "That would help. Sexual intercourse is best with a HARD dick."
scene sawyerprelick02:
    subpixel True
    xpos 0.0 ypos 0.0
    ease 7.0 ypos -1.0 xpos -0.04
with dissolve
$ renpy.pause(2.0, hard='True')
pause
mc "Now turn round, your ass is definitely cock-hardening..."
scene sawyerprelick03:
    subpixel True
    xpos -0.04 ypos -0.0
    ease 7.0 ypos -1.0 xpos 0.0
with dissolve
$ renpy.pause(2.0, hard='True')
pause
cs01 "You talk more like a sex pervert than a Super-Hero, you know that?"
scene sawyerprelick04:
    subpixel True
    xpos 0.0 ypos -1.0
    ease 6.0 ypos -.15 xpos -0.04
with dissolve
$ renpy.pause(2.0, hard='True')
pause
mc "Yeah, I know that."
cs01 "And I see that your cock is now ROCK-HARD."
scene sawyerprelick05 with dissolve
play sound "sounds/moan01.mp3"
cs01 "I can feel it pushing against my back... It's so amazingly HUGE!"
if age >= 20:
    mc "Yep, eighteen inches of SUPER-HERO COCK right there for you, Captain Sawyer..."
if age >= 18 and age <= 19:
    mc "Yep, eighteen inches of SUPER-HERO TEEN COCK right there for you, Captain Sawyer..."
cs01 "Call me Maggie. And go and sit on the sofa so I can take CARE of that giant love muscle..."
scene sawyerprelick06 with dissolve
cs01 "You simply can't concentrate on the job with a hardon THAT MASSIVE, can you?"
mc "It's true, you need to..."
scene sawyerprelick07 with dissolve
cs01 "I'm gonna hold this monster tight while I slowly lick the whole shaft to a mighty explosion!"
play channel1 "sounds/lick01.ogg"
label SawyerLickSlow:
window hide
$ sawyerlickfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickslowvideo behind sawyerlicksceneslowvideo
show sawyerlickslowvideo behind sawyerlickfastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlicksceneslowvideo
hide sawyerlickfastvideo
if sawyerlickslow == False:
    $ sawyerlickslow = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sawyerlickslow()
screen sawyerlickslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneSlow")

label SawyerLickSceneSlow:
$ sawyerlickfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlicksceneslowvideo behind sawyerlickslowvideo
show sawyerlicksceneslowvideo behind sawyerlickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlickslowvideo
hide sawyerlickscenefastvideo
if sawyerlickslow == False:
    $ sawyerlickslow = True
    mc "Yeah, lick that rod nice and slow..."
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sawyerlicksceneslow()
screen sawyerlicksceneslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SawyerLickSceneFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSlow")

label SawyerLickFast:
$ sawyerlickslow = False
if sawyerlickfast == False:
    $ sawyerlickfast = True
    mc "That's it, Maggie, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickfastvideo behind sawyerlickslowvideo
show sawyerlickfastvideo behind sawyerlickscenefastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlickslowvideo
hide sawyerlickscenefastvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerlickfast()
screen sawyerlickfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerLickCum")

label SawyerLickSceneFast:
$ sawyerlickslow = False
if sawyerlickfast == False:
    $ sawyerlickfast = True
    mc "That's it, Maggie, just like that..."
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerlickscenefastvideo behind sawyerlicksceneslowvideo
show sawyerlickscenefastvideo behind sawyerlickfastvideo
$ renpy.pause(1.0, hard='True')
hide sawyerlicksceneslowvideo
hide sawyerlickfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerlickscenefast()
screen sawyerlickscenefast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickSceneSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerLickFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerLickCum")

label SawyerLickCum:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "Oh God, oh..."
scene sawyerlickcum01 with dissolve
play sound "sounds/boymoan03.mp3"
cs01 "You're leaking pre-slime like a faucet! That means you're about to bust your nut!"
scene sawyerlickcum02 with dissolve
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "AAAH!"
window hide
with hpunch
cs01 "Mmh, yeah, it's FLYING out of your cumslit!"
scene sawyerlickcum03 with dissolve
if age >= 20:
    cs01 "Look at that shot, more manly cum in that single shot than a hundred men combined!"
if age >= 18 and age <= 19:
    cs01 "Look at that shot, more manly teenage cum in that single shot than a hundred men combined!"
window hide
with fastflash
cs01 "As the Captain of the CCPD, I ORDER you to KEEP PUMPING THAT LOAD!"
scene sawyerlickcum04 with dissolve
mc "FFF..FFFFFUUUUCCCKK, RHAAA!"
window hide
with hpunch
cs01 "Keep pumping boy, let it RAIN down upon us!"
window hide
with fastflash
cs01 "Good boy, COVER my body in your red-hot spunk!"
with hpunch
mc "AAAH, AAAAH!"
scene sawyerlickcum05 with dissolve
stop channel1
play sound "sounds/lick03.mp3"
cs01 "Mmmh, it's so thick and chunky. And there's so much of it..."
play sound "sounds/slurp.mp3"
cs01 "I've defeated your mighty cock once ag..."
scene sawyerprefuck01 with dissolve
play sound "sounds/gasp.mp3"
mc "No you haven't! I'm only just STARTING to have fun!"
cs01 "What? You're... LIFTING ME UP WITH YOUR COCK???"
mc "That's right, and I'm going to pound your pussy against the wall now!"
scene sawyerprefuck02 with dissolve
play sound "sounds/moan02.mp3"
mc "So let me help you get these panties down..."
scene sawyerprefuck03 with dissolve
cs01 "You're so... ROUGH. You're gonna fuck my poor pussy while I'm still CAKED in your cum?"
mc "I can't wait Maggie! My cock needs to go down so I can concentrate on the job, remember?"
scene sawyerfuckbackground
show sawyerprefuck04
with dissolve
cs01 "Fine, get on with it, just FUCK M..."
hide sawyerprefuck04
show sawyerprefuck05
with fastdissolve
play sound "sounds/spanking.mp3"
mc "Shut up and let me do the talking!"
hide sawyerprefuck05
show sawyerprefuck04
with fastdissolve
cs01 "Ouch! Why did you do that..."
hide sawyerprefuck04
show sawyerprefuck05
with fastdissolve
play sound "sounds/spanking.mp3"
cs01 "AAAH! I'm at your service!"
scene sawyerprefuck06 with dissolve
mc "Good, now let's start the FUCKING!"

label SawyerWallSlow:
window hide
$ sawyerwallfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallslowvideo behind sawyerwallpovslowvideo
show sawyerwallslowvideo behind sawyerwallfastvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sawyerwallfastvideo
hide sawyerwallpovslowvideo
show sawyerfuckbackground at sawyerstreetbackground behind sawyerwallslowvideo
if sawyerwallslow == False:
    $ sawyerwallslow = True
    cs01 "You fuck me so good... AAAH!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
call screen sawyerwallslow()
screen sawyerwallslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVSlow")

label SawyerWallPOVSlow:
$ sawyerwallfast = False
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallpovslowvideo behind sawyerwallslowvideo
show sawyerwallpovslowvideo behind sawyerwallpovfastvideo
show sawyerwallpovslowvideo behind sawyerfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex05.mp3"
hide sawyerfuckbackground
hide sawyerwallslowvideo
hide sawyerwallpovfastvideo
if sawyerwallslow == False:
    $ sawyerwallslow = True
    cs01 "You fuck me so good... AAAH!"
window hide
pause
show faster:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
call screen sawyerwallpovslow()
screen sawyerwallpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("SawyerWallPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallSlow")

label SawyerWallFast:
$ sawyerwallslow = False
if sawyerwallfast == False:
    $ sawyerwallfast = True
    cs01 "Oh God, fuck me faster, RAM that giant cock in me!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallfastvideo behind sawyerwallpovfastvideo
show sawyerwallfastvideo behind sawyerwallslowvideo
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sawyerwallslowvideo
hide sawyerwallpovfastvideo
show sawyerfuckbackground at sawyerstreetbackgroundb behind sawyerwallfastvideo
pause
show slower:
    xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerwallfast()
screen sawyerwallfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerWallCum")

label SawyerWallPOVFast:
$ sawyerwallslow = False
if sawyerwallfast == False:
    $ sawyerwallfast = True
    cs01 "Oh God, fuck me faster, RAM that giant cock in me!"
window hide
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show sawyerwallpovfastvideo behind sawyerwallfastvideo
show sawyerwallpovfastvideo behind sawyerwallpovslowvideo
show sawyerwallpovfastvideo behind sawyerfuckbackground
$ renpy.pause(1.0, hard='True')
stop channel1
play channel1 "sounds/womansex04.mp3"
hide sawyerfuckbackground
hide sawyerwallfastvideo
hide sawyerwallpovslowvideo
pause
show slower:
    xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500     
show cum:
    xpos 1750 ypos 1020    
call screen sawyerwallpovfast()
screen sawyerwallpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("SawyerWallFast")
    button:
        xpos 1750
        ypos 1020
        xysize(100, 60)        
        action Jump ("SawyerWallCum")

label SawyerWallCum:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
cs01 "You're TEARING my pussy apart, please just me give your seed, I WANT IT!"
stop channel1
scene wallsawyercum01 with dissolve
play channel1 "v031/boyorgasm02.mp3"
play channel2 "sounds/splooge02.mp3"
mc "Fuck, OH, here it comes!"
window hide
with fastflash
cs01 "I can take your load, I can tak..."
scene wallsawyercum02 with dissolve
play sound "sounds/moan05.mp3"
cs01 "...AAAAH, I'm cumming!"
window hide
with hpunch
mc "I'm gonna FLOOD your insides Maggie, RHAAA!"
scene wallsawyercum03 with dissolve
play sound "sounds/moan04.ogg"
cs01 "You're pumping so much cum, I can't believe it!"
window hide
with hpunch
play sound "sounds/moan05.mp3"
cs01 "Show me what a STUD you are, pull it out and douse my back with your mighty spunk!"
scene wallsawyercum04 with dissolve
stop channel2
play sound "sounds/boymoan05.mp3"
mc "AAAAH, FUCK!"
window hide
with fastflash
cs01 "That's it, EMPTY YOUR BALLS ON ME, AAAH!" 
scene wallsawyercum05 with dissolve
play sound "sounds/moan06.ogg"
cs01 "Oh my God, you're just a CUM MACHINE!"
window hide
with hpunch
play sound "sounds/splat.ogg"
mc "Y...YES, RHAAA! A little bit more..."
scene wallsawyercum06 with dissolve
play sound "sounds/moan01.mp3"
cs01 "STILL?"
window hide
with fastflash
mc "Fuck yeah, AAAH!"
scene wallsawyercum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "Phew..."
cs01 "You've made such a mess... I'm gonna have to call Sergeant Dani to help me clean all this nasty [age]yo spunk..."
mc "Oooh, can I watch?"
cs01 "NO! Go back to your compound and be READY to be be a superhero at last!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label Mission01:
show sawyereyeblink at centerleft with dissolve
cs01 "Ah, I'm glad you came [hero]. I'm Captain Sawyer, head of the CCPD and we have a serious case on our hands. A rape."
mc "Captain MILF told me I shouldn't be concerned with such petty crime or I'd do nothing else so..."
hide sawyereyeblink
show sawyer04 at centerleft
with fastdissolve
cs01 "I understand, But the Bureau f95, the Cockham branch of the FBI, has specifically requested your help on the matter."
hide sawyer04
show sawyer05 at centerleft
with fastdissolve
cs01 "It concerns a woman they have been scrutinizing for the past three years now in the hope of finding something interesting going on in her life. To no avail so far I might add."
hide sawyer05
show sawyer04 at centerleft
with fastdissolve
cs01 "And therefore, since something finally HAPPENED, they want YOU on the case. And they're giving you three days to make an arrest before they send in the \"Mods\"."
mc "The \"Mods\"?"
hide sawyer04
show sawyer02 at centerleft
with fastdissolve
cs01 "That's the name they give to their elite team. When they show up, things can turn ugly real quick. So, do you accept?"
mc "I suppose I could make an exception. If it's for the Bureau f95. So this is a mission, right? With a time-limit?"
window hide
play sound "sounds/achievement.mp3"
$ mission01 = True
show missionicon01 at poslocation
$ renpy.pause(0.5, hard=True)
show textmission01 at posmissiontext
pause
hide sawyer02
show sawyereyeblink at centerleft
with fastdissolve
cs01 "That's correct. Past a delay of three days without fulfilling your mission, the Bureau f95 will take you off the case and rip you apart with bad reviews in newspapers articles."
mc "Yikes. I'd better hurry up then. Let's start straight away!"
hide textmission01
hide missionicon01
hide sawyereyeblink
show sawyer03 at centerleft
with fastdissolve
cs01 "Follow me to my office, the victim is waiting for us in there right now."
stop music
scene sophiaoffice01 with dissolve
cs01 "This is Mrs Sophia Porker. This innocent wife and mother was raped twice in only two days."
so "And before that, I only had sex with my husband like once in three years, and it was a quick scene, plus he has a tiny dick."
mc "Sorry to hear that, ma'am. Can you describe your aggressors?" 
scene sophiaoffice02 with dissolve
so "The same two black thugs with GIANT cocks! Well, at least compared to my hubby, not to yours obviously Mr [hero]..."
scene sophiaoffice03 with dissolve
cs01 "Please concentrate Mrs Porker. Where did it happen exactly?"
so "In a dark alley, in the Narrows."
scene sophiaoffice06 with dissolve
mc "The same alley on both occasions?"
so "Yes... I, err... went back to see if they would be there again. You know, just to make sure it would be safe in the future."
scene sophiaoffice04 with dissolve
so "But they WERE there again, and then they both raped me, AGAIN! With their great big black cocks..."
scene sophiaoffice05 with dissolve
so "Like they first DPed me, then they even stuck both their huge shafts in my..."
scene sophiaoffice03 with dissolve
cs01 "Ok, ok, let's not go into too many details here. We wouldn't want you to re-live the traumatic experience in your head, now would we?" 
scene sophiaoffice04 with dissolve
so "No, you're right, that would be terrible. I do have drea... I mean, nightmares about their monster schlongs fucking me over and over again, you know?"
scene sophiaoffice06 with dissolve
mc "What's the name of the alley do you remember?"
so "Yes I do. It was called Rapists' Alley. The name kind of stuck."
mc "It's best if you accompany me and show me exactly what happened. So we can find clues and whatnot."
scene sophiaoffice07 with dissolve
cs01 "[hero], we need to talk for a moment. Please wait outside Mrs Porker, we'll be with you in a moment."
so "Uh... Alright, Madam officer."
scene sophiaoffice08 with dissolve
cs01 "I'm coming with you. I have strict instructions from Captain MILF not to let you go to the Narrows on your own on your first assignment."
mc "What? Doesn't anybody trust me in this town?"
cs01 "Apparently not. Let me get dressed for outdoors duties and let's go. Just sit here, I won't take long."

scene sawyerstrip01 with fade
play music "sounds/sexy03.mp3"
mc "* Oooh, she's getting undressed behind that curtain. Pity I can't see through it properly. *"
if mcsenses >= 1:
    call screen usepower("usesenses", "CopCurtain", "CopCurtainNaked") with dissolve

label CopCurtain:
scene sawyerstrip02 with dissolve
mc "* I can barely see anything but I'm gonna guess she's getting undressed. *"
scene sawyerstrip03 with dissolve
mc "* And now I believe she is changing into her outdoor gear... *"
scene sawyerstrip04 with dissolve
mc "* It's almost as if she's putting on a show for me, except I can't see a damn thing. *"
scene sawyerstrip05 with dissolve
mc "* But I guess I should just wait and stop thinking about it... *"
scene sawyerstrip06 with dissolve
mc "* I think she's almost ready now. Let's act natural... *"
stop music
scene sawyerstripend with dissolve
cs02 "So, are you ready for your first assignment, [hero]?"
mc "Sure, Captain Sawyer. The Cockham League of Justice will prevail!"
scene sawyerprefoot00 with dissolve
play sound "sounds/dispatch.mp3"
cs02 "Tell Mrs Porker we are good to go."
jump Mision01Alley

label CopCurtainNaked:
$ sawyerfootjob = True
scene sawyerstrip02b with dissolve
mc "* That's much better, I can totally see through this ..., it's like it's transparent. I like that Super-Power... *"
scene sawyerstrip03b with dissolve
mc "* Mmh, I'm starting to get a hardon... *"
scene sawyerstrip04b with dissolve
mc "* Ooh yeah, baby, take that bra off while I... adjust my hardening dong... *"
scene sawyerstrip05b with dissolve
mc "* Now we're talking! I'm gonna have a fast wank while she finishes... *"
scene sawyerstrip06b with dissolve
mc "* Just need a few more seco... *"
cs02 "I trust you didn't use your Super-Senses to w..."
stop music
scene sawyerstripendbad with dissolve
cs02 "What the hell! You DID use your Super-Vision you fucking PERVERT!"
scene sawyerprefoot01 with dissolve
mc "Err... Sorry, I couldn't help it... Your body... It's so HOT!"
cs02 "Is that so? Well, we can't go out with your giant cock sticking out like that for all to see. So I'm cancelling the mission for today."
scene sawyerprefoot00 with dissolve
play sound "sounds/dispatch.mp3"
cs02 "Chief Sawyer here. Tell Mrs Porker to come back tomorrow with apologies from the CCPD."
scene sawyerprefoot02 with dissolve
stop sound
cs02 "As for you... you deserve a PUNISHMENT for the crime of \"Misuse of Superpowers\"!"
mc "Uh oh..."
cs02 "Get on your knees and lick my feet!"
play channel1 "sounds/sexy03.mp3"
scene sawyerprefoot03 with dissolve
play sound "sounds/lick01.ogg"
cs02 "A bit higher now. While I tame that hard BEAST of yours..."
scene sawyerprefoot04 with dissolve
play sound "sounds/lick01.ogg"
cs02 "That's good... You like my fishnet stockings, don't you, naughty boy?"
mc "Yes, Captain Sawyer."
if age >= 20:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant young meat!"
if age >= 18 and age <= 19:
    cs02 "It's time to take the edge off your donkey-dick then. Lie against the sofa on the floor and let my FEET work that giant teeenage meat!"
show sawyerfootslowstart
play channel2 "sounds/wank.mp3"
scene sawyerfootslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
cs02 "Does this feel good on your trembling shaft, [hero]?"
mc "Oh yeah, fuck..."
window hide
pause
cs02 "Remove your hand and let me pump that fat shaft FASTER!"
scene sawyerfootfastvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "God, your feet... These stockings..."
window hide
pause
cs02 "You're gonna cum aren't you? You're gonna unload those bloated balls that are making you lose focus on your duties... Go on, DUMP YOUR YOUNG CREAM!" 
hide sawyerfootslowstart
scene sawyerfootcum01
with dissolve
cs02 "Ooh yeah, you're real close, you're spattering pre-cum all over the pl..."
scene sawyerfootcum02 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "AAAAH!"
window hide
with fastflash
cs02 "That's it, let it all out!"
scene sawyerfootcum03 with dissolve
cs02 "Look at the filthy mess you're making!"
window hide
with fastflash
mc "Ah, it's not my fault, AAAH!"
window hide
with fastflash
cs02 "YES IT IS! This is what happens when you MISUSE YOUR SUPERPOWERS!"
stop channel1
stop channel2
scene sawyerfootcum04 with dissolve
play sound "sounds/panting.mp3"
mc "Aaah... I came too much..."
cs02 "And now you're TIRED and USELESS. So much for that so-called Super-Studliness Captain MILF warned me about. My FEET defeated YOUR superpower!"
scene sawyerfootcum05 with dissolve
cs02 "So let this be a LESSON to you. Now get out of here and come back tomorrow when you're READY to tackle your mission PROPERLY!"
mc "Just give me a small break and I'll get another erection in no ti..."
cs02 "GET OUT OF MY OFFICE!"
jump Main

label Mision01Alley:
play music "sounds/covertmusic.mp3"
scene prealley01 with fade
so "It was right here... I remember it vividly."
cs02 "I'll go and look for clues in the neighborhood while you try and figure out what happened."
scene prealley02 with dissolve
mc "So, tell me Mrs Porker, how did it unfold?"
so "Well, Mister officer..."
mc "Call me [hero]."
scene prealley03 with dissolve
so "Well... Mister [hero]... they forced me against this filthy dumpster, like so..."
so "And then, one of them lifted my skirt...."
scene prealley04 with dissolve
mc "Like this?"
so "Yes Officer [hero]... And then, he pulled my panties aside with his rough hand...."
scene prealley05 with dissolve
mc "Keep going..."
so "Uuuh... He pushed two thick fingers between my moist pussylips..."
scene prealley06 with dissolve
so "...And then he wriggled them around..."
scene prealley07 with dissolve
play sound "sounds/moan01.mp3"
so "Aaah..."
scene prealley08 with dissolve
cs02 "What the hell are you doing?"
mc "Err, we were just re-enacting the scene. Standard procedures, right?"
scene prealley09 with dissolve
cs02 "And were you going to go as far as RAPE HER while you were at it?"
mc "Well, of course not, I mean, unless she asked for it..."
scene prealley10 with dissolve
so "Uuuh, are you going to just leave me like this? It feels like AWAM all over again..."
scene prealley09 with dissolve
cs02 "While you were fingering the victim, I found a clue."
cs02 "A notice was posted by the gang led by Samson Goldcock and states that this alley belongs to him. This means it was off-limits to anyone but members of his gang, the \"Narrows Bros\"."
mc "Oh yeah, that guy, he's in my blue folder. Then I shall confront him. Where does he live do you know?"
cs02 "Yes, the CCPD is aware of his current whereabouts. In a warehouse in Golden Row."
window hide
play sound "sounds/skill.mp3"
show locationstallion at poslocation
$ renpy.pause(0.5, hard=True)
$ locstallion = True
cs02 "But I ain't going with you, I... have other urgent business right now...."
scene prealley11 with dissolve
mc "Fine, I'll deal with him ON MY OWN."
scene prealley10 with dissolve
so "What about me?"
cs02 "Just pull your panties back up Mrs Porker. I'll give you a ride to the station."
stop music

label Stallion01:
scene stallionbase01 with fade
play music "sounds/stallionmusic.mp3"
show blackwigglevideo with moveinright
pause
mc "Hey, stop that, I need to interrogate Samson Goldcock!"
st "--. Let him through, girls. I want to know what this BO-AY is made of..."
hide blackwigglevideo with moveoutleft
stop music fadeout 1.0
scene stallion01 with dissolve
mc "Are you aware that an innocent wife and mother was raped TWICE in an alley that apparently belongs to YOU, Samson Goldcock?"
scene stallion02 with fastdissolve
st "--. Refer to me as \"The Stallion\". I've earned it. What's the name of that alley?"
mc "Rapists' Alley."
scene stallion03 with fastdissolve
st "--. Yeah, that belongs to ME. But my thugs have STRICT instructions to only MUG and NOT RAPE anybody."
mc "And they are clear on what you meant, Stallion?"
scene stallion02 with fastdissolve
st "--. Crystal."
mc "Could they have ignored your order?"
st "--. Ignored the order?"
mc "Or forgot it?"
scene stallion01 with fastdissolve
st "--. No."
mc "Could they have thought, \"the old man is wrong\"?"
scene stallion04 with fastdissolve
st "--. Ever been in a gang, son? We follow orders, son. Otherwise, people die. It's that simple, are we CLEAR?"
mc "Crystal."
mc "But... If your men always follow your orders, then why did Mrs Porker get raped walking down YOUR alley?"
scene stallion01 with fastdissolve
st "--. You snotty little bastard."
mc "Did you order a Code Red? Did you?"
scene stallion03 with fastdissolve
st "--. You want answers?"
mc "I want the truth!"
scene stallion04 with fastdissolve
st "--. You can't handle the TRUTH!"
window hide
pause
scene stallion02 with fastdissolve
st "--. You NEED me in the Narrows. I have more responsibility than you can fathom. \n---. Without me, the Narrows would fall into CHAOS!"
mc "DID YOU ORDER A CODE RED?"
scene stallion03 with fastdissolve
st "--. What's a \"Code Red\" anyway? Why do you keep talking about a \"Code Red\"???"
mc "Err..."
scene stallion04 with fastdissolve
st "--. You weep for Mrs Porker and curse my thugs, but her tragic rape saved other women. Do you get it, son?"
mc "I think so. I'm not sure. But about that Code R..."
scene stallion02 with fastdissolve
st "--. Get him out of here."
$ period += 1
scene sophiaoffice07 with fade
cs01 "So, did you get anything out of Samson Goldcock? Did he confess?"
mc "No, he didn't. I ALMOST got him to confess but he didn't fall for my provocative line of enquiry. It was a long shot anyway. But I have another idea."
scene sophiaoffice08 with dissolve
cs01 "What's that?"
mc "Use Mrs Porker as bait."
scene sophiaoffice06 with dissolve
so "Bait?"
mc "Yes, you walk down that alley tonight, looking all wifey and motherly, and I'll be watching from nearby, ready to pounce on those thugs when they start raping you!"
scene sophiaoffice05 with dissolve
so "So BEFORE they finish raping me? Did I get that right?"
mc "Well, yeah, obviously."
so " *sigh* "
scene sophiaoffice07 with dissolve
cs01 "I suppose it can be done. Hopefully, they'll be there again, like they were on both previous occasions. Let's head there straight away to set this up."

play channel1 "sounds/suspense.mp3"
scene alley01:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with fade
so "Are you there, Mr [hero]?"
scene alley02 with dissolve
mc "Yes, but don't call my name! Just walk and stay quiet. Look INNOCENT and WIFEY. Oh, and motherly too."
so "Alright, Officer [hero]."
scene alley03 with dissolve
mc "I hope they turn up..."
window hide
pause
scene alley04 with dissolve
th "Are you lost, ma'am?"
so "Me? err.. no, I'm fine, thanks for asking..."
scene alley05 with dissolve
th "Hey, you're that chick from the intro, aren't you? You must really have liked our nigga dicks to come back for more, didn't you?"
so "That's not true, I'm not like that! And don't you dare try and do something... naughty. This time, you'll regret it, I'm warning you!"
scene alley06 with dissolve
th "Oooh, I'm sssooo scared! Anyway, we won't. Just give us your bag, lady, cos we're still mugging you."
so "What, you're not going to rape me this time? Why not?"
scene alley07 with dissolve
th "I don't have all evening lady, give us your bag!"
so "Not if you won't even have the courtesy of raping me, I won't! What kind of lame thugs are you?"
th "Yo, this crazy bitch really wants it, I don't care about the Blue Code, the old man's wrong, let's rape her, she's literally begging for it!"
scene alley02 with dissolve
mc "AH! So they don't ALWAYS follow Stallion's orders after all. So much for gang discipline. I guess now is the time to intervene. Even if she IS begging for it."
scene alley08 with dissolve
mc "Hold it thugs, you're done for!"
th "Shit, let's make a run for it. Up the wall, Derek!"
scene alley09 with dissolve
mc "Come back, you cowards!"
so "They're escaping, do something, Mister [hero]!"
$ mission01win = True
$ mission01end = True
if mcagility >= 1:
    call screen usepower("useagility", "SophiaNoAgility", "SophiaAgility") with dissolve
if mccombat >= 1:
    $ maybecombat = True
    call screen usepower("usecombat", "SophiaNoAgility", "SophiaAgility") with dissolve

label SophiaNoAgility:
scene alley10 with dissolve
play sound "sounds/punch.mp3"
cw "Miaow!"
so "It's Catwoman!"
scene alley12 with dissolve
mc "I've got that one now, he won't escape this time!"
scene alley11 with dissolve
so "Yeah, thanks to Catwoman..."
scene alley13 with dissolve
play sound "sounds/punch.mp3"
so "Look at that cat ninja kick, she's just AMAZING!"
scene alley17 with dissolve
mc "And now I have them both! The Cockham League of Justice has prevailed!"
so "Again, thanks to Catwoman... She got both thugs while you just watched."
cs02 "I'll take it from here, you have successfully completed this mission. Thanks entirely to Catwoman."
window hide
play sound "sounds/winning.mp3"
show missionicon01 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
jump EndMission01

label SophiaAgility:
if maybecombat:
    $ usedcombat += 1
if maybecombat == False:
    $ usedagility += 1
scene alley15 with dissolve
play sound "sounds/thud.mp3"
mc "Got you!"
call Good from _call_Good_13
$ mission01dream = 1
pause
if mcagility >= 1:
    so "You're sssoo agile, Mister [hero]! But what about the other big bad thug?"
if mccombat >= 1:
    so "You're sssoo combative, Mister [hero]! But what about the other big bad thug?"
scene alley16 with dissolve
play sound "sounds/punch.mp3"
cw "Miaow!"
so "It's Catwoman!"
scene alley17 with dissolve
mc "Thanks to ME, the Cockham League of Justice has prevailed!"
so "And Catwoman, she got one the thugs actually."
cs02 "I'll take it from here, you have successfully completed this mission."
window hide
play sound "sounds/winning.mp3"
show missionicon01 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause

label EndMission01:
scene alley14 with dissolve
cs02 "Your days as Narrows Bros are over! You're going to give me the names of every other gang member when we get to the station, you hear me?"
th "I'll never talk, bitch!"
cs02 "Then I'll get your big friend to talk..."
th "He won't talk either, he doesn't even have a side sprite!"
cs02 "We'll see about that..."
scene alley18 with dissolve
so "Catwoman, I can't begin to express my gratitude for the amazing work you do around Cockham stopping nasty people from doing harm to innocent wives and mothers such as myself."
mc "Hi, I'm [hero] and I'm a superh..."
scene alley19 with dissolve
cw "This is nothing ma'am, all in a night's work for CATWOMAN. Now I must leave, DUTY CALLS! Also, I can smell some catnip nearby."
so "You go, girl!"
mc "Err, what about me?"
scene alley20 with dissolve
so "Goodbye Catwoman, you're my SUPERHEROINE!"
mc "Err, yeah, nice meeting you and all that."
scene sophiaprefuck01 with dissolve
so "I suppose I should thank you too, Mister Officer [hero]."
call screen usepower("useseduction", "SophiaNoSeduction", "SophiaSeduction") with dissolve

label SophiaNoSeduction:
scene sophiabadend01 with dissolve
so "Hang on, where's my necklace? Someone STOLE IT!"
mc "Ah. It must have been Catwoman, she's a known jewelry thief. Didn't see her do it, she really has skills."
so "Well DO SOMETHING! Fly after her, BRING ME BACK MY NECKLACE!"
mc "Err... I can't fly, Mrs Porker."
scene sophiabadend02 with dissolve
so "This evening has been a COMPLETE DISASTER! I didn't even get raped and I lost my necklace! I'm going home! ALONE. Walking. Down badly-lit alleys."
mc "Are you sure this is sa..."
so "You are USELESS, Mister [hero]!"
mc "Wow, that didn't go down well at all..."
menu:
    "Be resentful for her lack of gratitude (+1 Super-Villain)":
        mc "* Ungrateful bitch... *"
        call Evil from _call_Evil_17
        $ mission01dream = 2        
        pause
        pass
    "She's just upset after all she's been through (no change)":
        mc "* I did my job and I did it WELL. *"
        pass
jump Main

label SophiaSeduction:
$ usedseduction += 1
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play channel1 "sounds/sexy02.mp3"
mc "You can call me [name]... Sophia."
so "Ooh, well thank you then... [name]."
scene sophiaprefuck02 with dissolve
so "Now where were we in this re-enactement?"
mc "I was fingering your pussy if I remember correctly."
scene sophiaprefuck03 with dissolve
so "Ah yes. Let me get into position then. So we can do this re-enactement properly. I'll take my panties off for you, since I don't want them ripped off like when I was raped."
scene sophiaprefuck04 with dissolve
mc "Yes, that would be a shame."
scene sophiaprefuck05 with dissolve
so "One of the thugs pulled his great big cock and started slapping my arse with it."
scene sophiaprefuck06 with dissolve
mc "I see, did he leave a bruise on it?"
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
so "AAh, y.. yes, but his dong was not as HEAVY and POWERFUL as yours... [name]..."
scene sophiaprefuck06 with dissolve
mc "So I won't slap you TOO hard then."
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
scene sophiaprefuck06 with fastdissolve
$ renpy.pause(0.5, hard='True')
scene sophiaprefuck07 with fastdissolve
play sound "sounds/thud.mp3"
$ renpy.pause(0.8, hard='True')
so "Mmmh, the sound of your fat donkey-dick slapping against my slutty buttocks is making me so wet..."
if age >= 20:
    so "Please stick your massive pud inside me, [name]!"
if age >= 18 and age <=19:
    so "Please stick your massive teenage pud inside me, [name]!"
scene sophiaprefuck08 with fastdissolve
mc "Let's see if it will fit first... Your pussy looks VERY tight."
so "That's because it's never been STRETCHED by my pindick hubby... Just PUSH IT IN, I can take it, Officer [hero]!"
play sound "sounds/whoosh.mp3"
scene sophiaprefuck09 with fastdissolve
mc "Damn, your pussy really wanted that dick..."
so "Yes it did, Mister Officer [hero]... Now fuck me nice and slow with your giant boycock."
play channel2 "sounds/womansex01.mp3"
show sophiaslowvideo with dissolve
window hide
$ renpy.pause(3.0, hard='True')
mc "Like that? You like that Sophia?"
so "Mmh, yes, it feels so good..."
window hide
pause
so "Please... AAAAH, give it to me like a SUPER-STUD!"
mc "You want all 15 inches pounding inside of you?"
so "YY... YES [hero]!"
mc "Beg for it!"
if age >= 20:
    so "Please POUND ME WITH YOUR FIFTEEN INCHES OF MONSTER MEAT!"
if age >= 18 and age <= 19:
    so "Please POUND ME WITH YOUR FIFTEEN INCHES OF TEENAGE MONSTER MEAT!"
stop channel2
play channel2 "sounds/pounding.ogg"
show sophiafastvideo with dissolve
pause
so "Are you going to pump my pussy full of yummy cum? Like that thug did...?"
mc "I'm gonna WHITEWASH his load with mine, Mrs Porker!"
$ renpy.pause(2.0, hard='True')
stop channel2
scene sophiafuckcum01 with dissolve
play music "sounds/splooge02.mp3"
mc "AAAH, here it comes!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
so "Oooh, your monster shots are making me cum too!"
scene sophiafuckcum02 with dissolve
so "You're cumming so much!"
window hide
with fastflash
mc "That's cos I'm a SUPER-CUMMER! RHAAA!"
scene sophiafuckcum03 with dissolve
mc "Take some more young spunk, DEEP inside your womb!"
window hide
with fastflash
so "Oooh, Mister [hero], I'm BLOATED with your scalding cream!"
stop music
play music "sounds/boyorgasm01.mp3"
scene sophiafuckcum04 with dissolve
mc "Then I'l come the rest all over your back, RHOAR!"
window hide
with fastflash
so "AAAH!... Your shots are so HOT and POWERFUL, [name]!"
scene sophiafuckcum05 with dissolve
if age >= 20:
    so "My pussy is DRIPPING with your load and you're STILL blasting?"
if age >= 18 and age <= 19:
    so "My pussy is DRIPPING with your teenage load and you're STILL blasting?"
window hide
with fastflash
mc "Fuck yeah! Take those final shots Sophia, AAAH!"
window hide
with fastflash
so "So ssooo much young cum!"
stop music
scene sophiafuckcum06 with fade
play sound "sounds/panting.mp3"
so "You... came more than my husband in ALL our years of marriage... Oooh, how am I going to explain all that smelly spunk on me when I get home?"
stop channel1
scene sophiafuckcum07 with dissolve
so "Wait. What?... Where's my necklace? SOMEONE STOLE MY GOLD NECKLACE!"
mc "Must have been Catwoman, she does that kind of stuff. Didn't see her do it though, she's damn fast."
so "Well DO SOMETHING! Fly after her, BRING ME BACK MY NECKLACE!"
mc "Err... I can't fly, Mrs Porker."
scene sophiafuckcum08 with dissolve
so "This evening has been a COMPLETE DISASTER! I didn't even get raped and I lost my necklace! I'm going home! ALONE. Walking. Down badly-lit alleys."
mc "Are you sure this is sa..."
so "You are USELESS, Mister [hero]!"
mc "Wow, that didn't go down well at all..."
menu:
    "Be resentful for her lack of gratitude (+1 Super-Villain)":
        mc "* Ungrateful bitch. I hate the people of this stinky town... *"
        call Evil from _call_Evil_18
        $ mission01dream = 2
        pause
        pass
    "She's just upset after all she's been through (no change)":
        mc "* I did my SUPERHERO job and I did it WELL. *"
        pass
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
    
label Mission02:
play music "sounds/ccpdoffice.mp3"
scene ccpd01
show ccpd01back
with fade
show sawyer01 at midright with moveinright
cs01 "Ah, it's you. I was wondering who Captain MILF was going to send."
mc "Yep, it's me. The superhero with all the lame missions."
hide sawyer01
show sawyer04 at midright
with fastdissolve
cs01 "This mission isn't lame. It's ESSENTIAL. Sexy Luthor is a criminal mastermind of the WORST KIND."
mc "Well, she's gonna escape anyway, so what's the point?"
hide sawyer04
show sawyer02 at midright
with fastdissolve
cs01 "Not THIS time. We have built a special telephatic wave-proof cell to stop her from using her Super-Seduction powers."
hide sawyer02
show sawyer03 at midright
with fastdissolve
cs01 "And I am assigning you an assistant to make sure you don't have to deal with Sexy Luthor directly."
window hide
show dani01 at left with moveinleft
da "Ready to report for duty, Captain Sawyer!"
cs01 "Sergeant Dani here will be the only one allowed in the cell so YOU can stay out and make sure Sexy Luthor doesn't escape."
mc "What if she's seduced by Sexy Luthor?"
hide dani01
show dani02 at left
with fastdissolve
da "Yes, what if that happens Captain? What are my orders?"
hide sawyer03
show sawyer06 at midright
with fastdissolve
cs01 "[hero] here is meant to stop this from happening. He knows what to do, he's a superhero."
mc "I do? I mean, I am, but..."
hide sawyer06
show sawyer04 at midright
with fastdissolve
cs01 "Just keep the prisoner safe in her cell until the morning and her transfer to Arkham. Dismissed."
hide dani02
show dani01 at left
with fastdissolve
da "Aye aye, Captain!"
window hide
hide sawyer04 with moveoutright
$ mission02 = True
window hide
play sound "sounds/achievement.mp3"
show missionicon02 at poslocation
$ renpy.pause(0.5, hard=True)
show textmission02 at posmissiontext
pause
hide dani01
show dani03 at left
with fastdissolve
da "I guess it's just you and me against Sexy Luthor now, [hero]. Come, I'll take you to her special cell."
stop music
play music "sounds/covertmusic.mp3"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
$ period = 1
scene luthorcase01 with dissolve
da "This way, [hero]... Her cell is behind that heavy door."
scene luthorcase02 with dissolve
da "Are you ready to meet her?"
mc "Yes, she doesn't scare me one bit. I'm a SUPERHERO."
da "I'm glad to be assigned with YOU, [hero]..."
scene luthorcase03 with dissolve
da "First, I'll hand you the key to her cell door. And I'll keep the keys to her handcuffs."
mc "Is that her in there?"
da "Yes, if you wish to talk to her, there's the visitor's bay on your left."
scene luthorcase04 with dissolve
mc "Ah, there she is. Cockham's most notorious Super-Villain. A criminal mastermind of the worst kind. Been caught again by Superman, Sexy Luthor?"
lu "A small hiccup, nothing to worry about. But I see the League doesn't trust the CCPD anymore. How times have changed..."
da "Just some EXTRA security to make sure you won't escape this time, Sexy Luthor!"
scene luthorcase05 with dissolve
lu "What does [hero] here think about this lousy assignment? He should be on the streets fighting sex crime, should he not?"
mc "Err..."
lu "The sooner I escape, the sooner you'll be able to go back to your proper superhero duties, [hero]..."
mc "Don't try and..."
da "Don't listen to her. It's dinner time anyway, I'll bring her her food, that should shut her up."
mc "Alright, I'll stay here to make sure nothing happens."
scene luthorcase06 with dissolve
mc "Ooh, pizza? Can I get some?"
scene luthorcase07 with dissolve
da "Dinner is served. I'll remove your handcuffs but don't turn around until I've left the cell."
lu "My pizza might get cold..."
scene luthorcase08 with dissolve
mc "I think you should hurry up, Sergeant, she's standing up..."
da "What, but I told her to..."
mc "Quick, let me get the door for you!"
scene luthorcase09:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
play sound "sounds/radiation02.mp3"
lu "Dani, why don't you share that lovely pizza with me?..."
da "What? Oh, thanks for offering, I'm starving!"
mc "It's a ruse, GET OUT OF THERE RIGHT NOW!"
scene luthorcase10 with dissolve
stop sound
lu "I think we would be more comfortable WITHOUT clothes, don't you agree, Dani?"
da "Y...Yes, I agree. Let me take my skirt off. And my shirt."
mc "Uh oh, full lesbian seduction ahead..."
stop music
play music "sounds/sexy04.mp3"
scene luthorcase11 with dissolve
lu "Now, Dani. I have something that I would like you to taste for me... Something much TASTIER than that pizza..."
da "What is it?"
lu "MY PUSSY!"
scene luthorcase12 with dissolve
lu "Enjoying the show, [hero]? Why don't you join us?"
mc "I'm not falling for your tricks, Sexy Luthor!"
lu "Too bad, your loss... Dani here is going to really ENJOY herself, I can guarantee that!"
scene luthorcase13 with dissolve
lu "You'll see, Dani, it's the tastiest pussy in town!"
mc "Damn, what should I do? Except watch obviously... And think later."
play channel1 "sounds/lick01.ogg"
play channel2 "sounds/moan02.mp3"
scene luthorlickcasevideo with dissolve
pause
mc "Make her cum with your tongue, Dani! She might get tired..."
pause
scene luthorcasepostlick01 with dissolve
lu "Right there, just right... th..."
scene luthorcasepostlick02 with dissolve
stop channel1
play sound "sounds/splooge02.mp3"
lu "AAAH, I'm CUMMING!"
window hide
with fastflash
mc "Great, you did it, Dani!"
scene luthorcasepostlick03 with dissolve
stop channel2
play sound "sounds/womancum01.mp3"
lu "UUUUUHH!!!!"
window hide
with fastflash
mc "You've had your fun, now let her go, Sexy Luthor! Plus, your pizza is getting cold. And it does look yummy."
scene luthorcase14 with dissolve
stop sound
lu "Oh, I'm FAR from done, [hero]... You can't stop me, I'm going to FUCK HER TO DEATH!"
mc "I can't let you do that!"
lu "Oh well, I guess you'll just have to enter my cell and try and stop me then..."
mc "Damn you, Sexy Luthor, DAMN YOUR EVIL GENIUS!"
scene luthorcase15 with dissolve
play sound "sounds/moan02.mp3"
lu "Oh yeah, keep going, lick my cunt until you PASS OUT!"
scene luthorcase16 with dissolve
mc "That's it, I have to intervene or poor Sergeant Dani will turn into a pussy-licking zombie!"
scene luthorcase17 with dissolve
play sound "sounds/radiation02.mp3"
lu "Why don't you join us, [hero]? I'm sure you want some of THAT pussy too, don't you?"
mc "Y...Yes, YES I WANT THAT SEXY PUSSY!"
stop sound
scene luthorcase18 with dissolve
lu "Then get your cock HARD, I want to see if the rumors are true..." 
scene luthorcase19 with dissolve
if age >= 20:
    lu "I don't need you anymore, Dani, let me handle that MONSTERCOCK on my own... For STARTERS!"
if age >= 18 and age <= 19:
    lu "I don't need you anymore, Dani, let me handle that teenage MONSTERCOCK on my own... For STARTERS!"
scene luthorcase20 with dissolve
lu "Are you ready to handle MY PUSSY, [hero]?"
mc "Of course, Sexy Luthor, anything for YOU!"
lu "Then get on your knees and show me how you worship it."
scene luthorcase21 with dissolve
play sound "sounds/lick01.ogg"
lu "That's nice... You're a natural, despite your age... Let's see how expert your giant cock is now!"
scene luthorcase22 with dissolve
lu "Damn boy, I've never felt such a heavy piece of equipment..."
scene luthorcase23 with dissolve
play sound "sounds/womangroan.mp3"
lu "But Sexy Luthor is up to the challenge! I'm going to FUCK this dong into OBLIVION!"
play channel1 "sounds/womansex02.mp3"
window hide

label LuthorCaseFuck:
hide cum
hide nexticon
hide zoomicon
show luthorfuckcasevideo behind luthorfuckcasepussyvideo
$ renpy.pause(1.0, hard='True')
hide luthorfuckcasepussyvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show zoomicon:
     xpos 50 ypos 500     
call screen luthorfuck01()
screen luthorfuck01():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuckPussy")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEnd")

label LuthorCaseFuckPussy:
hide cum
hide nexticon
hide zoomicon
show luthorfuckcasepussyvideo behind luthorfuckcasevideo
$ renpy.pause(1.0, hard='True')
hide luthorfuckcasevideo with dissolve
lu "Yeah, WORK that pussy!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 1700 ypos 500     
call screen luthorfuck02()
screen luthorfuck02():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LuthorCaseFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LuthorCaseFuckEnd")

label LuthorCaseFuckEnd:
hide sceneicon
hide nexticon
hide zoomicon
lu "* puff * Still going, stud? But I can feel that you're getting close, aren't you?"
window hide
pause
mc "Uuuh, your sexy pussy is gripping me so tight..."
lu "I'm gonna PUMP you DRY!"
scene luthorcasefuckcum01 with dissolve
hide luthorfuckcasevideo
hide luthorfuckcasepussyvideo
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
mc "And I'm gonna pump you FULL! RHAAA!"
window hide
with fastflash
lu "A challenge, boy?"
scene luthorcasefuckcum02 with dissolve
stop channel1
play sound "sounds/thud.mp3"
lu "Here, challenge THAT!"
window hide
with fastflash
play channel1 "sounds/splooge02.mp3"
mc "Oh FUCK, AAAH!"
scene luthorcasefuckcum03 with dissolve
stop sound
play sound "sounds/boymoan02.mp3"
lu "You're BLOATING my insides with your MASSIVE pellets of young cum!"
window hide
with fastflash
mc "I cum a lot... I'm a SEX SUPERHERO!"
stop channel1
scene luthorcasefuckcum04 with dissolve
lu "I can't believe you're STILL spewing such FAT WADS!"
window hide
with fastflash
mc "Your sexy pussy is making cum non-stop, AAH!"
scene luthorcase25 with dissolve
stop sound
stop channel1
play sound "sounds/panting.mp3"
lu "Finally... You are true to your reputation, [hero]. What a cock... And it looks like it's still raring to go?"
mc "Yeah, SEXY PUSSY. NEED MORE SEXY PUSSY!"
lu "Well, I would love to hang around and have some fun all together, but I need to go... But why don't you two stay behind and get to know each other better?"
da "Uuh, his cock is sssooo BIG!"
lu "That's right, his cock is enormous, you want it, don't you? [hero], come and pick her up and show her what a STUD you are! While I get dressed..."
scene luthorcase26 with dissolve
lu "That's good, [hero], I'm sure you'll have a GOOD time with her. Fucking her up her tight ass!"
scene luthorcase27 with dissolve
da "Up my ass? But... His cock is too big for that!"
lu "Don't worry Dani, YOU will enjoy it too!"
scene luthorcase28 with dissolve
lu "Make her nice and wet [hero], she's going to need it..."
play sound "sounds/moan02.mp3"
scene luthorcase29 with dissolve
play sound "sounds/radiation02.mp3"
lu "And now I'll make sure that you'll be so taken by your lovemaking that you won't bother raising the alarm for a while..."
stop sound
lu "I think I'll take the key with me, just in case... Cheerio!"
scene luthorcase30 with dissolve
play sound "sounds/moan01.mp3"
da "Please fuck me in the ass, I NEED that HUGE COCK IN ME!"
mc "Alright, I'm going to POUND you against the cell wall!"
window hide
play channel1 "sounds/danimassive.mp3"
scene luthordanianalslowvideo with dissolve
da "Your cock is so MASSIVE! It's the BIGGEST bulldick I ever had!"
window hide
pause
da "What's going on? Hey, stop fucking me, she's gone and her Super-Seduction powers aren't active anymore!"
window hide
menu:
    "Keep going (use Super-Studliness, +1 Super-Villain)":
        mc "No way, I'm enjoying myself too much! And I'll make YOU enjoy yourself too!"
        $ danistudliness = True    
        if age >= 20:
            da "This young monster dong is so GOOD! Please fuck me senseless, fuck me till I cream all over your giant cunt-splitter!"
        if age >= 18 and age <= 19:
            da "This monster teenage dong is so GOOD! Please fuck me senseless, fuck me till I cream all over your giant cunt-splitter!"
        call Evil from _call_Evil_19
        mc "Get ready for some HEAVY POUNDING, Dani!"    
        hide supervillain
        jump DaniAnalFastFuck        
    "Stop fucking her (no change)":
        mc "Damn, I was just about to blow..."
        da "Since she locked us out, cum quick inside my ass, I have a key double hidden in there!"
        mc "Alright!"
        jump DaniAnalSlowFuck
        
label DaniAnalSlowFuck:
window hide
hide cum
hide faster
hide slower
play channel1 "sounds/danimassive.mp3"
show luthordanianalslowvideo behind luthordanianalfastvideo
$ renpy.pause(1.0, hard='True')
hide luthordanianalfastvideo with dissolve
pause
if danistudliness:
    da "Your cock is so HUGE! It's the BIGGEST bulldick I ever had!"
if danistudliness == False:
    da "Hurry up [name], we need to get that key!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
call screen luthordanianalslow()
screen luthordanianalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalFastFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEnd")

label DaniAnalFastFuck:
window hide
hide cum
hide faster
hide slower
play channel1 "sounds/danimassive.mp3"
show luthordanianalfastvideo behind luthordanianalslowvideo
$ renpy.pause(1.0, hard='True')
hide luthordanianalslowvideo with dissolve
pause
stop channel1
play channel1 "sounds/womansex01.mp3"
pause
if danistudliness:
    da "Oh my God, you're going so DEEP!"
if danistudliness == False:
    da "Why are you fucking me so HARD? Just blow your load already!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     
call screen luthordanianalfast()
screen luthordanianalfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("DaniAnalSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("DaniAnalFuckEnd")

label DaniAnalFuckEnd:
hide slower
hide cum
hide faster
if danistudliness:
    da "You're making me CUM NON-STOP!"
    mc "I'm about to bust my nut too..."
if danistudliness == False:
    da "Are you finally going to cum? Please do it quickly!"
scene danianalcum01 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
if danistudliness:
    da "I'm gonna CREAM all over that gigantic discharging DONG!"
if danistudliness == False:
    da "Try and come a LOT!"
window hide
with fastflash
if danistudliness:
    mc "Get ready for more of MY cream too!"
if danistudliness == False:
    mc "I AM, RHAAA!"
scene danianalcum02 with dissolve
da "More, MORE CUM!"
window hide
with fastflash
mc "You want some more, here's some MORE, AAAH!"
scene danianalcum03 with dissolve
stop channel1
play sound "sounds/moan03.mp3"
da "I'm just leaking your slimy scum out of my battered butthole... Uuuh..."
mc "Yeah, sorry about that, got carried away a bit. After all, I'm a Super-Hero."
stop music
scene luthorcase31 with dissolve
stop sound
if danistudliness:
    mc "We're locked in!"
    da "Quick, help me search for the key then!"
    mc "What key? I thought I was the one who had it and she took it with her!"
    scene luthorcase32 with dissolve
    da "No, I...kept a double in my ass just in case. It must have been expelled while you were pumping your slimy seed inside my butthole..."
    mc "Well, good thing I pummeled your ass and not your pus..."
    da "Ah, there it is!"
    mc "Oh, cool, open the door then and radio in that she escaped."
    scene luthorcase33 with dissolve
    play sound "sounds/dispatch.mp3"
    mc "In the meantime, I'm going to take these handcuffs with me. I need them to fill up my inventory..."
    window hide
    $ inventoryhandcuffs = True
    play sound "sounds/achievement.mp3"
    show acquiredhandcuffs at poslocation
    $ renpy.pause(0.5, hard='True')
    pause    
    scene luthorcase34 with dissolve
    da "It's too late! She... escaped... We failed miserably. And now we have to report to Captain Sawyer... * sniff * This is all YOUR fault!"
    $ mission02fail = True
    jump Mission02Debrief

if danistudliness == False:
    mc "We're locked in!"
    da "Quick, help me search for the key then!"
    mc "What key? I thought I was the one who had it and she took it with her!"
    scene luthorcase32 with dissolve
    da "No, I...kept a double in my ass just in case. It must have been expelled while you were pumping your slimy seed inside my butthole..."
    mc "Well, good thing I pummeled your ass and not your pus..."
    da "Ah, there it is!"
    mc "Oh, cool, open the door then and radio in that she escaped."
    scene luthorcase33 with dissolve
    play sound "sounds/dispatch.mp3"
    mc "In the meantime, I'm going to take these handcuffs with me. I need them to fill up my inventory..."
    window hide
    $ inventoryhandcuffs = True
    play sound "sounds/achievement.mp3"
    show acquiredhandcuffs at poslocation
    $ renpy.pause(0.5, hard='True')
    pause
    $ mission02win = True
    scene luthorcase34 with dissolve
    da "Hopefully, we were fast enough to alert the CCPD compound that Sexy Luthor was trying to escape... We have to go and report to Captain Sawyer now..."    
    jump Mission02Debrief

label Mission02Debrief:
$ mission02end = True
stop channel1
stop channel2
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
play music "sounds/ccpdoffice.mp3"
scene ccpd01
show ccpd01back
with fade
show sawyer01 at midright
with dissolve
show dani01 at left with moveinleft
if mission02fail:
    cs01 "What happened?"
    da "We... were both seduced. And [hero] took too long to cum in my ass for me to retrieve the extra key in time."
    mc "Hey! I was Super-Seduced against my will, remember?"
    hide sawyer01
    show sawyer04 at midright
    with fastdissolve
    cs01 "Next time, I'll make sure the League sends us a PROPER Superhero, one who doesn't get seduced so easily. You are dismissed!"
    play sound "sounds/losing.mp3"
    show missionicon02 at poslocation
    $ renpy.pause(0.5, hard='True')
    show failicon at poswin
    pause
    mc "What, I failed?"
    hide missionicon02
    hide failicon
    hide sawyer04
    show sawyer06 at midright
    with fastdissolve
    cs01 "And I am re-assigning YOU, Sergeant Dani. To a DESKJOB!"
    hide dani01
    show dani02 at left
    with fastdissolve    
    da "That's not fair, I did everything I was supposed to do... * sniff *"
    jump Main

if mission02win:
    cs01 "It was a close call, but we managed to catch Sexy Luthor before she could escape from CCPD grounds and she's being transferred to Arkham as we speak."
    window hide
    play sound "sounds/winning.mp3"
    show missionicon02 at poslocation
    $ renpy.pause(0.5, hard='True')
    show winicon at poswin
    pause
    mc "All thanks to me and my giant cumloads."
    hide missionicon02
    hide winicon
    hide sawyer01
    show sawyer06 at midright
    with fastdissolve
    cs01 "What is your report, Sergeant Dani? Why is [hero] mentioning the size of his cumloads exactly?"
    hide dani01
    show dani02 at left
    with fastdissolve    
    da "Well, err... I had to use the extra key to get out. And I managed to expel it when [hero] bloated my ass with his seed."
    mc "Yeah, quick thinking there, Sergeant, well done. You were an essential part of the pl..."
    hide sawyer06
    show sawyer05 at midright
    with fastdissolve
    cs01 "I don't want to even begin to imagine what the hell happened in that cell. Go back to your compound [hero]."
    hide sawyer05
    show sawyer06 at midright
    with fastdissolve
    cs01 "And Sergeant Dani, write me a FULL REPORT. DISMISSED!"
    jump Main

label PorkherBeat:
play music "sounds/covertmusic.mp3"
if lpspeakhq01 and locquiff == False:
    jump LollyCat
if lpspeakhq01 == False:
    jump PorkherBeatNothing
if lpspeakhq01 and locquiff:
    jump PorkherBeatNothing02

label LollyCat:
scene beatporkher01 with fade
cs02 "This is the main road in Porkher's Row. Hang on, this little girl seems to be in distress."
scene beatporkher02
show lolly01
with dissolve
lo "* sob * My pussy. My little pussy. Cat."
cs02 "What's wrong, little girl? Can we help you?"
hide lolly01
show lolly05
with fastdissolve
lo "* sob *. My... little... * sob * pussy. cat. is up in the tree. And he's all wet and cold."
mc "I'm not gonna let Catwoman steal the spotlight from me this time! I'll get this cat down!"
cs02 "Don't you worry, [hero] will save the day. What's your name?"
hide lolly05
show lolly02
with fastdissolve
lo "Lolly. Lolly Kohn. Is this... boy going to rescue my pussy?"
mc "Yes, I will!"
lo "Yippee! Please take good care of my wet pussy!"
scene beatporkher03 with dissolve
mc "* What should I do to get that damn pussycat down? *"
scene beatporkhercat01 with dissolve
mc "This is pretty high already and that stupid cat is even higher up in the tree..."
if mcagility >= 1:
    call screen usepower("useagility", "CatNoAgility", "CatAgility") with dissolve

label CatNoAgility:
scene beatporkhercat02 with dissolve
play sound "sounds/meow.mp3"
mc "Oh no, I'm gonna fall..."
scene beatporkher02
show lolly06
with dissolve
lo "Where's my pussy?"
mc "Err, still up in the tree. My agility is not high enough."
hide lolly06
show lolly01
with fastdissolve
lo "But... You promised you would save my pussy... * sob *"
cs02 "Let me call the fire brigade for you little girl, they'll rescue your cat. Unlike [hero] here..."
hide lolly01
show lolly03
with fastdissolve
lo "That's what I wanted in the first place. A hot fireman with a really BIG hose."
mc "Right. I get it. This is bait."
hide lolly03
show lolly02
with fastdissolve
lo "Hey, mister boy. You might want to come back around here when you have better agility. My pussy LOVES to get stuck up fat poles all the time."
mc "Yep. Definitely bait. But a hint to come back here when my agility is higher cos there's more to her pussy than meets the eye."
scene beatporkher04 with dissolve
cs02 "Well, we've wasted enough time here with your NON-Superpowers. And there's no criminal activity going on in these parts as far as I can tell. Let's head back."
mc "Sure, you to the CCPD. And me to the my compound."
jump Main

label CatAgility:
scene beatporkhercat03 with dissolve
play sound "sounds/meow.mp3"
mc "I got you!"
lo "Bring him down, bring him down! Leave my pussy alone!"
scene beatporkher02
show lollycat01
with dissolve
lo "Come here, Sylvester. Let me hold you in my arms."
hide lollycat01
show lollycat02
with fastdissolve
play sound "sounds/meow.mp3"
lo "I LOVE stroking my soft pussy."
mc "Yeah, okay. I think your parents need to..."
hide lollycat02
show lollycat04
with fastdissolve
lo "Are you a clown? Is the circus in town?"
mc "No, why are you asking?"
lo "Cos you stuffed a banana in your funny thong. That's what clowns do."
mc "Well, err, actually..."
hide lollycat04
show lollycat03
with fastdissolve
lo "And I saw another clown. A crazy woman with blue hair. And big tits."
cs02 "Oh really? Could you tell us where this \"clown lady\" went, little girl?"
hide lollycat03
show lolly04
with fastdissolve
lo "What's in it for me?"
mc "Hey, I just shaved your pussy! Err, I mean I saved your CAT!"
hide lolly04
show lolly06
with fastdissolve
lo "Oh yeah, but I wanted a nice hot fireman to do it, not a clown."
mc "This girl is starting to..."
cs02 "Listen, Lolly, if you tell me where the clown lady went, I promise next time, I'll send the hottest hunk of a fireman to save your cat."
hide lolly06
show lolly03
with fastdissolve
lo "Really? One with a really BIG hose?"
cs02 "Ehm, sure, sure, why not."
hide lolly03
show lolly05
with fastdissolve
lo "She went in that old warehouse building over there. I can hear her scream at night when she's practicing her clown routine."
window hide
play sound "sounds/skill.mp3"
show locationquiff at poslocation
$ renpy.pause(1.0, hard=True)
$ locquiff = True
hide lolly05
show lolly02
with fastdissolve
lo "So where's the circus? I like poneys. Cos they have massive..."
mc "That's bait. That's definitely bait."                                                                        
lo "...manes."
scene beatporkher04 with dissolve
cs02 "Well, now we know where Harley Quiff hangs out. See, going on the beat can bring valuable intel in a town like Cockham."
jump Main

label PorkherBeatNothing:
scene beatporkherempty:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with fade
cs02 "Uhm, this place is totally deserted."
mc "It's a working-class area if I'm not mistaken. People must be at work."
scene beatporkher04 with dissolve
cs02 "Either that or we're missing something. Meaning YOU're missing something."
mc "Like what?"
cs02 "I'm not sure. Perhaps you should have gotten a hint from someone to unlock this area..."
mc "Like from whom?"
scene beatporkher05 with dissolve
cs02 "THINK HARD! WHO gives hints, apart from me?"
mc "AAAH, I get it. Lois Pane...."
cs02 "No need to hang around here, this place will remain empty until you get that HINT."
jump Main

label PorkherBeatNothing02:
scene beatporkherempty:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with fade
cs02 "Now that you saved that pussy. cat, this place has become totally deserted."
mc "It's a working-class area if I'm not mistaken. People must be at work. And Lolly must be at the circus."
scene beatporkher04 with dissolve
cs02 "I guess so. So why are we here?"
mc "I CHOSE this area. And I'm the superhero here!"
cs02 " * snickers * Yeah, well, we've just wasted valuable police time. So I'm going back to the office and I'll drop you off at the seaport."
jump Main
label BarrBeat:
play music "sounds/covertmusic.mp3"
scene beatbarr00 with dissolve 
if seenbeatbarr == False:
    jump SeenBeatBarrNo
if seenbeatbarr:
    jump SeenBeatBarr
label SeenBeatBarrNo:
$ seenbeatbarr = True
cs02 "Let's head over to that corner, Homeless people tend to congregate around here and they can be a valuable source of information. Sometimes."
scene beatbarr01 with dissolve    
hb "Can you spare some change for an old man?"
mc "I'm sorry, I don't carry money. Actually, I have no money at all even back in my superhero compound."
scene beatbarr02 with dissolve    
hb "* mumbles * Bloody superheroes. Cost a fortune to the taxpayer..."
cs02 "Have you seen any suspicious individuals around the borough lately?"
scene beatbarr03 with dissolve    
hb "Let me think. While I scratch my balls. Yeah. YOU! HA HA HA!"
cs02 "I don't think we'll get anything out this drunken hobo..."
scene beatbarr04 with dissolve    
hb "Hey, hang on, I did. I saw some aliens. Landed right here. Woke me up in the middle of the night and gave me the fright of my life..."
cs02 "Yeah, sure. Let's go, [hero]."
mc "Take care of yourself, sir."
scene beatbarr05 with dissolve    
hb "I don't need no superhero to take care of myself, son! And you'd better watch out for those aliens."
jump Main

label SeenBeatBarr:
cs02 "Let's see if this drunken hobo has sobered up."
scene beatbarr04 with dissolve    
hb "The end is nigh! The aliens are coming! Watch your butts!"
mc "Apparently not."
scene beatbarr05 with dissolve 
hb "They won't get ME! I've stuck a padlock on my anus!"
cs02 "* sigh * OK, this is a waste of time. Let's go back to the CCPD. And you to your superhero compound."
jump Main

label CockhamBeat:
play music "sounds/covertmusic.mp3"
scene beatoldcockham01 with dissolve
cs02 "We're in the inner city area of Old Cockham. A high crime area. Be on the lookout."
mc "All I see are chrome-colored people playing basketball, Captain Sawyer."
scene beatoldcockham02 with dissolve
cs02 "Well, okay, it's the middle of the day, criminal activity takes place mostly at night."
scene beatoldcockham03 with dissolve
cs02 "Then, those same players would be dealing chromium, a potent new drug that just hit the market, I can guarantee you!"
mc "I see. Never trust tall basketball players then. I'm short, so I don't like them."
scene beatoldcockham02 with dissolve
cs02 "I heard that one day, you might end up taller than them..."
mc "Possibly, when I reach Level 3. But we're far from that at this stage."
scene beatoldcockham04 with dissolve
cs02 "I guess we've shown our presence. It's important to show criminals that we are ready to FACE them at any time of the day or night."
mc "Yeah, face them head on..."
scene beatoldcockham02 with dissolve
cs02 "I'll go back to the CCPD, I'll give you a ride to the seaport so you can catch the speedboat across to your compound. Since you can't fly."
jump Main

label Mission04:
stop music
scene ccpd01
show ccpd01back
with fade
play music "sounds/ccpdoffice.mp3"

show sawyereyeblink at centerleft with dissolve
cs01 "Ah, I'm glad you came, [hero]. We have a strange case on our hands."
mc "* sigh * Are they ever normal?"
hide sawyereyeblink
show sawyer04 at centerleft
with fastdissolve
cs01 "This is IMPORTANT! Cockham Grand Hospital reports an unusually high number of patients coming in with traumatic anal injuries recently..."
mc "I'm not interested in pulling gerbils out of people's asses."
hide sawyer04
show sawyer02 at centerleft
with fastdissolve
cs01 "I'm afraid it goes deeper than that."
mc "Eew..."
hide sawyer02
show sawyer05 at centerleft
with fastdissolve
cs01 "I mean, it's not gerbil-related. Or hamster-related. Nothing was found in their rectums."
mc "Uh oh..."
cs01 "And another thing they all have in common is memory loss. They are unable to explain what happened to them."
mc "Come on! You're not going to fall for that, are you? People never admit to sticking things up their asses!"
hide sawyer05
show sawyereyeblink at centerleft
with fastdissolve
cs01 "I would tend to agree, but they don't fall within the regular population of \"people who stick things up their asses\". These are regular family men AND women."
mc "That is unusual then..."
hide sawyereyeblink
show sawyer02 at centerleft
with fastdissolve
cs01 "Unfortunately, since they can't help us, I have no idea where to begin my investigation. That's why I'm putting YOU in charge of this delicate mission."
$ mission04 = True
window hide
play sound "sounds/achievement.mp3"
show missionicon04 at poslocation
$ renpy.pause(0.5, hard=True)
show textmission04 at posmissiontext
pause
mc "LAME!"
hide missionicon04
hide textmission04
hide sawyer02
show sawyer04 at centerleft
with fastdissolve
cs01 "Stop complaining. You're a superhero, you just need to probe DEEP into this and you'll find the way out."
mc "That's what the gerbil said."
hide sawyer04
show sawyer03 at centerleft
with fastdissolve
cs01 "Since you're obviously not taking this very seriously, which I expected, I called the S-X Files division of the FBI."
hide sawyer03
show sawyer06 at centerleft
with fastdissolve
cs01 "You will be paired with Agent Skully."
window hide
show sawyer06 at midright with move
mc "The S-X Files? What do they deal with?"
play sound "sounds/sexfiles.mp3"
window hide
show skully03 at farleft with moveinleft
sk "USPs. Unexplained Sexual Phenomenae."
mc "Oh. And you're Agent Skully?"
hide skully03
show skully01 at farleft
with fastdissolve
sk "That's right. SPECIAL Agent Skully even. * wink *"
hide sawyer06
show sawyer02 at midright
with fastdissolve
cs01 "Special Agent Skully will make sure you don't screw up this time. I'm off to cater to some more SERIOUS matters."
hide sawyer02 with moveoutright
show skully01 at left with move
hide skully01
show skully03 at left
with fastdissolve
sk "So, since you're in charge, do you have a lead on these USPs?"
if seenbeatbarr == False:
    mc "Not really, why the hell should I know anything about traumatic anal injuries? You're better off asking my sexual partners."
    hide skully03
    show skully02 at left
    with fastdissolve
    sk "What do you mean by that?"
    mc "Err..."
    hide skully02
    show skully01 at left
    with fastdissolve
    sk "Well, we NEED a lead. So I suggest you go on the beat with Captain Sawyer to see what info you can gather. I heard this is where she was going today. I'll be studying the dossier in my office."
    hide skully01 with moveoutleft
    show sawyerout01 at centerleft with dissolve
    cs02 "What do you want? I was about to go on the beat."
    mc "Yeah, I'd like to go with you actually. Need some info for that lame-ass mission. No pun intended."
    cs02 "I see. And where would you like to go?"
    stop music
    scene cockhammap
    menu:
        "Old Cockham":
            jump CockhamBeat                
        "Barr Town":
            jump BarrBeat
        "Porkher Row":
            jump PorkherBeat    

if seenbeatbarr:
    mc "Come to think about it, I did overhear some hobo talk about space aliens abducting people. I brushed it off, but now..."
    hide skully03
    show skully02 at left
    with fastdissolve
    sk "Aliens? That's preposterous! Aliens don't exist."
    if fleeghost:
        mc "And I suppose you're going to tell me that ghosts don't exist either?"
        hide skully03
        show skully04 at left
        with fastdissolve
        sk "That's right, they DON'T EXIST EITHER."
        mc "Well, I saw one, so I KNOW they DO! And that's my lead, we've got nothing else at this stage!"
        hide skully04
        show skully01 at left
        with fastdissolve
        sk "* sigh * Fine, where is this hobo you speak of?"
        mc "Downtown. I know how to get there."
        if period == 0:
            sk "Fine, let's go there in the evening then, this is when the USPs have been reported to occur. I'll be in my office until then. Meet me back here tonight."
            mc "Okey-dokey."
            jump Main
    if fleeghost == False:
        mc "Since you're into USPs, explain this: my ungodly HUGE cock. I'm waiting."
        hide skully02
        show skully01 at left
        with fastdissolve
        sk "Err... Good genes?"
        mc "We have no lead, this hobo is all I've got."
        if period == 0:
            sk "Fine, let's go there in the evening then, this is when the USPs have been reported to occur. I'll be in my office until then. Meet me back here tonight."
            mc "Okey-dokey."
            jump Main

hide skully01
show skully04 at left
with fastdissolve
sk "Fine, let's go there then, it's the evening and this is when the USPs have been reported to occur. Let's investigate that... alien theory of yours."
jump Mission04Nextb

label Mission04Next:
stop music
scene ccpd01
show ccpd01back
with fade
show skully04 at left with moveinleft
sk "It's getting dark, time to investigate that... alien theory of yours."
label Mission04Nextb:
mc "It's not my theory, it's a drunken hobo theory."
sk "* sigh *"

scene prealien01 with fade
play music "sounds/suspense.mp3"
mc "Ah, the drunken hobo is here. Again."
scene prealien02 with dissolve
sk "I'm starting to think we're wasting our time..."
mc "Just listen to what he'll say."
scene prealien03 with dissolve
hb "You again? And who's the pretty lady with you this time?"
sk "Special Agent Skully. You have apparently some information concerning... aliens doing... stuff to people's..."
mc "...Asses. Right?"
scene prealien04 with dissolve
play channel2 "sounds/spaceship.mp3"
hb "Yeah! They come, they take people, and then..."
mc "Hang on, what's that noise?"
scene prealien05 with dissolve
play channel1 "sounds/radiation02.mp3"
mc "Hey! What the hell???"
hb "I told you! They're coming! Watch out for your BUTTS!"
            
stop channel1
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
call screen usepower("usestud", "SkullyNoStud", "SkullyStud") with dissolve
label SkullyNoStud:
mc "I can't stand players who can't make up their minds. OVERRULED!"
label SkullyStud:
window hide

label GillianFuckSlow: 
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

call screen gillianfuckslow()
screen gillianfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("GillianFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GillianFuckEnd")

label GillianFuckFast:
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

call screen gillianfuckfast()
screen gillianfuckfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("GillianFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("GillianFuckEnd")

label GillianFuckEnd:
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

label Alien02FuckSlowUp:
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
call screen alien02fuckupslow()
screen alien02fuckupslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckFastUp")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("Alien02FuckDownSlow")

label Alien02FuckFastUp:
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
call screen alien02fuckupfast()
screen alien02fuckupfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckSlowUp")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien02FuckUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("Alien02FuckDownFast")

label Alien02FuckDownSlow:
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
call screen alien02fuckdownfuckslow()
screen alien02fuckdownfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckDownFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien02FuckSlowUp")

label Alien02FuckDownFast:
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
call screen alien02fuckdownfuckfast()
screen alien02fuckdownfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien02FuckDownSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien02FuckUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien02FuckFastUp")

label Alien02FuckUpEnd:
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

label Alien01FuckSlowUp:
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
call screen alien01fuckupslow()
screen alien01fuckupslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckFastUp")
    button:
        xpos 50
        ypos 500
        xysize(120, 120)        
        action Jump ("Alien01FuckDownSlow")

label Alien01FuckFastUp:
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
call screen alien01fuckupfast()
screen alien01fuckupfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckSlowUp")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien01FuckUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 120)        
        action Jump ("Alien01FuckDownFast")


label Alien01FuckDownSlow:
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
call screen alien01fuckdownfuckslow()
screen alien01fuckdownfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckDownFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien01FuckSlowUp")

label Alien01FuckDownFast:
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
call screen alien01fuckdownfuckfast()
screen alien01fuckdownfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("Alien01FuckDownSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("Alien01FuckUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 80)        
        action Jump ("Alien01FuckFastUp")

label Alien01FuckUpEnd:
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
pa "That's great, we'll both have INTERGALACTIC BABIES! We can go back to Xelaria and tell everyone the mission was a success!"
mc "And I can go back to the CCPD and tell them I've completed MY mission too! All thanks to my SUPERHERO cock!"
pa "I'm not sure about that. We need to erase your memory. Get cleaned up, I'll start with the female earthling."
scene postaliens01 with dissolve
mc "Are you going to erase my memory now? Please don't..."
ba "I'm afraid this is an Intergalactic Top Secret Program. Do you have Galactic Top Security Clearance?"
mc "Err.... No."
scene postaliens02 with dissolve
pa "For helping us in our breeding program, we return this strange human appendage we once removed from a test subject by mistake several decades ago..."
mc "Yuck, it's a testicle! What the hell am I supposed to do with that???"
ba "Returning it to its owner would be the polite thing to do. His name was... Adolf... Hitler, if I remember correctly. Strange little fellow, with a weird accent."
window hide
$ inventoryhitlerball = True
play sound "sounds/achievement.mp3"
show acquiredhitlerball at poslocation
$ renpy.pause(0.5, hard='True')
pause
pa "We hope he didn't become too angry about missing one of these things."
mc "Err..."
scene postaliens03 with dissolve
ba "Please look at the small light right here."
mc "What light?"
window hide
play sound "sounds/flash.mp3"
with fastflash
$ mission04end = True
stop music
jump NewDay

label Quest05Start:
stop music
scene sophiaoffice10 with dissolve
cs01 "There she is. Notice anything different, [name]?"
mc "She's... kinda flat-chested. She had breast reduction surgery? What a weird idea. Especially in this game." 
scene sophiaoffice11 with dissolve
so "No! I woke up one morning like that. With my breasts GONE!"
scene sophiaoffice12 with dissolve
cs01 "It appears someone is STEALING titflesh from women around Cockham. Mrs Porker here is only the most recent victim of this dreadful SEX CRIME."
window hide
play sound "sounds/achievement.mp3"
$ quest05 = True
show questicon05 at poslocation
$ renpy.pause(0.5, hard=True)
show textquest05 at posmissiontext
pause
scene sophiaoffice11 with dissolve
mc "Were you, by any chance, lurking in Rapists' Alley once again?"
scene sophiaoffice13 with dissolve
so "No I was NOT! Why would I go back there after all the awful things that happened to me?"
mc "Sorry, it was just a hunch. So, you just woke up and... poof, tiny tits?"
scene sophiaoffice14 with dissolve
so "There was a strange smell around. Like compost."
mc "Compost? Interesting... Had you been out during the evening?"
scene sophiaoffice11 with dissolve
so "I did take a short stroll down Robinson Park. I remember picking up some lovely white daisies, which have since withered away. Do you think it's relevant?"
mc "Maybe. I shall first find some of those flowers to make sure they are responsible for your, err, predicament. And I'm starting to have an inkling as to who the culprit might be."
scene sophiaoffice12 with dissolve
cs01 "And who do you have in mind?" 
mc "Poison Ivy. She lurks in Robinson Park, I saw her there and she attacked me. But I easily defeated her, what with my Super-Muscles and all that."
scene sophiaoffice10 with dissolve
cs01 "We hadn't heard from her in quite a while, she has apparently re-surfaced. And for the worse! Do your duty, [hero] and get Mrs Porker her... boobs back, if you can."
mc "Aye Aye Captain!"
cs01 "And be prepared! Poison Ivy can be a MIGHTY and DEADLY opponent."
jump MCRoomDay
