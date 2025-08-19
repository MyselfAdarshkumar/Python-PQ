#          A spam comment is defined as a text containing following keywords:
#         “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
#          to detect these spams.


text=input("Enter your text : ")

if 'Make a lot of money' in text:
	print( " spams")


elif 'subscribe this' in text:
	print( " spams")


elif 'buy now' in text:
	print( " spams")


else:

	 print("pass") 