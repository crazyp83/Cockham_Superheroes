label MafiaLair:
play music "sounds/mafiamusic.mp3" fadein 1.0
scene mafiabase01 with fade
if seenmafia == False:
    $ seenmafia = True
    jump MafiaFirst
if seenmafiasecond:
    jump MafiaFirstb
if seenmafiasecond == False:
    $ seenmafiasecond = True
    jump MafiaSecond

label MafiaFirstb:
show mafiasam with dissolve
mb "- You again?"
if withag:
    show mafiaexcella with fastdissolve
    ex "And a huge-breasted girl with him. Interesting..."
    hide mafiasam
    show mafiagoon
    with fastdissolve
    gg "Her tits are even bigger than Exce..."
    mb "- Shut up, Gutsy!"
    hide mafiagoon with fastdissolve
if withag == False:
    show mafiaexcella with fastdissolve
    ex "He's persistent, I'll give him that."
    hide mafiasam
    show mafiagoon
    with fastdissolve
    gg "And annoying. VERY annoying!"
    hide mafiagoon with fastdissolve
jump MafiaDialogues

label MafiaFirst:
show mafiasam with dissolve
mb "- Who are you?"
show mafiagoon with fastdissolve
gg "Look at him! He don't even wear nice clothes in front of the Boss! Va fa Napole!"
mc "Allow myself to introduce...err...myself."
window hide
pause
hide mafiasam with dissolve
mb "- I'm waiting."
hide mafiagoon with fastdissolve
gg "He's waiting. And he don't like to wait."
mc "Yes, ahem. * cough * I am [hero]. You might have heard of me, I'm the new Superhero in town."
show mafiaexcella with dissolve
ex "But you are in charge of SEX crimes, are you not? We don't do sex crime here."
show mafiagoon with fastdissolve
gg "That's right, we don't do sex crime. We do other crimes."
show mafiasam with fastdissolve
mb "- Shut up, Gutsy!"
hide mafiagoon
hide mafiasam
hide mafiaexcella
with dissolve
gg "Sorry, Boss."
label MafiaDialogues:
menu:
    "That's a nice little bar you have here. Shame if something were to happen to it." if mafiatalked == False:
        $ mafiatalked = True
        show mafiasam with dissolve
        mb "- Is this bambino fucking with me?"
        show mafiagoon with fastdissolve
        gg "He's pazzo, boss! He don't know what he's talking about! Do you wanta me to bump him off?"
        show mafiaexcella with fastdissolve
        ex "That won't be necessary. It looks like a misunderstanding. Isn't that right, bello?"
        hide mafiagoon with fastdissolve
        mc "Bello? Does this mean I'm handsome?"
        ex "It sure does, bello."
        hide mafiasam with fastdissolve
        mc "Then, yeah, I mean, si, it's all a misunderstanding. I ain't got no beef against the house."
        hide mafiaexcella with fastdissolve
        ex "Bene. One day, you might become an associate, bello."
        show mafiagoon with fastdissolve
        gg "What? But he's a cafone! He don't even have a biscuit!"
        show mafiasam with dissolve
        mb "- Chiudere il becco Gutsy, my wife is right. As always."
        show mafiaexcella with fastdissolve
        ex "Exactly, I'm ALWAYS right. Remember that Gutsy... Or I might have to break you."
        mc "* I think I need to learn their lingo if I want to infiltrate the Mafia. I don't understand a bloody word they're saying... *"
        jump Main
    "You shady guys have something to do with something shady with the shady mayor? I mean his lovely daughter?" if mission03 and mission03end == False and mafiatalked == False:
        $ mafiatalked = True
        show mafiasam with dissolve
        mb "- What is this bambino talking about?"
        show mafiagoon with fastdissolve
        gg "He's pazzo, boss! He don't know what he's talking about! Do you wanta me to bump him off?"
        show mafiaexcella with fastdissolve
        ex "That won't be necessary. It looks like a misunderstanding. Isn't that right, bello?"
        hide mafiagoon with fastdissolve
        mc "Bello? Does this mean I'm handsome?"
        ex "It sure does, bello."
        hide mafiasam with fastdissolve
        mc "Then, yeah, I mean, si, it's all a misunderstanding. I ain't got no beef against the house."
        hide mafiaexcella with fastdissolve
        ex "Bene. One day, you might become an associate, bello."
        show mafiagoon with fastdissolve
        gg "What? But he's a cafone! He don't even have a biscuit!"
        show mafiasam with dissolve
        mb "- Chiudere il becco Gutsy, my wife is right. As always."
        show mafiaexcella with fastdissolve
        ex "Exactly, I'm ALWAYS right. Remember that Gutsy... Or I might have to break you."
        mc "* I think I need to learn their lingo if I want to infiltrate the Mafia. I don't understand a bloody word they're saying... *"
        jump Main
    "I'd like to see your books.":
        show mafiasam with dissolve
        mb "- Our books? Why would he want to see our books?"
        show mafiaexcella with fastdissolve
        ex "Maybe he thinks we're involved in tax fraud. But he's WRONG."
        mc "I'll be the judge of that."
        hide mafiasam with fastdissolve
        mb "- Do you have a warrant, sonny?"
        mc "A what?"
        show mafiagoon with fastdissolve
        gg "He don't even have a warrant! What a buffone!"
        if withag == False:
            hide mafiaexcella with fastdissolve
            ex "No warrant, no books, bello."
            hide mafiagoon with fastdissolve
            gg "And arriverderci, buffone!"
            mc " * Damn it, I need to find some other ways to see their books... Maybe Audit Girl would know... *"
            jump Main
        if withag:
            hide mafiagoon with fastdissolve
            ag "We don't need one. According to City Ordnance 435-81, The Cockham League of Justice is allowed to view the books of any commercial entities, private corpor..."
            hide mafiaexcella with fastdissolve
            mb "- Alright, alright, basta! Who is this girl?"
            mc "That's Audit Girl. She'll audit you. Very QUICKLY. Cos, err... that's her superpower."
            show mafiasam with dissolve
            mb "- * grunt * Gutsy, get the books and give them to her..."
            show mafiagoon with fastdissolve
            gg "But boss, they're the bad guys!"
            hide mafiagoon with dissolve
            mb "- Chiudere il becco Gutsy and GIVE THEM THE BOOKS!"
            show mafiaexcella with fastdissolve
            ex "Maybe while Audit Girl is looking at our books, you might want to visit our back office, Bello?"
            hide mafiasam with fastdissolve
            mc "I guess, why not."
            hide mafiaexcella with fastdissolve
            ex "I'll show you around. Follow me."
            jump MafiaOffice
    "I'd like to become a \"Friend of Yours\"." if mclevel02 and seenexcellalingerie and seenexcellaseduction == False:
        show mafiagoon with fastdissolve
        gg "You? You can't be serious!"
        show mafiaexcella with fastdissolve
        ex "Let me handle this, Gutsy. I might give this bambino a chance."
        show mafiasam with dissolve
        mb "- Have a look at what he's made of. We need better capones."
        jump MafiaOfficeSeduction
    "I'd like to talk to Excella about my \"employment\" prospects..." if mclevel02 and seenexcellalingerie and seenexcellaseduction:
        show mafiasam with dissolve
        mb "- She did tell me you had shown great potential on your last visit. va bene. Go and speak with my wife, bambino."
        show mafiaexcella with fastdissolve
        ex "Follow me to the office, [hero]..."
        jump MafiaOfficeSeduction
    "I'm done talking.":
        show mafiagoon with fastdissolve
        gg "Va bene!"
        show mafiaexcella with fastdissolve
        ex "Goodbye then. [hero]."
        jump Main


