label LingerieStore:
if mclevel02 and seenharleystorefirst == False:
    jump HarleyStore
if mclevel02 and seenharleystorefirst and harleypicture == False:
    jump HarleyStoreSecond
if inventorygoldtrunks == False:
    jump LingerieStoreGoldTrunks
scene lingeriebackground with fade
play music "sounds/storemusic.mp3"
mc "Hope that busty store manager is going to be there..."
scene lingeriebackground blurred 
scene lingeriebackground blurred 
show clerk01 with moveinright
show clerk01 at center:
    breathe
ka "Ah, it's you again, [hero]."
mc "You don't seem that pleased to see me."
hide clerk01
show clerk03 
with fastdissolve
ka "You're starting to cost Gemini Lingerie a FORTUNE!"
mc "Hey, I haven't done anything!"
hide clerk03
show clerk04 
with fastdissolve
ka "Still, until I manage to sell some rich customer a LOT of very expensive items, I can't afford to offer you anything for free once again. Goodbye, [hero]."
mc "What, that's it?"
jump Main
    
label LingerieStoreGoldTrunks:
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
show kate02 at center:
    breathe
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
$ renpy.start_predict("katehandslowvideo")
$ renpy.start_predict("katehandfastvideo")
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

label KateHandjobSlow:
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
call screen katehandslowb()
screen katehandslowb():
    modal True
    button:
        xpos 1750
        ypos 500
        xysize(110, 60)        
        action Jump ("KateHandjobFast")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateHandjobEnd")

label KateHandjobFast:
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
call screen katehandfastb()
screen katehandfastb():
    modal True
    button:
        xpos 50
        ypos 500
        xysize(150, 60)        
        action Jump ("KateHandjobSlow")
    button:
        xpos 1700
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateHandjobEnd")

label KateHandjobEnd:
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
jump Main

label AuditGirlLingerieStore:
scene lingeriebackground with fade
play music "sounds/storemusic.mp3"
play sound "sounds/skill.mp3"
show locationstore at poslocation
$ renpy.pause(0.5, hard=True)
pause
mc "Well, this place looks like a very fancy lingerie store..."
hide locationstore
ag "I don't want to be a financial burden on the Cockham League of Justice..."
mc "Nonsense, we have plenty of money, we're SUPERHEROES! So much so that it's not even an icon on my screen."
scene lingeriebackground blurred 
show clerk01 with moveinright
show clerk01 at center:
    breathe
ka "My name is Kate and I'm the store manager. How may I help you?"
mc "I am told you are the sole provider of fine superhero garments in Cockham."
hide clerk01
show clerk02
with fastdissolve
show clerk02 at center:
    breathe
ka "Indeed, what can I do for you, [hero]? You need a BIGGER thong perhaps? One that will provide ample bulge room while maintaining your super-agility skills?"
if mcagility <= 0:
    mc "Err, I don't have super-agility skills."
    ka "Oh, what a shame then."
if mcagility >= 1:
    mc "Ooh, interesting. I do feel like I'm still GROWING a lot, if you see what I mean, hey? * wink *."
    hide clerk02
    show clerk01
    with fastdissolve    
    show clerk01 at center:
        breathe
    ka "Then I suggest you try on a speedo from our new Super-Line."
    mc "Alright! Oh, hang on, we didn't come here for that."
    hide clerk01
    show clerk02
    with fastdissolve
    show clerk02 at center:
        breathe
    ka "What a shame..."
