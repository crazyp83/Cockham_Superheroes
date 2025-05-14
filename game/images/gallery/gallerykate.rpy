label KateGallery:
stop channel3
play channel3 "sounds/storemusic.mp3"
scene katebackground
show katemaingallery at gallerypos01 with moveinleft
call screen gallerykate()
screen gallerykate():
    add "icons/returnicon.png"
    text "{font=Gui/Heroes Legend.ttf}Naughty Kate{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (3, "#fff8", 0, 0),  (2, "#fffc", 0, 0)] at gallerytoptext02
    button:
        focus_mask True
        button:
            xpos 1730
            ypos 1020
            xysize(145, 40)
            action [Hide ("gallerykate"), Jump ("MainGallery04b")]
    add "gallery/animidle.png" xpos 35 ypos 1010
    text "{font=Gui/Heroes Legend.ttf}Animation{/font}" color "#FF0000" size 25 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at galleryanimpos
    button:
            xpos 35
            ypos 1010
            xysize(300, 60)
            action [Hide ("gallerykate"), Jump ("KateGalleryAnim")]
    
    if renpy.seen_image("lingeriemc01"):
        imagebutton:
            focus_mask True
            idle "gallery/kategallery01.png" xpos 400 ypos 100
            hover "gallery/kategallery01.png"
            action Jump ("KateGallery01")
    text "{font=Gui/Heroes Legend.ttf}Sexy Handjob{/font}" color "#FF0000" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext01
    if renpy.seen_image("lingeriemc01") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 400 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("KateGallery")

    if renpy.seen_image("harleystore07"):
        imagebutton:
            focus_mask True
            idle "gallery/kategallery02.png" xpos 750 ypos 100
            hover "gallery/kategallery02.png"
            action Jump ("KateGallery02")
    text "{font=Gui/Heroes Legend.ttf}Anal Pounding{/font}" color "#c90076" size 20 outlines [(2, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at gallerytext02
    if renpy.seen_image("harleystore07") == False:
        imagebutton:
            focus_mask True
            idle "gallery/gallerylocked.png" xpos 750 ypos 100
            hover "gallery/gallerylocked.png"
            action Jump ("KateGallery")

label KateGalleryAnim:
call screen screenanimkate()
screen screenanimkate():
    modal True
    add "gallery/katebackground.jpg"
    add "icons/backicon.png" at posbackicon
    if animcount == 1:
        add "kateanimlin" xalign -0.1 yalign 1.0
    if animcount == 2:
        add "kateanimnak" xalign -0.1 yalign 1.0
    button:
        xpos 1730
        ypos 1020
        xysize(120, 50)        
        action [renpy.hide_screen("screenanimkate"), SetVariable ("animcount", 1), Jump ("KateGallery")]
    text "{font=Gui/Heroes Legend.ttf}      Kate{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero02
    text "{font=Gui/Heroes Legend.ttf}Age: 36{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge01
    text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight01
    text "{font=Gui/Heroes Legend.ttf}30E-21-32{/font}" color "#FF0000" size 25 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosMeasurements
    text "{font=Gui/Heroes Legend.ttf}Sexual Kinks{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink
    text "{font=Gui/Heroes Legend.ttf}Handjob{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink01
    text "{font=Gui/Heroes Legend.ttf}Cum Showers{/font}" color "#FF0000" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosKink02
    add "gallery/kateanim01.png" xpos 1100 ypos 800
    button:
        xpos 1100
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 1), Show ("screenanimkate")]
    add "gallery/kateanim02.png" xpos 1220 ypos 800
    button:
        xpos 1220
        ypos 800
        xysize(100, 100)        
        action [SetVariable ("animcount", 2), Show ("screenanimkate")]
            
label KateGallery01:
stop channel3
scene lingeriebackground with fade
play music "sounds/storemusic.mp3"
mc "Hope that busty store manager is going to be there..."
scene lingeriebackground blurred 
show kate01 with moveinright
show kate01 at center:
    breathe
