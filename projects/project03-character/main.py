# DEV 108 - Project 3 - Character Gnerator
# 08/01/26
# Katherine Luciano

# Generates random numbers 
import random 

# Display welcome message
def display_welcome(): 
    print("********************************************")
    print(" Welcome to the Sanrio Character Generator")
    print("********************************************")
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
    # List of accessories
    accessories = [
        "red bow",
        "black jester hat",
        "bow tie",
        "brown beret",
        "pink hood"
    ]

    create_character = input(
        "Would you like to generate a Sanrio character? yes or no: "
    )

    # Loop repeats the generator while the user answers yes
    while create_character.lower() == "yes":
        character_name = input("What would you like to name your character?: ")

        character_number = random.randint(1,5)
        character_type = get_character_type(character_number)

        accessory_number = random.randint(0,4)
        accessory = accessories[accessory_number]
                                
        # Five random character traits
        kindness = random.randint(1, 10)
        cuteness = random.randint(1, 10)
        energy = random.randint( 1, 10)
        friendship = random.randint(1, 10)
        creativity = random.randint(1, 10)

        # Random points for bake off
        baking_points = random.randint(50, 100)
       
        print()
        print("Welcome, " + character_name + "!")
        print("Sanrio Character: " + character_type)
        print("Accessory: " + accessory)
        print("Kindness: " + str(kindness))
        print("Cuteness: " + str(cuteness))
        print("Energy: " + str(energy))
        print("Friendship: " + str(friendship))
        print("Creativity: " + str(creativity))
        print("Baking Points: " + str(baking_points))
        print("-------------------------------")
        print()

        # Ask user if they want to enter the Bake Off Battle 
        battle_choice = input("\nWould you like to enter a Bake Off Battle with this character? yes or no: ").lower()
        if battle_choice == "yes":
            #Generate oppenents stats
            opponent_type = get_character_type(random.randint(1, 5))
            opponent_hp = random.randint(50, 100)

            print("\n*** Bake Off Battle Start ***")
            print("Opponent: " + opponent_type + " (Baking Points: " + str(opponent_hp)+ ")")
            print(character_name + " (" + character_type + ") (Baking Points: " + str(baking_points) + ")")
            print("==========================================\n")

            # Battle loop continues while both bakers have points remaining
            round_num = 1
            while baking_points > 0 and opponent_hp > 0:
                print("--- Round " + str(round_num) + " ---")

                # Player bakes & opponent attacks 
                player_bake = random.randint(10, 25)
                opponent_hp = opponent_hp - player_bake
                print(character_name + " baked a delicious pastry and dealt " + str(player_bake) + " points of damage!")

                # Check if opponent is defeated before they counter-attack
                if opponent_hp <= 0:
                    print(opponent_type + "'s cake collapsed!")
                    break

                # Opponent bakes & attacks player
                opponent_bake = random.randint(10, 25)
                baking_points = baking_points - opponent_bake
                print(opponent_type + " baked a sweet treat and dealt " + str(opponent_bake) + " points of damage!")

                # Random healing boost
                heal_chance = random.randint(1, 3)
                if heal_chance == 1 and baking_points > 0:
                    heal_amount = random.randint(5, 15)
                    baking_points = baking_points + heal_amount
                    print("Sugar sparkle scone added " + character_name + " got a bonus sugar boost and gained " + str(heal_amount) + " Baking Points!")

                print(character_name + " HP: " + str(max(0, baking_points)) + " | " + opponent_type + " HP: " + str(max(0, opponent_hp)) + "\n")
                round_num = round_num + 1

                # Declare winner
                print("=============================")
                if baking_points > 0:
                    print("Victory! " + character_name + " won the Bake Off!")
                else:
                    print("Oh no! " + opponent_type + " won the Bake Off this time!")
                print("=============================")

            # Ask if the user wants to generate another character
            create_character = input("\nWould you like to generate another Sanrio character? yes or no: ").lower()

    # Thank the user and farewell message
    print("\nThank you for playing the Sanrio Character Bake Off! Goodbye!")

if __name__ == "__main__":
    main()
