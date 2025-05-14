label CockhamMapDay:
$ cockhamday = True
scene cockhammap with dissolve
show returnicon
show placeplanet at posplanet
show placeccpd at posccpd
show placefrost at posfrost
if locmayors and mission08triadwin == False:
    show placemafia at posmafia
if mission08triadwin:
    show placemafiagrey at posmafia    
if locmayors:
    show placemayors at posmayors
if locmayors == False:
    show placemayorsgrey at posmayors
if loclingerie:
    show placelingerie at poslingerie
if locstallion and mission06win == False:
    show placesamson at posstallion
if locstallion and mission06win:
    show placesamsongrey at posstallion
if loclois:
    show placeloisgrey at poslois
if locquiff:
    show placequiff at posquiff
if locsirens:
    show placesirens at possirens
if locsirens == False or mission07win:
    show placesirensgrey at possirens
if locmayors and mission08mafiawin == False:
    show placetriad at postriad
if mission08mafiawin:
    show placetriadgrey at postriad
if locnazi and quest07end == False:
    show placenazi at posnazi
if locnazi and quest07end :
    show placenazigrey at posnazi
if locarkham:
    show placearkhamgrey at posarkham
if locivy:
    show placeivy at posivy
if preloccatcave or loccatcave:
    show placecatcavegrey at poscatcave
if locembassy:
    show placeembassygrey at posembassy
if lpspeakcw01:
    show placecatcavegrey at poscatcave
    
call screen cockhammapday()
screen cockhammapday():
    key "K_LCTRL" action [renpy.hide_screen("cockhammapday"), Jump ("MCRoomDay")]
    key "keyup_K_LCTRL" action [renpy.hide_screen("cockhammapday"), Jump ("MCRoomDay")]
    key "K_RCTRL" action [renpy.hide_screen("cockhammapday"), Jump ("MCRoomDay")]
    key "keyup_K_RCTRL" action [renpy.hide_screen("cockhammapday"), Jump ("MCRoomDay")]        
    modal True    
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("MCRoomDay")]
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
    button:
        xpos 257
        ypos 426
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("OfficeCCPD")]
    button:
        xpos 870
        ypos 710
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("FrostTower")]
    if locmayors and mission08triadwin == False:
        button:
            xpos 369
            ypos 795
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("MafiaLair")]
    button:
        xpos 496
        ypos 369
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("CockhamPlanet")]
    if locstallion and mission06win == False:
        button:
            xpos 48
            ypos 726
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("StallionDay")]
    if loclingerie:
        button:
            xpos 923
            ypos 287
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("LingerieStore")]
    if locquiff:
        button:
            xpos 1470
            ypos 380
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("HarleyPlace")]
    if locsirens and mission07win == False:
        button:
            xpos 1105
            ypos 543
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("SirensClub")]
    if locmayors:
        button:
            xpos 98
            ypos 187
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("MayorsHome")]
    if locmayors and mission08mafiawin == False:
        button:
            xpos 578
            ypos 722
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("ChineseTriad")]
    if locnazi and quest07end == False:
        button:
            xpos 1474
            ypos 541
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("NaziCompound")]
    if locivy:
        button:
            xpos 701
            ypos 443
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapday"), SetVariable("cockhamday", False), Jump ("IvyLair")]

label CockhamMapNight:
$ cockhamnight = True
scene cockhammap with dissolve
show returnicon
show placeplanetgrey at posplanet
show placeccpd at posccpd
show placefrostgrey at posfrost
if locmayors and mission08triadwin == False:
    show placemafia at posmafia
if mission08triadwin:
    show placemafiagrey at posmafia
show placemayorsgrey at posmayors
if loclingerie:
    show placelingerie at poslingerie
if locstallion and mission06win == False:
    show placesamson at posstallion
if locstallion and mission06win:
    show placesamsongrey at posstallion
if loclois == False:
    show placeloisgrey at poslois
if loclois:
    show placelois at poslois
if locquiff:
    show placequiff at posquiff
if locsirens and mission03 and mission03end == False and spokebarbaramission03 == False:
    show placesirens at possirens
if locsirens == False or (locsirens and (mission03 and mission03end == False and spokebarbaramission03)) or (locsirens and mission03end):
    show placesirensgrey at possirens
if locmayors and mission08mafiawin == False:
    show placetriad at postriad
if mission08mafiawin:
    show placetriadgrey at postriad    
if locmayors == False:
    show placetriadgrey at postriad
if locnazi and quest07end == False:
    show placenazi at posnazi
if locnazi and quest07end :
    show placenazigrey at posnazi
if locarkham:
    show placearkham at posarkham
if locivy:
    show placeivygrey at posivy
if preloccatcave or loccatcave:
    show placecatcave at poscatcave
if locembassy:
    show placeembassy at posembassy
if lpspeakcw01:
    show placecatcave at poscatcave

call screen cockhammapnight()
screen cockhammapnight():
    key "K_LCTRL" action [renpy.hide_screen("cockhammapnight"), Jump ("MCRoomNight")]
    key "keyup_K_LCTRL" action [renpy.hide_screen("cockhammapnight"), Jump ("MCRoomNight")]
    key "K_RCTRL" action [renpy.hide_screen("cockhammapnight"), Jump ("MCRoomNight")]
    key "keyup_K_RCTRL" action [renpy.hide_screen("cockhammapnight"), Jump ("MCRoomNight")]        
    modal True    
    button:
        xpos 1730
        ypos 1020
        xysize(145, 40)        
        action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("MCRoomNight")]
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
    button:
        xpos 257
        ypos 426
        xysize(130, 125)        
        action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("OfficeCCPD")]
    if locmayors and mission08triadwin == False:
        button:
            xpos 369
            ypos 795
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("MafiaLair")]
    if locstallion and mission06win == False:
        button:
            xpos 48
            ypos 726
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("StallionNight")]
    if loclingerie:
        button:
            xpos 923
            ypos 287
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("LingerieStore")]
    if loclois:
        button:
            xpos 344
            ypos 285
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("LoisFlat")]
    if locsirens and mission03 and mission03end == False and spokebarbaramission03 == False:
        button:
            xpos 1105
            ypos 543
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("SirensClub")]
    if locquiff:
        button:
            xpos 1470
            ypos 380
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("HarleyPlace")]
    if locmayors and mission08mafiawin == False:
        button:
            xpos 578
            ypos 722
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("ChineseTriad")]
    if locarkham:
        button:
            xpos 1282
            ypos 238
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("ArkhamAsylum")]
    if locnazi and quest07end == False:
        button:
            xpos 1474
            ypos 541
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("NaziCompound")]
    if locembassy:
        button:
            xpos 1235
            ypos 705
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("SovietEmbassy")]
    if preloccatcave or loccatcave:
        button:
            xpos 611
            ypos 195
            xysize(130, 125)        
            action [renpy.hide_screen("cockhammapnight"), SetVariable("cockhamnight", False), Jump ("PreCatCave")]

    

