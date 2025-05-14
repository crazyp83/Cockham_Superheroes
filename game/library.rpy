label CompoundLibrary:
stop music
$ seenlibrary = True
scene compoundlibrary with fade
call screen librarycompound()
screen librarycompound():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action Jump ("MainTime")
    imagebutton:
        focus_mask True
        idle "icons/statsiconscreenidle.png"
        hover "icons/statsiconscreenhover.png"
        action ui.callsinnewcontext("Statscreen")
    imagebutton:
        focus_mask True
        idle "icons/questsiconscreenidle.png"
        hover "icons/questsiconscreenhover.png"
        action ui.callsinnewcontext("Questscreen")
    if (period == 0 and d10locday <= 8) or (period == 1 and d10locnight >= 3):
        imagebutton:
            focus_mask True
            idle "v01/libraryauditidle.png"
            hover "v01/libraryaudithover.png"
            action Jump ("LibraryAuditGirl")
    if (period == 0 and (d10locday == 1 or d10locday == 2)) or (period == 1 and d10locnight == 7):
        imagebutton:
            focus_mask True
            idle "v01/librarymilfidle.png"
            hover "v01/librarymilfhover.png"
            action Jump ("LibraryMILF")
    imagebutton:
        focus_mask True
        idle "v01/libraryidle.png"
        hover "v01/libraryhover.png"
        action Jump ("EnterLibrary")


label LibraryAuditGirl:
scene libraryauditbackground
show auditeyeblink
with dissolve
ag "Oh, hello [name]."
label LibraryAuditGirlDialogue:
menu:
    "Hi Kayla. What are you doing here?" if agspeak05 == False:
        $ agspeak05 = True
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        ag "This is where I spend most of my time. Well, ALL my time actually."
        mc "Don't you have a bedroom?"
        hide allleagueaudit03
        show allleagueaudit05
        with fastdissolve
        ag "No. I'm just an intern so I sleep in... the library."
        mc "In the library?"
        hide allleagueaudit05
        show allleagueaudit02
        with fastdissolve
        ag "Yes, I have a small bed over there with a night table. I'm fine. I guess."
        mc "Ok, if you say so."
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        jump LibraryAuditGirlDialogue
    "What are you reading at this time of night?" if period == 1: 
        hide auditeyeblink
        show allleagueaudit02
        with fastdissolve
        ag "Well, err... I was looking at my dossier."
        mc "Oh yeah? And whose page specifically?..."
        hide allleagueaudit02
        show allleagueaudit03
        with fastdissolve
        ag "My page... The description in there is just... filthy!"
        mc "I thought YOU wrote it!"
        hide allleagueaudit03
        show allleagueaudit05
        with fastdissolve
        ag "Not MY page. The dev did. He wrote that I have \"enormous jugs and a big booty\". That's just... so LEWD!"
        mc "I think he was spot on personally."
        hide allleagueaudit05
        show allleagueaudit03
        with fastdissolve
        ag "That's just... such a naughty thing of you to say..."
        hide allleagueaudit03
        show auditeyeblink
        with fastdissolve
        jump LibraryAuditGirlDialogue
    "I know where we can get you a costume for you." if loclingerie == False and knowlingerie:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "Really? I'm so happy! Where is it?"
        mc "Some specialized clothing boutique downtown. We could go there right now if you want."
        hide allleagueaudit04
        show allleagueaudit05
        with fastdissolve
        if period == 0:
            ag "I guess I'm not TOO busy right now. I'm in!"
            jump AuditGirlLingerieStore
        if period == 1:
            ag "In the evening?"
            mc "Well sure, this is Cockham, the city that never sleeps! All the shops are still open."
        hide allleagueaudit05
        show allleagueaudit04
        with fastdissolve
        ag "I... didn't know. I come from upstate Cockham. Everything is just boring there. Alright, let's go!"
        jump AuditGirlLingerieStore
    "Do you know if we have any board games around here?" if inventorytwister == False and questtwister and not wonderquesttipaudit:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "Yes, I believe there is a game shelf in the library. Fourth one on the left."
        hide allleagueaudit04
        show auditeyeblink
        with fastdissolve
        mc "Thanks for the tip, Kayla. I'll go and have a look."
        $ wonderquesttipaudit = True
        jump CompoundLibraryTwister
    "You're not wearing your costume?" if loclingerie:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "No, I'm not on any mission and I feel more comfortable in this outfit."
        hide allleagueaudit04
        show auditeyeblink
        with fastdissolve
        ag "It helps me concentrate..."
        jump LibraryAuditGirlDialogue
    "I'm gonna guess you don't have a shower room in the library." if agspeak06 == False:
        $ agspeak06 = True
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        ag "No. And I haven't had a shower in days..."
        mc "Yeah, I noticed. And I don't even have Super-Smell."
        hide allleagueaudit03
        show allleagueaudit05
        with fastdissolve
        ag "That's not a very nice thing to say to a girl..."
        mc "Let me make it up to you. I have a jacuzzi in MY super-room."
        hide allleagueaudit05
        show allleagueaudit04
        with fastdissolve
        ag "You're inviting me? Oh, I'm so happy I'm finally going to be able to get rid of that smell!"
        mc "So are we all..."
        jump AuditJacuzzi
    "I think it's time for your weekly cleaning. In my jacuzzi." if agspeak06 and agstink >= 7:
        hide auditeyeblink
        show allleagueaudit05
        with fastdissolve
        ag "Alright. I guess I do start to stink a bit..."
        mc "Yeah, good thing no one has Super-Smell in this compound or they w..."
        ag "Alright, I get it!"
        if mclevel02:
            jump AuditJacuzziLevel02
        jump AuditJacuzzi
    "I feel tense. I think I need a massage. From YOU." if loclingerie and mclevel02 == False:
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        ag "Oh, I see... I suppose I could use my Super-Healing powers on those tense muscles of yours."
        mc "And you are supposing well."
        if agtoldmassage == False:
            $ agtoldmassage = True
            hide allleagueaudit03
            show allleagueaudit05
            with fastdissolve            
            ag "The massage room is not far away. Sometimes I sleep there when the library is too cold. I'll take you there."
        jump AuditMassage
    "I've gotta go, the period is about to advance...":        
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        if period == 0:
            ag "Well, I'll stay here for a while. I've got nothing better to do anyway."
        if period == 1:
            ag "You're right, it's getting late, I'd better go and snuggle inside my sleeping bag between rows of old books."
        jump Main