label MafiaSecond:
mc "Howdy, gentlemen! And... err, lady."
show mafiaexcella with fastdissolve
ex "We have no time for you, [hero]. Sam has arranged a call in for a capodecina and his crew."
mc "Right, right. No idea what you're talking about but it sounds important so I'll leave you to it then."
hide mafiaexcella with fastdissolve
ex "Maybe one day you can become a Friend of Ours."
jump Main

label MafiaOffice:
stop music
scene mafiaofficebackground with fade
show excella01 with dissolve
ex "I would like to show you something, [hero]. Some important documents that I keep in my safe..."
mc "* Damn, what a THICK ASS! *"
hide excella01
show excella02
with dissolve
ex "It won't take a moment. Please sit in the comfy mafia chair over there while I get them. The safe is hidden behind that divider so you won't be able to see the code."
if mcsenses >= 1:
    mc "You're right not to trust me, I have Super-senses I'll have you know!"
if mcsenses == 0:
    mc "Fine, whatever. Let's see those documents then."
    
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy11.mp3"
scene excellaoffice00 with dissolve
mc "Wh... Why is she showing me her leg like that???"
scene excellaoffice00b with dissolve
mc "Damn, she's changed into a SEXY gangsta outfit!"
scene excellaoffice00c with dissolve
ex "So, [hero], let's talk \"business\"..."
scene excellaoffice01 with dissolve
mc "Wh.. What business did you have in mind?"
scene excellaoffice02 with dissolve
ex "I was thinking... You help me, and I help you... A win-win kind of business, right?"
mc "That sounds... like..."
scene excellaoffice03 with dissolve
ex "For example, our books... They're clean."
scene excellaoffice04 with dissolve
mc "Ar... Are they? Audit Girl is..."
scene excellaoffice05 with dissolve
ex "...looking at them, and she will find NOTHING, understood?"
scene excellaoffice02 with dissolve
mc "This is highly inap..."
scene excellaoffice04 with dissolve
ex "And in exchange, I'll help YOU."
mc "Err... How so?"
scene excellaoffice06 with dissolve
ex "I'm sure we can find some arrangements to your liking..."
mc "I... don't know if..."
scene excellaoffice07 with dissolve
ex "Your cock seems to be demanding some attention... I could tend to it..."
mc "I.. Damn it, I'm getting HARD!"
scene excellaoffice08 with dissolve
ex "Indeed you are... And this great big whopper needs some relief, I can tell..."
mc "Fuck, what an ass!"
scene excellaoffice09 with dissolve
ex "You ain't seen nothing yet, [hero]!"
mc " * She's Super-Seducing me and there's nothing I can do about it, I'm just TOO HORNY! *"
scene excellaoffice10 with dissolve
if age >= 20:
    ex "Let me take good care of that monstercock... With my HUGE BREASTS!"
if age >= 18 and age <= 19:
    ex "Let me take good care of that teenage monstercock... With my HUGE BREASTS!"
