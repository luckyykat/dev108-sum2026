# DEV 108 - Project 2 - Mad Libs
# 07/25/26
# Katherine Luciano 

# Title
print("====================================")
print("    MAD LIBS DRAG RACE EDITION")
print("====================================")

# Ask the user if they want to play 
play_again= input("\nWould you like to play a game? (y/n): ").lower()

# Redirect the user if they don't select y or n
while play_again != "y" and play_again != "n":
    print("Please enter y for yes or n for no.")
    play_again = input("Would you like to play a game? (y/n): ").lower()

# Keeps track of how many stories the player completes
story_count = 0

# Ask the user for their name and greeting
if play_again == "y":
    player_name = input("\nFirst what is your name? ")
    print("\nHello," + player_name + "! Welcome to Mad Libs Drag Race Edition.")

# Ask the user to pick a storyline 
while play_again == "y":
    print("\nChoose your challenge:")
    print(" a. The Makeover Challenege")
    print("b. The Girl Group Challenge")

    story_choice =("\nWhich challenge would you like? (a/b): ").lower()

if story_choice == "a":
    print("\nThe Makeover Chalenege")
    print("Create a new memeber of your drag family!\n")