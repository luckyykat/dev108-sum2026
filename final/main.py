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