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

    # Make Over Challenege Questions
    if story_choice == "a":
        print("\nThe Makeover Chalenege")
        print("Create a new member of your drag family!\n")

        drag_name = input("1) What is your drag name? ")
        partner_name = input("2) What is your makeover partner's regular name? ")
        relationship = input("3) What is your relationship to this person? ")
        drag_adjective = input(
            "4) Enter a capitalized adjective for your partner's drag name: "
            )
        drag_noun = input("5) Enter a capitalized noun for your drag family name: ")
        special_quality = input(
            "6) Name a quality that makes them worthy of your House: "
            )
        outfit_color = input("7) Choose a color for your matching outfits: ")
        outfit_material = input(
            "8) Name an unusual material for the outfits: "
            )
        runway_move = input("9) Name a runway move or dance move: ")

        family_drag_name = drag_adjective + " " + drag_noun
        house_name = drag_noun

    # Makeover Challenge Story
        print("\n--------------------------------------------------------------")
        print(player_name + ", here is your Makeover Challenge story:\n")
        print(
                drag_name + " invited their " + relationship + ", " + partner_name + ", "
                "to compete in the Makeover Challenge."
            )
        print(
                partner_name + " nervously entered the workroom and prepared "
                "for a complete drag transformation."
            )
        print(
                "They welcomed the new queen into the House of " + house_name
                + " and gave them the family drag name " + family_drag_name + "."
            )
        print(
                "Together, they created matching " + outfit_color + " outfits made "
                "entirely from " + outfit_material + "."
            )
        print(
                "They finished the runway with a dramatic " + runway_move + ", and "
                "the judges cheered."
            )
        print(
                "Because of their incredible " + special_quality + ", " + family_drag_name
                + " proved they truly belonged in the House of " + house_name + "!"
            )

# The Girl Group Challenge Questions
elif story_choice == "b":
        print("\n--- THE GIRL GROUP CHALLENGE ---")
        print("Get ready to write and perform a brand-new drag anthem!\n")

        group_name = input("1) Give your girl group a name: ")
        music_genre = input("2) Name a type of music: ")
        song_title = input("3) Give the group's song a title: ")
        song_topic = input("4) What unusual topic is the song about? ")
        silly_lyric = input("5) Enter a silly lyric or catchphrase: ")
        dance_move = input("6) Name a signature dance move: ")
        stage_prop = input("7) Name an unusual object to use as a prop: ")

        # Makes sure the user eneters a number 1-10
        dancer_count = int(input(
            "8) Choose a number of backup dancers from 1 to 10: "
        ))

        while dancer_count < 1 or dancer_count > 10:
            print("Please enter a whole number from 1 to 10.")
            dancer_count = int(input(
                "8) Choose a number of backup dancers from 1 to 10: "
            ))

        rupaul_emotion = input(
            "9) Enter an emotion describing RuPaul's reaction: "
        )

        if dancer_count == 1:
            dancer_phrase = "one fearless backup dancer"
        elif dancer_count <= 5:
            dancer_phrase = str(dancer_count) + " energetic backup dancers"
        else:
            dancer_phrase = "a huge crew of " + str(dancer_count) + " backup dancers"

# Girl group Challenge Story
    print("\n--------------------------------------------------------------")
    print(player_name + ", here is your Girl Group Challenge story:\n")
    print(
                "The contestant joined the newest drag sensation, " + group_name + "."
            )
    print(
                "Together, the group recorded a " + music_genre + " anthem titled "
                "\"" + song_title + ".\""
            )
    print(
                "The song was about " + song_topic + ", and its unforgettable lyric "
                "was, \"" + silly_lyric + "!\""
            )
    print(
                "On the main stage, the group performed the " + dance_move + " with "
                + dancer_phrase + " while waving a " + stage_prop + "."
            )
    print(
                "RuPaul looked " + rupaul_emotion + " and declared the performance "
                "a drag masterpiece."
            )
    print(group_name + " had officially become the next big girl group!")

    story_count += 1
    print("--------------------------------------------------------------")

# Keeps track of how many stories created
    if story_count == 1:
        print("\nYou have created 1 story.")
    else:
        print("\nYou have created", story_count, "stories.")

    play_again = input("\nWould you like to play again? (y/n): ").lower()

    # Ask the user if they want to replay and farewell
    while play_again != "y" and play_again != "n":
        print("Please enter y for yes or n for no.")
        play_again = input("Would you like to play again? (y/n): ").lower()

print("\nThank you for playing!\n")