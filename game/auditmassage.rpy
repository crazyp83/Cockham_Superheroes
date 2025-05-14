label AuditMassage:
hide screen calendar
hide screen statscreenicon
hide screen questscreenicon
scene auditmassage00 with fade
play channel1 "sounds/relax.mp3"
if mctoldauditlingerie == False:
    $ mctoldauditlingerie = True    
    mc "Ooh, you're in lingerie?"
    scene auditmassage01 with dissolve
    voice "audit/massage01"
    ag "Yes... I hope you don't find it too lewd, the way it hugs my big fat curves..."
    scene auditmassage00 with dissolve
    mc "Not at all. Where do I put myself?"
    voice "audit/massage02"
    ag "Lie on your front on the massage bed, I'll give you a back rub first."
    jump AuditMassage02

mc "Ooh, you're in that sexy lingerie again?"
scene auditmassage01 with dissolve
voice "audit/massage03"
ag "Yes... I... don't have any other lingerie set yet..."
scene auditmassage00 with dissolve
mc "Do I lie on my front like last time?"
voice "audit/massage04"
ag "Yes, I'll give you a back rub first."

label AuditMassage02:
scene auditmassage02 with dissolve
voice "audit/massage05"
ag "You seem very tense. Your back muscles are super-hard. I hope my hands will help relieve the tension."
play sound "sounds/boymoan.mp3"
voice "audit/massage06"
ag "Yes, relax your muscles [name]. Just like that."
scene auditmassage03 with dissolve
voice "audit/massage07"
ag "And now I'm going to use my elbow to really push on the tension points..."
scene auditmassage04 with dissolve
play sound "sounds/boymoan02.mp3"
mc "Yeah, that's good..."
scene auditmassage05 with dissolve
voice "audit/massage08"
ag "You feel the tension in that muscle right there?"
mc "Ouch, yeah, oh, it hurts but in a good way..."
voice "audit/massage09"
ag "I need you to give me your arms, I'm going to really pull on those tension points. It might hurt a bit."
if gotmassage:
    menu:
        "Uh, ok.":
            jump AuditMassageFirst
        "Err, I'd rather not. Why don't you work my front?":
            voice "audit/massage10"
            ag "Your front? You have tension there?"
            mc "Yeah, PLENTY of tension."        
            jump AuditMassageSecond

label AuditMassageFirst:
scene auditmassage06 with dissolve
play sound "sounds/bonecrack.mp3"
mc "Oh God, AAAH!"
scene auditmassage08 with dissolve
voice "audit/massage11"
ag "Sorry, am I hurting you?"
mc "YES! I was hoping for something more... gentle!"
scene auditmassage09 with dissolve
voice "audit/massage12"
ag "I'm really sorry I'm... going to do it another way. Which I hope you'll like."
mc "Just don't crack any more ligaments please."
scene auditmassage10 with dissolve
voice "audit/massage13"
ag "I won't, I promise... I need to do something first though so that the rub will be much more slippery..."
scene auditmassage11 with dissolve
mc "What is it?"
voice "audit/massage14"
ag "I need to pour some baby oil on my hands..."
scene auditmassage12 with dissolve
voice "audit/massage14b"
ag "And my disgustingly fat tits..."
scene auditmassage13 with dissolve
voice "audit/massage15"
ag "Now I'm all oiled up and ready to give you a maximum-surface back rub..."
mc "With your breasts???"
voice "audit/massage16"
ag "Yes. They're so oversized and heavy that they should provide the most efficient back massage."
mc "Oooh! I'm READY, Kayla!"
scene auditmassage14 with dissolve
voice "audit/massage17"
ag "Alright, let me get into position. Placing my big fat dirty tits on your muscular back..."
play channel2 "sounds/wetmassage.mp3"
window hide
scene auditbackmassagea with dissolve
voice "audit/massage18"
ag "Can you feel my huge titflesh rubbing all over your back muscles?"
mc "Yeah... Mmmh, do it faster please."
scene auditbackmassageb with dissolve
pause
voice "audit/massage19"
ag "Like that? It's so LEWD, isn't it? I feel so dirty..."
mc "And I feel GOO-OOO-D."
stop channel2
scene auditmassage16 with fade
voice "audit/massage19b"
ag "I hope you're feeling better now. And relieved from the stress of being a superhero..."
mc "I sure am, thanks a lot for this wonderful... backrub, Audit Girl!"
mc "Hopefully, next time, we can work on relieving the stress out of some other part of my body... * wink*"
voice "audit/massage20"
ag "Err, I... I'll try my best to help you."
$ gotmassage = True
stop channel1
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main

