# Write a program which finds out whether a given name is present in a list or not.

# variable and constant that are used
_list = {"adarsh", "ashish", "ankit", "ram", "radha"}
_name = input("Enter your name: ")

# condition for checking list and final result
if _name in _list:
    print("present")
else:
    print("not present")
