label WWRoomDay:
stop music
if d10locday >= 7 and wonderbirth: 
    scene wonderroomday with fade
    mc "Wonder Woman is not around. And there's nothing to do in this room at this stage without her in it..."
    jump MainTime
if d10locday <= 3 and wonderbirth: 
    scene wonderroomday
    show wonderbaby01 at centerleft
    with fade
    jump WonderLevel02NewDialogues
if d10locday >= 4 and d10locday <= 6 and wonderbirth:
    jump WonderBirthAuditDialogues
stop music
scene wonderroomday with fade
mc "Wonder Woman is not around. She must be fighting nazis somewhere. And there's nothing to do in this room at this stage without her in it..."
jump MainTime

label WWRoomNight:
stop music
if d10locnight >= 3 and d10locnight <= 7: 
    scene wonderroomnight01 with fade
    mc "Wonder Woman is not around. She must be fighting nazis somewhere. And there's nothing to do in this room at this stage without her in it..."
    jump MainTime
    
if d10locnight == 1 or d10locnight == 2 or d10locnight == 9 or d10locnight == 10: 
    pass
if mclevel02 and wonderbirth == False and quest07end:
    jump WonderBirth
if mclevel02 and wonderbirth and quest07end and (wondertalkbaby01 == False or seennatalyawidow == False):
    scene wonderroomnight02
    show wonderbaby01 at centerleft
    with fade
    jump WonderLevel02NewDialogues
if mclevel02 and wonderbirth and quest07end and wondertalkbaby01 and seennatalyawidow and seenwonderworn == False:
    jump WonderRoomBigTits
if mclevel02 and wonderbirth and quest07end and wondertalkbaby01 and seennatalyawidow and seenwonderworn:
    jump WonderRoomFuck
if mclevel02:
    scene wonderroomnight02
    show wonderlingerie01 at centerleft
    with fade
    jump WonderLevel02Dialogues
    
play sound "sounds/wwomanmusic02.mp3"
scene wonderroomnight02 with fade
show wonder01 at centerleft with moveinleft
ww "Who comes hither?"
hide wonder01
show wondereyeblink at centerleft
with fastdissolve
stop sound
voice "wonder/room01"
ww "Ah, it's you, [hero]. What is the purpose of this nightly visit?"
menu:
    "I'm bored, I thought we could play a game together." if inventorytwister == False:
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        voice "wonder/room02"
        ww "Oh? I'm kinda bored too. Nazis have been quiet lately. Do you have a game to play? I hear people play board games to fight boredom in this era."
        mc "Oh, do they? I thought they played visual novel porn games."
        hide wonder03
        show wonder04 at centerleft
        with fastdissolve
        voice "wonder/room03"
        ww "Not in 1977. They play BOARD GAMES."
        mc "Ah, so that's the year we're in then. And I need to find a board game."
        window hide
        play sound "sounds/skill.mp3"
        $ questtwister = True
        show questwondertwister at poslocation
        $ renpy.pause(0.5, hard=True)
        show questwondertwistertext at posmissiontextb
        pause
        hide wonder04
        show wonder02 at centerleft
        with fastdissolve
        voice "wonder/room04"
        ww "I can't play with you if you don't have one."
        mc "I shall return one evening. With a board game."
        hide questwondertwistertext
        hide questwondertwister
        jump Main
    "I found a game we could play." if inventorytwister and playedtwister == False:
        $ playedtwister = True
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        voice "wonder/room05"
        ww "Oh? What game did you have in mind?"
        mc "A game called \"Twister\". It's a new game, just came out and it's all the rave."
        voice "wonder/room06"
        ww "You'll have to explain the rules to me then, I don't know anything about that game. Is it what you people call a \"board game\"?"
        mc "Kind of. There's a mat and dots on it. And it's played naked."
        hide wonder03
        show wonder04 at centerleft
        with fastdissolve
        voice "wonder/room07"
        ww "What, why naked?"
        mc "Well, it's a game that involves body agility and suppleness. Players have to be totally free of their movements."    
        voice "wonder/room08"
        ww "I'm surprised that such a game is popular, I find people in this place and era so prudish."
        mc "Not when they're playing \"Twister\". So are you in?"
        hide wonder04
        show wondereyeblink at centerleft
        with fastdissolve
        voice "wonder/room09"
        ww "And what is the reward for winning this game of yours?"
        hide winicon
        hide questwondertwister
        mc "Well, since it involves body parts, the winner gets to decide what the loser does on one of his body parts."
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        voice "wonder/room10"
        ww "Uhhm... OK, I'm bored so I'm in."
        jump WWTwister
    "Let's play a game of Twister again." if inventorytwister and playedtwister:
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        voice "wonder/room11"
        ww "Oh? You want to lose?"
        mc "No, I want to WIN!"
        hide wonder03
        show wonder01 at centerleft
        with fastdissolve
        voice "wonder/room12"
        ww "Uh oh, bring it on!"
        jump WWTwister
    "I was hoping we could, you know... breed?" if seenstroheimwonder == False:
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        ww "I'm pretty certain I told you I was NOT INTERESTED in getting impregnated by ANYONE."
        mc "Ah, but I'm not \"anyone\", I'm [hero]!"
        hide wonder03
        show wonder05 at centerleft
        with fastdissolve        
        ww "And I'm PRINCESS DIANA OF THEMYSCIRA."
        mc "Right, right, sorry to have bothered you. Your Highness. I shall leave."
        jump Main
    "That's a very nice room you have there.":
        hide wondereyeblink
        show wonder04 at centerleft
        with fastdissolve
        ww "Well, I AM a princess after all."
        mc "What are these pictures on the wall?"
        hide wonder04
        show wonder06 at centerleft
        with fastdissolve
        ww "Pictures of my lovely homeland. As it is NOW unfortunately."
        mc "You didn't bring pictures with you from Ancient Greece?"
        hide wonder06
        show wonder03 at centerleft
        with fastdissolve
        ww "Photography is an invention of THIS world! I only have memories. Of my beautiful island. *sighs* Please leave me alone while I reminisce..."
        mc "Ah, okay. Wrong dialogue choice then."
        jump Main
    "Do you always wear your costume?":
        hide wondereyeblink
        show wonder01 at centerleft
        with fastdissolve
        ww "Of course. Wonder Woman needs to be READY at ANY time. Nazis never tire and neither does she!"
        mc "It must be quite uncomfortable to sleep in an armor though..."
        hide wonder01
        show wonder03 at centerleft
        with fastdissolve
        ww "It's true that I would prefer something lighter. But I need it for protection. Day AND night. From Nazis."
        mc "I think you're just so damn obsessed with these nazis that you think they are everywhere, like a kid who thinks there's a monster under his bed..."
        hide wonder03
        show wonder06 at centerleft
        with fastdissolve
        ww "And that is why Wonder Woman's bed doesn't have ANY SPACE underneath it!"
        mc "*sigh* I give up."
        hide wonder06
        show wonder05 at centerleft
        with fastdissolve        
        ww "Wonder Woman WILL NEVER GIVE UP!"
        jump Main
    "You don't look very pregnant." if seenstroheimwonder:
        hide wondereyeblink
        show wonder03 at centerleft
        with fastdissolve
        ww "Nevertheless, I can feel that I am... Hopefully, not with NAZI babies. * sigh *"
        mc "Not a chance! With the mighty load I... err... delivered inside your...err..."
        hide wonder03
        show wonder05 at centerleft
        with fastdissolve        
        ww "Don't remind me! You have COMPROMISED the PURITY of my race! Get out of here!"
        jump Main
    "Sorry, wrong room.":
        hide wondereyeblink
        show wonder04 at centerleft
        with fastdissolve
        ww "You should be more careful in the future which door you pick. I ALMOST chopped you into pieces. Thinking you were a nazi."
        mc "Err, okay. Goodnight, Diana."
        hide wonder04
        show wonder05 at centerleft
        with fastdissolve        
        ww "PRINCESS Diana!"
        jump Main

