label LaraRoomDay:
scene laraplace with fade
if laraplacesaid == False:
    $ laraplacesaid = True
    mc "Ah, it's empty. Lara must be overseas and her butler is keeping the fire alive so that the dev doesn't have to re-render that scene."
    stop music
    jump MainTime
mc "Ah, it's empty. Lara must be overseas and her butler is keeping the fire alive so that the dev doesn't have to re-render that scene."
stop music
jump MainTime

label LaraRoomNight:
if mission07win and spokelaramission07 == False:
    $ spokelaramission07 = True
    scene laraplace with fade    
    show lara01 with moveinright
    show lara01 at center:
        breathe
    lc "Ah, it's you, [name]."
    if laradagger:  
        mc "Yeah, I was wondering what you did with that dagger of Ra's-Al-Ghul..."
        hide lara01
        show lara02
        with fastdissolve
        lc "I told you I would destroy it and that's what I did. By throwing it in the magma incinerator."
        mc "Ah, damn. It might have been useful to me. I mean us. The League, you know."
        hide lara02
        show lara03
        with fastdissolve
        lc "I don't believe summoning an evil army of shadow assassins is what the League stands for."
        mc "Err. Yeah, I guess you're right."
        jump Main
    if emmadagger:  
        mc "I wanted to apologize for throwing that dagger to Emma Frost instead of you. Got confused, don't know what went through my mind really..."
        hide lara01
        show lara05
        with fastdissolve
        lc "I fear your apologies, while accepted, have unleashed a power beyond our control. You should never have given that evil dagger to Emma Frost!"
        mc "I'll try and sort it out."
        hide lara05
        show lara03
        with fastdissolve
        lc "With your dick I imagine?"
        mc "Most likely. Good night, Lara."
        jump Main
    
if mission05end == False and mission05 and seenembassy:
    scene laraplace with fade    
    show larabikini01 with moveinright
    lc "Ah, it's you, [name]. I was about to go for a swim. In my PRIVATE swimming pool."
    mc "Before you go, I need that Jewel of Mind Control. To de-program Natasha. Orders come from the top!"
    hide larabikini01
    show larabikini02
    with fastdissolve
    lc "The top? Meaning Captain MILF?"
    mc "That's right. Natasha is turning into a total commie and we can't have radical leftists lunatics running around the compound like that."
    hide larabikini02
    show larabikini01
    with fastdissolve
    lc "The jewel would be useless in YOUR hands. It can only be used by a WOMAN."
    mc "Ah, damn. Then you'll have to do it?"
    hide larabikini01
    show larabikini02
    with fastdissolve
    lc "Let me think. I did invite Natasha tonight for our weekly swimming practice. But if I were to try and deceive her, she would probably Super-Snese it."
    lc "You need to hide in the shadows and pass the jewel to me at the most crucial moment."
    mc "Alright, I can do that! What will that crucial moment be?"
    hide larabikini02
    show larabikini03
    with fastdissolve
    lc "You'll have to Super-Sense yourself when it's about to happen... Quick, hide, I hear her footsteps!"
    jump LaraWidowPoolMission05

if d10locnight >= 5 and d10locnight <= 10 and inventorylustring == False:
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade
    show lara01 with moveinright
    show lara01 at center:
        breathe
    lc "Ah, it's you, [name]."
    mc "Yeah, I think I'm ready to go on that Cockring Quest."
    if mcagility == 0 and mccombat == 0:        
        hide lara01
        show lara05
        with fastdissolve
        lc "I don't think so. You have neither Super-Agility nor Super-Combat. This quest is too dangerous for you until you level up in at least one of these Super-Powers..."
        mc "Ah. I see. I'll be back... Goodnight, Lara."
        hide lara05
        show lara04
        with fastdissolve
        lc "...When you're READY. Goodnight, [name]."
        jump Main
    if (mission01 and mission01end == False) or (mission03 and mission03end == False): 
        hide lara01
        show lara05
        with fastdissolve
        lc "I don't think so. You have an ongoing mission and Cambodia is in a land far, far away. It would jeopardize your mission."
        mc "Ah. I see. I'll be back... Goodnight, Lara."
        hide lara05
        show lara04
        with fastdissolve
        lc "...When you've completed your MISSION. Goodnight, [name]."
        jump Main        
    if mcagility >= 1 or mccombat >= 1:                
        hide lara01
        show lara03
        with fastdissolve
        lc "I suppose we could go. My private jet is fuelled up. Let me get changed into my adventuring gear..."
        mc "Fine, I'm... already wearing my adventuring gear so I'll wait for you...."
        jump LaraCockRingQuest

if d10locnight >= 5 and d10locnight <= 10 and inventorylustring and mclevel02 == False:
    if questhulk and questhulkcompleted == False and hulkescaped == False:
        $ d2lochulk = renpy.random.randint(1,2)
        if d2lochulk == 2:
            jump HulkCompound    
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade    
    show lara01 with moveinright
    show lara01 at center:
        breathe
    lc "Ah, it's you, [name]."
    mc "Yes indeed it is. Are you planning on going on any exciting and sex-filled adventures, Lara?"
    hide lara01
    show lara03
    with fastdissolve
    lc "Maybe. But I don't need YOU where I'm going. At this stage."
    mc "Damn, I was really looking forward to some more sexy fu..."
    hide lara03
    show lara05
    with fastdissolve
    lc "Enough, I get it! Just wait for an update that includes ME."
    mc "I don't have Super-Patience!"
    hide lara05
    show lara02
    with fastdissolve
    lc "* sigh * Just go back to your room and have a wank or something, alright?"
    jump Main

if d10locnight >= 5 and d10locnight <= 7 and inventorylustring and mclevel02 and quest05end and quest06end == False and quest06:
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade    
    show lara02 with moveinright
    show lara02 at center:
        breathe
    lc "So, I gather you came because you are READY for an Egyptian adventure?"
    mc "That's right, let's go!"
    hide lara02
    show lara04
    with fastdissolve
    lc "I will change into my adventurer's costume while you, err... stay the same."
    mc "Not time wasting changing costume with me!"
    $ egyptlara02 = True
    jump LaraEgypt

if d10locnight >= 5 and d10locnight <= 7 and inventorylustring and mclevel02 and quest05end and quest06end == False and quest06 == False:
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade    
    show lara01 with moveinright
    show lara01 at center:
        breathe
    lc "Ah, it's you, [name]. Just the man I was looking for."
    mc "For some HO-O-OT SEX I presume."
    hide lara01
    show lara03
    with fastdissolve
    lc "No. For a dangerous adventure in Egypt to bring the Mind Jewel of Cleopatra back to the compound."
    window hide
    play sound "sounds/achievement.mp3"
    $ quest06 = True
    show questicon06 at poslocation
    $ renpy.pause(0.5, hard=True)
    show textquest06 at posmissiontext
    pause    
    mc "What's it got to do with me?"
    hide questicon06
    hide textquest06
    hide lara03
    show lara05
    with fastdissolve
    lc "Are YOU a superhero ADVENTURER or are you a WIMP?"
    mc "Err... I feel this is a trick question but I'll answer anyway: I ain't NO WIMP!"
    hide lara05
    show lara02
    with fastdissolve
    lc "Which is why you will come with me to retrieve the artefact. This sparkling green jewel would be immensely dangerous if it fell into the wrong hands."
    mc "Why so? It's just a jewel..."
    hide lara02
    show lara05
    with fastdissolve
    lc "It's a MIND CONTROL Jewel. Queen Cleopatra used it to control her entire slave army and especially her personal SEX slaves."
    mc "Oooh, she had SEX slaves?"
    lc "Yes, like all female pharaohs. If a Super-Villain were to get a hold of it, especially Emma Frost, he or she could yield immense power over the entire city!"
    hide lara05
    show lara01
    with fastdissolve
    lc "So, are you READY for an adventure, young hero? LIke RIGHT NOW?"
    menu:
        "Yeah, just not right now, got stuff to do, busy, busy.":
            hide lara01
            show lara03
            with fastdissolve
            lc "Come back when you ARE ready then, we should not wait too long, others covet this treasure too!"
            jump Main
        "Damn right, I'm ready, let's go!":
            hide lara01
            show lara04
            with fastdissolve
            lc "I will change into my adventurer's costume while you, err... stay the same."
            mc "Not time wasting changing costume with me!"
            $ egyptlara = True
            jump LaraEgypt

