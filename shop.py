class Shop:
    def _init_(self):
        self.items = {
            "Shotgun": 60,
            "Akm": 40,
            "Scar-L": 23,
            "Sniper": 90,
            "Med Kit": 23,
            "Energy Drink": 5,
            "Pain Killer": 5
        }

    def display_items(self):
        print("This is the shop... What would you like to buy?")
        for item, price in self.items.items():
            print(f"- {item}: {price} coins")

    def buy(self, player, item_name):
        if item_name not in self.items:
            print("Error- Unavailable")
            return
        
        cost = self.items[item_name]
        if player.coins < cost:
            print("You don't have enough coins. Broke")
            return
        
        player.coins -= cost
        player.inventory.append(item_name)
        print(f"You purchased {item_name}")

    def is_open(self, time_of_day):
        return time_of_day != "it is night time"