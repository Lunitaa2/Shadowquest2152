class Monster:
    def __init__(self, name, health, attack, defense, is_night=False):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_night = is_night
        if is_night:
            self.scale_stats_for_night()

    def take_damage(self, amount):
        damage = max(amount - self.defense, 0)
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def attack_player(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.take_damage(self.attack)

    #def scale_stats_for_night(self):
    #    self.attack += 3
    #   self.defense += 2
    #   self.health += 20