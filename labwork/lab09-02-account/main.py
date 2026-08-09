# DEV 108 - Enhance the Create Account Program
# 07/09/26
# Katherine Luciano

def main():
    # Program title
    print("Welcome to the Account Validaton Program")
    print()

    # Get user information
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()  

    email = get_email()
    print()

    phone = get_phone()
    print()

    # Get user first name and show confirmation message
    first_name = get_first_name(full_name)
    print(f"Hello {first_name}, thank you for creating an accouunt.")
    print(f"We'll text your confirmation code to this number: {phone}")

    # Exit message
    print("Thank you for using the Account Validation Program, take care!")             

# Loop for user to provide full name     
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

# Finds the space and slices the name     
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

# Loop until users passwords meets the requirements    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

# Loop until user contains "@" and ends with ".com"
def get_email():
    while True:
        email = input("Enter email address:    ").strip().lower()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("Please enter a 10 digit phone number.")

# Loop until user enters 10-digit phone number
def get_phone():
    while True:
        phone = input("Enter phone number:    ").strip()



        
if __name__ == "__main__":
    main()


