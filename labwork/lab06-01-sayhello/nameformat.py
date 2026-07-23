# DEV 108 - Lab Activity 6 - Name Format
# 07/23/26
# Katherine Luciano

"""Functions for greeting users and formatting names."""

# Get the users name
def sayHello(firstName):
    """Return a greeting that uses the user's first name."""
    return f"Hello {firstName}!"

# fullName() ex: Tony Stark
def fullName(firstName, lastName):
    """Return the user's first and last name separated by a space."""
    return f"{firstName} {lastName}"

# lastNameFirst() ex: Stark, Tony
def lastNameFirst(firstName, lastName):
    """Return the user's last name, followed by a comma and first name."""
    return f"{lastName}, {firstName}"