#find the maximum number of consonants before the first vowel in a string
name = str(input("Enter your name: -"))

#intilize variables
v=("a,io,u,e,A,I,O,U,E")
m=0
c=0
#loopfor each character in the string
for i in range(len(name)):
    if name[i] in v:
        max=(m,c)# update max if a vowel is found
        c= 0
        continue
    else:
        c+=1
    max=(m,c)
print("The maximum number of consonants before the first vowel is:", max[1])