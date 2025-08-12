
s=input("enter your name: ")
p=""
n=0
for i in range (0,len(s)-2):   
    p = s[i:i+3]
    if p[0]!= p[1] and p[1] != p[2] and p[0]!=p[2]:
        n+=1

print (n)