if d10locnight >= 5 and d10locnight <= 7:
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade    
    show lara01 with moveinright
    show lara01 at center:
        breathe
    lc "Ah, it's you, [name]."
    mc "Yes indeed it is. Are you planning on going on any exciting and sex-filled adventures, Lara?"
    hide lara01
    show lara03
    with fastdissolve
    lc "Maybe. But I don't need YOU where I'm going. At this stage."
    mc "Damn, I was really looking forward to some more sexy fu..."
    hide lara03
    show lara05
    with fastdissolve
    lc "Enough, I get it! Just wait for an update that includes ME."
    mc "I don't have Super-Patience!"
    hide lara05
    show lara02
    with fastdissolve
    lc "* sigh * Just go back to your room and have a wank or something, alright?"
    jump Main

if d10locnight >= 8 and d10locnight <= 10 and inventorylustring and mclevel02:
    if questhulk and questhulkcompleted == False and hulkescaped == False:
        $ d2lochulk = renpy.random.randint(1,2)
        if d2lochulk == 2:
            jump HulkCompound
    stop music
    play music "sounds/fire.mp3"
    scene laraplace with fade    
    show larabikini01 with moveinright
    lc "Ah, it's you, [name]. I was about to go for a swim. In my PRIVATE swimming pool."
    if seenlarapool == False:
        mc "Oooh. And you just invited me to join you, right?"
        call screen usepower("useseduction", "NoLaraPool", "YesLaraPool") with dissolve
        label NoLaraPool:
            hide larabikini01
            show larabikini02
            with fastdissolve
            lc "I don't think so. I'm pretty sure I bloody well didn't invite you! Goodnight, [name]."
            window hide
            hide larabikini02 with moveoutright
            jump Main
        label YesLaraPool:
            if mcseduction <= 1:
                mc "Shit, my Super-Seduction levels are not high enough to seduce Lara..."
                jump NoLaraPool    
        hide larabikini01
        show larabikini03
        with fastdissolve
        lc "I could use some... nice company. I hope you have some speedos on you."
        mc "I'm always equipped for such occasions!"
        lc "Let's go then, follow me..."
        $ usedseduction += 1
        jump LaraPool
    if seenlarapool:
        hide larabikini01
        show larabikini03
        with fastdissolve
        lc "And I'm willing to bet you'd like to join me, innit?"
        mc "In, definitely, nit!"
        jump LaraPool
            
if laraplacesaid == False:
    scene laraplace with fade
    $ laraplacesaid = True
    mc "Ah, it's empty. Lara must be overseas and her butler is keeping the fire alive so that the dev doesn't have to re-render that scene."
    stop music
    jump MainTime
scene laraplace with fade
mc "Ah, it's empty. Lara must be overseas and her butler is keeping the fire alive so that the dev doesn't have to re-render that scene."
stop music
jump MainTime

label LaraCockRingQuest:
stop music
play music "sounds/plane.mp3"
scene laraplane01 with fade
mc "We could have asked Powergirl to carry us there faster, no?"
voice "lara/temple01"
lc "Her Super-Flight skills aren't high enough to carry two people. And would you trust Superman?"
mc "No, I wouldn't trust Superman."
scene laraplane02 with fastdissolve
voice "lara/temple02"
lc "Neither would I. He doesn't even have a cock."

label laraTempleOutside:
$ period = 0
$ day += 1
stop music
play music "sounds/croft02.mp3"
scene laratemple01 with fade
voice "lara/temple03"
lc "Here's the entrance to the Temple of Lust. Looks like we'll have to jump across. Follow my lead."
scene laratemple02 with dissolve
voice "lara/temple04"
lc "All you have to do is jump..."
scene laratemple03 with fastdissolve
play sound "sounds/femalegrunt01.mp3"
voice "lara/temple05"
lc "...VERY FAR!"
scene laratemple04 with dissolve
voice "lara/temple06"
lc "And then land comfortably on the other side of that precipice."
mc "Err, that WAS quite far indeed."
scene laratemple05 with dissolve
voice "lara/temple07"
lc "This is the first obstacle to test your -how do you say- pluck. Come, do not fear, this is merely an appetizer for the perils ahead."
mc "Err, okay."
scene laratemple06 with dissolve
play sound "sounds/mangrunt01.mp3"
if mcagility >= 1:
    call screen usepower("useagility", "LaraNoAgility", "LaraAgility") with dissolve

label LaraNoAgility:
mc "Uh oh..."
scene laratemple07 with dissolve
mc "HELP! I'm falling!"
voice "lara/temple08"
lc "Take my hand. I will lift you up."
scene laratemple08 with dissolve
play sound "sounds/panting.mp3"
mc "That was almost a game over..."
jump LaraTempleEnter
label LaraAgility:
$ usedagility +=1
scene laratemple09 with dissolve
mc "I did it! I'm like, Super-Agile!"
voice "lara/temple09"
lc "Let's not exaggerate, that was merely a small hop. Come, we must carry on."
label LaraTempleEnter:
scene laratemple10 with dissolve
voice "lara/temple10"
lc "And so, we breach the sanctum of the ancients. The first footfalls in this tomb for centuries."
mc "This place gives me the creeps. After you, Lara."
play sound "sounds/doorsqueak.mp3"
$ renpy.pause(0.5, hard='True')
scene laratemple11 with fade
stop music
play music "sounds/croftintro.mp3"
voice "lara/temple11"
lc "All is not as it seems. Concealed traps and pitfalls await the unwary. You must stay close and follow my instruction."
mc "You talk like some NPC explaining the rules in a video game, you know that?"
scene laratemple12 with dissolve
voice "lara/temple11"
lc "All is not as it seems. Concealed traps and pitfalls await the unwary. You must stay close and follow my instruction."
mc "I see what you did there."
voice "lara/temple12"
lc "I will go first.... Be careful now, child. We have little time for incompetence."
mc "Child? I'm a SUPERHERO!"
scene laratemple13 with dissolve 
play channel1 "sounds/pillar.mp3"
voice "lara/temple13"
lc "You must have triggered a trap, I fear the ceiling is bearing down on us. Quick, we must run, there must be a lever at the end of the tunnel!"
mc "Hang on, I'll use my Super-Strength and stop that stupid ceiling from turning us into pancakes while you get that lever!"
scene laratemple14 with dissolve   
voice "lara/temple14"
lc "I hope you succeed, our lives depend upon your massive muscles!"
call screen usepower("usestrength", "LaraNoStrength", "LaraStrength") with dissolve
label LaraStrength:
$ usedstrength += 1
scene laratemple15 with dissolve   
play sound "sounds/mangrunt01.mp3"
mc "I'm... I don't think I can hold much longer, this ceiling is damn HEAVY!"
voice "lara/temple15"
lc "Hang on, I think I found the lever..."
stop channel1
play sound "sounds/clank.mp3"
scene laratemple16 with dissolve   
voice "lara/temple16"
lc "There, I have activated the reversal process... We are good to go!"
scene laratemple17 with dissolve   
mc "Thanks to my MASSIVE MUSCLES."
voice "lara/temple17"
lc "Stop bragging and follow me into the inner courtyard."
jump LaraTempleInside
label LaraNoStrength:
scene laratempledead with dissolve   
mc "Help, I have either a suicidal or a spastic player controlling me, we are about to die!"
scene blackscreen with fade
play sound "sounds/splat.ogg"
show gameovericon:
    xpos 600 ypos 400
