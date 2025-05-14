label Intro:
stop music

label IntroCreation:
play channel1 "sounds/intromusic.mp3"
scene mcintro01:
    subpixel True
    xpos -0.1
    linear 4.0 xpos 0.0
$ renpy.pause(1.0, hard='True')
show mcintro01text:
    xpos 1100 ypos 400
show mcintro01textb:
    xpos 50 ypos 600
"Before you embark on your superhero journey, give yourself a SUPERHERO name."
window hide
$ hero = renpy.input("My Superhero name is...", default = "Alpha-Boy", length = 24)
$ hero = hero.strip()
if not hero:
    $ hero = "Alpha-Boy"
scene mcintro02 with dissolve
show mcintro02textb:
    xpos 900 ypos 800
"And also a first name for more... intimate moments..."
window hide
show mcintro02text:
    xpos 1000 ypos 200    
$ name = renpy.input("My first name is...", default = "Magnus", length = 12)
$ name = name.strip()
if not name:
    $ name = "Magnus"
scene mcintro03 with dissolve
"How old is [hero]?"
window hide
label IntroAgeInput:
$ age = int(renpy.input("My age is...", default = 18, allow="0123456789"))
if 18 <= age <= 25:
    jump IntroNext
jump IntroAgeInput
label IntroNext:
"Here are your starting superpowers... Click over them to discover what they are."
show yoursuperpowers:
    xpos 1200 ypos 50
show nexticon:
    xpos 1750 ypos 1020
call screen intropowers()
screen intropowers():
    modal True
    imagebutton:
        focus_mask True
        idle "icons/introstrengthidle.png"
        hover "icons/introstrengthhover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(1)
    imagebutton:
        focus_mask True
        idle "icons/introseductionidle.png"
        hover "icons/introseductionhover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(2)
    imagebutton:
        focus_mask True
        idle "icons/introstudidle.png"
        hover "icons/introstudhover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(3)
    button:
        xpos 1750
        ypos 1020
        xysize(100, 50)        
        action Jump ("IntroChoosePower")
        
label IntroChoosePower:
hide nexticon
show introstrengthidle
show introseductionidle
show introstudidle
show introresistanceidle
show introsensesidle
show introagilityidle
show introcombatidle
"You may choose an extra power to begin the game. Click on the icon of the superpower you wish to acquire."
call screen introextrapower()
screen introextrapower():
    modal True
    imagebutton:
        focus_mask True
        idle "icons/introresistanceidle.png"
        hover "icons/introresistancehover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(1)
    imagebutton:
        focus_mask True
        idle "icons/introsensesidle.png"
        hover "icons/introsenseshover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(2)
    imagebutton:
        focus_mask True
        idle "icons/introagilityidle.png"
        hover "icons/introagilityhover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(3)
    imagebutton:
        focus_mask True
        idle "icons/introcombatidle.png"
        hover "icons/introcombathover.png" hovered Play("sound", "sounds/rollover.mp3")
        action Return(4)
$ extrasuperpower = _return
if extrasuperpower == 1:
    $ extrapower = "Super-Resistance"
    $ mcresistance = 1
if extrasuperpower == 2:
    $ extrapower = "Super-Senses"
    $ mcsenses = 1
if extrasuperpower == 3:
    $ extrapower = "Super-Agility"
    $ mcagility = 1
if extrasuperpower == 4:
    $ extrapower = "Super-Combat"
    $ mccombat = 1
stop channel1

play channel1 "sounds/suspense.mp3"
scene cockhamintro01
show introwatch01:
    xpos 520 ypos 200
show introskippart02:
    xpos 500 ypos 350
show introskipgame:
    xpos 620 ypos 500
show introgallerytext:
    xpos 100 ypos 900
show introvoicetext:
    xpos 1350 ypos 900
show introskiplevel:
    xpos 450 ypos 650
with dissolve

call screen intro02()
screen intro02():
    modal True
    button:
        xpos 520
        ypos 200
        xysize(770, 90)        
        action Jump ("Intro01")
    button:
        xpos 500
        ypos 350
        xysize(770, 80)        
        action Jump ("Intro02")
    button:
        xpos 620
        ypos 500
        xysize(490, 80)        
        action Jump ("IntroGame")
    button:
        xpos 450
        ypos 650
        xysize(700, 80)        
        action Jump ("IntroGameLevel02")

label IntroGameLevel02:
scene lab14 with dissolve
show texthero:
    xpos 200 ypos 600
show textvillain:
    xpos 500 ypos 600
show textchooseroute:
    xpos 200 ypos 400
call screen chooseroutescreen()
screen chooseroutescreen():
    modal True
    button:
        xpos 200
        ypos 600
        xysize(200, 80)        
        action Return(1)
    button:
        xpos 500
        ypos 600
        xysize(200, 80)        
        action Return(2)
$ choseroute = _return
if choseroute == 1:
    $ evilness = 5
    $ mccombat = 2
    $ widowpicked = True
    $ mission02win = True
    $ frostchosegood = True
    $ nicegymsuperman = True
    $ loisgood = True
    $ dreamangel = 0
    
if choseroute == 2:
    $ evilness = 15
    $ mcmind = 1
    $ frostpicked = True
    $ mission02fail = True
    $ choseevilphoto = True
    $ frostchoseevil = True
    $ loisevil = True
    $ dreamdemon = 0
    $ hulkescaped = True
 
$ metivy = True
$ supergirltraining = False
$ agtoldmassage = True
$ seentriad = True

$ day = 20
$ usedcombat = 1
$ usedseduction = 1
$ usedstrength = 1
$ usedagility = 2
$ usedstudliness = 1
$ usedsenses = 2
$ helpedpowergirl = True

$ dreamfrost = True
$ mission02dream = True
$ dreammission03 = True

$ mcagility = 1
$ mcstrength = 2
$ mcsenses = 1
$ mcseduction = 2
$ mcresistance = 1
$ seenstroheimwonder = True
$ supergirltraining = True
$ sawharley = True
$ lpspeakhq01 = True
$ lpspeak01 = True
$ locmayors = True
$ loclingerie = True
$ locstallion = True
$ loclois = True
$ locquiff = True
$ locsirens = True
$ locnazi = True
$ locarkham = True
$ locivy = True
$ mission01end = True
$ mission01win = True
$ mission01 = True
$ sawpicked = True
$ sawbmasturbation = True
$ mctoldauditlingerie = True
$ seentitmassage = True
$ mission02 = True
$ mission02end = True
$ milftoldmission02end = True
$ seenbeatbarr = True
$ fleeghost = True
$ mission04 = True
$ knowlingerie = True
$ mission04win = True
$ toldmilfharley = True
$ mission04end = True
$ mission04debrief = True
$ frosttoldmc = True

$ seenmilfyoga = True
$ mission03 = True
$ mission03end = True
$ mission03win = True
$ seenmilfseduction = True
$ seenmilfmaledom = True
$ toldmilfmission04 = True
$ toldmilffrost = True
$ questhulk = True
$ questhulkcompleted = True
$ spokemilfshehulk = True
$ gotmassage = True
$ smspeak02 = True
$ smspeak01 = True
$ smspeak03 = True
$ mission01win = True

$ inventorytwister = True
$ inventoryhandcuffs = True
$ inventorykryptonite = True
$ inventorylustring = True
$ inventorygoldtrunks = True
$ inventoryhitlerball = True
$ inventorysedative = True
$ inventorywhip = True
$ inventoryvine = True
$ inventoryantidote = True

$ frostfirstvisit = True
$ frosttrainedresistance = True
$ seenwonderbeast = True
$ wondertrain01 = True
$ seenwonderbeast = True
$ seenwonderagility = True
$ gymwidowspar = True
$ combattraining = 2
$ seenmilfgymendlevel01 = True
$ hulksexneed = 0
$ seenhulk01 = True
$ agspeak05 = True
$ questtwister = True
$ wonderquesttipaudit = True
$ agspeak06 = True
$ agstink = 0
$ sawghost = True
$ seensupergirl = True
$ seensuperpowergirl = True
$ seenloisflat = True

$ seenmafia = True
$ seenmafiasecond = True
$ mafiatalked = True
$ seenexcellalingerie = True
$ spokemilfshehulk = True
$ spokemayorshehulk = True

$ pgroomsneaked = True
$ powerlingerie = True
$ pgspeak05 = True
$ poolmcspeak01 = True
$ widowpoolsaid = True
$ seenpowerpool = True
$ seentabitha = True
$ seentabithastrip = True
$ seenbarbarastrip = True
$ spokebarbaramission03 = True
$ waitertrained = True
$ playedtwister = True
$ wondertalkbaby = True
$ wondertalkpregnant = True

stop channel1
jump Level02lab

label Intro01:
play channel2 "sounds/nightsounds.mp3"
scene cockhamintro01:
    subpixel True
    xpos -0.1
    linear 4.0 xpos 0.0
with fade
voice "narrator/intro01"
nar "Cockham City. A grim metropolis where crime is rife..."
scene cockham02a with dissolve
play sound "sounds/gunfire.mp3"
voice "narrator/intro02"
nar "Gang warfare..."
play sound "sounds/gunfire.mp3"
st "--. The Narrows are MINE, MOTHAFUCKAS!"
scene cockham02b with dissolve
voice "narrator/intro03"
nar "Bank robberies..."
play sound "sounds/gun.mp3"
jo "Why so serious? It's just a withdrawal..."
scene intromugging01 with dissolve
stop sound
voice "narrator/intro04"
nar "...Muggings of innocent wives and mothers in broad nightlight..."
scene intromugging02 with dissolve
voice "narrator/intro05"
nar "...Followed by SEX CRIME. The biggest scourge of Cockham."
so "No, please! Just mug me and don't rape me, I'm a game virgin!"
th "All the better! We're gonna milk this big time!"
scene intromugging03 with dissolve
so "AAAH, no! I haven't had sex for like, three years at least!"
voice "narrator/intro06"
nar "Who will fight the dark (sex) underworld of Cockham City?"
show cockham01:
    subpixel True
    zoom 1.2 xpos 0.0 ypos -0.15
    linear 10.0 xpos -0.1 ypos 0.0
show supermanintro01
with dissolve
voice "narrator/intro07"
nar "Not this guy, he doesn't even have a dick."
hide supermanintro01
show supermanintro02
with fastdissolve
sm "It's not my fault if reproduction is different on Krypton!"
scene cockhamintro02 with dissolve
voice "narrator/intro08"
nar "And this dude is just a billionnaire with a fancy car, he doesn't even have real superpowers."
scene cockhamintro03 with fastdissolve
bm "Hey! That's not fair, I can fly! Like... a bit. For a short while."
voice "narrator/intro09"
nar "No, Cockham City needs a REAL (sex) superhero."
stop channel1
stop channel2

stop music
scene league01 with fade
voice "milf/intro01"
cm "Cockham needs a REAL superhero to fight organized sex crime!"
scene league02 with dissolve
voice "widow/intro01"
bw "Yeah, I agree, I'm sick and tired of these perverts staring at my tits every time I go on a mission!"
scene league03 with dissolve
voice "power/intro01"
pg "And can we count on these two doofuses? Oh no, they're too busy fighting the same villains over and over again..."
scene league19 with dissolve
voice "superman/intro01"
sm "It's not my fault Sexy Luthor keeps escaping!"
scene league10 with dissolve
voice "batman/intro01"
bm "Can someone remind me which villain I'm supposed to be fighting, cos I get confused..."
scene league05 with dissolve
voice "milf/intro02a"
cm "Listen up! As you may know, I have been working on my superhero body enhancement radiation machine for a while now."
voice "milf/intro02b"
cm "And I've managed to create the PERFECT superhero for our cause!"
scene league06 with dissolve
voice "power/intro02"
pg "Alright! Hurray to our League Captain!"
scene league07 with dissolve
voice "superman/intro02"
sm "What an asslicker! *snickers*"
voice "batman/intro02"
bm "Yeah, like, totally..."
scene league03 with dissolve
voice "power/intro03"
pg "I heard that! I have super-hearing remember, douchebags?"
scene league09 with dissolve
voice "milf/intro03"
cm "Since I couldn't find any volunteer to enter my dangerous machine, I experimented on my landboy."
scene league10 with dissolve
voice "batman/intro03"
bm "What, she has a landboy?"
scene league11 with dissolve
voice "superman/intro03a"
sm "Housing is real expensive in Cockham, makes sense she would want to share her apartment to make a bit of money on the side."
voice "superman/intro03b"
sm "Not that you would know anything about the economic strife of the average person..."
scene league12 with dissolve
voice "milf/intro04"
cm "So let me introduce the new addition to our League of Justice!"
play sound "sounds/drumroll.mp3"
scene leaguemc01 with dissolve
$ renpy.pause(2.0, hard='True')
voice "batman/intro04"
bm "Pff, he's just a boy. Let me guess, he can turn water into ice cubes?"
scene league13 with dissolve
voice "superman/intro04"
sm "Ha ha, nice one Batman, his superhero name is probably Cocktail Boy!"
voice "batman/intro05"
bm "Hey, Cocktail Boy, I need some ice for my martini!"
scene leaguemc02 with dissolve
play sound "sounds/audiencegasp.mp3"
mc "Hi everyone, I'm [hero]."
voice "milf/intro05"
cm "You were saying, BOYS?"
scene league10 with dissolve
voice "batman/intro06"
bm "What the fuck???"
scene league14 with dissolve
voice "widow/intro02"
bw "Now THAT's what I call an ALPHA-COCK!"
scene league15 with dissolve
voice "wonder/intro01"
ww "Sorry to have to ask. But apart from possessing an oversized phallus and a superhero sign on his barely-concealing thong, what exactly are [hero]'s superpowers?"
scene league09 with dissolve
if extrapower == "Super-Agility":
    voice "milf/intro06a"
if extrapower == "Super-Combat":
    voice "milf/intro06b"
if extrapower == "Super-Senses":
    voice "milf/intro06c"
if extrapower == "Super-Resistance":
    voice "milf/intro06d"
