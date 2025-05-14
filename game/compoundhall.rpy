label CompoundHallDay:
stop music
$ seenhall = True

if d10locday >= 7 and d10locday <= 8:
    jump CompoundHallMILF
if d10locday == 9 or d10locday == 10:
    jump CompoundHallDayChoose

play channel1 "sounds/piano01.mp3"
scene compoundhalldaychoose with fade
mc "Nobody's around. I could play the piano but I'm level 0 in Super-Piano, so..."
stop channel1
jump MainTime

label CompoundHallDayChoose:
play channel1 "sounds/piano01.mp3"
scene compoundhalldaychoose
call screen hallcompoundday()
screen hallcompoundday():
    modal True    
    add "icons/returnicon.png"
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action Jump ("MainTime")
    imagebutton:
        focus_mask True
        idle "v01/hallauditdayidle.png"
        hover "v01/hallauditdayhover.png"
        action Jump ("CompoundHallAudit")
    imagebutton:
        focus_mask True
        idle "v01/hallmilfdayidle.png"
        hover "v01/hallmilfdayhover.png"
        action Jump ("CompoundHallMILF")
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

label CompoundHallMILF:
stop channel1
if mission02win and milftoldmission02end == False:
    $ milftoldmission02end = True
    scene compoundhall01d
    show compoundmilf01
    with fade
    mc "So, How is Sexy Luthor doing in Arkham? Where she ended up thanks to my quick Super-hero reactions."
    hide compoundmilf01
    show compoundmilf05
    with fastdissolve
    cm "I'm afraid she actually escaped last night..."
    mc "I KNEW this mission was totally lame and she would escape anyway!"
    hide compoundmilf05
    show compoundmilf02
    with fastdissolve
    cm "Don't say that, every successful mission brings us closer to eradicating the Super-Villain scum from this city."
    mc "It doesn't feel like it right now is all I'm saying..."
    hide compoundmilf02
    show compoundmilf04
    with fastdissolve
    cm "I'm sure Superman will capture her again. And THIS time..."
    mc "She won't escape?"
    cm "That's right. She WON'T. Trust your League Captain, [name]."
    mc "Fine, Captain MILF."
    hide compoundmilf04
    show compoundmilf06
    with fastdissolve
    cm" Now I have to go and talk to Superman. He's back from the North Pole and I must tell him he has to start all over again..."
    mc "The story of his life really. I'll be going too, I'd rather not be there where he learns what happened..."
    jump Main
if mission02fail and milftoldmission02end == False:
    $ milftoldmission02end = True
    scene compoundhall01d
    show compoundmilf02
    with fade
    cm "Ah, there you are. I heard about your dismal performance at the CCPD. You let Sexy Luthor escape."
    mc "She would have escaped anyway. Come on, everyone knows that!"
    hide compoundmilf02
    show compoundmilf05
    with fastdissolve
    cm "That's not the point, [name]! You FAILED in a mission assigned to you. Your progress towards Iconic Super-Hero status is already compromised."
    mc "Iconic Super-Hero status? What's that, I was never briefed on that!"
    hide compoundmilf05
    show compoundmilf06
    with fastdissolve
    cm "Too bad. Next time, make the RIGHT choices. If you ever want to follow that path again."
    mc "It doesn't seem fair. Not fair at all. I'm going back my room to sulk."
    hide compoundmilf06
    show compoundmilf02
    with fastdissolve
    cm "Yeah, you do that, [name]."
    jump Main
if mission04 and mission04end == False:
    scene compoundhall01d
    show compoundmilf02
    with fade
    cm "How is your CCPD mission going? Have you probed DEEP into it yet?"
    mc "Err... Not yet. I'm stumped, to be honest."
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve
    cm "Well, why don't you check the mission hints?"
    mc "I don't like cheating! I'll solve this case on my own!"
    hide compoundmilf06
    show compoundmilf01
    with fastdissolve
    cm "Sure, honeypot. But you don't have much time left..."
    jump Main
