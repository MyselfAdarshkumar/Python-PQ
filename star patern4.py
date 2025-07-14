num = int(input("enter your number"))

for i in range(1, num+1):
    for j in range(num+1, i, -1):  # print decreasing stars
        print("*", end="")
    print()  # next line

# code by Adarsh 😊