label WWTwister:
scene twister01 with dissolve
mc "So first, you have to stand on a yellow and a blue dot, like so."
voice "wonder/twister01"
ww "That sounds easy enough."
scene twister02 with dissolve
mc "Name a color and a body part and I'll have to put that body part on a dot of the color you picked. And you can pick a body part to remove too if you wish."
voice "wonder/twister02"
ww "I see. What a strange game. Then I pick left arm and yellow. And lift your... left leg."
scene twister03 with dissolve
voice "wonder/twister03"
ww "Oh, you're approaching me?"
mc "I can't beat the shit out of you at this game without getting closer."
voice "wonder/twister04"
ww "Oh ho, then come as close as you like."
mc "My turn to pick. I want to see you on all fours. Arms on yellow and blue dots."
scene twister04 with dissolve
voice "wonder/twister05"
ww "You're not making it even slightly hard. Or fun. I'll rise you up both arms on yellow and blue. But also your right leg..."
mc "But... that would mean..."
voice "wonder/twister06"
ww "That you must stand on your hands. Do you have a problem with that?"
scene twister05 with dissolve
mc "Of course not! There you go. I can't see much though. I don't know what to pick..."
voice "wonder/twister07"
ww "Then you miss your turn. My go AGAIN! Both legs forward now!"
mc "What, hang on... I would have to..."
scene twister05b with dissolve
voice "wonder/twister08"
ww "Do a twisting somersault. The game is called twister right?"
scene twister05c with dissolve
play sound "sounds/panting.mp3"
mc "I can do it..."
if mcagility >= 1:
    call screen usepower("useagility", "TwisterLose", "TwisterWin") with dissolve

label TwisterLose:
scene twister05d with dissolve
mc "AAAh, my agility is not high enough!"
scene twister05e with dissolve
play sound "sounds/thud.mp3"
voice "wonder/twister09"
ww "Really? ZERO super-agility in action right there. You LOSE!"
mc "It's unfair, I got to skip my turn!"
scene twister05f with dissolve
voice "wonder/twister10"
ww "Tsss, don't be a sore loser, that's unbecoming of a superhero."
mc "Fine, I won't be. I admit you won... Now is your time to choose what you want me to do... To ANY part of your body..."
voice "wonder/twister11"
ww "Mmmh, let me think. I think I'll choose to SCISSOR your head between my STRONG thighs!"
mc "Err, and then what?"
voice "wonder/twister11b"
ww "You'll see..."
scene twister11 with dissolve
mc "Indeed I see... Please, don't squash my head too much with your powerful thighs, I can barely breathe!"
voice "wonder/twister12"
ww "Then open your mouth and stick your tongue out to let the fresh air in [hero]..."
scene twister12 with dissolve
voice "wonder/twister13"
ww "And use it to lick my pussy. And relieve me of the stress of the day."
mc "Alright Princess Diana, I'll try my best."
window hide
play channel2 "sounds/lick01.ogg"
show twisterwonderlick with dissolve
pause
voice "wonder/twister14"
ww "Yes, just like that... Just like th..."
scene twister15 with dissolve
stop channel2
play sound "sounds/splooge01.mp3"
voice "wonder/twister15"
ww "Aaah, I'm CUMMING!"
window hide
with fastflash
mc "I made you SQUIRT! Like a true SUPER-STUD! And I didn't even use my super-cock."
scene twister16 with dissolve
play sound "sounds/moan02.mp3"
voice "wonder/twister16"
ww "God! I'm emptying my pussyjuices all over your face!"
window hide
with fastflash
mc "You can say that again..."
stop sound
scene twister19 with dissolve
voice "wonder/twister17"
ww "Now I feel better and I'll sleep VERY WELL. Thank you, [name], you can go."
play sound "sounds/slurp.mp3"
mc " Sure, after I've licked my face clean... *lick*"
jump Main

label TwisterWin:
if usedtwisteragility == False:
    $ usedagility += 1
    $ usedtwisteragility = True    
scene twister06 with dissolve
play sound "sounds/thud.mp3"
mc "Perfect landing! Now you get to have to reach out for a green dot with your right arm."
scene twister07 with dissolve
voice "wonder/twister18"
ww "Your leg.... It's in the way."
mc "Nothing I can do about that, Princess Diana. You'll just have to lean closer."
scene twister08 with dissolve
voice "wonder/twister19"
ww "It's... too far. I'll try from above."
mc "Let me help you out a bit then..."
scene twister09 with dissolve
voice "wonder/twister20"
ww "What is this? Your phallus is moving!"
scene twister10 with dissolve
voice "wonder/twister21a"
ww "You're blocking my head movement with that thing! How can a man's phallus be THAT BIG???"
mc "I'm entitled to use ANY part of my body to hinder your movements. Do you give up Wonder Woman?"
scene twister20 with dissolve
voice "wonder/twister22"
ww "I... Yes, I give up. You win. This time."
mc "And now you're WONDERING what I have in mind for you, aren't you?"
scene twister21 with dissolve
voice "wonder/twister23"
ww "I'm warning you, you are not TAKING MY VIRGINITY!"
mc "Fine, if you insist, Princess... But I am taking some jug-milk for you then! Come and SIT on my hard prong and feed me those hard milky nipples..."
scene twister22 with dissolve
voice "wonder/twister24"
ww "You're lucky they produce a WONDERFUL quality milk..."
mc "Oooh, I can't wait to taste it!"
scene twister17 with dissolve
play sound "sounds/lick03.mp3"
voice "wonder/twister25"
ww "You were thirsty, weren't you, naughty boy?"
scene twister18 with dissolve
stop sound
mc "Now rub your super-rump on my hard shaft, Wonder Woman..."
voice "wonder/twister26"
ww "That was not really part of the deal. But if that can make you leave my bedroom fully satisfied, then so be it."
window hide

play channel1 "sounds/wank.mp3"
show twistergrindvideo with dissolve
$ renpy.pause(2.0, hard='True')
voice "wonder/twister27"
ww "Like that? Is that what you wanted?"
mc "Y..yeah, that's great... Grind that ass..."
window hide
$ renpy.pause(2.0, hard='True')
pause
mc "Keep going, you're going to make me cum Diana!"
voice "wonder/twister28"
ww "PRINCESS Diana to you!"
window hide
$ renpy.pause(2.0, hard='True')
stop channel1
scene twistergrindcum01 with dissolve
hide twistergrindvideo
play channel2 "sounds/splooge02.mp3"
mc "Oh fuck, I'm blowing SUPER BIG-TIME!"
window hide
with fastflash
voice "wonder/twister29"
ww "Keep your giant boyload on the mat please!"
window hide
with fastflash
mc "I can't... control myself, RHAAA!"
scene twistergrindcum02 with dissolve
mc "Still CUMMING, AAAH!"
window hide
with fastflash
voice "wonder/twister30"
ww "You're just a FILTHY BOY! Cumming ALL OVER THE PLACE like that!"
window hide
with fastflash
mc "I just NEEDED that release, RHAAA!"
stop channel2
scene twistergrindcum03 with dissolve
play sound "sounds/panting.mp3"
voice "wonder/twister31"
ww "Finally... You made such a BIG mess. Fortunately, most of your spunk landed on the twister mat."
mc "That was... sssoo good."
scene twistergrindcum04 with dissolve
voice "wonder/twister32"
ww "I did what you asked of me. And what you asked was VERY NAUGHTY. So time to leave MY bedroom, [name]... And take that cum-soaked mat with you."
mc "Rhuuu... Okay... Your highness..."
jump Main

