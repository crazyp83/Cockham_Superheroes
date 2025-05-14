################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")
    line_leading 12

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    $ vtag = _get_voice_info().tag

    python:
        vinfo = _get_voice_info()
        vname = vinfo.filename
        vtag = vinfo.tag

    showif any([persistent.voice_text, not vname, not vtag, vtag in persistent._voice_mute, vtag and vtag not in [t for t, _ in voice_tags]]) and not renpy.is_skipping():
        window:
            id "window"

            if who is not None:

                window:
                    style "namebox"
                    text who id "who"

            text what id "what"


        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.95
    ypos 480
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("New Game") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        textbutton _("Patreon") text_color "#f96854" action OpenURL("https://www.patreon.com/epiclust")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("CREDITS") action ShowMenu("about")
        
        textbutton _("Changelog") action ShowMenu("changelog")
        
        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)

        imagebutton idle "icons/epicbanner.png" hover "icons/epicbanner.png" xpos 0 ypos 0 focus_mask True action OpenURL("https://www.patreon.com/epiclust")

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            # text "[config.name!t]":
                # style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    # label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 180
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 140

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"
            text _("{size=20}{font=gui/Heroes Legend.ttf}A game by Epiclust, also developer of Apocalypse. Android version by the66. {/font}{/size}")
            text _("\n")            
            text _("{size=20}{font=gui/Heroes Legend.ttf}Please follow me on my {a=https://timdonehy200.deviantart.com}{size=20}{font=gui/Heroes Legend.ttf}Deviant Art{/font}{/size}{/a} page. {/font}{/size}")
            text _("\n")            
            text _("{size=20}{font=gui/Heroes Legend.ttf}Join my discord channel with this invite: {a=https://discord.gg/8QUPH3w2A6}{size=20}{font=gui/Heroes Legend.ttf}Discord Invite{/font}{/size}{/a} {/font}{/size}")

## Changelog screen ################################################################
##
## This screen gives the latest changelog.

