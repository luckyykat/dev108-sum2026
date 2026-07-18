# DEV 108 Lab 04
# 07/17/26
# Katherine Luciano

# display a welcome message
print("Welcome to The Miles Per Gallon Application")
print()

# set the loop to run atleast once
repeat_mpg = "y"

while repeat_mpg.lower() == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:    "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # inputs must be good
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:          ", mpg)
        total_gas_cost = round(gallons_used * cost_per_gallon, 2)
        print("Total Gas Cost:          ", total_gas_cost)
        cost_per_mile = round(total_gas_cost / miles_driven, 2)
        print("Cost Per Mile:          ", cost_per_mile)

    print()
    repeat_mpg = input("Get entries for another trip? (y/n): ")
print("Thank you for using The Miles Per Gallon Application, have a great day!")