cm "He is level 1 on the Marvel Superpowers Scale for Super-Strength, [extrapower], Super-Seduction and..."
scene league16 with dissolve
voice "milf/intro07"
cm "...Super-Studliness."
scene league17 with dissolve
voice "power/intro04"
pg "Super-Studliness? I never heard of that superpower, what is it?"
scene league05 with dissolve
voice "milf/intro08"
cm "His cock can maintain unlimited erections and he will, shall we say, leave his sexual partners... blissfully satisfied. Which will be very useful on his missions."
scene league18 with dissolve
voice "widow/intro03"
bw "That's a superpower Superman will NEVER have. *snickers*"
scene league19 with dissolve
voice "superman/intro05"
sm "Can he fly? No, he doesn't have a cape so he can't fly. He's not a REAL superhero then."
scene league20 with dissolve
voice "batman/intro07"
bm "That's right. Only flying heroes are superheroes. I can fly. A bit. So I'm a superhero. And he's NOT."
scene league01 with dissolve
voice "milf/intro09a"
cm "ENOUGH! I'm the Captain here and I have decided that he will join our League of Justice! And that is FINAL."
voice "milf/intro09b"
cm "Now you two, concentrate on fighting your arch-enemies and let [hero] take care of SEX CRIME in Cockham."
scene league05 with dissolve
voice "milf/intro10"
cm "And remember to get ready for tonight's Charity Ball at Vayne Tower. We head there in an hour."

label IntroLeagueHall:
stop music
play music "sounds/piano01.mp3"
scene allleaguedialogues with fade
"Get to know the other members of the Cockham League of Justice by talking to them. Start with Captain MILF."
jump IntroLeagueHallc
label IntroLeagueHallb:
scene allleaguedialogues with fade
if agspeak04:
    jump EndIntroLeague
label IntroLeagueHallc:
play music "sounds/piano01.mp3"
call screen introleague()
screen introleague():
    modal True
    imagebutton:
        focus_mask True
        idle "intro/allleaguemilfidle.png"
        hover "intro/allleaguemilfhover.png"
        action Jump ("AllLeagueCaptain")
    if spokemilfleague and spokeleaguewidow == False:
        imagebutton:
            focus_mask True
            idle "intro/allleaguewidowidle.png"
            hover "intro/allleaguewidowhover.png"
            action Jump ("AllLeagueWidow")
    if spokemilfleague and spokeleaguepower == False:
        imagebutton:
            focus_mask True
            idle "intro/allleaguepoweridle.png"
            hover "intro/allleaguepowerhover.png"
            action Jump ("AllLeaguePowerGirl")
    if spokemilfleague and spokeleaguewonder == False:
        imagebutton:
            focus_mask True
            idle "intro/allleaguewonderidle.png"
            hover "intro/allleaguewonderhover.png"
            action Jump ("AllLeagueWonder")
    if spokemilfleague and spokeleaguesuper == False:
        imagebutton:
            focus_mask True
            idle "intro/allleaguesuperidle.png"
            hover "intro/allleaguesuperhover.png"
            action Jump ("AllLeagueSuperman")
    if spokemilfleague and spokeleaguebatman == False:
        imagebutton:
            focus_mask True
            idle "intro/allleaguebatmanidle.png"
            hover "intro/allleaguebatmanhover.png"
            action Jump ("AllLeagueBatman")
    if spokeleaguesuper and spokeleaguebatman and spokeleaguewonder and spokeleaguepower and spokeleaguewidow:
        imagebutton:
            focus_mask True
            idle "intro/allleagueauditidle.png"
            hover "intro/allleagueaudithover.png"
            action Jump ("AllLeagueAudit")

label AllLeagueAudit:
stop music
scene allleaguechair
show auditeyeblink
with dissolve

label AGDialogueLeague:
menu:
    "So you're that new intern, Audit Girl." if agspeak01 == False:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        $ agspeak01 = True
        voice "audit/intro01"
        ag "Yes, that's me! Nice to meet you... [hero]."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "I sure have a better superhero name than you, don't you think?"
        scene allleaguechair
        show allleagueaudit02
        with fastdissolve
        voice "audit/intro02"
        ag "Y... Yes, you do. I didn't get to choose mine, the dev did."
        mc "What a dick."
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        jump AGDialogueLeague        
    "What are your superpowers exactly?" if agspeak01:
        voice "audit/intro03"
        ag "I... I can do.... mental stuff real fast. Like auditing for example."
        mc "Ah. Interesting. I'm sure that'll come in handy one day."
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        voice "audit/intro03b"
        ag "I... I hope so too."
        hide allleagueaudit03
        show allleagueaudit04
        with fastdissolve
        voice "audit/intro04"
        ag "I have healing powers too. Level 3. If you ever get... injured, I could try and help..."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "Now we're talking! Do you also do massages?"
        scene allleaguechair
        show allleagueaudit02
        with fastdissolve
        voice "audit/intro05"
        ag "Well, err... If that can help you..."
        mc "Maybe it will, maybe it will. We'll have to find out. *wink*"
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        jump AGDialogueLeague
    "You seem to be very shy. Unusual for a superhero." if agspeak01:
        hide auditeyeblink
        show allleagueaudit02
        with fastdissolve
        voice "audit/intro06"
        ag "I... don't know if I belong here. I don't have much experience being a superheroine."
        mc "I'm sure you'll fit in, don't worry."
        hide allleagueaudit02
        show allleagueaudit04
        with fastdissolve
        voice "audit/intro07"
        ag "Thank you, ...[hero]."
        hide allleagueaudit04
        show auditeyeblink
        with fastdissolve
        jump AGDialogueLeague
    "How did you end up in the Cockham League of Justice?" if agspeak01 and agspeak02 == False:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        $ agspeak02 = True
        voice "audit/intro08"
        ag "I just graduated from the Xavier School for the Super-Gifted with the top grades of my class."
        hide allleagueaudit04
        show allleagueaudit03
        with fastdissolve
        voice "audit/intro09"
        ag "And... since most of the other students in my year ended up dead, Captain MILF asked me to join for an internship."
        mc "What? What happened?"
        hide allleagueaudit03
        show allleagueaudit05
        with fastdissolve
        voice "audit/intro10"
        ag "One guy could burst into flames. He set the school on fire by mistake one night and twenty students died."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit05b
        with fastdissolve        
        voice "audit/intro11"
        ag "I didn't manage to use my Super-Healing abilities to save them because I was away on a field trip to the Cockham library."
        scene allleaguechair
        show allleagueaudit03
        with fastdissolve        
        voice "audit/intro12"
        ag "So I feel guilty about that..."
        mc "You shouldn't, it wasn't your fault that idiot set the school on fire."
        hide allleagueaudit03
        show allleagueaudit05
        with fastdissolve
        voice "audit/intro13"
        ag "And then there was that girl, if you touched her, you would die. Ten students passed away during prom night. And she was kicked out."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit05b
        with fastdissolve        
        voice "audit/intro14"
        ag "So I was kind of the only one left..."
        mc "Well, we sure are glad to have you here rather than another freaky mutant student with a totally lame super-power." 
        scene allleaguechair
        show allleagueaudit04
        with fastdissolve        
        voice "audit/intro15"
        ag "Thank...you... That is vey nice of you to say."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        voice "audit/intro16"
        ag "I'm very happy that YOU are here too... If I may say so, [hero]."
        mc "Thank you for your kind welcome. Audit Girl."
        scene allleaguechair
        show auditeyeblink
        with fastdissolve        
        voice "audit/intro17"
        ag "My name is.... Kayla."
        mc "And I'm [name]."
        jump AGDialogueLeague
    "Will you be coming to the Charity Ball, Audit Girl?" if agspeak01 and agspeak03 == False:
        $ agspeak03 = True
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        voice "audit/intro18"
        ag "No... I don't even have a costume... I never go out of the compound..."
        mc "Oh. Then we'll have to find you one. I'm sure we can come up with something that you'll like and that befits your...err... nerdy superpowers."
        hide allleagueaudit03
        show auditeyeblink
        with fastdissolve
        voice "audit/intro19"
        ag "Uh... Okay. thank you... [hero]."
        jump AGDialogueLeague
    "You have a dossier for me?" if agspeak03 and agspeak02:
        $ agspeak04 = True
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        voice "audit/intro20"
        ag "Yes. I compiled it for you..."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "OK, well, where is it?"
        voice "audit/intro21"
        ag "It's right here in my hands."
        mc "Well, let's have a look at it, shall we?"
        scene allleaguechair
        show allleagueaudit05
        with fastdissolve        
        voice "audit/intro22"
        ag "O...Okay. The first blue folder contains what I have compiled on every known sexually depraved super-villain in Cockham."
        show folderblueidle
        mc "Right, that's great and will be very useful."
        hide allleagueaudit05
        show auditeyeblink
        with fastdissolve
        voice "audit/intro23"
        ag "And the second red folder contains info on... each of us. And our allies. Both folders will automatically update every time you learn something new."
        show folderredidle
        mc "Perfect. Let me have a look at these folders then. Err... How do I open them?"
        hide auditeyeblink
        show allleagueaudit05
        with fastdissolve
        voice "audit/intro24"
        ag "You have to click on the red or blue folder icon in the top left of your screen."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show folderredidle
        show folderblueidle
        show allleagueaudit05b
        with fastdissolve        
        mc "What, I'm in a screen? Someone's filming us?"
        scene allleaguechair
        show folderredidle
        show folderblueidle
        show allleagueaudit03
        with fastdissolve        
        voice "audit/intro25"
        ag "Yes, the dev. He's just a dirty pervert if you ask me... He keeps zooming in on my tits. I think he should be added to the blue folder but he refuses."
        mc "Oh, that was him? I thought it was me. Well, I'll leave you and get his camera out of your... ample cleavage then."
        hide allleagueaudit03
        show auditeyeblink
        with fastdissolve  
        voice "audit/intro26"
        ag "Uh, okay. Goodbye [name]."
        mc "See you around, Kayla."
        window hide
        hide folderredidle
        hide folderblueidle
        show screen folders
        pause
        pause
        jump EndIntroLeague

label AllLeagueBatman:
stop music
scene allleaguewindow
show allleaguebatman01 at center with dissolve:
    breathe
 
label BMDialogueLeague:
menu:
    "So you're Bruce Vayne in real life, right?" if bmspeak01 == False:
        hide allleaguebatman01
        show allleaguebatman03
        with fastdissolve
        $ bmspeak01 = True
        voice "batman/intro08"
        bm "And this is a SECRET. So don't tell anyone. Cos I'm super-rich and I could really HURT YOU if you did."
        hide allleaguebatman03
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        mc "Right, right..."
        jump BMDialogueLeague        
    "What are your superpowers Batman? If you have any that is...":
        hide allleaguebatman01
        show allleaguebatman02
        with fastdissolve
        voice "batman/intro09"
        bm "I DO, contrary to what the dev wrongfully implied in the intro!"
        hide allleaguebatman02
        show allleaguebatman03
        with fastdissolve
        voice "batman/intro10"
        bm "I CAN actually fly. A bit at least. So I'm level 1 in Super-Flight."
        mc "Alright, but you have a specially designed cape, so it's not a REAL superpower."
        hide allleaguebatman03
        show allleaguebatman02
        with fastdissolve
        voice "batman/intro11"
        bm "It's irrelevant! You CAN'T FLY, so you'd better show some RESPECT for us FLYING SUPERHEROES!"
        hide allleaguebatman02
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        voice "batman/intro12"
        bm "Or maybe I'll use my SUPER-COMBAT abilities on YOU. Level 1 to be more precise."
        mc "Whatever. I've got bigger muscles than you, I'd beat you anytime, any place."
        hide allleaguebatman01
        show allleaguebatman04
        with fastdissolve
        voice "batman/intro13"
        bm "If you tried to hit me, you'd find that your fist just hits my TITANIUM-HARD armor and it would hurt YOU."
        mc "Well, I've got something else that's titanium-hard... Whenever I want to. As Captain MILF rightfully mentioned."
        hide allleaguebatman04
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        voice "batman/intro13b"
        bm "Yeah, whatever."
        jump BMDialogueLeague
    "I hear the Joker is still running loose." if bmspeak02 == False:
        hide allleaguebatman01
        show allleaguebatman03
        with fastdissolve
        $ bmspeak02 = True
        voice "batman/intro14"
        bm "Yeah, so? I'll CATCH him one day, rest assured. Him and his filthy WHORE, Harley Quiff."
        hide allleaguebatman03
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        mc "I can't wait for that to happen..."
        jump BMDialogueLeague
    "Is it really dark around here or is it you?":
        hide allleaguebatman01
        show allleaguebatman03
        with fastdissolve
        voice "batman/intro15"
        bm "Both. It's really dark and I like it. You have a problem with that?"
        mc "Err, no. But I see it's a useful skill for a pervert to sneak on his preys from behind."
        hide allleaguebatman03
        show allleaguebatman02
        with fastdissolve
        voice "batman/intro16"
        bm "I'm not a PERVERT! But I do sneak on people. My enemies or those who piss me off for example... Hence my Level 1 in Super-Agility, which consists mainly in sneaking."
        hide allleaguebatman02
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        mc "I see..."
        jump BMDialogueLeague
    "Where's your batmobile?":
        hide allleaguebatman01
        show allleaguebatman04
        with fastdissolve
        voice "batman/intro17"
        bm "It's hidden so YOU can never drive it! HA HA HA!"
        mc "That's just nasty. Superheroes are supposed to help each other."
        hide allleaguebatman04
        show allleaguebatman02
        with fastdissolve
        voice "batman/intro18"
        bm "I don't consider you one of US, got it?"
        hide allleaguebatman02
        show allleaguebatman01
        with fastdissolve
        show allleaguebatman01 at center:
            breathe
        jump BMDialogueLeague
    "I'm done here.":
        hide allleaguebatman01
        show allleaguebatman04
        with fastdissolve
        voice "batman/intro19"
        bm "Don't let the door hit you on your way out."
        $ spokeleaguebatman = True
        jump IntroLeagueHallb

label AllLeagueCaptain:
stop music
scene allleaguedesk
show allleaguemilf01 at centerleft with dissolve:
    breathe

