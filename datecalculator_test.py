import datetime as dt

delta1 = dt.timedelta(
	days = 50,
	seconds = 27,
	microseconds = 10,
	milliseconds = 29000,
	minutes = 5,
	hours = 8,
	weeks = 2
	)

print(delta1)

delta2 = dt.timedelta(
	days = 25,
	seconds = 13,
	microseconds = 5,
	milliseconds = 14000,
	minutes = 2,
	hours = 4,
	weeks = 1
	)

print(delta2)

print(delta1 + delta2)
print(delta2 - delta1)