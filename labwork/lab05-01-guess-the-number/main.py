# DEV 108 - Lab Activity 5
# 07/20/26
# Katherine Luciano

# Picks the number randomly
import random

# Title of game
def display_title():
    print("Welcome to Guess the Number!")
    print()

# Get the users name
def get_name():
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}!")
    print()

# Ask the player to select a difficulty level
def play_game():    
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
        max_number = 100
        tries = 8
    else:
        max_number = 1000
        tries = 10

# Lets the user know if they are guessing too high or too low
    number = random.randint(1, max_number)
    print(f"I'm thinking of a number from 1 to {max_number}\n")
    count = 1

    while count <= tries:
        guess = int(input("Your guess: "))

        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        else:
            print(f"You guessed it in {count} tries!\n")
            return "win"
    else: 
        print(f"You ran out of guesses, the number was {number}.\n")
        return "loss"

# Main flow of the game     
def main():
    display_title()
    get_name()
    
    # Start players score at zero
    wins = 0
    losses = 0
    again = "y"

    while again.lower() == "y":
        result = play_game()

    # Update players score
        if result == "win":
            wins += 1
        else:
            losses += 1
        print(f"Score: {wins} wins and {losses} losses.")
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Thank you for playing, take care!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
