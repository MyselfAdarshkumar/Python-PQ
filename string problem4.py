name = str(input("enter your name: "))

# Initialize variables 
vowels = {'a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E'}  # Changed from string to set
m = 0  # total count
c = 0  # current consonant sequence length

for i in range(len(name)):
    if name[i] in vowels:  # Check if the character is a vowel
        m += c
        c = 0
    else:
        c += 1
m += c

print("Total number of consonant substrings:", m)