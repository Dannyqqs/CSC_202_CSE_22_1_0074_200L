# Introduction to the game
print("Welcome to the Treasure Hunt!")

# Asking the user to choose a direction
direction = input('You are at a crossroad. Would you like to go "right" or "left"? ').lower()

# Checking the chosen direction
if direction == "right":
    print("Oh no! You fell into a pit! Game Over!")
elif direction == "left":
    # Asking the user to choose between swimming or waiting
    action = input("Great choice! You've reached a lake. Would you like to 'swim' across or 'wait' here? ").lower()

    # Checking the user's choice at the lake
    if action == "swim":
        print("Brave move! You made it across the lake!")
        # Asking the user to choose between three doors
        door = input("Now you see three doors: 'Blue', 'Red', and 'Green'. Which door do you want to open? ").lower()

        # Checking the user's choice of door
        if door == "blue":
            print("Oops! You entered a room full of snakes! Game Over!")
        elif door == "red":
            print("Congratulations! You found the treasure! You win!")
        elif door == "green":
            print("Yikes! You walked into a room full of spiders! Game Over!")
        else:
            print("Invalid choice! Game Over!")
    elif action == "wait":
        print("Smart move! You avoided danger and lived to see another day!")
    else:
        print("Invalid choice! Game Over!")
else:
    print("Invalid choice! Game Over!")