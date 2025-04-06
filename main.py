import os
from player import Player
from monster import Monster
from fight_system import FightSystem
from shop import Shop
from dungeon import Dungeon
from day_night_mode import DayNightMode



# Monsters Creation
goblin_monster = Monster("Goblin", 50, 8, 3)

# System instances
fight_sys = FightSystem()
#quest
#shop
shop=Shop()
#dungeon
dungeon = Dungeon("Dark Dungeon", [goblin_monster])


# System definitions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#where to go...
def game_map():
    while True:
        print("Where would you like to go using the Map?")
        print("1. Dungeon access in night")
        print("3.Shop (This is where you can buy health and guns)")
        print("Exit game")
        choice=input("enter choice:")

        if choice == "1":
            dungeon.enter(player)
        elif choice == "2":
            shop.display_items()
            item = input("What do you want to buy? ")
            shop.buy(player, item)
        elif choice == "3":
            print("Maybe next time or not :)")
            exit()
        else:
            print("Invalid choice, please select again.")


#  === MAIN GAME ===
print("     Welcome to....")
print("""
   ▄████████    ▄█    █▄       ▄████████ ████████▄   ▄██████▄   ▄█     █▄ 
  ███    ███   ███    ███     ███    ███ ███   ▀███ ███    ███ ███     ███
  ███    █▀    ███    ███     ███    ███ ███    ███ ███    ███ ███     ███
  ███         ▄███▄▄▄▄███▄▄   ███    ███ ███    ███ ███    ███ ███     ███
▀███████████ ▀▀███▀▀▀▀███▀  ▀███████████ ███    ███ ███    ███ ███     ███
         ███   ███    ███     ███    ███ ███    ███ ███    ███ ███     ███
   ▄█    ███   ███    ███     ███    ███ ███   ▄███ ███    ███ ███ ▄█▄ ███
 ▄████████▀    ███    █▀      ███    █▀  ████████▀   ▀██████▀   ▀███▀███▀ 
                                                                          
████████▄   ███    █▄     ▄████████    ▄████████     ███                  
███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄              
███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██              
███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀              
███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███                  
███    ███  ███    ███   ███    █▄           ███     ███                  
███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███                  
 ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀                """)


while True:
    start_game = input("\nDo you want to continue? y = yes || x = exit: ").lower()

    if start_game == 'y':
        break
    elif start_game == 'x':
        print("Farewell, brave soul.")
        exit()
    else:
        print("Invalid input. Please type 'y' to start or 'x' to exit.")
   
clear()

# Creation of player
while True:
    player = Player(input("What is your name? "))
    if input(f"Is your name {player.name}? (y/n): ").lower() == "y":
        print("Great! Your journey begins now...")
        break
    else:
        print("Let's try again!")
    
if input("Press any key to continue or \"x\" to exit").lower() == "x":
    exit()

clear()
print('''
                   _     _    _     _
                  [_]___[_]__[_]___[_]
                  [__#__][__I_]__I__#]
                  [_I_#_I__#[__]__#__]
                     [_]_#_]__I_#_]
                     [I_|/ _W_ \|#]
                     [#_||{(")}||_]
                     [_I||{/~\}||_]
                     [__]|/\_/\||#]
                     [_I__I#___]__]
                     [__I_#_I___#_]
                     [#__I____]__I]
      .-.            [__I_#__I__[_]
    __|=|__          [_#_[__#_]__#]
   (_/`-`\_)         [__#_I__[#_I_]
   //\___/\\\\         [_I__]__#_I__]
   <>/   \<>         [#__I__#_]__I]
    \|_._|/          [_I#__I___I_#]    .:.
     <_I_>           [#__I__]_#___]   -=o=-
      |||            [_I__I#__]___]    ':'
jgs  /_|_\         \\\\[__]#___][__#]//, \|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''
)
print("Choose where do you wish to go!")

