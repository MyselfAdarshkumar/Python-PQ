name =str(input("Enter your name: -"))
# Count spaces, uppercase letters, lowercase letters, digits, and special characters in a string
#intialize counts
s_count = 0
n_count = 0
spe_count = 0
u_count = 0
l_count = 0
#loop through each character in the string
for i in range(len(name)):
    if name[i].isspace():
        s_count += 1
    elif name[i].isalpha():
        if name[i].isupper():
            u_count += 1
        else:
            l_count += 1
    elif name[i].isdigit():
        n_count += 1
    else:
        spe_count += 1

# Display results
print("Number of spaces:-", s_count)
print("Number of uppercase letters:-", u_count)
print("Number of lowercase letters:-", l_count)
print("Number of digits:-", n_count)
print("Number of special characters:-", spe_count)