# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

# create list
l = ["Harry", "Soham", "Sachin", "Rahul"]

# loop check
for name in l:
    if name.startswith("S"):
        print(f"hello {name}")
