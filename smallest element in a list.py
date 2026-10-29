l=list(map(int,input("Enter elements seperated by space").split()))
print(l)
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print(smallest)
