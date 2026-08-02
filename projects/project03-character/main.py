# DEV 108 - Project 3 - Character Gnerator
# 08/01/26
# Katherine Luciano

# Generates random numbers 
import random 

# Display welcome message
def display_welcome(): 
    print("********************************")
    print("   Sanrio Character Generator")
    print("********************************")
    print()

# Character generator
def main():
    display_welcome()

    create_character = input(
        "Would you like to generate a Sanrio character? yes or no: "
    )

    # Loop repeats the generator while the user answers yes
    while create_character.lower() == "yes":
        character_name = input("What would you like to name your character?: ")
        print()
        print("Welcome, " + character_name + "!")
        print()

        create_character = input(
            "Would you like to generate another Sanrio character? yes or no: "
        )
if __name__ == "__main__":
    main()