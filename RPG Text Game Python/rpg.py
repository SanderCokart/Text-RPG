import sys
print("This is an rpg.\n")
HEALTH = "100";
STAMINA = "100";
name=input("What is your name, brave hero? \n")
print("--------------------------------------------")
print("\nOh, "+name+", is it? That's a good name.\n")
print("\nWe've had an awful year, fighting with a fearsome dragon up in the north. Please help us!\n")

Option1 = "none"

while Option1 != "Y" or Option1 != "N":
    Option1=input("Will you help? [Y/N]\n").upper()
    print("--------------------------------------------")
    if Option1=="Y":
        print("\nWhat a wonderful day! We finally have a hero to fight for us!\n")
        break;

    elif Option1=="N":
        print("\nOh, that's a shame...too bad.\n")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option1=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option1=="STAMINA":
        print ("Your stamine is at "+STAMINA)


Option2 = "none"

while Option2 !="" or Option2 != "E" or Option2 != "W" or Option2 != "S":
    Option2=input("\nNow you're off on your journey, which way would you like to go? [N, E, W, S]\n> ").upper()
    print("--------------------------------------------")

    if Option2=="N":
        print("\nYou travel North and find the dragon but you are unprepared and thus you had no way to defend yourself, the dragon picked you up and let your fall to your death from very high up.\n")
        print("\nYou die.\n")
        print("""\n
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\\
               ::::::;       ;          OOOOO\\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
        :`:::::::`;::::::;;::: ;::\#  /            DOOO
        ::`:::::::`;:::::::: ;::::\# /              DOO
        `:`:::::::`;:::::: ;::::::\#/               DOO
         :::`:::::::`;; ;:::::::::\#\#                OO
         ::::`:::::::`;::::::::;:::\#                OO
         `:::::`::::::::::::;'`:;::\#                O
          `:::::`::::::::;' /  / `:\#
           ::::::`:::::;'  /  /   `\#\n""")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option2=="E":
        print("\nYou walk for a long time into an arid county where there are a lot of creatures, unfortunatly one of them saw you for a snack and decided to eat you.\n")
        print("\nYou die\n")
        print("""\n
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\\
               ::::::;       ;          OOOOO\\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
        :`:::::::`;::::::;;::: ;::\#  /            DOOO
        ::`:::::::`;:::::::: ;::::\# /              DOO
        `:`:::::::`;:::::: ;::::::\#/               DOO
         :::`:::::::`;; ;:::::::::\#\#                OO
         ::::`:::::::`;::::::::;:::\#                OO
         `:::::`::::::::::::;'`:;::\#                O
          `:::::`::::::::;' /  / `:\#
           ::::::`:::::;'  /  /   `\#\n""")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option2=="W":
        print("\nYou travel towords towords the seaguls in the sky and follow them to the ocean, unfortunatly looking up to the sky doesn't always work out wel for people, and so you fall to your death off the cliff with your head impaled on a rock\n")
        print("\nYou die\n")
        print("""\n
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\\
               ::::::;       ;          OOOOO\\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
        :`:::::::`;::::::;;::: ;::\#  /            DOOO
        ::`:::::::`;:::::::: ;::::\# /              DOO
        `:`:::::::`;:::::: ;::::::\#/               DOO
         :::`:::::::`;; ;:::::::::\#\#                OO
         ::::`:::::::`;::::::::;:::\#                OO
         `:::::`::::::::::::;'`:;::\#                O
          `:::::`::::::::;' /  / `:\#
           ::::::`:::::;'  /  /   `\#\n""")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option2=="S":
        print("\nYou travel far away from the dragon in order to prepare and will need armor, stabbing weapons and consumables such as water and food, a potion or two won't hurt either.\n")
        break;

    elif Option4=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option4=="STAMINA":
        print ("Your stamine is at "+STAMINA)

Option3 = "none"

