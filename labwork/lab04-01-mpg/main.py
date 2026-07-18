# DEV 108 Lab 04
# 07/17/26
# Katherine Luciano

# display a welcome message
print("Welcome to The Miles Per Gallon application")
print()

# set the loop to run atleast once
repeat_mpg = "y"

while repeat_mpg.lower() == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # inputs must be good
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:          ", mpg)

    print()
    repeat_mpg = input("Get entries for another trip? (y/n)")
print("Bye")

