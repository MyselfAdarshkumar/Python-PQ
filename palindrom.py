# This program checks if a word is palindrome (reads same forwards and backwards)

name = str(input("Enter your name: -"))
new_name = name[::-1]    # Reverse the input string

# Check if original equals reversed
if name == new_name:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

# Code by Adarsh 👨‍💻
