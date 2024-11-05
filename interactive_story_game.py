import random
import time
import os

# Simple inventory
inventory = []

def clear_console():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    print("Welcome to the Interactive Story!")
    print("You are standing at a crossroad.")
    draw_character()
    choice1()

def draw_character(position=0):
    clear_console()  # Clear the console before drawing
    # Simple character representation using symbols
    character = """
        O
       /|\\
       / \\
    """
    # Print the character in different horizontal positions
    print("\n" * position + character)

def animate_character():
    for position in range(5):  # Animate moving down the screen
        draw_character(position)
        time.sleep(0.2)  # Wait for 0.2 seconds
    for position in range(4, -1, -1):  # Animate moving up the screen
        draw_character(position)
        time.sleep(0.2)

def choice1():
    print("\nDo you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        choice1()

def left_path():
    print("\nYou went left and found a treasure chest!")
    draw_character()
    animate_character()  # Animate the character
    print("Do you want to open it or leave it?")
    choice = input("Type 'open' or 'leave': ").lower()
    if choice == "open":
        item = random.choice(["gold coins", "magic potion", "old map"])
        print(f"You found {item}! You add it to your inventory.")
        inventory.append(item)
        print(f"Your inventory: {inventory}")
    elif choice == "leave":
        print("You walked away safely. Maybe next time!")
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("\nYou went right and encountered a dragon!")
    draw_character()
    animate_character()  # Animate the character
    print("Do you want to fight or run away?")
    choice = input("Type 'fight' or 'run': ").lower()
    if choice == "fight":
        if "magic potion" in inventory:
            print("You used the magic potion and defeated the dragon! You win!")
        else:
            print("The dragon defeated you. Game over!")
    elif choice == "run":
        print("You escaped safely. Phew!")
        random_event()
    else:
        print("Invalid choice. Please try again.")
        right_path()

def random_event():
    events = [
        "You find a friendly squirrel who offers you some nuts.",
        "You stumble upon a mysterious old man who tells you a riddle.",
        "You find a lost puppy who wants to join you on your adventure!"
    ]
    print(random.choice(events))
    choice = input("Do you want to (1) befriend the squirrel, (2) solve the riddle, or (3) adopt the puppy? Type 1, 2, or 3: ")
    if choice == "1":
        print("The squirrel gives you some nuts for your journey!")
        inventory.append("squirrel nuts")
    elif choice == "2":
        print("You solved the riddle and the old man gives you a magic key!")
        inventory.append("magic key")
    elif choice == "3":
        print("You adopted the puppy! It will help you on your adventures.")
        inventory.append("puppy")
    else:
        print("Invalid choice. Please try again.")
        random_event()

# Start the game
start_game()