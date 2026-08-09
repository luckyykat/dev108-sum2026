# DEV 108 - 9.1 Enhance the Invoice Program
# 08/08/26
# Katherine Luciano

from decimal import Decimal, ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

# locale for US currency formatting
lc.setlocale(lc.LC_ALL, "en_US.UTF-8")

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    
    # calculate shipping cost
    shipping_cost = subtotal * Decimal("0.085")
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)

    # added shipping cost in total                                 
    invoice_total = subtotal + shipping_cost + sales_tax

    # currency strings using locale 
    order_total_str = lc.currency(order_total, grouping=True)
    discount_str = lc.currency(discount, grouping=True)
    subtotal_str = lc.currency(subtotal, grouping=True)
    shipping_cost_str = lc.currency(shipping_cost, grouping=True)
    sales_tax_str = lc.currency(sales_tax, grouping=True)
    invoice_total_str = lc.currency(invoice_total, grouping=True)

    # specifier variables for column widths
    s1 = 20
    s2 = ">12"

    # display the results
    print(f"{'Order total:':{s1}} {order_total_str:{s2}}")
    print(f"{'Discount amount:':{s1}} {discount_str:{s2}}")
    print(f"{'Subtotal:':{s1}} {subtotal_str:{s2}}")
    print(f"{'Shipping cost:':{s1}} {shipping_cost_str:{s2}}")
    print(f"{'Sales tax:':{s1}} {sales_tax_str:{s2}}")
    print(f"{'Invoice total:':{s1}} {invoice_total_str:{s2}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")