if mission04 and mission04end and mission04win == False and toldmilfmission04 == False:
    $ toldmilfmission04 = True
    scene compoundhall01d
    show compoundmilf04
    with fade
    cm "Congratulations on solving this CCPD case, [name]!"
    mc "What? Did I?"
    hide compoundmilf04
    show compoundmilf06
    with fastdissolve
    cm "Well, yeah, there is no longer any influx of patients coming into Cockham Grand Hospital with... traumatic... * cough * injuries."
    mc "Oh. I didn't know that. I can't remember solving the case to be honest, Carol."
    hide compoundmilf06
    show compoundmilf05
    with fastdissolve
    cm "You must have been distracted. Or you have early Alzheimer... You should go back to the CCPD for debriefing. And to your room for a rest."
    $ mission04win = True
    jump Main
if mission04 and mission04end and mission04win and toldmilfmission04 == False:
    $ toldmilfmission04 = True
    scene compoundhall01d
    show compoundmilf04
    with fade
    cm "Congratulations on solving this CCPD case, [name]!"
    mc "Yeah, it was a piece of cake for a superhero like ME!"
    hide compoundmilf04
    show compoundmilf06
    with fastdissolve
    cm "And how did you do it exactly, I'm curious."
    mc "Well, err, I used my SUPERPOWERS and I, err... defeated the Super-villains responsible for this depravity."
    hide compoundmilf06
    show compoundmilf05
    with fastdissolve
    cm "Which Super-Villains would that be?"
    mc "Well, you know, the usual suspects... The Joker and err... That guy in the Narrows and..."
    hide compoundmilf05
    show compoundmilf02
    with fastdissolve
    cm "That's strange, they never collaborated in the past... But nevertheless, you made the Cockham League of Justice proud! And your landlady proud too... Go back to your room, you deserve a rest today."
    jump Main

if mission05 and mission05end and mission05win and toldmilfmission05 == False:
    $ toldmilfmission05 = True
    scene compoundhall01d
    show compoundmilf04
    with fade
    cm "Well done, [name]! Natasha is back to being her normal grumpy self!"
    mc "Do I get a reward for that?"
    hide compoundmilf04
    show compoundmilf02
    with fastdissolve
    cm "Your reward is my gratitude. That should be sufficient. She also told me she might show YOU her gratitude if you visit her in her room at night."
    mc "Alright, now we're talking!"
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve
    cm "I really don't see why you're so excited about this. Do you think her gratitude will be better than mine?"
    mc "Err..."
    jump Main    

if mclevel02 and supergirlgone == False:
    play channel1 "sounds/piano01.mp3"
    $ supergirlgone = True
    scene compoundhall01d
    show compoundmilf02 at right
    with fade
    cm "Supergirl's training internship is over. And she will be leaving us to go back to Smallcoxville."
    window hide
    show sgirl04 at left with moveinleft
    mc "But why? We were going on so well. All THREE OF US."
    hide sgirl04
    show sgirl02 at left
    with fastdissolve
    sg "Is that how you call it? Raping me, getting my hopes high and then tearing them apart."
    hide compoundmilf02
    show compoundmilf03 at right
    with fastdissolve    
    cm "You entered my machine without consulting with me. That was YOUR fault, Linda."    
    hide sgirl02
    show sgirl04 at left
    with fastdissolve
    sg "I know, Captain MILF. Still, I can't help but dream about what could have been... * sigh *"    
    mc "Same here. I'll probably dream about it in my jacuzzi actually."
    hide sgirl04
    show sgirl02 at left
    with fastdissolve
    sg "I don't want to know. Anyway, I came to say goodbye, very very distant cousin [name]."
    mc "Have a safe flight back, Linda. Are you flying Pan Am?"
    hide compoundmilf03
    show compoundmilf04 at right
    with fastdissolve    
    cm "Supergirl has a cape, she can fly all my herself. Unlike you, [name]."
    mc "Yeah, thanks for reminding me. Bye, Linda, it was great meeting you, hopefully we'll meet again!"
    hide sgirl02
    show sgirl03 at left
    with fastdissolve    
    sg "And hopefully, you won't rape me with your great big whopper this time."
    window hide
    hide sgirl03 with moveoutleft
    stop channel1
    jump Main