label WonderLevel02Dialogues:
show wonderlingerie01 at centerleft:
    breathe
ww "Ah, It's you, [name]. I was getting ready to go to bed."
menu:
    "And you're wearing some SEXY lingerie to bed. That means you want ME to joi..." if wondertalkbaby == False:
        $ wondertalkbaby = True
        hide wonderlingerie01
        show wonderlingerie03 at centerleft
        with fastdissolve
        if evilness >= 13:
            ww "Wonder Woman KNOWS you are on the Villain Route. And therefore you are NOT invited to join her in her bed."
            mc "I'm just... trying to INFILTRATE Super-Villains so I can better DEFEAT them."
            hide wonderlingerie03
            show wonderlingerie05 at centerleft
            with fastdissolve
            ww "Umpf... That is plausible but coming from YOU, it doesn't sound very CONVINCING."
            mc "Then please let me convince you..."
            hide wonderlingerie05
            show wonderlingerie04 at centerleft
            with fastdissolve
            ww "Fine, I will grant you an audience. Stay at the edge of the bed though."
        if evilness <= 12:
            ww "You may be a SUPERHERO. With a... big cock. A VERY BIG COCK. But Wonder Woman is not an EASY woman."
            mc "An even BIGGER COCK now that I've reached Superhero Level 02 I might add..."
            hide wonderlingerie03
            show wonderlingerie05 at centerleft
            with fastdissolve
            ww "Well... Perhaps you may join me for a short while. We can talk about how you will use your superpowers for the GOOD of mankind."
            mc "Alright! Yeah, for the GOOO-OOOO-OOOD of womankind especially, if you get my drift..."
            hide wonderlingerie05
            show wonderlingerie04 at centerleft
            with fastdissolve
            ww "Stop being so puerile and follow me. Stay at the edge of the bed though."
        jump WWomanBed            
    "You still don't look very pregnant. While I've grown even BIGGER." if wondertalkpregnant == False:
        $ wondertalkpregnant = True
        hide wonderlingerie01
        show wonderlingerie02 at centerleft
        with fastdissolve
        ww "And yet, Wonder Woman feels that something is... different."
        mc "AH! So you ARE pregnant. We are BOUND by the spirit of sperm and err..."
        hide wonderlingerie02
        show wonderlingerie04 at centerleft
        with fastdissolve        
        ww "The future of MY child is with me and me ALONE."
        mc "Hang on there, this is the 20th century, not the 21st, and men get to decide stuff around here!"
        hide wonderlingerie04
        show wonderlingerie05 at centerleft
        with fastdissolve
        ww "This is why Wonder Woman needs to go back to her time. When women ruled the world. As it should be."
        hide wonderlingerie05
        show wonderlingerie03 at centerleft
        with fastdissolve
        ww "Will you help me?"
        menu:
            "Of course I will, Princess Diana of Themyscara. (+1 Super-Hero)":
                call Good from _call_Good_8
                hide wonderlingerie03
                show wonderlingerie04 at centerleft
                with fastdissolve                
                ww "You even remembered my name. How sweet of you. We will meet again, for sure."
            "I don't see why I should. Not my problem. Just like our child! (+1 Super-Villain)":
                call Evil from _call_Evil_9
                hide wonderlingerie03
                show wonderlingerie04 at centerleft
                with fastdissolve                
                ww "I should have expected that from a mere male mortal. Then Wonder Woman will find a way. ALONE! Be gone!"
        jump Main
    "I have no more future-daddy business here.":
        hide wonderlingerie01
        show wonderlingerie04 at centerleft
        with fastdissolve   
        ww "You should be more careful in the future which door you pick. I ALMOST chopped you into pieces. Thinking you were a nazi."
        mc "Err, okay. Goodnight, Diana."
        hide wonderlingerie04
        show wonderlingerie03 at centerleft
        with fastdissolve   
        ww "PRINCESS Diana!"
        jump Main

label WWomanBed:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy14.mp3"
scene wonderbedlingerie01 with fade
ww "So, what do you have to say to Wonder woman?"
mc "I will always protect you, Princess Diana. Mark my superhero words!"
scene wonderbedlingerie02 with dissolve
ww "That's all very well, but Wonder Woman can handle herself. I'm talking about how you will fight evil and help me go back to my time."
if evilness <= 12:
    mc "It appears Colonel Stroheim has developed some kind of portal. I will get more information about it by interrogating the hot SS prisoners."
if evilness >= 13:
    mc "I don't think it will happen. Time travel is technically impossible. You'd better resign yourself, you ain't never going back!"
scene wonderbedlingerie03 with dissolve
if evilness <= 12:
    ww "You think that portal could be a time portal?"
if evilness >= 13:
    ww "But what about that portal in Colonel Stroheim's compound?"
    mc "It was just some kind of space portal, not a time portal clearly. Otherwise, he would have used it to go back to warn Hitler."
scene wonderbedlingerie04 with dissolve
if evilness <= 12:
    ww "I will entrust you with getting the right information to save me... And our child... Sit down next to me, [name]..."
if evilness >= 13:
    mc "It was just some kind of space portal, not a time portal clearly. Otherwise, he would have used it to go back to warn Hitler."
    ww "That is what Wonder Woman wanted to hear. Sit down next to me, [name], I need some reassurnace in these dire times."
scene wonderbedlingerie05 with dissolve
if evilness <= 12:
    ww "I'm scared. I've never been pregnant before... What if the child has a defect? It would be the end of my people."
if evilness >= 13:
    ww "Then how am I going to go back to my time? I don't want to raise a child in this world... What if the child has a defect? It would be the end of my people."
mc "Don't you worry, my genes are like crazy super-genes."
scene wonderbedlingerie06 with dissolve
mc "Let me check how well he's doing."
ww "Or SHE's doing."
scene wonderbedlingerie07 with dissolve
mc "I can feel him kicking already. Or maybe it's his giant cock banging against your womb."
ww "That is... a weird thing to say. I don't even know if it's a boy or a girl."
scene wonderbedlingerie08 with dissolve
mc "Well, I mean if he has my genes, and well, your genes too I guess, imagine how STRONG and WONDERFUL he'll be!"
ww "I certainly hope he will be a BIG STRONG boy. We need such boys on my island to continue our lineage of Amazon women..."
mc "Ah, so there you go, I probably already saved your lineage as it is."
ww "* sigh * We'll see about that, young [hero]. Your audience has ended."
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main 