ag "It's for me actually. I would like a costume that... fits my curves. * blush *"
hide clerk02
show clerk03
with fastdissolve
ka "You? We do not cater to PRETEND superheroes here, this is a serious establishment!"
mc "She's for real! Audit Girl is her superhero name, so find something for her or I'll have Captain MILF revoke your exclusive selling rights!"
hide clerk03
show clerk04
with fastdissolve
ka "Oh, I'm so sorry sir, I didn't expect... My deepest apologies, Audit... Girl."
hide clerk04
show clerk05
with fastdissolve
ka "Please follow me to the superhero dressing room."
scene lingeriestore01 with dissolve
ag "Thank you [name] for defending my... superhero status, which I'm not sure I deserve."
mc "Oh, you DESERVE it, Kayla. And after tonight, you'll have a new SUPERHERO COSTUME for all to see and RESPECT you!"
scene lingeriestore02 with dissolve
ka "This way if you please Ms Audit Girl. And Mr [hero], sir."
scene lingeriestore03 with dissolve
ka "Please take off your... auditing garments Ms Audit Girl, so I can take your measurements."
ag "But... In front of [hero]?"
ka "He's a superhero madam, I'm sure he has seen his share of... women."
mc "I'm here to help, Kayla!"
ag "Oh. Uhm, okay. I'll get down to my... undies."
mc "That's a good girl."
scene lingeriestore04a with fade
ag "Do you think you'll be... able to find a costume for me... I have such a fat rump..."
ka "We... don't have many superheroines with your measurements, but I'm sure we'll find something."
mc "Relax, Kayla! Just let her take your measurements so you'll get a costume with a perfect fit for... those curves of yours."
if mcsenses >= 1:
    call screen usepower("usesenses", "AuditLingerieNoSenses", "AuditLingerieSenses") with dissolve

label AuditLingerieNoSenses:
scene lingeriestore05b with dissolve
jump AuditLingerieSensesNext
    
label AuditLingerieSenses:
scene lingeriestore04b with dissolve
$ usedsensesauditlingerie = True
mc "* Fuck yeah, that's better...*"
scene lingeriestore05a with dissolve

label AuditLingerieSensesNext:
ka "I think I have a few items in store for you to try on. Costumes that I'm sure Mr [hero] will appreciate."
mc "Ooooh, I can't wait!"
ag "Uh, alright. I... will be in the changing room."
mc "And I'll be right here waiting for you."

scene lingeriestoretrybackground blurred
show clerk02 at center:
    breathe
with dissolve
ka "This won't take a moment sir. Ms Audit Girl is trying on the first costume I found for her... size."
window hide
pause
hide clerk02
show clerk01
with fastdissolve
show clerk01 at center:
    breathe
ka "Still not interested in a pair of MEGA-sized superhero briefs for your great big fat young cock, sir?"
mc "Err, not at this stage, thanks. For asking."
hide clerk01
show clerk05
with fastdissolve
ka "Oh, there she comes. I will let her pose with this fine costume in front of a connoisseur such as yourself, sir."
scene lingeriestoretrybackground02 blurred
show auditcostume01a at centerright with slowmoveinright
ka "This patriotic costume is designed to remind everyone that..err... Audit Girl...here... is a true defender of the American Way of Life!"
hide auditcostume01a
show auditcostume01b
with dissolve
ag "And of the proper format of auditing documents."
mc "That's a selling point. Let's have a closer and longer examination here..."
scene lingeriestoretrybackgroundlarge blurred:
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume01c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "What do you think of this costume then [name]?"
mc "I'm still pondering... Turn round."
scene lingeriestoretrybackground02 blurred
show auditcostume01d
with dissolve
ag "I don't like it so much. I can feel my fat booty just wiggling around in it, it seems too loose..."

scene lingeriestoretrybackground02 blurred:
    zoom 1.5 xpos -0.2 ypos -0.4
show auditcostume01e
with dissolve
mc "Yes, I see clearer now... Indeed... Uhm. Let's have a look at the next costume before making any rash decision."
ka "Of course sir, I will bring it at once."
scene lingeriestoretrybackground blurred
show clerk01 at center:
    breathe
with fade
ka "Are you comfortable, [hero]?"
mc "Yes, why are you asking?"
window hide
pause
hide clerk01
show clerk02
with fastdissolve
show clerk02 at center:
    breathe
