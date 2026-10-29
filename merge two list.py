l1=list(map(int,input("Enter elements for list 1 seperated by space:").split()))
l2=list(map(int,input("Enter elemets for list 2 sepeated by space:").split()))
merged=[]
for i in l1:
    merged.append(i)
for i in l2:
    merged.append(i)
print("Merged list:",merged)
