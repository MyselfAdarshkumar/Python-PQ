# Program to accept marks of 6 students and display them sorted

marks = []  
number_of_student = int(input("Enter number of students: "))

# Taking input for marks
for i in range(1, number_of_student + 1):
    m1 = int(input(f"Enter marks of student {i}: "))
    marks.append(m1)

# Sort marks after collecting all inputs
marks.sort()

# Final result
print(f"Sorted marks of students: {marks}")