ka "I meant comfortable down there with your enormous dong stretching that poor thong of yours? Maybe a new super-stretchy pair of..."
mc "I'm here for Audit Girl, thank you very much. Is she ready yet?"
hide clerk02
show clerk05
with fastdissolve
ka "She is now. Please think of my offer while you admire this anime-themed costume which I hope will be to your liking. It's only 699 dollars."
scene lingeriestoretrybackground02 blurred
show auditcostume02a with slowmoveinright 
mc "Now that's a VERY interesting costume..."
ag "You... really think so?"
ka "High-quality Japanese import, sir!"
hide auditcostume02a
show auditcostume02b
with dissolve
ag "It's... a bit heavy though with those armor pads... And it barely covers my butt!"
mc "Ooh, really? Turn around then, let's have a look at this serious issue..."
scene lingeriestoretrybackgroundlarge blurred:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume02c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "Can you see? My fat glutes are just spilling all over the place! It's too LEWD!"
mc "Well, let's not get carried away here, I think it's..."
scene lingeriestoretrybackground02 blurred
show auditcostume02d
with dissolve
ag "Oh no, it's making me do weird poses against my will!"
mc "What are you talking about, this is a perfectly normal anime superhero pose..."
hide auditcostume02d
show auditcostume02e
with dissolve
ag "Look, I'm so silly! Please take it off, I can't control myself!"
ka "Err, I'll help you take it off Ms Audit Girl, don't panick. I'm going to have a strong word with the Japanese manufacturer after this..."
hide auditcostume02e with slowmoveoutright
mc "What a bummer."

scene lingeriestoretrybackground blurred
show clerk01 at center:
    breathe
with dissolve
ka "She will now try the last item I found that would fit her... ample figure."
mc "Good. I don't have all evening."
window hide
pause
hide clerk01
show clerk02
with fastdissolve
show clerk02 at center:
    breathe
ka "We do however have MANY pairs of XXXL-sized speedos and thongs that would perfectly suit a strapping young man with a giant monsterco..."
mc "Enough, jeez! I'll come back another day to try on your \"items\", how's that?"
hide clerk02
show clerk01
with fastdissolve
show clerk01 at center:
    breathe
ka "That would make me very happy indeed, Mister [hero]."
hide clerk01
show clerk05
with fastdissolve
ka "Ah, Ms Audit Girl is coming out of the changing room, I will leave her costume to your exquisite appreciation."

scene lingeriestoretrybackground02 blurred
show auditcostume03a at centerright with slowmoveinright
ag "I quite like this one, what do you think?"
mc "Ooh, it certainly looks high-tech!"
hide auditcostume03a
show auditcostume03b
with dissolve
ag "I feel... more confident and fiercer in it! Like I could take on some really nasty Super-Villains who failed to file their IRS forms in time!"
mc "Err, okay."
scene lingeriestoretrybackgroundlarge blurred:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
show auditcostume03c:
    subpixel True
    ypos -1.0
    linear 8.0 ypos 0.0
$ renpy.pause(4.0, hard='True')
ag "And it's not TOO lewd. Just enough to distract my ENEMIES while I audit their books and send them to jail for 20 years per count of tax fraud!"
window hide
scene lingeriestoretrybackground02 blurred:
    zoom 2.0 xpos -0.3 ypos -0.6
show auditasswigglevideo
pause
mc "Sure, whatever you say. Keep wiggling that ass for me."
scene lingeriestoretrybackground02 blurred
show auditcostume03d
with dissolve
ag "You don't seem to believe me but this is how ALL EVIL CRIMINALS go down eventually!"
mc "In that case, I know a guy from New York, who's now moved to Florida and..."
scene lingeriestoretrybackground02 blurred:
    zoom 1.5 xpos -0.2 ypos -0.1
show auditcostume03e
with dissolve
ag "Please tell me we're going to buy it, for real!"
mc "Yes of course, we're the Cockham League of Justice and we're LOADED!"
ag "Thank you so much [name]!"
ka "I will pack it up and I will also throw in a free jacket. The Cockham League of Justice being our finest customers." 
ag "I'm sssooo happy!"

scene lingeriebackground blurred
show clerk01 at center:
    breathe