pause
return

label LaraTempleInside:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play channel2 "sounds/waterrun.mp3"
stop music
play music "sounds/croft02.mp3"
scene laratemple20 with dissolve   
voice "lara/temple18"
lc "Finally, we reach the heart of the Temple. This is where the biggest dangers lie. Usually."
mc "Looks pretty peaceful to me."
voice "lara/temple19"
lc "Now, to find out how to obtain that Cockring of Lust...."
mc "What does your notebook say?"
scene laratemple21 with dissolve   
voice "lara/temple20"
lc "That we must enter the pool to retrieve the Sacred Bowl and be wary of snares."
mc "What snares?"
scene laratemple22 with dissolve   
voice "lara/temple21"
lc "There is no mention of that in the text. Well, I'm up to the challenge, I will change into my two-piece swimsuit. It doesn't look like you need to change into any swimming gear by the looks of it."
mc "I still need to take my shoes off. I'm gonna feel naked without them."
scene laratemple23 with dissolve
mc "Is the water temperature nice? Like, my huge nuts won't shrivel up?"
voice "lara/temple22"
lc "Just get in the water, will you? We must find these artefacts as fast as we can, before..."
scene laratemple26 with dissolve 
play sound "sounds/diving.mp3"
voice "lara/temple23"
lc "What is this dreadful creature?"
scene laratemple27 with dissolve   
mc "Looks like a giant octopus with cock-tentacles to me."
voice "lara/temple24"
lc "AAAH, it is trying to find its way into MY inner sanctum! I need... to reach... for my blade!"
scene laratemple28 with dissolve   
play sound "sounds/lick01.ogg"
mc "I think it found it..."
voice "lara/temple25"
lc "Damn you, vile creature!"
scene laratemple29 with dissolve   
play sound "sounds/moan06.ogg"
voice "lara/temple26"
lc "Get in there and stop that sperm-tacle from going any deeper, [name]!"
scene laratemple30 with dissolve   
mc "Alright, muscle-hero is GO!"
if mccombat >= 1:
    call screen usepower("usecombat", "LaraTempleNoCombat", "LaraTempleCombat") with dissolve

label LaraTempleNoCombat:
scene laratemple31b with dissolve
play sound "sounds/punch.mp3"
mc "Uh..."
voice "lara/temple27"
lc "That was kinda useless, now I have to deal with this monster on MY OWN! First, I need to cut off the constraining tentacle..."
play sound "sounds/knifecut.mp3"
voice "lara/temple28"
lc "There!"
scene laratemple32b with dissolve
play sound "sounds/femalegrunt01.mp3"
voice "lara/temple29"
lc "And now for the sperm-tacle! HIYAAH!"
scene laratemple33
show laratemple33b
with dissolve
play sound "sounds/knifecut.mp3"
voice "lara/temple30"
lc "My trusted blade will bleed this thing to death!"
jump LaraTempleEndCombat

label LaraTempleCombat:
$ usedcombat += 1
scene laratemple31 with dissolve 
play sound "sounds/knifecut.mp3"
voice "lara/temple31"
lc "Hold it still while I cut off the constraining tentacle! There, got you!"
play sound "sounds/mangrunt01.mp3"
mc "Stop moving, you damn sperm-tacle!"
scene laratemple32 with dissolve 
play sound "sounds/splooge01.mp3"
mc "Hey, this fucking thing is spewing all over me!"
play sound "sounds/femalegrunt01.mp3"
voice "lara/temple32"
lc "Hang tight, I'm free from the grip of its other tentacle now!"
scene laratemple33 with dissolve 
mc "YUCK! I've got slimy squid-sperm on my face!"
play sound "sounds/knifecut.mp3"
voice "lara/temple33"
lc "I'm going to cut this bloody sperm-tacle in half with my trusted blade!"

label LaraTempleEndCombat:
scene laratemple34 with dissolve 
voice "lara/temple34"
lc "Finally, this horrible creature has perished... We can now dive into the pool and retrieve the Sacred Bowl."
mc "Err, maybe I'll let you do that. That way, I can keep an eye out for any FURTHER snares. And wipe my face clean of that filthy spunk."
scene laratemple35 with dissolve 
play sound "sounds/diving.mp3"
voice "lara/temple35"
lc "Fine, I'll get it. ON MY OWN."                               
scene laratemple36 with dissolve 
stop channel2
play channel2 "sounds/underwater.mp3"
mc "* Hopefully, she finds it, this place is super-creepy... I mean, sperm-tacles, really? Who came up with this shit? *"
scene laratemple37 with dissolve 
stop channel2
play channel2 "sounds/waterrun.mp3"
voice "lara/temple36"
lc "Here, I got it, innit?"
mc "Oh cool, let's get out of this dark pool pronto before more tentacles emerge."
scene laratemple38 with dissolve
voice "lara/temple37"
lc "First, I will place the Sacred Bowl in front of the statue of the God of Lust."
mc "Ok. When do I get that cock ring?"
scene laratemple39 with dissolve
voice "lara/temple38"
lc "According to the legend, once you've filled it up with your seed."
mc "WTF???"
voice "lara/temple39"
lc "What did you expect? You think the God of Lust just gives out cockrings willy-nilly?"
mc "Err, that's a pretty BIG bowl."
scene laratemple40 with dissolve
voice "lara/temple40"
lc "I'm sure a strapping young lad like you won't have any problems filling it up. I estimate a quart of sperm will suffice."
mc "I'm gonna need... some help. You know, like something stimulating. Or I'll never be able to come THAT MUCH."
voice "lara/temple41"
lc "And you expect me to provide that `\"stimulation\" I assume?"
mc "I don't see any other sexy girl around here..."

voice "lara/temple42"
lc "Fine, I'll will undress for you then..."
stop channel2
stop music
play channel2 "sounds/sexy07.mp3"
scene laratemplestrip01:
    subpixel True
    ypos 0.0
    linear 6.0 ypos -1.0
with dissolve
$ renpy.pause(5.0, hard='True')
voice "lara/temple43"
lc "Are you getting hard, [name]?"
scene laratemplestrip02:
    subpixel True
    ypos -1.0
    linear 6.0 ypos 0.0
with dissolve
$ renpy.pause(5.0, hard='True')
mc "I'm certainly getting there..."
scene laratemple41 with dissolve
voice "lara/temple44"
lc "I can see that... You have a MASSIVE hardon..."
mc "All thanks to you, Lara..."
scene laratemple42 with dissolve
mc "And a MASSIVE desire to FUCK you..."
if age >= 20:
    voice "lara/temple45a"
    lc "Hey, hold your horses, young man... This is purely professional to get your monstercock to unleash a great big fat load."
if age >= 18 and age <= 19:
    voice "lara/temple45b"
    lc "Hey, hold your horses, young man... This is purely professional to get your teenage monstercock to unleash a great big fat load."
mc "Err... Can I at least use your body to achieve this..."
voice "lara/temple46"
lc "I suppose. I'll turn round and you can pretend to fuck me."
scene laratemple43 with dissolve
mc "Fuck yeah, just the rubbing from your thighs as my shaft pummels between your legs will be enough to make me cum."
voice "lara/temple47"
lc "Use my thighs as your personal wanksheath then, [name]!"
play music "sounds/wank.mp3"
stop channel1
window hide

