# Write a program to detect double space in a string

# Take input from the user
name = input("Enter your name: ")

# Check if the string contains two consecutive spaces
if "  " in name:
    print("Double space detected")  
    new_name=name.replace("  "," ") 
    print (new_name)
else:
    print("All OK")                   