label LibraryMILF:
scene librarymilfbackground
show librarymilf01
with dissolve
mc "Hi Carol."
hide librarymilf01
show librarymilf02
with fastdissolve
show librarymilf02 at center:
    breathe
cm "Oh, it's you, you almost scared me."
label LibraryMILFDialogue:
menu:
    "What are you doing here?":        
        hide librarymilf02
        show librarymilf03
        with fastdissolve
        cm "I was looking for a recipe book."
        mc "Why would you need that?"
        hide librarymilf03
        show librarymilf04
        with fastdissolve
        cm "Who do you think does the cooking around here while y'all gallivanting around town?"
        mc "I hadn't thought about that. What's for dinner then?"
        hide librarymilf04
        show librarymilf02
        with fastdissolve
        show librarymilf02 at center:
            breathe
        cm "Until I find a decent recipe book, burger and salad."
        mc "Oooh, camel burger?"
        hide librarymilf02
        show librarymilf04
        with fastdissolve
        cm "What? What a weird suggestion. Why did you even think I might serve you such a disgusting thing?"
        hide librarymilf04
        show librarymilf02
        with fastdissolve
        show librarymilf02 at center:
            breathe
        mc "Err..."        
        jump LibraryMILFDialogue
    "I'm loooking for a book.":
        cm "Then you're in the right place, this is the library. What book are you after?"
        mc "Something about HOT SEX. We can read it together if you'd like... * wink *"
        hide librarymilf02
        show librarymilf04
        with fastdissolve
        cm "Wow, I didn't see that lame line coming. * sigh *"
        hide librarymilf04
        show librarymilf03
        with fastdissolve
        if period == 0:
            cm "I'm very busy [name], why don't you go back to your room and try and do something more productive?"
            mc "Fine. I'll do that..."
        if period == 1:
            cm "I'm very busy [name], why don't you go back to your room and go to sleep? You might be called upon tomorrow to SAVE the WORLD!"
            mc "Alright! Off to bed I go then! Woo-hoo!"
        jump Main
    "Could I ask you to get a board game from the library for me?" if sawghost and inventorytwister == False:        
        cm "Why don't you get it yourself?"
        hide librarymilf02
        show librarymilf03
        with fastdissolve
        mc "Cos it's like SUPER-COLD in there. And I don't have Super-Resistance like you."
        hide librarymilf03
        show librarymilf04
        with fastdissolve
        cm "Fine, I'll do that. Because you're my sweet tenant and you always pay your rent on time. And I'm level 3 in SuUper-Resistance!"
        mc "Be careful though, there's also a ghost in there."
        cm "Pff!"
        scene librarymilfbackground
        show librarymilf04
        with fade
        "(a short while later)"
        cm "Okay, there actually IS a ghost in there!"
        mc "Ah, finally. Somebody believes me. What are we going to do about it?"
        hide librarymilf04
        show librarymilf03
        with fastdissolve
        cm "Nothing. And don't mention it to anyone. NOT EVER."
        mc "Roger that, let's just ignore the problem and hope it will go away, I get it!"
        hide librarymilf03
        show librarymilf02
        with fastdissolve
        show librarymilf02 at center:
            breathe
        cm "Here's your board game. I took the first one I saw on the shelf for obvious reasons... Now go back to your room and try and sleep..."
        $ inventorytwister = True
        play sound "sounds/achievement.mp3"
        show questwondertwister at poslocation
        $ renpy.pause(0.5, hard='True')
        show winicon at poswin
        pause
        mc "Thanks Captain MILF, goodnight to you too."
        jump Main
    "I was wondering where one could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide librarymilf02
        show librarymilf03
        with fastdissolve
        cm "But, she's just an intern. Why would she need a costume?"
        mc "She's still a SUPER-HERO! And superheroes have a costume, otherwise, they don't look like superheroes. And it gets confusing."
        hide librarymilf03
        show librarymilf04
        with fastdissolve
        cm "I suppose so... Well, there is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide auditquestcostumeprogress01
        hide librarymilf04
        show librarymilf03
        with fastdissolve
        cm "Just don't spend too much money on her. She's JUST an intern, sweetie."
        mc "Sure, Carol."
        jump Main
    "Where is Supergirl?" if seensupergirl and seensuperpowergirl:
        hide librarymilf02
        show librarymilf04
        with fastdissolve
        cm "She's with Lara Crotch. So God knows what country she's in right now."
        mc "And when will she paired with me?"
        hide librarymilf04
        show librarymilf03
        with fastdissolve
        cm "When she returns, and I decide it's time for her to be paired with a... sex super-hero. She's only 18, I'm not even sure this is appropriate at all."
        hide librarymilf03
        show librarymilf04
        with fastdissolve
        mc "If she's over 18, just like I am, then EVERYTHING is appropriate according to the Patreon bill passed by Cong..."
        cm "...Congress last year. Yes, I know, sweetie. Still..."
        jump Main
    "Nothing.":
        cm "Then I have nothing either to offer in return."
        jump Main