label WonderBirth:
play music "sounds/relax.mp3"
scene wonderroombirth01 with fade
show auditnurse01 at centerleft with moveinleft
ag "Thanks God you're here, [name]!"
mc "Why, what's happening?"
hide auditnurse01
show auditnurse02 at centerleft
with fastdissolve
ag "Wonder Woman is about to give BIRTH to her baby! I might need your assistance."
mc "Err, I'm not really qualif..."
hide auditnurse02
show auditnurse03 at centerleft
with fastdissolve
ag "Just come and do what I tell you, she's going into labor RIGHT NOW!"
scene wonderroombirth02 with dissolve
mc "How is it possible that she got pregnant so rapidly? She wasn't THAT pregnant when we came back from Berlin, 1945."
ag "Time-travelling must have dramatically accelerated her pregnancy."
mc "Even by the very low logic standards of time-travel stories, this makes absolutely no sense."
scene wonderroombirth03 with dissolve
ww "I'm about to GIVE BIRTH so SHUT THE HADES UP!"
ag "Don't stress her out, keep checking her pulse and let me know if it becomes irregular..."
mc "Err... Alright."
scene wonderroombirth04 with dissolve
ag "I'm going to gently remove your underwear, Princess Diana of Themyscira."
mc "* Damn, she seems to have BIGGER TITS too! *"
scene wonderroombirth05 with dissolve
ww "AAAH! My water just broke! It's coming!"
ag "Get her to hold still, [name]!"
scene wonderroombirth06 with dissolve
play sound "sounds/moan04.ogg"
ww "I'm in so much PAIN!"
mc "Come on now, calm down, bigger things have gone through that ho..."
ww "SHUT THE HADES UP!"
scene wonderroombirth07 with dissolve
play sound "sounds/femalegrunt01.mp3"
ag "I can see its head! PUSH, PUSH HARDER!"
play sound "sounds/moan06.ogg"
ww "AAAAAAAAAAAAHHHHHHHH!"
play sound "v041/plop.mp3"
scene wonderroombirth08 with dissolve
play sound "v051/babycrying.mp3"
ag "Look at this perfectly healthy wonderful baby!"
mc "Does he have a little Hitler moustache?"
ag "It's a girl."
mc "Okay. Does SHE have a little Hitler moustache then?"
scene wonderroombirth09 with dissolve
ag "NO SHE DOESN'T! She's just a BEAUTIFUL, little baby girl. Here, Princess Diana of Themyscira..."
ww "My daughter!"
mc "Mine too apparently, since she doesn't have a little Hitler moustache, thanks God."
scene wonderroombirth10 with dissolve
ww "You will become a fine Amazon Warrior. I shall name you \"Alpha-Girl\", Princess of Cockham, in honor of your birthplace!"
mc "The \"Alpha\" bit is of course in honor of her father, I like that."
scene wonderroombirth11 with dissolve
ww "No! It's because it's the first letter in the Greek alphabet!"
mc "So if you have a boy next, you'll call him \"Beta-Boy\"?"
ww "Maybe not. Ok, I admit it, it is in your honor... Do you want to meet your daughter, [name]?"
scene wonderroombirth12 with dissolve
play sound "v051/babytalk.mp3"
mc "Well, hello there, oochie-coochie-coo! Who's your daddy, hey? Who's your daddy?"
scene wonderroombirth13 with fastdissolve
play sound "sounds/punch.mp3"
mc "Hey!"
ag "She's got a nice punch already!"
scene wonderroombirth14 with dissolve
mc "Okay, she'll definitely make a fine Amazon warrior. Not sure about becoming a good wife though..."
ww "Amazon princesses don't have husbands. They are bred by a harem of stud slaves we keep locked up underground."
mc "Right. Remind me never to travel back in time to Ancient Greece then..."
ag "Wonder Woman and her baby need to rest. And you probably need to put some ice on that black eye..."
mc "Right..."
$ wonderbirth = True
jump Main

label WonderLevel02NewDialogues:
ww "Aren't you hungry, my sweet little angel!"
hide wonderbaby01
show wonderbaby02 at centerleft
with fastdissolve
ww "Oh look, it's daddy. And what does daddy want?"
label WonderLevel02NewDialogues02:
menu:
    "How is she doing? Growing BIG and STRONG, like her father?" if wondertalkbaby01 == False:
        $ wondertalkbaby01 = True
        hide wonderbaby02
        show wonderbaby03 at centerleft:
            zoom 0.5
        with fastdissolve
        play sound "v051/babycrying.mp3"
        ww "Shush! Don't raise your voice, you're making her cry!"
        mc "Ah, sorry..."
        hide wonderbaby03
        show wonderbaby01 at centerleft
        with fastdissolve
        stop sound
        ww "There, there, have some milk, the loud nasty man is gone..."
        window hide
        hide wonderbaby01
        show wonderbaby02 at centerleft
        with fastdissolve        
        jump WonderLevel02NewDialogues02            
    "That looks tasty. And I'm hungry." if wondertalkbaby01:
        hide wonderbaby02
        show wonderbaby03 at centerleft:
            zoom 0.5
        with fastdissolve
        ww "Don't be silly. It's for babies. Not for grown boys like you."
        mc "* Damn it! Let me zoom in on that tit while I can... *"
        show wonderbaby03 at centerleft:
            subpixel True
            linear 2.0 zoom 1 yanchor 0.4
        with fastdissolve
        ww "What are you doing, [name]?"
        mc "Nothing, nothing."
        hide wonderbaby03
        show wonderbaby02 at centerleft
        with dissolve
        jump WonderLevel02NewDialogues02
    "What are you going to do now that we got rid of your nazi enemies?":
        hide wonderbaby02
        show wonderbaby01 at centerleft
        with fastdissolve   
        ww "I need to go back home. With Alpha-Girl. And raise her to be a Amazon Princess, as is her destiny."
        mc "And how do you plan to do that? We left that SS nurse back in Berlin and she was the only one who knew how to program that portal."
        hide wonderbaby01
        show wonderbaby03 at centerleft:
            zoom 0.5
        with fastdissolve   
        ww "There are other portals. I didn't come here through a nazi one. I must find MY portal that will take me back to MY home."
        hide wonderbaby03
        show wonderbaby02 at centerleft
        with fastdissolve           
        mc "I see..."
        jump WonderLevel02NewDialogues02
    "It's a girl. But you said you needed big strong boys on your island. Sooooo...":
        hide wonderbaby02
        show wonderbaby03 at centerleft:
            zoom 0.5
        with fastdissolve   
        ww "You want to impregnate me again?"
        mc "Well, I mean, now that you mention it, yeah, why not, I would gladly sacrifice some of my seed to save your lineage of Amazon Warriors."
        hide wonderbaby03
        show wonderbaby01 at centerleft
        with fastdissolve   
        ww "How considerate of you. But right now, I'm busy nursing Alpha-Girl. She needs to grow big and strong herself..."
        mc "But after she's done nursing, you might... like, consider it?"
        hide wonderbaby01
        show wonderbaby02 at centerleft
        with fastdissolve           
        ww "Maybe..."
        jump WonderLevel02NewDialogues02
    "I have no more daddy business here.":
        hide wonderbaby02
        show wonderbaby03 at centerleft:
            zoom 0.5
        with fastdissolve   
        ww "Good, because a female Amazon baby doesn't NEED a father."
        jump Main

label WonderBirthAuditDialogues:
scene wonderroomday
show auditbaby01
with fade
ag "Oh, hello [name]."
if sawauditbaby:
    mc "How is she doing?"
    hide auditbaby01
    show auditbaby02
    with fastdissolve
    play sound "sounds/lick01.ogg"
    ag "She's doing just fine, she's been sucking on my nipple for over an hour again."
    mc "She's definitely my daughter. We both had the same idea."
    hide auditbaby02
    show auditbaby03
    with fastdissolve
    ag "You're not suggesting... Again???"
    mc "I am suggesting it again! I need to bond with my daughter through YOUR titty-milk!"
