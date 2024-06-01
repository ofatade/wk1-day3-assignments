# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temp = temperatures[7:14]
print("Temperatures for the second week of the month are:", second_week_temp)

# Task 2: Extract all the temperatures above 100.

temps_abv_100 = temperatures[24:]
print("Temperatures above 100 are:", temps_abv_100)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.sort(reverse=True)

temps_5th_10day = temperatures[4:10]
print("The temperature from day 5-10 are:", temps_5th_10day)