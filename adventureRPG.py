import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_attack_power = attack_power
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def get_status(self):
        return f"{self.name}: {self.health} HP"


class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
        self.inventory = []
        self.gold = 0
        self.experience = 0
        self.level = 1
        self.equipped_item = None
        self.allies = []

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"You have picked up a {item.name}: {item.description}")

    def equip_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower() and isinstance(item, Weapon):
                self.equipped_item = item
                self.attack_power = self.base_attack_power + item.attack_boost
                print(f"You have equipped the {item.name}. Your attack power is now {self.attack_power}.")
                return
        print(f"Item '{item_name}' not found or is not a weapon in your inventory.")

    def gain_experience(self, xp):
        self.experience += xp
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health = 100
        self.base_attack_power += 5
        self.experience = 0
        print(
            f"Congratulations! You have leveled up to level {self.level}. Your base attack power is now {self.base_attack_power}.")


class Monster(Character):
    def __init__(self, name, health, attack_power, xp_reward, loot=None):
        super().__init__(name, health, attack_power)
        self.xp_reward = xp_reward
        self.loot = loot


class Ally(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, attack_boost):
        super().__init__(name, description)
        self.attack_boost = attack_boost

class Shop:
    def __init__(self):
        self.items = {
            "Health Potion": {"price": 20, "description": "Restores 20 health points."},
            "Attack Boost": {"price": 30, "description": "Increases your attack power by 5."}
        }

    def display_items(self):
        print("Welcome to the shop!")
        print("Available items:")
        for item, details in self.items.items():
            print(f"{item}: {details['description']} - Price: {details['price']} gold")

    def purchase_item(self, player, item_name):
        if item_name in self.items:
            item_details = self.items[item_name]
            if player.gold >= item_details['price']:
                player.gold -= item_details['price']
                player.pick_item(Item(name=item_name, description=item_details['description']))
                print(f"You purchased {item_name}.")
            else:
                print("You don't have enough gold to purchase this item.")
        else:
            print("Item not found in the shop.")