if sawauditbaby == False:
    $ sawauditbaby = True
    mc "What are you doing with the baby, I mean, MY daughter???"
    hide auditbaby01
    show auditbaby02
    with fastdissolve
    ag "Wonder Woman needed a babysitter. And my tits are so fat and full of milk that I volunteered to feed Alpha-Girl..."    
    play sound "sounds/lick01.ogg"
    ag "She seems to like it, she's been sucking on my nipple for over an hour now!"
    mc "I see you have a free nipple. One that could feed another hungry mouth..."
    hide auditbaby02
    show auditbaby03
    with fastdissolve
    ag "You're not suggesting... That would be so..."
    mc "I need to taste it to make sure you're not feeding foul breastmilk to my daughter!"
window hide
show mcauditbaby01 at farleft with moveinleft
mc "So get that right nipple out for ME-EE!"
hide mcauditbaby01
hide auditbaby03
show auditbaby04 at centerleft
with fastdissolve
mc "Gimmee, gimmee, gimmee..."
ag "That just feels... wrong..."
hide auditbaby04
show auditbaby05 at centerleft
with fastdissolve
play sound "sounds/slurp.mp3"
ag "Don't be so rough..."    
scene wonderroomday blurred:
    zoom 1.6
show auditbaby06
with dissolve
play sound "sounds/lick02.mp3"
ag "Uhhh!"
hide auditbaby06
show auditbaby07
with fastdissolve
play sound "sounds/lick03.mp3"
ag "You're milking me like a fat cow, AAAH!"
play sound "v051/babycrying.mp3"
ag "Oh no, you made Alpha-Girl cry!"
hide auditbaby07
show auditbaby08
with fastdissolve
play sound "sounds/punch.mp3"
mc "Ouch!"
ag "She also pack a mighty kick!"
scene wonderroomday
show auditbaby02
show mcauditbaby02 at farleft
with dissolve
play sound "sounds/lick01.ogg"
ag "You'd better go back to your room and put some ice on that dislocated jaw, [name]..."
mc "mmuu...mmmaaa...mmmeee."
ag "Sorry, didn't get you just said..."
jump Main

label WonderRoomBigTits:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy03.mp3"
scene wonderroomnight02
show wonderworn01 at centerleft
with fade
mc "Oh, where's my dau... I mean our daughter, Princess Diana?" 
hide wonderworn01
show wonderworn02 at centerleft
with fastdissolve
ww "She's being taken care of by Audit Girl. She has sucked so much milk out of me that my tits have just grown painfully LARGE..."
mc "Ah yes, I thought there was something different about you. Bigger boobs, what a tragedy."
hide wonderworn02
show wonderworn03:
    xpos 0.1 zoom 0.5
with fastdissolve
ww "You think they're better like this? But they're too HEAVY! I can't fight properly with these huge udders... And I feel so tired..."
mc "Let me think... And let me do something else too, cos I can multi-task, being a Super-Hero and all that..."
window hide
show wonderworn03:
    subpixel True
    xpos 0.1 ypos 0.0
    linear 4.0 zoom 1.0 xpos -0.3 ypos -0.8
pause
mc "Mmh, yeah, now I'm thinking..."
window hide
show wonderworn04 as wonderworn03:
    xpos -0.3 ypos -0.8 zoom 1.0
with dissolve
pause
mc "...more clearly! And I have an idea."
scene wonderroomnight02 blurred:
    zoom 1.2
show wonderworn05 at centerleft
with dissolve
mc "I think we need to get the milk OUT!"
hide wonderworn05
show wonderworn06 at centerleft
with fastdissolve
ww "But that's what Alpha-Girl was doing!"
mc "Yeah, but I'll do it differently, trust me on this, I'm the boob expert."
scene wonderroomnight03 blurred
show wonderworn07 at centerleft
with fastdissolve
ww "What are you doing? I... I feel weak and helpless."
mc "Just holding you so you don't move too much while I do..."
hide wonderworn07
show wonderworn08 at centerleft
with fastdissolve
mc "...THAT!"
play sound "sounds/moan01.mp3"
ww "Uuuhhh..."
scene wonderroomnight03 blurred:
    zoom 1.2
show wonderworn09 
with fastdissolve
play sound "sounds/moan06.ogg"
mc "It's working, let's get more titty juice flowing..."
hide wonderworn09
show wonderworn10
with fastdissolve
play sound "sounds/moan05.mp3"
ww "My boobs are growing! You're doing it all WRONG!"
hide wonderworn10
show wonderworn11
with fastdissolve
mc "That depends on one's point of view I'd say..."
ww "They're just MASSIVE now! I NEEDED them to get smaller, you idiot!"
hide wonderworn11
show wonderworn12
with fastdissolve
mc "That's it, there's only one way to do this then, a TITTY-FUCK!"
ww "Wh... What? But... That doesn't make any sense!"
mc "It makes perfect sense to me, and that's all that matters."
scene wonderworn13 with dissolve
mc "Let me lay you down on the bed. Just relax, my Super-Cock will do the rest!"
ww "I... Are you sure this will work?"
scene wonderworn14:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
mc "Yes, I mean, the dev can't keep your tits that large for much longer, it looks like this is a BE scene. And BE scenes end back where they started usually."
ww "What are you talking about?"
scene wonderworn15 with dissolve
mc "You'll see, the Super-Studliness of my love sword will vanquish the pain in your boobs. Therefore, they should go back to normal."
ww "Fine, let's try then. It's my last hope anyway..."
scene wonderworn16 with dissolve
mc "First, let me introduce my big friend here..."
ww "I remember him. He's hard-headed and ends up spewing non-stop nonsense."
scene wonderworn17 with dissolve
play sound "sounds/thud.mp3"
mc "You feel that? That's your way out of this predicament..."
play sound "sounds/moan01.mp3"
ww "Uuuh..."
window hide
show wondertitslap
pause
scene wonderworn18 with dissolve
mc "Err. Just let me place my dong right between..."
mc "...those soft tittes, AAAH!"

play channel1 "sounds/wank.mp3"
label WonderWornSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornslowvideo behind wonderwornfastvideo
show wonderwornslowvideo behind wonderwornpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderwornfastvideo
hide wonderwornpovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderworntalkfast = False
if wonderworntalkslow == False:
    ww "This doesn't seem to work, I still feel PAIN in my boobs!"
    mc "Don't worry, it will come, let me enjoy this titfuck a while longer first..."
    $ wonderworntalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderwornslow()
screen wonderwornslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornPOVSlow")

label WonderWornFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornfastvideo behind wonderwornslowvideo
show wonderwornfastvideo behind wonderwornpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderwornslowvideo
hide wonderwornpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderworntalkslow = False
if wonderworntalkfast == False:
    ww "Come on, please, help me get my tits back to normal, [name]!"
    mc "Yeah, okay... * puff * Just a bit more... titfucking..."
    $ wonderworntalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderwornfast()
screen wonderwornfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderWornEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornPOVFast")

label WonderWornPOVSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornpovslowvideo behind wonderwornslowvideo
show wonderwornpovslowvideo behind wonderwornpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderwornslowvideo
hide wonderwornpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderworntalkfast = False
if wonderworntalkslow == False:
    ww "This doesn't seem to work, I still feel PAIN in my boobs!"
    mc "Don't worry, it will come, let me enjoy this titfuck a while longer first..."
    $ wonderworntalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderwornpovslow()
screen wonderwornpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornSlow")

label WonderWornPOVFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderwornpovfastvideo behind wonderwornfastvideo
show wonderwornpovfastvideo behind wonderwornpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderwornpovslowvideo
hide wonderwornfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderworntalkslow = False
if wonderworntalkfast == False:
    ww "Come on, please, help me get my tits back to normal, [name]!"
    mc "Yeah, okay... * puff * Just a bit more... titfucking..."
    $ wonderworntalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderwornpovfast()