if quest07 == False and mission06end and wondertalkpregnant:
    play channel1 "sounds/piano01.mp3"
    scene compoundhall01d
    show compoundmilf02
    with fade
    cm "I have a... delicate quest for you, [name]."
    mc "Delicate? That sounds girly."
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve    
    cm "I mean delicate because it forces me to admit you might have been right."    
    mc "About what?"
    hide compoundmilf06
    show compoundmilf05
    with fastdissolve    
    cm "I haven't been able to get those nazi henchwomen to talk. Even Wonder Woman's Lasso of Truth hasn't worked. Their minds are so...fanatical!"
    mc "Are you asking me to use the interrogation method I suggested on them, Captain MILF?"
    hide compoundmilf05
    show compoundmilf04
    with fastdissolve    
    cm "Err, yes. Do what you have to do."
    mc "Even if it means using my big fat TRUNCHEON and mercilessly POUNDING their..."
    hide compoundmilf04
    show compoundmilf02
    with fastdissolve    
    cm "I DON'T WANT TO KNOW HOW YOU DO IT! Just do it. Report back to me with valuable intel about Colonel Stroheim. Hopefully..."
    window hide
    play sound "sounds/achievement.mp3"
    $ quest07 = True
    show quest07icon at poslocation
    $ renpy.pause(0.5, hard=True)
    show textquest07 at posmissiontext
    pause                        
    mc "It will be done! My TRUNCHEON OF TRUTH never fails ME!"
    stop channel1 fadeout 1.0
    jump InterrogationRoom

if mission06end and quest07end and mission07 == False and mission07win == False and harleypicture:
    play channel1 "sounds/piano01.mp3"
    scene compoundhall01d
    show compoundmilf01
    with fade
    cm "I have an URGENT mission for you [hero]!"
    mc "Ooh? I'm always READY for missions and quests!"
    hide compoundmilf01
    show compoundmilf02
    with fastdissolve    
    cm "Something is coming down at the Sirens Club tonight. I don't know what exactly, but it will be MAJOR. So you have to be there to find out."    
    hide compoundmilf02
    show compoundmilf05
    with fastdissolve    
    cm "And I even managed to find you a waiting job there tonight! It was surprisingly easy, like they WANTED you to come..."
    mc "Err... Barbaara Keen is just recognizing my great... waiting skills."
    window hide
    play sound "sounds/achievement.mp3"
    $ mission07 = True
    show mission07icon at poslocation
    $ renpy.pause(0.5, hard=True)
    show textmission07 at posmissiontext
    pause
    hide compoundmilf05
    show compoundmilf04
    with fastdissolve    
    cm "So get going, and don't spill a drop, it's a high-society event! Be on the lookout for anything suspicious..."
    jump SirensParty

if mission07win and spokemilfmission07 == False:
    $ spokemilfmission07 = True
    play channel1 "sounds/piano01.mp3"
    scene compoundhall01d
    show compoundmilf01
    with fade
    cm "Ah, there your are!"
    mc "Here I am, since here I chose to come."
    hide compoundmilf01
    show compoundmilf04
    with fastdissolve    
    cm "I heard you managed to stop Barbara Keen from using that evil dagger of hers. Well done, my sweet HERO tenant. Your landlady is so PROUD of you!"    
    hide compoundmilf04
    show compoundmilf02
    with fastdissolve    
    cm "But you accused Batman of violent assault against... Harley Quiff. He bankrolls the League, may I remind you..."
    mc "Yeah, well, he DID assault her. Plus, he's a filthy pervert."
    hide compoundmilf02
    show compoundmilf06
    with fastdissolve    
    cm "Sometimes, Super-Heroes are allowed little white lies. To protect their own. Such as Batman, even if he is a filthy perv. Do you get it?"
    mc "* Sighs * Alright, sorry Captain MILF, won't happen again."
    jump Main

if period == 0:
    scene compoundhall01d
    show compoundmilf01
    with fade
    cm "Did you come to ask if I had a mission for you, [name]?"
if period == 1:
    scene compoundhall01n
    show compoundmilf01
    with fade
    cm "Hello, [name]."
