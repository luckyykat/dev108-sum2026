# DEV 108 - Lab Activity 6 - Say Hello
# 07/22/26
# Katherine Luciano


# Import nameformat.py
import nameformat

# Main
def main():
    print("The NameFormat Module")
    print("Hello!")

# Ask for the names only once.
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your name: ")

    print("\n* * MENU * *")
    print("1 - Say Hello")
    print("2 - Output Full Name")
    print("3 - Output Last Name, First Name")
    print("4 - Read Documentation")
    print("5 - Exit")

    choice = ""

    while choice != "5":
        choice = input("\nWhat is your choice? ")

        if choice == "1":
            print(nameformat.sayHello(firstName))