screen wonderwornpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderWornPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderWornEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderWornFast")

label WonderWornEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
ww "They're still MASSIVE!"
mc "Not for long, I'm about to..."
scene wonderbedtitcum01 with dissolve
stop channel2
play channel2 "sounds/boyorgasm01.mp3"
mc ".... BLOW MY NUT!"
window hide
with hpunch
mc "AAAH!"
scene wonderbedtitcum02 with dissolve
ww "What are you doing? You were supposed to come on my TITS!"
window hide
with fastflash
mc "AAAAH! Sorry about that, I'll try and..."
scene wonderbedtitcum03 with dissolve
mc "...aim better this time, RHAAA!"
window hide
with vpunch
ww "I've got your red-hot batter all over my face!"
scene wonderbedtitcum04 with dissolve
mc "Don't you worry, I still have enough nutsauce to shower your giant boobs! UUUUH!"
window hide
with fastflash
ww "Keep pumping, if what you say is true, they need to be COVERED in it!"
scene wonderbedtitcum05 with dissolve
stop channel2
play sound "sounds/femalegrunt01.mp3"
ww "This had better work! My breasts are aching so much!"
scene wonderbedtitcum06 with dissolve
ww "AAAAH! Finally, they seem to... get smaller..."
mc "I'd say what a pity, but I kind of knew it was bound to happen."
scene wonderbedtitcum07 with dissolve
ww "Finally!"
mc "See? My Super-Load made your Super-Boobs, errr.... less super."
ww "The pain is withering away... Thank you, but now I need to take a shower. I'm caked in your filthy scum."
mc "Hey! My Super-Scum is anything BUT filthy!"
$ seenwonderworn = True
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label WonderRoomFuck:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
play music "sounds/sexy03.mp3"
scene wonderroomnight02
show wonderlingerie03 at centerleft
if wonderharem == False:
    ww "I'm afraid Alpha-Girl isn't here, if that's who you were after..."
    mc "I was actually looking for YOU, Princess Diana..."
if wonderharem:
    ww "I'm in my lingerie, ready to serve you as your harem slave..."
    mc "Less time-wasting, that's good, you're learning fast."
hide wonderlingerie03
show wonderlingerie04 at centerleft
with fastdissolve
if wonderharem == False:
    ww "Oh? I'm... flattered. You actually CARE about me after all. Or do you?"
    mc "Err, Of course I do, you're the mother of my child!"
    if evilness >= 13:
        ww "But you have evil intents, I can still feel it, I cannot trust you..."
        scene wonderroomnight02 blurred:
            zoom 1.2
        show wonderevil01
        with dissolve
        mc "Come on now, that's no way to speak to your almost husband, Princess Diana..."
        ww "What are you doing? I don't like this, it's susp..."
        scene wonderroomnight03 blurred
        show wonderevil02
        with dissolve
        ww "Hey! Get this off me, you're handcuffing me!"
        mc "That's correct. And now you're TIED and you will OBEY me!"
        hide wonderevil02
        show wonderevil03
        with dissolve
        ww "I..."
        mc "Right?"
        ww "Yes, I am nothing but a subservient woman, my duty is to serve and obey the superior gender..."
        mc "Now we're talking! Let me get more confortable and admire your beauty..."
        scene wwomanpre00b with dissolve
        mc "I'm ready! And seeing you in handcuffs is making me particularly HORNY!"
        scene wwomanpre01b with dissolve
        ww "I can see that... Your thing... It's MONSTROUS! So manly and commanding my total womanly devotion, as it should."
        scene wwomanpre02b with dissolve
        mc "I think you're sufficiently obedient now for me to unlock your handcuffs. But you'll be a good girl, right?"
        ww "I... I am totally defeated by your superior masculinity..."
        mc "Wonderful..."

    if evilness <= 12:
        ww "I suppose you have shown some... fatherly affection towards her. Maybe it is time to show ME some of that attention."
        mc "Oooh, you want me to be your daddy?"
        hide wonderlingerie04
        show wonderlingerie05 at centerleft
        with fastdissolve
        ww "That's NOT what I meant. I meant... Some loving...Some..."
        mc "SEX!"
        hide wonderlingerie05
        show wonderlingerie02 at centerleft
        with fastdissolve
        ww "* sigh * Alright, if you have to be so blunt about it. But with some foreplay."
        mc "Of course, Princess Diana. I'll sit on the bed and you do the foreplay thingie."
        ww "* sigh*"
        scene wwomanpre00 with dissolve
        mc "I'm ready! And I'm getting HARD!"
        scene wwomanpre01 with dissolve
        ww "I can see that..."

if wonderharem:
    ww "I suppose I should let you sit on the bed for the formal harem proceedings to begin."
    menu:
        "Handcuff her.":
            scene wonderroomnight02 blurred:
                zoom 1.2
            show wonderevil01
            with dissolve
            mc "Hang on a minute, I want to have a closer look at your hot bod first..."
            ww "Err.... Of course..."
            scene wonderroomnight03 blurred
            show wonderevil02
            with fastdissolve
            ww "Hey, why are you handcuffing me, Master?"  
            mc "Just a little sexual kink of mine. Now you'll OBEY me even more..."
            hide wonderevil02
            show wonderevil03
            with fastdissolve
            ww "I was already going to obey you anyway since I'm in your harem..."
            mc "That's true, but it's more fun like this."
            scene wwomanpre00b with dissolve
            mc "I'm ready! And seeing you in handcuffs is making me particularly HORNY!"
            scene wwomanpre01b with dissolve
            ww "I can see that... Your thing... It's MONSTROUS! But how can I service it if I'm in handcuffs?"
            scene wwomanpre02b with dissolve
            mc "I suppose you're right. Come over here, and let's do this the proper way now that I'm ROCK-HARD!"
            mc "Wonderful..."
        "Don't handcuff her.":
            mc "You suppose right."
            scene wwomanpre00 with dissolve
            mc "I'm ready! And I'm getting HARD!"
            scene wwomanpre01 with dissolve
            ww "I can see that... Master's cock is getting MASSIVE for WOnder Woman!"

label WonderRoomPreAss:
scene wonderroompreass01 with dissolve
mc "Now I want you to show me those WONDERFUL titties of yours..."
if wonderharem == False:
    scene wonderroompreass02 with dissolve
    ww "They're not too small for you then?"
    mc "I like 'em big, but I also like' em nice and firm like yours. Variety is the spice of life. And your ass is just sumptuous too, let's see it actually..."
if wonderharem:
    scene wonderroompreass02 with dissolve
    ww "They're not too small for you then?"
    mc "I like 'em big, but I also like' em nice and firm like yours. Variety is the spice of life. And your ass is just sumptuous too, let's see it actually..."
    ww "Yes, Harem master..."
scene wonderroompreass03 with dissolve
ww "Should I take my panties off too?"
mc "Not yet, not yet.... Come foward, Princess Diana, approach my Super-Cock!"
if wonderharem == False:
    scene wonderroompreass04 with dissolve
    mc "That's nice, what a sumptuous pair of buns you have there..."
    ww "Thanks, I suppose."
    scene wonderroompreass05 with dissolve
    mc "Why don't rub it against my aching dong?"
    ww "Fine, I'll rub my ass against that hard dong of yours. Hopefully, it will explode and you'll be satisfied."
    mc "Try your best, we'll see. I'm like, SUPER-HORNY tonight, so I doubt it will work..."