class Game:
    def __init__(self):
        self.player = Player(name="Hero")
        self.rooms = self.create_rooms()
        self.current_room = self.rooms['start']
        self.defeated_enemies = 0
        self.shop = Shop()

    def create_rooms(self):
        start = {
            'description': "You are at the starting point of your adventure.",
            'monster': None,
            'item': None,
            'paths': {'north': 'forest', 'east': 'cave'}
        }
        forest = {
            'description': "You are in a dense forest. The atmosphere is eerie.",
            'monster': Monster(name="Goblin", health=30, attack_power=5, xp_reward=20,
                               loot=Item(name="Gold Coin", description="A shiny gold coin worth 10 gold.")),
            'item': None,
            'paths': {'south': 'start', 'north': 'lake', 'east': 'village', 'west': 'dark_forest'}
        }
        cave = {
            'description': "You have entered a dark cave. It's damp and cold.",
            'monster': Monster(name="Troll", health=50, attack_power=8, xp_reward=30, loot=Weapon(name="Silver Sword",
                                                                                                  description="A sword that increases your attack power by 5.",
                                                                                                  attack_boost=5)),
            'item': None,
            'paths': {'west': 'start', 'north': 'underground_lake'}
        }
        lake = {
            'description': "You are at the edge of a serene lake.",
            'monster': Monster(name="Water Serpent", health=40, attack_power=7, xp_reward=25,
                               loot=Item(name="Pearl", description="A precious pearl worth 20 gold.")),
            'item': Weapon(name="Old Gun",
                           description="An old but functional gun that increases your attack power by 10.",
                           attack_boost=10),
            'paths': {'south': 'forest'}
        }
        village = {
            'description': "You have reached a small village. Friendly faces greet you.",
            'monster': None,
            'item': None,
            'paths': {'west': 'forest', 'east': 'mountain', 'north': 'plains'}
        }
        mountain = {
            'description': "You are climbing a steep mountain. The air is thin and cold.",
            'monster': Monster(name="Dragon", health=80, attack_power=12, xp_reward=50,
                               loot=Weapon(name="Dragon Slayer",
                                           description="A mighty sword that increases your attack power by 20.",
                                           attack_boost=20)),
            'item': None,
            'paths': {'west': 'village', 'north': 'peak'}
        }
        dark_forest = {
            'description': "You are in a dark and gloomy forest. Strange noises surround you.",
            'monster': Monster(name="Dark Elf", health=35, attack_power=6, xp_reward=25, loot=Item(name="Mystic Amulet",
                                                                                                   description="An amulet that radiates a strange energy.")),
            'item': None,
            'paths': {'east': 'forest', 'north': 'abandoned_castle'}
        }
        plains = {
            'description': "You are in open plains. The grass is tall and the sky is clear.",
            'monster': Monster(name="Wild Boar", health=25, attack_power=4, xp_reward=15,
                               loot=Item(name="Boar Tusk", description="A sharp tusk from a wild boar.")),
            'item': None,
            'paths': {'south': 'village'}
        }
        underground_lake = {
            'description': "You have found an underground lake. The water is crystal clear.",
            'monster': Monster(name="Cave Guardian", health=45, attack_power=9, xp_reward=30,
                               loot=Item(name="Guardian's Shield",
                                         description="A shield that can block powerful attacks.")),
            'item': None,
            'paths': {'south': 'cave'}
        }
        abandoned_castle = {
            'description': "You have reached an abandoned castle. It looks haunted.",
            'monster': Monster(name="Ghost", health=20, attack_power=5, xp_reward=20,
                               loot=Item(name="Ancient Coin", description="An old coin that might be valuable.")),
            'item': None,
            'paths': {'south': 'dark_forest'}
        }
        peak = {
            'description': "You have reached the peak of the mountain. The view is breathtaking.",
            'monster': Monster(name="Ice Golem", health=60, attack_power=10, xp_reward=40,
                               loot=Item(name="Frost Gem", description="A gem that is cold to the touch.")),
            'item': None,
            'paths': {'south': 'mountain'}
        }

        return {
            'start': start,
            'forest': forest,
            'cave': cave,
            'lake': lake,
            'village': village,
            'mountain': mountain,
            'dark_forest': dark_forest,
            'plains': plains,
            'underground_lake': underground_lake,
            'abandoned_castle': abandoned_castle,
            'peak': peak
        }

    def play(self):
        print("Welcome to the Adventure RPG Game!")
        print("Type 'quit' to exit the game.")

        while True:
            print(f"\nLocation: {self.current_room['description']}")
            if self.current_room['monster'] and self.current_room['monster'].is_alive():
                print(f"A wild {self.current_room['monster'].name} appears!")
                self.battle(self.current_room['monster'])
                if not self.player.is_alive():
                    print("You have been defeated. Game over.")
                    break
                else:
                    self.collect_loot(self.current_room['monster'])
                    self.current_room['monster'] = None

            if self.current_room['item']:
                print(f"You see a {self.current_room['item'].name}: {self.current_room['item'].description}")
                self.pick_up_item()

            if self.current_room['description'].find("village") != -1 and not self.player.allies:
                print("You meet a friend who joins you in your adventure!")
                new_ally = Ally(name="Friend", health=80, attack_power=7)
                self.player.allies.append(new_ally)
                print(f"{new_ally.name} has joined your party!")

            if self.current_room['monster'] and not self.current_room['monster'].is_alive():
                self.defeated_enemies += 1
                if self.check_victory():
                    break

            command = input("> ").strip().lower()
            if command == 'quit':
                print("Thanks for playing!")
                break
            elif command.startswith('equip '):
                item_name = command[6:]
                self.player.equip_item(item_name)
            elif command in self.current_room['paths']:
                self.current_room = self.rooms[self.current_room['paths'][command]]
            else:
                print("Invalid command. Try again.")

            if self.current_room['item'] and isinstance(self.current_room['item'], Item):
                print(f"You found a {self.current_room['item'].name}.")
                self.pick_up_item()

            if self.current_room['description'].find("village") != -1:
                print("You are in the village. You can visit the shop.")
                self.visit_shop()
        

    def pick_up_item(self):
        while True:
            choice = input("Do you want to pick up the item? (yes/no): ").strip().lower()
            if choice == 'yes':
                self.player.pick_item(self.current_room['item'])
                self.current_room['item'] = None
                break
            elif choice == 'no':
                break
            else:
                print("Invalid choice. Please type 'yes' or 'no'.")

    def collect_loot(self, monster):
        if monster.loot:
            self.player.pick_item(monster.loot)
            if isinstance(monster.loot, Item) and monster.loot.name == "Gold Coin":
                self.player.gold += 10
                print(f"You now have {self.player.gold} gold.")
        self.player.gain_experience(monster.xp_reward)
        print(f"You have gained {monster.xp_reward} experience points.")

    def visit_shop(self):
        choice = input("Do you want to visit the shop? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.shop.display_items()
            while True:
                purchase_choice = input(
                    "Enter the name of the item you want to purchase (type 'exit' to leave): ").strip()
                if purchase_choice == 'exit':
                    break
                else:
                    self.shop.purchase_item(self.player, purchase_choice)
        else:
            print("You decide not to visit the shop.")

    def battle(self, monster):
        while monster.is_alive() and self.player.is_alive():
            print(f"\n{self.player.get_status()} vs {monster.get_status()}")
            for ally in self.player.allies:
                print(f"{ally.get_status()}")

            action = input("Do you want to 'attack' or 'run'? ").strip().lower()
            if action == 'attack':
                damage = self.player.attack(monster)
                print(f"You attack the {monster.name} for {damage} damage.")
                if not monster.is_alive():
                    print(f"You have defeated the {monster.name}!")
                    break
                for ally in self.player.allies:
                    if monster.is_alive():
                        damage = ally.attack(monster)
                        print(f"{ally.name} attacks the {monster.name} for {damage} damage.")
                        if not monster.is_alive():
                            print(f"The {monster.name} has been defeated by {ally.name}!")
                            break
                if monster.is_alive():
                    damage = monster.attack(self.player)
                    print(f"The {monster.name} attacks you for {damage} damage.")
                    if not self.player.is_alive():
                        print("You have been defeated.")
                        break
                    for ally in self.player.allies:
                        if monster.is_alive():
                            damage = monster.attack(ally)
                            print(f"The {monster.name} attacks {ally.name} for {damage} damage.")
                            if not ally.is_alive():
                                print(f"{ally.name} has been defeated.")
                                self.player.allies.remove(ally)
            elif action == 'run':
                print("You run away!")
                break
            else:
                print("Invalid action. Try again.")

    def visit_shop(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.play()