label CMDialogueLeague:
menu:
    "What exactly will my duties entail?" if cmspeak02 == False:
        $ cmspeak02 = True
        hide allleaguemilf01
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro11"
        cm "Since I have assigned you to the SEX CRIME division, you will be in charge of fighting SEX CRIME in Cockham City."
        mc "Ok, but like what kind of crime exactly? I'm not a police detective or anything."
        hide allleaguemilf02
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro12a"
        cm "Some supervillains are known to lead a life of SEXUAL DEPRAVITY. So you will have many strong enemies to FIGHT. And DEFEAT."
        voice "milf/intro12b"            
        cm "Every now and then, the CCPD (that's the Cockham City Police Department) might ask us for assistance. If we are talking about a SEX CRIME, then I might assign the mission to YOU!"
        hide allleaguemilf05
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        jump CMDialogueLeague
    "Why did you say that my massive teenage cock would be helpful on missions??" if cmspeak02 and age >= 18 and age <=19:
        hide allleaguemilf01
        show allleaguemilf03 at centerleft
        with fastdissolve
        voice "milf/intro13"
        cm "Well, err... I just blurted it out to justify giving you such an appendage! But I'm SURE it WILL! I mean, it's just sssooo BIG. And yummy..."
        mc "I think you're... drooling a bit."
        hide allleaguemilf03
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        jump CMDialogueLeague
    "Why did you say that my massive cock would be helpful on missions?" if cmspeak02 and age >= 20:
        hide allleaguemilf01
        show allleaguemilf03 at centerleft
        with fastdissolve
        voice "milf/intro13"
        cm "Well, err... I just blurted it out to justify giving you such an appendage! But I'm SURE it WILL! I mean, it's just sssooo BIG. And yummy..."
        mc "I think you're... drooling a bit."
        hide allleaguemilf03
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        jump CMDialogueLeague
    "What are your superpowers?":
        hide allleaguemilf01
        show allleaguemilf04 at centerleft
        with fastdissolve
        voice "milf/intro16a"
        cm "As the Captain of this league of Superheroes, I am a TRUE superhero able to FIGHT and WITHSTAND ATTACKS from our enemies."
        voice "milf/intro16b"
        cm "Therefore, I am level 1 in Super-Agility and 2 in Super-Strength."
        hide allleaguemilf04
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro17"
        cm "But most importantly, I am level 3 in Super-Resistance and am totally immune to all forms of toxins and mental disturbances. Including from YOU."
        mc "Well, I have no superpowers in mind control anyway. Apart from Super-Seduction, which I guess is a form of mind control."
        hide allleaguemilf05
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        voice "milf/intro18"
        cm "I suppose it is...  I also have certain... seduction powers by the way. Level 3 to be more precise..."
        mc "Wow! You've got so many superpowers. You can fly too I presume?"
        hide allleaguemilf01
        show allleaguemilf03 at centerleft
        with fastdissolve
        voice "milf/intro19"
        cm "Uhm... No. I'm scared of heights actually. One of my weaknesses I'm afraid."
        mc "Oh, superheroes have weaknesses?"
        hide allleaguemilf03
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro20"
        cm "Sure. Yours is that you are unsure where you stand. You might be tempted by EVIL. I'm warning you though. DON'T BE TEMPTED BY EVIL."
        mc "Roger that, Chief."
        hide allleaguemilf02
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        voice "milf/intro21a"
        cm "Captain to you. Or Carol if you prefer."
        mc "Roger that, Captain."
        jump CMDialogueLeague
    "Will you come with me on missions?" if cmspeak01 == False:
        hide allleaguemilf01
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro22"
        cm "Why? Don't you feel you are able to fight sex crime alone?"
        mc "Well, I'm new to this superhero stuff..."
        hide allleaguemilf02
        show allleaguemilf04 at centerleft
        with fastdissolve
        voice "milf/intro23"
        cm "Fine, I'll come along for your first mission. But then you're on your own. I'm super-busy managing this compound."
        mc "Okay, thanks Captain MILF!"
        hide allleaguemilf04
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        voice "milf/intro24a"
        cm "You can call me Carol. As your landlady, I think it's appropriate to call each other by our first names."
        mc "Right. Sure, Carol!"
        $ cmspeak01 = True
        jump CMDialogueLeague
    "So, when do I get to go on a mission?":
        hide allleaguemilf01
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro25"
        cm "What does your mission log say?"
        mc "Err. Nothing, it's empty."
        hide allleaguemilf02
        show allleaguemilf04 at centerleft
        with fastdissolve
        voice "milf/intro26"
        cm "Then you don't have a mission do you? Wait for some worthy SEX CRIME to be reported. It shouldn't take too long in this city full of scummy super-villains."
        mc "Okay... But what can I do while I wait?"
        hide allleaguemilf04
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro27"
        cm "You can train in the gym to maintain your Super-Strength. I go there at least twice a week since I'm level 2 in Super-Strength. You should go at least once a week."
        mc "I'm starting to get where this game is going..."
        hide allleaguemilf05
        show allleaguemilf04 at centerleft
        with fastdissolve
        voice "milf/intro28"
        cm "Or you could train with the Black Widow when she's around to increase your Super-Combat stats."
        hide allleaguemilf04
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro29"
        cm "Finally, you can hang out at the pool or the jaccuzzi or read here. We have a wonderful library."
        mc "What about just hanging out in the city and getting the feel of it?"
        hide allleaguemilf02
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro30"
        cm "Yes, you can do that too. You go to the wall map over there and you pick an area. Some might be off-limits at this stage. You're a novice. And your costume is kinda lewd."
        mc "Hey! You gave it to me!"
        hide allleaguemilf05
        show allleaguemilf03 at centerleft
        with fastdissolve
        voice "milf/intro31"
        cm "I know. I couldn't help myself when I saw how... BIG your cock was!"
        mc "Yeah, it's quite impressive isn't it?"
        hide allleaguemilf03
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro32"
        cm "Y... Yes. Damn it boy, you KNOW it is! It's a fucking gorgeous piece of MASSIVE MANMEAT! There, I said it."
        mc "So you did. So you did..."
        hide allleaguemilf02
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        jump CMDialogueLeague
    "How do I become even more buff and hung?":
        hide allleaguemilf01
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro33"
        cm "You must first train with other superheroes of higher levels of various superpowers and fulfill missions and quests."
        hide allleaguemilf02
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro34"
        cm "Once you are ready to reach Superhero Level 2, we will test my superhero body enhancement radiation machine on you again. Then, you should become more muscular and... hung."
        hide allleaguemilf05
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        mc "Alright! That sounds like a plan."
        jump CMDialogueLeague
    "How come I don't see Captain Canuck?" if cmspeak03 == False:
        $ cmspeak03 = True
        hide allleaguemilf01
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro35"
        cm "Captain who???"
        mc "Captain Canuck, you know. The FAMOUS Canadian superheroine."
        hide allleaguemilf05
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro36"
        cm "I never heard of her and I know ALL superheroes. I think you're imagining things. Plus, I'm the Captain here."
        hide allleaguemilf02
        show allleaguemilf01 at centerleft
        with fastdissolve        
        show allleaguemilf01 at centerleft:
            breathe
        mc "I could have sworn it was a superhero that existed for some reason..."
        jump CMDialogueLeague
    "I'm done here.":
        hide allleaguemilf01
        show allleaguemilf02 at centerleft
        with fastdissolve
        voice "milf/intro37"
        cm "Go and speak with the other superheroes. And once you're done, talk to Audit Girl, she has a dossier prepared for you."
        mc "Audit Girl? Who is that?"
        hide allleaguemilf02
        show allleaguemilf04 at centerleft
        with fastdissolve
        voice "milf/intro38"
        cm "She's the new intern."
        mc "Okay. I didn't know we took interns into the League..."
        hide allleaguemilf04
        show allleaguemilf05 at centerleft
        with fastdissolve
        voice "milf/intro39"
        cm "They are much cheaper than full superhero employees."
        $ spokemilfleague = True
        jump IntroLeagueHallb
        
label AllLeaguePowerGirl:
stop music
scene allleaguepiano blurred
show powereyeblink
with dissolve

label PGDialogueLeague:
menu:
    "Hi Powergirl. I'm [name], nice to meet you. And your little name is?..." if pgspeak01 == False:
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        $ pgspeak01 = True
        voice "power/intro06"
        pg "My name is Kara. Or Karen if you prefer. But I'd rather you called me Kara to be honest, I feel like Karen might not go down in history as such a good name."
        mc "What a lovely name. As lovely as you are..."
        hide allleaguepower04
        show powereyeblink
        with fastdissolve
        voice "power/intro07"
        pg "Are you trying to seduce me [name]? It might take a while to succeed..."
        jump PGDialogueLeague
    "Remind me what your superpowers are?":
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        voice "power/intro10"
        pg "I have MULTIPLE superpowers."
        mc "Yeah, okay. So do I."
        hide allleaguepower04
        show allleaguepower05
        with fastdissolve
        voice "power/intro11"
        pg "I'm SUPER-STRONG for starters. Level 1 but still."
        mc "Yeah, okay, same as me. What else?"
        hide allleaguepower05
        show powereyeblink
        with fastdissolve
        voice "power/intro12"
        pg "I have SUPER-SENSES. I can see through walls - but not metal - and I can hear through walls. Except if they are made of metal obviously."
        mc "Obviously."
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        voice "power/intro13"
        pg "I also have super-resistance. To fire, ice and lightning bolts. Pretty neat, hey?"
        mc "Ah, okay, that's what that super-power is for, I was wondering."
        hide allleaguepower04
        show powereyeblink
        with fastdissolve
        voice "power/intro14"
        pg "It can also be used to resist mind control attempts, but I don't have that ability."
        mc "Too bad."
        hide powereyeblink
        show allleaguepower05
        with fastdissolve
        voice "power/intro15"
        pg "But I can FLY! Right through the air like a speeding bullet. Except in turbulent weather obviously."
        mc "Obviously."   
        hide allleaguepower05
        show powereyeblink
        with fastdissolve
        voice "power/intro16"
        pg "And I'm a super-fighter too. Oh, and I have big tits. Double DDs. You like them?"
        mc "Obviously."
        voice "power/intro17"
        pg "Good."
        jump PGDialogueLeague
    "So you can play the piano?" if pgspeak02 == False and pgspeak01:
        $ pgspeak02 = True
        hide powereyeblink
        show allleaguepower02
        with fastdissolve
        voice "power/intro20"
        pg "Yes, I'm level 1 in Super-Piano. Still improving but listen to this."
        window hide
        hide allleaguepower02
        show allleaguepower03a
        with fastdissolve
        play music "sounds/piano02.mp3"
        while pianocount <= 5:
            hide allleaguepower03a
            show allleaguepower03b
            with fastdissolve
            hide allleaguepower03b
            show allleaguepower03a
            with dissolve
            hide allleaguepower03a
            show allleaguepower03b
            with dissolve
            hide allleaguepower03b
            show allleaguepower03a
            with fastdissolve
            $ pianocount += 1
        stop music
        hide allleaguepower03a
        show powereyeblink
        with fastdissolve
        voice "power/intro21"
        pg "So, what do you think?"
        mc "Impressive. Completely useless but impressive."
        jump PGDialogueLeague
    "Will you be coming with me on missions?" if pgspeak03 == False:
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        $ pgspeak03 = True
        voice "power/intro22"
        pg "Maybe. I don't have many enemies. I'm so nice, even super-villains stay clear of me."
        mc "I see. Then, you shall fight SEX CRIME with me! Together, we shall take on the filthy underbel..."
        hide allleaguepower04
        show allleaguepower02
        with fastdissolve
        voice "power/intro23"
        pg "Hang on a minute. I do have other assignments. Like I need to train my piano skills and increase my mental resistance through intensive yoga sessions. So only if I'm not busy."
        mc "But how will I know?"
        hide allleaguepower02
        show powereyeblink
        with fastdissolve        
        voice "power/intro24"
        pg "You'll know because the option to take me with you won't be available. That's how You'll KNOW."
        jump PGDialogueLeague
    "Will you be going to that Charity Ball?" if pgspeak04 == False:
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        $ pgspeak04 = True
        voice "power/intro25"
        pg "Of course! It's a great event with lots of nice people. Except for the Super-Villains."
        mc "What??? Super-Villains are INVITED????"
        hide allleaguepower04
        show allleaguepower01
        with fastdissolve
        voice "power/intro26"
        pg "Some are members of the Cockham social elite unfortunately."
        hide allleaguepower01
        show allleaguepower05
        with fastdissolve
        voice "power/intro27"
        pg "But don't worry, the Cockham League of Justice will be READY if they cause any trouble!"
        hide allleaguepower05
        show powereyeblink
        with fastdissolve        
        jump PGDialogueLeague
    "I'm done here.":
        hide powereyeblink
        show allleaguepower04
        with fastdissolve
        voice "power/intro28"
        pg "Bye [hero]!"        
        $ spokeleaguepower = True
        jump IntroLeagueHallb
        
label AllLeagueSuperman:
stop music
scene allleaguedoor
show allleaguesuper01 at centerleft with dissolve:
    breathe

