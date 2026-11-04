l1=list(map(int,input("enter list 1 elements seperated by spaces:").split()))
l2=list(map(int,input("enter list 2 elements seperated by spaces:").split()))
common=list(set(l1) & set(l2))
print("common elements:",common)