if wonderharem:
    scene wonderroompreass04 with dissolve
    mc "That's nice, what a sumptuous pair of buns you have there..."
    ww "I... Thank you Master for the compliment. My duty is to serve you."
    scene wonderroompreass05 with dissolve
    mc "Then why don't rub it against my aching dong?"
    if evilness >= 13:  
        ww "Your wish is my command, I am bound to obey you. Even if you are truly EVIL."
        mc "Well, let's not exaggerate, I haven't done anything too nasty. YET."
    if evilness <= 12:  
        ww "Your wish is my command, I am bound to obey you.."
        mc "You know this for the best, since a SEX Super-Hero like me needs a heavy does of love-making to keep going..."
window hide

play channel1 "sounds/wank.mp3"
label WonderAssSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderassslowvideo behind wonderassfastvideo
show wonderassslowvideo behind wonderasspovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderassfastvideo
hide wonderasspovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderasstalkfast = False
if wonderasstalkslow == False:
    ww "Is my ass making your cock SUPER-HARD, [name]?"
    mc "Oh damn, YES!"
    $ wonderasstalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderassslow()
screen wonderassslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssPOVSlow")

label WonderAssFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderassfastvideo behind wonderassslowvideo
show wonderassfastvideo behind wonderasspovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderassslowvideo
hide wonderasspovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderasstalkslow = False
if wonderasstalkfast == False:
    ww "And what if I slid down your shaft a bit faster... Would that make you EXPLODE?"
    mc "I... OH FUCK!"
    $ wonderasstalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wonderassfast()
screen wonderassfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAssEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssPOVFast")

label WonderAssPOVSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderasspovslowvideo behind wonderassslowvideo
show wonderasspovslowvideo behind wonderasspovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderassslowvideo
hide wonderasspovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderasstalkfast = False
if wonderasstalkslow == False:
    ww "Is my ass making your cock SUPER-HARD, [name]?"
    mc "Oh damn, YES!"
    $ wonderasstalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderasspovslow()
screen wonderasspovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssSlow")

label WonderAssPOVFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wonderasspovfastvideo behind wonderassfastvideo
show wonderasspovfastvideo behind wonderasspovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderasspovslowvideo
hide wonderassfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderasstalkslow = False
if wonderasstalkfast == False:
    ww "And what if I slid down your shaft a bit faster... Would that make you EXPLODE?"
    mc "I... OH FUCK!"
    $ wonderasstalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderasspovfast()
screen wonderasspovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderAssPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderAssEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderAssFast")

label WonderAssEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
mc "You tried your best, but I resisted... I'm still SUPER-HARD and SUPER-HORNY!"
scene wonderroompretits01 with dissolve
ww "That's disappointing... Please tell me how to make it go down, I beg you!"
mc "Maybe you could let me play with your breasts for a while. I'm more of a breastman than an assman. Although it depends on the player obviously."
scene wonderroompretits02 with dissolve
ww "Fine, go ahead, I'm here to serve you after all..."
mc "That's a good girl."
scene wonderroompretits03 with dissolve
play sound "sounds/slurp.mp3"
mc "Now let's see if there's still some titty-milk left in there for ME!"
ww "Aaaah..."
scene wonderroompretits04 with dissolve
play sound "sounds/moan05.mp3"
mc "Ta-da!"
scene wonderroompretits05 with dissolve
ww "That was embarrassing, it should have been for Alpha-Girl."
mc "She's a pain in the boobs, remember? Pain in the boobs, Get it?"
scene wonderroompretits06 with dissolve
if wonderharem == False:
    ww "Your jokes are getting worse and worse. I'm going to make you PAY with your load for that one!"
if wonderharem:
    ww "As your harem slave, I am bound to find this funny. Even if I didn't get it. Let me get you off with my tits, and this time, Wonder Woman will succeed!"
mc "Alright! Let's see what you've got in store for me then!"
scene wonderroompretits07 with dissolve
play sound "sounds/lick01.ogg"
scene wonderroompretits08 with dissolve
play sound "sounds/lick02.mp3"
ww "Too much for you, [name]?"
play sound "sounds/boymoan.mp3"
mc "Uuuh.... It's just a small plume of premature cum, not to worry..."
scene wonderroompretits09 with dissolve
play sound "v032/gulp.mp3"
ww "Is that so? Then let's make this cock REALLY EXPLODE!"
window hide
play channel1 "sounds/wank.mp3"

label WonderTitSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitslowvideo behind wondertitfastvideo
show wondertitslowvideo behind wondertitpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wondertitfastvideo
hide wondertitpovslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wondertittalkfast = False
if wondertittalkslow == False:
    ww "This time, don't even try and resist."
    $ wondertittalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wondertitslow()
screen wondertitslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitPOVSlow")

label WonderTitFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitfastvideo behind wondertitslowvideo
show wondertitfastvideo behind wondertitpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wondertitslowvideo
hide wondertitpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wondertittalkslow = False
if wondertittalkfast == False:
    if age >= 20:
        ww "If I do it faster like this, your great big whopper is going to explode, isn't it?"
    if age >= 18 and age <= 19:
        ww "If I do it faster like this, your great big teenage whopper is going to explode, isn't it?"
    mc "Oh... Fuck, yeah... Just a bit more..."
    $ wondertittalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show pov:
     xpos 50 ypos 500     
call screen wondertitfast()
screen wondertitfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderTitEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitPOVFast")

label WonderTitPOVSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitpovslowvideo behind wondertitslowvideo
show wondertitpovslowvideo behind wondertitpovfastvideo
$ renpy.pause(1.0, hard='True')      
hide wondertitslowvideo
hide wondertitpovfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wondertittalkfast = False
if wondertittalkslow == False:
    ww "This time, don't even try and resist."
    $ wondertittalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wondertitpovslow()
screen wondertitpovslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitPOVFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitSlow")

label WonderTitPOVFast:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
show wondertitpovfastvideo behind wondertitfastvideo
show wondertitpovfastvideo behind wondertitpovslowvideo
$ renpy.pause(1.0, hard='True') 
hide wondertitpovslowvideo
hide wondertitfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wondertittalkslow = False
if wondertittalkfast == False:
    if age >= 20:
        ww "If I do it faster like this, your great big whopper is going to explode, isn't it?"
    if age >= 18 and age <= 19:
        ww "If I do it faster like this, your great big teenage whopper is going to explode, isn't it?"
    mc "Oh... Fuck, yeah... Just a bit more..."
    $ wondertittalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wondertitpovfast()
screen wondertitpovfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderTitPOVSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderTitEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderTitFast")

label WonderTitEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide pov
ww "Come on, come for me, come for WONDER WOMAN!"
scene wwomantitcum01 with dissolve
stop channel2
play sound "sounds/boymoan03.mp3"
mc "Alrigh,t here it comes, AAAH!"
window hide
with fastflash
play channel2 "v031/boyorgasm02.mp3"
ww "Yes, YES!"
scene wwomantitcum02 with dissolve
play sound "sounds/wow.mp3"
ww "I did it, I made you come!"
window hide
with hpunch
mc "And I'm only getting started, AAAH!"
scene wwomantitcum03 with dissolve
ww "By Zeus, let your baby-batter rain down upon us!"
window hide
with fastflash
mc "RHOOOOO!"
scene wwomantitcum04 with dissolve
stop channel1
stop channel2
play sound "sounds/panting.mp3"
ww "Once again, Wonder Woman defeats her beastly opponent."
play sound "sounds/slurp.mp3"
mc "Gggg...."
scene wwomantitcum05:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
play sound "sounds/lick02.mp3"
ww "Mmh, it's wonderfully tasty..."
mc "I agree, I tasted it myself when, err... the Black Widow forced me to."
scene wwomantitcum06 with dissolve
ww "But that wasn't enough for you, was it?"
mc "What? I mean, yeah, one is NEVER enough!"
scene wwomantitcum07 with dissolve
play sound "sounds/lick01.ogg"
ww "So I NEED to make you explode AGAIN, right?"
scene wwomantitcum08 with dissolve
play sound "sounds/lick03.mp3"
mc "Indeed, you have your need, I have my needs too!"
scene wwomantitcum09 with dissolve
if age >= 20:
    ww "You've made me so horny coming like a true STALLION that I'm ready to take your MASSIVE cock..."