label SMDialogueLeague:
menu:
    "Yo buddy." if smspeak01 == False:
        $ smspeak01 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        voice "superman/intro07"
        sm "What do you want? We have NOTHING in common."
        mc "I feel like we have started off on the wrong footing..."
        voice "superman/intro08"
        sm "My footing is just fine. And I can fly out of here ANYTIME I WANT."
        mc "Oooh!... You've got an important date you need to fly to? No? No date on the horizon, Superman? What a shame."
        hide allleaguesuper02
        show allleaguesuper04 at centerleft
        with fastdissolve
        voice "superman/intro09"
        sm "I have a love interest for your information! Lois Pane, a reporter from the Cockham Planet. I work wih her. Undercover as Clark Kunt."
        mc "Why are you undercover anyway?"
        hide allleaguesuper04
        show allleaguesuper03 at centerleft
        with fastdissolve
        voice "superman/intro10"
        sm "That's a good question. I have no idea to be honest."
        hide allleaguesuper03
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        jump SMDialogueLeague
    "What are your superpowers, Superman?" if smspeak02 == False and smspeak01:
        $ smspeak02 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        voice "superman/intro11"
        sm "Come on! I'm the most FAMOUS superhero. Everyone knows my amazing superpowers. My incredible Super-Strength, my Super-Flight, my Super-Combat ability, my Super-..."
        mc"Yeah, yeah, ok, I get it. I also know of your super-weakness. Of some little rock called \"kryptonite\"..."
        hide allleaguesuper02
        show allleaguesuper03 at centerleft
        with fastdissolve
        voice "superman/intro12"
        sm "Well, err... It's really rare anyway, so..."
        mc "Still. Someone might get his or her hands on some of that rock. And when they do, you'll turn into a pathetic underhero weakling."
        hide allleaguesuper03
        show allleaguesuper02 at centerleft
        with fastdissolve
        voice "superman/intro13"
        sm "And that has NEVER happened! Except once. But I was saved by... Captain MILF."
        mc "Interesting. Is that why you keep obeying her like a little poodle?"
        hide allleaguesuper02
        show allleaguesuper04 at centerleft
        with fastdissolve
        voice "superman/intro14"
        sm "She's OUR boss. Including YOURS. Don't forget that!"
        mc "Well, she's also my landlady so I have a... special relationship with her."
        hide allleaguesuper04
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        voice "superman/intro15"
        sm "Within the guidelines set forth by the Patreon Bill passed by Congress last year?"
        mc "Err, yeah, of course. Totally within those guidelines."
        hide allleaguesuper01
        show allleaguesuper04 at centerleft
        with fastdissolve
        voice "superman/intro16"
        sm "Good, it would be embarrassing for me to have to ban you from this game for doing something that goes against that Patreon Bill."
        mc "Err, yeah, sure, whatever."
        hide allleaguesuper04
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        jump SMDialogueLeague
    "So Sexy Luthor keeps escaping, hey?" if smspeak03 == False and smspeak01:
        $ smspeak03 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        voice "superman/intro17"
        sm "The CCPD are USELESS! She just seduces the guard with her Super-Seduction powers and they let her out."
        mc "I bet you're IMMUNE to Super-Seduction. Having no dick and all that."
        hide allleaguesuper02
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        voice "superman/intro18"
        sm "Yes, I AM immune. I'm a REAL superhero and I'm here to CONCENTRATE on my job. Unlike you clearly."
        mc "I can concentrate. And use my monster cock at the same time. Unlike you clearly."
        voice "superman/intro19"
        sm "Umpf..."
        jump SMDialogueLeague
    "Man, you should stop wearing eyeliner. It's for girls.":
        hide allleaguesuper01
        show allleaguesuper03 at centerleft
        with fastdissolve
        voice "superman/intro20"
        sm "It's not eyeliner, I just... keep burning all my eyelashes every time I use my super-laser eyes."
        mc "Yikes, that sucks. I'm glad I don't have this silly superpower."
        hide allleaguesuper03
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        voice "superman/intro21"
        sm "It's very useful to fight SUPER-VILLAINS. You'll learn the hard way I guess."
        jump SMDialogueLeague
    "I'm done here.":
        hide allleaguesuper01
        show allleaguesuper03 at centerleft
        with fastdissolve
        voice "superman/intro22"
        sm "Are you though? If only..."        
        $ spokeleaguesuper = True
        jump IntroLeagueHallb
        
label AllLeagueWidow:
stop music
scene allleaguesofa
show widoweyeblink at centerleft
with dissolve

label BWDialogueLeague:
menu:
    "I hope we'll go on missions together Black Widow.":
        voice "widow/intro04"
        bw "Maybe. If you are fighting a REALLY STRONG enemy that only I can defeat."
        mc "I can defeat anybody I want, I'll prove it to you!"
        hide widoweyeblink
        show allleaguewidow03 at centerleft
        with fastdissolve
        voice "widow/intro05"
        bw "Oh yeah? So why do you want me to accompany you on missions then?"
        mc "Err... Well, for the good company and..."
        hide allleaguewidow03
        show allleaguewidow02 at centerleft
        with fastdissolve        
        voice "widow/intro06"
        bw "... The big tits?"
        mc "Well. Yeah, that too."
        window hide
        hide allleaguewidow02
        show widoweyeblink at centerleft
        with fastdissolve                
        jump BWDialogueLeague
    "Your outfit seems to be rather tight... around the top." if wispeak01 == False:
        $ wispeak01 = True
        hide widoweyeblink
        show allleaguewidow02 at centerleft
        with fastdissolve
        voice "widow/intro07"
        bw "Oh, you think so? It must be because of these BIG SUMPTUOUS titties of mine perhaps?"
        mc "That would be a rational explanation indeed."
        hide allleaguewidow02
        show allleaguewidow04 at centerleft
        with fastdissolve                
        voice "widow/intro08"
        bw "I've been known to SMOTHER my enemies with them, you know."
        mc "I... I'll keep that in mind."
        voice "widow/intro09"
        bw "So you should."
        window hide
        hide allleaguewidow04
        show widoweyeblink at centerleft
        with fastdissolve                
        jump BWDialogueLeague
    "Are you, like, a REAL widow?" if wispeak02 == False:
        $ wispeak02 = True
        hide widoweyeblink
        show allleaguewidow05 at centerleft
        with fastdissolve
        voice "widow/intro10"
        bw "Yes, my late husband died of SEXUAL EXHAUSTION, if you see what I mean. *wink*"
        mc "Err, right."
        window hide
        hide allleaguewidow05
        show widoweyeblink at centerleft
        with fastdissolve                
        jump BWDialogueLeague
    "I'm [name]. What's YOUR real name?":
        hide widoweyeblink
        show allleaguewidow04 at centerleft
        with fastdissolve
        voice "widow/intro11"
        bw "Natasha. I'm Russian originally but now I'm a true Cockham-addict."
        mc "Aren't the commies still a threat though?"
        hide allleaguewidow04
        show allleaguewidow03 at centerleft
        with fastdissolve                
        voice "widow/intro12"
        bw "Sure, but they are pretty tame, you shouldn't worry about them too much."
        window hide
        hide allleaguewidow03
        show widoweyeblink at centerleft
        with fastdissolve                
        jump BWDialogueLeague
    "Remind me your superpowers Black Widow.":
        hide widoweyeblink
        show allleaguewidow03 at centerleft
        with fastdissolve
        voice "widow/intro13"
        bw "I am a specialist superhero. In COMBAT. Level 3 actually. And Super-Agility."
        mc "And... Do you teach willing superhero trainees to fight? And be, like, super-agile?"
        hide allleaguewidow03
        show allleaguewidow05 at centerleft
        with fastdissolve
        voice "widow/intro14"
        bw "Of course I do. If you're capable of handling THIS BODY. *wink*"
        mc "I'm sure I can..."
        hide allleaguewidow05
        show allleaguewidow04 at centerleft
        with fastdissolve
        voice "widow/intro15"
        bw "Do you have a special superhero weapon?"
        mc "Does my cock count?"
        voice "widow/intro16"
        bw "No, it doesn't, silly."
        mc "Then no. Why, do I need a weapon?"
        hide allleaguewidow04
        show allleaguewidow03 at centerleft
        with fastdissolve
        voice "widow/intro17"
        bw "Sure, a superhero trained in Super-Combat always has a unique weapon. Usually some ancient and valuable artefact of some sort."
        mc "Ah, Damn. Where could I find one?"
        hide allleaguewidow03
        show allleaguewidow05 at centerleft
        with fastdissolve
        voice "widow/intro18"
        bw "Mmh. You'd have to look for one. Lara Crotch is a superhero adventurer specialized in seeking stuff like that. She's not here right now, she's in Cambodia or something."
        mc "Thanks, I shall seek her and her advice then. When she returns."
        hide allleaguewidow05
        show widoweyeblink at centerleft
        with fastdissolve
        voice "widow/intro19"
        bw "Or you could just try and swing that thing between your legs like a baseball bat... *wink*"
        mc "Ah! So it COULD count as a weapon then!"
        jump BWDialogueLeague
    "I'm done here.":
        hide widoweyeblink
        show allleaguewidow05 at centerleft
        with fastdissolve                
        voice "widow/intro20"
        bw "I'd like to see you again. And that dong of yours."    
        mc "Err, yeah, okay. Thank you, Black Widow."
        $ spokeleaguewidow = True
        jump IntroLeagueHallb
        
label AllLeagueWonder:
stop music
scene allleaguepillar
show allleaguewonder01 at centerleft with dissolve:
    breathe

label WWDialogueLeague:
menu:
    "Will you be willing to accompany me on... my missions, Wonder Woman?" if wwspeak01 == False:
        $ wwspeak01 = True
        hide allleaguewonder01
        show allleaguewonder04 at centerleft
        with fastdissolve
        voice "wonder/intro02"
        ww "I doubt it, I'm very busy."
        mc "Oh. Who are you fighting exactly?"
        hide allleaguewonder04
        show allleaguewonder03 at centerleft
        with fastdissolve
        voice "wonder/intro03"
        ww "Lots of bad people. Nazis mainly."
        mc "I didn't expect the Third Reich to show up."
        hide allleaguewonder03
        show allleaguewonder02 at centerleft
        with fastdissolve
        voice "wonder/intro04"
        ww "Me neither, I'm from Ancient Greece."
        window hide
        hide allleaguewonder02
        show allleaguewonder01 at centerleft
        with fastdissolve
        show allleaguewonder01 at centerleft:
            breathe
        jump WWDialogueLeague
    "What's your... little name, may I ask?" if wwspeak02 == False:
        $ wwspeak02 = True
        hide allleaguewonder01
        show allleaguewonder02 at centerleft
        with fastdissolve
        voice "wonder/intro05"
        ww "You mean my non-superheroine name?"
        mc "Yeah. I'm [name] by the way."
        hide allleaguewonder02
        show allleaguewonder04 at centerleft
        with fastdissolve
        voice "wonder/intro06"
        ww "Then mine is Princess Diana of Themyscira."
        mc "Wow, I didn't know you were a princess."
        hide allleaguewonder04
        show allleaguewonder01 at centerleft
        with fastdissolve
        show allleaguewonder01 at centerleft:
            breathe
        voice "wonder/intro07"
        ww "And now you do."
        mc "It's a rather long and complicated name though. Mind if I just call you Gal? Like, because I'm a guy and you're a gal. A GAL, get it?"
        hide allleaguewonder01
        show allleaguewonder03 at centerleft
        with fastdissolve
        voice "wonder/intro08"
        ww "No, I don't get it. Is that supposed to be funny?"
        mc "Err..."
        hide allleaguewonder03
        show allleaguewonder02 at centerleft
        with fastdissolve
        voice "wonder/intro09"
        ww "Then it's still PRINCESS DIANA OF THEMYSCIRA to you."
        mc "Alright, I'll try and remember."
        window hide
        hide allleaguewonder02
        show allleaguewonder01 at centerleft
        with fastdissolve
        show allleaguewonder01 at centerleft:
            breathe
        jump WWDialogueLeague
    "That's a hot outfit you got there." if wwspeak01:
        hide allleaguewonder01
        show allleaguewonder02 at centerleft
        with fastdissolve
        voice "wonder/intro10"
        ww "Don't flatter me. I'm a virgin and I intend to remain one until the end of times."
        mc "What... But... Why???"
        hide allleaguewonder02
        show allleaguewonder03 at centerleft
        with fastdissolve
        voice "wonder/intro11"
        ww "The purity of my race is at stakes."
        mc "Ok, but if you were to mate with ANOTHER superhero, imagine what kind of pure, superior überbabies you could have..."
        hide allleaguewonder03
        show allleaguewonder04 at centerleft
        with fastdissolve
        voice "wonder/intro12"
        ww "Mmmh, I hadn't thought of that... It sounds kind of nazi though. I'll give it a pass."
        window hide
        hide allleaguewonder04
        show allleaguewonder01 at centerleft
        with fastdissolve
        show allleaguewonder01 at centerleft:
            breathe
        jump WWDialogueLeague
    "Remind me what superpowers you have if you please.":
        hide allleaguewonder01
        show allleaguewonder04 at centerleft
        with fastdissolve
        voice "wonder/intro13"
        ww "Sure. Super-Strength, level 1, Super-Agility, Level 1, Super-Healing, level 1, Super-Combat, level 2, Super-S..."
        mc "Hang on, hang on, I can't take that down fast enough..."
        hide allleaguewonder04
        show allleaguewonder03 at centerleft
        with fastdissolve
        voice "wonder/intro14"
        ww "Audit Girl can. Super-Senses, level 2. It's all available in my dossier by the way. I sense you haven't read it."
        mc "How did you guess?"
        hide allleaguewonder03
        show allleaguewonder02 at centerleft
        with fastdissolve
        voice "wonder/intro15"
        ww "Super-Senses. Level 2."
        window hide
        hide allleaguewonder02
        show allleaguewonder01 at centerleft
        with fastdissolve
        show allleaguewonder01 at centerleft:
            breathe
        jump WWDialogueLeague
    "I'm done here." if wwspeak01:
        hide allleaguewonder01
        show allleaguewonder04 at centerleft
        with fastdissolve
        voice "wonder/intro16"
        ww "We will meet again. Different time, different place."    
        mc "That's kinda cryptic..."
        $ spokeleaguewonder = True
        jump IntroLeagueHallb

label EndIntroLeague:
scene league05 with fade
voice "milf/intro40"
cm "Alright, let's all make a move. Those who can't fly take the speedboat across and meet the others there."
voice "batman/intro20"
bm "Err, yeah, you know what, I think I'll take the speedboat. Just this time."

label VIP:
hide screen folders
stop music
play channel1 "sounds/gala.mp3"
scene loisvip01 with fade    
voice "lois/intro01"
lp "Welcome to the Vayne Enterprises Charity Ball, I'm Lois Pane, reporting from Vayne Tower where the city's elite will gather tonight under the auspices of Bruce Vayne."
scene loisvip02 with dissolve    
voice "lois/intro02"
lp "Hang on a minute, I am being told that Bruce Vayne will actually be a no-show at his own charity ball. Just like last year and the year before th..."
scene loisvip01 with dissolve    
voice "lois/intro03"
lp "The first car has arrived, I recognize Mayor Krass's tax-funded limousine..."
scene mayorvip01 with dissolve
voice "lois/intro04"
lp "And here he is walking down the red carpet with his socialite daughter Catherine in his arm."
scene mayorvip02 with dissolve
voice "lois/intro05"
lp "Catherine is wearing an expensive designer gown which is getting the paparazzi's attention."
play sound "sounds/flash.mp3"
scene mayorvip02 with fastflash
voice "lois/intro06a"
lp "The mayor waves at the crowd, I will attempt an interview..."
voice "lois/intro06b"
lp "Lois Pane, from the Cockham Planet, a minute of your time please sir!"
scene mayorvip03 with dissolve
voice "lois/intro07"
lp "Mayor Krass, are the rumors true that you plan to re-open Arkham's Asylum? And don't you think this is a dangerous move when sex crime is at an all-time high in Cockham?"
mk "Ms Pane... I don't know where you get your numbers from but I can assure you that Town Hall, in conjunction with the CCPD and the Cockham League of Justice, has everything under control and..."
scene loisvip03 with dissolve
voice "lois/intro08"
lp "Sorry to interrupt you Mister Mayor, but the Black Widow and Powergirl have just arrived and you are boring our listeners."
ck "Let's move daddy, I want to get inside."

