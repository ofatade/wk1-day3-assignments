# Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

print("Student with grade below 80 is:", students[2], grades[2], activities[2])

# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students.remove("Jane")

students_approved = students.copy()
print("student_approved =", students_approved)

# Task 3: Print the list students_approved

print(students_approved)