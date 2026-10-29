l=list(map(int,input("Enter elements seperated by space").split()))    #we can't perform split() operation in list  
print(l)                                                    #that's why give gave split function in input method
largest=l[0]

for num in l:
    if num>largest:
        largest=num
print(largest)
