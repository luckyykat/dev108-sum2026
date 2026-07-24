# DEV 108 - Lab Activity 6 - Say Hello
# 07/22/26
# Katherine Luciano


# Import nameformat.py
import nameformat

# Main, title and opening greeting
def main():
    print("Welcome to The NameFormat Module")
    print("Hello!")

# Ask for the names
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your name: ")

# Display the menu choices
    print("\n* * MENU * *")
    print("1 - Say Hello")
    print("2 - Output Full Name")
    print("3 - Output Last Name, First Name")
    print("4 - Read Documentation")
    print("5 - Exit")

# Start with an empty choice to begin the loop 
    choice = ""

#Keep repeating the menu options until the user selects 5
    while choice != "5":
        # Ask the user to select an option
        choice = input("\nWhat is your choice? ")

        # Option 1 calls the sayHello function
        if choice == "1":
            print(nameformat.sayHello(firstName))

        # Option 2 calls the fullName function
        elif choice == "2":
            print(nameformat.fullName(firstName, lastName))

        # Option 3 calls the lastNameFirst function
        elif choice == "3":
            print(nameformat.lastNameFirst(firstName, lastName))

        # Option 4 displays the documentation for each function
        elif choice == "4":
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)

        # Option 5 displays a message before ending the loop
        elif choice == "5":
            print("Goodbye!")

        # If the user enters anything other than 1 through 5
        else:
            print("Please choose an option from 1 through 5.")

    # Run main when this file is executed directly
    if __name__ == "__main__":
        main()