label LaraTempleSlowFuck:
window hide
show laratemplewankslowvideo behind laratemplewankfastvideo
show laratemplewankslowvideo behind laratemplesideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple48"
lc "Mmmh, just like that. And play with my big boobs..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen laratemplefuckslow()
screen laratemplefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleFastFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSideSlow")

label LaraTempleFastFuck:
window hide
show laratemplewankfastvideo behind laratemplewankslowvideo
show laratemplewankfastvideo behind laratemplesidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex05.mp3"
hide laratemplesidefastvideo
hide laratemplewankslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple49"
lc "Yes, go on, pound that great big whopper between my thighs..."
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sideicon:
     xpos 50 ypos 500     
call screen laratemplefuckfast()
screen laratemplefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSlowFuck")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSideFast")


label LaraTempleSideSlow:
window hide
show laratemplesideslowvideo behind laratemplewankslowvideo
show laratemplesideslowvideo behind laratemplesidefastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide laratemplesidefastvideo
hide laratemplewankslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
with dissolve
voice "lara/temple50"
lc "I love how your fuckstick reaches so far in front of me..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratemplesidefuckslow()
screen laratemplesidefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSideFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSlowFuck")

label LaraTempleSideFast:
window hide
show laratemplesidefastvideo behind laratemplewankfastvideo
show laratemplesidefastvideo behind laratemplesideslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex03.mp3"
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
voice "lara/temple51"
lc "I can feel your strong abs pounding against my ass, mmhh..."
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratemplesidefuckfast()
screen laratemplesidefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSideSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleFastFuck")

label LaraTempleFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide sideicon
mc "I'm gonna cum, Lara!"
voice "lara/temple52"
lc "Not yet, I need to get the bowl!"
scene laratemplecum01 with dissolve
hide laratemplewankfastvideo
hide laratemplesideslowvideo
hide laratemplesidefastvideo
hide laratemplewankslowvideo
stop music
stop channel1
play channel1 "sounds/splooge02.mp3"
play sound "sounds/moan03.mp3"
mc "Too late, RHAAA!"
window hide
with fastflash
voice "lara/temple53"
lc "Aim for the bowl!"
scene laratemplecum02a with dissolve
play sound "sounds/boymoan05.mp3"
mc "I can't aim, I'm CUUUU-UUU-MMMIIING!"
window hide
with fastflash
voice "lara/temple54"
lc "Then I'll take charge of your disgorging cum-cannon!"
show laratemplecum02b with fastdissolve
voice "lara/temple55"
lc "We're not even CLOSE to filling it up!"
window hide
with fastflash
play sound "sounds/boymoan03.mp3"
mc "That's the last of it, AAAH!"
stop channel1
scene laratemplecum03 with dissolve
play sound "sounds/panting.mp3"
voice "lara/temple56"
lc "That was a BAD idea, there's more cum OUTSIDE the bowl than INSIDE and it's only HALF-FULL!"
mc "Who says I can't keep on going?"
scene laratemplecum04 with dissolve
voice "lara/temple57"
lc "What? You're STILL hard?"
mc "Hey, I'm a Super-Hero, remember?"
scene laratemplecum05 with dissolve
voice "lara/temple58"
lc "You ARE indeed... Seeing your rock-hard leaking shaft makes me want to SLURP on your fat bullballs!"
mc "Be my guest, Lara... That'll help me churn up another HUGE load."
scene laratemplecum06 with dissolve
play sound "sounds/slurp.mp3"
mc "Yeah, try and get one massive testicle in your mouth, you can do it..."
lc "Mmmgggbbb..."
mc "That's enough, I'm fucking horny for your PUSSY now!"
scene laratemplecum07 with dissolve
play sound "sounds/moan02.mp3"
mc "Are you ready to get impaled on my Superhero cock, Lara?"
voice "lara/temple59"
lc "Y...Yes, I am. Fuck me, fuck me HARD like the Super-Stud that you are!"
window hide

label LaraTempleSlowUp:
window hide
show laratemplefuckslowvideo behind laratemplefuckfastvideo
show laratemplefuckslowvideo behind laratempledownslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen laratempleupslow()
screen laratempleupslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleFastUp")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleDownSlow")

label LaraTempleFastUp:
window hide
show laratemplefuckfastvideo behind laratemplefuckslowvideo
show laratemplefuckfastvideo behind laratempledownfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide laratemplefuckslowvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show assview:
     xpos 50 ypos 500     
call screen laratempleupfast()
screen laratempleupfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleSlowUp")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleDownFast")


label LaraTempleDownSlow:
window hide
show laratempledownslowvideo behind laratemplefuckslowvideo
show laratempledownslowvideo behind laratempledownfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownfastvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratempledownfuckslow()
screen laratempledownfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleDownFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleSlowUp")

label LaraTempleDownFast:
window hide
show laratempledownfastvideo behind laratemplefuckfastvideo
show laratempledownfastvideo behind laratempledownslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide cum
hide faster
hide slower
hide assview
hide sceneicon
with dissolve
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen laratempledownfuckfast()
screen laratempledownfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraTempleDownSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraTempleUpEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraTempleFastUp")

label LaraTempleUpEnd:
hide cum
hide faster
hide slower
hide assview
hide sceneicon
voice "lara/temple60"
lc "Please hurry up, my cunt is getting DESTROYED by the ungodly width of your love muscle!"
mc "I'm almost there, Lara. I'm about to..."
window hide
scene laratemplefuckcum01 with dissolve
hide laratemplefuckslowvideo
hide laratemplefuckfastvideo
hide laratempledownslowvideo
hide laratempledownfastvideo
stop channel1
play channel1 "sounds/splooge01.mp3"
play music "sounds/boyorgasm01.mp3"
mc "BLOW.... RHAAAA!"
window hide
with fastflash
voice "lara/temple61"
lc "Godammit boy, you're doing it again, you're NOT pumping your seed into the bowl!"
with hpunch
window hide
with fastflash
play sound "sounds/womancum02.mp3"
voice "lara/temple62"
lc "You're pumping DIRECTLY into my womb, aaah!"
scene laratemplefuckcum02 with dissolve
mc "AAAH! I'm gonna fill you up till it's cascading out of your fuckhole!"
with hpunch
window hide
with fastflash
voice "lara/temple63"
lc "I can feel every POWERFUL blast, keep PUMPING!"
window hide
with fastflash
voice "lara/temple64"
lc "Pull me up, I'm getting bloated with your cream!"
scene laratemplefuckcum03 with dissolve
stop music
stop channel1
play sound "sounds/panting.mp3"
mc "Fuck yeah, that was another SPUNKY load..."
voice "lara/temple65"
lc "Now put me down, I need to check whether the Sacred Bowl is finally full... And whether we need ANOTHER load from you or not..."
scene laratemplefuckcum04 with dissolve
stop channel2
play music "sounds/waterrun.mp3"
voice "lara/temple66"
lc "This time, you managed to fill up the Sacred Bowl to the brim... Thanks God, I don't think my poor pussy could have taken another pounding like that..."
mc "Too bad, I could go ON and ON if I wanted to... * wink *"
voice "lara/temple67"
lc "Keep your strength, you must remain hard for the next phase. The magical transfer of the Prince Albert Cockring of Lust to your giant phallus!"
scene laratemplefuckcum05 with dissolve
play sound "sounds/coldwind.mp3"
mc "That sound is ominous..."
voice "lara/temple68"
lc "Do not fear, we have followed what my notebook says, it should be fi..."
scene laratemplefuckcum06 with dissolve
with hpunch
play sound "sounds/magic.mp3"
mc "What the?..."
scene laratemplefuckcum07 with dissolve
voice "lara/temple69"
lc "The Cockring of Lust has been transferred to your phallus!"
$ inventorylustring = True
play sound "sounds/achievement.mp3"
show acquiredcockring at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Fuck yeah!"
scene laratemplefuckcum08 with dissolve
play sound "sounds/splooge02.mp3"
mc "AAAHHHH!!!!!"
with hpunch
window hide
with fastflash
voice "lara/temple70"
lc "What the? Why are you cumming like that?"
play sound "sounds/splooge01.mp3"
with hpunch
window hide
with fastflash
play sound "sounds/boymoan04.mp3"
mc "I can't help myself, it just came out like that, RHAAAA!"
scene laratemplefuckcum09 with dissolve
stop sound
voice "lara/temple71"
lc "Finally, your MEGA-ORGASM is over..."
mc "And my cock ring is disappearing... Why is this happening?"
scene laratemplefuckcum10 with dissolve
play sound "sounds/slurp.mp3"
voice "lara/temple72"
lc "Don't you worry, this was to be expected. It is an invisible ring. But it is there, and you should see it in your inventory..."
mc "Oh cool, we didn't do all this for nothing then."
voice "lara/temple73"
lc "Just make sure nobody ever steals it. Especially Super-Villains. Let's get dressed and go back to Cockham City now..."
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label LaraPool:
$ seenlarapool = True
play music "sounds/croftintro.mp3"
scene larapool01 with fade
if larapoolsaid:
    lc "You remember my private pool? We've been here before..."
    mc "Damn, I sure remember Lara!"
