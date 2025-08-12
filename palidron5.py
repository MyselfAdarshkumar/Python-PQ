name = str(input("Enter your name: "))
n = len(name)
for i in range(n //2):
    if name[i]!=name[n-i-1]:
        print ( " name is not palindron ")
        break
    
