class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.coins = 0
        self.skills = ["Basic Strike"]
        self.inventory = []

    def attack_monster(self, monster):
        print(f"{self.name} attacks {monster.name}!")
        monster.take_damage(self.attack)

    def take_damage(self, amount):
        damage = max(amount - self.defense, 0)
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def level_up(self):
        self.level += 1
        self.attack += 2
        self.defense += 1
        self.health += 20
        print(f"{self.name} leveled up! Now at level {self.level}")

    def learn_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"{self.name} learned a new skill: {skill}")

    def use_item(self, item):
        print(f"{self.name} uses {item}")
        # To be implemented

    def add_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins. Total: {self.coins}")