ka "[hero], your timing is perfect."
mc "Why is that? And why are you wearing such a skimpy outfit?"
hide kate01
show kate03
with fastdissolve
ka "It's \"Sexy Night\" here at Gemini Fancy Store. All employees, including myself, are required to wear something sexy."
hide kate03
show kate05
with fastdissolve
ka "Do you like what I'm wearing?"
mc "Damn, fuck yeah!"
hide kate05
show kate04
with fastdissolve
ka "So, are you here to try some \"sexy\" outfits?"
mc "I am indeed..."
hide kate04
show kate02
with fastdissolve
ka "Then follow me upstairs, to the REAL men's section..."
scene lingeriemc01 with dissolve
mc "Is that... Captain MILF? My landlady?"
ka "Yes it is. Members of the Cockham League of Justice are all regular customers here. Except YOU. And Superman because he only has one outfit and we don't do underwear in XXS size."
scene lingeriemc02 with dissolve
ka "Just sit down, I'll be right back with a pair of luxury gold-plated trunks that will be perfect for your MONSTER package..."
mc "Alright, I hope it's in XXL size then."
ka "XXXXL even. For special superheroes like YOU. * wink *"
scene lingeriemc03 with dissolve
mc "There's a nice view of the city from up here... And a nice view of Powergirl in lingerie..."
window hide
show kate01 with moveinright
show kate01 at center:
    breathe
ka "Now is time for you to get your gear off, [hero]."
mc "Err, like totally naked?"
hide kate01
show kate03
with fastdissolve
ka "Of course. Don't worry, I am a professional and I have seen plenty of cocks before. Or absence of cocks in the case of Superman."
scene lingeriemc04 with dissolve
ka "Now that's better. MUCH better. Please stand on the platform in front of you and I will fit you with this designer-jockstrap for HEROIC BULGES."
scene lingeriemc05 with dissolve
ka "There, a perfect fit. I have an eye for estimating the bulge sizes of my clientele."
mc "I'm not surprised for some reason..."
scene lingeriemc06 with dissolve
ka "Let me just check that your BULLBALLS have ample breathing room..."
mc "Err... You're literally fondling my nuts."
ka "As long as it's not making you hard, I'm just doing my j..."
scene lingeriemc07 with dissolve
play sound "sounds/gasp.mp3"
ka "Oh no, you're getting hard, aren't you?"
play sound "sounds/bonecrack.mp3"
mc "Yes, and my cock is getting stuck in this metal thing!"
scene lingeriemc08 with dissolve
play sound "sounds/boymoan03.mp3"
mc "AAAH, it hurts, do something about it, please!"
ka "Don't move, I'll try and unclasp the trunks!"
play sound "sounds/panting.mp3"
mc "Do it FAST, AAH!"
scene lingeriemc09 with dissolve
ka "There, your cock should have more breathing room now!"
scene lingeriemc10 with dissolve
play sound "sounds/thud.mp3"
mc "UUUUH!"
play sound "sounds/wow.mp3"
ka "Oh my, it's so fucking BIG!"
scene lingeriemc11 with dissolve
stop music
play music "sounds/sexy04.mp3"
mc "Now, this is your fault for not taking into account the fact that I am a GROWER on top of being hung like a horse when I'm soft..."
ka "Well, err... Maybe I can offer you the trunks for free?"
mc "And what are we going to do with my massive hardon?"
ka "I could... jack you off? On the house."
scene lingeriemc12 with dissolve
ka "It's so big. My tiny hand can't get all around it massive girth..."
mc "Then put both hands on it and do your best..."
scene lingeriemc13 with dissolve
if age >= 20:
    ka "Like this? You want me to jerk off your monster schlong with both my tiny little hands?"
if age >= 18 and age <= 19:
    ka "Like this? You want me to jerk off your monster teenage schlong with both my tiny little hands?"
mc "Fuck yeah, stop talking and start jacking!"
play channel1 "sounds/boymoan04.mp3"
play channel2 "sounds/wank.mp3"

