init python:
    def random_1_5(trans, st, at):
        global r_int_1_5

        if st >= r_int_1_5:
            r_int_1_5 = renpy.random.randint(1,5)
            return None
        else:
            return 0
init python:
    import random

    def pause_trans(trans, st, at, pi=3, po=7):
        if st > pi:
            return None
        return float(pi + random.random() * po)

init:
    image introstudidle = "icons/introstudidle.png"
    image introstudhover = "icons/introstudhover.png"
    image introstrengthidle = "icons/introstrengthidle.png"
    image introstrengthhover = "icons/introstrengthhover.png"
    image introseductionidle = "icons/introseductionidle.png"
    image introseductionhover = "icons/introseductionhover.png"
    image introsensesidle = "icons/introsensesidle.png"
    image introsenseshover = "icons/introsenseshover.png"
    image introcombatidle = "icons/introcombatidle.png"
    image introcombathover = "icons/introcombathover.png"
    image introagilityidle = "icons/introagilityidle.png"
    image introagilityhover = "icons/introagilityhover.png"

    image froststrip00b = im.FactorScale("intro/froststrip00.png", 0.5)
    image widowoffice01b = im.FactorScale("intro/widowoffice01.png", 0.5)
    image widowoffice02b = im.FactorScale("intro/widowoffice02.png", 0.5)
    image widowoffice03b = im.FactorScale("intro/widowoffice03.png", 0.5)
    image widowoffice05b = im.FactorScale("intro/widowoffice05.png", 0.5)
    image widowoffice06b = im.FactorScale("intro/widowoffice06.png", 0.5)
    
    image goodbutton01 = "icons/goodbutton.png"
    image goodbutton02 = "icons/goodbutton.png"
    image goodbutton03 = "icons/goodbutton.png"
    image goodbutton04 = "icons/goodbutton.png"
    image goodbutton05 = "icons/goodbutton.png"
    image goodbutton06 = "icons/goodbutton.png"
    image goodbutton07 = "icons/goodbutton.png"
    image goodbutton08 = "icons/goodbutton.png"
    image goodbutton09 = "icons/goodbutton.png"
    image goodbutton10 = "icons/goodbutton.png"

    image evilbutton01 = "icons/evilbutton.png"
    image evilbutton02 = "icons/evilbutton.png"
    image evilbutton03 = "icons/evilbutton.png"
    image evilbutton04 = "icons/evilbutton.png"
    image evilbutton05 = "icons/evilbutton.png"
    image evilbutton06 = "icons/evilbutton.png"
    image evilbutton07 = "icons/evilbutton.png"
    image evilbutton08 = "icons/evilbutton.png"
    image evilbutton09 = "icons/evilbutton.png"
    image evilbutton10 = "icons/evilbutton.png"
    
    image allleaguechairzoom = im.FactorScale("intro/allleaguechair.jpg",2.0)
    image allleaguechair blurred = im.Blur("intro/allleaguechair.jpg", 1.5)
    image allleaguepiano blurred = im.Blur("intro/allleaguepiano.jpg", 1.5)

    image widowofficewiggle = Movie(play="intro/widowwiggle.webm", side_mask=True)    
    image froststripwiggle = Movie(play="intro/frostwiggle.webm", side_mask=True)    

    image frostofficelick = Movie(play="intro/frostlick.webm", loop=True, size=(1920,1080))    
    image frostofficetitfuck = Movie(play="intro/frosttitfuck.webm", side_mask=True)    

    image frosttitfuckbackgroundb = im.FactorScale("intro/frosttitfuckbackground.jpg", 1.1)

    image blackwigglevideo = Movie(play="v01/blackwiggle.webm", side_mask=True)    

    image auditasswigglevideo = Movie(play="v01/auditasswiggle.webm", side_mask=True)    

    image sawyerfootslowvideo = Movie(play="v01/sawyerfootslow.webm", loop=True, size=(1920,1080))    
    image sawyerfootfastvideo = Movie(play="v01/sawyerfootfast.webm", loop=True, size=(1920,1080))    

    image sophiaslowvideo = Movie(play="v01/sophiasex.webm", loop=True, size=(1920,1080))    
    image sophiafastvideo = Movie(play="v01/sophiapound.webm", loop=True, size=(1920,1080))    

    image twistergrindvideo = Movie(play="v01/twistergrind.webm", loop=True, size=(1920,1080))
    image milfgymvideo = Movie(play="v02/milftreadmill.webm", loop=True, size=(1920,1080))
    image milfgymvideo02 = Movie(play="v02/milftreadboobs.webm", loop=True, size=(1920,1080))
    image milfgymvideo03 = Movie(play="v02/milftreadnude.webm", loop=True, size=(1920,1080))
    image milfgymvideo04 = Movie(play="v02/milftreadnudeslow.webm", loop=True, size=(1920,1080))
    image milfgymvideo05 = Movie(play="v02/milftreadnight.webm", loop=True, size=(1920,1080))
    image milfgymvideo06 = Movie(play="v02/milftreadnightslow.webm", loop=True, size=(1920,1080))
    image milfgymvideo07 = Movie(play="v02/milftreadboobsnight.webm", loop=True, size=(1920,1080))
    image wondergymvideo = Movie(play="v02/gymwonder.webm", loop=True, size=(1920,1080))
    image gymbeastvideo = Movie(play="v02/gymwonderbeast.webm", loop=True, size=(1920,1080))
    image gymbeastpovvideo = Movie(play="v02/gymwonderbeastpov.webm", loop=True, size=(1920,1080))
    image gymmcliftvideo = Movie(play="v02/gymmclift.webm", loop=True, size=(1920,1080))
    image gymmcliftnudevideo = Movie(play="v02/gymmcliftnude.webm", loop=True, size=(1920,1080))
    image gymmclifthardvideo = Movie(play="v02/gymmclifterect.webm", loop=True, size=(1920,1080))
    image gymmclifterectingvideo = Movie(play="v02/gymmclifterecting.webm", loop=False, size=(1920,1080))
    image gymmcpower01video = Movie(play="v02/gymmcpowerlift.webm", loop=True, size=(1920,1080))
    image gymmcpowershortvideo = Movie(play="v02/gympoweranimshort.webm", size=(1920,1080))
    image gymmcpower02video = Movie(play="v02/gymmcpowerlift02.webm", loop=True, size=(1920,1080))
    image gympowerliftvideo = Movie(play="v02/gympowerliftanim.webm", loop=True, size=(1920,1080))

    image auditmunchvideo = Movie(play="v02/auditmunch.webm", loop=True, size=(1920,1080))
    image auditmassage02video = Movie(play="v02/audittitsupdown.webm", loop=True, size=(1920,1080))
    image auditmassage01video = Movie(play="v02/audittitsmassage.webm", loop=True, size=(1920,1080))

    image milfsaunablowslowvideo = Movie(play="v02/milfsaunablowslow.webm", loop=True, size=(1920,1080))    
    image milfsaunablowfastvideo = Movie(play="v02/milfsaunablowfast.webm", loop=True, size=(1920,1080))    
    image poolmilftonguevideo = Movie(play="v02/milfsaunatongue.webm", loop=True, size=(1920,1080))    

    image luthorlickcasevideo = Movie(play="v02/luthorlickcase.webm", loop=True, size=(1920,1080))
    image luthorfuckcasevideo = Movie(play="v02/luthorfuckcase.webm", loop=True, size=(1920,1080))
    image luthorfuckcasepussyvideo = Movie(play="v02/luthorfuckcasepussy.webm", loop=True, size=(1920,1080))
    image luthordanianalslowvideo = Movie(play="v02/danianalslow.webm", loop=True, size=(1920,1080))
    image luthordanianalfastvideo = Movie(play="v02/danianalfast.webm", loop=True, size=(1920,1080))

    image loissuckslowvideo = Movie(play="v02/loissuckanimslow.webm", loop=True, size=(1920,1080))
    image loissuckfastvideo = Movie(play="v02/loissuckanimfast.webm", loop=True, size=(1920,1080))
    image loissofaslowvideo = Movie(play="v02/loissofaanimslow.webm", loop=True, size=(1920,1080))
    image loissofafastvideo = Movie(play="v02/loissofaanimfast.webm", loop=True, size=(1920,1080))

    image harleytitsvideo = Movie(play="v02/harleytits.webm", side_mask=True)    
    image harleyassvideo = Movie(play="v02/harleyass.webm", side_mask=True)    
    image harleysidevideo = Movie(play="v02/harleyside.webm", side_mask=True)    
    image harleyassfastvideo = Movie(play="v02/harleyassfast.webm", side_mask=True)    
    image harleysidefastvideo = Movie(play="v02/harleysidefast.webm", side_mask=True)    
    image harleyassveryvideo = Movie(play="v02/harleyassvery.webm", side_mask=True)    
    image harleysideveryvideo = Movie(play="v02/harleysidevery.webm", side_mask=True)    

    image honokalickvideo = Movie(play="v02/honokalick.webm", loop=True, size=(1920,1080))    
    image honokafuckfastvideo = Movie(play="v02/honokafuckfast.webm", side_mask=True)    
    image honokafuckslowvideo = Movie(play="v02/honokafuckslow.webm", side_mask=True)    
    image honokafacefastvideo = Movie(play="v02/honokafacefast.webm", side_mask=True)    
    image honokafaceslowvideo = Movie(play="v02/honokafaceslow.webm", side_mask=True)    
    image catherineshowerfastvideo = Movie(play="v02/catherinefuckfast.webm", loop=True, size=(1920,1080))    
    image catherineshowerslowvideo = Movie(play="v02/catherinefuckslow.webm", loop=True, size=(1920,1080))    

    image widowshowerslowvideo = Movie(play="v021/widowshowerslow.webm", loop=True, size=(1920,1080))    
    image widowshowerfastvideo = Movie(play="v021/widowshowerfast.webm", loop=True, size=(1920,1080))    
    image widowshowerassslowvideo = Movie(play="v021/widowshowerassslow.webm", loop=True, size=(1920,1080))    
    image widowshowerassfastvideo = Movie(play="v021/widowshowerassfast.webm", loop=True, size=(1920,1080))    
    image widowshowerfaceslowvideo = Movie(play="v021/widowpoolfaceslow.webm", loop=True, size=(1920,1080))    
    image widowshowerfacefastvideo = Movie(play="v021/widowpoolfacefast.webm", loop=True, size=(1920,1080))    
    
    image wonderblowslowvideo = Movie(play="v021/wonderblowslow.webm", loop=True, size=(1920,1080))    
    image wonderblowfastvideo = Movie(play="v021/wonderblowfast.webm", loop=True, size=(1920,1080))    

    image katehandslowvideo = Movie(play="v021/katehandslow.webm", loop=True, size=(1920,1080))    
    image katehandfastvideo = Movie(play="v021/katehandfast.webm", loop=True, size=(1920,1080))    

    image powerfootjobslowvideo = Movie(play="v021/powerfootjobslow.webm", loop=True, size=(1920,1080))    
    image powerfootjobfastvideo = Movie(play="v021/powerfootjobfast.webm", loop=True, size=(1920,1080))    
    image powerfootsceneslowvideo = Movie(play="v021/powerfootsceneslow.webm", loop=True, size=(1920,1080))    
    image powerfootscenefastvideo = Movie(play="v021/powerfootscenefast.webm", loop=True, size=(1920,1080))    

    image laratemplewankslowvideo = Movie(play="v021/larawanksceneslow.webm", loop=True, size=(1920,1080))    
    image laratemplewankfastvideo = Movie(play="v021/larawankscenefast.webm", loop=True, size=(1920,1080))    
    image laratemplesideslowvideo = Movie(play="v021/larawankpovslow.webm", loop=True, size=(1920,1080))    
    image laratemplesidefastvideo = Movie(play="v021/larawankpovfast.webm", loop=True, size=(1920,1080))    
    image laratemplefuckslowvideo = Movie(play="v021/laratemplefuckslow.webm", loop=True, size=(1920,1080))    
    image laratemplefuckfastvideo = Movie(play="v021/laratemplefuckfast.webm", loop=True, size=(1920,1080))    
    image laratempledownslowvideo = Movie(play="v021/laratemplefuckdownslow.webm", loop=True, size=(1920,1080))    
    image laratempledownfastvideo = Movie(play="v021/laratemplefuckdownfast.webm", loop=True, size=(1920,1080))    

    image gillianfuckslowvideo = Movie(play="v022/gillianfuckslow.webm", loop=True, size=(1920,1080))    
    image gillianfuckfastvideo = Movie(play="v022/gillianfuckfast.webm", loop=True, size=(1920,1080))    
    image alien02fuckslowvideo = Movie(play="v022/alien02fuckslow.webm", loop=True, size=(1920,1080))    
    image alien02fuckfastvideo = Movie(play="v022/alien02fuckfast.webm", loop=True, size=(1920,1080))    
    image alien02fuckzoomslowvideo = Movie(play="v022/alien02fuckzoomslow.webm", loop=True, size=(1920,1080))    
    image alien02fuckzoomfastvideo = Movie(play="v022/alien02fuckzoomfast.webm", loop=True, size=(1920,1080))    
    image alien01fuckslowvideo = Movie(play="v022/alien01fuckslow.webm", loop=True, size=(1920,1080))    
    image alien01fuckfastvideo = Movie(play="v022/alien01fuckfast.webm", loop=True, size=(1920,1080))    
    image alien01fuckzoomslowvideo = Movie(play="v022/alien01fuckzoomslow.webm", loop=True, size=(1920,1080))    
    image alien01fuckzoomfastvideo = Movie(play="v022/alien01fuckzoomfast.webm", loop=True, size=(1920,1080))    

    image milfassfuckslowvideo = Movie(play="v022/milfassfuckslow.webm", loop=True, size=(1920,1080))    
    image milfassfuckfastvideo = Movie(play="v022/milfassfuckfast.webm", loop=True, size=(1920,1080))    
    image milfassfuckfrontslowvideo = Movie(play="v022/milfassfuckfrontslow.webm", loop=True, size=(1920,1080))    
    image milfassfuckfrontfastvideo = Movie(play="v022/milfassfuckfrontfast.webm", loop=True, size=(1920,1080))    
    image milftitfuckslowvideo = Movie(play="v022/milftitfuckslow.webm", loop=True, size=(1920,1080))    
    image milftitfuckfastvideo = Movie(play="v022/milftitfuckfast.webm", loop=True, size=(1920,1080))    
    image milftitfuckfrontslowvideo = Movie(play="v022/milftitfuckfrontslow.webm", loop=True, size=(1920,1080))    
    image milftitfuckfrontfastvideo = Movie(play="v022/milftitfuckfrontfast.webm", loop=True, size=(1920,1080))    

    image sirensbarbshortslowvideo = Movie(play="v022/sirensbarbshortslow.webm", loop=True, size=(1920,1080))    
    image sirensbarbshortfastvideo = Movie(play="v022/sirensbarbshortfast.webm", loop=True, size=(1920,1080))    
    image sirensbarbslowvideo = Movie(play="v022/sirensbarbslow.webm", loop=True, size=(1920,1080))    
    image sirensbarbfastvideo = Movie(play="v022/sirensbarbfast.webm", loop=True, size=(1920,1080))    
    image sirensbarbshortpovslowvideo = Movie(play="v022/sirensbarbshortpovslow.webm", loop=True, size=(1920,1080))    
    image sirensbarbshortpovfastvideo = Movie(play="v022/sirensbarbshortpovfast.webm", loop=True, size=(1920,1080))    
    image sirensbarbpovslowvideo = Movie(play="v022/sirensbarbpovslow.webm", loop=True, size=(1920,1080))    
    image sirensbarbpovfastvideo = Movie(play="v022/sirensbarbpovfast.webm", loop=True, size=(1920,1080))    
    image sirenstabslowvideo = Movie(play="v022/sirenstabslow.webm", loop=True, size=(1920,1080))    
    image sirenstabfastvideo = Movie(play="v022/sirenstabfast.webm", loop=True, size=(1920,1080))    
    image sirenstabpovslowvideo = Movie(play="v022/sirenstabpovslow.webm", loop=True, size=(1920,1080))    
    image sirenstabpovfastvideo = Movie(play="v022/sirenstabpovfast.webm", loop=True, size=(1920,1080))    

    image angelajerkslowvideo = Movie(play="v022/angelajerkslow.webm", loop=True, size=(1920,1080))    
    image angelajerkfastvideo = Movie(play="v022/angelajerkfast.webm", loop=True, size=(1920,1080))    
    image demonatitfuckslowvideo = Movie(play="v023/demonatitfuckslow.webm", loop=True, size=(1920,1080))    
    image demonatitfuckfastvideo = Movie(play="v023/demonatitfuckfast.webm", loop=True, size=(1920,1080))    

    image wonderstroheimfuckslowvideo = Movie(play="v023/wonderstroheimfuckslow.webm", loop=True, size=(1920,1080))    
    image wonderstroheimfuckfastvideo = Movie(play="v023/wonderstroheimfuckfast.webm", loop=True, size=(1920,1080))    
    image wonderstroheimhardslowvideo = Movie(play="v023/wonderstroheimhardslow.webm", loop=True, size=(1920,1080))    
    image wonderstroheimhardfastvideo = Movie(play="v023/wonderstroheimhardfast.webm", loop=True, size=(1920,1080))    

    image powerpoolhjslowvideo = Movie(play="v023/powerpoolhjslow.webm", loop=True, size=(1920,1080))    
    image powerpoolhjfastvideo = Movie(play="v023/powerpoolhjfast.webm", loop=True, size=(1920,1080))    
    image powerpoolhardhjslowvideo = Movie(play="v023/powerpoolhardhjslow.webm", loop=True, size=(1920,1080))    
    image powerpoolhardhjfastvideo = Movie(play="v023/powerpoolhardhjfast.webm", loop=True, size=(1920,1080))    
    image powerpoolbreastslowvideo = Movie(play="v023/powerpoolbreastslow.webm", loop=True, size=(1920,1080))    
    image powerpoolbreastfastvideo = Movie(play="v023/powerpoolbreastfast.webm", loop=True, size=(1920,1080))    

    image psychfuckslowvideo = Movie(play="v023/psychfuckslow.webm", side_mask=True)    
    image psychfuckfastvideo = Movie(play="v023/psychfuckfast.webm", side_mask=True)    
    image psychfuckslowpovvideo = Movie(play="v023/psychfuckslowpov.webm", side_mask=True)    
    image psychfuckfastpovvideo = Movie(play="v023/psychfuckfastpov.webm", side_mask=True)    

    image hulkpreblowslowvideo = Movie(play="v023/hulkpreblowslow.webm", loop=True, size=(1920,1080))    
    image hulkpreblowfastvideo = Movie(play="v023/hulkpreblowfast.webm", loop=True, size=(1920,1080))    
    image hulkblowslowvideo = Movie(play="v023/hulkblowslow.webm", loop=True, size=(1920,1080))    
    image hulkblowfastvideo = Movie(play="v023/hulkblowfast.webm", loop=True, size=(1920,1080))    
    image hulkblowpovslowvideo = Movie(play="v023/hulkblowpovslow.webm", loop=True, size=(1920,1080))    
    image hulkblowpovfastvideo = Movie(play="v023/hulkblowpovfast.webm", loop=True, size=(1920,1080))    
    image hulkfuckslowvideo = Movie(play="v023/hulkfuckslow.webm", loop=True, size=(1920,1080))    
    image hulkfuckfastvideo = Movie(play="v023/hulkfuckfast.webm", loop=True, size=(1920,1080))    
    image hulkfuckharderslowvideo = Movie(play="v023/hulkfuckhardslow.webm", loop=True, size=(1920,1080))    
    image hulkfuckharderfastvideo = Movie(play="v023/hulkfuckhardfast.webm", loop=True, size=(1920,1080))    
    image hulkanalfuckslowvideo = Movie(play="v023/hulkanalfuckslow.webm", loop=True, size=(1920,1080))    
    image hulkanalfuckfastvideo = Movie(play="v023/hulkanalfuckfast.webm", loop=True, size=(1920,1080))    
    image hulkanalfuckbackslowvideo = Movie(play="v023/hulkanalfuckbackslow.webm", loop=True, size=(1920,1080))    
    image hulkanalfuckbackfastvideo = Movie(play="v023/hulkanalfuckbackfast.webm", loop=True, size=(1920,1080))    

    image powersuperslowvideo = Movie(play="v03/powersuperslow.webm", loop=True, size=(1920,1080))    
    image powersuperfastvideo = Movie(play="v03/powersuperfast.webm", loop=True, size=(1920,1080))    
    image powersuperfrontslowvideo = Movie(play="v03/powersuperfrontslow.webm", loop=True, size=(1920,1080))    
    image powersuperfrontfastvideo = Movie(play="v03/powersuperfrontfast.webm", siloop=True, size=(1920,1080))    

    image blowsuperslowvideo = Movie(play="v03/blowsuperslow.webm", loop=True, size=(1920,1080))    
    image blowsuperfastvideo = Movie(play="v03/blowsuperfast.webm", loop=True, size=(1920,1080))    
    image blowsupersideslowvideo = Movie(play="v03/blowsupersideslow.webm", loop=True, size=(1920,1080))    
    image blowsupersidefastvideo = Movie(play="v03/blowsupersidefast.webm", loop=True, size=(1920,1080))    

    image wanksuperslowvideo = Movie(play="v03/wanksuperslow.webm", loop=True, size=(1920,1080))    
    image wanksuperfastvideo = Movie(play="v03/wanksuperfast.webm", loop=True, size=(1920,1080))    
    image wanksuperpovslowvideo = Movie(play="v03/wanksuperpovslow.webm", loop=True, size=(1920,1080))    
    image wanksuperpovfastvideo = Movie(play="v03/wanksuperpovfast.webm", loop=True, size=(1920,1080))    

    image superpoolslowvideo = Movie(play="v03/superpoolslow.webm", loop=True, size=(1920,1080))    
    image superpoolfastvideo = Movie(play="v03/superpoolfast.webm", loop=True, size=(1920,1080))    
    image superpoolpovslowvideo = Movie(play="v03/superpoolslowpov.webm", loop=True, size=(1920,1080))    
    image superpoolpovfastvideo = Movie(play="v03/superpoolfastpov.webm", loop=True, size=(1920,1080))    

    image supergirlcrunchslowvideo = Movie(play="v03/supergirlcrunchslow.webm", loop=True, size=(1920,1080))    
    image supergirlcrunchfastvideo = Movie(play="v03/supergirlcrunchfast.webm", loop=True, size=(1920,1080))    
    image supergirlgymsensesvideo = Movie(play="v03/supergirlgymsenses.webm", loop=True, size=(1920,1080))    

    image auditjacuzzislowvideo = Movie(play="v03/auditfuckjacuzzislow.webm", loop=True, size=(1920,1080))    
    image auditjacuzzifastvideo = Movie(play="v03/auditfuckjacuzzifast.webm", loop=True, size=(1920,1080))    
    image auditjacuzzipovslowvideo = Movie(play="v03/auditpovjacuzzislow.webm", loop=True, size=(1920,1080))    
    image auditjacuzzipovfastvideo = Movie(play="v03/auditpovjacuzzifast.webm", loop=True, size=(1920,1080))    

    image auditsuckslowvideo = Movie(play="v03/auditsuckslow.webm", loop=True, size=(1920,1080))    
    image auditsuckfastvideo = Movie(play="v03/auditsuckfast.webm", loop=True, size=(1920,1080))    

    image wonderanalslowvideo = Movie(play="v03/wonderanalslow.webm", loop=True, size=(1920,1080))    
    image wonderanalfastvideo = Movie(play="v03/wonderanalfast.webm", loop=True, size=(1920,1080))    
    image wonderanalfrontslowvideo = Movie(play="v03/wonderanalzoomslow.webm", loop=True, size=(1920,1080))    
    image wonderanalfrontfastvideo = Movie(play="v03/wonderanalzoomfast.webm", loop=True, size=(1920,1080))    
    image wonderanalhardvideo = Movie(play="v03/wonderanalhard.webm", loop=True, size=(1920,1080))    
    image wonderanalfronthardvideo = Movie(play="v03/wonderanalzoomhard.webm", loop=True, size=(1920,1080))    

    image gymmilfsquatvideo = Movie(play="v03/gymmilfsquat.webm", loop=True, size=(1920,1080))    
    image gymmilfsquatnakedslowvideo = Movie(play="v03/gymmilfsquatnakedslow.webm", loop=True, size=(1920,1080))    
    image gymmilfsquatnakedfastvideo = Movie(play="v03/gymmilfsquatnakedfast.webm", loop=True, size=(1920,1080))    

    image milfmassageslowvideo = Movie(play="v031/milfmassageslow.webm", loop=True, size=(1920,1080))    
    image milfmassagefastvideo = Movie(play="v031/milfmassagefast.webm", loop=True, size=(1920,1080))    
    image milfmassagepovslowvideo = Movie(play="v031/milfmassagepovslow.webm", loop=True, size=(1920,1080))    
    image milfmassagepovfastvideo = Movie(play="v031/milfmassagepovfast.webm", loop=True, size=(1920,1080))    

    image larapoollickvideo = Movie(play="v031/larapoollick.webm", loop=True, size=(1920,1080))    
    image larapoolslowvideo = Movie(play="v031/larapoolslow.webm", loop=True, size=(1920,1080))    
    image larapoolfastvideo = Movie(play="v031/larapoolfast.webm", loop=True, size=(1920,1080))    
    image larapoolpovslowvideo = Movie(play="v031/larapoolpovslow.webm", loop=True, size=(1920,1080))    
    image larapoolpovfastvideo = Movie(play="v031/larapoolpovfast.webm", loop=True, size=(1920,1080))    

    image gymmccurlvideo = Movie(play="v031/gymmccurl.webm", loop=True, size=(1920,1080))
    image gymmccurlsoftvideo = Movie(play="v032/gymmccurlsoft.webm", loop=True, size=(1920,1080))
    image gymmccurlhardvideo = Movie(play="v032/gymmccurlhard.webm", loop=True, size=(1920,1080))
    image gymmccurlgettingvideo = Movie(play="v032/gymmccurlgetting.webm", loop=False, size=(1920,1080))
    image mccurltitslowvideo = Movie(play="v032/mccurltitslow.webm", loop=True, side_mask=True)
    image mccurltitfastvideo = Movie(play="v032/mccurltitfast.webm", loop=True, side_mask=True)
    image mccurltitslowsensesvideo = Movie(play="v032/mccurltitslowsenses.webm", loop=True, side_mask=True)
    image mccurltitfastsensesvideo = Movie(play="v032/mccurltitfastsenses.webm", loop=True, side_mask=True)

    image doublefuckslowvideo = Movie(play="v031/doublefuckslow.webm", loop=True, size=(1920,1080))    
    image doublefuckfastvideo = Movie(play="v031/doublefuckfast.webm", loop=True, size=(1920,1080))    
    image doublefuckslowpovvideo = Movie(play="v031/doublefuckslowpov.webm", loop=True, size=(1920,1080))    
    image doublefuckfastpovvideo = Movie(play="v031/doublefuckfastpov.webm", loop=True, size=(1920,1080))    

    image doublefuckcumslowvideo = Movie(play="v031/doublefuckcumslow.webm", loop=True, size=(1920,1080))    
    image doublefuckcumfastvideo = Movie(play="v031/doublefuckcumfast.webm", loop=True, size=(1920,1080))    
    image doublefuckcumpovslowvideo = Movie(play="v031/doublefuckcumpovslow.webm", loop=True, size=(1920,1080))    
    image doublefuckcumpovfastvideo = Movie(play="v031/doublefuckcumpovfast.webm", loop=True, size=(1920,1080))    

    image doublefuckmilfswitchvideo = Movie(play="v031/doublefuckmilfswitch.webm", loop=False, size=(1920,1080))    
    image doublefucksupswitchvideo = Movie(play="v031/doublefucksupswitch.webm", loop=False, size=(1920,1080))    
    image doublefuckmilfswitchcumvideo = Movie(play="v031/doublefuckmilfswitchcum.webm", loop=False, size=(1920,1080))    
    image doublefucksupswitchcumvideo = Movie(play="v031/doublefucksupswitchcum.webm", loop=False, size=(1920,1080))    

    image doublefucksupslowvideo = Movie(play="v031/doublefucksupslow.webm", loop=True, size=(1920,1080))    
    image doublefucksupfastvideo = Movie(play="v031/doublefucksupfast.webm", loop=True, size=(1920,1080))    
    image doublefucksupcumslowvideo = Movie(play="v031/doublefucksupcumslow.webm", loop=True, size=(1920,1080))    
    image doublefucksupcumfastvideo = Movie(play="v031/doublefucksupcumfast.webm", loop=True, size=(1920,1080))    

    image doublefucksupslowpovvideo = Movie(play="v031/doublefucksupslowpov.webm", loop=True, size=(1920,1080))    
    image doublefucksupfastpovvideo = Movie(play="v031/doublefucksupfastpov.webm", loop=True, size=(1920,1080))    
    image doublefucksupcumpovslowvideo = Movie(play="v031/doublefucksupcumpovslow.webm", loop=True, size=(1920,1080))    
    image doublefucksupcumpovfastvideo = Movie(play="v031/doublefucksupcumpovfast.webm", loop=True, size=(1920,1080))    

    image lindasuckslowvideo = Movie(play="v031/lindasuckslow.webm", loop=True, size=(1920,1080))    
    image lindasuckfastvideo = Movie(play="v031/lindasuckfast.webm", loop=True, size=(1920,1080))    
    image doublethroatslowvideo = Movie(play="v031/doublethroatslow.webm", loop=True, size=(1920,1080))    
    image doublethroatfastvideo = Movie(play="v031/doublethroatfast.webm", loop=True, size=(1920,1080))    
    image massagelickthreesomevideo = Movie(play="v031/massagelickthreesome.webm", loop=True, size=(1920,1080))    
    image mommassagelickvideo = Movie(play="v031/mommassagelick.webm", loop=True, size=(1920,1080))    

    image milfloneslowvideo = Movie(play="v031/milfloneslow.webm", loop=True, size=(1920,1080))    
    image milflonefastvideo = Movie(play="v031/milflonefast.webm", loop=True, size=(1920,1080))    
    image milfloneslowpovvideo = Movie(play="v031/milfloneslowpov.webm", loop=True, size=(1920,1080))    
    image milflonefastpovvideo = Movie(play="v031/milflonefastpov.webm", loop=True, size=(1920,1080))    

    image milflonecumslowvideo = Movie(play="v031/milflonecumslow.webm", loop=True, size=(1920,1080))    
    image milflonecumfastvideo = Movie(play="v031/milflonecumfast.webm", loop=True, size=(1920,1080))
    image milflonecumpovslowvideo = Movie(play="v031/milflonepovcumslow.webm", loop=True, size=(1920,1080))    
    image milflonecumpovfastvideo = Movie(play="v031/milflonepovcumfast.webm", loop=True, size=(1920,1080))    
    
    image loisdildoslowvideo = Movie(play="v031/loisdildoslow.webm", loop=True, size=(1920,1080))    
    image loisdildofastvideo = Movie(play="v031/loisdildofast.webm", loop=True, size=(1920,1080))    
    image loisdildofrontslowvideo = Movie(play="v031/loisdildofrontslow.webm", loop=True, size=(1920,1080))    
    image loisdildofrontfastvideo = Movie(play="v031/loisdildofrontfast.webm", loop=True, size=(1920,1080))    

    image mccurlballsuckvideo = Movie(play="v032/mccurlballsuck.webm", loop=True, size=(1920,1080))    

    image widowblowshortslowvideo = Movie(play="v032/widowblowshortslow.webm", loop=True, size=(1920,1080))    
    image widowblowshortfastvideo = Movie(play="v032/widowblowshortfast.webm", loop=True, size=(1920,1080))    
    image widowblowhardslowvideo = Movie(play="v032/widowblowhardslow.webm", loop=True, size=(1920,1080))    
    image widowblowhardfastvideo = Movie(play="v032/widowblowhardfast.webm", loop=True, size=(1920,1080))    
    image widowblowshortpovslowvideo = Movie(play="v032/widowblowshortpovslow.webm", loop=True, size=(1920,1080))    
    image widowblowshortpovfastvideo = Movie(play="v032/widowblowshortpovfast.webm", loop=True, size=(1920,1080))    
    image widowblowhardpovslowvideo = Movie(play="v032/widowblowhardpovslow.webm", loop=True, size=(1920,1080))    
    image widowblowhardpovfastvideo = Movie(play="v032/widowblowhardpovfast.webm", loop=True, size=(1920,1080))    

    image widowbedanalslowvideo = Movie(play="v032/widowbedanalslow.webm", loop=True, size=(1920,1080))    
    image widowbedanalfastvideo = Movie(play="v032/widowbedanalfast.webm", loop=True, size=(1920,1080))    
    image widowbedanalpovslowvideo = Movie(play="v032/widowbedanalpovslow.webm", loop=True, size=(1920,1080))    
    image widowbedanalpovfastvideo = Movie(play="v032/widowbedanalpovfast.webm", loop=True, size=(1920,1080))    
    
    image ivyfucksoftvideo = Movie(play="v032/ivyfucksoft.webm", loop=True, size=(1920,1080))    
    image ivyfucksoftsidevideo = Movie(play="v032/ivyfucksoftside.webm", loop=True, side_mask=True)    
    image ivyfuckhardslowvideo = Movie(play="v032/ivyfuckhardslow.webm", loop=True, size=(1920,1080))    
    image ivyfuckhardfastvideo = Movie(play="v032/ivyfuckhardfast.webm", loop=True, size=(1920,1080))    
    image ivyfuckhardsideslowvideo = Movie(play="v032/ivyfuckhardsideslow.webm", loop=True, side_mask=True)    
    image ivyfuckhardsidefastvideo = Movie(play="v032/ivyfuckhardsidefast.webm", loop=True, side_mask=True)    

    image ivytwerkslowvideo = Movie(play="v032/ivytwerkslow.webm", loop=True, size=(1920,1080))    
    image ivytwerkfastvideo = Movie(play="v032/ivytwerkfast.webm", loop=True, size=(1920,1080))    
    image ivytwerkfrontslowvideo = Movie(play="v032/ivytwerkfrontslow.webm", side_mask=True)    
    image ivytwerkfrontfastvideo = Movie(play="v032/ivytwerkfrontfast.webm", side_mask=True)    

    image ivyhumslowvideo = Movie(play="v032/ivyhumslow.webm", loop=True, size=(1920,1080))    
    image ivyhumfastvideo = Movie(play="v032/ivyhumfast.webm", loop=True, size=(1920,1080))    
    image ivyhumsideslowvideo = Movie(play="v032/ivyhumsideslow.webm", loop=True, size=(1920,1080))    
    image ivyhumsidefastvideo = Movie(play="v032/ivyhumsidefast.webm", loop=True, size=(1920,1080))    
    
    image ivytitslowvideo = Movie(play="v032/ivytitslow.webm", loop=True, size=(1920,1080))    
    image ivytitfastvideo = Movie(play="v032/ivytitfast.webm", loop=True, size=(1920,1080))    
    image ivytitfrontslowvideo = Movie(play="v032/ivytitfrontslow.webm", loop=True, size=(1920,1080))    
    image ivytitfrontfastvideo = Movie(play="v032/ivytitfrontfast.webm", loop=True, size=(1920,1080))    

    image sophiaboobgrowvideo = Movie(play="v032/sophiaboobgrow.webm", loop=False, size=(1920,1080))    
    image sophiaboobgrowslowvideo = Movie(play="v032/sophiaboobgrowslow.webm", loop=False, size=(1920,1080))    

    image sophiablowslowvideo = Movie(play="v032/sophiablowslow.webm", loop=True, size=(1920,1080))    
    image sophiablowfastvideo = Movie(play="v032/sophiablowfast.webm", loop=True, size=(1920,1080))    
    image sophiablowtopslowvideo = Movie(play="v032/sophiablowtopslow.webm", loop=True, size=(1920,1080))    
    image sophiablowtopfastvideo = Movie(play="v032/sophiablowtopfast.webm", loop=True, size=(1920,1080))    

    image sophiadeskslowvideo = Movie(play="v032/sophiadeskslow.webm", loop=True, size=(1920,1080))    
    image sophiadeskfastvideo = Movie(play="v032/sophiadeskfast.webm", loop=True, size=(1920,1080))    
    image sophiadeskpovslowvideo = Movie(play="v032/sophiadeskpovslow.webm", loop=True, size=(1920,1080))    
    image sophiadeskpovfastvideo = Movie(play="v032/sophiadeskpovfast.webm", loop=True, size=(1920,1080))    

    image sophialickslowvideo = Movie(play="v032/sophialickslow.webm", loop=True, size=(1920,1080))    
    image sophialickfastvideo = Movie(play="v032/sophialickfast.webm", loop=True, size=(1920,1080))    
    image sophialicksceneslowvideo = Movie(play="v032/sophialicksceneslow.webm", loop=True, size=(1920,1080))    
    image sophialickscenefastvideo = Movie(play="v032/sophialickscenefast.webm", loop=True, size=(1920,1080))    

    image sawyerlickslowvideo = Movie(play="v032/sawyerlickslow.webm", loop=True, size=(1920,1080))    
    image sawyerlickfastvideo = Movie(play="v032/sawyerlickfast.webm", loop=True, size=(1920,1080))    
    image sawyerlicksceneslowvideo = Movie(play="v032/sawyerlicksceneslow.webm", loop=True, size=(1920,1080))    
    image sawyerlickscenefastvideo = Movie(play="v032/sawyerlickscenefast.webm", loop=True, size=(1920,1080))    

    image sawyerwallslowvideo = Movie(play="v032/sawyerwallslow.webm", loop=True, side_mask=True)    
    image sawyerwallfastvideo = Movie(play="v032/sawyerwallfast.webm", loop=True, side_mask=True)    
    image sawyerwallpovslowvideo = Movie(play="v032/sawyerwallpovslow.webm", loop=True, size=(1920,1080))    
    image sawyerwallpovfastvideo = Movie(play="v032/sawyerwallpovfast.webm", loop=True, size=(1920,1080))    
    
    image daniwankslowvideo = Movie(play="v04/daniwankslow.webm", loop=True, size=(1920,1080))    
    image daniwankfastvideo = Movie(play="v04/daniwankfast.webm", loop=True, size=(1920,1080))    

    image powerfootslowvideo = Movie(play="v04/powerfootslow.webm", loop=True, size=(1920,1080))    
    image powerfootfastvideo = Movie(play="v04/powerfootfast.webm", loop=True, size=(1920,1080))    
    image powerfootsideslowvideo = Movie(play="v04/powerfootsideslow.webm", loop=True, size=(1920,1080))    
    image powerfootsidefastvideo = Movie(play="v04/powerfootsidefast.webm", loop=True, size=(1920,1080))    

    image powerrideslowvideo = Movie(play="v04/powerrideslow.webm", loop=True, size=(1920,1080))    
    image powerridefastvideo = Movie(play="v04/powerridefast.webm", loop=True, size=(1920,1080))    
    image powerridepovslowvideo = Movie(play="v04/powerridepovslow.webm", loop=True, size=(1920,1080))    
    image powerridepovfastvideo = Movie(play="v04/powerridepovfast.webm", loop=True, size=(1920,1080))    

    image powerdickslowvideo = Movie(play="v04/powerdickslow.webm", loop=True, size=(1920,1080))    
    image powerdickfastvideo = Movie(play="v04/powerdickfast.webm", loop=True, size=(1920,1080))    

    image auditupslowvideo = Movie(play="v04/auditupslow.webm", loop=True, size=(1920,1080))    
    image auditupfastvideo = Movie(play="v04/auditupfast.webm", loop=True, size=(1920,1080))    
    image auditupsideslowvideo = Movie(play="v04/auditupsideslow.webm", loop=True, size=(1920,1080))    
    image auditupsidefastvideo = Movie(play="v04/auditupsidefast.webm", loop=True, size=(1920,1080))    
    image auditsideslowvideo = Movie(play="v04/auditsideslow.webm", loop=True, size=(1920,1080))    
    image auditsidefastvideo = Movie(play="v04/auditsidefast.webm", loop=True, size=(1920,1080))    
    image auditpovslowvideo = Movie(play="v04/auditpovslow.webm", loop=True, size=(1920,1080))    
    image auditpovfastvideo = Movie(play="v04/auditpovfast.webm", loop=True, size=(1920,1080))    

    image demonafuckslowvideo = Movie(play="v04/demonaslow.webm", loop=True, size=(1920,1080))    
    image demonafuckfastvideo = Movie(play="v04/demonafast.webm", loop=True, size=(1920,1080))    
    image angelafuckslowvideo = Movie(play="v04/angelafuckslow.webm", loop=True, size=(1920,1080))    
    image angelafuckfastvideo = Movie(play="v04/angelafuckfast.webm", loop=True, size=(1920,1080))    

    image powershortslowvideo = Movie(play="v04/powerfuckslow.webm", loop=True, size=(1920,1080))    
    image powershortfastvideo = Movie(play="v04/powerfuckfast.webm", loop=True, size=(1920,1080))    
    image powerhardslowvideo = Movie(play="v04/powerhardslow.webm", loop=True, size=(1920,1080))    
    image powerhardfastvideo = Movie(play="v04/powerhardfast.webm", loop=True, size=(1920,1080))    
    image powershortpovslowvideo = Movie(play="v04/powerfuckpovslow.webm", loop=True, size=(1920,1080))    
    image powershortpovfastvideo = Movie(play="v04/powerfuckpovfast.webm", loop=True, size=(1920,1080))    
    image powerhardpovslowvideo = Movie(play="v04/powerhardpovslow.webm", loop=True, size=(1920,1080))    
    image powerhardpovfastvideo = Movie(play="v04/powerhardpovfast.webm", loop=True, size=(1920,1080))    
    image powerpullanimvideo = Movie(play="v04/powerpullanim.webm", loop=False, size=(1920,1080))    
    image powercowgirlslowvideo = Movie(play="v04/powercowgirlslow.webm", loop=True, size=(1920,1080))    
    image powercowgirlfastvideo = Movie(play="v04/powercowgirlfast.webm", loop=True, size=(1920,1080))    
    image powercowgirlfrontslowvideo = Movie(play="v04/powercowgirlfrontslow.webm", loop=True, size=(1920,1080))    
    image powercowgirlfrontfastvideo = Movie(play="v04/powercowgirlfrontfast.webm", loop=True, size=(1920,1080))    

    image ivyharemfuckslowvideo = Movie(play="v04/ivyharemfuckslow.webm", loop=True, size=(1920,1080))    
    image ivyharemfuckfastvideo = Movie(play="v04/ivyharemfuckfast.webm", loop=True, size=(1920,1080))    
    image ivyharemfuckpovslowvideo = Movie(play="v04/ivyharemfuckpovslow.webm", loop=True, size=(1920,1080))    
    image ivyharemfuckpovfastvideo = Movie(play="v04/ivyharemfuckpovfast.webm", loop=True, size=(1920,1080))    
    image ivyharemtitfuckslowvideo = Movie(play="v04/ivyharemtitfuckslow.webm", loop=True, size=(1920,1080))    
    image ivyharemtitfuckfastvideo = Movie(play="v04/ivyharemtitfuckfast.webm", loop=True, size=(1920,1080))    
    image ivyharemtitfuckfrontslowvideo = Movie(play="v04/ivyharemtitfuckfrontslow.webm", loop=True, size=(1920,1080))    
    image ivyharemtitfuckfrontfastvideo = Movie(play="v04/ivyharemtitfuckfrontfast.webm", loop=True, size=(1920,1080))    

    image wondersquatvideo = Movie(play="v041/wondersquat.webm", loop=True, size=(1920,1080))    
    image mcupcurlvideo = Movie(play="v041/mcupcurl.webm", loop=True, size=(1920,1080))    
    image wonderblowshortslowvideo = Movie(play="v041/wonderblowshortslow.webm", loop=True, size=(1920,1080))    
    image wonderblowshortfastvideo = Movie(play="v041/wonderblowshortfast.webm", loop=True, size=(1920,1080))    
    image wonderblowhardslowvideo = Movie(play="v041/wonderblowhardslow.webm", loop=True, size=(1920,1080))    
    image wonderblowhardfastvideo = Movie(play="v041/wonderblowhardfast.webm", loop=True, size=(1920,1080))    
    image wonderblowshortpovslowvideo = Movie(play="v041/wonderblowshortpovslow.webm", loop=True, size=(1920,1080))    
    image wonderblowshortpovfastvideo = Movie(play="v041/wonderblowshortpovfast.webm", loop=True, size=(1920,1080))    
    image wonderblowhardpovslowvideo = Movie(play="v041/wonderblowhardpovslow.webm", loop=True, size=(1920,1080))    
    image wonderblowhardpovfastvideo = Movie(play="v041/wonderblowhardpovfast.webm", loop=True, size=(1920,1080))    

    image kateanalslowvideo = Movie(play="v041/kateanalslow.webm", loop=True, size=(1920,1080))    
    image kateanalfastvideo = Movie(play="v041/kateanalfast.webm", loop=True, size=(1920,1080))    
    image kateanalbackslowvideo = Movie(play="v041/kateanalbackslow.webm", loop=True, size=(1920,1080))    
    image kateanalbackfastvideo = Movie(play="v041/kateanalbackfast.webm", loop=True, size=(1920,1080))    

    image milfwankgymslowvideo = Movie(play="v041/milfwankgymslow.webm", loop=True, size=(1920,1080))    
    image milfwankgymfastvideo = Movie(play="v041/milfwankgymfast.webm", loop=True, size=(1920,1080))    
    image milfwankgymfrontslowvideo = Movie(play="v041/milfwankgymfrontslow.webm", loop=True, size=(1920,1080))    
    image milfwankgymfrontfastvideo = Movie(play="v041/milfwankgymfrontfast.webm", loop=True, size=(1920,1080))    
    image milfhjgymslowvideo = Movie(play="v041/milfhjgymslow.webm", loop=True, size=(1920,1080))    
    image milfhjgymfastvideo = Movie(play="v041/milfhjgymfast.webm", loop=True, size=(1920,1080))    
    image milfhjgymfrontslowvideo = Movie(play="v041/milfhjgymfrontslow.webm", loop=True, size=(1920,1080))    
    image milfhjgymfrontfastvideo = Movie(play="v041/milfhjgymfrontfast.webm", loop=True, size=(1920,1080))    

    image cleopoolslowvideo = Movie(play="v041/cleopoolslow.webm", loop=True, size=(1920,1080))    
    image cleopoolfastvideo = Movie(play="v041/cleopoolfast.webm", loop=True, size=(1920,1080))    
    image cleopoolpovslowvideo = Movie(play="v041/cleopoolpovslow.webm", loop=True, size=(1920,1080))    
    image cleopoolpovfastvideo = Movie(play="v041/cleopoolpovfast.webm", loop=True, size=(1920,1080))    
    image cleosideslowvideo = Movie(play="v041/cleosideslow.webm", loop=True, size=(1920,1080))    
    image cleosidefastvideo = Movie(play="v041/cleosidefast.webm", loop=True, size=(1920,1080))    
    image cleosidepovslowvideo = Movie(play="v041/cleosidepovslow.webm", loop=True, size=(1920,1080))    
    image cleosidepovfastvideo = Movie(play="v041/cleosidepovfast.webm", loop=True, size=(1920,1080))    

    image robotassfuckslowvideo = Movie(play="v042/robotassfuckslow.webm", loop=True, size=(1920,1080))    
    image robotassfuckfastvideo  = Movie(play="v042/robotassfuckfast.webm", loop=True, size=(1920,1080))    
    image robotassfuckfrontslowvideo = Movie(play="v042/robotassfuckfrontslow.webm", loop=True, size=(1920,1080))    
    image robotassfuckfrontfastvideo = Movie(play="v042/robotassfuckfrontfast.webm", loop=True, size=(1920,1080))    

    image auditpushupvideo = Movie(play="v041/auditpushup.webm", loop=True, size=(1920,1080))    
    image auditpushupnudevideo = Movie(play="v041/auditpushupnude.webm", loop=True, size=(1920,1080))    
    image auditsitupvideo = Movie(play="v041/auditsitup.webm", loop=True, size=(1920,1080))    
    image auditsitupsweatvideo = Movie(play="v041/auditsitupsweat.webm", loop=True, size=(1920,1080))    

    image supershootanim01video = Movie(play="v042/supershootanim01.webm", loop=False, size=(1920,1080))    
    image supershootanim02video = Movie(play="v042/supershootanim02.webm", loop=False, size=(1920,1080))    
    image strapfuckslowvideo = Movie(play="v042/strapfuckslow.webm", loop=True, size=(1920,1080))    
    image strapfuckfastvideo = Movie(play="v042/strapfuckfast.webm", loop=True, size=(1920,1080))    
    image strapfuckpovslowvideo = Movie(play="v042/strapfuckpovslow.webm", loop=True, size=(1920,1080))    
    image strapfuckpovfastvideo = Movie(play="v042/strapfuckpovfast.webm", loop=True, size=(1920,1080))    

    image loissupershortslowvideo = Movie(play="v042/loissupershortslow.webm", loop=True, size=(1920,1080))    
    image loissupershortpovslowvideo = Movie(play="v042/loissupershortpovslow.webm", loop=True, size=(1920,1080))    
    image loissupershortfastvideo = Movie(play="v042/loissupershortfast.webm", loop=True, size=(1920,1080))    
    image loissupershortpovfastvideo = Movie(play="v042/loissupershortpovfast.webm", loop=True, size=(1920,1080))    
    image loissuperfuckslowvideo = Movie(play="v042/loissuperfuckslow.webm", loop=True, size=(1920,1080))    
    image loissuperfuckfastvideo = Movie(play="v042/loissuperfuckfast.webm", loop=True, size=(1920,1080))    
    image loissuperfuckpovslowvideo = Movie(play="v042/loissuperpovslow.webm", loop=True, size=(1920,1080))    
    image loissuperfuckpovfastvideo = Movie(play="v042/loissuperpovfast.webm", loop=True, size=(1920,1080))    

    image frostbedsuckslowvideo = Movie(play="v042/frostbedsuckslow.webm", loop=True, size=(1920,1080))    
    image frostbedsuckfastvideo = Movie(play="v042/frostbedsuckfast.webm", loop=True, size=(1920,1080))    
    image frostbedsuckpovslowvideo = Movie(play="v042/frostbedsuckpovslow.webm", loop=True, size=(1920,1080))    
    image frostbedsuckpovfastvideo = Movie(play="v042/frostbedsuckpovfast.webm", loop=True, size=(1920,1080))    
    image frostbedfuckslowvideo = Movie(play="v042/frostbedfuckslow.webm", loop=True, size=(1920,1080))    
    image frostbedfuckfastvideo = Movie(play="v042/frostbedfuckfast.webm", loop=True, size=(1920,1080))    

    image adawankslowvideo = Movie(play="v042/adawankslow.webm", loop=True, size=(1920,1080))    
    image adawankfastvideo = Movie(play="v042/adawankfast.webm", loop=True, size=(1920,1080))    
    image adawankcloserslowvideo = Movie(play="v042/adawankcloserslow.webm", loop=True, size=(1920,1080))    
    image adawankcloserfastvideo = Movie(play="v042/adawankcloserfast.webm", loop=True, size=(1920,1080))    
    image adafutawankslowvideo = Movie(play="v042/adafutawankslow.webm", loop=True, size=(1920,1080))    
    image adafutawankfastvideo = Movie(play="v042/adafutawankfast.webm", loop=True, size=(1920,1080))    
    image adafutawankcloserslowvideo = Movie(play="v042/adafutawankcloserslow.webm", loop=True, size=(1920,1080))    
    image adafutawankcloserfastvideo = Movie(play="v042/adafutawankcloserfast.webm", loop=True, size=(1920,1080))    

    image larawidowpoolwankslowvideo = Movie(play="v042/larawidowpoolwankslow.webm", loop=True, size=(1920,1080))    
    image larawidowpoolwankfastvideo = Movie(play="v042/larawidowpoolwankfast.webm", loop=True, size=(1920,1080))    

    image powerpoolpussyslowvideo = Movie(play="v05/powerpoolpussyslow.webm", loop=True, size=(1920,1080))    
    image powerpoolpussyfastvideo = Movie(play="v05/powerpoolpussyfast.webm", loop=True, size=(1920,1080))    
    image powerpoolpussycloserslowvideo = Movie(play="v05/powerpoolpussycloserslow.webm", loop=True, size=(1920,1080))    
    image powerpoolpussycloserfastvideo = Movie(play="v05/powerpoolpussycloserfast.webm", loop=True, size=(1920,1080))    

    image catwomanpussyslowvideo = Movie(play="v05/catwomanpussyslow.webm", loop=True, size=(1920,1080))    
    image catwomanpussyfastvideo = Movie(play="v05/catwomanpussyfast.webm", loop=True, size=(1920,1080))    
    image catwomanpussyharderslowvideo = Movie(play="v05/catwomanpussyharderslow.webm", loop=True, size=(1920,1080))    
    image catwomanpussyharderfastvideo = Movie(play="v05/catwomanpussyharderfast.webm", loop=True, size=(1920,1080))    
    
    image catanalshortslowvideo = Movie(play="v05/catanalshortslow.webm", loop=True, size=(1920,1080))    
    image catanalshortfastvideo = Movie(play="v05/catanalshortfast.webm", loop=True, size=(1920,1080))    
    image catanalshortpovslowvideo = Movie(play="v05/catanalshortpovslow.webm", loop=True, size=(1920,1080))    
    image catanalshortpovfastvideo = Movie(play="v05/catanalshortpovfast.webm", loop=True, size=(1920,1080))    
    image catanalslowvideo = Movie(play="v05/catanalslow.webm", loop=True, size=(1920,1080))    
    image catanalfastvideo = Movie(play="v05/catanalfast.webm", loop=True, size=(1920,1080))    
    image catanalpovslowvideo = Movie(play="v05/catanalpovslow.webm", loop=True, size=(1920,1080))    
    image catanalpovfastvideo = Movie(play="v05/catanalpovfast.webm", loop=True, size=(1920,1080))    

    image africashortslowvideo = Movie(play="v05/africashortslow.webm", loop=True, size=(1920,1080))    
    image africashortfastvideo = Movie(play="v05/africashortfast.webm", loop=True, size=(1920,1080))    
    image africashortfrontslowvideo = Movie(play="v05/africashortfrontslow.webm", loop=True, size=(1920,1080))    
    image africashortfrontfastvideo = Movie(play="v05/africashortfrontfast.webm", loop=True, size=(1920,1080))    
    image africaslowvideo = Movie(play="v05/africaslow.webm", loop=True, size=(1920,1080))    
    image africafastvideo = Movie(play="v05/africafast.webm", loop=True, size=(1920,1080))    
    image africafrontslowvideo = Movie(play="v05/africafrontslow.webm", loop=True, size=(1920,1080))    
    image africafrontfastvideo = Movie(play="v05/africafrontfast.webm", loop=True, size=(1920,1080))    

    image jasmineassfuckslowvideo = Movie(play="v05/jasmineassfuckslow.webm", loop=True, size=(1920,1080))    
    image jasmineassfuckfastvideo = Movie(play="v05/jasmineassfuckfast.webm", loop=True, size=(1920,1080))    
    image jasmineassfuckfrontslowvideo = Movie(play="v05/jasmineassfuckfrontslow.webm", loop=True, size=(1920,1080))    
    image jasmineassfuckfrontfastvideo = Movie(play="v05/jasmineassfuckfrontfast.webm", loop=True, size=(1920,1080))    

    image powerbellanim01 = Movie(play="v05/powerbell01.webm", side_mask=True)    
    image powerbellanim02 = Movie(play="v05/powerbell02.webm", side_mask=True)    
    image powerbellanimfast01 = Movie(play="v05/powerbell01fast.webm", side_mask=True)    
    image powerbellanimfast02 = Movie(play="v05/powerbell02fast.webm", side_mask=True)    
    
    image friedaliftslowvideo = Movie(play="v051/friedaliftslow.webm", loop=True, size=(1920,1080))    
    image friedaliftfastvideo = Movie(play="v051/friedaliftfast.webm", loop=True, size=(1920,1080))    

    image ingridliftslowvideo = Movie(play="v051/ingridliftslow.webm", loop=True, size=(1920,1080))    
    image ingridliftfastvideo = Movie(play="v051/ingridliftfast.webm", loop=True, size=(1920,1080))    
    image ingridanalslowvideo = Movie(play="v051/ingridanalslow.webm", loop=True, size=(1920,1080))    
    image ingridanalfastvideo = Movie(play="v051/ingridanalfast.webm", loop=True, size=(1920,1080))    
    image ingridanalcloserslowvideo = Movie(play="v051/ingridanalcloserslow.webm", loop=True, size=(1920,1080))    
    image ingridanalcloserfastvideo = Movie(play="v051/ingridanalcloserfast.webm", loop=True, size=(1920,1080))    

    image ssblowjobslowvideo = Movie(play="v051/ssblowjobslow.webm", loop=True, size=(1920,1080))    
    image ssblowjobfastvideo = Movie(play="v051/ssblowjobfast.webm", loop=True, size=(1920,1080))    
    image ssblowjobcloserslowvideo = Movie(play="v051/ssblowjobcloserslow.webm", loop=True, size=(1920,1080))    
    image ssblowjobcloserfastvideo = Movie(play="v051/ssblowjobcloserfast.webm", loop=True, size=(1920,1080))    

    image catblowslowvideo = Movie(play="v051/catblowslow.webm", loop=True, size=(1920,1080))    
    image catblowfastvideo = Movie(play="v051/catblowfast.webm", loop=True, size=(1920,1080))    
    image catblowpovslowvideo = Movie(play="v051/catblowpovslow.webm", loop=True, size=(1920,1080))    
    image catblowpovfastvideo = Movie(play="v051/catblowpovfast.webm", loop=True, size=(1920,1080))    

    image catblowharderslowvideo = Movie(play="v051/catblowharderslow.webm", loop=True, size=(1920,1080))    
    image catblowharderfastvideo = Movie(play="v051/catblowharderfast.webm", loop=True, size=(1920,1080))    
    image catblowharderpovslowvideo = Movie(play="v051/catblowharderpovslow.webm", loop=True, size=(1920,1080))    
    image catblowharderpovfastvideo = Movie(play="v051/catblowharderpovfast.webm", loop=True, size=(1920,1080))    

    image catblowdeeperslowvideo = Movie(play="v051/catblowdeeperslow.webm", loop=True, size=(1920,1080))    
    image catblowdeeperfastvideo = Movie(play="v051/catblowdeeperfast.webm", loop=True, size=(1920,1080))    
    image catblowdeeperpovslowvideo = Movie(play="v051/catblowdeeperpovslow.webm", loop=True, size=(1920,1080))    
    image catblowdeeperpovfastvideo = Movie(play="v051/catblowdeeperpovfast.webm", loop=True, size=(1920,1080))    

    image friedafuckslowvideo = Movie(play="v051/friedafuckslow.webm", loop=True, size=(1920,1080))    
    image friedafuckfastvideo = Movie(play="v051/friedafuckfast.webm", loop=True, size=(1920,1080))    
    image friedafuckpovslowvideo = Movie(play="v051/friedafuckpovslow.webm", loop=True, size=(1920,1080))    
    image friedafuckpovfastvideo = Movie(play="v051/friedafuckpovfast.webm", loop=True, size=(1920,1080))    

    image friedafuckharderslowvideo = Movie(play="v051/friedafuckharderslow.webm", loop=True, size=(1920,1080))    
    image friedafuckharderfastvideo = Movie(play="v051/friedafuckharderfast.webm", loop=True, size=(1920,1080))    
    image friedafuckharderpovslowvideo = Movie(play="v051/friedafuckharderpovslow.webm", loop=True, size=(1920,1080))    
    image friedafuckharderpovfastvideo = Movie(play="v051/friedafuckharderpovfast.webm", loop=True, size=(1920,1080))    

    image milftitjobslowvideo = Movie(play="v052/milftitjobslow.webm", loop=True, size=(1920,1080))    
    image milftitjobfastvideo = Movie(play="v052/milftitjobfast.webm", loop=True, size=(1920,1080))    
    image milftitjobharderslowvideo = Movie(play="v052/milftitjobharderslow.webm", loop=True, size=(1920,1080))    
    image milftitjobharderfastvideo = Movie(play="v052/milftitjobharderfast.webm", loop=True, size=(1920,1080))    
    image milftittransitionhardervideo = Movie(play="v052/milftittransitionharder.webm", loop=False, size=(1920,1080))    
    image milftittransitionsoftervideo = Movie(play="v052/milftittransitionsofter.webm", loop=False, size=(1920,1080))    

    image milffootjobslowvideo = Movie(play="v052/milffootjobslow.webm", loop=True, size=(1920,1080))    
    image milffootjobfastvideo = Movie(play="v052/milffootjobfast.webm", loop=True, size=(1920,1080))    
    image milffootjobharderslowvideo = Movie(play="v052/milffootjobharderslow.webm", loop=True, size=(1920,1080))    
    image milffootjobharderfastvideo = Movie(play="v052/milffootjobharderfast.webm", loop=True, size=(1920,1080))    
    image milffootjobslowpovvideo = Movie(play="v052/milffootjobslowpov.webm", loop=True, size=(1920,1080))    
    image milffootjobfastpovvideo = Movie(play="v052/milffootjobfastpov.webm", loop=True, size=(1920,1080))    
    image milffootjobharderpovslowvideo = Movie(play="v052/milffootjobharderpovslow.webm", loop=True, size=(1920,1080))    
    image milffootjobharderpovfastvideo = Movie(play="v052/milffootjobharderpovfast.webm", loop=True, size=(1920,1080))    

    image milfnewanalslowvideo = Movie(play="v052/milfnewanalslow.webm", loop=True, size=(1920,1080))    
    image milfnewanalfastvideo = Movie(play="v052/milfnewanalfast.webm", loop=True, size=(1920,1080))    
    image milfnewanalharderslowvideo = Movie(play="v052/milfnewanalharderslow.webm", loop=True, size=(1920,1080))    
    image milfnewanalharderfastvideo = Movie(play="v052/milfnewanalharderfast.webm", loop=True, size=(1920,1080))    
    image milfnewanalslowpovvideo = Movie(play="v052/milfnewanalslowpov.webm", loop=True, size=(2112,1080))    
    image milfnewanalfastpovvideo = Movie(play="v052/milfnewanalfastpov.webm", loop=True, size=(2112,1080))    
    image milfnewanalharderpovslowvideo = Movie(play="v052/milfnewanalharderpovslow.webm", loop=True, size=(2112,1080))    
    image milfnewanalharderpovfastvideo = Movie(play="v052/milfnewanalharderpovfast.webm", loop=True, size=(2112,1080))    

    image excelladeskfuckslowvideo = Movie(play="v052/excelladeskfuckslow.webm", loop=True, size=(1920,1080))    
    image excelladeskfuckfastvideo = Movie(play="v052/excelladeskfuckfast.webm", loop=True, size=(1920,1080))    
    image excelladeskfuckharderslowvideo = Movie(play="v052/excelladeskfuckharderslow.webm", loop=True, size=(1920,1080))    
    image excelladeskfuckharderfastvideo = Movie(play="v052/excelladeskfuckharderfast.webm", loop=True, size=(1920,1080))    
    image excelladeskfuckslowpovvideo = Movie(play="v052/excelladeskfuckslowpov.webm", loop=True, size=(2112,1080))    
    image excelladeskfuckfastpovvideo = Movie(play="v052/excelladeskfuckfastpov.webm", loop=True, size=(2112,1080))    
    image excelladeskfuckharderpovslowvideo = Movie(play="v052/excelladeskfuckharderpovslow.webm", loop=True, size=(2112,1080))    
    image excelladeskfuckharderpovfastvideo = Movie(play="v052/excelladeskfuckharderpovfast.webm", loop=True, size=(2112,1080))    

    image loispussypunishslowvideo = Movie(play="v052/loispussypunishslow.webm", loop=True, size=(1920,1080))    
    image loispussypunishfastvideo = Movie(play="v052/loispussypunishfast.webm", loop=True, size=(1920,1080))    
    image loispussypunishharderslowvideo = Movie(play="v052/loispussypunishharderslow.webm", loop=True, size=(1920,1080))    
    image loispussypunishharderfastvideo = Movie(play="v052/loispussypunishharderfast.webm", loop=True, size=(1920,1080))    
    image loispussypunishslowpovvideo = Movie(play="v052/loispussypunishslowpov.webm", loop=True, size=(2112,1080))    
    image loispussypunishfastpovvideo = Movie(play="v052/loispussypunishfastpov.webm", loop=True, size=(2112,1080))    
    image loispussypunishharderpovslowvideo = Movie(play="v052/loispussypunishharderpovslow.webm", loop=True, size=(2112,1080))    
    image loispussypunishharderpovfastvideo = Movie(play="v052/loispussypunishharderpovfast.webm", loop=True, size=(2112,1080))    

    image hulkjacuzziblowslowvideo = Movie(play="v052/hulkjacuzziblowslow.webm", loop=True, size=(1920,1080))    
    image hulkjacuzziblowfastvideo = Movie(play="v052/hulkjacuzziblowfast.webm", loop=True, size=(1920,1080))    
    image hulkjacuzziblowharderslowvideo = Movie(play="v052/hulkblowharderslow.webm", loop=True, size=(1920,1080))    
    image hulkjacuzziblowharderfastvideo = Movie(play="v052/hulkblowharderfast.webm", loop=True, size=(1920,1080))    
    image hulkjacuzziblowslowpovvideo = Movie(play="v052/hulkjacuzziblowpovslow.webm", loop=True, size=(2112,1080))    
    image hulkjacuzziblowfastpovvideo = Movie(play="v052/hulkjacuzziblowpovfast.webm", loop=True, size=(2112,1080))    
    image hulkjacuzziblowharderpovslowvideo = Movie(play="v052/hulkblowharderpovslow.webm", loop=True, size=(2112,1080))    
    image hulkjacuzziblowharderpovfastvideo = Movie(play="v052/hulkblowharderpovfast.webm", loop=True, size=(2112,1080))    

    image hulkjacuzzifuckslowvideo = Movie(play="v052/hulkjacuzzifuckslow.webm", loop=True, size=(1920,1080))    
    image hulkjacuzzifuckfastvideo = Movie(play="v052/hulkjacuzzifuckfast.webm", loop=True, size=(1920,1080))    
    image hulkjacuzzifuckharderslowvideo = Movie(play="v052/hulkjacuzzifuckharderslow.webm", loop=True, size=(1920,1080))    
    image hulkjacuzzifuckharderfastvideo = Movie(play="v052/hulkjacuzzifuckharderfast.webm", loop=True, size=(1920,1080))    
    image hulkjacuzzifuckslowpovvideo = Movie(play="v052/hulkjacuzzifuckslowpov.webm", loop=True, size=(2112,1080))    
    image hulkjacuzzifuckfastpovvideo = Movie(play="v052/hulkjacuzzifuckfastpov.webm", loop=True, size=(2112,1080))    
    image hulkjacuzzifuckharderpovslowvideo = Movie(play="v052/hulkjacuzzifuckharderpovslow.webm", loop=True, size=(2112,1080))    
    image hulkjacuzzifuckharderpovfastvideo = Movie(play="v052/hulkjacuzzifuckharderpovfast.webm", loop=True, size=(2112,1080))    

    image hulkgymlifttopvideo = Movie(play="v06/hulkgymlifttop.webm", loop=True, size=(1920,1080))    
    image hulkgymliftsidevideo = Movie(play="v06/hulkgymliftside.webm", loop=True, size=(1920,1080))    
    image hulkgymlifttopnudevideo = Movie(play="v06/hulkgymlifttopnude.webm", loop=True, size=(1920,1080))    
    image hulkgymliftsidenudevideo = Movie(play="v06/hulkgymliftsidenude.webm", loop=True, size=(1920,1080))    

    image wonderwornslowvideo = Movie(play="v06/wonderwornslow.webm", loop=True, size=(1920,1080))    
    image wonderwornfastvideo = Movie(play="v06/wonderwornfast.webm", loop=True, size=(1920,1080))    
    image wonderwornpovslowvideo = Movie(play="v06/wonderwornpovslow.webm", loop=True, size=(1920,1080))    
    image wonderwornpovfastvideo = Movie(play="v06/wonderwornpovfast.webm", loop=True, size=(1920,1080))    

    image wonderassslowvideo = Movie(play="v06/wonderassslow.webm", loop=True, size=(1920,1080))    
    image wonderassfastvideo = Movie(play="v06/wonderassfast.webm", loop=True, size=(1920,1080))    
    image wonderasspovslowvideo = Movie(play="v06/wonderasspovslow.webm", loop=True, size=(1920,1080))    
    image wonderasspovfastvideo = Movie(play="v06/wonderasspovfast.webm", loop=True, size=(1920,1080))    

    image wondertitslowvideo = Movie(play="v06/wondertitslow.webm", loop=True, size=(1920,1080))    
    image wondertitfastvideo = Movie(play="v06/wondertitfast.webm", loop=True, size=(1920,1080))    
    image wondertitpovslowvideo = Movie(play="v06/wondertitpovslow.webm", loop=True, size=(1920,1080))    
    image wondertitpovfastvideo = Movie(play="v06/wondertitpovfast.webm", loop=True, size=(1920,1080))    

    image wonderbedanalslowvideo = Movie(play="v06/wonderbedanalslow.webm", loop=True, size=(1920,1080))    
    image wonderbedanalfastvideo = Movie(play="v06/wonderbedanalfast.webm", loop=True, size=(1920,1080))    
    image wonderbedanalfrontslowvideo = Movie(play="v06/wonderbedanalfrontslow.webm", loop=True, size=(1920,1080))    
    image wonderbedanalfrontfastvideo = Movie(play="v06/wonderbedanalfrontfast.webm", loop=True, size=(1920,1080))    

    image natalyafistslowvideo = Movie(play="v06/natalyafistslow.webm", loop=True, size=(1920,1080))    
    image natalyafistfastvideo = Movie(play="v06/natalyafistfast.webm", loop=True, size=(1920,1080))    
    image natalyafistharderslowvideo = Movie(play="v06/natalyafistharderslow.webm", loop=True, size=(1920,1080))    
    image natalyafistharderfastvideo = Movie(play="v06/natalyafistharderfast.webm", loop=True, size=(1920,1080))    

    image natalyablowslowvideo = Movie(play="v06/natalyablowslow.webm", loop=True, size=(1920,1080))    
    image natalyablowfastvideo = Movie(play="v06/natalyablowfast.webm", loop=True, size=(1920,1080))    
    image natalyablowpovslowvideo = Movie(play="v06/natalyablowpovslow.webm", loop=True, size=(1920,1080))    
    image natalyablowpovfastvideo = Movie(play="v06/natalyablowpovfast.webm", loop=True, size=(1920,1080))    

    image natalyaswitchslowvideo = Movie(play="v06/natalyaswitchslow.webm", loop=True, size=(1920,1080))    
    image natalyaswitchfastvideo = Movie(play="v06/natalyaswitchfast.webm", loop=True, size=(1920,1080))    
    image natalyaswitchcloserslowvideo = Movie(play="v06/natalyaswitchcloserslow.webm", loop=True, size=(1920,1080))    
    image natalyaswitchcloserfastvideo = Movie(play="v06/natalyaswitchcloserfast.webm", loop=True, size=(1920,1080))    

    image natalyafuckslowvideo = Movie(play="v06/natalyafuckslow.webm", loop=True, size=(1920,1080))    
    image natalyafuckfastvideo = Movie(play="v06/natalyafuckfast.webm", loop=True, size=(1920,1080))    
    image natalyafuckpovslowvideo = Movie(play="v06/natalyafuckpovslow.webm", loop=True, size=(1920,1080))    
    image natalyafuckpovfastvideo = Movie(play="v06/natalyafuckpovfast.webm", loop=True, size=(1920,1080))    

    image natalyawidowfuckslowvideo = Movie(play="v06/natalyawidowfuckslow.webm", loop=True, size=(1920,1080))    
    image natalyawidowfuckfastvideo = Movie(play="v06/natalyawidowfuckfast.webm", loop=True, size=(1920,1080))    
    image natalyawidowfuckfastervideo = Movie(play="v06/natalyawidowfuckfaster.webm", loop=True, size=(1920,1080))    

    image daniblowslowvideo = Movie(play="v061/daniblowslow.webm", loop=True, size=(1920,1080))    
    image daniblowfastvideo = Movie(play="v061/daniblowfast.webm", loop=True, size=(1920,1080))    
    image daniblowsceneslowvideo = Movie(play="v061/daniblowsceneslow.webm", loop=True, size=(1920,1080))    
    image daniblowscenefastvideo = Movie(play="v061/daniblowscenefast.webm", loop=True, size=(1920,1080))    

    image daniblowharderslowvideo = Movie(play="v061/daniblowharderslow.webm", loop=True, size=(1920,1080))    
    image daniblowharderfastvideo = Movie(play="v061/daniblowharderfast.webm", loop=True, size=(1920,1080))    
    image daniblowharderpovslowvideo = Movie(play="v061/daniblowharderpovslow.webm", loop=True, size=(1920,1080))    
    image daniblowharderpovfastvideo = Movie(play="v061/daniblowharderpovfast.webm", loop=True, size=(1920,1080))    

    image harleyblowslowvideo = Movie(play="v061/harleyblowslow.webm", loop=True, size=(1920,1080))    
    image harleyblowfastvideo = Movie(play="v061/harleyblowfast.webm", loop=True, size=(1920,1080))    
    image harleyblowpovslowvideo = Movie(play="v061/harleyblowpovslow.webm", loop=True, size=(1920,1080))    
    image harleyblowpovfastvideo = Movie(play="v061/harleyblowpovfast.webm", loop=True, size=(1920,1080))    

    image harleypoundslowvideo = Movie(play="v061/harleypoundslow.webm", loop=True, size=(2112,1080))    
    image harleypoundfastvideo = Movie(play="v061/harleypoundfast.webm", loop=True, size=(2112,1080))    
    image harleypoundfrontslowvideo = Movie(play="v061/harleypoundfrontslow.webm", loop=True, size=(2112,1080))    
    image harleypoundfrontfastvideo = Movie(play="v061/harleypoundfrontfast.webm", loop=True, size=(2112,1080))    

    image milfnewpussyslowvideo = Movie(play="v061/milfnewpussyslow.webm", loop=True, size=(1920,1080))    
    image milfnewpussyfastvideo = Movie(play="v061/milfnewpussyfast.webm", loop=True, size=(1920,1080))    
    image milfnewpussyslowpovvideo = Movie(play="v061/milfnewpussyslowpov.webm", loop=True, size=(1920,1080))    
    image milfnewpussyfastpovvideo = Movie(play="v061/milfnewpussyfastpov.webm", loop=True, size=(1920,1080))    

    image milfnewpussyharderslowvideo = Movie(play="v061/milfnewpussyharderslow.webm", loop=True, size=(1920,1080))    
    image milfnewpussyharderfastvideo = Movie(play="v061/milfnewpussyharderfast.webm", loop=True, size=(1920,1080))    
    image milfnewpussyharderpovslowvideo = Movie(play="v061/milfnewpussyharderpovslow.webm", loop=True, size=(1920,1080))    
    image milfnewpussyharderpovfastvideo = Movie(play="v061/milfnewpussyharderpovfast.webm", loop=True, size=(1920,1080))    

    image frostrimjobvideo = Movie(play="v061/frostrimjob.webm", loop=True, size=(1920,1080))    

    image frostanalslowvideo = Movie(play="v061/frostanalslow.webm", loop=True, size=(1920,1080))    
    image frostanalfastvideo = Movie(play="v061/frostanalfast.webm", loop=True, size=(1920,1080))    
    image frostanalbackslowvideo = Movie(play="v061/frostanalbackslow.webm", loop=True, size=(1920,1080))    
    image frostanalbackfastvideo = Movie(play="v061/frostanalbackfast.webm", loop=True, size=(1920,1080))    

    image mafiaassslowvideo = Movie(play="v07/mafiaassslow.webm", loop=True, size=(1920,1080))    
    image mafiaassfastvideo = Movie(play="v07/mafiaassfast.webm", loop=True, size=(1920,1080))    
    image mafiaasspovslowvideo = Movie(play="v07/mafiaasspovslow.webm", loop=True, size=(1920,1080))    
    image mafiaasspovfastvideo = Movie(play="v07/mafiaasspovfast.webm", loop=True, size=(1920,1080))    
    image mafiaassharderslowvideo = Movie(play="v07/mafiaharderslow.webm", loop=True, size=(1920,1080))    
    image mafiaassharderfastvideo = Movie(play="v07/mafiaharderfast.webm", loop=True, size=(1920,1080))    
    image mafiaassharderpovslowvideo = Movie(play="v07/mafiaharderpovslow.webm", loop=True, size=(1920,1080))    
    image mafiaassharderpovfastvideo = Movie(play="v07/mafiaharderpovfast.webm", loop=True, size=(1920,1080))    

    image adasuckslowvideo = Movie(play="v07/adasuckslow.webm", loop=True, size=(1920,1080))    
    image adasuckfastvideo = Movie(play="v07/adasuckfast.webm", loop=True, size=(1920,1080))    
    image adasuckpovslowvideo = Movie(play="v07/adasuckpovslow.webm", loop=True, size=(1920,1080))    
    image adasuckpovfastvideo = Movie(play="v07/adasuckpovfast.webm", loop=True, size=(1920,1080))    

    image adasuckfutaslowvideo = Movie(play="v07/adasuckfutaslow.webm", loop=True, size=(1920,1080))    
    image adasuckfutafastvideo = Movie(play="v07/adasuckfutafast.webm", loop=True, size=(1920,1080))    

    image adasuckharderslowvideo = Movie(play="v07/adasuckharderslow.webm", loop=True, size=(1920,1080))    
    image adasuckharderfastvideo = Movie(play="v07/adasuckharderfast.webm", loop=True, size=(1920,1080))    
    image adasuckharderpovslowvideo = Movie(play="v07/adasuckharderpovslow.webm", loop=True, size=(1920,1080))    
    image adasuckharderpovfastvideo = Movie(play="v07/adasuckharderpovfast.webm", loop=True, size=(1920,1080))    

    image adasuckharderfutaslowvideo = Movie(play="v07/adasuckharderfutaslow.webm", loop=True, size=(1920,1080))    
    image adasuckharderfutafastvideo = Movie(play="v07/adasuckharderfutafast.webm", loop=True, size=(1920,1080))    

    image adaanalslowvideo = Movie(play="v07/adaanalslow.webm", loop=True, size=(1920,1080))    
    image adaanalfastvideo = Movie(play="v07/adaanalfast.webm", loop=True, size=(1920,1080))    
    image adaanalcloserslowvideo = Movie(play="v07/adacloseslow.webm", loop=True, size=(1920,1080))    
    image adaanalcloserfastvideo = Movie(play="v07/adaclosefast.webm", loop=True, size=(1920,1080))    

    image adaanalfutaslowvideo = Movie(play="v07/adaanalfutaslow.webm", loop=True, size=(1920,1080))    
    image adaanalfutafastvideo = Movie(play="v07/adaanalfutafast.webm", loop=True, size=(1920,1080))    
    image adaanalcloserfutaslowvideo = Movie(play="v07/adaclosefutaslow.webm", loop=True, size=(1920,1080))    
    image adaanalcloserfutafastvideo = Movie(play="v07/adaclosefutafast.webm", loop=True, size=(1920,1080))    

    image auditgymfuckslowvideo = Movie(play="v07/auditgymfuckslow.webm", loop=True, size=(1920,1080))    
    image auditgymfuckfastvideo = Movie(play="v07/auditgymfuckfast.webm", loop=True, size=(1920,1080))    
    image auditgymfuckveryfastvideo = Movie(play="v07/auditgymfuckveryfast.webm", loop=True, size=(1920,1080))    
    image auditgymassslowvideo = Movie(play="v07/auditgymassslow.webm", loop=True, size=(1920,1080))    
    image auditgymassfastvideo = Movie(play="v07/auditgymassfast.webm", loop=True, size=(1920,1080))    
    image auditgymassveryfastvideo = Movie(play="v07/auditgymassveryfast.webm", loop=True, size=(1920,1080))    

    image auditanimbik = Movie(play="gallery/auditbik.webm", side_mask=True)    
    image auditanimlin = Movie(play="gallery/auditlin.webm", side_mask=True)    
    image auditanimcos = Movie(play="gallery/auditcos.webm", side_mask=True)    
    image auditanimnak = Movie(play="gallery/auditnak.webm", side_mask=True)    
    image auditanimclo = Movie(play="gallery/auditclo.webm", side_mask=True)    

    image laraanimbik = Movie(play="gallery/larabik.webm", side_mask=True)    
    image laraanimcos = Movie(play="gallery/laracos.webm", side_mask=True)    
    image laraanimnak = Movie(play="gallery/laranak.webm", side_mask=True)    

    image milfanimbik = Movie(play="gallery/milfbik.webm", side_mask=True)    
    image milfanimlin = Movie(play="gallery/milflin.webm", side_mask=True)    
    image milfanimcos = Movie(play="gallery/milfcos.webm", side_mask=True)    
    image milfanimnak = Movie(play="gallery/milfnak.webm", side_mask=True)    
    image milfanimgym = Movie(play="gallery/milfgym.webm", side_mask=True)    

    image poweranimbik = Movie(play="gallery/powerbik.webm", side_mask=True)    
    image poweranimlin = Movie(play="gallery/powerlin.webm", side_mask=True)    
    image poweranimcos = Movie(play="gallery/powercos.webm", side_mask=True)    
    image poweranimnak = Movie(play="gallery/powernak.webm", side_mask=True)    
    image poweranimgym = Movie(play="gallery/powergym.webm", side_mask=True)    

    image widowanimbik = Movie(play="gallery/widowbik.webm", side_mask=True)    
    image widowanimlin = Movie(play="gallery/widowlin.webm", side_mask=True)    
    image widowanimcos = Movie(play="gallery/widowcos.webm", side_mask=True)    
    image widowanimnak = Movie(play="gallery/widownak.webm", side_mask=True)    
    image widowanimgym = Movie(play="gallery/widowgym.webm", side_mask=True)    

    image wonderanimlin = Movie(play="gallery/wonderlin.webm", side_mask=True)    
    image wonderanimcos = Movie(play="gallery/wondercos.webm", side_mask=True)    
    image wonderanimnak = Movie(play="gallery/wondernak.webm", side_mask=True)    
    image wonderanimgym = Movie(play="gallery/wondergym.webm", side_mask=True)    

    image superanimbik = Movie(play="gallery/superbik.webm", side_mask=True)    
    image superanimcos = Movie(play="gallery/supercos.webm", side_mask=True)    
    image superanimnak = Movie(play="gallery/supernak.webm", side_mask=True)    
    image superanimmus = Movie(play="gallery/supermus.webm", side_mask=True)    

    image excellaanimlin = Movie(play="gallery/excellalin.webm", side_mask=True)    
    image excellaanimcos = Movie(play="gallery/excellacos.webm", side_mask=True)    
    image excellaanimnak = Movie(play="gallery/excellanak.webm", side_mask=True)    

    image harleyanimbik = Movie(play="gallery/harleybik.webm", side_mask=True)    
    image harleyanimcos = Movie(play="gallery/harleycos.webm", side_mask=True)    
    image harleyanimnak = Movie(play="gallery/harleynak.webm", side_mask=True)    
    
    image loisanimlin = Movie(play="gallery/loislin.webm", side_mask=True)    
    image loisanimcos = Movie(play="gallery/loiscos.webm", side_mask=True)    
    image loisanimnak = Movie(play="gallery/loisnak.webm", side_mask=True)    

    image barbanimlin = Movie(play="gallery/barblin.webm", side_mask=True)    
    image barbanimcos = Movie(play="gallery/barbcos.webm", side_mask=True)    
    image barbanimnak = Movie(play="gallery/barbnak.webm", side_mask=True)    

    image sawyeranimlin = Movie(play="gallery/sawyerlin.webm", side_mask=True)    
    image sawyeranimcos = Movie(play="gallery/sawyercos.webm", side_mask=True)    
    image sawyeranimnak = Movie(play="gallery/sawyernak.webm", side_mask=True)    
    image sawyeranimout = Movie(play="gallery/sawyerout.webm", side_mask=True)    

    image scarletanimbig = Movie(play="gallery/scarletbig.webm", side_mask=True)    
    image scarletanimcos = Movie(play="gallery/scarletcos.webm", side_mask=True)    
    image scarletanimnak = Movie(play="gallery/scarletnak.webm", side_mask=True)    
    image scarletanimmus = Movie(play="gallery/scarletmus.webm", side_mask=True)    
    
    image tabithaanimlin = Movie(play="gallery/tabithalin.webm", side_mask=True)    
    image tabithaanimcos = Movie(play="gallery/tabithacos.webm", side_mask=True)    
    image tabithaanimnak = Movie(play="gallery/tabithanak.webm", side_mask=True)    

    image adaanimcos = Movie(play="gallery/adacos.webm", side_mask=True)    
    image adaanimlin = Movie(play="gallery/adalin.webm", side_mask=True)    
    image adaanimlinfuta = Movie(play="gallery/adafutalin.webm", side_mask=True)    
    image adaanimnak = Movie(play="gallery/adanak.webm", side_mask=True)    
    image adaanimnakfuta = Movie(play="gallery/adafutanak.webm", side_mask=True)    

    image frostanimcos = Movie(play="gallery/frostcos.webm", side_mask=True)    
    image frostanimnak = Movie(play="gallery/frostnak.webm", side_mask=True)    

    image angelaanimcos = Movie(play="gallery/angelacos.webm", side_mask=True)    
    image angelaanimnak = Movie(play="gallery/angelanak.webm", side_mask=True)    

    image demonaanimcos = Movie(play="gallery/demonacos.webm", side_mask=True)    
    image demonaanimnak = Movie(play="gallery/demonanak.webm", side_mask=True)    

    image cathanimlin = Movie(play="gallery/cathlin.webm", side_mask=True)    
    image cathanimnak = Movie(play="gallery/cathnak.webm", side_mask=True)    

    image kateanimlin = Movie(play="gallery/katlin.webm", side_mask=True)    
    image kateanimnak = Movie(play="gallery/katnak.webm", side_mask=True)    

    image ivyanimcos = Movie(play="gallery/ivycos.webm", side_mask=True)    
    image ivyanimnak = Movie(play="gallery/ivynak.webm", side_mask=True)    
    image ivyanimtit = Movie(play="gallery/ivytit.webm", side_mask=True)    

    image honokaanimcos = Movie(play="gallery/honokacos.webm", side_mask=True)    
    image honokaanimnak = Movie(play="gallery/honokanak.webm", side_mask=True)    

    image luthoranimcos = Movie(play="gallery/luthorcos.webm", side_mask=True)    
    image luthoranimnak = Movie(play="gallery/luthornak.webm", side_mask=True)    

    image shehulkanimcos = Movie(play="gallery/hulkcos.webm", side_mask=True)    
    image shehulkanimnak = Movie(play="gallery/hulknak.webm", side_mask=True)    

    image skullyanimcos = Movie(play="gallery/skucos.webm", side_mask=True)    
    image skullyanimnak = Movie(play="gallery/skunak.webm", side_mask=True)    

    image sophiaanimcos = Movie(play="gallery/sophiacos.webm", side_mask=True)    
    image sophiaanimnak = Movie(play="gallery/sophianak.webm", side_mask=True)    

    image danianimcos = Movie(play="gallery/danicos.webm", side_mask=True)    
    image danianimnak = Movie(play="gallery/daninak.webm", side_mask=True)    

    image catwomananimcos = Movie(play="gallery/catwomancos.webm", side_mask=True)    
    image catwomananimlin = Movie(play="gallery/catwomanlin.webm", side_mask=True)    
    image catwomananimnak = Movie(play="gallery/catwomannak.webm", side_mask=True)    

    image cleoanimcos = Movie(play="gallery/cleocos.webm", side_mask=True)    
    image cleoanimnak = Movie(play="gallery/cleonak.webm", side_mask=True)    

    image natalyaanimcos = Movie(play="gallery/natalyacos.webm", side_mask=True)    
    image natalyaanimlin = Movie(play="gallery/natalyalin.webm", side_mask=True)    
    image natalyaanimnak = Movie(play="gallery/natalyanak.webm", side_mask=True)    

    image wangroom01 blurred = im.Blur("v042/wangroom01.jpg", 1.5)
    image frostfuck03 blurred = im.Blur("v042/frostfuck03.jpg", 1.5)
    image lingeriebackground blurred = im.Blur("v01/lingeriebackground.jpg", 1.5)
    image lingeriestoretrybackground blurred = im.Blur("v01/lingeriestoretrybackground.jpg", 1.5)
    image lingeriestoretrybackground02 blurred = im.Blur("v01/lingeriestoretrybackground02.jpg", 1.5)
    image lingeriestoretrybackgroundlarge blurred = im.Blur("v01/lingeriestoretrybackgroundlarge.jpg", 1.5)
    image widowroomnight blurred = im.Blur("v01/widowroomnight.jpg", 1.5)
    image cockhamplanet01a blurred = im.Blur("v01/cockhamplanet01a.jpg", 1.5)
    image cockhamplanet01b blurred = im.Blur("v01/cockhamplanet01b.jpg", 1.5)
    image sirens01 blurred = im.Blur("v02/sirens01.jpg", 1.5)
    image sirens01bara blurred = im.Blur("v02/sirens01bara.jpg", 1.5)
    image sirens01barb blurred = im.Blur("v02/sirens01barb.jpg", 1.5)
    image compoundmilfbedroomnight blurred = im.Blur("v01/compoundmilfbedroomnight.jpg", 1.5)
    image widowpoolbackground02 blurred = im.Blur("v01/widowpoolbackground02.jpg", 1.5)
    image widowpoolbackground01 blurred = im.Blur("v01/widowpoolbackground01.jpg", 1.5)
    image poolbackground blurred = im.Blur("v01/poolbackground.jpg", 1.5)
    image allleaguedoor blurred = im.Blur("intro/allleaguedoor.jpg", 1.5)
    image harleyplace02 blurred = im.Blur("v02/harleyplace02.jpg", 1.5)
    image harleyplace03 blurred = im.Blur("v02/harleyplace03.jpg", 1.5)
    image harleybikini01small = im.FactorScale("v02/harleybikini01.png", 0.5)
    image harleyplace02small = im.FactorScale("v02/harleyplace02.jpg", 0.5)
    image honokafullback blurred = im.Blur("v02/honokafullback.jpg", 1.5)
    image honokafuckbackground blurred = im.Blur("v02/honokafuckbackground.jpg", 1.5)
    image honokafuckfacebackground blurred = im.Blur("v02/honokafuckfacebackground.jpg", 1.5)
    image powerlingeriebackground01 blurred = im.Blur("v021/powerlingeriebackground01.jpg", 1.5)
    image compoundmilfnightseduction02 blurred = im.Blur("v021/compoundmilfnightseduction02.jpg", 1.5)

    image harleysidebackground blurred = im.Blur("v02/harleysidebackground.jpg", 1.5)
    image harleyassbackground blurred = im.Blur("v02/harleyassbackground.jpg", 1.5)
    
    image psychevalback blurred = im.Blur("v023/psychevalback.jpg", 1.5)

    image compoundpooldaybackground blurred = im.Blur("v01/compoundpooldaybackground.jpg", 1.5)
    image compoundpoolnight blurred = im.Blur("v01/compoundpoolnight.jpg", 1.5)
    image loisbedroombackground01 blurred = im.Blur("v031/loisbedroombackground01.jpg", 1.5)
    image powerpoolbellback blurred = im.Blur("v05/powerpoolbellback.jpg", 1.5)
    image powerpoolbellanimback blurred = im.Blur("v05/powerpoolbellanimback.jpg", 1.5)
    image catwomanlair01 blurred = im.Blur("v05/catwomanlair01.jpg", 1.5)
    image wonderroomday blurred = im.Blur("v01/wonderroomday.jpg", 1.5)
    image wonderroomnight02 blurred = im.Blur("v01/wonderroomnight02.jpg", 1.5)
    image wonderroomnight03 blurred = im.Blur("v06/wonderroomnight03.jpg", 1.5)

    screen questscreeniconfirst():
        imagebutton:
            focus_mask True
            idle "icons/questsiconscreenidle.png"
            hover "icons/questsiconscreenhover.png"
            action Jump ("QuestscreenFirst")

    screen questscreenicon():
        imagebutton:
            focus_mask True
            idle "icons/questsiconscreenidle.png"
            hover "icons/questsiconscreenhover.png"
            action ui.callsinnewcontext("Questscreen")

    screen statscreeniconfirst():
        imagebutton:
            focus_mask True
            idle "icons/statsiconscreenidle.png"
            hover "icons/statsiconscreenhover.png"
            action Jump ("StatscreenFirst")

    screen statscreenicon():
        imagebutton:
            focus_mask True
            idle "icons/statsiconscreenidle.png"
            hover "icons/statsiconscreenhover.png"
            action ui.callsinnewcontext("Statscreen")

    screen folders():
        imagebutton:
            focus_mask True
            idle "icons/folderblueidle.png"
            hover "icons/folderbluehover.png"
            action [renpy.hide_screen("folders"), Show ("screenredfolder")]
        imagebutton:
            focus_mask True
            idle "icons/folderredidle.png"
            hover "icons/folderredhover.png"
            action [renpy.hide_screen("folders"), Show ("screenredfolder")]
        key "hide_windows" action NullAction()
        key ["game_menu"] action NullAction()

    screen screenredfolder():
        modal True
        add "icons/dossierbackgroundbase.png"
        add "icons/returnicon.png"
        text "{font=Gui/Heroes Legend.ttf}Super-Heroes{/font}" color "#ff0000" size 20 outlines [(2, "#fff4", 0, 0), (1, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posdossierhero
        imagebutton:
            focus_mask True
            idle "icons/auditfolder.png"
            hover "icons/auditfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenauditdossier")]
        imagebutton:
            focus_mask True
            idle "icons/widowfolder.png"
            hover "icons/widowfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenwidowdossier")]
        imagebutton:
            focus_mask True
            idle "icons/wonderfolder.png"
            hover "icons/wonderfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenwonderdossier")]
        imagebutton:
            focus_mask True
            idle "icons/milffolder.png"
            hover "icons/milffolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenmilfdossier")]
        imagebutton:
            focus_mask True
            idle "icons/larafolder.png"
            hover "icons/larafolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenlaradossier")]
        imagebutton:
            focus_mask True
            idle "icons/powerfolder.png"
            hover "icons/powerfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenpowerdossier")]
        imagebutton:
            focus_mask True
            idle "icons/batmanfolder.png"
            hover "icons/batmanfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenbatmandossier")]
        imagebutton:
            focus_mask True
            idle "icons/superfolder.png"
            hover "icons/superfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screensuperdossier")]
        imagebutton:
            focus_mask True
            idle "icons/mcfolder.png"
            hover "icons/mcfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screenmcdossier")]
        imagebutton:
            focus_mask True
            idle "icons/catwomanfolder.png"
            hover "icons/catwomanfolder.png"
            action [renpy.hide_screen("screenredfolder"), Show ("screencatwomandossier")]
        if questhulk:
            imagebutton:
                focus_mask True
                idle "icons/hulkfolder.png"
                hover "icons/hulkfolder.png"
                action [renpy.hide_screen("screenredfolder"), Show ("screenhulkdossier")]
        if questhulkcompleted:
            imagebutton:
                focus_mask True
                idle "v03/supergirlfolder.png"
                hover "v03/supergirlfolder.png"
                action [renpy.hide_screen("screenredfolder"), Show ("screensupergirldossier")]
        if day <= 2:
            button:
                xpos 1730
                ypos 1020
                xysize(145, 40)        
                action [renpy.hide_screen("screenredfolder"), Return()]
        if day >= 3:
            button:
                xpos 1730
                ypos 1020
                xysize(145, 40)        
                action [renpy.hide_screen("screenredfolder"), Jump ("Statscreen")]
        key "hide_windows" action NullAction()
        key ["game_menu"] action NullAction()

    screen screenbluefolder():
        modal True
        add "icons/dossierbackgroundbase.png"
        add "icons/returnicon.png"
        text "{font=Gui/Heroes Legend.ttf}Super-Villains{/font}" color "#0000ff" size 20 outlines [(2, "#fff4", 0, 0), (1, "#fff8", 0, 0),  (1, "#fffc", 0, 0)] at posdossierhero
        imagebutton:
            focus_mask True
            idle "icons/wangfolder.png"
            hover "icons/wangfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenwangdossier")]
        imagebutton:
            focus_mask True
            idle "icons/keenfolder.png"
            hover "icons/keenfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenkeendossier")]
        imagebutton:
            focus_mask True
            idle "icons/harleyfolder.png"
            hover "icons/harleyfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenharleydossier")]
        imagebutton:
            focus_mask True
            idle "icons/stallionfolder.png"
            hover "icons/stallionfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenstalliondossier")]
        imagebutton:
            focus_mask True
            idle "icons/stroheimfolder.png"
            hover "icons/stroheimfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenstroheimdossier")]
        imagebutton:
            focus_mask True
            idle "icons/luthorfolder.png"
            hover "icons/luthorfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenluthordossier")]
        imagebutton:
            focus_mask True
            idle "icons/jokerfolder.png"
            hover "icons/jokerfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenjokerdossier")]
        imagebutton:
            focus_mask True
            idle "icons/frostfolder.png"
            hover "icons/frostfolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenfrostdossier")]
        imagebutton:
            focus_mask True
            idle "icons/excellafolder.png"
            hover "icons/excellafolder.png"
            action [renpy.hide_screen("screenbluefolder"), Show ("screenexcelladossier")]
        if seenembassy:
            imagebutton:
                focus_mask True
                idle "v06/natalyafolder.png"
                hover "v06/natalyafolder.png"
                action [renpy.hide_screen("screenbluefolder"), Show ("screennatalyadossier")]
        if metivy:
            imagebutton:
                focus_mask True
                idle "v03/ivyfolder.png"
                hover "v03/ivyfolder.png"
                action [renpy.hide_screen("screenbluefolder"), Show ("screenpoisondossier")]
        if day <= 2:
            button:
                xpos 1730
                ypos 1020
                xysize(145, 40)        
                action [renpy.hide_screen("screenbluefolder"), Return()]
        if day >= 3:
            button:
                xpos 1730
                ypos 1020
                xysize(145, 40)        
                action [renpy.hide_screen("screenredfolder"), Jump ("Statscreen")]
        key "hide_windows" action NullAction()
        key ["game_menu"] action NullAction()
            
    image helicock:
        "v061/mcstrip06.jpg" with fastdissolve
        pause .3
        "v061/mcstrip05.jpg" with fastdissolve
        pause 0.3
        "v061/mcstrip06a.jpg" with fastdissolve
        pause .3
        "v061/mcstrip06b.jpg" with fastdissolve
        pause .3
        repeat

    image wonderyogaflex:
        "v041/wonderyoga02.jpg" with fastdissolve
        pause 1.0
        "v041/wonderyoga03.jpg" with fastdissolve
        pause 0.5
        repeat
    
    image loccmblink:
        "icons/loccm.png" with dissolve
        pause 0.5
        "v031/loccm02.png" with dissolve
        pause 0.5
        repeat

    image twisterwonderlick:
        "v01/twister13.jpg" with dissolve
        pause 0.5
        "v01/twister14.jpg" with dissolve
        pause 0.5
        repeat
    
    image catwomanblink:
        "v05/catwoman01a.png"
        function random_1_5
        "v05/catwoman01b.png"
        pause 0.05
        "v05/catwoman01c.png"
        pause 0.05
        "v05/catwoman01b.png"
        pause 0.05
        repeat

    image auditblink:
        "intro/allleagueaudit01a.png"
        function random_1_5
        "intro/allleagueaudit01b.png"
        pause 0.05
        "intro/allleagueaudit01c.png"
        pause 0.05
        "intro/allleagueaudit01b.png"
        pause 0.05
        repeat

    image powerblink:
        "intro/allleaguepower01a.png"
        function random_1_5
        "intro/allleaguepower01b.png"
        pause 0.05
        "intro/allleaguepower01c.png"
        pause 0.05
        "intro/allleaguepower01b.png"
        pause 0.05
        repeat

    image widowblink:
        "intro/leaguewidow01a.png"
        function random_1_5
        "intro/leaguewidow01b.png"
        pause 0.05
        "intro/leaguewidow01c.png"
        pause 0.05
        "intro/leaguewidow01b.png"
        pause 0.05
        repeat

    image sawyerblink:
        "v01/sawyer01a.png"
        function random_1_5
        "v01/sawyer01b.png"
        pause 0.05
        "v01/sawyer01c.png"
        pause 0.05
        "v01/sawyer01b.png"
        pause 0.05
        repeat

    image loisblink:
        "v01/lois01a.png"
        function random_1_5
        "v01/lois01b.png"
        pause 0.05
        "v01/lois01c.png"
        pause 0.05
        "v01/lois01b.png"
        pause 0.05
        repeat

    image wonderblink:
        "v01/wonder02a.png"
        function random_1_5
        "v01/wonder02b.png"
        pause 0.05
        "v01/wonder02c.png"
        pause 0.05
        "v01/wonder02b.png"
        pause 0.05
        repeat

    image widowroomblink:
        "v01/widowroom01a.png"
        function random_1_5
        "v01/widowroom01b.png"
        pause 0.05
        "v01/widowroom01c.png"
        pause 0.05
        "v01/widowroom01b.png"
        pause 0.05
        repeat

    image milfpoolblink:
        "v01/milfpool01a.png"
        function random_1_5
        "v01/milfpool01b.png"
        pause 0.05
        "v01/milfpool01c.png"
        pause 0.05
        "v01/milfpool01b.png"
        pause 0.05
        repeat

    image milfgymblink:
        "v02/milfgym01a.png"
        function random_1_5
        "v02/milfgym01b.png"
        pause 0.05
        "v02/milfgym01c.png"
        pause 0.05
        "v02/milfgym01b.png"
        pause 0.05
        repeat

    image milfgymblink02:
        "v031/milfgym80s01a.png"
        function random_1_5
        "v031/milfgym80s01b.png"
        pause 0.05
        "v031/milfgym80s01c.png"
        pause 0.05
        "v031/milfgym80s01b.png"
        pause 0.05
        repeat

    image wondergymblink:
        "v02/wondergym01a.png"
        function random_1_5
        "v02/wondergym01b.png"
        pause 0.05
        "v02/wondergym01c.png"
        pause 0.05
        "v02/wondergym01b.png"
        pause 0.05
        repeat

    image widowgymblink:
        "v02/gymwidow01a.png"
        function random_1_5
        "v02/gymwidow01b.png"
        pause 0.05
        "v02/gymwidow01c.png"
        pause 0.05
        "v02/gymwidow01b.png"
        pause 0.05
        repeat

    image powerpoolblink:
        "v05/powerpoolnew03a.png"
        function random_1_5
        "v05/powerpoolnew03b.png"
        pause 0.05
        "v05/powerpoolnew03c.png"
        pause 0.05
        "v05/powerpoolnew03b.png"
        pause 0.05
        repeat

    image auditeyeblink = Composite(
        (1920,1080),                      # size of the overall image
        (0,0), "intro/allleagueaudit01.png",
        (0,0), "auditblink")         # top left corner of where I want my eyes to appear.

    image powereyeblink = Composite(
        (1920,1080),
        (0,0), "intro/allleaguepower01.png",
        (0,0), "powerblink")

    image widoweyeblink = Composite(
        (1920,1080),
        (0,0), "intro/leaguewidow01.png",
        (0,0), "widowblink")

    image loiseyeblink = Composite(
        (1920,1080),
        (200,0), "v01/lois01.png",
        (200,0), "loisblink")

    image wondereyeblink = Composite(
        (1920,1080),
        (200,0), "v01/wonder02.png",
        (200,0), "wonderblink")

    image widowroomeyeblink = Composite(
        (1920,1080),
        (168,0), "v01/widowroom01.png",
        (168,0), "widowroomblink")

    image sawyereyeblink = Composite(
        (1920,1080),
        (0,0), "v01/sawyer01.png",
        (0,0), "sawyerblink")

    image milfpooleyeblink = Composite(
        (1920,1080),
        (168,0), "v01/milfpool01.png",
        (168,0), "milfpoolblink")

    image milfgymeyeblink = Composite(
        (1920,1080),
        (168,0), "v02/milfgym01.png",
        (168,0), "milfgymblink")

    image milfgymeyeblink02 = Composite(
        (1920,1080),
        (168,0), "v031/milfgym80s01.png",
        (168,0), "milfgymblink02")

    image wondergymeyeblink = Composite(
        (1920,1080),
        (168,0), "v02/wondergym01.png",
        (168,0), "wondergymblink")

    image widowgymeyeblink = Composite(
        (1920,1080),
        (168,0), "v02/gymwidow01.png",
        (168,0), "widowgymblink")

    image powerpooleyeblink = Composite(
        (1920,1080),
        (168,0), "v05/powerpoolnew03.png",
        (168,0), "powerpoolblink")

    image catwomaneyeblink = Composite(
        (1920,1080),
        (168,0), "v05/catwoman01.png",
        (168,0), "catwomanblink")

    image photowankslow:
        "v01/photowank00.jpg"
        pause 0.04
        "v01/photowank01.jpg"
        pause 0.035
        "v01/photowank02.jpg"
        pause 0.035
        "v01/photowank03.jpg"
        pause 0.035
        "v01/photowank04.jpg"
        pause 0.035
        "v01/photowank05.jpg"
        pause 0.035
        "v01/photowank06.jpg"
        pause 0.035
        "v01/photowank07.jpg"
        pause 0.035
        "v01/photowank08.jpg"
        pause 0.035
        "v01/photowank09.jpg"
        pause 0.035
        "v01/photowank10.jpg"
        pause 0.035
        "v01/photowank11.jpg"
        pause 0.035
        "v01/photowank12.jpg"
        pause 0.04
        "v01/photowank11.jpg"
        pause 0.035
        "v01/photowank10.jpg"
        pause 0.035
        "v01/photowank09.jpg"
        pause 0.035
        "v01/photowank08.jpg"
        pause 0.035
        "v01/photowank07.jpg"
        pause 0.035
        "v01/photowank06.jpg"
        pause 0.035
        "v01/photowank05.jpg"
        pause 0.035
        "v01/photowank04.jpg"
        pause 0.035
        "v01/photowank03.jpg"
        pause 0.035
        "v01/photowank02.jpg"
        pause 0.035
        "v01/photowank01.jpg"
        pause 0.035
        repeat

    image photowankfast:
        "v01/photowank00.jpg"
        pause 0.03
        "v01/photowank01.jpg"
        pause 0.025
        "v01/photowank02.jpg"
        pause 0.025
        "v01/photowank03.jpg"
        pause 0.025
        "v01/photowank04.jpg"
        pause 0.025
        "v01/photowank05.jpg"
        pause 0.025
        "v01/photowank06.jpg"
        pause 0.025
        "v01/photowank07.jpg"
        pause 0.025
        "v01/photowank08.jpg"
        pause 0.025
        "v01/photowank09.jpg"
        pause 0.025
        "v01/photowank10.jpg"
        pause 0.025
        "v01/photowank11.jpg"
        pause 0.025
        "v01/photowank12.jpg"
        pause 0.03
        "v01/photowank11.jpg"
        pause 0.025
        "v01/photowank10.jpg"
        pause 0.025
        "v01/photowank09.jpg"
        pause 0.025
        "v01/photowank08.jpg"
        pause 0.025
        "v01/photowank07.jpg"
        pause 0.025
        "v01/photowank06.jpg"
        pause 0.025
        "v01/photowank05.jpg"
        pause 0.025
        "v01/photowank04.jpg"
        pause 0.025
        "v01/photowank03.jpg"
        pause 0.025
        "v01/photowank02.jpg"
        pause 0.025
        "v01/photowank01.jpg"
        pause 0.025
        repeat
        
    image excellateaselick:
        "v052/excellatease09.jpg" with fastdissolve
        pause .7
        "v052/excellatease10.jpg" with fastdissolve
        pause .5
        repeat

    image loissuperlick:
        "v042/supermanshoot37.jpg" with fastdissolve
        pause .7
        "v042/supermanshoot38.jpg" with fastdissolve
        pause .5
        repeat

    image friedatits:
        "v051/interrogation15.jpg" with fastdissolve
        pause 1.0
        "v051/interrogation16.jpg" with fastdissolve
        pause 0.5
        "v051/interrogation17.jpg" with fastdissolve
        pause 1.0
        "v051/interrogation18.jpg" with fastdissolve
        pause 0.5
        repeat

    image harleystoredildo:
        "v041/harleystore23.jpg" with fastdissolve
        pause .7
        "v041/harleystore24.jpg" with fastdissolve
        pause .5
        repeat

    image auditbackmassagea:
        "v01/auditmassage15a.jpg" with dissolve
        pause 1
        "v01/auditmassage15b.jpg" with dissolve
        pause 1
        repeat
        
    image auditbackmassageb:
        "v01/auditmassage15a.jpg" with fastdissolve
        pause .7
        "v01/auditmassage15b.jpg" with fastdissolve
        pause .7
        repeat

    image cockhamplanet01:
        "v01/cockhamplanet01a.jpg" with fastdissolve
        pause 2
        "v01/cockhamplanet01b.jpg" with fastdissolve
        pause 1.5
        repeat

    image sirensbaranim:
        "sirens01bara blurred" with fastdissolve
        pause 4
        "sirens01barb blurred" with fastdissolve
        pause 2.5
        repeat

    image ccpd01back:
        "v01/ccpd01back01.png" with fastdissolve
        pause 1
        "v01/ccpd01back02.png" with fastdissolve
        pause 1.2
        repeat

    image special01:
        "v023/special01b.jpg" with fastdissolve
        pause 1.5
        "v023/special01a.jpg" with fastdissolve
        pause 1.0
        repeat

    image embassy06c:
        "v042/embassy06a.jpg" with fastdissolve
        pause 1.5
        "v042/embassy06bb.jpg" with fastdissolve
        pause 1.0
        repeat

    image widowlarapoolwank:
        "v042/larawidowpool11a.jpg" with dissolve
        pause 0.8
        "v042/larawidowpool11b.jpg" with dissolve
        pause 0.8
        repeat

    image stroheim05:
        "v023/stroheim05b.jpg" with fastdissolve
        pause 1.5
        "v023/stroheim05a.jpg" with fastdissolve
        pause 1.0
        repeat
        
    image auditjacuzzisplash:
        subpixel True
        "v03/auditjacuzzicum06.jpg" with fastdissolve
        pause 1.0
        "v03/auditjacuzzicum07.jpg" with fastdissolve
        pause .6
        repeat
        
    image wonderfightfistfuck:
        subpixel True
        "v03/wonderfight28.jpg" with fastdissolve
        pause 0.5
        "v03/wonderfight29.jpg" with fastdissolve
        pause 0.2
        "v03/wonderfight30.jpg" with fastdissolve
        pause 1.0
        "v03/wonderfight29.jpg" with fastdissolve
        pause 0.2
        repeat
            
    image doublethroatsup:
        "v031/supthroatpost04.jpg" with fastdissolve
        pause 0.6
        "v031/supthroatpost05.jpg" with fastdissolve
        pause 1.2
        repeat

    image wondertitslap:
        "v06/wonderworn16.jpg" with fastdissolve
        pause .7
        "v06/wonderworn17.jpg" with fastdissolve
        pause .5
        repeat

    transform frostzoomleft:
        subpixel True
        ease 2.5 zoom 1 xoffset 0 yoffset -100
    transform frostzoomleftcenter:
        subpixel True
        ease 2.5 zoom 1 xoffset 0 yoffset -400
    transform frostzoomleftdown:
        subpixel True
        ease 2.5 zoom 1 xoffset 0 yoffset -1000
    transform frostzoomleftout:
        subpixel True
        ease 2.5 zoom 1 xoffset -2000 yoffset -1000
    transform frostunzoomleft:
        subpixel True
        ease 1.5 zoom 0.5 xoffset 0 yoffset 0
    transform frostwiggleleft:
        subpixel True
        ease 1.5 zoom 1 xoffset 0 yoffset 0
    transform frostwiggleright:
        subpixel True
        ease 1.5 zoom 1 xoffset 900 yoffset 0
    transform frostunzoomwiggle:
        subpixel True
        ease 1.5 zoom 1 xoffset 400 yoffset 0
    transform frostunzoomwiggleout:
        subpixel True
        ease 1.5 zoom 1 xoffset -1200 yoffset 0
    transform frostzoomleft02:
        subpixel True
        ease 1.5 zoom 1 xoffset -1800 yoffset -300
    transform frostzoombackgroundleft:
        subpixel True
        ease 2.5 zoom 1.5 xoffset 200 yoffset 300
    transform frostzoombackgroundleftcenter:
        subpixel True
        ease 2.5 zoom 1.5 xoffset 200 yoffset 0
    transform frostzoombackgroundright:
        subpixel True
        ease 2.5 zoom 1.5 xoffset -300 yoffset 300
    transform frostzoombackgroundleftup:
        subpixel True
        ease 2.5 zoom 1.5 xoffset 200 yoffset 200
    transform frostzoombackgroundrightup:
        subpixel True
        ease 2.5 zoom 1.5 xoffset 400 yoffset 0
    transform frostzoombackgroundleftdown:
        subpixel True
        ease 2.5 zoom 1.5 xoffset 300 yoffset 0
    transform frostzoombackgroundrightdown:
        subpixel True
        ease 2.5 zoom 1.5 xoffset -300 yoffset 0
    transform frostunzoombackgroundleft:
        subpixel True
        ease 1.5 zoom 1 xoffset 0 yoffset 0
    transform widowzoomleft:
        subpixel True
        ease 2.5 zoom 1 xoffset 1200 yoffset -100
    transform widowunzoomleft:
        subpixel True
        ease 1.5 zoom .5 xoffset 800 yoffset 0
    transform widowunzoomleftfar:
        subpixel True
        ease 1.5 zoom .5 xoffset 1500 yoffset 0
    transform widowzoomleft02:
        subpixel True
        ease 2.5 zoom 1 xoffset 0 yoffset -400
    transform widowzoomleftdown:
        subpixel True
        ease 2.0 zoom 1 xoffset 0 yoffset -1080
    transform widowunzoomleftdown:
        subpixel True
        ease 2.5 xoffset 1600 yoffset -900
    transform frostzoomleftdown:
        subpixel True
        ease 2.5 zoom 1 xoffset 0 yoffset -900
    transform frostzoomleftdownup:
        subpixel True
        ease 2.5 xoffset 0 yoffset -400
    transform widowzoomleftfar:
        subpixel True
        ease 2.5 zoom 1 xoffset 1500 yoffset -400
    transform widowzoomleftfar02:
        subpixel True
        ease 1.5 zoom 1 xoffset 1600 yoffset -200
    transform titfuckbackground:
        subpixel True
        ease 0.525 xoffset 0 yoffset -50
        ease 0.49 xoffset 0 yoffset 0
        repeat
    transform honokazoom03:
        subpixel True
        zoom 1.2 xoffset 0 yoffset -220
    transform honokafullbackzoombackground:
        subpixel True
        ease 8.0 zoom 1.0 xoffset 0 yoffset 0
    transform honokafullup:
        subpixel True
        ease 7.0 zoom 1 xoffset 250 yoffset 0
    transform widowpoolbackzoombackground:
        subpixel True
        ease 8.0 zoom 1.05 xoffset -50 yoffset -1080
    transform powerpoolfullup:
        subpixel True
        ease 7.0 zoom 1 xoffset 0 yoffset -1200
    transform powerpoolfulldown:
        subpixel True
        ease 7.0 zoom 1 xoffset 80 yoffset 0
    transform powerpoolfulldown02:
        subpixel True
        ease 7.0 zoom 1 xoffset 0 yoffset 0

    transform widowgymfullup:
        subpixel True
        ease 8.0 zoom 1 xoffset 0 yoffset -400
    transform widowgymfulldown:
        subpixel True
        ease 8.0 zoom 1 xoffset 0 yoffset -1600

    transform powerbellanim:
        subpixel True
        ease 1.525 xoffset 450 yoffset -30
        ease 1.49 xoffset 450 yoffset 0
        repeat
    transform powerbellanim2:
        subpixel True
        ease 1.525 xoffset 350 yoffset -30
        ease 1.49 xoffset 350 yoffset 0
        repeat
    transform powerbellanimback:
        subpixel True
        ease 1.525 xoffset 0 yoffset 20
        ease 1.49 xoffset 0 yoffset 0
        repeat

    transform widowpoolfullup:
        subpixel True
        ease 7.0 zoom 1 xoffset 50 yoffset -1080
    transform widowfullbackzoombackground:
        subpixel True
        ease 8.0 zoom 1.7 xoffset 0 yoffset 720
    transform widowbackfulldown:
        subpixel True
        ease 7.0 zoom 1 xoffset 200 yoffset -1080
    transform widowbackfullbackzoombackground:
        subpixel True
        ease 8.0 zoom 1.7 xoffset 200 yoffset -0
    transform poolbackgroundup:
        subpixel True
        ease 7.0 zoom 1.8 xoffset -450 yoffset 0
    transform poolbackgroundpowerup:
        subpixel True
        ease 8.0 zoom 1.0 xoffset 0 yoffset -100
    transform poolbackgroundpowerup02:
        subpixel True
        ease 8.0 zoom 1.0 xoffset 0 yoffset -200
    transform harleybackgrounddown:
        subpixel True
        ease 8.0 zoom 1.8 xoffset -300 yoffset -1080
    transform harleyfulldown:
        subpixel True
        ease 7.0 zoom 1 xoffset -100 yoffset -1080
    transform powerfullup:
        subpixel True
        ease 7.0 zoom 1 xoffset 50 yoffset 0
    transform powerfulldown:
        subpixel True
        ease 7.0 zoom 1 xoffset 50 yoffset -1080
    transform powerfulldown02:
        subpixel True
        ease 7.0 zoom 1 xoffset 50 yoffset -800
    transform powerfulldownbackground:
        subpixel True
        ease 8.0 zoom 1.8 xoffset -50 yoffset -800
    transform henchmandown01:
        subpixel True
        xoffset 500 yoffset 0
    transform henchmandown02:
        subpixel True
        ease 2.0 zoom 1.05 xoffset 500 yoffset 2000
    transform backalleydown:
        subpixel True
        ease 2.0 xoffset 0 yoffset 2000
    transform scarlettfullzoombackground:
        subpixel True
        ease 5.5 zoom 1.1 xoffset 0 yoffset 0
    transform scarlettfullzoom:
        subpixel True
        linear 6.0 xoffset 50 yoffset -100
    transform scarlettfulldownzoombackground:
        subpixel True
        ease 5.5 zoom 1.1 xoffset 0 yoffset -1080
    transform scarlettfulldownzoom:
        subpixel True
        linear 6.0 xoffset 0 yoffset -1080
    transform sawyerstreetbackground:
        subpixel True
        ease 0.68 xoffset 0 yoffset 0
        ease 0.68 xoffset 0 yoffset -10
        repeat
    transform sawyerstreetbackgroundb:
        subpixel True
        ease 0.45 xoffset 0 yoffset 0
        ease 0.45 xoffset 0 yoffset -10
        repeat

    transform harleyassbackgroundpos01:
        subpixel True
        ease 0.82 xoffset 0 yoffset -50
        ease 0.82 xoffset 0 yoffset 0
        repeat
    transform harleyassbackgroundpos02:
        subpixel True
        ease 0.49 xoffset 0 yoffset -50
        ease 0.49 xoffset 0 yoffset 0
        repeat
    transform harleyassbackgroundpos03:
        subpixel True
        ease 0.35 xoffset 0 yoffset -50
        ease 0.35 xoffset 0 yoffset 0
        repeat
    transform moveleftinslow:
        subpixel True
        linear 1.0 xpos 0.5            
    transform moveleftoutslow:
        subpixel True
        linear 1.0 xpos -0.5            
    
    transform breathe:
        subpixel True
        ycenter .5
        block:
            ease 1. zoom 1.003
            ease 0.5 zoom 1.
            function renpy.partial(pause_trans, pi=1, po=4)
            repeat
        
    transform conscienceflydown:
        subpixel True
        ease 2.0 zoom 1.01 xoffset 0 yoffset 50
    transform conscienceflyup:
        subpixel True
        ease 0.5 zoom 1.00 xoffset 0 yoffset 0
        repeat
        
    image angelafly01:
        "intro/angela01a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/angela01b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image angelafly02:
        "intro/angela02a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/angela02b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image angelafly03:
        "intro/angela03a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/angela03b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image angelafly04:
        "intro/angela04a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/angela04b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image demonafly01:
        "intro/demona01a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/demona01b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image demonafly02:
        "intro/demona02a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/demona02b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image demonafly03:
        "intro/demona03a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/demona03b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image demonafly04:
        "intro/demona04a.png"
        linear 2.0 xoffset 0 yoffset 50
        "intro/demona04b.png"
        ease 0.5 xoffset 0 yoffset 0
        repeat

    image ghostanim:
        "v01/ghost03.png"
        linear 3.0 xoffset 0 yoffset 50
        "v01/ghost02.png"
        ease 1.5 xoffset 0 yoffset 0
        repeat

    image milfdream:
        "v01/milfdream01.png"
        2.0
        "v01/milfdream02.png"
        2.0
        "v01/milfdream03.png"
        2.0
        "v01/milfdream04.png"
        2.0
        "v01/milfdream05.png"
        2.0
        repeat

    image widowdream:
        "v01/widowdream01.png"
        2.0
        "v01/widowdream02.png"
        2.0
        "v01/widowdream03.png"
        2.0
        "v01/widowdream04.png"
        2.0
        "v01/widowdream05.png"
        2.0
        repeat

    image frostdream:
        "v01/frostdream01.png"
        2.0
        "v01/frostdream02.png"
        2.0
        "v01/frostdream03.png"
        2.0
        "v01/frostdream04.png"
        2.0
        "v01/frostdream05.png"
        2.0
        repeat

    image powerdream:
        "v02/powerdream01.png"
        2.0
        "v02/powerdream02.png"
        2.0
        "v02/powerdream03.png"
        2.0
        "v02/powerdream04.png"
        2.0
        "v02/powerdream05.png"
        2.0
        repeat

    image wonderdream:
        "v02/wonderdream01.png"
        2.0
        "v02/wonderdream02.png"
        2.0
        "v02/wonderdream03.png"
        2.0
        "v02/wonderdream04.png"
        2.0
        "v02/wonderdream05.png"
        2.0
        repeat

    image auditdream:
        "v02/auditdream01.png"
        2.0
        "v02/auditdream02.png"
        2.0
        "v02/auditdream03.png"
        2.0
        "v02/auditdream04.png"
        2.0
        "v02/auditdream05.png"
        2.0
        repeat

    image laradream:
        "v021/laradream01.png"
        2.0
        "v021/laradream02.png"
        2.0
        "v021/laradream03.png"
        2.0
        "v021/laradream04.png"
        2.0
        "v021/laradream05.png"
        2.0
        repeat

    image angeladream:
        "v022/angeladream01.png"
        2.0
        "v022/angeladream02.png"
        2.0
        "v022/angeladream03.png"
        2.0
        "v022/angeladream04.png"
        2.0
        "v022/angeladream05.png"
        2.0
        repeat

    image demonadream:
        "v022/demonadream01.png"
        2.0
        "v022/demonadream02.png"
        2.0
        "v022/demonadream03.png"
        2.0
        "v022/demonadream04.png"
        2.0
        "v022/demonadream05.png"
        2.0
        repeat

    image sawyerdream:
        "v022/sawyerdream01.png"
        2.0
        "v022/sawyerdream02.png"
        2.0
        "v022/sawyerdream03.png"
        2.0
        "v022/sawyerdream04.png"
        2.0
        "v022/sawyerdream05.png"
        2.0
        repeat

    image supergirldream:
        "v031/supergirldream01.png"
        2.0
        "v031/supergirldream02.png"
        2.0
        "v031/supergirldream03.png"
        2.0
        "v031/supergirldream04.png"
        2.0
        "v031/supergirldream05.png"
        2.0
        repeat

    image jacuzzijo:
        "v01/mcjacuzzi03.jpg" with fastdissolve
        0.5 
        "v01/mcjacuzzi04.jpg" with fastdissolve
        0.5
        repeat

    image jacuzzijolevel02:
        "v031/mcwanklevel02c.jpg" with fastdissolve
        0.5 
        "v031/mcwanklevel02d.jpg" with fastdissolve
        0.5
        repeat

    image jacuzzijofast:
        "v01/mcjacuzzi03.jpg" with fastdissolve
        0.3 
        "v01/mcjacuzzi04.jpg" with fastdissolve
        0.3
        repeat

    image jacuzzijofastlevel02:
        "v031/mcwanklevel02c.jpg" with fastdissolve
        0.3 
        "v031/mcwanklevel02d.jpg" with fastdissolve
        0.3
        repeat

    image catherineshowerdick:
        "v02/catherineshower08a.jpg" with fastdissolve
        0.5 
        "v02/catherineshower08b.jpg" with fastdissolve
        0.5
        repeat

    transform duelmc:
        subpixel True
        zoom 0.5
        linear 3.0 zoom 1.5 xoffset -2000 yoffset -550
    transform duelpi:
        subpixel True
        zoom 0.5
        linear 3.0 zoom 1.5 xoffset -1920 yoffset -600
            
    transform posgalleryhintpic:
        xpos 450 ypos 880

    transform posgalleryhint:
        xpos 800 ypos 900

    transform posbackicon:
        xpos 1735 ypos 1020

    transform poslocation:
        subpixel True
        xpos 1920 ypos 300
        linear .5 xpos 1400

    transform posharem:
        subpixel True
        xpos -200 ypos 300
        linear .5 xpos 100

    transform posharemtext:
        xpos 53 ypos 525

    transform posiconup:
        subpixel True
        xpos 1920 ypos 100
        linear .5 xpos 1400

    transform posadatext:
        xpos 1300 ypos 300

    transform posmissiontext:
        xpos 1300 ypos 470
    transform posmissiontextb:
        xpos 1360 ypos 470

    transform posmissionherotext:
        xpos 1570 ypos 250

    transform poswin:
        xpos 1440 ypos 300
        
    transform posmcicon:
        xpos 800 ypos 860
        
    transform posmission01:
        xpos 150 ypos 200
    transform posmissiontext01:
        xpos 150 ypos 160
    transform posmission02:
        xpos 150 ypos 450
    transform posmissiontext02:
        xpos 150 ypos 410
    transform posmission03:
        xpos 150 ypos 700
    transform posmissiontext03:
        xpos 150 ypos 660

    transform posdream:
        xpos 0.02 ypos 0.02

    transform posdream02:
        xpos 0.1 ypos 0.05

    transform usepowersbar01:
        xpos 0.1 ypos 0.2

    transform usepowers01:
        xpos 0.1 ypos 0.1
    
    transform poshall:
        xpos 0.05 ypos 0.1
    transform poshall01:
        xpos 0.055 ypos 0.09
    transform poshall02:
        xpos 0.075 ypos 0.09
    transform poshall03:
        xpos 0.095 ypos 0.09

    transform pospool:
        xpos 0.15 ypos 0.1
    transform pospool01:
        xpos 0.155 ypos 0.09
    transform posgym02:
        xpos 0.175 ypos 0.09
    transform posgym03:
        xpos 0.195 ypos 0.09

    transform posgym:
        xpos 0.25 ypos 0.1
    transform posgym01:
        xpos 0.255 ypos 0.09
    transform posgym02:
        xpos 0.275 ypos 0.09
    transform posgym03:
        xpos 0.295 ypos 0.09

    transform poslib:
        xpos 0.35 ypos 0.1
    transform poslib01:
        xpos 0.355 ypos 0.09
    transform poslib02:
        xpos 0.375 ypos 0.09

    transform posbwr:
        xpos 0.05 ypos 0.3
    transform posbwr01:
        xpos 0.055 ypos 0.29

    transform poscmr:
        xpos 0.15 ypos 0.3
    transform poscmr01:
        xpos 0.155 ypos 0.29

    transform pospgr:
        xpos 0.25 ypos 0.3
    transform pospgr01:
        xpos 0.255 ypos 0.29
    transform pospgr02:
        xpos 0.275 ypos 0.29

    transform poswwr:
        xpos 0.35 ypos 0.3
    transform poswwr01:
        xpos 0.355 ypos 0.29

    transform poslcr:
        xpos 0.45 ypos 0.3
    transform poslcr01:
        xpos 0.455 ypos 0.29

    transform posmap:
        xpos 0.5 ypos 0.6

    transform posmafia:
        xpos 369 ypos 795

    transform posfrost:
        xpos 872 ypos 710

    transform poslois:
        xpos 344 ypos 285

    transform posplanet:
        xpos 496 ypos 369

    transform posccpd:
        xpos 257 ypos 426

    transform posmayors:
        xpos 98 ypos 187

    transform posstallion:
        xpos 48 ypos 726

    transform poslingerie:
        xpos 923 ypos 287

    transform posquiff:
        xpos 1470 ypos 380

    transform possirens:
        xpos 1105 ypos 543

    transform postriad:
        xpos 578 ypos 722
    
    transform posnazi:
        xpos 1474 ypos 541

    transform posarkham:
        xpos 1282 ypos 238

    transform posivy:
        xpos 701 ypos 443

    transform posembassy:
        xpos 1235 ypos 705

    transform poscatcave:
        xpos 611 ypos 195

    transform posevil00:
        xpos 225 ypos 1040
    transform posevil01:
        xpos 265 ypos 1040
    transform posevil02:
        xpos 290 ypos 1040
    transform posevil03:
        xpos 315 ypos 1040
    transform posevil04:
        xpos 340 ypos 1040
    transform posevil05:
        xpos 365 ypos 1040
    transform posevil06:
        xpos 390 ypos 1040
    transform posevil07:
        xpos 415 ypos 1040
    transform posevil08:
        xpos 440 ypos 1040
    transform posevil09:
        xpos 465 ypos 1040
    transform posevilneutral:
        xpos 475 ypos 1040
    transform posevil13:
        xpos 565 ypos 1040
    transform posevil14:
        xpos 590 ypos 1040
    transform posevil15:
        xpos 615 ypos 1040
    transform posevil16:
        xpos 640 ypos 1040
    transform posevil17:
        xpos 665 ypos 1040
    transform posevil18:
        xpos 690 ypos 1040
    transform posevil19:
        xpos 715 ypos 1040
    transform posevil20:
        xpos 740 ypos 1040
    transform posevil21:
        xpos 765 ypos 1040
    transform posevil22:
        xpos 790 ypos 1040

    transform posinventory01:
        xpos 1084 ypos 150
    transform posinventory02:
        xpos 1273 ypos 150
    transform posinventory03:
        xpos 1462 ypos 150
    transform posinventory04:
        xpos 1651 ypos 150
    transform posinventory05:
        xpos 1084 ypos 350
    transform posinventory06:
        xpos 1273 ypos 350
    transform posinventory07:
        xpos 1462 ypos 350
    transform posinventory08:
        xpos 1651 ypos 350
    transform posinventory09:
        xpos 1084 ypos 550
    transform posinventory10:
        xpos 1273 ypos 550
    transform posinventory11:
        xpos 1462 ypos 550
    transform posinventory12:
        xpos 1651 ypos 550
    
    transform posinventorytext01:
        xpos 1070 ypos 280
    transform posinventorytext02:
        xpos 1260 ypos 280
    transform posinventorytext03:
        xpos 1450 ypos 270
    transform posinventorytext04:
        xpos 1640 ypos 270
    transform posinventorytext05:
        xpos 1070 ypos 470
    transform posinventorytext06:
        xpos 1260 ypos 470
    transform posinventorytext07:
        xpos 1450 ypos 470
    transform posinventorytext08:
        xpos 1640 ypos 470
    transform posinventorytext09:
        xpos 1070 ypos 670
    transform posinventorytext10:
        xpos 1260 ypos 670
    transform posinventorytext11:
        xpos 1450 ypos 670
    transform posinventorytext12:
        xpos 1640 ypos 670
    
    transform postopmissiontext:
        xpos 300 ypos 380
    transform postopquesttext:
        xpos 1250 ypos 380

    transform posquesthints01:
        xpos 1000 ypos 500
    transform posmissionhints01:
        xpos 100 ypos 500
    transform posmissionhints02:
        xpos 100 ypos 550
        
    transform PosHero:
        xpos 900
        ypos 90
    transform PosHeight:
        xpos 1400
        ypos 200
    transform PosAge:
        xpos 1000
        ypos 200
    transform PosHero01:
        xpos 1000
        ypos 90
    transform PosHero02:
        xpos 1100
        ypos 90
    transform PosHero03:
        xpos 1200
        ypos 90
    transform PosHeight01:
        xpos 1500
        ypos 200
    transform PosAge01:
        xpos 1100
        ypos 200
    transform PosMeasurements:
        xpos 1250
        ypos 250
    transform PosKink:
        xpos 1200
        ypos 350
    transform PosKink01:
        xpos 1200
        ypos 450
    transform PosKink02:
        xpos 1200
        ypos 500
    transform PosKink03:
        xpos 1200
        ypos 550
    transform PosKink04:
        xpos 1200
        ypos 600
    transform PosKink05:
        xpos 1200
        ypos 650
    transform PosScale:
        xpos 1100
        ypos 1000
    transform Line01:
        xpos 880
        ypos 250
    transform Line02:
        xpos 880
        ypos 275
    transform Line03:
        xpos 880
        ypos 300
    transform Line04:
        xpos 880
        ypos 325
    transform Line05:
        xpos 880
        ypos 350
    transform Line06:
        xpos 880
        ypos 375


    transform Line11:
        xpos 880
        ypos 860
    transform Line12:
        xpos 880
        ypos 885
    transform Line13:
        xpos 880
        ypos 910


    transform PowerName01:
        xpos 900
        ypos 500
    transform Power01a:
        xpos 880
        ypos 530
    transform Power01b:
        xpos 970
        ypos 530
    transform Power01c:
        xpos 1060
        ypos 530

    transform PowerName02:
        xpos 1200
        ypos 500
    transform Power02a:
        xpos 1180
        ypos 530
    transform Power02b:
        xpos 1270
        ypos 530
    transform Power02c:
        xpos 1360
        ypos 530

    transform PowerName03:
        xpos 1500
        ypos 500
    transform Power03a:
        xpos 1480
        ypos 530
    transform Power03b:
        xpos 1570
        ypos 530
    transform Power03c:
        xpos 1660
        ypos 530

    transform PowerName04:
        xpos 900
        ypos 650
    transform Power04a:
        xpos 880
        ypos 680
    transform Power04b:
        xpos 970
        ypos 680
    transform Power04c:
        xpos 1060
        ypos 680

    transform PowerName05:
        xpos 1200
        ypos 650
    transform Power05a:
        xpos 1180
        ypos 680
    transform Power05b:
        xpos 1270
        ypos 680
    transform Power05c:
        xpos 1360
        ypos 680

    transform PowerName06:
        xpos 1500
        ypos 650
    transform Power06a:
        xpos 1480
        ypos 680
    transform Power06b:
        xpos 1570
        ypos 680
    transform Power06c:
        xpos 1660
        ypos 680

    transform PowerName07:
        xpos 900
        ypos 800
    transform Power07a:
        xpos 880
        ypos 830
    transform Power07b:
        xpos 970
        ypos 830
    transform Power07c:
        xpos 1060
        ypos 830

    transform PowerName08:
        xpos 1220
        ypos 800
    transform Power08a:
        xpos 1200
        ypos 830
    transform Power08b:
        xpos 1290
        ypos 830
    transform Power08c:
        xpos 1138
        ypos 830

    transform PowerName09:
        xpos 1540
        ypos 800
    transform Power09a:
        xpos 1520
        ypos 830
    transform Power09b:
        xpos 1610
        ypos 830
    transform Power09c:
        xpos 1700
        ypos 830

    transform posstatshero:
        xpos 800
        ypos 30
    transform posstatslevel:
        xpos 600
        ypos 1020
    transform posstatsage:
        xpos 600
        ypos 980

    transform posharem01:
        xpos 200
        ypos 200
    transform posharem02:
        xpos 460
        ypos 200
    transform posharem03:
        xpos 720
        ypos 200
    transform posharem04:
        xpos 980
        ypos 200
    transform posharem05:
        xpos 1240
        ypos 200
    transform posharem06:
        xpos 1500
        ypos 200
    transform posharem07:
        xpos 200
        ypos 600
    transform posharem08:
        xpos 460
        ypos 600
    transform posharem09:
        xpos 720
        ypos 600
    transform posharem10:
        xpos 980
        ypos 600
    transform posharem11:
        xpos 1240
        ypos 600
    transform posharem12:
        xpos 1500
        ypos 600

    transform posgood01:
        xpos 260
        ypos 978
    transform posgood02:
        xpos 285
        ypos 978
    transform posgood03:
        xpos 310
        ypos 978
    transform posgood04:
        xpos 335
        ypos 978
    transform posgood05:
        xpos 360
        ypos 978
    transform posgood06:
        xpos 385
        ypos 978
    transform posgood07:
        xpos 410
        ypos 978
    transform posgood08:
        xpos 435
        ypos 978
    transform posgood09:
        xpos 460
        ypos 978
    transform posgood10:
        xpos 485
        ypos 978


    transform posgood13:
        xpos 585
        ypos 978
    transform posgood14:
        xpos 610
        ypos 978
    transform posgood15:
        xpos 635
        ypos 978
    transform posgood16:
        xpos 660
        ypos 978
    transform posgood17:
        xpos 685
        ypos 978
    transform posgood18:
        xpos 710
        ypos 978
    transform posgood19:
        xpos 735
        ypos 978
    transform posgood20:
        xpos 760
        ypos 978
    transform posgood21:
        xpos 785
        ypos 978
    transform posgood22:
        xpos 810
        ypos 978

    transform posquest01:
        xpos 1000
        ypos 200
    transform posquesttext01:
        xpos 1000
        ypos 160
    transform posquestwin01:
        xpos 1020
        ypos 200
    transform posquest02:
        xpos 1000
        ypos 450
    transform posquesttext02:
        xpos 1000
        ypos 410
    transform posquestwin02:
        xpos 1020
        ypos 450
    transform posquest03:
        xpos 1000
        ypos 700
    transform posquesttext03:
        xpos 1000
        ypos 660
    transform posquestwin03:
        xpos 1020
        ypos 700
        
    transform posdossierhero:
        xpos 70 ypos 25
    
    transform gallerypos01:
        xpos 35 ypos 100
    transform gallerypos02:
        xpos 345 ypos 100
    transform gallerypos03:
        xpos 655 ypos 100
    transform gallerypos04:
        xpos 965 ypos 100
    transform gallerypos05:
        xpos 1275 ypos 100
    transform gallerypos06:
        xpos 1585 ypos 100

    transform galleryanimpos:
        xpos 67 ypos 1028

    transform galleryposleftarrow:
        xpos 5 ypos 500
    transform galleryposrightarrow:
        xpos 1890 ypos 500
        
    transform gallerytext01:
        xpos 400 ypos 280
    transform gallerytext02:
        xpos 750 ypos 280
    transform gallerytext03:
        xpos 1100 ypos 280
    transform gallerytext04:
        xpos 1450 ypos 280
    transform gallerytext05:
        xpos 400 ypos 560
    transform gallerytext06:
        xpos 750 ypos 560
    transform gallerytext07:
        xpos 1100 ypos 560
    transform gallerytext08:
        xpos 1450 ypos 560
    transform gallerytext09:
        xpos 400 ypos 840
    transform gallerytext10:
        xpos 750 ypos 840
    transform gallerytext11:
        xpos 1100 ypos 840
    transform gallerytext12:
        xpos 1450 ypos 840
        
        
    transform gallerytexthero01:
        xpos 600 ypos 100
    transform gallerytexthero02:
        xpos 950 ypos 100
    transform gallerytexthero03:
        xpos 1300 ypos 100
    transform gallerytexthero04:
        xpos 1650 ypos 100
    transform gallerytexthero05:
        xpos 600 ypos 380
    transform gallerytexthero06:
        xpos 950 ypos 380
    transform gallerytexthero07:
        xpos 1300 ypos 380
    transform gallerytexthero08:
        xpos 1650 ypos 380
    transform gallerytexthero09:
        xpos 600 ypos 660
    transform gallerytexthero10:
        xpos 950 ypos 660
    transform gallerytexthero11:
        xpos 1300 ypos 660
    transform gallerytexthero12:
        xpos 1450 ypos 660

    transform gallerytoptext:
        xpos 600 ypos 25
    transform gallerytoptext02:
        xpos 100 ypos 25

    transform extrapowermenupos:
        xpos 1400 ypos 50
    transform extrapowerpos01:
        xpos 1600 ypos 200
    transform extrapowerpos02:
        xpos 1600 ypos 400
    transform extrapowerpos03:
        xpos 1600 ypos 600
    transform extrapowerpos04:
        xpos 1600 ypos 800

    transform extrapowertextpos01:
        xpos 1570 ypos 300
    transform extrapowertextpos02:
        xpos 1570 ypos 500
    transform extrapowertextpos03:
        xpos 1550 ypos 700
    transform extrapowertextpos04:
        xpos 1570 ypos 900

    image harleychoke:
        "v061/harleychoke04.jpg" with fastdissolve
        0.8
        "v061/harleychoke05.jpg" with fastdissolve
        1.2
        repeat

    image harleyslap:
        "v061/harleycell29.jpg" with fastdissolve
        0.5
        "v061/harleycell28.jpg" with fastdissolve
        1.0
        repeat

    image loisasscrack:
        "v052/loisdildo12.jpg" with fastdissolve
        0.7
        "v052/loisdildo13.jpg" with fastdissolve
        0.7
        repeat

    image loisrackdildo:
        "v042/supermanshoot23.jpg" with fastdissolve
        0.5
        "v042/supermanshoot24.jpg" with fastdissolve
        1.0
        repeat

    image loisrackhand:
        "v02/loisrack04.jpg" with fastdissolve
        0.5
        "v02/loisrack03.jpg" with fastdissolve
        1.0
        repeat

    image loisrackcock:
        "v02/loisrack06.jpg" with fastdissolve
        0.4
        "v02/loisrack05.jpg" with fastdissolve
        0.8
        repeat

    image powersuperbreast:
        "v03/powersuper08a.jpg" with fastdissolve
        0.5
        "v03/powersuper08b.jpg" with fastdissolve
        1.0
        repeat
    
    image powersuperpussy:
        "v03/powersuper09a.jpg" with fastdissolve
        0.5
        "v03/powersuper09b.jpg" with fastdissolve
        1.0
        repeat
    
    image powercockslap:
        "v04/powerprefuck03.jpg" with fastdissolve
        0.4
        "v04/powerprefuck02.jpg" with fastdissolve
        0.8
        repeat

    image supergympushup:
        "v03/supergirlgym08.jpg" with fastdissolve
        0.5
        "v03/supergirlgym09.jpg" with fastdissolve
        1.0
        repeat

    image milfcockslap:
        "v031/mcroomsex19a.jpg" with fastdissolve
        0.8
        "v031/mcroomsex19b.jpg" with fastdissolve
        0.5
        repeat

    image useagility:
        alpha 0.
        "icons/usesuperagility.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usestrength:
        alpha 0.
        "icons/usesuperstrength.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usecombat:
        alpha 0.
        "icons/usesupercombat.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usehealing:
        alpha 0.
        "icons/usesuperhealing.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usesenses:
        alpha 0.
        "icons/usesupersenses.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usestud:
        alpha 0.
        "icons/usesuperstud.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image useresistance:
        alpha 0.
        "icons/usesuperresistance.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image useseduction:
        alpha 0.
        "icons/usesuperseduction.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    image usemind:
        alpha 0.
        "v041/usemindcontrol.png"
        block:
            linear .2 alpha 1.
            .2
            linear .2 alpha 0.
            .2
            repeat

    transform newhpunch(n=1):
        easein_back 0.03 xoffset -20
        easein_back 0.03 xoffset 20
        easein_back 0.03 xoffset -10
        easein_back 0.03 xoffset 10
        easein_back 0.03 xoffset -5
        easein_back 0.03 xoffset 5
        easein_back 0.03 xoffset 0
        pause 0.1
        repeat n

    screen usepower(img, l1, l2, t=2.4):
        default time_left = t
        default _img = [img] if isinstance(img, (str, unicode)) else img
        default _l2 = [l2] if isinstance(l2, (str, unicode)) else l2
        default img_l = len(_img)
        default hidden = False
        $print(img)
        if time_left <= 0:
            timer .01 action SetVariable("selected_power", None), Hide("usepower"), With(dissolve), Jump(l1)
        else:
            timer .1 repeat True action SetScreenVariable("time_left", time_left-.1)

        showif not hidden:
            vbox at usepowers01:
                spacing 10
                for i in range(img_l):
                    imagebutton:
                        idle _img[i]
                        action SetScreenVariable("hidden", True), SetVariable("selected_power", _img[i]), Hide("usepower"), With(dissolve), Jump(_l2[i])
                bar value AnimatedValue(0, 1, t, 1):
                    xsize 400
                    ysize 10
                    left_bar Color("#f00").rotate_hue(1. * time_left / t / 3)
                    right_bar Color("#f00").rotate_hue(1. * time_left / t / 3).opacity(.2)
                            
    style doss_text is text:
        color "#1c73ff"
        size 40
        outlines [(3, "#fff4", 0, 0), (2, "#fff8", 0, 0), (1, "#fffc", 0, 0)]

    style doss_vscrollbar is vscrollbar:
        unscrollable "hide"

    screen powers_frame(power, number):
        fixed:
            xysize (260, 120)
            add "icons/text{}.png".format(power):
                xpos 20
            hbox:
                spacing 10
                ypos 30
                for i in range(1,4):
                    if number >= i:
                        add "icons/super{}.png".format(power)
                    else:
                        add "icons/super{}grey.png".format(power)