l=list(map(int,input("Enter elements seperated by space").split()))    
print(l)                                                 
largest=l[0]

for num in l:
    if num>largest:
        largest=num
print(largest)