scene excellaoffice11 with dissolve
play sound "sounds/boymoan.mp3"
mc "Damn! Mamma Mia!"
ex "Maybe I should squeeze my tits a little bit more around that shaft..."
scene excellaoffice12 with dissolve
play sound "sounds/boymoan02.mp3"
ex "And lick the abundant precum that is flowing from your throbbing cock..."
scene excellaoffice13 with dissolve
ex "There's so much of it, it seems like you're about to BURST!"
mc "Oh God, oh God..."
scene excellaoffice14 with dissolve
play sound "sounds/boymoan04.mp3"
ex "My tits were THAT enticing, [hero]?"
scene excellaoffice15 with dissolve
ex "You just couldn't hold back and now you're having a FULL-BLOWN ORGASM!"
window hide
with fastflash
play sound "sounds/boymoan05.mp3"
mc "AAAAH, FUCK, I'm CU-UUU-MMM-IIING!!!"
scene excellaoffice16 with dissolve
mc "AAAH, what are you doing?"
ex "Do you agree that our books are CLEAN, [hero]?"
mc "Yes, YES, I AGREE, LET ME CUM!!!"
scene excellaoffice17 with dissolve
ex "Good, now you can come! Come as MUCH AS YOU LIKE!"
play sound "sounds/boymoan03.mp3"
window hide
with hpunch
ex "That's it, let it all out, let my sumptuous tits MILK YOU DRY!"
scene excellaoffice18 with dissolve
play sound "sounds/slurp.mp3"
ex "Wow, your balls were FULL TO THE BRIM it seems!"
play sound "sounds/panting.mp3"
mc "No, I... usually come... That much..."
ex "Impressive, young stallone... And tasty too... Let me get cleaned up and let's go back to the bar..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
scene mafiabase01 with fade
ag "I checked their books and I found some major irregul..."
mc "Their books are clean Audit Girl, let's go!"
show mafiaexcella with fastdissolve
ag "But..."
mc "I checked myself with Excella Gionne, and I am confident they are CLEAN! Don't argue with me and let's go!"
$ seenexcellalingerie = True
$ withag = False
jump Main

label MafiaOfficeSeduction:
stop music
scene mafiaofficebackground with fade
show excella01 with dissolve
if seenexcellaseduction == False:
    ex "So, you would like to become a Friend of Ours..."
    mc "Yeah, sure, I think I am meant for this kind of job."
if seenexcellaseduction:
    ex "So, you're back... And I suppose you want to prove to me once again that you would be an ideal asset to the Famiglia?"
    mc "These were my intentions indeed..."
hide excella01
show excella02
with dissolve
if seenexcellaseduction == False:
    ex "I will have to test you then. We don't accept just anyone in the Mafia... Wait for me here, I will change into... something more appropriate."
if seenexcellaseduction:
    ex "You're certainly already proven your studly worth... But I'd like to be reminded of how much of a young STALLONE you truly are..."
    mc "I will do my best. Again."
play sound "sounds/sexy09.mp3"
scene excellatease00 with fade
ex "I'm back... Follow me and let's see if you've got the BALLS for the job..."
scene excellatease01 with dissolve
if seenexcellaseduction == False:
    ex "For example, what would you do if you met an enemy with SUCH A FINE BOOTY?"
    mc "Err... Pound it hard until she submits?"
if seenexcellaseduction:
    ex "You remember that FINE BOOTY?"
    mc "I sure do!"
scene excellatease02 with dissolve
if seenexcellaseduction == False:
    ex "WRONG answer. You need to SEDUCE her first. Or you'll end up DEAD."
    mc "I've got plenty of Super-Seduction superpowers!"
if seenexcellaseduction:
    ex "Then you know how to treat it well, don't you?"
    mc "I'll treat it like royalty!"
scene excellatease03 with dissolve
ex "Is that so? Well, why don't you try and seduce ME then? Let's see if your supposed superpowers really work..."
scene excellatease04 with dissolve
ex "You see this nice pussy... It needs some tender loving."
mc "It sure looks like it does! I'll give it my best!"
if seenexcellaseduction == False:
    call screen usepower("useseduction", "ExcellaNoSeduction", "ExcellaSeduction") with dissolve
jump ExcellaSeduction

label ExcellaNoSeduction:
scene excellatease05 with dissolve
mc "Let me spread those asscheeks so I can..."
ex "You're just... being too ROUGH! That is not good. Not good AT ALL!"
stop music
scene excellatease05b with dissolve
play sound "sounds/slap.mp3"
ex "You're no seducer, you wouldn't last long in the Mafia!"
ex "Now get out of my office and come back when you are TRULY ready to Super-Seduce ME!"
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
 
label ExcellaSeduction:
if mcseduction <= 1 or usedseduction <= 2:
    mc "Looks like my Super-Seductions skills aren't high enough or I haven't used them enough times..."
    jump ExcellaNoSeduction

scene excellatease05 with dissolve
if seenexcellaseduction == False:
    $ usedseduction += 1
mc "Let me delicately expose that nice muff of yours..."
scene excellatease06 with dissolve
ex "Get that tongue right in there..."
scene excellatease07 with dissolve
play sound "sounds/moan02.mp3"
ex "Mmh, si, just like that..."
scene excellatease08 with dissolve
play sound "sounds/moan04.ogg"
ex "Oooh!"
scene excellatease08b with dissolve
play sound "sounds/moan04.ogg"
ex "Oooh!"
mc "Now turn round, I'm not done toying with your horny snatch..."
scene excellatease09 with dissolve
play sound "sounds/moan02.mp3"
ex "You're... sticking a finger inside me!"
mc "That's right..."
scene excellatease10 with dissolve
play sound "sounds/moan05.mp3"
mc "And now half my fist!"
ex "AAAH!"
window hide
scene excellateaselick with fastdissolve
pause
ex "You're going to make me..."
scene excellatease11 with dissolve
play sound "sounds/splooge01.mp3"
ex "...CUM!!!!"
scene excellatease12 with dissolve
play sound "sounds/womancum02.mp3"
ex "AAAH!"
scene excellatease13 with dissolve
ex "You did well, I might consider a position for y..."
scene excellatease14 with dissolve
mc "Ain't done yet! Gonna make that pussy SQUIRM with pleasure with my Super-Dong!"
ex "Ooh, you're such a NAUGHTY Super-Hero!"
scene excellatease15 with dissolve
ex "I've met quite a few \"Italian Stallions\" in my time, but none anywhere near as BIG as you!"
mc "I'm only half-hard, Mrs Gionne. But I'll soon be ROCK-HARD to pound that sweet MILF pussy of yours!"
scene excellatease16 with dissolve
if seenexcellaseduction == False:
    ex "It's even BIGGER than the last time I saw it! Almost...Intimidating..."
