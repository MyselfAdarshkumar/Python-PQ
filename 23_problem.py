# Write a program to calculate the factorial of a given number using for loop.

#variable and constant
num=int(input("enter your number : "))
factorial=1

#for loop
for i in range(1,num+1):
	factorial*=i

print(factorial)