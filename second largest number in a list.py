l=list(map(int,input("Enter elements seperated by space").split()))
w=list(set(l))  
w.sort()    
if len(w)<2:
    print("No second largest element")
else:
    print("Second largest element in the list is:",w[-2])
