# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    if persistent.voice_text == None:
        persistent.voice_text = False

    @renpy.pure
    class ToggleVoiceMuteAll(Action, DictEquality):

        def __init__(self, voice_tags, invert=False):
            self.voice_tags = voice_tags
            self.invert = invert


        def get_selected(self):
            rv = all([t in persistent._voice_mute for t, _ in self.voice_tags])

            if self.invert:
                return not rv
            else:
                return rv

        def __call__(self):
            mute = not self.get_selected()
            for t, _ in self.voice_tags:
                if mute:
                    persistent._voice_mute.add(t)
                else:
                    persistent._voice_mute.discard(t)

            renpy.restart_interaction()

    @renpy.pure
    class SetVoiceMuteAll(Action, DictEquality):

        def __init__(self, voice_tags, mute):
            self.voice_tags = voice_tags
            self.mute = mute

        def get_selected(self):
            rv = all([t in persistent._voice_mute for t in self.voice_tags])

            return rv

        def __call__(self):
            for t in self.voice_tags:
                if self.mute:
                    persistent._voice_mute.add(t)
                else:
                    persistent._voice_mute.discard(t)

            renpy.restart_interaction()

    def GetCharacterVolume(voice_tag):
        return persistent._character_volume.get(voice_tag, 1.0)

    _in_voice = False
    def show_voiceacting_menu():
        if any([_in_voice, _in_gallery, _menu]):
            return
        store._in_voice = True
        renpy.run(ShowMenu("preferences_voice", show_voice_ext=True))
    config.underlay.append(renpy.Keymap(open_voiceacting_menu = show_voiceacting_menu))
    config.keymap["open_voiceacting_menu"] = ["v"]

    _in_gallery = False
    def show_gallery_menu():
        if any([_in_voice, _in_gallery, _menu]):
            return
        store._in_gallery = True
        renpy.call_in_new_context("MainGallery")
    config.keymap["open_gallery_menu"] = ["g"]
    
    # When key is pressed at anytime, open custom screen.
    config.underlay.append(renpy.Keymap(open_gallery_menu=show_gallery_menu))
    config.underlay.append(renpy.Keymap(open_voiceacting_menu=show_voiceacting_menu))
    define.move_transitions("movefast", 0.1)

    renpy.music.register_channel("channel1", mixer="music", loop=True)
    renpy.music.register_channel("channel2", mixer="music", loop=True)
    renpy.music.register_channel("channel3", mixer="music", loop=True)
    renpy.music.register_channel("channel4", mixer="sound", loop=True)
    
init:
    $ define.move_transitions('slowmove', 2.0, subpixel=True)    
    define fastdissolve = Dissolve(0.2)
    define ultrafastdissolve = Dissolve(0.1)
    define flash  = Fade(.25, 0.0, .5, color="#fff")
    define fastflash  = Fade(.2, 0.0, .3, color="#fff")
    style say_dialogue2:
        size 40
        font "gui/Boogaloo-Regular.ttf"
        xpos 300
        ypos 40
        xmaximum 1500
        bold False
        color "#e2edff"
        justify True
        line_spacing 2

    style say_dialogue1:
        size 40
        font "gui/Boogaloo-Regular.ttf"
        xpos 300
        ypos 40
        xmaximum 1500
        bold False
        color "#feedff"
        justify True
        line_spacing 2

    style statsCommon is default:
        outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)]
        font "Gui/Heroes Legend.ttf"

    style statsMain is statsCommon:
        size 25
        color "#1c73ff"

    style statsPhysical is statsCommon:
        size 35
        color "#ff0000"

    define farright = Position(xcenter=0.8)
    define midright = Position(xcenter=0.7)
    define centerright = Position(xcenter=0.6)
    define centerleft = Position(xcenter=0.4)
    define midleft = Position(xcenter=0.3)
    define farleft = Position(xcenter=0.2)
    define farleft02 = Position(xcenter=0.1)

    style PeriodDay:
        size 15
        outlines [(1, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)]
        color "#1c73ff"
        font "Gui/Heroes Legend.ttf"

    transform PeriodPosition:
        xalign .9
        yalign 0.00
    screen calendar():
        zorder 99        
        add ("Icons/{}icon.png".format( [ "day", "night"][period%2] )) at PeriodPosition
        text ( "Day {:002}".format( day ) ) style "PeriodDay" xalign 0.96 yalign 0.017

