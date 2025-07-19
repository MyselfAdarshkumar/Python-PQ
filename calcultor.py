# A simple calculator that adds, subtracts, multiplies and finds remainder

# Taking numbers from user
first = int(input(" Enter your first number: - "))      # Get the first number from the user
second = int(input("Enter your 2nd number: -"))         # Get the second number from the user

# Ask user which math operation they want to do
calculate = str(input(" what you want to perform ( + , - , * , % ) : -"))

# Check which operation user chose and show result
if calculate == "+":
    print(" Addation is :-")
    print(first + second)       # Add two numbers

elif calculate == "-":
    print(" subtraction is :-")
    print(first - second)       # Subtract second from first number

elif calculate == "*":
    print(" multiply is :-")
    print(first * second)       # Multiply two numbers

elif calculate == "%":
    print(" remainder is :-")
    print(first % second)       # Show remainder after division

else:
    print("wrong input")        # Show error if user types wrong operation

# Created by Adarsh 👨‍💻

