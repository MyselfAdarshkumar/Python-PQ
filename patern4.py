n = int(input("enter your number"))  
i = 1

while i <= n:  
    for j in range(1, n+1):  
        print(j," " ,end="")  # print number on same line
        if i == j:  # stop printing after reaching i
            break
    i += 1  # move to next row
    print()  # new line after each row

# code by Adarsh 😊
