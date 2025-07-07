odd = int(input("Enter odd number you want to add up to: "))
sum = 0

if odd % 2 != 0:
    for i in range(1, odd + 1, 2):  # start from 1, step by 2 to get only odd numbers
        sum += i
    print("Sum of odd numbers up to", odd, "is =", sum)
else:
    print("You did not enter an odd number.")
