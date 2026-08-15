# DEV 108 - Final Project: Mission to Mars
# 08/11/26
# Katherine Luciano 

# Import csv tools and randomizer 
import csv
import random

# Main settings for csv file, admin password, and pod size
FILE_NAME = "marsbase_humans.csv"
ADMIN_PASSWORD = "MarsBaseAdmin4"
POD_LIMIT = 4

# This function reads all saved humans from the csv file
def load_humans():
    humans = []

    with open (FILE_NAME, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            humans.append(row)

    return humans

# This function saves all humans back to the csv file
def save_humans(humans):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(humans)

# This function asks for text and restricts a blank answer
def get_text(prompt):
    answer = input(prompt).strip()

    while answer == "":
        print("Please do not leave this blank.")
        answer = input(prompt).strip()

    return answer

# This function asks for users age and makes sure the answer the user submits is a number 
def get_age():
    age = input("Age: ").strip()

    while age.isdigit() == False:
        print("Please enter the age using numbers only.")
        age = input("Age: ").strip()

    return age

# This function creates an id number that is not already used
def make_id(humans):
    used = []

    for human in humans:
        used.append(human[0])

    new_id = str(random.randint(1000, 9999))

    return new_id

# This function gives the user an email from name and id
def make_email(first_name, last_name, human_id):
    first_name = first_name.lower()
    last_name = last_name.lower()
    email = "{}.{}{}@mars.org".format(first_name, last_name, human_id)

    return email

# This function creates a password w/ lowercase, uppercase, numbers and symbols
def make_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%&"

    password = ""
    password = password + random.choice(lower)
    password = password + random.choice(upper)
    password = password + random.choice(numbers)
    password = password + random.choice(symbols)

    all_chars = lower + upper + numbers + symbols

    while len(password) < 10:
        password = password + random.choice(all_chars)

    return password

# This function assigns a random habitat and pod
def make_pod():
    habitats = []
    habitats.append("Erebus Habitat")
    habitats.append("Amazonis Habitat")
    habitats.append("Greenhouse Habitat")
    habitats.append("Research Habitat")

    habitat = random.choice(habitats)
    pod_number = random.randint(1, 5)
    pod = "{} - Pod {}".format(habitat, pod_number)

    return pod 

# This function creates a Mars Base note for the user
def make_note():
    notes = []
    notes.append("Greenhouse soil team candidate")
    notes.append("Rover resource run recommended")
    notes.append("Assigned to crop nutrient research")
    notes.append("Extra oxygen safety training complete")
    notes.append("Possible Erebus Montes exploration crew")
    notes.append("Martian meal prep volunteer")

    note = random.choice(notes)

    return note

# This function creates and saves a new user account
def create_account():
    humans = load_humans()

    print("\nCreate a new Mars Base Human Account")
    print("----------------------------------------")

    first_name = get_text("First name: ")
    last_name = get_text("Last name: ")
    age = get_age()

    human_id = make_id(humans)
    email = make_email(first_name,  last_name, human_id)
    password = make_password()
    pod = make_pod()
    note = make_note()

    new_human = []
    new_human.append(human_id)
    new_human.append(first_name)
    new_human.append(last_name)
    new_human.append(age)
    new_human.append(email)
    new_human.append(password)
    new_human.append(pod)
    new_human.append(note)

    humans.append(new_human)
    save_humans(humans)

    print("\nNew Mars Base HUman Account Created")
    print("---------------------------------------")
    print("ID: {}".format(human_id))
    print("Name: {} {}".format(first_name, last_name))
    print("Age: {}".format(age))
    print("Email: {}".format(email))
    print("Password: {}".format(password))
    print("Living Pod: {}".format(pod))
    print("Note: {}".format(note))

# This function puts the humans in a list 
def list_humans():
    humans = load_humans()

    print("\nAll Mars Base Humans")
    print("------------------------")

    if len(humans) == 0:
        print("No humans are saved yet.")
    else:
        print("{:<15} {:<15} {:<30} {:<5} {:<20}".format("First", "Last", "Email", "Age", "Pod"))
        print("-" * 90)

        for human in humans:
            print("{:<15} {:<15} {:<30} {:5} {:<20}".format(human[1], human[2], human[4], human[3], human[6]))

# This function searches the humans by last name
def search_last_name():
    humans = load_humans()
    search_name = get_text("Enter a last name to search: ").lower()
    found = False

    print("\nSearch Results")
    print("-------------------")

    for human in humans:
        if human[2].lower() == search_name:
            found = True
            print("Name: {} {}".format(human[1], human[2]))
            print("Pod: {}".format(human[6]))
            print("Notes: {}".format(human[7]))
            print()

    if found == False:
        print("No matching humans were found.")

# This function shows how full each pod is 
def pod_status():
    humans = load_humans()
    pods = []

    for human in humans:
        if human[6] not in pods:
            pods.append(human[6])

    print("\nMars Base Living Pod Status")
    print("-------------------------------")

    if len(pods) == 0:
        print("No pod assignments yet.")
    else:
        for pod in pods:
            count = 0

            for human in humans:
                if human[6] == pod:
                    count = count + 1
            spaces = POD_LIMIT - count

            if spaces < 0:
                spaces = 0 

            print("{}: {} assigned, {} spaces remaining".format(pod, count, spaces))

 # This function shows the full report if admin password is correct
def admin_report():
    password = input("Enter admin password: ")

    if password == ADMIN_PASSWORD:
        humans = load_humans()

        print("\nMars Base Admin Human Population Report")
        print("-------------------------------------------")

        if len(humans) == 0:
            print("No humans are saved yet.")
        else:
            print("{:<6} {:<12} {:<12} {:<28} {:<12} {}".format("ID", "First", "Last", "Email", "Password", "Notes"))
            print("-" * 100)

            for human in humans:
                print("{:<6} {:<12} {:<12} {:<28} {:<12} {}".format(human[0], human[1], human[2], human[4], human[5], human[7]))
    else:
        print("Access denied. Incorrect password.")

# This function deletes one human account by ID
def delete_account():
    humans = load_humans()
    human_id = get_text("Enter the ID number to delete: ")
    found = False
    new_list = []

    for human in humans:
        if human [0] == human_id:
            found = True
            print("Found: {} {} in {}".format(human[1], human[2], human[6]))
            sure = input("Are you sure you want to delete this account? yes or no: ").lower()

            if sure == "yes":
                print("Account deleted.")
            else:
                new_list.append(human)
                print("Human account deleted.")
        else:
            new_list.append(human)
    if found == True:
        save_humans(new_list)
    else:
        print("No human with that ID was found.")

# This is the bonus function randomly picks 2-4 humans for a greenhouse mission
def special_mission():
    humans = load_humans()

    print("\nSpecial Mars Base Greenhouse Mission")
    print("----------------------------------------")

    if len(humans) < 2:
        print("At least 2 humans are needed for this mission.")

    else:
        mission_size = random.randint(2, 4)

        if mission_size > len(humans):
            mission_size = len(humans)

        chosen = []

        while len(chosen) < mission_size:
            human = random.choice(humans)

            if human not in chosen:
                chosen.append(human)

        print("Mission crew selected for soil recovery:")

        for human in chosen:
            print("- {} {} from {}".format(human[1], human[2], human[6]))

            print("\nMission note: Collect Martian soil samples near Erebus Montes.")
            print("Goal: turn one planter of toxic soil into safe crop soil.")

# This function shows the menu and checks for a menu choice 
def show_menu():
    print("\nMars Base - Human Account Setup System")
    print("------------------------------------------")
    print("1. Create a new Mars Base human account")
    print("2. List all Mars Base humans")
    print("3. Search by last name")
    print("4. Living pod status")
    print("5. Admin population report")
    print("6. Delete a human account")
    print("7. Bonus greenhouse mission")
    print("8. Exit")

    choice = input("Choose an option from 1 to 8: ")

    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("That is not a valid menu choice")
        choice = input("Choose an option from 1 to 8: ")

    return choice

# This function keeps the program running until the user exits
def main():
    choice = ""

    while choice != "8":
        choice = show_menu()

        if choice == "1":
            create_account()
        elif choice == "2":
            list_humans()
        elif choice == "3":
            search_last_name()
        elif choice == "4":
            pod_status()
        elif choice == "5":
            admin_report()
        elif choice == "6":
            delete_account()
        elif choice == "7":
            special_mission()
        elif choice == "8":
            print("Goodbye, Mars Base crew member!")


if __name__ == "__main__":
    main()