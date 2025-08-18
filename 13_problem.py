# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# create set
number = set()

# take input
for i in range(0, 8):
    s = int(input("Enter your number = "))
    number.add(s)

# final result
print(number)