while Option3 !="RUSTIC TAVERN" or Option3 != "BANDIT LODGE" or Option3 != "CROSSROADS INN" or Option3 != "CONTINUE WALKING":
    HEALTH = "75"
    STAMINA = "50"
    Option3=input("\nYou walked a long way and reduced your STAMINA 50 and HEALTH to 75 as result of lack the lack of food. There are a number of taverns nearby where would you like to go? The Rustic Tavern, Bandit Lodge, Crossroads Inn or continue walking?\n").upper()
    print("--------------------------------------------")

    if Option3=="RUSTIC TAVERN":
        STAMINA = "100"
        HEALH = "75"
        print("""                              ____
                          _           |---||            _
                          ||__________|SSt||___________||
                         /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\\`.
                        /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\\:`.
                       /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\\::`.
                      /:.___________________________________\\:::`-._
                  _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
              _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
            ,'_:._________________________________________________`:_.::::-';`
             `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
              ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
              ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
              ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
              ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
              ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
           .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
            );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
            ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
            ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
            '''''           ''-         ''-         ''-         '''  '''""")
        print("\nThis seems like an old place but it will have to do, the beds are not comfortable and there is no water anywhere but at least your stamina is back up.\n")
        break;

    elif Option3=="BANDIT LODGE":
        print("""                                   /\\
                                      /\\  //\\\\
                               /\\    //\\\\///\\\\\\        /\\
                              //\\\\  ///\\////\\\\\\\\  /\\  //\\\\
                 /\\          /  ^ \\/^ ^/^  ^  ^ \\/^ \\/  ^ \\
                / ^\\    /\\  / ^   /  ^/ ^ ^ ^   ^\\ ^/  ^^  \\
               /^   \\  / ^\\/ ^ ^   ^ / ^  ^    ^  \\/ ^   ^  \\       *
              /  ^ ^ \\/^  ^\\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \\     /|\\
             / ^ ^  ^ \\ ^  _\\___________________|  |_____^ ^  \\   /||o\\
            / ^^  ^ ^ ^\\  /______________________________\\ ^ ^ \\ /|o|||\\
           /  ^  ^^ ^ ^  /________________________________\\  ^  /|||||o|\\
          /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\\
         / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
        / ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
        ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo""")
        print("\nYou get robbed on your way in and stabbed at the bar, with your current wounds you are unlikely to survive and in fact as you walk out the door you collapse and drown in the mud outside the door\n")
        print("\nYou die\n")
        print("""\n
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\\
               ::::::;       ;          OOOOO\\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
        :`:::::::`;::::::;;::: ;::\#  /            DOOO
        ::`:::::::`;:::::::: ;::::\# /              DOO
        `:`:::::::`;:::::: ;::::::\#/               DOO
         :::`:::::::`;; ;:::::::::\#\#                OO
         ::::`:::::::`;::::::::;:::\#                OO
         `:::::`::::::::::::;'`:;::\#                O
          `:::::`::::::::;' /  / `:\#
           ::::::`:::::;'  /  /   `\#\n""")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option3=="CROSSROADS INN":
        HEALH = "100"
        STAMINA = "100"
        print("""\n                                  .-.
                                         /___\\
                                         |___|
                                         |]_[|
                                         / I \\
                                      JL/  |  \\JL
           .-.                    i   ()   |   ()   i                    .-.
           |_|     .^.           /_\\  LJ=======LJ  /_\\           .^.     |_|
        ._/___\\._./___\\_._._._._.L_J_/.-.     .-.\\_L_J._._._._._/___\\._./___\\._._._
               ., |-,-| .,       L_J  |_| [I] |_|  L_J       ., |-,-| .,        .,
               JL |-O-| JL       L_J%%%%%%%%%%%%%%%L_J       JL |-O-| JL        JL
        IIIIII_HH_'-'-'_HH_IIIIII|_|=======H=======|_|IIIIII_HH_'-'-'_HH_IIIIII_HH_
        -------[]-------[]-------[_]----\\.=I=./----[_]-------[]-------[]--------[]-
         _/\\_  ||\\\\_I_//||  _/\\_ [_] []_/_L_J_\\_[] [_] _/\\_  ||\\\\_I_//||  _/\\_  ||\\
         |__|  ||=/_|_\\=||  |__|_|_|   _L_L_J_J_   |_|_|__|  ||=/_|_\\=||  |__|  ||-
         |__|  |||__|__|||  |__[___]__--__===__--__[___]__|  |||__|__|||  |__|  |||
        IIIIIII[_]IIIII[_]IIIIIL___J__II__|_|__II__L___JIIIII[_]IIIII[_]IIIIIIII[_]
         \\_I_/ [_]\\_I_/[_] \\_I_[_]\\II/[]\\_\\I/_/[]\\II/[_]\\_I_/ [_]\\_I_/[_] \\_I_/ [_]
        ./   \\.L_J/   \\L_J./   L_JI  I[]/     \\[]I  IL_J    \\.L_J/   \\L_J./   \\.L_J
        |     |L_J|   |L_J|    L_J|  |[]|     |[]|  |L_J     |L_J|   |L_J|     |L_J
        |_____JL_JL___JL_JL____|-||  |[]|     |[]|  ||-|_____JL_JL___JL_JL_____JL_J
                               '-''--'--'-----'--'--''-'\n""")
        print("\nThis look like a tavern where a lot of soldiers come through we might be safe here and it has a fireplace and lots of food and water this regenerates your health and stamina completely and stock up on food while you're there\n")
        break;

    elif Option3=="CONTINUE WALKING":
        print("\nYou get tired and exhausted from the long walk and collapse on the floor, unfortunatly this is the end of you\n")
        print("\nYou die\n")
        print("""\n
                     ;::::;
                   ;::::; :;
                 ;:::::'   :;
                ;:::::;     ;.
               ,:::::'       ;           OOO\\
               ::::::;       ;          OOOOO\\
               ;:::::;       ;         OOOOOOOO
              ,;::::::;     ;'         / OOOOOOO
            ;:::::::::`. ,,,;.        /  / DOOOOOO
          .';:::::::::::::::::;,     /  /     DOOOO
         ,::::::;::::::;;;;::::;,   /  /        DOOO
        ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
        :`:::::::`;::::::;;::: ;::\#  /            DOOO
        ::`:::::::`;:::::::: ;::::\# /              DOO
        `:`:::::::`;:::::: ;::::::\#/               DOO
         :::`:::::::`;; ;:::::::::\#\#                OO
         ::::`:::::::`;::::::::;:::\#                OO
         `:::::`::::::::::::;'`:;::\#                O
          `:::::`::::::::;' /  / `:\#
           ::::::`:::::;'  /  /   `\#\n""")
        print("\nPlease restart the game to try again")
        sys.exit()

    elif Option3=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option3=="STAMINA":
        print ("Your stamine is at "+STAMINA)


