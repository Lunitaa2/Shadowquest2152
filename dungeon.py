class Dungeon: 
    def _init_(personal, name, monsters):
        super()._init_(name, ["Fight", "Explore", "Exit"], monsters)

    def enter(personal, player):
        print(f"You have entered the dungeonnn!!!danger {personal.name}!")
        if personal.monsters:
            print("CAREFUL! THERE ARE MONSTERS...")
        personal.show_actions()