if seenexcellaseduction:
    ex "Just as MASSIVE as I remember..."
scene excellatease17 with dissolve
mc "This is going to be a tight fit but a big girl like you should be able to take it without too much complaining..."
scene excellatease18 with dissolve
play sound "sounds/moan01.mp3"
ex "You're talking like someone who is in total control of the situation, bambino! This is making me so horny, just do it!"
play channel1 "sounds/womansex02.mp3"

label ExcellaDeskFuckSlow:
$ excelladeskfuckfast = False
$ excelladeskharder = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if excelladeskfuckslow == False:
    if age >= 20:
        ex "Be careful with that huge weapon of yours, it might accidentally discharge inside me!"
    if age >= 18 and age <= 19:
        ex "Be careful with that huge teenage weapon of yours, it might accidentally discharge inside me!"
    $ excelladeskfuckslow = True
window hide
show excelladeskfuckslowvideo behind excelladeskfuckfastvideo
show excelladeskfuckslowvideo behind excelladeskfuckslowpovvideo
show excelladeskfuckslowvideo behind excelladeskfuckharderslowvideo
pause 1.0
hide excelladeskfuckfastvideo
hide excelladeskfuckslowpovvideo
hide excelladeskfuckharderslowvideo
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
call screen excelladeskfuckslow()
screen excelladeskfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVSlow")

label ExcellaDeskFuckFast:
$ excelladeskharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if excelladeskfuckfast == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ excelladeskfuckfast = True
show excelladeskfuckfastvideo behind excelladeskfuckslowvideo
show excelladeskfuckfastvideo behind excelladeskfuckfastpovvideo
show excelladeskfuckfastvideo behind excelladeskfuckharderfastvideo
pause 1.0
hide excelladeskfuckslowvideo
hide excelladeskfuckfastpovvideo
hide excelladeskfuckharderfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen excelladeskfuckfast()
screen excelladeskfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVFast")

label ExcellaDeskFuckPOVSlow:
$ excelladeskharder = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if excelladeskfuckslow == False:
    if age >= 20:
        ex "Be careful with that huge weapon of yours, it might accidentally discharge inside me!"
    if age >= 18 and age <= 19:
        ex "Be careful with that huge teenage weapon of yours, it might accidentally discharge inside me!"
    $ excelladeskfuckslow = True
show excelladeskfuckslowpovvideo behind excelladeskfuckslowvideo
show excelladeskfuckslowpovvideo behind excelladeskfuckfastpovvideo
show excelladeskfuckslowpovvideo behind excelladeskfuckharderpovslowvideo
pause 1.0
hide excelladeskfuckslowvideo
hide excelladeskfuckfastpovvideo
hide excelladeskfuckharderpovslowvideo
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen excelladeskfuckslowpov()
screen excelladeskfuckslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckSlow")

label ExcellaDeskFuckPOVFast:
$ excelladeskharder = False
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if excelladeskfuckfast == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ excelladeskfuckfast = True
window hide
show excelladeskfuckfastpovvideo behind excelladeskfuckslowpovvideo
show excelladeskfuckfastpovvideo behind excelladeskfuckfastvideo
show excelladeskfuckfastpovvideo behind excelladeskfuckharderpovfastvideo
pause 1.0
hide excelladeskfuckslowpovvideo
hide excelladeskfuckfastvideo
hide excelladeskfuckharderpovfastvideo
with dissolve
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen excelladeskfuckfastpov()
screen excelladeskfuckfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckFast")

label ExcellaDeskFuckHarderSlow:
if excelladeskharder == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharder = True        
window hide
show excelladeskfuckharderslowvideo behind excelladeskfuckharderfastvideo
show excelladeskfuckharderslowvideo behind excelladeskfuckharderpovslowvideo
show excelladeskfuckharderslowvideo behind excelladeskfuckslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderfastvideo
hide excelladeskfuckharderpovslowvideo
hide excelladeskfuckslowvideo
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
call screen excelladeskfuckharderslow()
screen excelladeskfuckharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCum")

label ExcellaDeskFuckHarderFast:
if excelladeskharder == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharder = True        
window hide
show excelladeskfuckharderfastvideo behind excelladeskfuckharderslowvideo
show excelladeskfuckharderfastvideo behind excelladeskfuckharderpovfastvideo
show excelladeskfuckharderfastvideo behind excelladeskfuckfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderslowvideo
hide excelladeskfuckharderpovfastvideo
hide excelladeskfuckfastvideo
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
call screen excelladeskfuckharderfast()
screen excelladeskfuckharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCum")

label ExcellaDeskFuckHarderPOVSlow:
if excelladeskharder == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharder = True        
window hide
show excelladeskfuckharderpovslowvideo behind excelladeskfuckharderslowvideo
show excelladeskfuckharderpovslowvideo behind excelladeskfuckharderpovfastvideo
show excelladeskfuckharderpovslowvideo behind excelladeskfuckslowpovvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderslowvideo
hide excelladeskfuckharderpovfastvideo
hide excelladeskfuckslowpovvideo
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
call screen excelladeskfuckharderpovslow()
screen excelladeskfuckharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCum")

