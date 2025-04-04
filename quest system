import random

class Character:
    def __init__(self, name, health_points, combat_strength):
        self.name = name
        self.health_points = health_points
        self.combat_strength = combat_strength

    def attack(self, target):
        damage = random.randint(1, self.combat_strength)
        target.health_points -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health_points > 0

class Hero(Character):
    def __init__(self, name, health_points, combat_strength, coins=0, skills=None, level=1):
        super().__init__(name, health_points, combat_strength)
        self.coins = coins
        self.skills = skills if skills else ["Basic Attack"]
        self.level = level
        self.inventory = []
        self.enemies_defeated = 0

    def earn_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins! Current coins: {self.coins}")

    def buy_item(self, item, cost):
        if self.coins >= cost:
            self.coins -= cost
            self.inventory.append(item)
            print(f"{self.name} bought {item}!")
        else:
            print("Not enough coins!")

    def level_up(self):
        self.level += 1
        self.combat_strength += 2
        self.health_points += 5
        print(f"{self.name} leveled up to level {self.level}!")

    def defeat_enemy(self):
        self.enemies_defeated += 1
        if self.enemies_defeated % 3 == 0:  # Unlock a new skill every 3 enemies defeated
            new_skill = f"Skill {self.level}"
            self.skills.append(new_skill)
            print(f"{self.name} unlocked a new skill: {new_skill}!")

class Monster(Character):
    def __init__(self, name, health_points, combat_strength, reward_coins):
        super().__init__(name, health_points, combat_strength)
        self.reward_coins = reward_coins

class Quest:
    def __init__(self, description, reward_coins, required_enemies):
        self.description = description
        self.reward_coins = reward_coins
        self.required_enemies = required_enemies
        self.completed = False

    def check_completion(self, hero):
        if hero.enemies_defeated >= self.required_enemies and not self.completed:
            hero.earn_coins(self.reward_coins)
            self.completed = True
            print(f"Quest completed: {self.description}! Reward: {self.reward_coins} coins")

class Game:
    def __init__(self):
        self.hero = Hero("Knight", 100, 10)
        self.monsters = [Monster("Goblin", 30, 5, 10), Monster("Orc", 50, 8, 20)]
        self.daylight_mode = "Day"
        self.quests = [Quest("Defeat 5 enemies", 50, 5)]

    def toggle_daylight_mode(self):
        self.daylight_mode = "Night" if self.daylight_mode == "Day" else "Day"
        print(f"Switched to {self.daylight_mode} mode.")

    def battle(self, monster):
        print(f"A wild {monster.name} appeared!")
        while self.hero.is_alive() and monster.is_alive():
            self.hero.attack(monster)
            if monster.is_alive():
                monster.attack(self.hero)

        if self.hero.is_alive():
            print(f"{self.hero.name} defeated {monster.name}!")
            self.hero.earn_coins(monster.reward_coins)
            self.hero.defeat_enemy()
            self.hero.level_up()
            for quest in self.quests:
                quest.check_completion(self.hero)
        else:
            print("Game Over!")

# Example Usage
game = Game()
game.toggle_daylight_mode()
game.battle(game.monsters[0])
