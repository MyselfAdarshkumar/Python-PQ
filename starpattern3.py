num = int(input("enter your number :-"))

for i in range(1, num+1):
    for j in range(i):  # print spaces
        print(" ", end="")
    for k in range(i, num+1):  # print stars
        print("*", end="")
    print()  # next line

# code by Adarsh 😊
