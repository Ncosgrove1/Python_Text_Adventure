import random # Randomized encounters

def enemy_encounter(room_enemies):
    """
    Handles a randomized enemy encounter.
    Returns True if the player survives, False if they lose.
    """
    enemy = random.choice(room_enemies)
    print(f"\n!!! WARNING: A {enemy} lunges from the shadows !!!")
    
    # Input Explanation
    print("Choices: [fight], [run]")
    choice = input("What do you do? ").lower().strip()
    
    # Combat logic
    if choice == "fight":
        # 60% chance to win a fight
        if random.random() < 0.60:
            print(f"Victory! You defeated the {enemy}.")
            return True
        else:
            print(f"The {enemy} was too fast. You have been defeated.")
            return False
    elif choice == "run":
        print("You narrowly escaped back to the center of the room!")
        return True
    else:
        print(f"Your hesitation cost you. The {enemy} strikes!")
        return False

def start_game():
    """
    Main function to initialize and run the text adventure game.
    """
    # World layout
    world_map = {
        "hallway": {
            "desc": "A dim hallway. An IRON DOOR is north, a STAIRCASE is down, and a small WOODEN DOOR is east.",
            "enemies": ["Shadow Rat", "Giant Spider"]
        },
        "dungeon": {
            "desc": "A cold and damp pit. A shiny KEY glints on the muddy floor. A STAIRCASE is up",
            "enemies": ["Slime Blob", "Skeleton"]
        },
        "armory": {
            "desc": "Racks of rusted swords line the walls. A golden SHIELD rests in the corner.",
            "enemies": ["Animated Armor", "Ghost Knight"]
        },
        "bedroom": {
            "desc": "A cramped, and dusty bedroom. It's a DEAD END room filled with broken shelves.",
            "enemies": ["Angry Bat"]
        }
    }

    inventory = []
    current_room = "hallway"
    game_running = True

    print("--- WELCOME TO THE CRYPT ESCAPE ---")
    print("Commands: [north, south, east, west, down, up], 'look', 'take [item]', 'inventory', 'quit'")

    while game_running:
        print(f"\nLocation: {current_room.upper()}")
        print(world_map[current_room]["desc"])
        
        # Randomized Encounter Logic: 25% chance per turn
        if random.random() < 0.25:
            survived = enemy_encounter(world_map[current_room]["enemies"])
            if not survived:
                print("GAME OVER")
                break

        # User Input
        user_input = input("\nAction: ").lower().strip().split()
        if not user_input: continue
        
        # Split input into action (verb) and target (noun)
        action = user_input[0]
        target = user_input[1] if len(user_input) > 1 else None

        # Potential Input Logic
        # (quit, look, inventory, north, south, east, west, up, down, take key, take shield)
        
        if action == "quit":
            game_running = False
        elif action == "look":
            print("You search the room but find nothing new.")
        elif action == "inventory":
            print(f"Items: {inventory if inventory else 'None'}")
        
        # Navigation logic using if/else
        elif action in ["north", "south", "east", "west", "up", "down"]:
            if action == "north" and current_room == "hallway":
                if "key" in inventory:
                    print("You unlock the door!")
                    current_room = "armory"
                else: print("Locked.")
            elif action == "east" and current_room == "hallway":
                current_room = "bedroom"
            elif action == "west" and current_room == "bedroom":
                current_room = "hallway"
            elif action == "down" and current_room == "hallway": 
                current_room = "dungeon"
            elif action == "up" and current_room == "dungeon": 
                current_room = "hallway"
            elif action == "south" and current_room == "armory": 
                current_room = "hallway"
            else: 
                print("You can't go that way. It might be a wall or a dead end.")
        
        # Interaction logic
        elif action == "take":
            if target == "key" and current_room == "dungeon":
                if "key" not in inventory:
                    inventory.append("key")
                    print("Key added to inventory.")
                else: print("You already have the key.")
            elif target == "shield" and current_room == "armory":
                print("You found the golden shield! YOU ESCAPED THE CRYPT!")
                game_running = False
            else: print("Nothing here to take.")
        else:
            print("Unknown command. Try a direction or 'look'.")

if __name__ == "__main__":
    start_game()
