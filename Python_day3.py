#Treasure hunt 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You\'re at a fork in the road, which direction do you want to go? "
                "Type 'left' or 'right'.\n ").lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is an island in the middle.'
                    ' Type "swim" to swim across '
                    'or "wait" to wait for a boat.\n').lower()
    if choice2 == "wait":
        choice3 = input("You\'ve arrived at the house safely."
                  "There are 3 doors."
                  " One red, one blue, and one yellow."
                  " Which color do you pick? \n ").lower()
        if choice3 == "red":
            print("Trapped door! You fell into a pit of angry vipers. GAME OVER!")
        elif choice3 == "blue":
            print("You were attacked by Lycans. GAME OVER!")
        elif choice3 == "yellow":
            print("You\'ve found the treasure! YOU WIN!")
    else:
        print("You\'re attacked by mutant frogs. GAME OVER!")
else:
        print("You fell into a snake pit! GAME OVER!")

