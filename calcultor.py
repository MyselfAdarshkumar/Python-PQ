first = int (input (" Enter your first number: - "))
second =int (input("Enter your 2nd number: -"))
calculate  = str (input ( " what you want to perform ( + , - , * , % ) : -"))


if calculate == "+"  :
    print ( " Addation is :-")
    print(first+second)

elif calculate == "-"  :
    print ( " subtraction is :-")
    print(first-second)
elif calculate == "*"  :
    print ( " multiply is :-")
    print(first*second)
elif calculate == "%"  :
    print ( " remainder is :-")
    print(first%second)
else:
    print("wrong input") 