init:
    screen screenmcdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundmc.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenmcdossier"), Show ("screenredfolder")]
        text "[hero] was recently recruited into the Cockham League of Justice to fight the" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "scourge of sex crimes taking over the city. He acquired his superpowers in" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "Captain MILF's radiation device and came out of it as a muscle-bound, horse-hung" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "superhero. He must now fight his way through the dark sex underworld of Cockham" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "and increase his superpowers to become the ULTIMATE SUPERHERO (or Super-Villain?)" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}           [hero]{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: [age]{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        if mclevel02 == False:
            text "{font=Gui/Heroes Legend.ttf}Height: 5ft5 (1m65){/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        if mclevel02:
            text "{font=Gui/Heroes Legend.ttf}Height: 5ft8 (1m73){/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight

        vpgrid:
            pos (880, 500)
            xspacing 40
            yspacing 30
            cols 3
            ysize 270
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_spacing 22

            for power in ["strength", "seduction", "stud", "senses", "resistance", "combat", "agility", "healing", "mind"]:
                $ number = getattr(store, "mc{}".format(power))
                if number:
                    use powers_frame(power, number)

        text "- Hesitant about where he stands. May be led into evil" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "- Easily distracted by his sexual libido" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screenwidowdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundwidow.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenwidowdossier"), Show ("screenredfolder")]
        text "The Black Widow is a fighting superhero who was trained as an assassin in Russia." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "She uses her electro-shock batons with extreme agility, making her the fiercest" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "superhero in hand-to-hand combat." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "She is a complete sex-addict and feels sexually-deprived as most men do not meet" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "her standards for rough, unending sex..." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}      Black Widow{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 32{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft3{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textcombat.png" at PowerName01
        add "icons/supercombat.png" at Power01a
        add "icons/supercombat.png" at Power01b
        add "icons/supercombat.png" at Power01c

        add "icons/textagility.png" at PowerName02
        add "icons/superagility.png" at Power02a
        add "icons/superagility.png" at Power02b
        add "icons/superagilitygrey.png" at Power02c
            
        text "- Still has subconscious loyalty to Communist Russia and is vulnerable to mind control" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "by infiltrated Red Agents in Cockham City" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screenwonderdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundwonder.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenwonderdossier"), Show ("screenredfolder")]
        text "Wonder Woman is a princess from Ancient Greece who somehow ended up in Cockham" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "through a time portal. She longs to go back to her homeland but a cabal of Nazis" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "keep foiling her attempts. Therefore, Nazis are her sworn enemies and she will go" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "to great lengths to seek them out." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "Her Lasso of Truth is a powerful weapon in her quest for peace and freedom." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}      Wonder Woman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: unknown{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textcombat.png" at PowerName01
        add "icons/supercombat.png" at Power01a
        add "icons/supercombat.png" at Power01b
        add "icons/supercombatgrey.png" at Power01c

        add "icons/textsenses.png" at PowerName02
        add "icons/supersenses.png" at Power02a
        add "icons/supersenses.png" at Power02b
        add "icons/supersensesgrey.png" at Power02c

        add "icons/textagility.png" at PowerName03
        add "icons/superagility.png" at Power03a
        add "icons/superagilitygrey.png" at Power03b
        add "icons/superagilitygrey.png" at Power03c
            
        add "icons/texthealing.png" at PowerName04
        add "icons/superhealing.png" at Power04a
        add "icons/superhealinggrey.png" at Power04b
        add "icons/superhealinggrey.png" at Power04c

        add "icons/textstrength.png" at PowerName05
        add "icons/superstrength.png" at Power05a
        add "icons/superstrengthgrey.png" at Power05b
        add "icons/superstrengthgrey.png" at Power05c

        text "- Becomes submissive if bound or tied up" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "- Has no clue about the real modern world" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screencatwomandossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundcatwoman.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screencatwomandossier"), Show ("screenredfolder")]
        text "Catwoman is a notorious jewelry thief who steals from the rich and powerful" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "to give to herself. Anything that glitters immediately attracts her" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "attention. She is elusive and is often seen at nights on top of buildings." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "She might help out the League of Justice every now and then to appease the" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "CCPD." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}        Catwoman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 30{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft8{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textagility.png" at PowerName01
        add "icons/superagility.png" at Power01a
        add "icons/superagility.png" at Power01b
        add "icons/superagility.png" at Power01c

        add "icons/textsenses.png" at PowerName02
        add "icons/supersenses.png" at Power02a
        add "icons/supersenses.png" at Power02b
        add "icons/supersensesgrey.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        text "- Anything that glitters distracts her immediately" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenmilfdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundmilf.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenmilfdossier"), Show ("screenredfolder")]
        text "Captain MILF is the leader of the Cockham League of Justice and its most powerful" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "superheroine. She is also incidentally the MC's landlady. Her nemesis is Emma Frost," color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "who she fought time and time again on a different astral plane until a truce was" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "established between them. She manages the compound and assigns missions to each" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "superhero, while herself helping them if the need arises." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}    Captain MILF{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 40{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft6{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textresistance.png" at PowerName01
        add "icons/superresistance.png" at Power01a
        add "icons/superresistance.png" at Power01b
        add "icons/superresistance.png" at Power01c

        add "icons/textseduction.png" at PowerName02
        add "icons/superseduction.png" at Power02a
        add "icons/superseduction.png" at Power02b
        add "icons/superseduction.png" at Power02c

        add "icons/textstrength.png" at PowerName03
        add "icons/superstrength.png" at Power03a
        add "icons/superstrength.png" at Power03b
        add "icons/superstrengthgrey.png" at Power03c

        add "icons/texthealing.png" at PowerName04
        add "icons/superhealing.png" at Power04a
        add "icons/superhealing.png" at Power04b
        add "icons/superhealinggrey.png" at Power04c

        add "icons/textcombat.png" at PowerName05
        add "icons/supercombat.png" at Power05a
        add "icons/supercombatgrey.png" at Power05b
        add "icons/supercombatgrey.png" at Power05c
            
        add "icons/textagility.png" at PowerName06
        add "icons/superagility.png" at Power06a
        add "icons/superagilitygrey.png" at Power06b
        add "icons/superagilitygrey.png" at Power06c
            
        text "- Huge cocks make her weak in the knees and reduces her superpowers" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "- Scared of heights" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screensuperdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundsuper.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screensuperdossier"), Show ("screenredfolder")]
        text "Superman is a powerful superhero born on planet Krypton. He landed on Earth as a boy" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "and was constantly made fun of at school for not having a dick." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "He has a regular undercover job as a reporter at the Cockham Planet and has fallen." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "in love with his co-worker Lois Pane (but he can't get to third base obviously...)." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "His arch-enemy is Sexy Luthor, who keeps escaping over and over again." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}           Superman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 33{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 6ft0{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textstrength.png" at PowerName01
        add "icons/superstrength.png" at Power01a
        add "icons/superstrength.png" at Power01b
        add "icons/superstrength.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombat.png" at Power02b
        add "icons/supercombat.png" at Power02c

        add "icons/textflight.png" at PowerName03
        add "icons/superflight.png" at Power03a
        add "icons/superflight.png" at Power03b
        add "icons/superflight.png" at Power03c

        add "icons/textresistance.png" at PowerName04
        add "icons/superresistance.png" at Power04a
        add "icons/superresistance.png" at Power04b
        add "icons/superresistancegrey.png" at Power04c

        add "icons/textagility.png" at PowerName05
        add "icons/superagility.png" at Power05a
        add "icons/superagility.png" at Power05b
        add "icons/superagilitygrey.png" at Power05c
            
        add "icons/textsenses.png" at PowerName06
        add "icons/supersenses.png" at Power06a
        add "icons/supersenses.png" at Power06b
        add "icons/supersensesgrey.png" at Power06c
            
        text "- Proximity with Kryptonite turns Superman into a weakling" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "- Doesn't even have a dick" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screenpowerdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundpower.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenpowerdossier"), Show ("screenredfolder")]
        text "Powergirl is a young superhero and the daughter of Captain MILF who trained her" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "as a superhero at a young age. She is known for being super-nice but may go into" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "a rage when faced with plants or flowers. Powergirl's arch-enemy is the elusive" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "Ivy Popper who she dreads above all. As the MC's landlady's daughter, she is" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "also very protective of him." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}          Powergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft5{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight

        add "icons/textflight.png" at PowerName01
        add "icons/superflight.png" at Power01a
        add "icons/superflight.png" at Power01b
        add "icons/superflightgrey.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombatgrey.png" at Power02b
        add "icons/supercombatgrey.png" at Power02c

        add "icons/textsenses.png" at PowerName03
        add "icons/supersenses.png" at Power03a
        add "icons/supersensesgrey.png" at Power03b
        add "icons/supersensesgrey.png" at Power03c

        add "icons/textresistance.png" at PowerName04
        add "icons/superresistance.png" at Power04a
        add "icons/superresistancegrey.png" at Power04b
        add "icons/superresistancegrey.png" at Power04c
            
        add "icons/textstrength.png" at PowerName05
        add "icons/superstrength.png" at Power05a
        add "icons/superstrengthgrey.png" at Power05b
        add "icons/superstrengthgrey.png" at Power05c

        text "- weakened by natural elements such as plants which she hates" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenbatmandossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundbatman.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenbatmandossier"), Show ("screenredfolder")]
        text "Batman is a billionaire who goes by the name of Bruce Vayne in real life." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "While the Head of Vayne Enterprises, he doesn't really take care of his company and" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "prefers to scour the city at nights in search of criminals, most especially, the elusive." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "Joker and his acolyte, Harley Quiff, who are his arch-enemies." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "{font=Gui/Heroes Legend.ttf}           Batman{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 35{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textflight.png" at PowerName01
        add "icons/superflight.png" at Power01a
        add "icons/superflightgrey.png" at Power01b
        add "icons/superflightgrey.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombatgrey.png" at Power02b
        add "icons/supercombatgrey.png" at Power02c

        add "icons/textagility.png" at PowerName03
        add "icons/superagility.png" at Power03a
        add "icons/superagilitygrey.png" at Power03b
        add "icons/superagilitygrey.png" at Power03c

        text "- His superpowers are the product of enhanced technology and not mutation, therefore," color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "without it, he is no longer a superhero" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screenauditdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundaudit.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenauditdossier"), Show ("screenredfolder")]
        text "Audit Girl is a young intern superheroine who recently joined the Cockham League" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "of Justice. As a novice, she is very shy despite graduating top of her class at" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "the Xavier School for the Gifted. Often referred to as a nerd superheroine," color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "her mental skills are unparalleled. Her hands are also capable of super-healing." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "Her enormous jugs and big booty are a constant source of anxiety for her." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}         Audit Girl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft2{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textbrain.png" at PowerName01
        add "icons/superbrain.png" at Power01a
        add "icons/superbrain.png" at Power01b
        add "icons/superbrain.png" at Power01c

        add "icons/texthealing.png" at PowerName02
        add "icons/superhealing.png" at Power02a
        add "icons/superhealing.png" at Power02b
        add "icons/superhealing.png" at Power02c

        text "- Doesn't have a superhero costume and therefore never goes out of the compound" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11
        text "- Untrained for any form of combat" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line12

    screen screenlaradossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundlara.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenlaradossier"), Show ("screenredfolder")]
        text "Lara Crotch is an adventurer and archeologist who specializes in seeking rare" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "and powerful artefacts in order to stop them from being used by supervillains." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "Thanks to her extreme agility and sense of danger, she has survived numerous" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "expeditions around the world. While living in the compound, she is often abroad" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "and is therefore rarely seen in Cockham City." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}         Lara Crotch{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 28{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textagility.png" at PowerName01
        add "icons/superagility.png" at Power01a
        add "icons/superagility.png" at Power01b
        add "icons/superagility.png" at Power01c

        add "icons/textsenses.png" at PowerName02
        add "icons/supersenses.png" at Power02a
        add "icons/supersenses.png" at Power02b
        add "icons/supersenses.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        text "- Often takes unnecessary risks that put her in danger" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenhulkdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundhulk.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenhulkdossier"), Show ("screenredfolder")]
        text "She-Hulk used to be a normal girl, but a bad blood transfusion after an" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "accident left her with a rare condition called \"Totallinutis\". Her skin" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "and hair turned green and her mood turned angry. While she used her colossal" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "Super-Strength as a efficient League Member for many years, the Mayor" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "ordered for her to be held captive until she can control her anger." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}         She-Hulk{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 6ft10{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textstrength.png" at PowerName01
        add "icons/superstrength.png" at Power01a
        add "icons/superstrength.png" at Power01b
        add "icons/superstrength.png" at Power01c

        add "icons/texthealing.png" at PowerName02
        add "icons/superhealing.png" at Power02a
        add "icons/superhealing.png" at Power02b
        add "icons/superhealinggrey.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        text "- Can go berserk once again if pushed into anger territory" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screensupergirldossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "v03/dossierbackgroundsupergirl.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screensupergirldossier"), Show ("screenredfolder")]
        text "Supergirl is a young superheroine from the Coxville League of Superheroes" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "on the other side of the country. She got bored from nothing ever" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "happening there and has moved for an internship to Cockham where she" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "hopes her superpowers will help her see some real action." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "She also happens to be the MC's cousin." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}         Supergirl{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 18{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft2{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textstrength.png" at PowerName01
        add "icons/superstrength.png" at Power01a
        add "icons/superstrength.png" at Power01b
        add "icons/superstrengthgrey.png" at Power01c

        add "icons/textsenses.png" at PowerName02
        add "icons/supersenses.png" at Power02a
        add "icons/supersenses.png" at Power02b
        add "icons/supersensesgrey.png" at Power02c

        add "icons/textflight.png" at PowerName03
        add "icons/superflight.png" at Power03a
        add "icons/superflight.png" at Power03b
        add "icons/superflightgrey.png" at Power03c

        add "icons/textcombat.png" at PowerName04
        add "icons/supercombat.png" at Power04a
        add "icons/supercombatgrey.png" at Power04b
        add "icons/supercombatgrey.png" at Power04c

        add "icons/textresistance.png" at PowerName05
        add "icons/superresistance.png" at Power05a
        add "icons/superresistancegrey.png" at Power05b
        add "icons/superresistancegrey.png" at Power05c

        text "- Feels inadequate breast- and muscle-wise compared to her cousin Powergil" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenpoisondossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "v03/dossierbackgroundivy.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenpoisonivydossier"), Show ("screenbluefolder")]
        text "Poison Ivy used to be botanist at Cockham's Robinson Park before" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "being splashed by plant-controlling chemicals she had developed" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "in her lab. Since then, she has become obsessed with plants, and harbors " color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "a strong desire for them to overtake the world." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "She can control plants and use their toxins to great effect against" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "her perceived enemies." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line06
        text "{font=Gui/Heroes Legend.ttf}          Poison Ivy{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 22{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft7{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textplant.png" at PowerName01
        add "icons/plantcontrol.png" at Power01a
        add "icons/plantcontrol.png" at Power01b
        add "icons/plantcontrol.png" at Power01c

        add "icons/textagility.png" at PowerName02
        add "icons/superagility.png" at Power02a
        add "icons/superagility.png" at Power02b
        add "icons/superagility.png" at Power02c

        add "icons/textresistance.png" at PowerName03
        add "icons/superresistance.png" at Power03a
        add "icons/superresistance.png" at Power03b
        add "icons/superresistance.png" at Power03c

        add "icons/textcombat.png" at PowerName04
        add "icons/supercombat.png" at Power04a
        add "icons/supercombatgrey.png" at Power04b
        add "icons/supercombatgrey.png" at Power04c

        text "- Her hatred of humanity leads to her loneliness and can depress her at times" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenwangdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundwang.png"
        add "icons/paperclip.png"
        if mission08mafiawin:
            add "v051/neutralized.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenwangdossier"), Show ("screenbluefolder")]
        text "Ada Wang is the leader of the Chinese Triad and resides in a palace in Chinatown," color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "surrounded by her notoriously dangerous ninjas female warriors. She constantly" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "plots to seek commercial advantages over the Mafia, using any means necessary." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "She also runs the famous \"Misohawny\" brothel in Chinatown." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "{font=Gui/Heroes Legend.ttf}            Ada Wang{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 32{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft7{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textseduction.png" at PowerName01
        add "icons/superseduction.png" at Power01a
        add "icons/superseduction.png" at Power01b
        add "icons/superseductiongrey.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombatgrey.png" at Power02b
        add "icons/supercombatgrey.png" at Power02c

        add "icons/textagility.png" at PowerName03
        add "icons/superagility.png" at Power03a
        add "icons/superagilitygrey.png" at Power03b
        add "icons/superagilitygrey.png" at Power03c

        text "- No known weaknesses" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenharleydossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundharley.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenharleydossier"), Show ("screenbluefolder")]
        text "Harley Quiff is an insane serial rapist who used to be an inmate at Arkham's Asylum" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "until Mayor Krass's general amnesty. Since then, she has been spotted living in an" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "abandoned warehouse where she talks to herself and becomes crazier by the day." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "She is supposedly dating the Joker but this has not been confirmed." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "{font=Gui/Heroes Legend.ttf}         Harley Quiff{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 27{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft6{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textseduction.png" at PowerName01
        add "icons/superseduction.png" at Power01a
        add "icons/superseduction.png" at Power01b
        add "icons/superseduction.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombatgrey.png" at Power02b
        add "icons/supercombatgrey.png" at Power02c

        add "icons/textagility.png" at PowerName03
        add "icons/superagility.png" at Power03a
        add "icons/superagilitygrey.png" at Power03b
        add "icons/superagilitygrey.png" at Power03c

        text "- Bat-shit crazy which can be used against her" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenfrostdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundfrost.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenfrostdossier"), Show ("screenbluefolder")]
        text "Emma Frost is a businesswoman and head of Frost Inc, the competitors of Vayne" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "Enterprises. Her astonishingly-fast rise to the top is attributed to her" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "telepathic abilities. Once a foe of Captain MILF, she has established a truce with" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "the Cockham League of Justice and it is unclear where she stands in the fight" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "of good vs evil in Cockham. She can project both minds and bodies onto a different" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "astral plane and turn into solid diamond, making her extremely powerful in any case." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line06
        text "{font=Gui/Heroes Legend.ttf}         Emma Frost{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 45{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft8{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textprojection.png" at PowerName01
        add "icons/astralprojection.png" at Power01a
        add "icons/astralprojection.png" at Power01b
        add "icons/astralprojection.png" at Power01c

        add "icons/textmind.png" at PowerName02
        add "icons/mindcontrol.png" at Power02a
        add "icons/mindcontrol.png" at Power02b
        add "icons/mindcontrol.png" at Power02c

        add "icons/textbrain.png" at PowerName03
        add "icons/superbrain.png" at Power03a
        add "icons/superbrain.png" at Power03b
        add "icons/superbraingrey.png" at Power03c

        add "icons/textstrength.png" at PowerName04
        add "icons/superstrength.png" at Power04a
        add "icons/superstrengthgrey.png" at Power04b
        add "icons/superstrengthgrey.png" at Power04c

        add "icons/textcombat.png" at PowerName05
        add "icons/supercombat.png" at Power05a
        add "icons/supercombatgrey.png" at Power05b
        add "icons/supercombatgrey.png" at Power05c

        text "- Her fashion desires may hinder her mobility during combat" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenkeendossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        if mission07win:
            add "v051/neutralized.png"
        add "icons/dossierbackgroundkeen.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenkeendossier"), Show ("screenbluefolder")]
        text "Barbara Keen runs the famous Sirens Club in downtown Cockham." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "She turned Super-Villain after her love affair with Mayor Krass turned sour." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "After killing Ra's Al-Ghul, she acquired his summoning superpowers and leads" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "a legion of sex assassins who are known for getting rid of her pesky enemies" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "after engaging in wild and deadly orgies with them." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}       Barbara Keen{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 32{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft3{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textsummoning.png" at PowerName01
        add "icons/astralprojection.png" at Power01a
        add "icons/astralprojection.png" at Power01b
        add "icons/astralprojectiongrey.png" at Power01c

        add "icons/textbrain.png" at PowerName02
        add "icons/superbrain.png" at Power02a
        add "icons/superbrain.png" at Power02b
        add "icons/superbraingrey.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        text "- Deep down still in love with Mayor Krass" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenexcelladossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundexcella.png"
        add "icons/paperclip.png"
        if mission08triadwin:
            add "v051/neutralized.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenexcelladossier"), Show ("screenbluefolder")]
        text "Excella Gionne is the young wife of mafia boss Sam \"The Cigar\" but is the de facto" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line01
        text "leader of the local mafia due to her powers of seduction over men. She demands" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line02
        text "complete loyalty from Sam's henchmen and sees the Cockham League of Justice as" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line03
        text "a small nuisance to her criminal enterprise. She is more concerned about the" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line04
        text "Chinese Triad or the Joker's misdeeds and may help the MC under certain" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line05
        text "circumstances." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)] at Line06
        text "{font=Gui/Heroes Legend.ttf}     Excella Gionne{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 38{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft9{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textseduction.png" at PowerName01
        add "icons/superseduction.png" at Power01a
        add "icons/superseduction.png" at Power01b
        add "icons/superseductiongrey.png" at Power01c

        text "- No known weaknesses" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenjokerdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundjoker.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenjokerdossier"), Show ("screenbluefolder")]
        text "The Joker is a psychopathic criminal mastermind as well as a perverse sex deviant." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "Specialized in bank robberies and kidnappings, he likes to mentally and sexually" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "torture his victims with devious contraptions he himself built." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "Thought to date Harley Quiff, his whereabouts remain unknown at this stage." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "Batman is his sworn enemy and he will not hesitate to use extreme violence." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}        The Joker{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 39{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft9{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textbrain.png" at PowerName01
        add "icons/superbrain.png" at Power01a
        add "icons/superbrain.png" at Power01b
        add "icons/superbrain.png" at Power01c

        add "icons/textmind.png" at PowerName02
        add "icons/mindcontrol.png" at Power02a
        add "icons/mindcontrolgrey.png" at Power02b
        add "icons/mindcontrolgrey.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        add "icons/textsenses.png" at PowerName04
        add "icons/supersenses.png" at Power04a
        add "icons/supersensesgrey.png" at Power04b
        add "icons/supersensesgrey.png" at Power04c

        text "- Ugly as fuck, he is rejected by all women and is incapable of love" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11


    screen screenluthordossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundluthor.png"
        add "icons/paperclip.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenluthordossier"), Show ("screenbluefolder")]
        text "Sexy Luthor is the most devious and long-standing criminal in Cockham City." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "Since she was little, she has always attempted to destroy everything around her," color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "using her wit and charm to get her ways. Trained as a scientist, she concocts" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "doomsday machines in order to achieve world domination." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "She may ally with various groups of villains to achieve her goals." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}      Sexy Luthor{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 35{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft10{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textbrain.png" at PowerName01
        add "icons/superbrain.png" at Power01a
        add "icons/superbrain.png" at Power01b
        add "icons/superbrain.png" at Power01c

        add "icons/textseduction.png" at PowerName02
        add "icons/superseduction.png" at Power02a
        add "icons/superseduction.png" at Power02b
        add "icons/superseduction.png" at Power02c

        add "icons/textstrength.png" at PowerName03
        add "icons/superstrength.png" at Power03a
        add "icons/superstrength.png" at Power03b
        add "icons/superstrengthgrey.png" at Power03c

        text "- Fear of getting injured leads her to always attempt to flee fights" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenstalliondossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundstallion.png"
        add "icons/paperclip.png"
        if mission06win:
            add "v051/neutralized.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenstalliondossier"), Show ("screenbluefolder")]
        text "Samson Goldcock, aka \"The Stallion\" is the head of the Narrows Bros, a gang" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "of thugs who mug, rape and pillage for a living. His giant dong is coated" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "with gold leaves and needs to be regularly repainted, hence his constant need" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "for gold. His two favorites henchwomen, Jasmine and Africa, rarely leave" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "his side or his monster cock." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}      The Stallion{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 44{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 6ft8{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textstrength.png" at PowerName01
        add "icons/superstrength.png" at Power01a
        add "icons/superstrength.png" at Power01b
        add "icons/superstrength.png" at Power01c

        add "icons/textstud.png" at PowerName02
        add "icons/superstud.png" at Power02a
        add "icons/superstud.png" at Power02b
        add "icons/superstudgrey.png" at Power02c

        text "- Without its gold coating, his cock loses its appeal to women" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screenstroheimdossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "icons/dossierbackgroundstroheim.png"
        add "icons/paperclip.png"
        if quest07end:
            add "v051/neutralized.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screenstroheimdossier"), Show ("screenbluefolder")]
        text "Colonel Stroheim is a neo-nazi SS officer who acquired superpowers" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "from experimenting on himself with dangerous machines he designed." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "He is a zealous patriot surrounded by fanatical SS Valkyries." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "Wonder Woman is his sworn enemy as he believes her success in returning" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "to her land would trigger the space-time early downfall of the Third Reich." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line05
        text "{font=Gui/Heroes Legend.ttf}          Stroheim{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 33{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 6ft2{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textbrain.png" at PowerName01
        add "icons/superbrain.png" at Power01a
        add "icons/superbraingrey.png" at Power01b
        add "icons/superbraingrey.png" at Power01c

        add "icons/textstrength.png" at PowerName02
        add "icons/superstrength.png" at Power02a
        add "icons/superstrengthgrey.png" at Power02b
        add "icons/superstrengthgrey.png" at Power02c

        add "icons/textcombat.png" at PowerName03
        add "icons/supercombat.png" at Power03a
        add "icons/supercombatgrey.png" at Power03b
        add "icons/supercombatgrey.png" at Power03c

        text "- Adolf Hitler's burnt body parts are the seat of his evil desires" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

    screen screennatalyadossier():
        modal True
        add "icons/dossierbackground.png"
        add "icons/backicon.png" at posbackicon
        add "v06/dossierbackgroundnatalya.png"
        add "icons/paperclip.png"
        if seennatalyawidow:
            add "v051/neutralized.png"
        button:
            xpos 1730
            ypos 1020
            xysize(120, 50)        
            action [renpy.hide_screen("screennatalyadossier"), Show ("screenbluefolder")]
        text "Natalya Ivanabloyuov is a KGB Agent stationed in Cockham." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line01    
        text "Her mission is to manipulate the Black Widow and turn her" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line02
        text "into a sleeper agent for the KGB. She is an expert in" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line03
        text "mind manipulation techniques and hand-to-hand combat." color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line04
        text "{font=Gui/Heroes Legend.ttf}   Agent Natalya{/font}" color "#FF0000" size 50 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHero
        text "{font=Gui/Heroes Legend.ttf}Age: 30{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosAge
        text "{font=Gui/Heroes Legend.ttf}Height: 5ft11{/font}" color "#FF0000" size 22 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at PosHeight
        add "icons/textmind.png" at PowerName01
        add "icons/mindcontrol.png" at Power01a
        add "icons/mindcontrol.png" at Power01b
        add "icons/mindcontrolgrey.png" at Power01c

        add "icons/textcombat.png" at PowerName02
        add "icons/supercombat.png" at Power02a
        add "icons/supercombat.png" at Power02b
        add "icons/supercombatgrey.png" at Power02c

        text "- Failing her mission means being sent to a Siberian gulag" color "#1c73ff" size 30 outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at Line11

# The game starts here.

label start:
stop music
jump Intro