if age >= 18 and age <= 19:
    ww "You've made me so horny coming like a true STALLION that I'm ready to take your MASSIVE teen cock..."
mc "Now we're talking!"
scene wwomantitcum10 with dissolve
ww "But I can't get pregnant again. Not until I find my home portal..."
mc "So I guess ANAL it is then!"
scene wwomantitcum11 with dissolve
ww "You guessed right..."
mc "Bingo!"
scene wwomantitcum12:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1    
with dissolve
ww "But be careful with that thing. I still need to be able to FIGHT."
if age >= 20:
    mc "I'll be as gentle as a man equipped with an eighteen-inch cum-cannon can be."
if age >= 18 and age <= 19:
    mc "I'll be as gentle as a teenage boy equipped with an eighteen-inch cum-cannon can be."
scene wwomantitcum13 with dissolve
ww "You promise you'll be gentle?"
mc "Of course, Pricness Diana."
scene wwomantitcum14 with dissolve
play sound "sounds/gasp.mp3"
mc "What harm could THIS weapon possibly do?"
play sound "sounds/moan01.mp3"
ww "It's so BIG..."
scene wwomantitcum15 with dissolve
mc "Get on top of me and let me gently pleasure... your backdoor."
scene wwomantitcum16 with dissolve
play sound "sounds/womangroan.mp3"
ww "My ass! It's distending so much!"
scene wwomantitcum17 with dissolve
mc "NOT ENOUGH FOR MY DONG!"
play channel1 "sounds/wank.mp3"

label WonderBedAnalSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalslowvideo behind wonderbedanalfastvideo
show wonderbedanalslowvideo behind wonderbedanalfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderbedanalfastvideo
hide wonderbedanalfrontslowvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderbedanaltalkfast = False
if wonderbedanaltalkslow == False:
    ww "Oh God, it's so BIG in my ass!"
    $ wonderbedanaltalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen wonderbedanalslow()
screen wonderbedanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalFrontSlow")

label WonderBedAnalFast:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfastvideo behind wonderbedanalslowvideo
show wonderbedanalfastvideo behind wonderbedanalfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderbedanalslowvideo
hide wonderbedanalfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderbedanaltalkslow = False
if wonderbedanaltalkfast == False:
    mc "Yeah, that's it, ride my fat dong faster, you know you want to!"
    ww "I want to make you come!"
    $ wonderbedanaltalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500     
show front:
     xpos 50 ypos 500     
call screen wonderbedanalfast()
screen wonderbedanalfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBedAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFrontFast")

label WonderBedAnalFrontSlow:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfrontslowvideo behind wonderbedanalslowvideo
show wonderbedanalfrontslowvideo behind wonderbedanalfrontfastvideo
$ renpy.pause(1.0, hard='True')      
hide wonderbedanalslowvideo
hide wonderbedanalfrontfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan02.mp3"
$ wonderbedanaltalkfast = False
if wonderbedanaltalkslow == False:
    ww "Oh God, it's so BIG in my ass!"
    $ wonderbedanaltalkslow = True
window hide
pause
show faster:
     xpos 1700 ypos 500     
show sceneicon:
     xpos 50 ypos 500     
call screen wonderbedanalfrontslow()
screen wonderbedanalfrontslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFrontFast")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalSlow")

label WonderBedAnalFrontFast:
hide cum
hide faster
hide slower
hide sceneicon
hide front
show wonderbedanalfrontfastvideo behind wonderbedanalfastvideo
show wonderbedanalfrontfastvideo behind wonderbedanalfrontslowvideo
$ renpy.pause(1.0, hard='True') 
hide wonderbedanalfrontslowvideo
hide wonderbedanalfastvideo
with dissolve
stop channel2
play channel2 "sounds/boymoan04.mp3"
$ wonderbedanaltalkslow = False
if wonderbedanaltalkfast == False:
    mc "Yeah, that's it, ride my fat dong faster, you know you want to!"
    ww "I want to make you come!"
    $ wonderbedanaltalkfast = True
window hide
pause
show cum:
    xpos 1750 ypos 1020    
show sceneicon:
     xpos 50 ypos 500     
show slower:
     xpos 1700 ypos 500     
call screen wonderbedanalfrontfast()
screen wonderbedanalfrontfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(120, 60)        
        action Jump ("WonderBedAnalFrontSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("WonderBedAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(180, 60)        
        action Jump ("WonderBedAnalFast")

label WonderBedAnalEnd:
hide cum
hide faster
hide slower
hide sceneicon
hide front
ww "Are you ready to explode your cream inside Wonder Woman's ass?"
if wonderharem:
    mc "Is that what you want? Go on, say it, my harem slave!"
if wonderharem == False:
    mc "Is that what you want? I'll turn you into my harem slave with my spunk!"
scene wwomananalcum01 with dissolve
stop channel2
play channel2 "v031/boyorgasm02.mp3"
play channel1 "sounds/splooge01.mp3"
mc "AAAH! FU-UUUUCK!!!"
window hide
with fastflash
ww "I can FEEL your shots! They're so PLENTIFUL!"
scene wwomananalcum02 with dissolve
mc "Those were just an appetizer, THESE are the REALLY MONSTER ONES! UUUH!"
window hide
with hpunch
ww "SSSSOOO MUCH WARM BABY-BATTER!!!"
scene wwomananalcum03 with dissolve
mc "I've got more in store for you, Wonder Woman! RHAAA!"
window hide
with fastflash
play sound "sounds/moan06.ogg"
ww "AAAAAH, By Zeus, you're coming so DEEP inside me!"
scene wwomananalcum04 with dissolve
ww "I'm just ass-blowing your cum now, there's just too much of it!"
window hide
with vpunch
mc "I filled you up, now it's time to COVER you with my Alpha-Spunk then!"
scene wwomananalcum05 with dissolve
stop channel1
if age >= 20:
    ww "You're STILL cumming? You have such a HUGE reservoir of potent seed!"
if age >= 18 and age <= 19:
    ww "You're STILL cumming? You have such a HUGE reservoir of potent teenage seed!"
window hide
with fastflash
mc "Damn right, AAAH!"
scene wwomananalcum06 with dissolve
stop channel2
play sound "sounds/panting.mp3"
ww "You came so much..."
mc "Phew, thanks to your HOT BOD, Princess Diana!"
scene wwomananalcum07 with dissolve
play sound "sounds/kiss.mp3"
if wonderharem:
    ww "That's such a sweet thing to say. Kiss me, my beloved BREEDING STUD!"
if wonderharem == False:
    ww "You fucked me so WONDERFULLY... You are a true HAREM MASTER!"
    window hide
    play sound "sounds/achievement.mp3"
    show haremgirlwonder at posharem
    $ renpy.pause(0.5, hard='True')
    show haremgirltext at posharemtext
    pause
    $ wonderharem = True
    mc "And you'll be a WONDERFUL addition to my harem!"
    ww "I submit to it... And I'll be ready to service you every time you come to my room in the evening when I'm around..."    
stop music
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main