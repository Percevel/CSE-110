ul = []
var = -1
while var != 0:
    var = int(input("Enter number: "))
    if var != 0:
        ul.append(var)

sum = 0
for x in ul:
    sum += x
print(sum)

avg = sum/ len(ul)
print(avg)

biggest = 0
for x in ul:
    if x > biggest:
        biggest = x
print(biggest)

smallest = biggest
for x in ul:
    if x < smallest and x>=0:
        smallest = x
print(smallest)

ol = sorted(ul)
print(ol)