n=int(input("enter your number"))
ok=[]
for i in range(n):
	name=input(f"enter your chr" ,i+1)
	ok.append(name)
final=''.join(ok)
print(final)
