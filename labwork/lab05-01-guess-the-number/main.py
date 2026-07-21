# DEV 108 - Lab Activity 5
# 07/20/26
# Katherine Luciano

import random

def display_title():
    print("Welcome to Guess the Number!")
    print()

def get_name():
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}!")
    print()

def play_game():    
    # Ask the player to select a difficulty level
    level = input(
        "Chose a level: e for Easy, m for Medium, or h for Hard: "
    ).lower()

    # Keep asking the user until they choose a level
    while level != "e" and level != "m" and level != "h":
        print("That was an invalid input, please try again!")
        level = input(
            "Choose a level: e for Easy, m for Medium, or h for Hard: "
        ).lower()

    # Setting the levels and amount of tries 
    if level == "e":
        max_number = 10
        tries = 5
    elif level == "m":
        max_number == 100
        tries == 8
    else:
        max_number == 1000
        tries == 10
    
    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
    print(f"You guessed it in {count} tries.\n")
     
def main():
    display_title()
    get_name()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