Option4 = "none"

while Option4 != "SMITH":
    Option4=input("\nYou are going to need weapons, where should we go?\n\nSmith?\nDoctor?\nCarpenter?\n\n").upper()
    print("--------------------------------------------")


    if Option4=="SMITH":
        print("""\n      '
               ,
               '
              '                   :=<]
               '          *__       /
              (          (___/     e
             '  )        ('L')    /
            ')('          \\=/____/
           ( )  )')      |   |
            ( /(( )      \\____m=====\\
           )')(( ) )      +()+      (")
        |E -_-_-_-_-||   ++vv++     ======
        |J-_-_-_-_-_||  +++++++       \\/
        |M-_-_-_---_|| ++++++++       /\\
        |9-_-_-_-_-_||   // ||       /  \\
        |6-_-_-_---_||  (__D(__D    /    \\\n""")
        print("\nYes indeed! Let's go!\n")
        print("\nYou find your way to the smith and get yourself a nice sword that you will use to fight the dragon! \n")
        break;

    elif Option4=="DOCTOR":
        print("""\n.     |___________________________________
        |-----|- - -|''''|''''|''''|''''|''''|'##\\|__
        |- -  |  cc 6    5    4    3    2    1 ### __]==----------------------
        |-----|________________________________##/|
        '     |""""""""""""""""""""""""""""""""""\"\n""")
        print("\nNo you dumbass...you don't mean to fight a dragon with needles right?\n")

    elif Option4=="CARPENTER":
        print("""
                   /\\                                                 /\\
         _         )( ______________________   ______________________ )(         _
        (_)///////(**)______________________> <______________________(**)\\\\\\\\\\\\\\(_)
                   )(                                                 )(
                   \\/                                                 \\/
        """)

        print("\nNo you dumbass...you wanna fight a dragon with a wooden stick? You must be new here.\n")

    elif Option4=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option4=="STAMINA":
        print ("Your stamine is at "+STAMINA)

