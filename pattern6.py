num = int(input("enter your number"))
n = 1

for i in range(num, 0, -1):  # rows from num down to 1
    for j in range(i):        # print i numbers in each row
        print(n, " ", end="") # print number with space
        n += 1                # move to next number
    print()                   # new line

# code by Adarsh 😊
