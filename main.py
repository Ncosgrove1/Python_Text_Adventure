import random # Randomized encounters

def enemy_encounter(room_enemies):
    """
    Function to handle a randomized enemy encounter.
    Returns True if the player survives, False if they lose.
    """
    enemy = random.choice(room_enemies)
    print(f"\n!!! WARNING: A {enemy} lunges from the shadows !!!")
    
    # Combat options
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
        print("You narrowily escaped back to the center of the room!")
        return True
    else:
        print(f"Your hesitation cost you. The {enemy} strikes!")
        return False

def start_game():
    """
    Main function to initialize and run the text adventure game.
    """
    # 1. Variables and Dictionaries: World layout with enemy lists
    world_map = {
        "hallway": {
            "desc": "A dim hallway. A heavy IRON DOOR is north and a STAIRCASE leads down.",
            "enemies": ["Shadow Rat", "Giant Spider"]
        },
        "dungeon": {
            "desc": "Cold and damp. A SHINY KEY glints on the muddy floor.",
            "enemies": ["Slime Blob", "Skeleton"]
        },
        "armory": {
            "desc": "Racks of rusted swords line the walls. A golden SHIELD rests in the corner.",
            "enemies": ["Animated Armor", "Ghost Knight"]
        }
    }

    inventory = []
    current_room = "hallway"
    game_running = True

    print("--- WELCOME TO THE CRYPT ESCAPE ---")
    print("Commands: [north, south, down, up], 'look', 'take [item]', 'inventory', 'quit'")

    while game_running:
        print(f"\nLocation: {current_room.upper()}")
        print(world_map[current_room]["desc"])
        
        # 4. Randomized Encounter Logic: 30% chance per turn
        if random.random() < 0.30:
            survived = enemy_encounter(world_map[current_room]["enemies"])
            if not survived:
                print("GAME OVER")
                break

        # Navigation and interaction
        user_input = input("\nAction: ").lower().strip().split()
        if not user_input: continue
        
        action = user_input[0]
        target = user_input[1] if len(user_input) > 1 else None

        # Potential Input Logic
        if action == "quit":
            game_running = False
        elif action == "look":
            print("You search the room but find nothing new.")
        elif action == "inventory":
            print(f"Items: {inventory if inventory else 'None'}")
        elif action in ["north", "south", "up", "down"]:
            # Movement logic (similar to previous version)
            if action == "north" and current_room == "hallway":
                if "key" in inventory:
                    print("You unlock the door!")
                    current_room = "armory"
                else: print("Locked.")
            elif action == "down" and current_room == "hallway": current_room = "dungeon"
            elif action == "up" and current_room == "dungeon": current_room = "hallway"
            elif action == "south" and current_room == "armory": current_room = "hallway"
            else: print("You can't go that way.")
        elif action == "take":
            if target == "key" and current_room == "dungeon":
                inventory.append("key")
                print("Key added to inventory.")
            elif target == "shield" and current_room == "armory":
                print("You found the shield! YOU ESCAPED THE CRYPT!")
                game_running = False
            else: print("Nothing here to take.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    start_game()