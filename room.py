import sys


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []
        self.locked = False
        self.puzzle = None

    def add_paths(self, paths):
        self.paths.update(paths)

    def go(self, direction):
        if direction in self.paths:
            if self.paths[direction].locked:
                return "locked"
            return self.paths[direction]
        else:
            return None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_puzzle(self, puzzle):
        self.puzzle = puzzle

    def solve_puzzle(self, answer):
        if self.puzzle and self.puzzle.check_answer(answer):
            self.puzzle = None
            return True
        return False


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, answer):
        return self.answer.lower() == answer.lower()


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms['entrance']
        self.inventory = []

    def create_rooms(self):
        entrance = Room("Entrance", "You are at the entrance of a dark cave.")
        hallway = Room("Hallway", "You are in a narrow hallway. It's damp and dark.")
        treasure_room = Room("Treasure Room", "You've found the treasure room! Shiny gold everywhere.")
        trap_room = Room("Trap Room", "It's a trap room! Watch out for the spikes.")
        kitchen = Room("Kitchen", "You are in a kitchen. It smells like rotten food.")
        library = Room("Library", "You are in a library. There are many old books here.")
        garden = Room("Garden", "You are in a beautiful garden. Flowers are blooming.")

        # Add items to rooms
        key = Item("Key", "A small rusty key.")
        treasure_map = Item("Treasure Map", "A map showing the way to the treasure room.")

        kitchen.add_item(key)
        library.add_item(treasure_map)

        # Lock the treasure room
        treasure_room.locked = True

        # Add a puzzle to the library
        puzzle = Puzzle("What has keys but can't open locks?", "Piano")
        library.add_puzzle(puzzle)

        # Define room connections
        entrance.add_paths({'north': hallway})
        hallway.add_paths(
            {'south': entrance, 'east': treasure_room, 'west': trap_room, 'north': kitchen, 'south': library})
        treasure_room.add_paths({'west': hallway})
        trap_room.add_paths({'east': hallway})
        kitchen.add_paths({'south': hallway})
        library.add_paths({'north': hallway, 'west': garden})
        garden.add_paths({'east': library})

        return {
            'entrance': entrance,
            'hallway': hallway,
            'treasure_room': treasure_room,
            'trap_room': trap_room,
            'kitchen': kitchen,
            'library': library,
            'garden': garden,
        }

    def play(self):
        print("Welcome to the Adventure Game!")
        print("Type 'quit' to exit the game.")

        while True:
            print("\n" + self.current_room.name)
            print(self.current_room.description)
            if self.current_room.items:
                print("You see the following items:")
                for item in self.current_room.items:
                    print(f"- {item.name}: {item.description}")

            if self.current_room.puzzle:
                print("Puzzle: " + self.current_room.puzzle.question)

            command = input("> ").strip().lower()

            if command == 'quit':
                print("Thanks for playing!")
                break

            if command.startswith('take '):
                item_name = command.split(' ', 1)[1]
                item = next((i for i in self.current_room.items if i.name.lower() == item_name), None)
                if item:
                    self.current_room.remove_item(item)
                    self.inventory.append(item)
                    print(f"You have taken the {item.name}.")
                else:
                    print("There is no such item here.")
                continue

            if command.startswith('use '):
                item_name = command.split(' ', 1)[1]
                item = next((i for i in self.inventory if i.name.lower() == item_name), None)
                if item:
                    if item.name.lower() == 'key' and self.current_room == self.rooms[
                        'hallway'] and 'east' in self.current_room.paths:
                        self.rooms['treasure_room'].locked = False
                        self.inventory.remove(item)
                        print("You have unlocked the door to the treasure room!")
                    else:
                        print("You can't use that here.")
                else:
                    print("You don't have such item.")
                continue

            if command.startswith('answer '):
                answer = command.split(' ', 1)[1]
                if self.current_room.solve_puzzle(answer):
                    print("Correct! The puzzle has been solved.")
                else:
                    print("Incorrect answer.")
                continue

            next_room = self.current_room.go(command)
            if next_room:
                if next_room == "locked":
                    print("The door is locked. You need a key to open it.")
                else:
                    self.current_room = next_room
            else:
                print("You can't go that way.")


if __name__ == "__main__":
    game = Game()
    game.play()