scene widowvip01 with dissolve
play channel2 "sounds/crowd.mp3"
voice "lois/intro09"
lp "The Black Widow and Powergirl are walking down the red carpet. Please pose for your adoring fans, ladies!"
scene widowvip02 with dissolve
voice "lois/intro10"
lp "That is a sure crowd-pleaser. These two Cockham Superheroes are really popular with the men."
play sound "sounds/flash.mp3"
voice "lois/intro11"
lp "And I now see the boys arriving..."
scene supermanvip01 with dissolve
voice "lois/intro12"
lp "It's Batman and Superman!"
scene supermanvip02 with dissolve
voice "lois/intro13"
lp "Still fighting crime in our city after decades and unfortunately getting little progress with their super-villain enemies."
play sound "sounds/flash.mp3"
scene supermanvip02 with fastflash
stop channel2
voice "lois/intro14"
lp "I will approach them with pressing questions."
scene loisvip04 with dissolve
voice "lois/intro15"
lp "So, you have clearly overcome your distrust stemming from that epic battle you fought against each other a few years back and which was turned into a calamitous Hollywood movie." 
scene supermanvip03 with dissolve
voice "superman/intro23"
sm "Excuse me! You'll find that a great reporter from your own newspaper described it, and I quote, as a \"Cinematographic masterpiece featuring Cockham's most beloved superhero, Superman\"."
voice "lois/intro16"
lp "Yes, that was Clark Kunt, who is not qualified as a movie critique."
voice "batman/intro20b"
bm "Clark Kunt is a FRAUD."
scene loisvip04 with dissolve
voice "lois/intro17"
lp "And Batman, what do you make of Bruce Vayne's continuous absence from his own company's annual Charity Ball?"
scene supermanvip04 with dissolve
voice "batman/intro21"
bm "Well, err... I'm sure he is a very busy man, you know, being a super-rich BILLIONNAIRE, and there is absolutely nothing to..."
voice "superman/intro24"
sm "Bruce Vayne is a FRAUD!"
voice "lois/intro18"
lp "Well, thank you fellows, I believe your boss is about to arrive, so you really should get going..."
scene milfvip01 with dissolve
play channel2 "sounds/crowd.mp3"
voice "lois/intro19"
lp "Captain MILF is making her entrance into Vayne Tower wearing a see-thru gala dress that leaves very little to the imagination. I don't think she's even wearing any panties." 
scene milfvip02 with dissolve
voice "lois/intro20"
lp "The paparazzis are going berserk..." 
play sound "sounds/flash.mp3"
scene milfvip02 with fastflash
voice "lois/intro21"
lp "We apologize to our viewers for the flash photography."
scene milfvip03 with dissolve
voice "lois/intro22"
lp "And look at her flexing her huge muscles for the crowd..."
play sound "sounds/flash.mp3"
scene milfvip03 with fastflash
voice "lois/intro23"
lp "I will attempt a short interview. Captain MILF, Captain MILF, over here!"
scene milfvip04 with dissolve
voice "lois/intro24"
lp "Could you please tell us more about the NEW superhero who joined the Cockham League of Justice recently please? What kind of crime will he be fighting exactly?"
play sound "sounds/flash.mp3"
stop channel2
scene milfvip04 with fastflash
voice "milf/intro40a"
cm "I will let you ask him yourself when you see him!"
scene loisvip03 with dissolve
voice "lois/intro25"
lp "Is it true that he is, in fact, your landboy? And what does that imply for your work relationship with him?"
scene milfvip04 with dissolve
voice "milf/intro40b"
cm "That is indeed correct, he's my landboy and our relationship will be purely a professional landlady-tenant relationship, within the guidelines set forth by the Patreon Bill passed by Congress last year."
voice "lois/intro26"
lp "I see... Thank you for your time, Captain MILF."
scene loisvip02 with dissolve
voice "lois/intro27"
lp "Before the arrival of the League's new superhero, more elite members of our city are on their way."
scene keenvip01 with dissolve
voice "lois/intro28"
lp "Barbara Keen, the self-proclaimed nightlife Queen of Cockham has just arrived. Her most famous nightclub, \"The Sirens\", is where everyone who's anyone must be seen!"
scene keenvip02 with dissolve
voice "lois/intro29"
lp "Are you here to corrupt Mayor Krass like you usually do Ms Keen?"
play sound "sounds/flash.mp3"
scene keenvip02 with fastflash
bk "No comment..."
window hide
voice "lois/intro30"
lp "As usual... Let's wait for the next guest, who according to my list is Ms Scarlet, the head of research at Vayne Enterprises."
scene scarletvip01 with dissolve
voice "lois/intro31"
lp "There she is, posing for the photographers after having walked down the red carpet."
play sound "sounds/flash.mp3"
scene scarletvip01 with fastflash
play sound "sounds/flash.mp3"
voice "lois/intro32"
lp "Ms Scarlet, a word with the Cockham Planet please?"
scene scarletvip02 with dissolve
voice "lois/intro33"
lp "Now that Arkham's asylum is about to re-open, how will this affect your research?"
voice "scarlet/intro01"
sc "This is great news for the research division of Vayne Enterprises. It will allow us to make FULL USE of Arkham's facilities..."
voice "lois/intro34"
lp "Meaning what exactly? Do you plan on physically experimenting on humans?"
voice "scarlet/intro02"
sc "Of course not, that would be illegal, we will only STUDY the inmates to better understand the human mind, nothing more..."
scene loisvip03 with dissolve
voice "lois/intro35"
lp "Thank you Ms Scarlet, I am sure our viewers are completely reassured."
scene loisvip02 with dissolve
voice "lois/intro36"
lp "Ms Scarlet is followed by Harley Quiff, the famed accused - but innocent until proven guilty - serial rapist super-villain."
scene harleyvip01 with dissolve
voice "harley/intro01"
hq "Hello everyone!"
scene harleyvip02 with dissolve
voice "harley/intro02"
hq "Kisses to all of you!"
play sound "sounds/flash.mp3"
scene harleyvip02 with fastflash
voice "lois/intro37"
lp "Ms Quiff! Lois Pane here!"
play sound "sounds/flash.mp3"
scene harleyvip02 with fastflash
voice "harley/intro03"
hq "Yes, go on, ask your silly question..."
scene harleyvip03 with dissolve
voice "lois/intro38"
lp "What are your reactions following the announcement that Arkham's asylum will re-open?"
voice "harley/intro04"
hq "I won't be visiting, that's for sure! Been captive there long enough myself..."
voice "lois/intro39"
lp "Even your ex-inmate friends that will be transferred there?"
voice "harley/intro05"
hq "I ain't going back to the nuthouse, I have been certified as completely sane by my doctor!"
scene loisvip03 with dissolve
voice "lois/intro40"
lp "...Deceased Dr. Weakheart who was recently found dead in his bed in a puddle of your own cuntjuices?"
voice "harley/intro06"
hq "Err, yeah, that one."
voice "lois/intro41"
lp "Thank you for you honest answer Ms Quiff, I will let you go as billionnaire socialite Emma Frost is scheduled for arrival..."
voice "harley/intro07"
hq "That slut? Who cares about her!"
play sound "sounds/flash.mp3"
scene emmafrostvip01 with dissolve
voice "lois/intro42"
lp "And there she is, in a dress befitting of her title of \"White Queen\" and CEO of Frost International."
play sound "sounds/flash.mp3"
scene emmafrostvip02:
    subpixel True
    xpos -0.1
    linear 4.0 xpos 0.0
with dissolve
voice "lois/intro43"
lp "I will let her finish posing for the photographers..."
play sound "sounds/flash.mp3"
scene emmafrostvip02:
    xpos 0.0
with fastflash
voice "lois/intro44"
lp "Some people claim that Ms Frost is the most beautiful woman in the world but with the competition we have seen tonight, I am not so su..."
scene emmafrostvip03 with dissolve
play sound "sounds/radiation02.mp3"
$ renpy.pause(1.0, hard='True')
voice "lois/intro45"
lp "I... I am actually SURE that she IS the MOST beautiful woman on PLANET EARTH."
voice "frost/intro00"
ef "Now that's better."
stop sound
scene loisvip01 with dissolve
voice "lois/intro46"
lp "And now for the long-awaited arrival of the Cockham League of Justice's new addition, I give you..."
play channel2 "sounds/crowd.mp3"
scene mcvip01 with dissolve
lp "[hero]!"
scene mcvip02 with dissolve
voice "lois/intro47"
lp "Oh my God, look at his incredible physique, he puts Superman to shame! And what a gorgeous smile!"
play sound "sounds/flash.mp3"
scene mcvip02 with fastflash
voice "lois/intro48"
lp "Marty, zoom in on that MASSIVE bulge! Our viewers need to see THIS!"
scene mcvip03 with dissolve
voice "lois/intro49"
lp "[hero]! Lois Pane, please flex your muscles for our viewers!"
scene mcvip04:
    subpixel True
    xpos 0.0
    linear 4.0 xpos -0.1
with dissolve
voice "lois/intro50"
lp "Oh damn, I'm getting ... funny between the legs."
play sound "sounds/flash.mp3"
scene mcvip04:
        xpos -0.1
with fastflash
voice "lois/intro51"
lp "I'll... try and keep my professionalism. And ask [hero] some questions..."
scene loisvip03 with dissolve
voice "lois/intro52"
lp "Rumor has it that you might be underage, is there any truth to it?"
scene mcvip05 with dissolve
mc "Err... Absolutely not! I am totally over eighteen, in full compliance with the Patreon Bill passed by Congr..."
scene loisvip03 with dissolve
voice "lois/intro53"
lp "...Congress last year, yeah, yeah, sure. And what type of crime will you be fighting exactly?"
scene mcvip05 with dissolve
mc "Captain MILF has assigned me to the sex crime division."
window hide
voice "lois/intro54"
lp "There you have it folks, I think there will be an increase in SEX CRIME reporting by women all over the city tonight! *giggles*"
stop channel2
scene loisvip01 with dissolve
voice "lois/intro55"
lp "This was Lois Pane, reporting from Vayne Tower, over back to you in the studio."
stop channel1 fadeout 1.0

label ConscienceIntro:
stop sound
scene intromcsleep01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with fade
mc "Ah, off to sleep in my new SUPERHERO bed after this boring charity ball... I hope I have nice dreams."
scene intromcsleep02
with dissolve
play sound "sounds/dream.mp3"
$ renpy.pause(1.0, hard='True')
play music "sounds/introdreaming.mp3"
scene intromcsleep02a
with fade
show angela01a at topleft with moveinleft
hide angela01a
show angelafly01 at topleft
voice "angel/intro01"
an "Hello [name], can you hear my voice?"
show intromcsleep02b
with dissolve
mc "Sure, loud and clear. Even though I'm sleeping. And I can see you too, sexy angel with big tits..."
window hide
hide angelafly01
show angelafly02 at topleft
with fastdissolve
voice "angel/intro02"
an "Please don't think of me as a sexual object, my name is Angela, I am your GOOD conscience, guiding you away from the wretched path of..."
window hide
show demona01a at topright with moveinright
hide demona01a
show demonafly01 at topright
voice "demona/intro01"
de "Hey bitch, you started without me! That's CHEATING!"
hide intromcsleep02b
show intromcsleep02c
with dissolve
mc "Oooh, Batwoman?"
hide demonafly01
show demonafly02 at topright
with fastdissolve
voice "demona/intro02"
de "I'm NOT Batwoman, I'm Demona, your FILTHY, NASTY conscience."
voice "demona/intro02b"
de "I'm here to tell you to let loose, enjoy yourself! Screw that stupid superhero job, let's FUCK and get some POONTANG!"
mc "Fuck yeah, damn right Batwoman!"
hide demonafly02
show demonafly04 at topright
with fastdissolve
voice "demona/intro03"
de "I told you I WASN'T BATWOMAN. Are you stupid or something?"
mc "Err..."
hide angelafly02
show angelafly03 at topleft
with fastdissolve
hide intromcsleep02c
show intromcsleep02b
with dissolve
voice "angel/intro03"
an "Don't listen to her [name], she's a succubus! Straight from hell to lead you astray on your righteous path of spreading good around the world!"
hide demonafly04
show demonafly03 at topright
with fastdissolve
voice "demona/intro04"
de "Oh come on, this is BORING! Much better to SPREAD something else, get where I'm going, hey buddy? *wink*"
voice "angel/intro04"
an "Don't be tempted by her sexual advances, this is WRONG!"
hide intromcsleep02b
show intromcsleep02c
with dissolve
hide demonafly03
show demonafly01 at topright
with fastdissolve
voice "demona/intro05"
de "This is a PORN GAME, you stupid heaven-whore! What's wrong with DESTROYING cunts with his MONSTERCOCK?"
hide angelafly03
show angelafly02 at topleft
with fastdissolve
voice "angel/intro05"
an "Well, err..."
hide demonafly01
show demonafly02 at topright
with fastdissolve
voice "demona/intro06"
de "If you choose MY path, you'll have more FUN and I'll let you FUCK ME IN YOUR DREAMS. Eventually."
hide angelafly02
show angelafly04 at topleft
with fastdissolve
hide intromcsleep02c
show intromcsleep02b
with dissolve
voice "angel/intro06"
an "Hang on, hang on. I have no choice I guess... I'll let you have your ways with ME, even up the ass if you like, if you listen to ME! You said you liked my big tits, right?"
hide intromcsleep02b
show intromcsleep02c
with dissolve
hide demonafly02
show demonafly04 at topright
with fastdissolve
voice "demona/intro07"
de "I KNEW you were just a filthy cock-slut! But look at mine [name], they're even bigger than hers! Let them take care of that aching hardon..."
hide intromcsleep02c
show intromcsleep02b
with dissolve
voice "angel/intro07"
an "I'll take you to HEAVENS and... MORE! If you choose the nice hero way, the path of our GOOD Lord!"
stop music fadeout 1.0
scene intromcsleep04 with fade
stop channel4
mc "Oh shit, I think I had a wet dream... Those superpowers are messing with my mind!"
mc "Fortunately, it's already morning. I'll take a shower to be ready for my FIRST day as a SUPERHERO!"
scene intromcshower01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with fade
play music "sounds/shower.mp3"
mc "Mmh yeah, that hot water is clearing my mind..."
scene intromcshower02 with dissolve
mc "I shouldn't be late. Let's head to the main hall. To get my SUPERHERO assignments for the day."
stop music