label AuditMassageSecond:
scene auditmassage09 with dissolve
voice "audit/massage21"
ag "I think I know what kind of LEWD massage you want. Let me get ready and then turn round..."
scene auditmassage19 with dissolve
mc "You guessed right. I need a good rub. DOWN THERE."
voice "audit/massage22"
ag "Should I help it get out of its tight confinement?"
scene auditmassage20 with dissolve
mc "Be my guest, Kayla, it's waiting to get HARDER and BIGGER so you can REALLY massage it ALL OVER!"
voice "audit/massage23"
ag "You're such a lewd boy... So young and yet so... HUNG!"
scene auditmassage21 with dissolve
voice "audit/massage24"
ag "Oh, look your great big snake is peeking out!"
mc "All the better, I'm getting HARD real quick!"
scene auditmassage22 with dissolve
if age >= 20:
    voice "audit/massage25a"
    ag "Wow, your veins are throbbing... And your behemoth is getting BIGGER so fast!"
if age >= 18 and age <= 19:
    voice "audit/massage25b"
    ag "Wow, your veins are throbbing... And your teenage behemoth is getting BIGGER so fast!"
scene auditmassage23 with dissolve
if seentitmassage == False:
    voice "audit/massage26"
    ag "Oh my God, it's ssoo HUGE! The biggest schlong I've ever seen, and a LOT of boys tried to stick their puds between my mounds at Xavier High..."
    mc "Did you let them?"
    voice "audit/massage27"
    ag "No, I was keeping my lewd tits ready for a REAL MONSTERCOCK! And now I've found it! * giggles *"
if seentitmassage:
    voice "audit/massage28"
    ag "Still so HUGE! The perfect size for my HUGE MOUNDS!"
    mc "That's what I was thinking too."
scene auditmassage24 with dissolve
play sound "sounds/kiss.mp3"
voice "audit/massage29"
ag "Let me help you get even more ROCK-HARD and SUPER-BIG for my monster boobs... By kissing the tip."
mc "Are you planning on a tit massage Kayla?"
scene auditmassage25 with dissolve
voice "audit/massage30"
ag "Isn't that what you wanted, [name]?"
mc "Fuck yeah!"
voice "audit/massage31"
ag "Just lie back and let me take care of your HUGE cock."
play channel2 "sounds/wank.mp3"
window hide

label AuditTitsAnim:
window hide
hide cum
hide alternatetitfuck
hide titfucking
show auditmassage01video behind auditmassage02video
$ renpy.pause(1.0, hard='True')
hide auditmassage02video with dissolve
$ renpy.pause(2.0, hard='True')
mc "Damn that's good... Nice and slow between those huge tiddies..."
window hide
show alternatetitfuck:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500
call screen audittitfuck()
screen audittitfuck():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(400, 60)        
        action Jump ("AuditTitsUpDownAnim")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("AuditTitsCum")

label AuditTitsUpDownAnim:
hide cum
hide alternatetitfuck
hide titfucking
voice "audit/massage32"
ag "I think this cock needs more friction from my lewd tits!"
window hide
show auditmassage02video behind auditmassage01video
$ renpy.pause(1.0, hard='True')
window hide
hide auditmassage01video with dissolve
show titfucking:
     xpos 50 ypos 500
show cum:
     xpos 1700 ypos 500

call screen audittitfuckup()
screen audittitfuckup():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(250, 60)        
        action Jump ("AuditTitsAnim")
    button:
        xpos 1700
        ypos 500
        xysize(70, 60)        
        action Jump ("AuditTitsCum")

label AuditTitsCum:
hide cum
hide alternatetitfuck
hide titfucking
voice "audit/massage33"
ag "Are you going to unleash all that pent-up young sperm and relieve your tension points, [name]?"
window hide
$ seentitmassage = True
$ renpy.pause(1.0, hard='True')
mc "Yeah, I think I'm close to..."
stop channel2
scene audittitcum01 with dissolve
hide auditmassage01video
hide auditmassage02video
play sound "sounds/boyorgasm01.mp3"
mc "...IT! AAAH!"
window hide
with fastflash
voice "audit/massage34"
ag "Let all that stress out!"   
scene audittitcum03 with dissolve
voice "audit/massage35"
ag "You're cumming like a FOUNTAIN! You must have been really TENSE!"
window hide
with fastflash
mc "Oh fuck, oh fuck, RHAAA!"
scene audittitcum03 with dissolve
voice "audit/massage36"
ag "You're STILL spewing all that pent-up tension? Keep PUMPING IT until it's ALL GONE!"
window hide
with fastflash
mc "I am, I am, FU-UUU-CK!"
stop sound
scene audittitcum04 with dissolve
play sound "sounds/panting.mp3"
voice "audit/massage37"
ag "There you go [name]. Did my filthy tits do a good job?"
mc "Yeah... A damn good job, Kayla... Phew..."
voice "audit/massage38"
ag "I think you need to rest for a while to recover from all that relieved stress..."
stop channel1
show screen calendar
show screen statscreenicon
show screen questscreenicon
jump Main
