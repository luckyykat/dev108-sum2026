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
        used.append(humans[0])

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

    print("\nCreate a new Mars Base HUman Account")
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
    print("ID: {}".format(first_name, last_name))
    print("Name: {} {}".format(age))
    print("Email: {}".format(email))
    print("Password: {}".format(password))
    print("Living Pod: {}".format(pod))
    print("Note: {}".format(note))