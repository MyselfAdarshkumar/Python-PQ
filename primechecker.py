from math import sqrt


num=int(input(" enter your number "))

for i in range(2,int(sqrt(num))+1):
	if num%i==0:
		print( "not prime")
		break
else:
	print ("prime number")