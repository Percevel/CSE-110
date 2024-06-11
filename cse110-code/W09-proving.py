#Aiden Penman
print("Welcome to the Shopping Cart Program!")
ans = -1
items = []
iCost = []
while ans != 5:
    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")
    ans = int(input("Please enter an action: "))
    if ans ==1:
        item = input("What item do you want to add to the cart?")
        items.append(item)
        iCost.append(float(input(f"How much is {item}?")))
        print(f"{item} is added to the cart")
    elif ans ==2:
        for x in range(0,len(items)):
            print(f"{x}. {items[x]} - ${float}")
    elif ans ==3:
        num = input("Which item would you liek to remove?")
        item = items.pop(num)
        iCost.pop(num)
        print(f"{item} removed")
    elif ans==4:
        tot = 0
        for x in iCost:
            tot += x
        print(f"The total cost of the items in the cart is {tot}")
    elif ans ==5:
        break
    else:
        print("Invalid Input, try again")