label CompoundHallMilfDialoguesDay:
menu:
    "That's right. I'm READY to FIGHT!" if period == 0 and mission01end:
        if mission03end:
            hide compoundmilf01
            show compoundmilf02
            with fastdissolve
            cm "Unfortunately, you'll have to wait. No major sex crime has been reported today."
            mc "Super-Villains in this town are just LAME!"
            hide compoundmilf02
            show compoundmilf04
            with fastdissolve
            cm "Don't say that, Cockham City is BETTER without SEX CRIMES!"
            mc "I suppose so..."
            hide compoundmilf04
            show compoundmilf01
            with fastdissolve
            jump CompoundHallMilfDialoguesDay
        if mission02 == False and milftoldmission02end == False:
            hide compoundmilf01
            show compoundmilf04
            with fastdissolve
            cm "Good. Because I HAVE a mission for you!"
            mc "Yeah! Who do I need to fuck into submission?"
            hide compoundmilf04
            show compoundmilf06
            with fastdissolve
            cm "That's NOT how it works, [name]. Especially in THIS MISSION."
            hide compoundmilf06
            show compoundmilf02
            with fastdissolve
            cm "Superman has captured Sexy Luthor again!"
            mc "Well, woo-hoo. So she's going to escape. Again."
            hide compoundmilf02
            show compoundmilf01
            with fastdissolve
            cm "Not this time, because YOU will be guarding her! Since we can't trust the CCPD guards."            
            mc "That sounds like a MENIAL job unbefitting of my SUPERHERO status. Why don't they just use a FEMALE guard?"
            hide compoundmilf01
            show compoundmilf05
            with fastdissolve
            cm "They did. But she also seduced them. She's a bisexual."
            mc "Okay. Why doesn't Superman GUARD HER then? Since he doesn't even have a dick, she can't seduce HIM!"
            hide compoundmilf05
            show compoundmilf02
            with fastdissolve
            cm "I agree this would make the most sense. Unfortunately, every time he captures her, he immediately goes on holidays to the North Pole. So there's only YOU left to do this job."            
            mc "And what if she seduces ME?"
            cm "That's a risk I'm willing to take. All the other superheroes are busy anyway. You're the novice and that's your mission, understood?"
            mc "* sigh * I suppose so... Captain MILF."
            hide compoundmilf02
            show compoundmilf01
            with fastdissolve
            cm "Now off you go. Just stand OUTSIDE her cell, she can't use her superpowers on you as long as you stay OUT OF HER CELL."
            mc "Roger that."
            window hide
            play sound "sounds/achievement.mp3"
            $ mission02 = True
            show missionicon02 at poslocation
            $ renpy.pause(0.5, hard=True)
            show textmission02 at posmissiontext
            pause                        
            jump Mission02
        if milftoldmission02end and mission03 == False:
            hide compoundmilf01
            show compoundmilf04
            with fastdissolve
            cm "And fight you shall! With ME this time."
            mc "Yeah! Who are we beating the shit out of?"
            hide compoundmilf04
            show compoundmilf06
            with fastdissolve
            cm "Nobody for the moment. We'll only be INVESTIGATING. A sensitive matter that involves the Mayor who just called me."
            mc "Mayor Krass? A lot of people say he's corrupt, why should I care about him?"
            hide compoundmilf06
            show compoundmilf02
            with fastdissolve
            cm "He's THE Mayor nevertheless. And we need his support to stay afloat. You apparently haven't seen our balance sheet lately. Let's go, he's waiting for us, [name]."
            $ mission03 = True
            jump Mission03
        if milftoldmission02end and mission03 and mission03end == False:
            hide compoundmilf01
            show compoundmilf02
            with fastdissolve
            cm "How about your finish your CURRENT mission first."
            mc "I don't like that mission, it's boring."
            hide compoundmilf02
            show compoundmilf06
            with fastdissolve
            cm "I'm not giving you any more assignment until you COMPLETE YOUR MISSION!"
            mc "Alright... * sigh* "
            hide compoundmilf06
            show compoundmilf01
            with fastdissolve
            jump CompoundHallMilfDialoguesDay
    "I was wondering where one could find a costume for Audit Girl." if knowlingerie == False:
        $ knowlingerie = True
        hide compoundmilf01
        show compoundmilf02
        with fastdissolve
        cm "But, she's just an intern. Why would she need a costume?"
        mc "She's still a SUPER-HERO! And superheroes have a costume, otherwise, they don't look like superheroes. And it gets confusing."
        hide compoundmilf02
        show compoundmilf06
        with fastdissolve
        cm "I suppose so... Well, there is a store downtown that has exclusive rights to sell superhero costumes... Whether they have HER size..."
        play sound "sounds/skill.mp3"
        show auditquestcostumeprogress01 at poslocation
        $ renpy.pause(0.5, hard='True')
        mc "Great, I'll take her there then!"
        hide compoundmilf06
        show compoundmilf05
        with fastdissolve
        hide auditquestcostumeprogress01
        cm "Just don't spend too much money on her. She's JUST an intern, sweetie."
        mc "Sure, Carol."
        hide compoundmilf05
        show compoundmilf01
        with fastdissolve
        jump CompoundHallMilfDialoguesDay
    "I'd like to see that giant Cockham map again.":
        hide compoundmilf01
        show compoundmilf04
        with fastdissolve
        cm "Don't we all!"
        scene hallwallformap01 with dissolve
        cm "And there it is. A giant Cock...ham map."
        scene hallwallformap02 with dissolve
        cm "Was there anything specific you wanted to know about it?"
        mc "Not really. I just wanted to hear you say \"Giant Cock\"."
        cm "That's very puerile. I'm busy, so go and do something useful. With your giant cock."
        jump Main
    "I was raped by Harley Quiff. Anally raped." if sawharley and toldmilfharley == False:
        $ toldmilfharley = True
        hide compoundmilf01
        show compoundmilf05
        with fastdissolve
        cm "What? You mean... You took it up the ass?"
        mc "No! She forced my dick up HER ass! And drained my nuts. I must have come, like, a gallon."
        hide compoundmilf05
        show compoundmilf06
        with fastdissolve
        cm "Oh, that's terrible, my sweet little pumpkin. Did you arrest her then?"
        mc "No... I failed miserably..."
        hide compoundmilf06
        show compoundmilf02
        with fastdissolve
        cm "That's not very impressive any longer. You're a disappointing tenant, [name]. I gave you these huge muscles to be able to ARREST Super-Villains!"
        mc "Her Super-Seduction powers are just too strong for me at this stage. I need MORE superpower!"
        cm "Therefore, you need to train and reach level 2 SUPERHERO!"
        mc "But I can't yet."
        hide compoundmilf02
        show compoundmilf04
        with fastdissolve
        if period == 1:
            cm "The time will come, the time will come, sweetie. Goodnight, [name]."
        if period == 0:
            cm "The time will come, the time will come, sweetie. Go back to your room, your landlady has a lot of paperword to do."
        jump Main
    "Emma Frost told me the truth." if frosttoldmc and toldmilffrost == False:
        $ toldmilffrost = True
        hide compoundmilf01
        show compoundmilf05
        with fastdissolve
        cm "What lying truth would that be?"
        mc "You don't own this place fully and half of my rent goes to her!"
        hide compoundmilf05
        show compoundmilf07
        with fastdissolve
        cm "Well, err, these details are best kept between homeowners, sweetie. As a tenant, you have no say in these matters."
        mc "That's not fair! Tenants have rights! Tenants have rights!"
        hide compoundmilf07
        show compoundmilf02
        with fastdissolve
        cm "Sure you do. You pay your rent on time, and nothing will happen to you... Emma Frost is a really tough landlord, I'm warning you..."
        mc "Good thing money ain't even a stat so nobody can actually see how totally broke I am."
        hide compoundmilf02
        show compoundmilf01
        with fastdissolve
        if period == 1:
            cm "Sleep tight, [name]. In your bed. Partly owned by Emma Frost and myself."
        if period == 0:
            cm "Sleep tight, [name]. In your bed. Partly owned by Emma Frost and myself."
        jump Main
    "I saw She-Hulk tied up. IN OUR COMPOUND." if questhulk and questhulkcompleted == False and spokemilfshehulk == False:
        $ spokemilfshehulk = True
        hide compoundmilf01
        show compoundmilf02
        with fastdissolve
        cm "Ah... Err... We had to... restrain her, under the Mayor's orders!"
        mc "And why is that?"
        hide compoundmilf02
        show compoundmilf05
        with fastdissolve        
        cm "She was causing millions of dollars of public property damage every time she went on a mission!"
        hide compoundmilf05
        show compoundmilf06
        with fastdissolve        
        cm "I'm sorry I didn't tell you earlier, [name]. But there's nothing we can do for her at this stage."
        mc "I will convince the Mayor to release her from this humiliating predicament!"
        hide compoundmilf06
        show compoundmilf02
        with fastdissolve
        cm "Well, good luck with that..." 
        mc "Oh, and Batman was also down there. Jerking off like a dirty old pervert."
        hide compoundmilf02
        show compoundmilf05
        with fastdissolve        
        cm "Hum... That is indeed disgusting. But..."
        mc "Yeah, yeah, he bankrolls the League so you'll just swipe it under the carpet, I get it!"
        hide compoundmilf05
        show compoundmilf01
        with fastdissolve                
        cm "If we weren't so broke, I would definitely DO SOMETHING ABOUT IT, you've got to believe me!"
        jump Main
    "Natasha insulted me and won't talk to me anymore. And I didn't even do anything to deserve it!" if premission05 and mission05 == False:
        hide compoundmilf01
        show compoundmilf05
        with fastdissolve
        cm "She also called me names the other day. Which I won't repeat here. She has changed lately. And not for the better!"
        mc "Something is definitely fishy. Someone should investigate what is going on with her."
        hide compoundmilf05
        show compoundmilf04
        with fastdissolve        
        cm "The League appreciates you volunteering for this delicate mission, my sweet tenant!"
        mc "Hey! I didn't say that!"
        hide compoundmilf04
        show compoundmilf06
        with fastdissolve
        cm "I already tried to follow her lately and I found out she always rides her Dodge downtown at high speeds. You must find out where she goes!"
        window hide
        play sound "sounds/achievement.mp3"
        $ mission05 = True
        show missionicon05 at poslocation
        $ renpy.pause(0.5, hard=True)
        show textmission05 at posmissiontext
        pause  
        mc "Oh, and I have only three days, right?"
        hide compoundmilf06
        show compoundmilf05
        with fastdissolve
        cm "Exactly. This is a MISSION, not a mere quest. So good luck, and God Speed!"
        mc "I'd better start following her around right NOW!"
        jump SovietEmbassy        
    "I'm done talking to you.":
        hide compoundmilf01
        show compoundmilf05
        with fastdissolve
        cm "That's a bit rude. But so be it, I'm done talking to YOU!"
        jump Main