label ExcellaDeskFuckHarderPOVFast:
if excelladeskharder == False:
    ex "You STALLONE! Give it to me REALLY HARD!"
    mc "Alright, you asked for it!"
    $ excelladeskharder = True        
window hide
show excelladeskfuckharderpovfastvideo behind excelladeskfuckharderpovslowvideo
show excelladeskfuckharderpovfastvideo behind excelladeskfuckharderfastvideo
show excelladeskfuckharderpovfastvideo behind excelladeskfuckfastpovvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide excelladeskfuckharderpovslowvideo
hide excelladeskfuckharderfastvideo
hide excelladeskfuckfastpovvideo
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
call screen excelladeskfuckharderpovfast()
screen excelladeskfuckharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("ExcellaDeskFuckHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("ExcellaDeskFuckCum")

label ExcellaDeskFuckCum:
hide faster
hide slower
hide pov
hide sceneicon
hide cum
ex "I want you to give me your young spunk! Can you do that for me, amico?"
mc "Ooh yeah I can, I certainly..."
scene excelladeskcum00 with dissolve
stop channel1
play channel1 "sounds/splooge02.mp3"
play channel2 "sounds/boyorgasm01.mp3"
mc "...CAAAAAAN!"
window hide
with fastflash
if age >= 20:
    ex "Oh my, you certainly are a true STALLONE!"
if age >= 18 and age <= 19:
    ex "Oh my, you certainly are a true TEENAGE STALLONE!"
scene excelladeskcum01 with dissolve
ex "STILL BLOWING! AAAH!"
window hide
with hpunch
ex "Ooh, look at that, it's already leaking from my pussy!"
scene excelladeskcum02 with dissolve
mc "Now DEEP INSIDE YOUR MAFIOSO FUCKHOLE! RHAAA!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
ex "AAAH!"
scene excelladeskcum03 with dissolve
ex "You're pumping too much seed into my poor pussy!"
window hide
with hpunch
mc "It's never too much spunk for a SEX Super-Hero! AAAH!"
window hide
with vpunch
ex "Please... PULL OUT!"
scene excelladeskcum04 with dissolve
stop channel1
mc "Alright, you asked for it, then you'll take my scum all over your chest and face, RHAAA!"
window hide
with fastflash
play sound "sounds/moan03.mp3"
ex "Oh God, you're going to PLASTER me with your [age]-yo cream!"
scene excelladeskcum05 with dissolve
mc "Damn right I will! Take that!"
window hide
with vpunch
ex "Mamma Mia! So much young HOT SPUNK!"
scene excelladeskcum06 with dissolve
stop music
stop channel2
play sound "sounds/moan02.mp3"
     
if mission07win and mission08 == False:
    scene excelladeskcum07 with dissolve
    ex "You made me cum so much bambino... I have some job for you. Will you help the Famiglia? As a reward, I would let you... FUCK MY ASS!"
    menu:
        "A mission? Alright!":
            scene excelladeskcum09 with dissolve
            ex "Excellent, bambino... Let me get (* lick *)... cleaned up and I'll tell what it's about."
            jump MafiaMission
        "Na, I don't do mafia crimes, I'm the good guy.":
            scene excelladeskcum08 with dissolve
            ex "That is VERY disappointing! And also won't make you advance much towards your ultimate goal... Except if you decide to work for the ENEMY!"
            mc "And who would that be?"
            scene excelladeskcum09 with dissolve
            ex "The Chinese Triad of course! You'd better not go and see them or I'll have to BREAK YOU!"
            mc "Right, right..."
            jump EndMafiaSeduction

if seenexcellaseduction:
    ex "I'm definitely going to try and find some \"employment\" for you with the Famiglia..."
if seenexcellaseduction == False:
    ex "Come back anytime STALLONE, I'll definitely try and find some \"employment\" for you with the Famiglia..."
    mc "I'll bear that in mind..."
$ seenexcellaseduction = True

label EndMafiaSeduction:
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label MafiaMission:
$ mission08mafia = True
scene mafiaofficebackground
show excella04
with fade
ex "So [hero]...Welcome to the Famiglia! Here's our mission. The Famiglia's mission. And therefore YOUR mission."
mc "There's no way out is there once you're in?"
hide excella04
show excella03
with fastdissolve
ex "There is. In a coffin."
mc "I see. I totally accept the mission then. What is it about?"
hide excella03
show excella02
with fastdissolve
ex "It involves SCREWING the Chinese Triad for GOOD! We leave tonight, they have a shipment of Chromium coming in and we're gonna steal it right from under their noses, capiche?"
mc "Drugs are bad, m'kay. But I'd rather the Mafia had it than the Chinese Triad because I'm a mafioso now."
window hide
play sound "sounds/achievement.mp3"
$ mission08 = True
show mission08icon at poslocation
$ renpy.pause(0.5, hard=True)
show textmission08 at posmissiontext
pause    
hide excella02
show excella04
with fastdissolve
ex "That's right, bambino. The Famiglia is the best at dealing drugs in an honest, proper manner."
mc "Sure, boss."

$ period = 1
show screen calendar
show screen statscreenicon
show screen questscreenicon
play music "sounds/mafiamusic.mp3"
scene docks01 with fade
play sound "v07/carpark.mp3"
$ renpy.pause(1.0, hard='True')
scene docks02 with fastdissolve
$ renpy.pause(2.0, hard='True')
scene docks03 with fastdissolve
$ renpy.pause(1.0, hard='True')
stop sound
scene docks08:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with fastdissolve
play sound "v07/cardoor.mp3"
ex "The deal will take place in this hangar. Let's get into position and ambush them."
gg "I'll fill them with so many bullet holes, they'll look like asagio cheese!"
scene docks09 with dissolve
ex "Gutsy, you go up there with the machine gun. I don't trust you in close combat."
mc "And me?"
scene docks10 with dissolve
ex "You I trust, bambino. You will be in the first line of attack."
mc "With you?"
ex "No, alone. You are a Super-Hero are you not?"
mc "Err, yeah, but I CAN get killed!"
scene docks11 with dissolve
ex "You should be able to deal with any threat easily. Including flying bullets. And remember, that ass is yours at the end of the mission, bambino..."
mc "I suppose the sacrifice of my life is worth it to tap THAT..."
scene docks40 with dissolve
gg "All set, boss!"
ex "And you?"
scene docks41 with dissolve
mc "Err, I suppose I'm in position. FRONTLINE position actually. And I hear them coming!"
ex "Then let's not make any more noise and let them fall into MY TRAP!"
scene docks42:    
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with fastdissolve
aw "Let's check out the rest of the hangar before the seller arrives. I don't want any nasty surprises."
mc "* I'm starting to wonder whether I'm not the one falling into a trap... *"
scene docks43 with dissolve
play sound "sounds/gunfire.mp3"
aj "We're being shot at from up there!"
aw "You? TRAITOR!"
mc "Uh oh, she's about to fire at me!"

$ img_l = []
$ l2_l = []
$ img_l.append("usestrength")
$ l2_l.append("DocksMafiaStrength")
$ img_l.append("useagility")
$ l2_l.append("DocksMafiaStrength")
if img_l:
    call screen usepower(img_l, "DocksMafiaNoStrength", l2_l) with dissolve

label DocksMafiaStrength:
if selected_power == "useagility":
    jump DocksMafiaAgility
scene docks44 with dissolve
$ usedstrength += 1
play sound "sounds/gun.mp3"
mc "MASSIVE ROCK-HARD ABS FLEX!"
jump DocksMafiaNext

label DocksMafiaAgility:
$ usedagility += 1
scene docks45 with dissolve
play sound "v07/matrixbullet.mp3"
mc "SUPER-BULLET-DODGE!"
jump DocksMafiaNext

label DocksMafiaNoStrength:
scene docks46:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/gun.mp3"
mc "AAAH, I'm hit... Like, CRITICALLY!"
scene blackscreen with fade
show gameovericon:
    xpos 600 ypos 400
pause
return

label DocksMafiaNext:
scene docks47 with dissolve
play sound "sounds/punch.mp3"
mc "And now, take that, Ada!"
scene docks48 with dissolve
mc "And THIS!"
aw "EEEEEH!"

scene docks40 with dissolve
gg "I got her, I got the one with the tits out, boss! It's the first time I don't miss!"
ex "There's still one Triad member left... And Ada Wang isn't dead.... YET."
scene docks49:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
play sound "sounds/gunfire.mp3"
play channel1 "v07/forklift.mp3"
mc "Are you looking at me? Are YOU looking at me? You want some of that too?"
ls "I... No, I 'm out of here!"
mc "That's  what I thought."
scene docks50 with dissolve
ex "Now I'm gonna CRUSH YOU, Ada Wang!"
aw "No!!! [hero], do something, you can't let her kill me in cold blood like this!"
menu:
    "Interfere to stop the killing (+1 Super-Hero)":
        scene docks51 with dissolve
        play sound "sounds/panting.mp3"
        mc "Stop this, Excella! She needs to face the justice of the Justice League! Or the CCPD, or some randomly-assigned judge. But NOT LIKE THIS!"
        call Good
        stop channel1
        $ sparedada = True
        ex "Damn you, [hero], you're no Famiglia man, you're too emotional! But I'll grant you your wish because you are still my bambino..."
        jump MafiaMissionEnd
    "Let Excella dispose of her (+1 Super-Villain)":
        scene docks52 with dissolve
        mc "I ain't seen nothin'. Apart from YOU shooting at me and dying during the ensuing fire exchange, Ada Wang! Your reign of terror is OVER! (* And MINE begins! *)"
        $ sparedada = False
        call Evil
        ex "Bene, bambino, bene. You are a TRUE Famiglia man..."
        stop channel1
            
label MafiaMissionEnd:
scene docks53:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
ex "Gutsy, secure the drug. And give a box to [hero] as a gift for entering the Famiglia..."
window hide
$ inventorydrugs = True
play sound "sounds/achievement.mp3"
show acquiredchromium at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Drugs? And what do they do?"
ex "A libido boost, some memory loss and an increase in heart failures."
mc "That sounds... dangerous."
hide acquiredchromium
if sparedada:
    mc "I'll wait for the cops to hand them Ada Wang and I'll meet you back at the office for my \"reward\"..."
    ex "Sure, bambino, sure..."
if sparedada == False:
    ex "Let's get out of here and head back to the office. You and me, bambino... For your \"reward\"..."

window hide
play sound "sounds/winning.mp3"
show mission08icon at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
$ mission08mafiawin = True
stop channel2
stop music

label MafiaMissionReward:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy09.mp3"
scene mafiareward01 with fade
if seenmafiareward:
    ex "You want some more of my fine Italian ass, don't you [name]?"
    mc "Well, you're in my harem now and I need to take care of my harem girls REGULARLY."
if seenmafiareward == False:
    ex "I guess it's time..."
    mc "That's right, time for some ITALIAN ASS ANAL DESTRUCTION!"
scene mafiareward02 with dissolve
if seenmafiareward:
    ex "And I certainly have my NEEDS. And my ASS TOO."
    mc "Then you found the right Harem Master. I service asses 24/7!"
if seenmafiareward == False:
    ex "The way you put it sounds very brutal... Perhaps I should teach you to be more gentle..."
    mc "Err, it's just that I'm EXCITED!"

scene mafiareward03:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan02.mp3"
if seenmafiareward:
    ex "Mmmh, I know you do... You're such a young handsome STALLIONE..."
    mc "Just show me that fine booty and I'll show you my SUPERHERO cock!"
if seenmafiareward == False:
    ex "Mmmmh, so am I...You're such a young handsome STALLIONE..."
    mc "Just show me that fine booty and I'll show you my SUPERHERO cock!"
scene mafiareward04:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
if age >= 20:
    ex "You MONSTER SUPERHERO cock? The one that will DESTROY my ass?"
if age >= 18 and age <= 19:
    ex "You MONSTER TEENAGE SUPERHERO cock? The one that will DESTROY my ass?"
play sound "sounds/moan04.ogg"
mc "That's right, Excella... Once it gets HARD from feeling that superb rump of yours..."
scene mafiareward05 with dissolve
mc "And to feel it, I need to remove that G-string..."
scene mafiareward06 with dissolve
play sound "sounds/moan02.mp3"
ex "OOOOH!"
scene mafiareward07 with dissolve
play sound "sounds/ripping.mp3"
mc "...FORCEFULLY!"
play sound "sounds/moan05.mp3"
ex "AAAH, you're such a BEAST!"
scene mafiareward08 with dissolve
play sound "sounds/slap.mp3"
ex "I can hear your giant horsedick SLAPPING against your hard pecs!"
play sound "sounds/boymoan.mp3"
mc "Fuck yeah, I'm sssooo HARD!"
scene mafiareward09 with dissolve
mc "Let me check that your ass is nice and wet for my ANAL-DESTROYER!"
play sound "sounds/moan02.mp3"
if seenmafiareward:
    mc "Yeah, even more than last time. You're really looking forawrd toit, aren't you my little cock-slut?"
if seenmafiareward == False:
    ex "Ooooh... Why did I let myself into offering such a reward..."
scene mafiareward10 with dissolve
if seenmafiareward:
    ex "Last time, you totally DESTROYED me. My ass hurt so much..."
if seenmafiareward == False:
    mc "Yeah, I think you're ready, despite your hesitation..."
    ex "I don't know, Maybe we should recons..."
scene mafiareward11:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
if seenmafiareward:
    mc "...Tsss... A harem girl shouldn't complain. It does not please her Harem Master. And I AM YOUR HAREM MASTER!"
    ex "I'm sorry, Master. It's just that... you're so HUGE!"
if seenmafiareward == False:
    mc "...Tsss... A mafiosa's word cannot be taken back. I'm going in no matter what!"
ex "Oh God..."
scene mafiareward12 with dissolve
play sound "sounds/moan03.mp3"
if seenmafiareward:
    mc "You can take it. You took it last time, remember?"
if seenmafiareward == False:
    mc "There, the tip is in... Doesn't feel so bad, does it?"
scene mafiareward13:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan06.ogg"
mc "And a few more inches..."
scene mafiaassprestart:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
play sound "sounds/moan05.mp3"
ex "I can't believe it fits!"
scene mafiaassstart with dissolve
if age >= 20:
    mc "It totaly does, that ass of yours is THICK! A perfect match for my FAT FUCKSTICK!"
if age >= 18 and age <= 19:
    mc "It totaly does, that ass of yours is THICK! A perfect match for my FAT TEENAGE FUCKSTICK!"
window hide

$ mafiaasssoft = True
label MafiaAssSlow:
$ mafiaassfast = False
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
if mafiaasssoft == False:
    ex "Calm down STALLONE! I want it nice and slow please..."
    show mafiaassstart behind mafiaassharderfastvideo
    show mafiaassstart behind mafiaassharderslowvideo
    show mafiaassstart behind mafiaassharderpovfastvideo
    show mafiaassstart behind mafiaassharderpovslowvideo
    $ renpy.pause(0.5, hard=True)
    hide mafiaassharderfastvideo
    hide mafiaassharderslowvideo
    hide mafiaassharderpovslowvideo
    hide mafiaassharderpovfastvideo
    hide mafiaasstransition
    with dissolve
    mc "Alright, I'll show you I can be a GENTLE Harem Master... sometimes."
    $ mafiaasssoft = True        
    $ mafiaassharder = False        
window hide
show mafiaassslowvideo behind mafiaassfastvideo
show mafiaassslowvideo behind mafiaasspovslowvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassfastvideo
hide mafiaasspovslowvideo
with dissolve
play channel2 "sounds/womansex02.mp3"
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassslow()
screen mafiaassslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssPOVSlow")

label MafiaAssFast:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if mafiaassfast == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ mafiaassfast = True
show mafiaassfastvideo behind mafiaassslowvideo
show mafiaassfastvideo behind mafiaasspovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassslowvideo
hide mafiaasspovfastvideo
with dissolve
play channel2 "sounds/womansex03.mp3"
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassfast()
screen mafiaassfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssPOVFast")

label MafiaAssPOVSlow:
play channel2 "sounds/womansex02.mp3"
$ mafiaassfast = False
window hide
hide faster
hide slower
hide pov
hide sceneicon
hide harder
hide softer
hide cum
show mafiaasspovslowvideo behind mafiaassslowvideo
show mafiaasspovslowvideo behind mafiaasspovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassslowvideo
hide mafiaasspovfastvideo
with dissolve
play channel2 "sounds/womansex02.mp3"
show harder:
    xpos 1700 ypos 700    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassslowpov()
screen mafiaassslowpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssPOVFast")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssSlow")

