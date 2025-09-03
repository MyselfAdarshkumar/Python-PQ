# Write a python function to remove a given word from a list and strip it at the same
#     time.


def word(w,n):
    new=[]
    for item in w:
        if not(item==n):
            new.append(item.strip(n))
    return new
    
w=["word","one","oke"]
print(word(w,"o"))
print(w)