if larapoolsaid == False:
    lc "This is my private pool. And over yonder, there is a helipad so I'm ready to take off at a moment's notice."
    $ larapoolsaid = True
scene larapool02 with dissolve
lc "Last one in is a chicken-shit superhero adventurer!"
play sound "sounds/diving.mp3"
mc "Hey!"
scene larapool03 with dissolve
lc "Come on, are you scared or something?"
mc "No I'm not... I just... don't like cold water. My cock doesn't at least."
scene larapool04 with dissolve
lc "The water is warmed to a perfect temperature all year round... Your cock shouldn't have anything to fear."
mc "* Damn, look at those tits... *"
scene larapool05 with dissolve
lc "I could check if you want..."
mc "Check what?"
scene larapool06 with dissolve
play sound "sounds/underwater.mp3"
mc "* Ah, now I get it... Maybe I should get HARD for her then... *"
scene larapool07 with dissolve
mc "* Yeah... That's it, get hard, cock!"
scene larapool08 with dissolve
stop sound
mc "She's fondling my shaft... This is about to get STEAMY!"
scene larapool09 with dissolve
play sound "sounds/underwater.mp3"
mc "* Oooh, fuck, she's pulling my speedoes down... Just in time as I'm getting... *"
scene larapool10 with dissolve
mc "* ... ROCK-HARD! *"
scene larapool11 with dissolve
stop sound
mc "Fuck yeah, my cock is so fucking BIG now, need to hold it steady before I blow my load!"
scene larapool12 with dissolve
play sound "sounds/underwater.mp3"
mc "* Oh God, she's sucking my balls... underwater. *"
window hide
stop sound
play channel1 "sounds/lick02.mp3"
show larapoollickvideo with dissolve
pause 1.0
play channel2 "sounds/boymoan04.mp3"
mc "* And now she's licking all the way up my shaft.... *"
window hide
pause
stop channel1
stop channel2
scene larapool13 with dissolve
if laratoldcock:
    lc "Now I bet you want you to FUCK ME again with this enormous dong of yours, don't you? You're already drooling so much pre-cum..."
    mc "I'm so hard, I simply NEED to, Lara!"
if laratoldcock == False:
    lc "Now I bet you want you to FUCK ME with this enormous dong of yours, don't you? You're already drooling so much pre-cum..."
    mc "I'm so hard, I simply NEED to, Lara!"
scene larapool14 with dissolve
if age >= 20:
    lc "Then let's switch places. Get in the water and prep your giant tool while I remove my bikini bottom..."
if age >= 18 and age <= 19:
    lc "Then let's switch places. Get in the water and prep your giant teenage tool while I remove my bikini bottom..."
scene larapool20 with dissolve
if laratoldcock:
    play sound "sounds/moan02.mp3"
    lc "Pound me real good with it please, [name]!"
    mc "My SUPER-STUD powers will be on full display, don't you worry about that!"
    scene larapool21 with dissolve
    lc "Then, I think I'm ready... Even though your cock is truly IMMENSE."
if laratoldcock == False:
    play sound "sounds/moan02.mp3"
    lc "Your cock... It's even bigger than I remember!"
    mc "That's cos I grew a bit down there, now that I'm a level 2 Superhero..."
    scene larapool21 with dissolve
    lc "I... don't know if it will fit."
    mc "There's only one way to find out!"
    $ laratoldcock = True
stop sound

label LaraPoolFuckSlow:
$ larapoolfuckfast = False
window hide
show larapoolslowvideo behind larapoolfastvideo
show larapoolslowvideo behind larapoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide larapoolfastvideo
hide larapoolpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckslow == False:
    $ larapoolfuckslow = True
    lc "Your dick is so fucking big... I love it when you fuck me slowly like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen larapoolfuckslow()
screen larapoolfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckPOVSlow")

label LaraPoolFuckFast:
$ larapoolfuckslow = False
window hide
show larapoolfastvideo behind larapoolslowvideo
show larapoolfastvideo behind larapoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide larapoolpovfastvideo
hide larapoolslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckfast == False:
    $ larapoolfuckfast = True    
    if age >= 20:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant horsecock!"
    if age >= 18 and age <= 19:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant teen horsecock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen larapoolfuckfast()
screen larapoolfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckPOVFast")

label LaraPoolFuckPOVSlow:
$ larapoolfuckfast = False
window hide
show larapoolpovslowvideo behind larapoolslowvideo
show larapoolpovslowvideo behind larapoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide larapoolpovfastvideo
hide larapoolslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if larapoolfuckslow == False:
    $ larapoolfuckslow = True
    lc "Your dick is so fucking big... I love it when you fuck me slowly like that..."
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen larapoolpovfuckslow()
screen larapoolpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckSlow")

label LaraPoolFuckPOVFast:
$ larapoolfuckslow = False
window hide
show larapoolpovfastvideo behind larapoolfastvideo
show larapoolpovfastvideo behind larapoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide larapoolfastvideo
hide larapoolpovslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide pov
if larapoolfuckfast == False:
    $ larapoolfuckfast = True    
    if age >= 20:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant horsecock!"
    if age >= 18 and age <= 19:
        lc "That's it, give it to me HARD, POUND MY DRIPPING PUSSY with your giant teen horsecock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen larapoolpovfuckfast()
screen larapoolpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("LaraPoolFuckFast")

