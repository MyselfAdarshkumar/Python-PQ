name=str(input("Enter your name: -"))
s_count=0
# space count
for i in range(len(name)):
    if name[i].isspace():
        s_count+=1

#special character count
sp_count=0
for k in range(len(name)):
    if not name[k].isalnum() and not name[k].isspace():
        sp_count+=1

#display results
print("Number of spaces:", s_count)
print("Number of special characters:", sp_count)


# Code by Adarsh 👨‍💻         