# This program analyzes characters in text (uppercase, lowercase, digits)

name = str(input("Enter your name: -"))

# Count uppercase letters
u_count = 0
for i in range(len(name)): 
    if name[i].isupper():
         u_count += 1

# Count lowercase letters 
i_count = 0
for j in range(len(name)):
    if name[j].islower():
        i_count += 1

# Count digits
n_count = 0
for k in range(len(name)):
    if name[k].isdigit():
        n_count += 1

# Display results
print("Number of uppercase letters:", u_count)
print("Number of lowercase letters:", i_count)
print("Number of digits:", n_count)


# Code by Adarsh 👨‍💻