inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

print("Total snowfall inches: ", sum(inches_snow.values()))
n = int(input("How many inches of snow fell on Thursday?"))
inches_snow.update({"Thusday":n})
print("Total snowfall inches: ", sum(inches_snow.values()))
print(inches_snow)