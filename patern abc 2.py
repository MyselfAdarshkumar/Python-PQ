n = int(input("enter"))

x = 65  # ASCII for 'A'
for i in range(1, n+1):
    for j in range(i):  # print current letter i times
        print(chr(x), end="")
    x += 1  # move to next letter
    print()  # next line

# code by Adarsh 😊