Option5 = "none"

while Option5 != "ARMORER":
    Option5=input("\nYou are going to need armor as well, where should we go?\n\nSchool?\nArmorer?\nFortune Teller?\n\n").upper()
    print("--------------------------------------------")

    if Option5=="ARMORER":
        print("""
                      .
                     /.\\
                     |.|
                     |.|
                     |.|
                     |.|   ,'`.
                     |.|  ;\\  /:
                     |.| /  \\/  \\
                     |.|<.<_\\/_>,>
                     |.| \\`.::,'/
                     |.|,'.'||'/.
                  ,-'|.|.`.____,'`.
                ,' .`|.| `.____,;/ \\
               ,'=-.`|.|\\ .   \\ |,':
              /_   :)|.|.`.___:,:,'|.
             (  `-:;\\|.|.`.)  |.`-':,\\
             /.   /  ;.:--'   |    | ,`.
            / _>-'._.'-'.     |.   |' / )._
           :.'    ((.__;/     |    |._ /__ `.___
           `.>._.-' |)=(      |.   ;  '--.._,`-.`.
                    ',--'`-._ | _,:          `='`'
                    /_`-. `..`:'/_.\\
                   :__``--..\\\\_/_..:
                   |  ``--..,:;\\__.|
                   |`--..__/:;  :__|
                   `._____:-;_,':__;
                    |:'    /::'  `|
                    |,---.:  :,-'`;
                    : __  )  ;__,'\\
                    \\' ,`/   \\__  :
                    :. |,:   :  `./
                    | `| |   |   |:
                    |  | |   |   ||
                    |  | |   |   ||
                    |  | |   '   ||
                    |  : |    \\  ||
                    |  ; :    :  ||
                    | / ,;    |\\,'`.
                    ;-.(,'    '-._,-`.
                  ,'-.//          `--'
                  `---'
        """)


        print("\nYes indeed you're right! Let's go!\n")
        print("\nYou find your way to the armorer and get yourself a hefty set of armor that will surely surive the flames and punches from the dragon! \n")
        break;

    elif Option5=="SCHOOL":
        print("""
              __...--~~~~~-._   _.-~~~~~--...__
            //               `V'               \\\\
           //                 |                 \\\\
          //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\
         //__.....----~~~~._\\ | /_.~~~~----.....__\\\\
        ====================\\\\|//====================
                            `---`
        """)
        print("\nNo, I mean yes but no, you may need it but this hero I know for a fact doesn't!\n")

    elif Option5=="FORTUNE TELLER":
        print("""
                             .---.
                           .'_..._'.
                          .''_   _''.
                         .' :  '  : '.
                        .'_.-'_~_'-._'.
                       .'(     '     )'.
                      .'  \\ \\     / /  '.
                     .'    \\ \\   / /    '.
               ____________'''` '```____________
              /              .''.               \\
             /              (  ` )               \\
            /               .'..'.                \\
           /                '----'                 \\
          /_________________________________________\\
            \\  /'--'                       '--'\\  /
             ||                                 ||
             ||                                 ||
            _||_                               _||_
            '--'                               '--'
        """)


        print("\nI sense you dead in the future...\n")

    elif Option5=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option5=="STAMINA":
        print ("Your stamine is at "+STAMINA)