label LaraPoolFuckEnd:
hide cum
hide sceneicon
hide faster
hide slower
hide pov
lc "You're gonna pump a fat load inside my pussy aren't you?"
mc "Y... Yes, I'm..."
scene larapoolcum01 with dissolve
stop channel1
play sound "sounds/boymoan05.mp3"
mc "... BLOWING, AAAH!"
window hide
with hpunch
play channel2 "sounds/moan04.ogg"
lc "I can feel it, I'm coming too!"
scene larapoolcum02 with dissolve
stop channel2
play channel2 "sounds/splooge02.mp3"
lc "You're filling me up with so much spunk!"
window hide
with fastflash
play sound "sounds/kiss.mp3"
lc "Mmmh, kiss me while you cum DEEP inside me, STUD!"
scene larapoolcum03 with dissolve
lc "Mmmhh, you're a good kisser."
window hide
with fastflash
play sound "sounds/moan05.mp3"
lc "And a good CUMMER!"
scene larapoolcum04 with dissolve
play sound "sounds/moan02.mp3"
lc "I want you to pull out your disgorging dong and COVER MY TITS in your thick scum. Can you do that for me, [name]?"
scene larapoolcum05 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc "I'm... STILL BLOWING BIG TIME!"
window hide
with fastflash
lc "I can see THAT! It's FLYING everywhere!"
scene larapoolcum06 with dissolve
play sound "sounds/splooge03.mp3"
lc "For Queen's sake, try and aim your giant spurts better! You've pumping half of it all over my face!"
window hide
with fastflash
mc "AAAAH, sorry, can't control myself when I'm NU-UUU-TTTING!"
scene larapoolcum07 with dissolve
stop channel2
play sound "sounds/panting.mp3"
lc "Finally, your cum-cannon is done spewing its GIGANTIC load all over the place..."
scene larapoolcum08 with dissolve
play sound "sounds/lick02.mp3"
lc "Mmh, it's very tasty actually. I think I might... * slurp * stick around a bit longer..."
play sound "sounds/panting.mp3"
mc "Rhuuu...."
play sound "sounds/lick03.mp3"
lc "But you seem to be rather drained, so you'd better go back and get some rest, [name]...."
stop music
jump Main

label LaraEgypt:
stop music
play music "sounds/plane.mp3"
scene laraplane01 with fade
lc "You should rest. This is a long flight and a long march through the desert awaits us."
mc "Hey, I'm a SUPER-HERO and I don't need no stinkin' sleep!"
scene laraplane02 with fastdissolve
lc "Fine, suit yourself. But the desert is hot and you will regret not listening to me, young hero..."
$ period = 0
$ day += 1
stop music
play music "v041/egyptianmood.mp3"
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene laraegypt01 with fade
mc "Oh god, it's sssooo hot. Are we there yet?"
lc "Yes indeed, we have arrived. This must be the temple of Titi-Khok. Queen Cleopatra used it as a private beauty parlor where she would get pampered by her slaves."
scene laraegypt02 with dissolve
mc "Finally! It's like, super-hot in this desert."
lc "I did warn you, didn't I?"
scene laraegypt03 with dissolve
mc "Look, they even have an indoors swimming pool! Last one in is a chicken-shit superhero adventurer!"
lc "[hero], be careful! I didn't have time to give my speech and warn you about pitfalls and snares!"
scene laraegypt04 with dissolve
mc "That's just boring, I NEED to cool down anyway! Geronimo!"
play sound "sounds/diving.mp3"
lc "Oh dear, I should check the time. It might be happening soon."
scene laraegypt05 with dissolve
mc "What's happening? The water is clear and I don't see no sperm-tacle around me, it's safe, I'm telling you!"
lc "I am referring to the apparition of the ghost of Queen Cleopatra."
mc "Ghosts? Come on! They, like, barely exist at all."
lc "Cleopatra was killed right inside this temple by her husband Mark-Anthony. Nobody knows why he got so enraged..."
scene laraegypt06 with dissolve
lc "And it is time for the Queen to appear and seek her vengeance according to my notes, you'd better get out of the water NOW, [name]!"
mc "Pff, I ain't scared of nobo.."
play channel1 "sounds/jacuzzi.mp3"
scene laraegypt07 with dissolve
mc "What's going on, the water is... boiling behind me!"
lc "I told you, when will you listen, it's HER!"
mc "Damn, just when I was cooling down a bit..."
scene laraegypt08 with dissolve
play sound "sounds/healing.mp3"
mc "What the hell is this thing coming out of the water???"
lc "That's her crown. And the Jewel of the Mind Slaves is right there, I see it!"
mc "Ok, I'll try and grab it then and we can get the hell out of..."
stop music
play music "v041/egyptian.mp3"
scene laraegypt09 with dissolve
mc "She's rising from the water! And what a pair of titties!"
scene laraegypt10:
    subpixel True
    ypos -1.0
    ease 8.0 ypos 0.0
with dissolve
$ renpy.pause(6.0, hard='True')
mc "And what a spectacular nose! I am in awe of her pharaonic beauty!"
scene laraegypt11 with dissolve
stop channel1
qc "Who are you? And how dare you be in my regal presence?"
lc "We are advent..."
scene laraegypt12 with dissolve
qc "Is that you, my beloved slave, Mamm-Hoth-Khok?"
lc "She doesn't seem to be hearing me....Maybe she can hear you, Mamm-Hoth-Khok was her favorite male slave, so just say yes [name]!"
scene laraegypt13 with dissolve
mc "Sure, it's me, my Queen. Mammoth...err...Cock."
qc "You have come to please your Queen again? Oh, how long I have waited for this glorious day!"
scene laraegypt14 with dissolve
mc "Yeah, same here. Like 2000 years I think."
lc "Get her to take her crown off if you can!"
scene laraegypt15 with dissolve
lc "There's an upright Egyptian coffin. I wonder who could have been buried here..."
scene laraegypt16 with dissolve
qc "Show your Queen what she's been longing for all these millenia..."
mc "Alright! Here we go, I'm getting hard as a PYRAMID for you, my Queen!"
scene laraegypt17 with dissolve
stop music
play music "sounds/sexy14.mp3"
qc "Mmh, your divine rod is even BIGGER than I remember! And so are your young muscles, my beloved slave..."
mc "Err, yeah, I've been training for the last centuries and practising jelqing on a regular basis. Why don't you take that cumbersome crown off so we can get to the SWEE-EE-ET queen-slave love."
scene laraegypt18 with dissolve
qc "You know how to talk to your Queen, Mamm-Hoth-Khok. I hope you remained FAITHFUL to her during these long millenia."
mc "Oh yeah, like, totally."
scene laraegypt19 with dissolve
qc "Your Queen is ready, come and RAVISH her body, like you used to..."
scene laraegypt20 with dissolve
play sound "sounds/slurp.mp3"
qc "Drink my royal milk, it will make you even STRONGER."
scene laraegypt21 with dissolve
play sound "sounds/moan02.mp3"
qc "Oooh, you are such an adorable slave for your Queen!"
scene laraegypt22 with dissolve
play sound "sounds/moan03.mp3"
qc "You know how to play with my pussy, you haven't lost your sensual touch! AAAAH!"
scene laraegypt23:
    subpixel True
    xpos -0.1
    linear 3.0 xpos 0.0
with dissolve
play sound "sounds/moan01.mp3"
pause
mc "I also know how to play with those heavy funbags, my Queen..."
qc "Oooh! Carry over to the edge of the pool and FUCK ME, Mamm-Hoth-Khok!"
scene laraegypt24 with dissolve
play sound "sounds/wow.mp3"
qc "By the beak of Horus, your love muscle is so HUGE!"
mc "All the better to please you, my Queen!"
scene laraegypt25 with dissolve
play sound "sounds/doorsqueak.mp3"
lc "Blimey, that coffin just opened by itself and there's a mummy inside it. I don't like that."
scene laraegypt26 with dissolve
play sound "sounds/hulkgrowl.mp3"
lc "It be must Mamm-Hoth-Khok, judging by the size of this mummy's bulge! And he's NOT happy!"
scene laraegypt27 with dissolve
play sound "sounds/punch.mp3"
lc "Get that jewel as soon as you have the opportunity, [hero], I'll try and fend him off for as long as I can!"
scene laraegypt28 with dissolve
qc "Just fuck me, I can't wait any longer, STICK THAT MIGHTY SLAVE PILLAR INSIDE YOUR QUEEN NOW!"
mc "Err... Right now, I'm kind of busy, she's demanding some HOT SEX, and she wants it RIGHT NOW!"
scene laraegypt29 with dissolve
play sound "sounds/moan02.mp3"
qc "You're DROOLING lots of precum all over your Queen's tummy, this is just so NASTY!"
mc "You ain't see nothing yet my Queen, Mamm-Hoth-Khok is going to take you to the Other World!"

