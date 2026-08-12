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