label KateHandjobSlowx:
hide nexticon
hide faster
hide slower
window hide
show katehandslowvideo behind katehandfastvideo
$ renpy.pause(1.0, hard='True')
hide katehandfastvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020     
show faster:
     xpos 1750 ypos 500
call screen katehandslowbx()
screen katehandslowbx():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("KateHandjobFastx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateHandjobEndx")

label KateHandjobFastx:
window hide
hide faster
hide slower
hide nexticon
show katehandfastvideo behind katehandslowvideo
$ renpy.pause(1.0, hard='True')
hide katehandslowvideo with dissolve
show nexticon:
    xpos 1700 ypos 1020   
show slower:
     xpos 50 ypos 500
call screen katehandfastbx()
screen katehandfastbx():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("KateHandjobSlowx")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateHandjobEndx")

label KateHandjobEndx:
hide nexticon
hide faster
hide slower
ka "Are you getting there [hero] or do you have SUPER-ENDURANCE?"
mc "I could go forev..."
scene katehandjobcum01 with dissolve
hide katehandfastvideo
hide katehandslowvideo
stop channel1
stop channel2
play sound "sounds/boymoan.mp3"
mc "...oh shit!"
window hide
with fastflash
ka "It looks like you're already spewing a little..."
scene katehandjobcum02 with dissolve
ka "A LOT actually. My expert hands are really that good, hey?"
play sound "sounds/boymoan03.mp3"
window hide
with fastflash
mc "Fuck, I'm..."
scene katehandjobcum03 with dissolve
play sound "sounds/boymoan03.mp3"
mc "...BLOWING BIG TIME!!!! AAAAH!!!"
window hide
with fastflash
with hpunch
ka "You're covering me with your hot SPUNK!"
scene katehandjobcum04 with dissolve
mc "FUCK YEAH, RHAAA!"
play sound "sounds/boyorgasm01.mp3"
window hide
with fastflash
ka "That was defintely a SUPERHERO load!"
window hide
with fastflash
mc "Take those last shots, AAAH!!!!"
scene katehandjobcum05 with dissolve
stop sound
mc "Damn it. I guess you did it. I can get soft again and fit in my thong..."
ka "At Gemini Lingerie, we pride ourselves in catering to our customers' every need...."
scene lingeriebackground blurred 
show kate06 with moveinright
show kate06 at center:
    breathe
ka "Well, I promised you I would give you the trunks for free since I ALMOST broke your MEGA-COCK, which would have been a great loss to Cockham City."
mc "Indeed. And to the very future of this game."
window hide
$ inventorygoldtrunks = True
play sound "sounds/achievement.mp3"
show acquiredgoldtrunks at poslocation
$ renpy.pause(0.5, hard='True')
pause
mc "Oh, by the way, you have a little bit of spunk left on your face."
ka "Do I? Thanks for letting me know... [hero]."
stop channel1
stop music
jump KateGallery

label KateGallery02:
stop channel3
stop music
scene harleystore04 with dissolve
hq "I don't know... It' just not CRAZY enough for me!"
jo "It's PRACTICAL. How are we supposed to blend into a crowd?"
scene harleystore05 with dissolve
hq "Number 1: No one is like me. Have you seen your face in a mirror recently? You wouldn't even fit in a freak circus, puddin!"
scene harleystore06 with dissolve
hq "Na, I want something else, so get me something SEXY you stupid bitch!"
ka "Yy..yes ma'am, of course!"
scene harleystore07 with dissolve
mc "Kate is clearly being FORCED to comply at batpoint. But I need to see more before intervening... Also, I want to see what sexy outfit Harley will be wearing next."
play music "sounds/sexy08.mp3"
scene harleystore08:
    subpixel True
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "Alright! Let's wait for her to pose in that fishnet bodysuit..."
scene harleystore09:
    subpixel True
    ypos 0.0
    linear 8.0 ypos -1.0
