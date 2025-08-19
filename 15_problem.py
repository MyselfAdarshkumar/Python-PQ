# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# create dict
d = {}

# take input
for i in range(0, 4):
    a = input("Enter your name     : ")
    b = input("Enter your language : ")
    d.update({a: b})

# final result
print(d)
