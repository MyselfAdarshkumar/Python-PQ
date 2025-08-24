# Write a program using functions to find greatest of three number

def greatest_num(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(greatest_num(9,3,8))