Option6="none"

while Option6 != "Y":
    Option6=input("\nAre you ready to fight the dragon?! [Y/N]\n\n").upper()
    print("--------------------------------------------")

    if Option6=="Y":
        print("\nGOOD THAT IS WHAT I LIKE TO HEAR!\n")
        print("\nLET'S GO KILL THAT BEAST!\n")
        break;

    elif Option6=="N":
        print("\nNo, no, no, no we've come too far to give up now!\n")

    elif Option6=="HEALTH":
        print ("Your health is at "+HEALTH)
    elif Option6=="STAMINA":
        print ("Your stamine is at "+STAMINA)

Option7="none"
Option8 = "none"

print("""                _ ___                /^^\\ /^\\  /^^\\_
    _          _@)@) \\            ,,/ '` ~ `'~~ ', `\\.
  _/o\\_ _ _ _/~`.`...'~\\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\\_
( ' _' _ '_` _  '  .    , `\\_/ .' ..' '  `  `   `..  `,   \\_
 ~V~ V~ V~ V~ ~\\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \\_
  _/\\ /\\ /\\ /\\_/, . ' ,   `_/~\\_ .' .,. ,, , _/~\\_ `. `. '.,  \\_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \\_ '      `_/ ::: \\_ `.,' . ',  \\_
  \\ ' `_  '`_    _    ',/ _::_::_ \\ _    _/ _::_::_ \\   `.,'.,`., \\-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \\(_)(_)(_)/  `~~' \\(_)(_)(_)/ ~'`\\_.._,._,'_;_;_;_;_;""")