$ renpy.pause(4.0, hard='True')
hq "Now that's better, whaddya reckon, puddin?"
jo "Err..."
scene harleystore10:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
with dissolve
$ renpy.pause(4.0, hard='True')
jo "You want to walk down the street like that? That's nuts!"
hq "Why not, you're walking down the street looking like a supervillain clown freak!"
jo "Hey!"
hq "Oh, boo hoo."
scene harleystore11 with dissolve
hq "I'm getting real horny wearing this bodysuit."
jo "Yeah, I'm getting horny too, my belov..."
scene harleystore12 with dissolve
hq "I ain't talking to you, Mr J.! I'm talking to that brunette harlot over there. Why dontya come over here and taste my cunt, you sweet thing?"
ka "But... I'm not a lesbian, Ms Quiff!"
hq "That's okay, cos I AM! So come over here and put that face where it can't talk no more. Right between my legs!"
scene harleystore13 with dissolve
jo "You'd better do as you're told, she's crazy and I have a gun!"
scene harleystore14 with dissolve
hq "Love your perfume, what is that? The scent of Death?"
scene harleystore15 with dissolve
hq "My pussy is welcoming you with open legs!"
scene harleystore16 with dissolve
hq "Go on, have a good lick, twist that tongue in there!"
scene harleystore17 with dissolve
play sound "sounds/moan05.mp3"
hq "Mmh, yes, just like that, mamma's gonna paint your face with white juice!"
scene harleystore18 with dissolve
play sound "sounds/moan05.mp3"
hq "Sweetie, you're getting mommy's bazookas all tingly!"
scene harleystore12 with dissolve
hq "That was good, now it's my turn to return the favor. So get naked, my sweet girl, cos Mamma has a SURPRISE for you!"
scene harleystore19 with dissolve
hq "Wow, what's this? I knew I was carrying some HEAVY WEAPONRY today!"
scene harleystore20 with dissolve
ka "Wh.. What are you going to do with this???"
jo "It's getting steamy in here, I'll just, like, polish my gun real quick..."
hq "Do it quietly puddin, I can hear your voices inside my head!"
scene harleystore21 with dissolve
play sound "sounds/lick02.mp3"
hq "Isn't it tasty, darlin'? Hang on, I'm the one choking on it, silly me!"
hq "Just come over here and I'll let your backdoor have a real good taste of it too!"
scene harleystore22 with dissolve
ka "I've never had something this huge inside my hole, please be gentle, Ms Quiff!"
hq "It's not that big, I've had bigger, so don't ya worry! Your ass looks ready to swallow it whole!"
ka "But, no, plea..."
scene harleystore23 with dissolve
play sound "sounds/moan05.mp3"
ka "AAAH!"
hq "Tada! I always wanted to be a magician and make stuff disappear inside holes. But I'm stuck with a clown..."
jo "Not clown, Joker!"
scene harleystore24 with dissolve
play sound "sounds/moan03.mp3"
hq "How deep is that rabid hole, only one way to find out!"
window hide
play channel2 "sounds/moan04.ogg"
show harleystoredildo with dissolve
pause
stop channel2
scene harleystore24 with fastdissolve
hq "How about we have a DEEPER look at that gaping hole of yours?"
ka "No, please Ms Quiff, this is too deep already, I can't take that much!"
scene harleystore25 with dissolve
play sound "sounds/moan06.ogg"
ka "AAAAAHHHH!"
hq "I’m sorry girl, I’m just a terrible person I guess."
scene harleystore26 with dissolve
play sound "sounds/moan02.mp3"
hq "Well, look at that, your ass looks happier than your face!"
scene harleystore27 with dissolve
hq "I wonder if it'll be THRILLED if I go EVEN DEEPER?"
stop sound
ka "NO, I BEG YOU!"
mc "Maybe I should do something now. Even if I am quite intrigued to see how deep she can take it..."
scene harleystore28 with dissolve
stop music
play music "sounds/dark.mp3"
play sound "sounds/moan04.ogg"
mc "Drop that dildo! And that gun!"
hq "What a party-pooper, boo-hoo!"
scene harleystore29 with dissolve
jo "What, you mean my gun? The one pointed right at your head?"
mc "Err... How did you...?"
scene harleystore30 with dissolve
jo "You're not the only one with Super-Senses, [hero]! I KNEW you were spying on us all along. Now the Joker's on you!"
hq "Don't you just love the CRAZINESS of it all!"
scene harleystore31 with dissolve
jo "I think you've been a very NAUGHTY boy."
scene harleystore30 with dissolve
jo "What kind of superhero RAPES innocent store managers?"
mc "What, I didn't do any such thing!"
scene harleystore31 with dissolve
jo "But what about that picture of you? Harley, put some handcuffs on the young fellow."
scene harleystore32 with dissolve
mc "What picture?"
jo "Why so serious, you'll see."
scene harleystore33 with dissolve
jo "Now you just stand over there while we escape, and don't you move an inch, or I put a bullet in your DONG!"
scene harleystore34 with dissolve
hq "Don't smile puddin', it's for the camera!"
play sound "sounds/flash.mp3"
window hide
with fastflash
jo "I used to think my life was a tragedy, but now I realize it's a comedy! Ha ha ha!"
scene harleystore35 with dissolve
stop sound
play sound "v041/metalbreak.mp3"
stop music
mc "Phew, the crazies are gone so I can use my Super-Strength and get rid of these handcuffs. And then chase after them!"
scene harleystore36 with dissolve
ka "Ggg... Would you mind pulling that dildo out of my ass first, [hero]?"
mc "Ah yes, I suppose I should do that."
scene harleystore37 with dissolve
mc "But now they're gone. And they have that incriminating picture of me and...err... you with a giant dildo up your ass."
ka "It sounds bad. Especially for you."
scene harleystore38 with dissolve
play channel2 "sounds/moan02.mp3"
$ renpy.pause(0.5, hard='True')
scene harleystore39 with fastdissolve
play sound "v041/plop.mp3"
ka "Ohhhh. Now I feel a vacuum in my backdoor. I..."
stop channel2
mc "Yes?"
ka "Please stick your giant cock in there, [hero]! I need to feel like a woman again, not a hole for a sex toy!"
mc "Wow, I did not... expect that."
scene harleystore40 with dissolve
mc "Nevertheless, I can see you are a damsel in distress and if my cock can alleviate your anguish, then it is my duty to DELIVER!"
scene harleystore41 with dissolve
play sound "sounds/winning.mp3"
mc "And [hero]'s Super-Cock is always READY to DELIVER!"
scene katepreanal01 with dissolve
mc "So you want your backdoor to be filled by something HUGE?"
ka "Y...Yes! YES!"
scene katepreanal02 with dissolve
mc "You'd better OPEN UP real WIDE then, cos my cock is HUGER THAN HUGE!"
ka "Just PUSH IT IN, I beg you!"
scene katepreanal03 with dissolve
play sound "sounds/moan05.mp3"
mc "The tip is in, just 15 inches to go!"
ka "Oh God, I might have bitten more than I could chew..."
mc "Too late to BACK DOWN!"
$ kateanalslowx = False