label CompoundHallAudit:
stop channel1
scene allleaguechair
show auditeyeblink
with dissolve

label AGDialogueLeagueDay:
menu:
    "Hi Kayla." if period == 0:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        $ agspeak01 = True
        ag "Hi [name]! What a beautiful day, isn't it?"
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "Yeah, a day to go OUT and FIGHT Super-Villains!"
        scene allleaguechair
        show allleagueaudit02
        with fastdissolve
        ag "Y... Yes. But I don't think I'm quite ready yet. You go ahead. Without me."
        mc "Soon you'll be ready to come with ME! I promise."
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        ag "I hope so too!"
        jump AGDialogueLeagueDay
    "Hi Kayla." if period == 1:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        $ agspeak01 = True
        ag "Hi [name]! What a beautiful evening, isn't it?"
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "Yeah, an evening to go OUT and FIGHT Super-Villains!"
        scene allleaguechair
        show allleagueaudit02
        with fastdissolve
        ag "Y... Yes. But I don't think I'm quite ready yet. You go ahead. Without me."
        mc "Soon you'll be ready to come with ME! I promise."
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        ag "I hope so too!"
        jump AGDialogueLeagueDay        
    "What are your superpowers exactly?" if gotmassage == False:
        ag "I... I can do.... mental stuff real fast. Like auditing for example."
        mc "Ah. Interesting. I'm sure that'll come in handy one day."
        hide auditeyeblink
        show allleagueaudit03
        with fastdissolve
        ag "I... I hope so too."
        hide allleagueaudit03
        show allleagueaudit04
        with fastdissolve
        ag "I have healing powers too. Level 3. If you ever get... injured, I could try and help..."
        scene allleaguechair blurred:
            zoom 1.5 xpos -0.2 ypos -0.2
        show allleagueaudit04b
        with fastdissolve        
        mc "Now we're talking! Do you also do massages?"
        scene allleaguechair
        show allleagueaudit02
        with fastdissolve
        ag "Well, err... If that can help you..."
        mc "Maybe it will, maybe it will. We'll have to find out. *wink*"
        hide allleagueaudit02
        show auditeyeblink
        with fastdissolve
        jump AGDialogueLeagueDay
    "You seem to be very shy. Unusual for a superhero.":
        hide auditeyeblink
        show allleagueaudit02
        with fastdissolve
        ag "I... don't know if I belong here. I don't have much experience being a superheroine."
        mc "I'm sure you'll fit in, don't worry."
        hide allleagueaudit02
        show allleagueaudit04
        with fastdissolve
        ag "Thank you, ...[hero]."
        hide allleagueaudit04
        show auditeyeblink
        with fastdissolve
        jump AGDialogueLeagueDay
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
            ag "The massage room is not far away. I'll take you there!"
        jump AuditMassage
    "You're not wearing your costume?" if loclingerie:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "No, I'm not on any mission and I feel more comfortable in this outfit."
        hide allleagueaudit04
        show auditeyeblink
        with fastdissolve
        ag "It helps me concentrate..."
        jump AGDialogueLeagueDay
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
    "Maybe it's time you got out of this compound and join me in the fight against SUPER-VILLAINS!" if period == 1 and locmayors and knowlingerie and seenexcellalingerie == False:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "Yippee! And which super-Villains shall we fight TOGETHER?"
        mc "I was thinking about taking on the MAFIA!"
        hide allleagueaudit04
        show allleagueaudit05
        with fastdissolve        
        ag "That's a GREAT idea, [hero]! Did you know that Al Capone went down through tax fraud? We could ask to see their books and I'll be wearing my..."
        mc "I'll do the talking. You just watch and learn how a REAL hero behaves in the face of DANGER."
        hide allleagueaudit05
        show allleagueaudit03
        with fastdissolve
        ag "But... can I wear my costume at least?"
        mc "I suppose so. Go and get dressed and let's go."
        $ withag = True
        jump MafiaLair
    "It's late, I'm off to bed now..." if period == 1:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "I'll be off too. To my campbed in the cold library."
        jump Main
    "I'm talking and time is flying. Better get going." if period == 0:
        hide auditeyeblink
        show allleagueaudit04
        with fastdissolve
        ag "Yes, I need to move too. From here to the library most likely. Same scene with a different background."
        jump Main
        