with dissolve
ka "That will be 999 dollars, sir."
mc "What? Err, can you put it on the credit card account of the Cockham League of Justice please."
hide clerk01
show clerk03
with fastdissolve
ka "Credit what???"
mc "Shit, I forgot it was the 70s. Or the 80s. Before credit cards and mobile phones anyway."
hide clerk03
show clerk01
with fastdissolve
show clerk01 at center:
    breathe
ag "Let me do it, I'll write a Cockham Express cheque, then I'll deduct the costs in our next quarterly account filing under provision D-456-B that stipulates that work-related expenses can be claimed for..."
mc "Oh God, I'm bored."
hide clerk01
show clerk04
with fastdissolve
ka "I'll give it to you for free if you please stop talking! On the house, on the house, goodbye!"
ag "... Sorry, auditing is... boring. Just like me."
mc "Let's... just get out of here. Thank you for your time, Kate."
hide clerk04
show clerk01
with fastdissolve
show clerk01 at center:
    breathe
ka "Please remember to come back for those \"items\" I mentioned. Without her preferably."
stop channel1
play sound "sounds/achievement.mp3"
show questauditcostume at poslocation
$ renpy.pause(0.5, hard='True')
show winicon at poswin
pause
$ loclingerie = True
stop sound
stop music
jump Main

label HarleyStoreSecond:
scene lingeriebackground with fade
play music "sounds/storemusic.mp3"
mc "Hope that busty store manager is going to be there..."
window hide
$ renpy.pause(2.0, hard='True')
mc "Uh oh, not around again. Meaning the crazies are back!"
scene harleystore02 with dissolve
if mcsenses >= 2:
    mc "As I suspected, the Joker is here. But this time, I have Super-Senses level 02!"
if mcsenses <= 1:
    mc "And I still haven't levelled up in Super-Senses. I should really try and meet up with Wonder Woman in the gym for that."
    jump Main
scene harleystore03a with dissolve
mc "And this time, I 'll make sure to USE them."
scene harleystore03b with dissolve
mc "There, that's better, I can see through the wall now. And Harley Quiff is here again too! Let me squint my eyes a bit more to see EVEN CLEARER. Like I'm in the room."
jump HarleyStoreMid

label HarleyStore:
$ seenharleystorefirst = True
scene lingeriebackground with fade
play music "sounds/storemusic.mp3"
mc "Hope that busty store manager is going to be there..."
window hide
$ renpy.pause(2.0, hard='True')
mc "Well? Hello? Pff, you just can't get good cervyx these days. Or maybe she's already dealing wih a customer, let's find out cos I'm nosy like that."
scene harleystore01 with dissolve
mc "Hang on, what's going on here? I recognized that ugly clown face. It's the Joker!"
scene harleystore02 with dissolve
mc "Let's hide and see what he's up to. The store manager seems to have her hands bound, something's definitely fishy!"
scene harleystore03a with dissolve
mc "I should use my Super-Senses to see through this thick wall."
call screen usepower("usesenses", "StoreNoSenses", "StoreSenses") with dissolve
label StoreNoSenses:
mc "Damn it, I didn't use my powers fast enough cos I have a sadistic player controlling me, I can't see anything!"
mc "Therefore, I shall confront the Joker and rid this town of this perverted filth once and for all!"
label HarleyStoreFirstConfront:
scene harleystore28b with dissolve
stop music
play music "sounds/dark.mp3"
mc "Drop it Harley! And that gun!"
hq "What a party-pooper, boo-hoo!"
scene harleystore29 with dissolve
jo "What, you mean my gun? The one pointed right at your head?"
mc "Err... How did you...?"
scene harleystore30 with dissolve
jo "You're not the only one with Super-Senses, [hero]! I KNEW you were hiding behind that door. Now the Joker's on you!"
hq "Don't you just love the CRAZINESS of it all!"
scene harleystore31 with dissolve
jo "I could kill you. But where would be the fun in that?"
mc "Y.. yes, you're right, it would be... no fun at all. Especially for me."
scene harleystore30 with dissolve
jo "Harley, let's take a hike, I have BIGGER plans for this BOY. Ha ha ha!"
hq "But I wanted something SEXY!"
scene harleystore50 with dissolve
jo "Then we'll come back. When the place is more quiet!"
mc "Yes, great idea, I won't be around again ever, I promise!"
scene harleystore51 with dissolve
hq "But why, I like seeing you around, and hearing your voices in my head, puddin'! Tell them Harley said hi!"
mc "Err... sure."
scene harleystore52 with dissolve
stop music
ka "Thank you [hero], you saved my life, God knows what they would have done to me. Can you please untie me?"
call Good from _call_Good_6
$ renpy.pause(2.0, hard='True')
scene harleystore53 with dissolve
mc "Still, I can't help but feel I kind of failed in that I didn't get to see what they would have done to you because my Super-Senses aren't high enough..."
mc "Perhaps I should come back, once I manage to RAISE THEM HIGHER. At least to Level 02 that is."
jump Main

