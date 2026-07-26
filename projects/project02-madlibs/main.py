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