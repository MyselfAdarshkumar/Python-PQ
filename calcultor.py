# Simple calculator script that performs basic arithmetic operations based on user input

first = int(input(" Enter your first number: - "))      # Get the first number from the user
second = int(input("Enter your 2nd number: -"))         # Get the second number from the user
calculate = str(input(" what you want to perform ( + , - , * , % ) : -"))  # Get the operation

if calculate == "+":
    print(" Addation is :-")
    print(first + second)       # Perform addition

elif calculate == "-":
    print(" subtraction is :-")
    print(first - second)       # Perform subtraction

elif calculate == "*":
    print(" multiply is :-")
    print(first * second)       # Perform multiplication

elif calculate == "%":
    print(" remainder is :-")
    print(first % second)       # Perform modulo operation

else:
    print("wrong input")        # Handle invalid operation input

