x = int(input("enter start number"))
y = int(input("enter end number"))

for i in range(x, y+1):        # check numbers from x to y
	for z in range(2, i):       # try all divisors from 2 to i-1
		if i % z == 0:          # if divisible, not prime
			print(i, "not prime")
			break               # stop checking further
	else:                       # runs only if no break (prime)
		print(i, "prime")
if x>y:
	print (" not valid" )
	print("first number is always smaller")

# code by Adarsh 😊
