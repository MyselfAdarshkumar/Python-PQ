n = int(input("enter your number"))

for i in range(1, n+1):
    for j in range(65, 65+i):  # print characters from 'A' up to i-th letter
        print(chr(j), end="")
    print()  # go to next line

# code by Adarsh 😊
