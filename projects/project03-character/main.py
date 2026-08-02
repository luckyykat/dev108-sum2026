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

    # Select a sanrio character using random number 
def get_character_type(character_number):
    if character_number == 1:
        return "Hello Kitty"
    elif character_number == 2:
        return "My Melody"
    elif character_number == 3:
        return "Kuromi"
    elif character_number == 4:
        return "Cinnamoroll"
    else:
        return "Pompompurin"

# Character generator
def main():
    display_welcome()

    create_character = input(
        "Would you like to generate a Sanrio character? yes or no: "
    )

    # Loop repeats the generator while the user answers yes
    while create_character.lower() == "yes":
        character_name = input("What would you like to name your character?: ")

        character_number = random.randint(1,5)
        character_type = get_character_type(character_number)
        # Five random character traits
        kindness = random.randint(1, 10)
        cuteness = random.randint(1, 10)
        energy = random.randint( 1, 10)
        friendship = random.randint(1, 10)
        creativity = random.randint(1, 10)
       
        print()
        print("Welcome, " + character_name + "!")
        print("Sanrio Character: " + character_type)
        print("Kindness: " + str(kindness))
        print("Cuteness: " + str(cuteness))
        print("Energy: " + str(energy))
        print("Friendship " + str(friendship))
        print("Creativity: " + str(creativity))
        print()

        create_character = input(
            "Would you like to generate another Sanrio character? yes or no: "
        )
if __name__ == "__main__":
    main()