$ day = 2
$ period = 0
scene compoundhall01d with fade
show screen calendar
show compoundmilf01 at right with moveinright
voice "milf/intro41"
cm "Hello, early superhero bird!"
mc "I can't fly Carol, I'm not a bird..."
hide compoundmilf01
show compoundmilf02
with fastdissolve
voice "milf/intro42"
cm "You don't need to know how to fly to be a superhero. I can't fly and I'm a superhero, right?"
mc "I guess so."
hide compoundmilf02
show compoundmilf04
with fastdissolve
voice "milf/intro43"
cm "And anyway, you're going to go way up today, almost to the sky!"
mc "What do you mean?"
hide compoundmilf04
show compoundmilf02
with fastdissolve
voice "milf/intro44"
cm "It is customary for any new superhero to introduce himself (or herself) to Emma Frost, also known as the White Queen. As a sign of... goodwill from the League."
mc "Why, isn't she supposed to be a Super-Villain? She's in my blue folder I'm pretty sure."
hide compoundmilf02
show compoundmilf06
with fastdissolve
voice "milf/intro45"
cm "She might be, we're not SURE at this stage. And to keep her from the temptation of using her POWERFUL super-powers to spread EVIL, I have made a truce with her."
hide compoundmilf06
show compoundmilf01
with fastdissolve
voice "milf/intro46"
cm "Part of the deal is that she gets to meet new superheroes. It's just a polite visit really, you have nothing to worry about [name]."
mc "Okay. Will you be coming with me then?"
hide compoundmilf01
show compoundmilf05
with fastdissolve
voice "milf/intro47"
cm "Err, no. Her office is up on the 666th floor of Frost Tower and I... can't go up there."
hide compoundmilf05
show compoundmilf04
with fastdissolve
voice "milf/intro48"
cm "But the Black Widow can! She'll be accompanying you so you don't fall prey to her mind-controlling abilities."
window hide
show compoundmilf04 at right with move
show compoundwidow01 at farleft with moveinleft
voice "widow/intro21"
bw "I have better things to do normally, but fine, I'll bring [hero] to see that wicked witch."
mc "You don't seem to like her that much."
hide compoundwidow01
show compoundwidow02 at farleft
with fastdissolve
voice "widow/intro22a"
bw "Oooh, look at me, I'm the most beautiful woman in the world, look at how beautiful I am! That's her CONSTANTLY."
voice "widow/intro22b"
bw "She's just an attention-seeking self-aggrandizing EVIL BITCH!"
hide compoundmilf04
hide compoundwidow02
show compoundmilf03 at right
show compoundwidow01 at farleft
with fastdissolve
with fastdissolve
voice "milf/intro49"
cm "Natasha, please remember to be polite with her. And make sure she doesn't use her telepathic powers to tamper with [hero]'s fragile mind."
mc "Hey, my mind is not fragile!"
hide compoundwidow01
hide compoundmilf03
show compoundwidow03 at farleft
show compoundmilf01 at right
with fastdissolve
voice "widow/intro23"
bw "Let's just go and get this over with."

play channel1 "sounds/suspense.mp3"
scene cockhamintro01
show introwatch02:
    xpos 500 ypos 300
show introskipgame:
    xpos 620 ypos 450
with dissolve

call screen intro03()
screen intro03():
    modal True
    button:
        xpos 500
        ypos 300
        xysize(780, 90)        
        action Jump ("Intro02")
    button:
        xpos 620
        ypos 450
        xysize(490, 80)        
        action Jump ("IntroGame")
        
label Intro02:
$ day = 2
$ period = 0
stop channel1
scene frostoffice01 with fade
voice "frost/intro01"
ef "[hero]. I was expecting you. And the Black Widow. *sigh*"
voice "widow/intro24"
bw "Pleasure to be a nuisance to you, White Queen!"
scene frostoffice02 with dissolve
voice "frost/intro02"
ef "Are you on chaperoning duty today, Black Widow?"
voice "widow/intro25"
bw "You KNOW why we are here. So let's get it over with. [hero], introduce yourself, so we can leave as quickly as possible."
mc "Well, err, I'm [hero]. In charge of sex crimes. You're not a sex criminal, right?"
scene frostoffice03 with dissolve
voice "frost/intro03"
ef "Apparently, the Black Widow did not brief you correctly. I have stood on the right side of the law for many years now."
scene frostoffice02 with dissolve
voice "frost/intro04"
ef "Except if my immense beauty qualifies as a \"sex crime\" in itself in your eyes, [hero]..."
scene frostoffice04 with dissolve
voice "widow/intro26"
bw "You think you're so hot don't you? Well, I'm HOTTER, I'm so hot I bet I could be a Hollywood actress!"
scene frostoffice05 with dissolve
voice "frost/intro05"
ef "You? Pff, what a joke, I'm the most beautiful woman in the world. Why don't we ask [hero]? Or are you too scared to face the TRUTH?"
voice "widow/intro27"
bw "Of course NOT! Ask him, he'll tell YOU!"
scene frostoffice02 with dissolve
voice "frost/intro06"
ef "So, [hero]. You are a ladies man I gather. Who is the most beautiful woman here, the Black Widow or ME?"
mc "Err, well, it's hard to tell, I mean, if..."
voice "frost/intro07"
ef "...we showed you MORE, you might be able to better decide?"
mc "Err, yeah, that would help I guess."
scene frostoffice04 with dissolve
voice "widow/intro28"
bw "Fine, I'm game, I have nothing to HIDE, unlike YOU!"
scene frostoffice05 with dissolve
voice "frost/intro08"
ef "Just sit back [hero], and let our bodies do the TALKING."
hide screen calendar
play music "sounds/sexy01.mp3"
scene frostofficebackground
show froststrip00:
    zoom 0.5 xpos 100 ypos 0    
show widowoffice01:
    zoom 0.5 xpos 800 ypos 0
voice "frost/intro09"
ef "I will show you how my body is clearly SUPERIOR to the Black Widow's!"
voice "widow/intro29"
bw "What-ever!"
window hide
show frostofficebackground at frostzoombackgroundleft
show froststrip00 at frostzoomleft
show widowoffice01 at widowzoomleft
$ renpy.pause(1.5, hard='True')
voice "frost/intro10"
ef "So just watch ME, and not that redhead trollop."
voice "widow/intro30"
bw "Why would he watch an old hag like you?"
voice "frost/intro11"
ef "Despite my age, I keep VERY FIT as you can see..."
window hide
hide widowoffice01
show widowoffice02:
    xoffset 1200 yoffset -100 
show froststrip00 at frostunzoomleft
show frostofficebackground at frostunzoombackgroundleft
show widowoffice02 at widowunzoomleft
$ renpy.pause(1.5, hard='True')
voice "widow/intro31"
bw "Yeah, well so do I! I'll PROVE it to you!"
window hide
show froststrip00 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice02 at widowzoomleft02
$ renpy.pause(1.5, hard='True')
voice "frost/intro12"
ef "Your breasts are no where near as perfect as mine!"
voice "widow/intro32"
bw "I'll let [hero] be the judge of that..."
window hide
hide widowoffice02
show widowoffice03:
    zoom 1.0 xoffset 0 yoffset -400
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice03 at widowzoomleftdown
$ renpy.pause(1.5, hard='True')
voice "widow/intro33"
bw "And I'll let him be the judge of my fine ass, he won't find one better in Cockham!"
window hide
show widowoffice03 at widowunzoomleftdown
show frostofficebackground at frostzoombackgroundleftdown
hide froststrip00
show froststrip01:
    zoom 1 xoffset -1200 yoffset -1080 
show froststrip01 at frostzoomleftdown
$ renpy.pause(1.5, hard='True')
voice "frost/intro13"
ef "My tits are the most EFFICIENT in the city at bringing studs over the edge! Look at how LARGE they are, ideal for a HUGE-COCKED BOY like you I'd say!"
window hide
show froststrip01 at frostzoomleftdownup
show frostofficebackground at frostzoombackgroundleftup
$ renpy.pause(1.0, hard='True')
voice "frost/intro14"
ef "Don't you agree [hero]?"
mc "Err..."
window hide
hide widowoffice03
show widowoffice04:
    zoom 1.0 xoffset 1500 yoffset -400        
show froststrip01 at frostunzoomleft
show widowoffice04 at widowunzoomleft
show frostofficebackground at frostunzoombackgroundleft
$ renpy.pause(1.0, hard='True')
voice "widow/intro34"
bw "My SUPER-TITS aren't just for SMOTHERING ENEMIES, they can also wrap like velvet around a big hard shaft and make it CONVULSE WITH PLEASURE!"
window hide
show froststrip01 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice04 at widowzoomleft02
$ renpy.pause(1.5, hard='True')
voice "widow/intro35"
bw "I'll show you MORE if you're a GOOD boy..."
window hide
hide froststrip01
show froststrip02:
    zoom 1 xoffset -1200 yoffset -100     
show froststrip02 at frostzoomleftcenter
show frostofficebackground at frostzoombackgroundleftcenter
show widowoffice04 at widowzoomleftfar
$ renpy.pause(1.5, hard='True')
voice "frost/intro15"
ef "Why wait? He can have a closer look RIGHT NOW at MY sumptuous rack!"
window hide
hide widowoffice04
show widowoffice05:
    zoom 1.0 xoffset 1500 yoffset -400        
show froststrip02 at frostunzoomleft
show widowoffice05 at widowunzoomleft
show frostofficebackground at frostunzoombackgroundleft
$ renpy.pause(1.0, hard='True')
voice "widow/intro36"
bw "Oh, we're playing THAT game, hey?"
window hide
show froststrip02 at frostzoomleft02
show frostofficebackground at frostzoombackgroundright
show widowoffice05 at widowzoomleft02
$ renpy.pause(1.5, hard='True')
voice "widow/intro37"
bw "Then have a good LONG look at these titties [hero]. And imagine them SQUEEZING your hard shaft... Until you EXPLODE your warm nectar all over them."
window hide
hide froststrip02
show froststrip03:
    zoom 1 xoffset -1200 yoffset -100     
show froststrip03 at frostzoomleftdown
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice05 at widowunzoomleftdown
$ renpy.pause(1.5, hard='True')
voice "frost/intro16"
ef "Look at how TIGHT my ass is! Ideal for PUMPING a nice big fat load out of a rockhard monstercock..."
window hide
hide widowoffice05
show widowoffice06:
    zoom 1 xoffset 1600 yoffset -800 
show froststrip03 at frostzoomleftout
show frostofficebackground at frostzoombackgroundrightdown
show widowoffice06 at widowzoomleftdown
$ renpy.pause(1.5, hard='True')
voice "widow/intro38"
bw "Pff, my BUBBLE BUTT is the MOST cock-hardening in the whole town! It can make any dong BLOW ITS LOAD in a super-instant!"
window hide
hide froststrip03
show froststripwiggle:
    zoom 1 xoffset -800 yoffset 0
show froststripwiggle at frostunzoomwiggle
show frostofficebackground at frostzoombackgroundleftup
show widowoffice06 at widowzoomleftfar02
$ renpy.pause(1.5, hard='True')
voice "frost/intro17"
ef "Time to show [hero] the ULTIMATE PROOF that I AM the MOST BEAUTIFUL WOMAN IN THE WORLD!"
window hide
hide widowoffice06
show widowofficewiggle:
    zoom 1 xoffset 1600 yoffset 0
show widowofficewiggle at frostunzoomwiggle
show frostofficebackground at frostzoombackgroundrightup
show froststripwiggle at frostunzoomwiggleout
$ renpy.pause(1.5, hard='True')
voice "widow/intro39"
bw "That's no proof! THIS will DEFINITELY convince him that I am MORE BEAUTIFUL THAN YOU!"
show froststripwiggle:
    zoom 1 xoffset -1200 yoffset 0
show froststripwiggle at frostwiggleleft
show frostofficebackground at frostunzoombackgroundleft
show widowofficewiggle at frostwiggleright
voice "frost/intro18"
ef "Let HIM decide then, he'll have NO CHOICE but to RECOGNIZE MY UNWORLDLY BEAUTY!"
mc "I'm STILL undecided. Do I really have to choose?"
voice "frost/intro19"
ef "YES you DO! And since you're INCAPABLE of taking IMPORTANT decisions, my tits will take them for YOU!"
voice "widow/intro40"
bw "I'm not letting you pervert his mind on your own, White Queen. Count me in for whatever SALACIOUS idea you have in mind!"
scene frostofficemc01 with dissolve
voice "frost/intro20"
ef "Well, it involves our tits and that GROWING boyhood... Whoever makes him EXPLODE first is clearly the MOST BEAUTIFUL WOMAN IN THE WORLD! And it will be ME!"
voice "widow/intro41"
bw "Not a chance, my SUPER-TITS will bring him over the edge BEFORE yours do FOR SURE!"
scene frostofficemc02 with dissolve
mc "Err..."
voice "frost/intro21"
ef "Just get your cock out of that straining thong, lie on the coffee table and let our FUNBAGS do the rest, [hero]!"
window hide
scene frosttitfuckbackground
show frostofficemc03
with dissolve
play sound "sounds/gasp.mp3"
voice "frost/intro22"
ef "Damn boy, that thing is just MASSIVE..."
voice "widow/intro42"
bw "It's even BIGGER than I imagined."
voice "frost/intro23"
ef "This double-titfuck is going to be EPIC!"
stop sound
window hide