label MafiaAssPOVFast:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
window hide
if mafiaassfast == False:
    ex "Fuck me, fuck me FASTER please, like hubby never could!"
    $ mafiaassfast = True
window hide
show mafiaasspovfastvideo behind mafiaasspovslowvideo
show mafiaasspovfastvideo behind mafiaassfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaasspovslowvideo
hide mafiaassfastvideo
with dissolve
play channel2 "sounds/womansex03.mp3"
window hide
show harder:
    xpos 1700 ypos 700    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassfastpov()
screen mafiaassfastpov():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssPOVSlow")
    button:
        xpos 1700
        ypos 700
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssFast")

label MafiaAssHarderSlow:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
if mafiaassharder == False:
    ex "STALLONE! Give it to me REALLY HARD!"
    show mafiaasstransition behind mafiaassfastvideo
    show mafiaasstransition behind mafiaassslowvideo
    show mafiaasstransition behind mafiaasspovslowvideo
    show mafiaasstransition behind mafiaasspovfastvideo
    $ renpy.pause(0.5, hard=True)
    hide mafiaassslowvideo
    hide mafiaassfastvideo
    hide mafiaasspovslowvideo
    hide mafiaasspovfastvideo
    hide mafiaassstart    
    with dissolve
    mc "Alright, you asked for it!"
    $ mafiaassharder = True
    $ mafiaasssoft = False
