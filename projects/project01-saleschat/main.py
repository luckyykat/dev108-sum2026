# DEV 108 - Project 1
# 07/13/26
# Katherine Luciano

# Set the product price and sales tax rate.
price = 69.99
tax_rate = 0.10

# Greet the customer and introduce the chatbot.
print("========================================")
print("  Welcome to Happy Little Creations!")
print("========================================")
print("Hello there! My name is Bob, your happy little sales chatbot.")
print()

# Ask if the customer wants to learn more about the product.
learn_more = input("Would you like to learn about our product? Enter yes or no: ")
print()

if learn_more == "yes":
    # Sales Pitch
    print("""Our Happy Little Creation is a follow by number 5 x 7 Canvas
made to bring a peaceful touch of nature into your home. Each one is unique,
but they will always include happy little trees. There are no mistakes here,
only happy little creations!

Features and Benefits:
- 5x7 Canvas
- Paint
- Brushes
- Color Key Guide""")
    
print()
print("Price: $" + str(price) + "for each painting")
print()

# Ask if the customer wants to make a purchase.
buy_product = input("Would you like to buy a Happy Little Creation? Enter yes or no: ")
print()

if buy_product == "yes":
    # Gather the customer's information.
    print("Wonderful! Bob will help you complete your order.")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    quantity = int(input("How many paintings would you like to buy? "))

# Calculate the subtotal, slaes tax, and total
subtotal = round(price * quantity, 2)
tax = round(subtotal * tax_rate, 2)
total = round(subtotal + tax, 2)

# Display the receipt.
print()
print("============================================")
print("        Happy Little Creations")
print("               Receipt")
print("============================================")
print("Customer: " + first_name +" "+ last_name")
print("Email:" + email)
print("Phone: " + phone)
print("--------------------------------------------")
print("Item: Happy Little Creation")
print("Quantity: " + str(quantity))
print("Price each: $" + str(price))
print("Subtotal: $" + str(subtotal))
print("Sales tax (10%): $" + str(tax))
print("Total amount due: $" + str(total))
print("==============================================")
print()
print("Thank you for shopping with Happy Little Creations!")
print("Don't forget there are no mistakes, only happy accidents. Happy Painting! - Bob")

# End if customer does not want to buy.
else: 
print("No problem! Thank you for visiting Happy Little Creations.")
print("Bob hopes you have a happy little day!")