if Option3=="RUSTIC TAVERN":
    print("\nYou return North to fight the dragon and you came prepared but because you went to the Rustic Tavern you now start with 75 HEALTH.\n")
    while Option7 != "ATTACK" or "DEFEND":
        Option7=input("\nThe dragon strikes! Do you wish to fight back or defend? [Attack/Defend]\n").upper()
        print("--------------------------------------------")


        if Option7=="DEFEND":
            HEALTH = "25"
            print("\nYou block the dragons attack but lost 25 HEALTH in the process!\n")

        elif Option7=="ATTACK":
            print("\nThe dragon is much larger in size than you and has the advantage of strength, this foolish attack will hurt you dearly and does 75 Damage and put your HEALTH to 0, This unfortunatly is the end of you.\n")
            print("\nYou die\n")
            print("""\n
                         ;::::;
                       ;::::; :;
                     ;:::::'   :;
                    ;:::::;     ;.
                   ,:::::'       ;           OOO\\
                   ::::::;       ;          OOOOO\\
                   ;:::::;       ;         OOOOOOOO
                  ,;::::::;     ;'         / OOOOOOO
                ;:::::::::`. ,,,;.        /  / DOOOOOO
              .';:::::::::::::::::;,     /  /     DOOOO
             ,::::::;::::::;;;;::::;,   /  /        DOOO
            ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
            :`:::::::`;::::::;;::: ;::\#  /            DOOO
            ::`:::::::`;:::::::: ;::::\# /              DOO
            `:`:::::::`;:::::: ;::::::\#/               DOO
             :::`:::::::`;; ;:::::::::\#\#                OO
             ::::`:::::::`;::::::::;:::\#                OO
             `:::::`::::::::::::;'`:;::\#                O
              `:::::`::::::::;' /  / `:\#
               ::::::`:::::;'  /  /   `\#\n""")
            sys.exit()

        elif Option7=="HEALTH":
            print ("Your health is at "+HEALTH)
        elif Option7=="STAMINA":
            print ("Your stamine is at "+STAMINA)


        while Option8 !="Y":
            Option8=input("\nThe dragon is staggerd by your defense! Do you wish to take this oppertunity to strike back! [Y/N]\n").upper()
            print("--------------------------------------------")
            if Option8=="Y":
                print("You hurt the dragon by stabbing him in the back of his leg, causing him to bleed severly and weakening him, you run away from him at his point trying to make him tired until the dragon bleeds out.\n YOU WON!\n CONGRATULATIONS!"+name.upper()+"!")
                print("""
                   _                             .-.
                  / )  .-.    ___          __   (   )
                 ( (  (   ) .'___)        (__'-._) (
                  \\ '._) (,'.'               '.     '-.
                   '.      /  "\\               '    -. '.
                     )    /   \\ \\   .-.   ,'.   )  (  ',_)    _
                   .'    (     \\ \\ (   \\ . .' .'    )    .-. ( \\
                  (  .''. '.    \\ \\|  .' .' ,',--, /    (   ) ) )
                   \\ \\   ', :    \\    .-'  ( (  ( (     _) (,' /
                    \\ \\   : :    )  / _     ' .  \\ \\  ,'      /
                  ,' ,'   : ;   /  /,' '.   /.'  / / ( (\\    (
                  '.'      "   (    .-'. \\       ''   \\_)\\    \\
                                \\  |    \\ \\__             )    )
                              ___\\ |     \\___;           /  , /
                             /  ___)                    (  ( (
                             '.'                         ) ;) ;
                                                        (_/(_/
                """)


                sys.exit()

            elif Option8=="N":
                print("\nYou flinched and that will come to pay dearly, the dragon strikes back with twice the anger and you die as he sets you on fire with his breath\n")
                print("\nYou die\n")
                print("""\n
                             ;::::;
                           ;::::; :;
                         ;:::::'   :;
                        ;:::::;     ;.
                       ,:::::'       ;           OOO\\
                       ::::::;       ;          OOOOO\\
                       ;:::::;       ;         OOOOOOOO
                      ,;::::::;     ;'         / OOOOOOO
                    ;:::::::::`. ,,,;.        /  / DOOOOOO
                  .';:::::::::::::::::;,     /  /     DOOOO
                 ,::::::;::::::;;;;::::;,   /  /        DOOO
                ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
                :`:::::::`;::::::;;::: ;::\#  /            DOOO
                ::`:::::::`;:::::::: ;::::\# /              DOO
                `:`:::::::`;:::::: ;::::::\#/               DOO
                 :::`:::::::`;; ;:::::::::\#\#                OO
                 ::::`:::::::`;::::::::;:::\#                OO
                 `:::::`::::::::::::;'`:;::\#                O
                  `:::::`::::::::;' /  / `:\#
                   ::::::`:::::;'  /  /   `\#\n""")
                sys.exit()

            elif Option8=="HEALTH":
                print ("Your health is at "+HEALTH)
            elif Option8=="STAMINA":
                print ("Your stamine is at "+STAMINA)