screen changelog():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("\n")
            
            text _("{size=30}Changelog for version [config.version!t]\n{/size}")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission08 implemented. Talk to Excella or Ada Wang to trigger. (allows either Excella or Ada to join harem){/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Anal SEX scene with Excella Gionne if chose to help the Mafia in Mission 08. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Anal SEX scene with Ada Wang if chose to help triad in Mission 08. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Extra SEX scene with Audit Girl in the gym. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Naughty galleries accessible by pressing \"g\" in-game!{/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.6\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission07 implemented. Talk to Captain MILF to trigger. (BLOWJOB with Dani, SEX with Harley (voiced), allows Sergeant Dani to join harem){/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Visit Mayor after completing mission to receive missing gift. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Captain MILF can join the Harem on Hero Route, extra scene with her in her room at night (VAGINAL SEX). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Extra SEX scene with Emma Frost on Villain Route (ANAL SEX). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Some v04 slow vids redone to 60fps. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - 2 new gym scenes with She-Hulk available, visit her to trigger option (FMG). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with the Black Widow and Natalya in her room at night (THREESOME). Allows for the BW to join harem. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - TWO new SEX cenes with Wonder Woman in her room at night. One repeatable, allows for her to join harem. (TITFUCK, ANAL) {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New Harem Girls screen and Agent Natalya added to dossier (available from Stats screen). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - All v05 upwards slow vids redone to 60fps. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.5\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Major SEX scene with Captain MILF in her room at night (TITJOB, FOOTJOB, ANAL). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with Excella Gionne (go to mafia loc to launch). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New sexy scene with Audit Girl in the gym. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Continuation of Lois Pane BDSM training in her flat (VAGINAL). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New SEX scene with She-Hulk after fucking Emma Frost in her office (if she has escaped). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Some more voice acting available (PG room yoga, Lara Temple, Twister with WW, Harley sex). {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest07 implemented. Talk to Captain MILF in hall to trigger. (SEX with SS Valkyries, travel back in time to Berlin, 1945 with Wonder Woman). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Extra blowjob scene available with Catwoman in her Cat-Cave. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sexy Wrestling scene with The Black Widow at the gym (HANDJOB, TEASING). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Wonder Woman pregnancy and birth scene (visit her room at night after completing Quest07). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Small scenes post-birth with Wonder Woman and Audit Girl (Breastfeeding). {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Resistance training with Captain MILF at the pool (nudity). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sexy scenes with Powergirl at the pool (Muscles, Masturbation, unlocks the Powergirl Bedroom SEX scene upon completion for those who chose to help the Black Widow during WW kidnapping scene). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission06 implemented (SEX with Stallion's henchwomen). Talk to Captain Sawyer or Emma Frost to launch depending on route. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Catwoman's lair unlocked by Mission06 (Vaginal and anal SEX). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New gallery for Catwoman.{/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.4\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission05 implemented. Talk to the Black Widow in her room, then to Captain MILF in the Hall to launch (SEX with Robots, LESBIAN SEX between Lara and Natasha, unlocks the Black Widow Bedroom SEX scene upon completion for those who chose to help Powergirl during WW kidnapping scene). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Cucking SEX Scene with Lois and Superman at Cockham Planet HQ (Lois can now become a Harem girl). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Handjob scene with Ada Wang Redux available at the Triad location. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sex scene available with Emma Frost at Frost Towers during the day. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Agent Natalya added to gallery w/ animations. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Can now jump to Game Level02 after the intro. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.4\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Senses level 02 training with Wonder Woman at night in the gym (+BLOWJOB). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New scene at the Lingerie store (LESBIAN, ANAL SEX). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest 06 implemented: visit Lara in the evening to trigger (SEX with Queen Cleopatra, + new gallery for her, +1 Mind Control if on HERO route). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sexy Gym scene with Audit Girl during the day. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Post-clothed curling sexy scene with Captain MILF in the gym at night (THIGH FUCKING). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Poison Ivy can now become part of the MC's Good Harem.{/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Voice Acting now implemented for the intro (press \"v\" in-game to activate-inactivate).{/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sergeant Dani sexy photoshoot at Cockham Planet (SOLO, Masturbation) + new gallery for her. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with Powergirl in her room at night (if MC chose to help her during WW kidnapping scene). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Audit girl jacuzzi cleaning SEX scene level02. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Angela and Demona Level02 dreamy scenes (VAGINAL SEX). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Poison Ivy SEX scene if she is in the MC's Evil Harem.{/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.3\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Saves can now be named (still, don't save within a screen!) {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New animation screens added to the galleries, with different outfits + naked for each girl. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Titjob from Powergirl in the gym (train naked when nobody's around). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with The Black Widow in her room at night (if MC chose to help her during WW kidnapping scene). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest05 implemented - Go to the CCPD during the day to trigger (SEX with Poison Ivy, THREESOME SEX with Sophia Porker and Captain Sawyer).{/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with Captain Sawyer in her office during the day once Quest05 has been completed.{/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Superhero leveling up scene (FMG (Supergirl) and THREESOME SEX with Captain MILF and Supergirl, parts of which become a new repeateable sex scene with Captain MILF available from her room at night). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Several existing scenes now become unavailable due to leveling up. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - SEX scene with Lara Crotch in her room at night (need Super-Seduction Level 2). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sexy scene with Wonder Woman in her room at night. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Several NEW small scenes at the gym with various girls. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Supergirl added to MC jacuzzi jerkoff scene + new MC pics for that scene. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - New sexy scene at Lois' place (DILDO MASTURBATION). {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Introduction of Supergirl (Lesbian scene with Powergirl, HANDJOB and VAGINAL SEX, meet Poison Ivy). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Extension of the Audit Girl Jacuzzi scene (SEX, +1 Villain pt available). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mind Control level 1 training with Emma Frost on the Villain Route. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Fight with Wonder Woman (ANAL SEX, +1 Super-Combat on the Hero Route). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sexy gym scene with Captain MILF ending Game Level 1. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.2\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Special action-packed Event that will trigger automatically (sex with Wonder Woman). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Arkham Asylum location added - fly with Powergirl in the evening to obtain it. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest 04 implemented - Go to Lara's room during the day after Special Event to trigger it. Introduces She-Hulk (sex). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Two sexy scenes with Miss Scarlet once She-Hulk quest is activated - visit Arkham in the evening. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Two sexy night pool scenes with Powergirl available. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Titjob from Demona in the Villain route available every week at night. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission 04 implemented - Go to CCPD during the day to trigger it. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Resistance training with Emma Frost (Villain Route - need to be at least neutral). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Maledom sex scene with Captain MILF - visit her at night (Hero or Villain Route, need to be very good or at least evil) - same scene bar dialogues and two pics. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Titfuck scene available with Excella Gionne - visit the Mafia Lair with Audit Girl at night to trigger. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Threesome sex scene with Barbara and Tabitha available at the Sirens Club - visit during the day. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Handjob from Angela in the Hero route available every week at night. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Extended Lois Pane BDSM scene (+1 Super-Villain pt available). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - 3 more girls to dream about while wanking in the jacuzzi. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest 02 implemented - sex with Lara Crotch. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Combat training with the Black Widow at the gym.  Two scenes (so return), one with a \"happy ending\". {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Agility training with Wonder Woman at the gym (ending in a blowjob). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Seduction training with Captain MILF in her room at night (sexy scene with breastfeeding). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Super-Strength training with Superman at the gym (Super-Villain or Super-Hero point available). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Sex scene with the Black Widow at the pool during the day available (extended scene if MC has acquired the Cockring of Lust). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Lingerie sessions with Powergirl in her room at night (ending in a footjob) {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Lingerie store available with a handjob scene with store clerk available. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission 03 implemented - Talk to Captain MILF in the hall in the morning to unlock. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission 03 sex details - Scenes with Mayor's daughter + new character Honoka. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Several town locations added: Sirens Club, Mafia, Lois' Flat, Harley Quiff's Den, Mayor's House, Frost Towers, Chinese Triad. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Go on the beat with Captain Sawyer (ask about sex crimes during the day at the CCPD - needed to unlock Harley's den). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Yoga Stretching scene with Captain MILF added (go to her room at night). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Minor bug fixes (can now open screen and stats screens during location choosing, MC dossier page displays extra superpowers) {/font}{/size}")
            text _("\n")            
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} Previous changelogs for versions 0.1\n {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission 02 implemented - sex with Sexy Luthor and Sergeant Dani. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Compound gym added: happy endings with Wonder Woman and Powergirl available, other small sexy scenes. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Audit Girl massage scene extended to titfucking. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Audit Girl jacuzzi scene added (available every week when she needs cleaning (- talk to her in library)). {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Blowjob scene with Captain MILF in the pool sauna added. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Dildo masturbation scene with Black Widow in her room added. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - 3 more girls added to MC jacuzzi jerkoff sessions. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - GAMEPLAY: added a counter for when Super-Powers are used effectively during quests or missions - might need to replay game to activate them. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - GAMEPLAY: This will be used in the future for Super-Power progress. {/font}{/size}")
            text _("\n")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Audit Girl costume quest implemented. Another quest also available. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Mission 01  implemented. Sex with Sophia Porker, optional footjob by Captain Sawyer (Super-Senses needed) {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Compound locations: MC room, girls' rooms, pool, main hall, library, added. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Cockham City map implemented with 2 locations added. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Side naughty scenes: Twister game with Wonder Woman, photoshoot session with Lois Pane, Back rub with Audit Girl, jerk off in jacuzzi. {/font}{/size}")
            text _("{size=40}{font=gui/Boogaloo-Regular.ttf} - Quest screen with hints implemented (all mssions and quests so far are EASY). {/font}{/size}")

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slotssave(_("Save"))

screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slotssave(Save):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(Save):

        fixed:
            if save_input == "save_name":
                input:
                    default "[save_name]"
                    value VariableInputValue('save_name')
                    length 30
            else:
                if save_name.strip() == "":
                    textbutton "{size=20}{font=gui/Heroes Legend.ttf} Click to name your save {/font}{/size}":
                        action SetVariable("save_input","save_name")
                else:
                    textbutton "[save_name]":
                        action SetVariable("save_input","save_name")

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 16) gives the numbers from 1 to 15.
                for page in range(1, 16):        
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

screen file_slots(Load):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(Load):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 16) gives the numbers from 1 to 15.
                for page in range(1, 16):        
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

init python:
    def get_volume(mixer):
        m = {
            "Music" : "music",
            "Sound" : "sfx",
            "Voice" : "voice"
            }
        f = getattr(preferences, "get_mixer", preferences.get_volume)
        return f(m[mixer])

screen mixer_label(mixer):
    fixed:
        label _("[mixer!t] Volume")
        label "{{size=-5}}{:.0%}".format(get_volume(mixer)) xalign 1. yoffset 5

screen preferences(show_voice_ext=False):

    tag menu

    default show_voice = False

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"

                vbox:

                    $ text_cps = "inf." if not _preferences.text_cps else "{:.1f} cps".format(_preferences.text_cps)
                    fixed:
                        label _("Text Speed")
                        label "{size=-5}[text_cps]" xalign 1. yoffset 5

                    bar value Preference("text speed")

                vbox:

                    $ afm = "{:.0%}".format(_preferences.afm_time / 30.) if _preferences.afm_time else "Off"
                    fixed:
                        label _("Auto-Forward Speed")
                        label "{size=-5}[afm]" xalign 1. yoffset 5

                    bar value Preference("auto-forward time")


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"

                vbox:

                    if config.has_music:
                        use mixer_label(_('Music'))

                        bar value Preference("music volume")

                    if config.has_sound:
                        use mixer_label(_('Sound'))

                        bar value Preference("sound volume")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_button"

                vbox:

                    if config.has_voice:
                        use mixer_label(_('Voice'))

                        hbox:
                            bar value Preference("voice volume")

                        null height gui.pref_spacing

                        textbutton _("Mute All Voices"):
                            action ToggleVoiceMuteAll(voice_tags)
                            style "mute_button"

                        textbutton _("Manage Voices"):
                            action With(config.intra_transition), ToggleScreenVariable("show_voice")
                            style "manage_button"

    showif show_voice or show_voice_ext:
        use preferences_voice(show_voice_ext)

screen preferences_voice(show_voice_ext):
    modal True

    default fsize = 104
    default fspacing = 30
    default fitems = 4
    default fspaces = fitems - 1
    default yadjustment = ui.adjustment(step=fsize + fspacing)

    if show_voice_ext:
        $ dismiss_action = If(not main_menu, RestartStatement()), SetVariable("_in_voice", False), With(config.intra_transition), Return()

    else:
        $ dismiss_action = With(config.intra_transition), ToggleScreenVariable("show_voice")

    imagebutton:
        idle "#0008"
        action NullAction()

    frame:
        align (.5, .5)
        padding (30, 20)

        vbox:
            spacing 30

            label "Voices Mute & Volume":
                xalign .5

            textbutton _("Voice + Dialog"):
                style "check_button"
                xalign .5
                action ToggleVariable("persistent.voice_text")

            vpgrid:
                style_prefix "mute"

                cols 2
                ymaximum fsize * fitems + fspacing * fspaces
                spacing fspacing
                mousewheel True
                pagekeys True
                scrollbars "vertical"
                yadjustment yadjustment
                side_spacing 30

                for t, n in voice_tags:
                    fixed:

                        vbox:
                            spacing 10

                            fixed:
                                textbutton _("[n]"):
                                    yoffset 5
                                    action ToggleVoiceMute(t)
                                label "{{size=-5}}{:.0%}".format(GetCharacterVolume(t)):
                                    xalign 1.
                                    yoffset 5

                            bar value SetCharacterVolume(t)

            textbutton _("Return"):
                style "button"
                text_style "navigation_button_text"
                xalign .5
                selected False
                keysym "game_menu"
                action dismiss_action


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style slider_fixed is fixed

style mute_label is slider_label
style mute_label_text is pref_label_text
style mute_slider is gui_slider
style mute_button is gui_button
style mute_button_text is gui_button_text
style mute_pref_vbox is pref_vbox
style mute_fixed is slider_fixed
style mute_vscrollbar is gui_vscrollbar
style mute_bar is slider_slider

style manage_button is mute_button
style manage_button_text is mute_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    layout "nobreak"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    layout "nobreak"

style mute_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/mute_[prefix_]foreground.png"

style mute_button:
    variant "small"
    foreground "gui/phone/button/mute_[prefix_]foreground.png"

style mute_button_text:
    properties gui.button_text_properties("check_button")
    layout "nobreak"

style mute_vscrollbar:
    unscrollable gui.unscrollable

style manage_button:
    properties gui.button_properties("check_button")
    foreground None

style slider_slider:
    xsize 645

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style slider_fixed:
    xsize 645
    yfit True


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("G")
        text _("Opens Naughty Gallery.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.label_text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    add "intro/cockham01.jpg"
    add "gui/overlay/confirm.png"
    frame:

        vbox:
            xalign .5
            yalign .3
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