label KateAnalSlowx:
$ kateanalfastx = False
window hide
show kateanalslowvideo behind kateanalfastvideo
show kateanalslowvideo behind kateanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide kateanalfastvideo
hide kateanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if kateanalslowx == False:
    $ kateanalslowx = True
    if age >= 20:
        ka "My ass is so full. Ssooo full of MEGACOCK!"
    if age >= 18 and age <= 19:
        ka "My ass is so full. Ssooo full of MEGA TEEN COCK!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen kateanalslowx()
screen kateanalslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalBackSlowx")

label KateAnalFastx:
$ kateanalslowx = False
window hide
show kateanalfastvideo behind kateanalslowvideo
show kateanalfastvideo behind kateanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide kateanalbackfastvideo
hide kateanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if kateanalfastx == False:
    $ kateanalfastx = True    
    ka "Oooh yeah, POUND MY HORNY ASS with your giant cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen kateanalfastx()
screen kateanalfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalBackFastx")

label KateAnalBackSlowx:
$ kateanalfastx = False
window hide
show kateanalbackslowvideo behind kateanalslowvideo
show kateanalbackslowvideo behind kateanalbackfastvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex01.mp3"
hide kateanalbackfastvideo
hide kateanalslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
with dissolve
if kateanalslowx == False:
    $ kateanalslowx = True
    if age >= 20:
        ka "My ass is so full. Ssooo full of MEGACOCK!"
    if age >= 18 and age <= 19:
        ka "My ass is so full. Ssooo full of MEGA TEEN COCK!"
