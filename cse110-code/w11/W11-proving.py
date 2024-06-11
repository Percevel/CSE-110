with open("w11/life-expectancy.csv") as fileL:
    dat_highest= []
    dat_lowest= []
    highest = 0
    lowest = 100
    skip = 1
    for dat in fileL:
        if skip ==1:
            skip = 0
            continue
        line = dat.strip()
        line = line.split(",")
        if float(line[3]) > highest:
            highest = float(line[3])
            dat_highest = line
        if float(line[3]) < lowest:
            lowest = float(line[3])
            dat_lowest = line
    print(f"{dat_highest[0]} during {dat_highest[2]} had the highest life expectency of {dat_highest[3]}.")
    print(f"{dat_lowest[0]} during {dat_lowest[2]} had the lowest life expectency of {dat_lowest[3]}.")
    year = int(input("What year do you want to know the average life expectancy for the world?"))
    skip = 1
    tot = 0
    x = 0

with open("w11/life-expectancy.csv") as fil:
    for da in fil:
        if skip ==1:
            skip = 0
            continue
        line = da.strip()
        line = line.split(",")
        if int(line[2]) == year:
            tot += float(line[3])
            x += 1
    print(f"the average life expectancy of the world during {year} was {tot/x:.2f}")