# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print("highest to lowest grade: ", grades)


# Task 2: Calculate the average grade and display it.

total = sum(grades)
grade_avg = total / len(grades)

print("The grade average is", grade_avg)


# Task 3: Replace any grade below 80 with the value Failed.

grades[7] = "Failed"
grades[8] = "Failed"
grades[9] = "Failed"
print("The grades below 80 fails:", grades)