window hide
show mafiaassharderslowvideo behind mafiaassharderfastvideo
show mafiaassharderslowvideo behind mafiaassharderpovslowvideo
$ renpy.pause(0.5, hard=True)
stop channel2
play channel2 "v031/womansex08.mp3"
hide mafiaassharderfastvideo
hide mafiaassharderpovslowvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassharderslow()
screen mafiaassharderslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCum")

label MafiaAssHarderFast:     
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderfastvideo behind mafiaassharderslowvideo
show mafiaassharderfastvideo behind mafiaassharderpovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderslowvideo
hide mafiaassharderpovfastvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen mafiaassharderfast()
screen mafiaassharderfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCum")

label MafiaAssHarderPOVSlow:      
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderpovslowvideo behind mafiaassharderslowvideo
show mafiaassharderpovslowvideo behind mafiaassharderpovfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderslowvideo
hide mafiaassharderpovfastvideo
with dissolve
show cum:
    xpos 1750 ypos 1020    
show softer:
    xpos 1700 ypos 300    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen mafiaassharderpovslow()
screen mafiaassharderpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderPOVFast")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCum")

label MafiaAssHarderPOVFast:    
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
window hide
show mafiaassharderpovfastvideo behind mafiaassharderpovslowvideo
show mafiaassharderpovfastvideo behind mafiaassharderfastvideo
$ renpy.pause(0.5, hard=True)
hide mafiaassharderpovslowvideo
hide mafiaassharderfastvideo
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
call screen mafiaassharderpovfast()
screen mafiaassharderpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("MafiaAssHarderPOVSlow")
    button:
        xpos 1700
        ypos 300
        xysize(120, 60)        
        action Jump ("MafiaAssSlow")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("MafiaAssHarderFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("MafiaAssCum")

label MafiaAssCum:
hide cum
hide faster
hide slower
hide harder
hide softer
hide pov
hide sceneicon
with dissolve
ex "Are you going to BLAST THAT LOAD for me, bambino?"
mc "Mamma Mia, si, SI..."
stop channel2
play channel2 "v031/boyorgasm02.mp3"
scene mafiahardcum01 with dissolve
mc "...SI!!!!! AAAH!"
window hide
with vpunch
play sound "sounds/moan05.mp3"
ex "OOOH!"
scene mafiahardcum02 with dissolve
mc "RHAAAAAA!!!!"
window hide
with fastflash
play sound "sounds/splooge01.mp3"
ex "AAAH! SO DEEP!!!"
scene mafiahardcum03:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "Take THAT right up your backside!"
play sound "sounds/splooge01.mp3"
window hide
with fastflash
ex "SO MCUH YOUNG CUM!"
scene mafiahardcum04:
    subpixel True
    xpos -0.01 ypos -0.01 zoom 1
    linear 6 xpos -0.05 ypos -0.05 zoom 1.05
with dissolve
mc "And THAT!!!!"
play sound "sounds/splooge02.mp3"
window hide 
with hpunch
ex "Santissima Madonna!!!!"
scene mafiahardcum05:
    subpixel True
    xpos 0.0
    linear 6.0 xpos -0.1
with dissolve
mc "Damn, I'm cumming so hard, your ass can't take all of it!"
window hide
with fastflash
ex "No ass can hold a load that HUGE!"
scene mafiahardcum06 with dissolve
stop channel2
if seenmafiareward:
    mc "Well, I had hoped your fat booty had been distended enough from last time but I guess not."
if seenmafiareward == False:
    mc "Well, I had hoped your fat booty would."
    ex "Now I have MASSIVE streamers of young spunk all over my back. My hubby is totally cucked..."
scene mafiahardcum07 with dissolve
stop music
stop channel1
play sound "sounds/panting.mp3"
if seenmafiareward:
    mc "And I think my job as Harem Master is done here."
    play sound "sounds/moan03.mp3"
    ex "And a job well done it is..."
if seenmafiareward == False:
    mc "Never mind him. You're in my Harem now. For LIFE."
    $ excellaharem = True
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlexcella at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause            
    play sound "sounds/moan03.mp3"
    ex "Just like you're in the Famiglia... For LIFE."

$ seenmafiareward = True
jump Main