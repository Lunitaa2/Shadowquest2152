import os
from player import Player
from monster import Monster
from fight_system import FightSystem



# Monsters Creation
goblin_monster = Monster("Goblin", 50, 8, 3)

# System instances
fight_sys = FightSystem()
#quest
#shop
#dungeon

# System definitions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

print("Choose where do you wish to go!")

