def start_game():
    """
    Main function to initialize and run the text adventure game.
    """
    # Variables and Dictionaries: Store game state and world layout
    # world_map uses a dictionary to store room descriptions and exits (lists)

    world_map = {
        "hallway": {
            "desc": "You are in a dim hallway. A heavy IRON DOOR is north and a STAIRCASE leads down.",
            "exits": ["north", "down"]
        },
        "dungeon": {
            "desc": "It's cold and damp. A SHINY KEY glints on the muddy floor.",
            "exits": ["up"]
        },
        "armory": {
            "desc": "Racks of rusted swords line the walls. A golden SHIELD rests in the corner.",
            "exits": ["south"]
        }
    }

    # Player state variables
    inventory = []
    current_room = "hallway"
    game_running = True

    # Input Explanation
    print("--- WELCOME TO THE CRYPT ESCAPE ---")
    print("Commands: [north, south, east, west, up, down], 'look', 'take [item]', 'inventory', 'quit'")

    # Main game loop
    while game_running:
        # Display current status to the user
        print(f"\nLocation: {current_room.upper()}")
        print(world_map[current_room]["desc"])
        
        # Gathering user input and normalizing it to lowercase
        user_input = input("\nWhat would you like to do? ").lower().strip().split()
        
        if not user_input:
            continue
            
        action = user_input[0]
        # Multi-word input handling (e.g., 'take key')
        target = user_input[1] if len(user_input) > 1 else None

        # If/Else Statements: Logic for movement and interaction
        # Potential Inputs (Action count towards 10+ limit): 
        # 1. quit, 2. look, 3. inventory, 4. north, 5. south, 6. down, 7. up, 8. take key, 9. take shield, 10. unknown commands
        
        if action == "quit":
            print("You gave up on your quest. Goodbye!")
            game_running = False

        elif action == "look":
            # Re-describes the current room
            print("You look around carefully...")
            continue

        elif action == "inventory":
            # Shows a list of items currently held
            print(f"Inventory: {inventory if inventory else 'empty'}")

        elif action == "north":
            if current_room == "hallway":
                if "key" in inventory:
                    print("You unlock the iron door with the key!")
                    current_room = "armory"
                else:
                    print("The iron door is locked tight. You need a key.")
            else:
                print("A solid wall blocks your path.")

        elif action == "south":
            if current_room == "armory":
                current_room = "hallway"
            else:
                print("There is nothing to the south.")

        elif action == "down":
            if current_room == "hallway":
                current_room = "dungeon"
            else:
                print("The floor is solid here.")

        elif action == "up":
            if current_room == "dungeon":
                current_room = "hallway"
            else:
                print("There is no way up from here.")

        elif action == "take":
            # Logical handling for picking up items based on location
            if target == "key" and current_room == "dungeon" and "key" not in inventory:
                inventory.append("key")
                print("You picked up the shiny key!")
            elif target == "shield" and current_room == "armory" and "shield" not in inventory:
                inventory.append("shield")
                print("You grab the golden shield! You feel a surge of power. YOU WIN!")
                game_running = False # Game ends successfully
            else:
                print(f"You don't see a {target if target else 'item'} here.")

        else:
            # Fallback for invalid inputs
            print("I don't understand that command. Try 'look' or a direction.")

# Entry point for the script
if __name__ == "__main__":
    start_game()
