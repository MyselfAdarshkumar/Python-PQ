num = int(input("Enter your number: "))

for i in range(2, num):
    if num % i == 0:  # found a divisor, so number is not prime
        print("not prime")
        break  # exit early since no need to check further
else:
    print("prime")  # runs only if loop didn't break; means no divisors found