print("Welcome to Treasure Island.")  
print("Your mission is to find the treasure.") 

# Get user's direction choice, remove leading/trailing spaces and convert to lowercase
direction = input("You\'re at a crossroad. Wher you want to go? left or right? ").strip().lower()  # strip() removes spaces, lower() makes input lowercase

if direction == "right":
    print("Game Over.")    # End game if user chooses right
elif direction == "left":
    action = input("swim or wait? ").strip().lower()  # strip() removes spaces, lower() makes input lowercase
    if action == "swim":
        print("Game Over.")  # End game if user chooses swim
    elif action == "wait":
        door = input("Which door? Red, Blue, or Yellow? ").strip().lower()  # strip() removes spaces, lower() makes input lowercase
        if door == "red":
            print("Game Over.")  # End game if user chooses red door
        elif door == "blue":
            print("Game Over.")  # End game if user chooses blue door
        elif door == "yellow":
            print("You Win!")  # Win if user chooses yellow door
        else:
            print("Invalid door. Game Over.")  # Handle invalid door input
    else:
        print("Invalid action. Game Over.")  # Handle invalid action input
else:
    print("Invalid choice. Game Over.")  # Handle invalid direction input