label CleoPoolFuckSlow:
$ cleopoolfuckfast = False
window hide
show cleopoolslowvideo behind cleopoolfastvideo
show cleopoolslowvideo behind cleopoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide cleopoolfastvideo
hide cleopoolpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckslow == False:
    $ cleopoolfuckslow = True
    qc "Mamm-Hoth-Khok... Your dong is divinely HUGE!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleopoolfuckslow()
screen cleopoolfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckPOVSlow")

label CleoPoolFuckFast:
$ cleopoolfuckslow = False
window hide
show cleopoolfastvideo behind cleopoolslowvideo
show cleopoolfastvideo behind cleopoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide cleopoolpovfastvideo
hide cleopoolslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckfast == False:
    $ cleopoolfuckfast = True    
    qc "Give it to me hard and good, my beloved slave, your Queen demands it!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleopoolfuckfast()
screen cleopoolfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckPOVFast")

label CleoPoolFuckPOVSlow:
$ cleopoolfuckfast = False
window hide
show cleopoolpovslowvideo behind cleopoolslowvideo
show cleopoolpovslowvideo behind cleopoolpovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide cleopoolpovfastvideo
hide cleopoolslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleopoolfuckslow == False:
    $ cleopoolfuckslow = True
    qc "Mamm-Hoth-Khok... Your dong is divinely HUGE!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleopoolpovfuckslow()
screen cleopoolpovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckSlow")

label CleoPoolFuckPOVFast:
$ cleopoolfuckslow = False
window hide
show cleopoolpovfastvideo behind cleopoolfastvideo
show cleopoolpovfastvideo behind cleopoolpovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide cleopoolfastvideo
hide cleopoolpovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if cleopoolfuckfast == False:
    $ cleopoolfuckfast = True    
    qc "Give it to me hard and good, my beloved slave, your Queen demands it!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleopoolpovfuckfast()
screen cleopoolpovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoPoolFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoPoolFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoPoolFuckFast")

label CleoPoolFuckEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
qc "Don't stop thrusting, I've been waiting for this too long!"
scene laraegypt30 with dissolve
stop channel1
lc "Get the jewel now! This mummy is much tougher than I thought and he seems real HORNY too!"
scene laraegypt31 with dissolve
mc "I... can't reach..."
scene laraegypt32 with dissolve
qc "What can't you reach, my beloved? Your Queen will make you reach a mighty orgasm, do not worry!"
scene laraegypt33 with dissolve
mc "Alright, let's switch position then, I'm gonna give it to you HARD and DEEP with your legs spread WIDE OPEN, so get ready for the pounding of the MILLENIUM, Queen Cleopatra!"
qc "Mmh, I can't wait to feel your immense pole RAVISH my horny pussy!"

label CleoSideFuckSlow:
$ cleosidefuckfast = False
window hide
show cleosideslowvideo behind cleosidefastvideo
show cleosideslowvideo behind cleosidepovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex06.mp3"
hide cleosidefastvideo
hide cleosidepovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckslow == False:
    $ cleosidefuckslow = True
    qc "Yes, fuck like an Egyptian!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleosidefuckslow()
screen cleosidefuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckPOVSlow")

label CleoSideFuckFast:
$ cleosidefuckslow = False
window hide
show cleosidefastvideo behind cleosideslowvideo
show cleosidefastvideo behind cleosidepovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide cleosidepovfastvideo
hide cleosideslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckfast == False:
    $ cleosidefuckfast = True    
    qc "You are more godly than Osiris the way you fuck me so DEEP!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show pov:
     xpos 50 ypos 500    
call screen cleosidefuckfast()
screen cleosidefuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckPOVFast")

label CleoSideFuckPOVSlow:
$ cleosidefuckfast = False
window hide
show cleosidepovslowvideo behind cleosideslowvideo
show cleosidepovslowvideo behind cleosidepovfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex06.mp3"
hide cleosidepovfastvideo
hide cleosideslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
with dissolve
if cleosidefuckslow == False:
    $ cleosidefuckslow = True
    qc "Yes, fuck like an Egyptian!"
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleosidepovfuckslow()
screen cleosidepovfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckPOVFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckSlow")

label CleoSideFuckPOVFast:
$ cleosidefuckslow = False
window hide
show cleosidepovfastvideo behind cleosidefastvideo
show cleosidepovfastvideo behind cleosidepovslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex04.mp3"
hide cleosidefastvideo
hide cleosidepovslowvideo
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
if cleosidefuckfast == False:
    $ cleosidefuckfast = True    
    qc "You are more godly than Osiris the way you fuck me so DEEP!"