label StoreSenses:
if mcsenses <= 1:
    mc "Damn it, my Super-Senses are not high enough, I can't see anything!"
    mc "Therefore, I shall confront the Joker and rid this town of this perverted filth once and for all!" 
    jump HarleyStoreFirstConfront
scene harleystore03b with dissolve
$ usedsenses += 1
mc "Yes, I'm starting to see more clearly... Harley Quiff is there too! Let me squint my eyes a bit more to see EVEN CLEARER. Like I'm in the room."
label HarleyStoreMid:
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
    xpos 0.0
    linear 3.0 xpos -0.1
with dissolve
mc "Alright! Let's wait for her to pose in that fishnet bodysuit..."
scene harleystore09 :
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
$ harleypicture = True
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

label KateAnalSlow:
$ kateanalfast = False
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
if kateanalslow == False:
    $ kateanalslow = True
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
call screen kateanalslow()
screen kateanalslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalBackSlow")

label KateAnalFast:
$ kateanalslow = False
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
if kateanalfast == False:
    $ kateanalfast = True    
    ka "Oooh yeah, POUND MY HORNY ASS with your giant cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show backicon:
     xpos 50 ypos 500    
call screen kateanalfast()
screen kateanalfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalBackFast")

label KateAnalBackSlow:
$ kateanalfast = False
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
if kateanalslow == False:
    $ kateanalslow = True
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
call screen kateanalbackfuckslow()
screen kateanalbackfuckslow():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalBackFast")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalSlow")

label KateAnalBackFast:
$ kateanalslow = False
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
if kateanalfast == False:
    $ kateanalfast = True    
    ka "Oooh yeah, POUND MY HORNY ASS with your giant cock!"
window hide
show cum:
    xpos 1750 ypos 1020    
show slower:
     xpos 1700 ypos 500    
show sceneicon:
     xpos 50 ypos 500    
call screen kateanalbackfuckfast()
screen kateanalbackfuckfast():
    modal True
    button:
        xpos 1700
        ypos 500
        xysize(180, 60)        
        action Jump ("KateAnalBackSlow")
    button:
        xpos 1750
        ypos 1020
        xysize(120, 60)        
        action Jump ("KateAnalEnd")
    button:
        xpos 50
        ypos 500
        xysize(120, 60)        
        action Jump ("KateAnalFast")

label KateAnalEnd:
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

if inventorygoldtrunks :
    ka "Thank you. Thank you so much for destroying and ruining my backdoor..."
    mc "All in a day's work for a superhero, ma'am!"

if inventorygoldtrunks == False:
    ka "To thank you for this amazing assfuck, I'm offering you these gold-plated trunks that should protect your... dong in the face of danger."
    window hide
    $ inventorygoldtrunks = True
    play sound "sounds/achievement.mp3"
    show acquiredgoldtrunks at poslocation
    $ renpy.pause(0.5, hard='True')
    pause
    mc "Finally! I forgot to get it before levelling up, now I can confront Poison Ivy!"
mc "Better get going, I need to find out what these two dastardly villains are up to!"
jump Main