label FrostOfficeTitAnim:
show frosttitfuckbackgroundb behind frostofficelick at titfuckbackground
show frostofficetitfuck behind frostofficelick 
$ renpy.pause(1.0, hard='True')
if frostlicksaw:
    voice "widow/intro43"
    bw "Maybe we should go back to using our tits, he seems to be a bit more responsive to them..."
    voice "frost/intro24"
    ef "Especially to MINE. Let's make him cum then!"
    hide cum
    hide titfucking
    stop channel1
    hide frosttitfuckbackground
    hide frostofficelick
    hide frostofficemc03
    with dissolve
    show cum:
        xpos 1800 ypos 500
    show licking:
        xpos 50 ypos 500
    jump FrostTitfuck

stop channel1
hide frosttitfuckbackground
hide frostofficelick
hide frostofficemc03
with dissolve
show cum:
    xpos 1800 ypos 500
show licking:
    xpos 50 ypos 500
label FrostTitfuck:
play channel1 "sounds/wank.mp3"
call screen screentitfuck()
screen screentitfuck():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("FrostOfficeLickAnim")
    button:
        xpos 1800
        ypos 500
        xysize(100, 60)        
        action Jump ("FrostOfficeCum")
    
label FrostOfficeLickAnim:
window hide
show frostofficelick behind frosttitfuckbackgroundb
show frostofficelick behind frostofficetitfuck
$ renpy.pause(1.0, hard='True')
hide cum
hide titfucking
hide licking
if frostlicksaw == False:
    $ frostlicksaw = True
    if age >= 20:
        voice "frost/intro25a"
        ef "You like that don't you? Our big soft breasts rubbing against your rockhard alpha-cock?"
    if age >= 18 and age <=19:
        voice "frost/intro25b"
        ef "You like that don't you? Our big soft breasts rubbing against your rockhard teenage alpha-cock?"
    mc "Damn it, yeah, it feels real good."
    voice "widow/intro44"
    bw "How about we lick that dong for a while? I wanna TASTE it!"
    voice "frost/intro26"
    ef "Good idea, Let's take turns so he can rate our licking..."
hide frostofficetitfuck
hide frosttitfuckbackgroundb
with dissolve
show titfucking:
    xpos 50 ypos 500
stop channel1
play channel1 "sounds/lick01.ogg"
call screen screenlickfuck()
screen screenlickfuck():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(240, 60)        
        action Jump ("FrostOfficeTitAnim")
 
label FrostOfficeCum:
if age >= 20:
    voice "frost/intro27a"
    ef "It looks like this monster alpha-dong is going to spew its load..."
if age >= 18 and age <= 19:
    voice "frost/intro27b"
    ef "It looks like this monster teenage alpha-dong is going to spew its load..."
window hide
$ renpy.pause(2.0, hard='True')
voice "widow/intro45"
bw "Yeah, I can feel it too, his shaft is TREMBLING with anticipation..."
window hide
$ renpy.pause(2.0, hard='True')
hide frostofficetitfuck
hide cum
stop channel1
play channel1 "sounds/boyorgasm01.mp3"
scene frosttitfuckbackground
show frosttitfuckcum01
with dissolve
voice "frost/intro28"
ef "That's it? My fat tits around your shaft are making you cum already, [hero]?"
hide frosttitfuckcum01
show frosttitfuckcum02
with dissolve
voice "widow/intro46"
bw "I very much doubt it, it's clearly the pumping action of MY EXQUISITE breasts that are making him BLAST such a load!"
window hide
with fastflash
if age >= 20:
    voice "frost/intro29a"
    ef "In your DREAMS! PROVE her WRONG and douse ME in your cream, [hero]!"
if age >= 18 and age <= 19:
    voice "frost/intro29b"
    ef "In your DREAMS! PROVE her WRONG and douse ME in your teenage cream, [hero]!"
hide frosttitfuckcum02
show frosttitfuckcum03a
with dissolve
voice "frost/intro30"
ef "YEAH, just like that..."
window hide
with fastflash
voice "frost/intro31"
ef "More, MORE SUPER-SPUNK for ME!"
hide frosttitfuckcum03a
show frosttitfuckcum03b
with fastdissolve
voice "frost/intro32"
ef "COVER my face in your red-hot nectar!"
play sound "sounds/moan02.mp3"
window hide
with fastflash
voice "widow/intro47"
bw "You dirty whore, you're STEALING his cum from ME! Let me SWALLOW your cream, [hero]..."
hide frosttitfuckcum03b
show frosttitfuckcum04
with dissolve
play sound "sounds/moan01.mp3"
voice "widow/intro48"
bw "Gimme, gimme, gimme... mmggllurb...."
window hide
with fastflash
voice "frost/intro33"
ef "My turn, I'm gonna drain him with my mouth!"
hide frosttitfuckcum04
show frosttitfuckcum05
with dissolve
voice "frost/intro34"
ef "Gl...uuu... *swallow*"
window hide
with fastflash
voice "frost/intro35"
ef "De...li...glllb...cious!"
hide frosttitfuckcum05
show frosttitfuckcum06
with dissolve
play sound "sounds/panting.mp3"
stop channel1
stop music fadeout 1.0
voice "widow/intro49"
bw "I think he's drained. For NOW."
voice "frost/intro36"
ef "His cock is still hard though... Maybe we could... But no. We've done enough to his poor dong."
scene frostofficebackground
show froststrip06 at left
show widowoffice07 at centerright
with fade
show screen calendar
voice "frost/intro37"
ef "I think you've seen enough to take a decision [hero]. Who is the most beautiful, me or her?"
menu:
    "Don't pick anyone (no change)":
        mc "I think you are both equally super-beautiful. And hot."
        hide froststrip06
        show froststrip08 at left
        with fastdissolve
        voice "frost/intro38"
        ef "That is LAME. A superhero who can't even take a decision on such a simple TASK."
        hide widowoffice07
        show widowoffice09 at centerright
        with fastdissolve         
        voice "widow/intro50"
        bw "I agree with Emma Frost for once, it comes a time when it is crucial for you to DECIDE, [hero]!"
        mc "Alright, alright, gee why is everyone pushing me, even in my godamn dreams?"
        hide froststrip08
        show froststrip09 at left
        with fastdissolve
        voice "frost/intro39"
        ef "Have you been having dreams [hero]? That is interesting..."
        hide widowoffice09
        show widowoffice10 at centerright
        with fastdissolve         
        voice "widow/intro51a"
        bw "You'd better not astrally-project into his head, White Queen, the League of Justice is keeping an eye on you."
        voice "widow/intro51b"
        bw "Us superheroes are OFF-LIMITS may I remind you."
        hide froststrip09
        show froststrip08 at left
        with fastdissolve
        voice "frost/intro40"
        ef "And what have you found so far Black Widow? NOTHING. Don't put our truce in jeopardy, or you will regret it..."
        hide widowoffice10
        show widowoffice07 at centerright
        with fastdissolve         
        voice "widow/intro52"
        bw "Let's get out of here [hero], we came, you were introduced, this is the extent of the courtesy the League of Justice needs to give her at this stage."
        mc "Well, err, okay, nice meeting you Ms Fr..."
        hide widowoffice07
        show widowoffice09 at centerright
        with fastdissolve         
        voice "widow/intro52b"
        bw "Shut up and let's go!"
        hide froststrip08
        show froststrip06 at left
        with fastdissolve
        voice "frost/intro41"
        ef "You are welcome back ANY TIME, [hero]. * wink *"
        jump FrostIntroBack

    "Pick the Black Widow (+1 Super-Hero)":
        $ widowpicked = True
        call Good from _call_Good
        mc "I believe the Black Widow is the most beautiful here."
        hide superhero
        hide froststrip06
        hide widowoffice07
        show widowoffice08 at centerright
        show froststrip07 at centerleft
        with fastdissolve
        voice "frost/intro42"
        ef "How dare you!"
        play sound "sounds/slap.mp3"
        mc "Hey! I didn't deserve that!"
        hide froststrip07
        hide widowoffice08
        show froststrip08 at left
        show widowoffice10 at centerright        
        with fastdissolve 
        voice "widow/intro53"
        bw "[hero] has CHOSEN! And he chose ME. Take THAT, White Queen! HA HA HA!"
        voice "frost/intro43"
        ef "Get out of here, BOTH OF YOU!"
        hide widowoffice10
        show widowoffice07 at centerright
        with fastdissolve         
        voice "widow/intro54"
        bw "With pleasure... Come [name], we're DONE here."
        jump FrostIntroBack

    "Pick Emma Frost (+1 Super-Villain)":
        $ frostpicked = True
        call Evil from _call_Evil
        mc "Well, there's a reason Ms Frost is known for her amazing beauty. She's the most beautiful woman on Earth!"
        hide supervillain
        hide froststrip06
        hide widowoffice07
        show froststrip09 at left
        show widowoffice11 at centerright
        with fastdissolve        
        voice "widow/intro55"
        bw "So disappointing [hero]... I wonder what Captain MILF will make of that..."
        mc "Err, Captain MILF? Why don't we...err... leave her out of this..."
        hide froststrip09
        hide widowoffice11
        show froststrip10 at left
        show widowoffice09 at centerright
        with fastdissolve        
        voice "widow/intro56"
        bw "You OWE me one, [name]."
        voice "frost/intro44"
        ef "Oh, that's his little name? How cute..."
        hide widowoffice09
        show widowoffice11 at centerright
        with fastdissolve         
        voice "widow/intro57"
        bw "Let's GO. NOW!"
        jump FrostIntroBack

label FrostIntroBack:
$ period = 1
scene compoundhall01n with fade
show compoundmilf01 at right with moveinright
show compoundwidow01 at farleft with moveinleft
voice "milf/intro50"
cm "So, how did it go? Well, I hope..."
mc "It went err... smoothly."
if frostpicked:
    hide compoundwidow01
    show compoundwidow02 at farleft
    with fastdissolve
    voice "widow/intro60"
    bw "Oh yeah? I guess having her big tits wrapped around your huge cock is what YOU call a \"smooth\" introduction!"
    hide compoundmilf01
    show compoundmilf03 at right
    with fastdissolve    
    voice "milf/intro51"
    cm "What? Is... that what happened? You were NOT supposed to let her take control of his mind."
    hide compoundmilf03
    show compoundmilf05 at right
    with fastdissolve
    mc "Well, err, my mind is fine, she just took control of my dong."
    hide compoundwidow02
    show compoundwidow04 at farleft
    with fastdissolve
    voice "widow/intro61"
    bw "And that dong has a mind of its OWN!"
    hide compoundmilf05
    show compoundmilf06 at right
    with fastdissolve    
    voice "milf/intro52"
    cm "Well, as long as she was satisfied I suppose..."
    hide compoundmilf06
    show compoundmilf02 at right
    with fastdissolve    
    voice "milf/intro53"
    cm "Lara Crotch has returned. Go and speak to her [name], she would like to meet you."
    hide compoundwidow04
    show compoundwidow03 at farleft
    with fastdissolve
    voice "widow/intro62"
    bw "Try not to come all over HER tits this time! * snickers *"
    jump LaraCrotchIntro
if widowpicked:
    hide compoundwidow01
    show compoundwidow05 at farleft
    with fastdissolve
    voice "widow/intro63"
    bw "I agree. Everything went just fine."
    hide compoundmilf01
    show compoundmilf02 at right
    with fastdissolve    
    voice "milf/intro54"
    cm "Was she happy when you left? That's what's important."
    hide compoundwidow05
    show compoundwidow03 at farleft
    with fastdissolve
    mc "Err, she... seemed... quite happy. Something was definitely glowing on her face."
    hide compoundwidow03
    show compoundwidow02 at farleft
    with fastdissolve
    voice "widow/intro64"
    bw "Oh yeah, PLENTY of stuff glowing on her face."
    hide compoundmilf02
    hide compoundwidow02
    show compoundmilf06 at right
    show compoundwidow01 at farleft
    with fastdissolve
    voice "milf/intro55"
    cm "I'm not quite sure what to make of this..."
    hide compoundmilf06
    show compoundmilf02 at right
    with fastdissolve    
    voice "milf/intro53"
    cm "Lara Crotch has returned. Go and speak to her [name], she would like to meet you."
    hide compoundwidow01
    show compoundwidow03 at farleft
    with fastdissolve
    mc "Yes, Captain MILF."
    jump LaraCrotchIntro

hide compoundwidow01
show compoundwidow03 at farleft
with fastdissolve
voice "widow/intro65"
bw "I suppose we could say that, all things considered..."
hide compoundmilf01
show compoundmilf06 at right
with fastdissolve    
voice "milf/intro56"
cm "It seems you are hiding something from me..."
mc "I'm not, I swear! She... seemed... quite happy. Something was definitely glowing on her face."
hide compoundwidow03
show compoundwidow02 at farleft
with fastdissolve
voice "widow/intro64"
bw "Oh yeah, PLENTY of stuff glowing on her face."
hide compoundmilf06
show compoundmilf02 at right
with fastdissolve    
voice "milf/intro52"
cm "Well, as long as she was satisfied I suppose..."
voice "milf/intro53"
cm "Lara Crotch has returned. Go and speak to her [name], she would like to meet you."
hide compoundwidow02
show compoundwidow03 at farleft
with fastdissolve
mc "Yes, Captain MILF."

label LaraCrotchIntro:
play music "sounds/croftintro.mp3"
scene laraplace with fade
show lara01 with moveinright
show lara01 at center:
    breathe
voice "lara/intro01"
lc "Who are you?"
mc "Err, Captain MILF told me to come and visit you, sorry if this is a bad time, I can come back lat..."
window hide
hide lara01
show lara03
with fastdissolve
voice "lara/intro02"
lc "Ah, so you're the new superhero who joined the Cockham League of Justice? [hero], is that right?"
mc "Yes, that's me. Name says it all. I work in the Sex Crime Division of the League."
hide lara03
show lara01
with fastdissolve
show lara01 at center:
    breathe
voice "lara/intro03"
lc "Well I'm Lara Crotch. And the name says nothing."
hide lara01
show lara04
with dissolve
voice "lara/intro04"
lc "I was just relaxing after a long week in the jungle. Hence the... undies. Hope you don't mind?"
mc "Not at all..."
window hide
hide lara04
show lara01
with fastdissolve
show lara01 at center:
    breathe
