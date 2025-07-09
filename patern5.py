num = int(input("enter number:-"))  # input for rows
i = 1
n = 1  # starting number

while i <= num:
    j = 1
    while j < i:
        print(n, end="")  # print current number
        j += 1
        n += 1  # move to next number
    i += 1
    print()  # new line after each row

# code by Adarsh 😊
