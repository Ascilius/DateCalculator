import datetime as dt

# input dates
print("Inputting Date 1:")
year1 = int(input("Year: "))
month1 = int(input("Month: "))
day1 = int(input("Day: "))

date1 = dt.date(year1, month1, day1)
print("Date 1: " + str(date1) + "\n")

print("Inputting Date 2:")
year2 = int(input("Year: "))
month2 = int(input("Month: "))
day2 = int(input("Day: "))

date2 = dt.date(year2, month2, day2)
print("Date 2: " + str(date2) + "\n")

# calculate difference
diff = abs(date1 - date2)

# display results
print(str(diff.days) + " day(s) difference between " + str(date1) + " and " + str(date2) + "!")