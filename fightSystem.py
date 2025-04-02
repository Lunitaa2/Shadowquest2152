class FightSystem:
    def start_fight(self, player, monster):
        print(f"Fight started between {player.name} and {monster.name}")
        while player.health > 0 and monster.health > 0:
            player.attack_monster(monster)
            if monster.health <= 0:
                self.calculate_rewards(player, monster)
                break
            monster.attack_player(player)

    def calculate_rewards(self, player, monster):
        print(f"{monster.name} defeated!")
        player.add_coins(10)
        player.exp += 10
        if player.exp >= player.level * 10:
            player.exp = 0
            player.level_up()
