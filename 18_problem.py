# Write a program to find whether a given username contains less than 10
# characters or not.

# variables that are used
name = input("Enter your username: ")

# string length
count = len(name)

# check condition
if count < 10:
    print("less than 10 characters")
elif count == 10:
    print("exactly 10 characters")
else:
    print("more than 10 characters")