window hide
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen cleosidepovfuckfast()
screen cleosidepovfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("CleoSideFuckPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("CleoSideFuckEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("CleoSideFuckFast")

label CleoSideFuckEnd:
hide nexticon
hide sceneicon
hide faster
hide slower
hide pov
mc "Get ready for my mighty load, my Queen!"
qc "Pump me FULL of your seed, I don't care if Mark-Anthony finds out, I just want your BABY!"
scene laraegyptcum01 with dissolve
stop channel1
play channel1 "v031/boyorgasm02.mp3"
mc "Then here it CUMS, RHAAA!"
window hide
with fastflash
qc "By the scepter of Osiris, I can feel your seed BLASTING inside me!"
scene laraegyptcum02 with dissolve
mc "Wait, there's MORE for you, AAAH!"
window hide
with fastflash
qc "With such a load, I will surely get pregnant and finally have a worthy heir to my Egyptian throne!"
scene laraegyptcum03 with dissolve
qc "Just keep filling me up, make sure you KNOCK ME UP GOOD!"
mc "Damn right, I'm got tons more in store, don't you worry about that!"
scene laraegyptcum04 with dissolve
mc "Like So, RHAAA!"
window hide
with fastflash
play sound "sounds/womancum01.mp3"
qc "AAAH, your giant spunk shots are making me cumming too!"
scene laraegyptcum05 with dissolve
mc "* I just need to keep pumping and keep her distracted, AAAH! *"
window hide
with vpunch
qc "You're filling me up with so much yummy slave spunk, my royal belly looks pregnant already!"
stop channel1
scene laraegypt36 with dissolve
play sound "sounds/hulkgrowl.mp3"
lc "Just get that jewel, this mummy is getting too close for comfort!"
scene laraegypt37 with dissolve
mc "I definitely don't want to see any NTR mummy shit, so I'm gonna grab it right now. Hang on, there are several jewels on this crown, which one is it?"
call screen usepower("usesenses", "CleoNoSenses", "CleoSenses") with dissolve
label CleoNoSenses:
mc "Damn it, I just can't remember anything... Hopefully, the player remembers or I'm SCREWED."
jump JewelChoice
label CleoSenses:
if mcsenses <= 1:
    mc "I still can't remember anything despite my Super-Senses, they aren't high enough...Hopefully, the player remembers or I'm SCREWED."
    jump JewelChoice
play sound "sounds/dream.mp3"
scene laraegyptrecall with dissolve
lc "... This sparkling green jewel would be immensely dangerous if it fell into..."
$ usedsenses += 1
mc "Ah yeah, I remember, it's the GREEN one!"

label JewelChoice:
scene laraegypt31 with dissolve
menu:
    "Pick the Green jewel":
        if mcmind == 0:
            scene laraegypt41 with dissolve
            play sound "sounds/healing.mp3"
            mc "I feel something..."
            call ControlPlus
            scene laraegypt38 with dissolve
            mc "Fuck yeah, I've acquired a NEW Superpower! And I have the jewel now, Lara!"
            jump CleoNext
        if mcmind >= 1:
            mc "I have the jewel now, Lara!"
            jump CleoNext
    "Pick the Blue Jewel":
        scene laraegypt38 with dissolve
        mc "I have the jewel now, Lara!"
        jump CleoNextWrong

label CleoNextWrong:
scene laraegypt50 with dissolve
qc "Who is this \"Lara\" that you speak of? Have you been unfaithful to your Queen?"
mc "Err... Nobody, I swear!"
scene laraegypt53 with dissolve
qc "I curse you, impostor!"
mc "No, please what did I do?"
lc "You picked the WRONG jewel!"
scene laraegypt54 with dissolve
play sound "sounds/healing.mp3"
"You have been cursed by Queen Cleopatra and turned into her zombie sex slave."
window hide
show gameovericon:
    xpos 600 ypos 400
pause
return

label CleoNext:
scene laraegypt50 with dissolve
qc "Who is this \"Lara\" that you speak of? Have you been unfaithful to your Queen?"
scene laraegypt51 with dissolve
stop music
play music "v041/egyptianmood.mp3"
lc "Let's get out of here NOW!"
mc "I think it's a good idea, she just saw the mummy and she's coming to her senses it seems..."
scene laraegypt52 with dissolve
lc "Run, [name], run!"
mc "But I forgot my thong and I'm all naked!"
lc "We'll get you a new one back at the compound! Run faster!"
$ day += 1
$ period = 0
$ quest06end = True
scene laraplace with fade
show lara01
show screen calendar
show screen statscreenicon
show screen questscreenicon
lc "That was a close call but we did it!"
mc "Well, I'd like to remind you that I did MOST of the job. Or at least my cock did."
hide lara01
show lara02
with fastdissolve
lc "And who took you there, and who fought the horny mummy of Mamm-Hoth-Khok for you while you were banging that slutty Queen?"
mc "Yeah, sure, you did your bit, but I still deserve that Jewel MORE than you!"
hide lara02
show lara04
with fastdissolve
lc "This is OUT OF THE QUESTION! You cannot be trusted with it. I will store it in my high-security artefacts room. You can leave now, [hero]."
menu:
    "Be resentful of her condescending attitude (+1 Super-Villain)":
        call Evil
        mc "* I'll get my hands on that jewel one day, I swear, I'll get it... *"
    "Acquiesce and agree. (+1 Super-Hero)":
        call Good
        mc "* I guess she's right, it's her job, not mine to keep these things *"
jump Main

label LaraWidowPoolMission05:
stop music
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/waterrun.mp3"
scene larawidowpool01 with dissolve
lc "I'm so glad you came. I heard you were... rather busy lately."
bw "Yeah, I am. But I thought it would be a nice change from my NEW routine."
scene larawidowpool02 with dissolve
lc "So, what new routine is that? Would you like to talk about it?"
bw "I'm fighting Western DECADENCE. Greed is the root of all evil. Speaking of which, your GOLDEN swimsuit is... rather tasteless."
scene larawidowpool03 with dissolve
lc "Ah, err... I can take it off if you want. I wanted to get a new one. A more modest one anyway."
scene larawidowpool04:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
bw "That's better... I see you are ready to abandon your depraved ways."
stop music
play music "sounds/sexy03.mp3"
scene larawidowpool05 with dissolve
bw "Now there's ONE thing that needs sharing more than money..."
lc "And what is that?"
scene larawidowpool06 with dissolve
bw "LOVE..."
lc "Oooh... I ssooo agree..."
scene larawidowpool07 with dissolve
play sound "sounds/slurp.mp3"
lc "Mmmh..."
scene larawidowpool08 with dissolve
play sound "sounds/lick02.mp3"
lc "Aaah... You know my weak spots, Natasha..."
scene larawidowpool09 with dissolve
play sound "sounds/kiss.mp3"
bw "And you know mine..."
scene larawidowpool10 with dissolve
mc "Mmmh, I wonder whether now is a good time? My Super-Libido tells me to wait a bit longer for this lesbian show to escalate..."
lc "Now it's my turn to return the favor. I'm gonna hold you up in the water so you can play with your pussy in zero gravity..."
scene larawidowpool11a with dissolve
bw "Oh yeah, I like that..."
play channel1 "sounds/wank.mp3"
window hide
show widowlarapoolwank with fastdissolve
pause
bw "Gonna..."
scene larawidowpool12 with dissolve
stop channel1
play sound "sounds/moan05.mp3"
bw "... CUM, AAAHH!"
scene larawidowpool13 with dissolve
play sound "sounds/kiss.mp3"
bw "That was wonderful... Now your pussy needs some tender loving too... From my fingers!"
scene larawidowprewank01 with dissolve
lc "Ooooh..."
play channel1 "sounds/wetmassage.mp3"
window hide

label LaraPoolWankSlow: 
hide nexticon
hide faster
hide slower
show larawidowpoolwankslowvideo behind larawidowpoolwankfastvideo
pause 1.0
hide larawidowpoolwankfastvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500     

call screen larawidowpoolwankslow()
screen larawidowpoolwankslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolWankEnd")

label LaraPoolWankFast:
show larawidowpoolwankfastvideo behind larawidowpoolwankslowvideo
hide nexticon
hide faster
hide slower
hide larawidowpoolwankslowvideo with dissolve
show nexticon:
    xpos 1750 ypos 1020    
show slower:
     xpos 50 ypos 500     

call screen larawidowpoolwankfast()
screen larawidowpoolwankfast():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("LaraPoolWankSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("LaraPoolWankEnd")

label LaraPoolWankEnd:
hide nexticon
hide slower
hide faster
lc "Just like that, just like that...You're going to make me..."
scene larawidowpostwank01 with dissolve
stop channel1
play sound "sounds/moan06.ogg"
lc "...SQUIRT! AAAH!"
scene larawidowpool14 with dissolve
bw "Now I NEED to taste those yummy juices of yours..."
scene larawidowpool15 with dissolve
play channel1 "sounds/moan02.mp3"
lc "Oh God... Your tongue..."
play sound "sounds/lick02.mp3"
bw " * lick *"
scene larawidowpool16 with dissolve
lc "Yes, just keep going Natasha... "
mc "* Why is she holding her hand like that? *"
scene larawidowpool17 with dissolve
mc "* Oh, I got it. NOW is the time! Here's the gem, Lara! *"
scene larawidowpool18 with dissolve
play sound "sounds/magic.mp3"
lc "Patra-Khok-..."
scene larawidowpool19 with dissolve
lc "...Mindh-Khon-Troll!"
scene larawidowpool20 with dissolve
lc "Let go of your mind, Natasha! Remove the lock and escape from the grip of your enslaver! You are not working for the Soviets!"
scene larawidowpool21 with dissolve
play sound "sounds/magic.mp3"
lc "I FREE YOU, by the Power of the Queen Jewel!"
scene larawidowpool22 with dissolve
mc "Did it work?"
lc "Of course it did. I said the correct incantation which were left in a notebook by my late explorer father!"
mc "So she's no longer a radical leftist lunatic then? She's a normal decadent American capitalist right?"
lc "She needs to recover from the exhaustion. Let me take her back to her room and make sure she sleeps well."
mc "Right, I'll come with y..."
lc "WITHOUT YOU! You mission is OVER."
window hide
play sound "sounds/winning.mp3"
show missionicon05 at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
$ mission05win = True
$ mission05end = True
mc "Gee, alright, I was just trying to help."
$ locembassy = True
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main