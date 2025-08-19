# Write a program to find whether a given username contains less than 10
# characters or not.

name=input("Enter your username ")

#string function
count=len(name)

#condition for checking result
if (count<10):
	print("less than 10 characters")

else:
	print ("More than 10 characters")