label LaraCrotchDialogues:
menu:
    "And... What do you do exactly, Lara... Crotch?" if lcspeak01 == False:
        $ lcspeak01 = True
        hide lara01
        show lara03
        with fastdissolve
        voice "lara/intro05"
        lc "I'm not a regular superhero in that my job is to recover artefacts with superpowers before any super-villain gets his - or her - evil hands on them."
        mc "That's pretty cool."
        hide lara03
        show lara05
        with fastdissolve
        voice "lara/intro06"
        lc "I get to travel a lot, so I'm not often around. But as you can see, here are my private quarters, right here in the League's compound."
        mc "You've got your own quarters? How come I just get a bedroom and nothing else?"
        hide lara05
        show lara02
        with fastdissolve
        voice "lara/intro07"
        lc "Well, you're paying rent, right? I mean, you're a tenant, right? I OWN this place. I'm very rich, just like Batman."
        mc "Ah yes, that's right, I'm a LANDBOY, I remember now. *cough*"
        hide lara02
        show lara01
        with fastdissolve
        show lara01 at center:
            breathe
        jump LaraCrotchDialogues
    "You have a British accent. Like most movie supervillains..." if lcspeak02 == False:
        $ lcspeak02 = True
        hide lara01
        show lara05
        with fastdissolve
        voice "lara/intro08"
        lc "That is a ridiculous Hollywood cliché. There are 65 million of us Brits, are you seriously suggesting we are all evil?"
        mc "Err, no I guess not. Guv'nor."
        hide lara05
        show lara01
        with fastdissolve
        show lara01 at center:
            breathe
        jump LaraCrotchDialogues
    "Do you happen to have an artefact I could use?" if lcspeak01 and lcspeak02:
        hide lara01
        show lara05
        with fastdissolve
        voice "lara/intro09"
        lc "I just came back from Cambodia where I unearthed the \"Precious Ring of Gollum\", but I'm afraid it's useless."
        mc "What do you mean? It sounds kinda powerful if you ask me."
        hide lara05
        show lara02
        with fastdissolve
        voice "lara/intro10"
        lc "I tried it on, didn't see any bloody difference. I ended up tossing it in the magma incinerator."
        mc "But..."
        hide lara02
        show lara04
        with fastdissolve
        voice "lara/intro11"
        lc "However, I might have heard of another ring that you might find useful. Considering your job description. The \"Prince Albert Cockring of Lust\". Heard of it?"
        mc "Err, no."
        voice "lara/intro12"
        lc "Follow me, I'm sure I have a book on where to find it somewhere..."
        jump LaraCrotchLibrary
        
label LaraCrotchLibrary:
scene lara06 with dissolve
voice "lara/intro12b"
lc "Let me think. It should be in that section..."
scene lara07 with dissolve
voice "lara/intro13"
lc "On the top shelf, where books on sexual artefacts are located..."
mc "Do you want me to hold the ladder steady Lara?"
scene lara08 with dissolve
voice "lara/intro14"
lc "Yeah, why not, I wouldn't want to have a silly accident after surviving the \"Temple of Imminent Doom\" two days ago."
voice "lara/intro14b"
lc "Let me look... Hold the ladder... There, I found it."
scene lara09 with dissolve
voice "lara/intro15"
lc "So, let's have a closer look. It says it's in the \"Temple of Lust\" near Angkor."
scene lara10 with dissolve
voice "lara/intro16"
lc "Oh bugger, that's where I was innit? I could have gotten it while I was there, couldn't I?"
mc "Yes, you could have. Indeed. That would have saved us quite a bit of time."
scene lara09 with dissolve
voice "lara/intro17"
lc "\"The Ring wil grant the wearer the ability to produce ungodly amounts of cum.\" That could be useful to you I'm going to guess."
mc "I come plenty as it is I'll have you know!"
scene lara11 with dissolve
voice "lara/intro18"
lc "Perhaps, but you have a spare slot on your cock in your stats screen. There's a reason for that."
mc "What stats screen?"
show statsiconscreenidle
voice "lara/intro19"
lc "The one you access by clicking the icon that's on the top left of your screen, can't you see it?"
mc "Oh yeah, I see it now. It wasn't there just before you mentioned it though."
voice "lara/intro20"
lc "Well click on it, what are you waiting for?"
window hide
hide statsiconscreenidle
call screen statscreeniconfirst()

label StatscreenFirst():
hide screen statscreeniconfirst
show equipmentscreen at left with moveinleft
show equipmentbasicharness
show statsheroesicon
show statsvillainsicon
if evilness == 4:
    show goodbutton05 at posgood05
    show goodbutton06 at posgood06
    show goodbutton07 at posgood07
    show goodbutton08 at posgood08
    show goodbutton09 at posgood09
    show goodbutton10 at posgood10
if evilness == 5:
    show goodbutton06 at posgood06
    show goodbutton07 at posgood07
    show goodbutton08 at posgood08
    show goodbutton09 at posgood09
    show goodbutton10 at posgood10
if evilness == 6:
    show goodbutton07 at posgood07
    show goodbutton08 at posgood08
    show goodbutton09 at posgood09
    show goodbutton10 at posgood10
if evilness == 4:
    show text "{size=-10}{color=#00ff00}{font=Gui/Heroes Legend.ttf}+6{/font}{/color}{/size}" at posevil04   
if evilness == 5:
    show text "{size=-10}{color=#00ff00}{font=Gui/Heroes Legend.ttf}+5{/font}{/color}{/size}" at posevil05   
if evilness == 6:
    show text "{size=-10}{color=#00ff00}{font=Gui/Heroes Legend.ttf}+4{/font}{/color}{/size}" at posevil06   

voice "lara/intro21"
lc "See? That's your equipment screen on the left. There are slots on your body for various items to be added. And there's a slot for your dong too."
mc "Neat. Oh, and I can access the red and blue folders from here too it seems."
voice "lara/intro22"
lc "And on the right is your inventory. You own NOTHING right now."
mc "It's only the intro, I don't mind. And I DO have a superhero thong at least."
voice "lara/intro23"
lc "At the bottom of the equipment screen is your \"Scale of Evil-Goodness\". You can't see it right now so I'll stop talking."
window hide
pause
if evilness == 4:
    voice "lara/intro24a"
    lc "You're on +6 Goodness right now. So you're a pretty GOOD superhero."
if evilness == 5:
    voice "lara/intro24b"
    lc "You're on +5 Goodness right now. That was your starting point."
if evilness == 6:
    voice "lara/intro24c"
    lc "You're on +4 Goodness right now. You lost a point by choosing Emma Frost over the Black Widow and becoming more EVIL. Tss, tss."
    mc "I was asked a question and I answered it honestly! That was MY choice!"
    voice "lara/intro24d"
    lc "If you tip over into evil, God only knows what will happen."
    
call screen statsscreeninterfacefirst()
screen statsscreeninterfacefirst():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}[hero]{/font}" color "#ff0000" size 40 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posstatshero
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [renpy.hide_screen("statsscreeninterfacefirst"), renpy.hide_screen("statscreeniconfirst"), Jump ("FrostIntroEnd")]

label FrostIntroEnd:
hide screen statscreeniconfirst
scene lara11
show statsiconscreenidle
with dissolve
voice "lara/intro25"
lc "Now you know everything you need to know."
mc "What about that quest to retrieve this cockring?"
scene lara10
show statsiconscreenidle
with dissolve
voice "lara/intro26"
lc "There's a quest and mission log that's now available."
mc "Where?"
show questsiconscreenidle
voice "lara/intro27"
lc "Just below the stats screen... Go on, click on it."
call screen questscreeniconfirst()

label QuestscreenFirst():
hide screen questscreeniconfirst
show questscreen at left with moveinleft
show questscreenintro

voice "lara/intro28"
lc "See? The quest is now in your Quests screen on the right. And another one too, apparently, you need to find a superhero costume for Audit Girl."
mc "Without hints, this screen is rather useless..."
voice "lara/intro29"
lc "That's true, but a hints system has been implemented. Next time you access this screen, you can click on the icons to obtain them."
mc "What's the difference between a quest and a mission?"
voice "lara/intro30"
lc "A mission has a time limit. A quest doesn't. So relax, you have all the time in the world right now..."
mc "And what I am going to do while I wait?"
voice "lara/intro31"
lc "You could always re-play the lewd scenes you've been in so far. Get out of this screen and I'll show you."
window hide
call screen questsscreeninterfacefirst()
screen questsscreeninterfacefirst():
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [renpy.hide_screen("questsscreeninterfacefirst"), renpy.hide_screen("questscreeniconfirst"), Jump ("FrostIntroEnd02")]

label FrostIntroEnd02:
scene lara11
show statsiconscreenidle
show questsiconscreenidle
with dissolve
voice "lara/intro32"
lc "You can access the naughty gallery anytime in-game by pressing \"g\". That's \"g\" for GALLERY. I'll show you what it looks like at this stage."
show introgallery with dissolve
voice "lara/intro33"
lc "There only seems to be one lewd scene available for replay involving the Black Widow, that's why she's in technicolor. I wonder what you did to her... In the INTRO, no less."
mc "Err, let's not click on her then. I know it's there, it's all that matters... I'll peruse it in my own time when I'm... on my own."
hide introgallery with dissolve
mc "Okay, thanks for your help. I have one final question, considering you are a superhero. How do I use my superpowers?"
voice "lara/intro34"
lc "When the time comes for you to use a superpower, the corresponding icon will appear on the top left of your screen. And then you'll have two seconds to use it by clicking on it."
mc "Interesting..."
call screen usepower("useseduction", "LaraIntroNoSeduction", "LaraIntroSeduction") with dissolve

label LaraIntroSeduction:
scene lara10 with dissolve
voice "lara/intro35"
lc "Nice try [hero]. But you didn't really expect to seduce me when you're only on level 1 for Super-Seduction, did you?"
mc "It was worth a try..."
label LaraIntroNoSeduction:
mc "Is it the end of the intro now?"
voice "lara/intro36"
lc "Yes. Yes, it is. And therefore, you need to go back to your room and SLEEP."
mc "Okay, I get it."
stop music
hide statsiconscreenidle
hide questsiconscreenidle
jump Intro03

label IntroGame:
scene gothambackground
menu:
    "You picked Emma Frost during your visit (+1 Super-Villain)":
        call Evil from _call_Evil_1
        $ frostpicked = True
    "You picked the Black Widow during your visit (+1 Super-Hero)":
        call Good from _call_Good_1
        $ widowpicked = True
    "You picked neither (no change)":
        pass
stop channel1
show screen calendar
jump Intro03b

label Intro03:
scene intromcsleep01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with fade
mc "Time to go to bed... And to SAVE my game progress right now. Before I wake up. And save ONLY at that time, and NEVER within a screen, like the inventory or the quest log, cos that might corrupt my saves..."
scene mcwake01:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.04
with fade
play sound "sounds/yawn.mp3"
pause
stop sound
mc "Let's head to the main hall. I think this day is going to be AWESOME!"

label Intro03b:
$ d10locday = renpy.random.randint(1,10)
$ d10locnight = renpy.random.randint(1,10)
$ d10locnightpoolmilf = renpy.random.randint(1,2)
$ d10locnightpgroom = renpy.random.randint(1,2)
stop music
$ day = 3
$ period = 0
scene compoundhall01d with fade
show screen statscreenicon
show screen questscreenicon
show compoundmilf01 with moveinright
voice "milf/intro60"
cm "Good morning [name], I was expecting you."
mc "I'm here and READY to fight SEX CRIME!"
window hide
hide compoundmilf01
show compoundmilf02
with fastdissolve
voice "milf/intro61"
cm "Well, I don't actually have a mission for you today."
hide compoundmilf02
show compoundmilf04
with fastdissolve
voice "milf/intro62"
cm "But I received a phone call from Lois Pane asking you to come over to the Cockham Planet offices for a photoshoot session."
mc "What's that about?"
window hide
hide compoundmilf04
show compoundmilf06
with fastdissolve
voice "milf/intro63"
cm "Something about a Superheroes Calendar that she does every year."
mc "Ok, maybe I'll go. How do I get there?"
hide compoundmilf06
show compoundmilf01
with fastdissolve
voice "milf/intro64"
cm "Ah, this is where our giant Cockham interactive map comes in handy! Let me show you."
scene hallwallformap01 with dissolve
voice "milf/intro65"
cm "There it is. I hang in in the Main Hall to track our adversaries based on their last known locations. I haven't had much success so far..."
scene hallwallformap02 with dissolve
voice "milf/intro66"
cm "Hopefully, you will help the League add more knowledge to it..."
scene hallwallformap01 with dissolve
voice "milf/intro67"
cm "Now let's zoom in on the map shall we?"
scene cockhammap with dissolve
show placeplanet at posplanet
show placeccpd at posccpd
show placefrostgrey at posfrost
show placemafiagrey at posmafia
show placemayorsgrey at posmayors

voice "milf/intro68a"
cm "Our compound is located on a secure island on the City's west Coast, facing Old Cockham."
voice "milf/intro68b"
cm "All you have to do is click on the icon for the Cockham Planet Offices to get there... by your own means of transportation. The underground in your case at this stage since you can't fly."
mc "What's those other places I see?"
voice "milf/intro69"
cm "The grey ones are unavailable so far I'm afraid. But the CCPD, in Old Cockham, is a place you might also want to visit soon. Captain Sawyer might give you a mission if she's had reports of a major SEX CRIME."
mc "Right, so I guess, right now, I have to choose between Lois Pane and a photoshoot or the CCPD and a mission... Let me ponder that for a while..."
call screen cockhammapintro()
screen cockhammapintro():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [renpy.hide_screen("cockhammapday"), Return]
    button:
        xpos 257
        ypos 426
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapday"), Jump ("OfficeCCPD")]
    button:
        xpos 496
        ypos 369
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapday"), Jump ("CockhamPlanet")]
        

scene compoundhall01d
scene hallwallformap02 with dissolve
voice "milf/intro70"
cm "Oh, so you've decided to not go to Cockham City today?"
mc "Yep. I'm staying in the compound."
voice "milf/intro71"
cm "I suppose... you can do that too. Go back to your room then and think about what you want to do in the compound today..."
mc "Rightee-o."
jump MCRoomDay
