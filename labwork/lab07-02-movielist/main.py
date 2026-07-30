# DEV 108 Lab 7.2 - Movie List
# 07/29/26
# Katherine Luciano

# Title and available commands 
def display_menu():
    print("The Movie List")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by a year")
    print("exit - Exit program")
    print()
    

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for movie in movie_list:
            row = movie
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ") @ " + str(row[2]))
            i += 1
        print()

# Add a new movie to the list
def add(movie_list):
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price: "))

    # Stores the name, year, and price in a new movie list
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price)

    # Add the new movie to main menu list
    movie_list.append(movie)

    # Confirms that a new movie was added 
    print(movie[0] + " was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

# Finds and dispays movies released in a specific year
def find_by_year(movie_list):
    year = int(input("Year: "))

    for movie in movie_list:
        if movie[1] == year:
            print(movie[0] + " was released in " + str(year) + ".")
        print()
        
def main():
    # Organizes each movie by name, year and price
    movie_list = [
        ["Monty Python and the Holy Grail", 1975, 9.95],
        ["On the Waterfront", 1954, 5.59],
        ["Cat on a Hot Tin Roof", 1958, 7.95]
    ]
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "find":
            find_by_year(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
