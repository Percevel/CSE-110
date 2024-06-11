import math
user_input = int(input("How many rows and columns is the table"))
range_table = user_input +1

spacing = int(math.log10((user_input*user_input))) + 1

for r in range(1, range_table):
    for c in range(1,range_table):
        number = c*r
        print(f"{number:{spacing}}", end=" ")
    print()
