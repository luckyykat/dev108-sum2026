# DEV 108 Lab 8.1 - MPG/CSV
# 07/31/26
# Katherine Luciano

# Import the csv module and file name 
import csv
FILENAME = "trips.csv"

# Trip data for the CSV file 
def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    # List to store all trip data 
    trips = []
    more = "y"
    
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        # Store current trip data in the trips list
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trips.append(trip)
        
        more = input("More entries? (y or n): ")

    # Write all trip data after the user is done
    write_trips(trips)

    print("Bye")

if __name__ == "__main__":
    main()

