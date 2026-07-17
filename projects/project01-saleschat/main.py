# DEV 108 - Project 1
# 07/13/26
# Katherine Luciano

# Set the product price and sales tax rate.
price = 69.99
tax_rate = 0.10

# Greet the customer and introduce the chatbot.
print("========================================")
print("Welcome to Happy Little Creations!")
print("========================================")
print("Hello there! My name is Bob, your happy little sales chatbot.")
print()

# Ask if the customer wants to learn more about the product.
learn_more = input("Would you like to learn about our product? Enter yes or no: ")
print()

if learn_more == "yes":
    # Sales Pitch
    print("""Our Happy Little Landscape is a follow by number 5 x 7 Canvas
made to bring a peaceful touch of nature into your home. Each one is unique,
but they will always include happy little trees. There are no mistakes here,
only happy little creations!

Features and Benefits:
- 5x7 Canvas
- Paint
- Brushes
- Color Key Guide""")