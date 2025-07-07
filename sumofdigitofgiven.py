num=int(input(" enter numer :-"))

sum_of_digit=0
while num>0:
	digit=num%10
	sum_of_digit+=digit
	num=num//10

print(" sum_of_digit:-",sum_of_digit)
