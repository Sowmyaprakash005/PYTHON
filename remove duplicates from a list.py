l=list(map(int,input("Enter elements seperated by space").split()))
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)