label CompoundLibraryTwister:
scene library02a with dissolve
mc "So, fourth shelf on the left..."
play sound "sounds/glitch.mp3"
scene library02b with fastdissolve
$ renpy.pause(0.2, hard=True)
scene library02a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene library02b with fastdissolve
$ renpy.pause(0.2, hard=True)
scene library02a with fastdissolve
$ renpy.pause(0.3, hard=True)
scene library02b with fastdissolve
mc "Ah, shit, what happened? I can't see a  damn thing."
scene library04 with dissolve
mc "I think this is where the game shelf should be..."
play sound "sounds/coldwind.mp3"
scene library04 with hpunch
mc "It's super-cold in here suddenly, I..."
if mcresistance >= 1:
    call screen usepower("useresistance", "FleeTwister", "TakeTwister") with dissolve

label FleeTwister:
$ fleeghost = True
play music "sounds/lalala.mp3"
mc "What's that sound???"
window hide
show ghost01:
    xpos 0.15
    linear 6.0 xpos 0.45
show library04b
$ renpy.pause(4.0, hard='True')
hide ghost01
show ghostanim at centerright
$ sawghost = True
mc "AAAH, a GHOST! This place is HAUNTED, I'm getting the fuck outta here!"
stop sound
stop music
scene libraryauditbackground
show auditeyeblink
with fade
play sound "sounds/panting.mp3"
ag "So did you find the game shelf?"
mc "I just saw a ghost!"
hide auditeyeblink
show allleagueaudit04
with fastdissolve
ag "Ghosts don't exist, [name]. They're not REAL."
mc "Yeah? Well, superheroes don't exist either, and yet, here we are!"
hide allleagueaudit04
show allleagueaudit05
with fastdissolve
ag "But I LIVE there and I never saw a ghost!"
mc "Well, maybe that ghost just finds you too boring..."
hide allleagueaudit05
show allleagueaudit02
with fastdissolve
ag "That's not a very nice thing to say..."
mc "Sorry, I... didn't mean it. I'll leave you alone."
jump Main        

label TakeTwister:
$ usedresistance += 1
mc "I'll just take whatever game I can grab and leave quickly before I freeze to death..."
window hide
$ inventorytwister = True
play sound "sounds/achievement.mp3"
show questwondertwister at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
mc "Cool, Twister. I'll head back to my room to warm up a bit."
jump Main   

label EnterLibrary:
if period == 0:
    scene library02c with fade
if period == 1:
    scene library02a with fade
mc "This library looks really old. I'm going to guess it's full of old books."
scene library03 with dissolve
if agspeak05:
    mc "Oh, and this looks like where Audit Girl must be sleeping at nights. Poor girl. Sleeping in such a spooky place."
if agspeak05 == False:
    mc "Why is there a bed here? Who the hell sleeps in a LIBRARY???"
mc "Anyway, I've done my tour of the library, not need to stick around, so I'll go back to my all-amenities comfy room."
jump Main

