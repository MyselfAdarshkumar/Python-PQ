n = int(input("enter your number"))  # take user input for size

for i in range(1, n+1):  
    for j in range(1, n+1):  
        print(j, end="")  # print column number on same line
    print()  # move to next line after each row