label CompoundHallNight:
stop music
if d10locnight == 8 or d10locnight == 9:
    jump CompoundHallMILF

if d10locnight == 1 or d10locnight == 2:
    jump CompoundHallAudit

if d10locnight == 3 or d10locnight == 4:
    jump CompoundHallSuper

play channel1 "sounds/piano01.mp3"
scene compoundhallnightchoose with fade
mc "Nobody's around. I could play the piano but I'm level 0 in Super-Piano, so..."
stop channel1
jump MainTime

label CompoundHallSuper:
stop channel1

if choseevilphoto:
    scene allleaguedoor
    show allleaguesuper02 at centerleft
    with fade
    sm "You?"
    scene allleaguedoor blurred
    show supermanangryhall
    with dissolve
    sm "I distinctly remember telling you NOT TO CROSS MY PATH AGAIN!"
    mc "Okay, let's calm down a minute... I'll be going, was just passing by..."
    jump MCRoomNight

scene allleaguedoor
show allleaguesuper01 at centerleft with dissolve:
    breathe

label CompoundSMDialogue:
menu:
    "Yo buddy." if smspeak01 == False:
        $ smspeak01 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        sm "What do you want? We have NOTHING in common."
        mc "I feel like we have started off on the wrong footing..."
        sm "My footing is just fine. And I can fly out of here ANYTIME I WANT."
        mc "Oooh!... You've got an important date you need to fly to? No? No date on the horizon, Superman? What a shame."
        hide allleaguesuper02
        show allleaguesuper04 at centerleft
        with fastdissolve
        sm "I have a love interest for your information! Lois Pane, a reporter from the Cockham Planet. I work wih her. Undercover as Clark Kunt."
        mc "Why are you undercover anyway?"
        hide allleaguesuper04
        show allleaguesuper03 at centerleft
        with fastdissolve
        sm "That's a good question. I have no idea to be honest."
        hide allleaguesuper03
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        jump CompoundSMDialogue
    "What are your superpowers, Superman?" if smspeak02 == False and smspeak01:
        $ smspeak02 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        sm "Come on! I'm the most FAMOUS superhero. Everyone knows my amazing superpowers. My incredible Super-Strength, my Super-Flight, my Super-Combat ability, my Super-..."
        mc"Yeah, yeah, ok, I get it. I also know of your super-weakness. Of some little rock called \"kryptonite\"..."
        hide allleaguesuper02
        show allleaguesuper03 at centerleft
        with fastdissolve
        sm "Well, err... It's really rare anyway, so..."
        mc "Still. Someone might get his or her hands on some of that rock. And when they do, you'll turn into a pathetic underhero weakling."
        hide allleaguesuper03
        show allleaguesuper02 at centerleft
        with fastdissolve
        sm "And that has NEVER happened! Except once. But I was saved by... Captain MILF."
        mc "Interesting. Is that why you keep obeying her like a little poodle?"
        hide allleaguesuper02
        show allleaguesuper04 at centerleft
        with fastdissolve
        sm "She's OUR boss. Including YOURS. Don't forget that!"
        mc "Well, she's also my landlady so I have a... special relationship with her."
        hide allleaguesuper04
        show allleaguesuper01 at centerleft
        with fastdissolve
        sm "Within the guidelines set forth by the Patreon Bill passed by Congress last year?"
        mc "Err, yeah, of course. Totally within those guidelines."
        hide allleaguesuper01
        show allleaguesuper04 at centerleft
        with fastdissolve
        sm "Good, it would be embarrassing for me to have to ban you fron this game for doing something that goes against that Patreon Bill."
        mc "Err, yeah, sure, whatever."
        hide allleaguesuper04
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        jump CompoundSMDialogue
    "So Sexy Luthor keeps escaping, hey?" if smspeak03 == False and smspeak01:
        $ smspeak03 = True
        hide allleaguesuper01
        show allleaguesuper02 at centerleft
        with fastdissolve
        sm "The CCPD are USELESS! She just seduces the guard with her Super-Seduction powers and they let her out."
        mc "I bet you're IMMUNE to Super-Seduction. Having no dick and all that."
        hide allleaguesuper02
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        sm "Yes, I AM immune. I'm a REAL superhero and I'm here to CONCENTRATE on my job. Unlike you clearly."
        mc "I can concentrate. And use my monster cock at the same time. Unlike you clearly."
        sm "Umpf..."
        jump CompoundSMDialogue
    "Man, you should stop wearing eyeliner. It's for girls.":
        hide allleaguesuper01
        show allleaguesuper03 at centerleft
        with fastdissolve
        sm "It's not eyeliner, I just... keep burning all my eyelashes every time I use my super-laser eyes."
        mc "Yikes, that sucks. I'm glad I don't have this silly superpower."
        hide allleaguesuper03
        show allleaguesuper01 at centerleft
        with fastdissolve
        show allleaguesuper01 at centerleft:
            breathe
        sm "It's very useful to fight SUPER-VILLAINS. You'll learn the hard way I guess."
        jump CompoundSMDialogue
    "I'm done here.":
        hide allleaguesuper01
        show allleaguesuper03 at centerleft
        with fastdissolve
        sm "Are you though? If only..."        
        jump Main
   
