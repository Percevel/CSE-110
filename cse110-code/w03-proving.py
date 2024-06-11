#getting info for meal pricing
print()
chil_meal= float(input("What's the price of a childrens meal? "))
adul_meal= float(input("What's the price of an adults meal? "))
num_chil= int(input("How many children are getting food? "))
num_adul= int(input("How many adults are getting food? "))
tax_rate= float(input("What's the sales tax rate? "))
print()

#manipulating variables to get subtoatal and sales tax
meal_toatal= (num_adul*adul_meal)+(num_chil*chil_meal)
sales_tax= meal_toatal*(tax_rate/100)
print(f"Subtoatal: ${meal_toatal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
total = meal_toatal+sales_tax
print(f"Total: ${total:.2f}\n")

#Change giving
payment= int(input("What is the payment amount? "))
if (payment-total) < 0:
    print(f"Not enough money, please order again.\n")
else:
    print(f"Change: ${(payment-total):.2f}\n")
