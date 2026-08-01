# DEV 108 Lab 8.1 & 8.2 - MPG/CSV
# 07/31/26
# Katherine Luciano

# Import the csv module and file name 
import csv
FILENAME = "trips.csv"

# Trip data for the CSV file 
def write_trips(trip):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(trip)

# Read the existing CSV data into the trips list
def read_trips():
    trips = []

    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            trips.append(row)

    return trips

# Display all the trip data on the screen for the user 
def list_trips(trips):
    print("Distance\tGallons\t\tMPG")

    for i in range(0, len(trips)):
        trip = trips[i]
        print(str(trip[0])) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2])

    print()

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

    # Display the exiting trip data
    trips = read_trips()
    list_trips(trips)
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
        # Save and display new trip
        write_trips(trip)
        list_trips(trips)
        
        more = input("More entries? (y or n): ")

    # Write all trip data after the user is done
    write_trips(trips)

    print("Bye")

if __name__ == "__main__":
    main()

