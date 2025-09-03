# Recursive function to calculate sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    elif n < 0:
        return "Not valid for negative numbers"
    else:
        return n + sum_natural(n - 1)

# Input from user
n = int(input("Enter your number: "))

# Call function
result = sum_natural(n)
print(f"Sum of first {n} natural numbers = {result}")