show cum:
    xpos 1750 ypos 1020    
show faster:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen kateanalbackfuckslowx()
screen kateanalbackfuckslowx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalBackFastx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalSlowx")

label KateAnalBackFastx:
$ kateanalslowx = False
window hide
show kateanalbackfastvideo behind kateanalfastvideo
show kateanalbackfastvideo behind kateanalbackslowvideo
pause 1.0
stop channel1
play channel1 "sounds/womansex02.mp3"
hide kateanalfastvideo
hide kateanalbackslowvideo
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
if kateanalfastx == False:
    $ kateanalfastx = True    
    ka "Oooh yeah, POUND MY HORNY ASS with your giant cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen kateanalbackfuckfastx()
screen kateanalbackfuckfastx():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalBackSlowx")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEndx")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalFastx")

label KateAnalEndx:
hide cum
hide sceneicon
hide faster
hide slower
hide backicon
ka "Are you going to flood my ass with a giant cumload, [hero]?"
mc "You want to?"
ka "Mmmh, yes, YES, PLEASE!"
scene kateanalcum01 with dissolve
stop channel1
play sound "sounds/womancum01.mp3"
play channel1 "v031/boyorgasm02.mp3"
mc "THAR SHE BLOWS, RHAAA!"
window hide
with vpunch
ka "AAAH, I'm coming too!"
scene kateanalcum02 with dissolve
if evilness <= 12: 
    mc "Take your reward, my load DEEP in your ass!"
if evilness >= 13: 
    mc "Take my load DEEP in your ass, you dirty slut!"
window hide
with fastflash
play sound "sounds/womancum02.mp3"
ka "I'm letting a superhero give me a cum enema, aaaah!"
scene kateanalcum03 with dissolve
mc "I'm not done with your ass, here's MOOOO-AAAR!"
window hide
with hpunch
ka "You cum so much for me! Cover me in your superhero spunk, I beg you [hero]!"
scene kateanalcum04 with dissolve
if evilness <= 12:
    mc "Since you're asking so nicely, here goes, RHAAA!"
if evilness >= 13: 
    mc "I always mark my cum-sluts with my spunk after I've DESTROYED their asses, RHAAA!"
window hide
with fastflash
ka "Your shot are so HEAVY!"
scene kateanalcum05 with dissolve
mc "I ain't done, FUUU-UUUCK!"
window hide
with fastflash
ka "You're just a cum-fountain! Sooo much red-hot spunk for my ass and me..."
scene kateanalcum06 with dissolve
play sound "sounds/moan02.mp3"
if age >= 20:
    ka "I've never been fucked so hard and so POWERFULLY... I hope my ass was worthy of your superior alpha-cock..."
if age >= 18 and age <= 19:
    ka "I've never been fucked so hard and so POWERFULLY... I hope my ass was worthy of your superior teen alpha-cock..."
mc "Hang on, still a few more dregs, aaah..."
scene kateanalcum07 with dissolve
stop channel1
play sound "sounds/panting.mp3"
mc "I let the Joker escape from my grip. But for some fine piece of booty I must admit, so it was all worth it."
stop channel1
stop music
jump KateGallery