if Option3=="CROSSROADS INN":
    print("\nYou return North to fight the dragon and you came prepared.\n")
    while Option7 != "ATTACK" or "DEFEND":
        Option7=input("\nThe dragon strikes! Do you wish to fight back or defend? [Attack/Defend]\n").upper()
        print("--------------------------------------------")


        if Option7=="DEFEND":
            print("\nYou block the dragons attack but lost 25 HEALTH in the process!\n")
            break;

        elif Option7=="ATTACK":
            print("\nThe dragon is much larger in size than you and has the advantage of strength, this foolish attack will hurt you dearly and does 75 Damage and put your HEALTH to 25, But it has made an opening in the dragons defense and allows you to slit his throat and finish him off!.\n")
            print("\nYOU WON!\n")
            print("\nCONGRATULATIONS "+name.upper()+"!")
            print("""
               _                             .-.
              / )  .-.    ___          __   (   )
             ( (  (   ) .'___)        (__'-._) (
              \\ '._) (,'.'               '.     '-.
               '.      /  "\\               '    -. '.
                 )    /   \\ \\   .-.   ,'.   )  (  ',_)    _
               .'    (     \\ \\ (   \\ . .' .'    )    .-. ( \\
              (  .''. '.    \\ \\|  .' .' ,',--, /    (   ) ) )
               \\ \\   ', :    \\    .-'  ( (  ( (     _) (,' /
                \\ \\   : :    )  / _     ' .  \\ \\  ,'      /
              ,' ,'   : ;   /  /,' '.   /.'  / / ( (\\    (
              '.'      "   (    .-'. \\       ''   \\_)\\    \\
                            \\  |    \\ \\__             )    )
                          ___\\ |     \\___;           /  , /
                         /  ___)                    (  ( (
                         '.'                         ) ;) ;
                                                    (_/(_/
            """)


            sys.exit()

        elif Option7=="HEALTH":
            print ("Your health is at "+HEALTH)
        elif Option7=="STAMINA":
            print ("Your stamine is at "+STAMINA)


    if Option7 =="DEFEND":
        while Option8 !="Y":
            Option8=input("\nThe dragon is staggerd by your defense! Do you wish to take this oppertunity to strike back! [Y/N]\n").upper()
            print("--------------------------------------------")

            if Option8=="Y":
                print("You hurt the dragon by stabbing him in the back of his leg, causing him to bleed severly and weakening him, you run away from him at his point trying to make him tired until the dragon bleeds out.\n YOU WON!\n CONGRATULATIONS "+name.upper()+"!")
                print("""
                   _                             .-.
                  / )  .-.    ___          __   (   )
                 ( (  (   ) .'___)        (__'-._) (
                  \\ '._) (,'.'               '.     '-.
                   '.      /  "\\               '    -. '.
                     )    /   \\ \\   .-.   ,'.   )  (  ',_)    _
                   .'    (     \\ \\ (   \\ . .' .'    )    .-. ( \\
                  (  .''. '.    \\ \\|  .' .' ,',--, /    (   ) ) )
                   \\ \\   ', :    \\    .-'  ( (  ( (     _) (,' /
                    \\ \\   : :    )  / _     ' .  \\ \\  ,'      /
                  ,' ,'   : ;   /  /,' '.   /.'  / / ( (\\    (
                  '.'      "   (    .-'. \\       ''   \\_)\\    \\
                                \\  |    \\ \\__             )    )
                              ___\\ |     \\___;           /  , /
                             /  ___)                    (  ( (
                             '.'                         ) ;) ;
                                                        (_/(_/
                """)


                sys.exit()

            elif Option8=="N":
                print("\nYou flinched and that will come to pay dearly, the dragon strikes back with twice the anger and you die as he sets you on fire with his breath\n")
                print("\nYou die\n")
                print("""\n
                             ;::::;
                           ;::::; :;
                         ;:::::'   :;
                        ;:::::;     ;.
                       ,:::::'       ;           OOO\\
                       ::::::;       ;          OOOOO\\ bc b43
                       ;:::::;       ;         OOOOOOOO
                      ,;::::::;     ;'         / OOOOOOO
                    ;:::::::::`. ,,,;.        /  / DOOOOOO
                  .';:::::::::::::::::;,     /  /     DOOOO
                 ,::::::;::::::;;;;::::;,   /  /        DOOO
                ;`::::::`'::::::;;;::::: ,\#/  /          DOOO
                :`:::::::`;::::::;;::: ;::\#  /            DOOO
                ::`:::::::`;:::::::: ;::::\# /              DOO
                `:`:::::::`;:::::: ;::::::\#/               DOO
                 :::`:::::::`;; ;:::::::::\#\#                OO
                 ::::`:::::::`;::::::::;:::\#                OO
                 `:::::`::::::::::::;'`:;::\#                O
                  `:::::`::::::::;' /  / `:\#
                   ::::::`:::::;'  /  /   `\#\n""")
                sys.exit()

            elif Option4=="HEALTH":
                print ("Your health is at "+HEALTH)
            elif Option4=="STAMINA":
                print ("Your stamine is at "+STAMINA)
