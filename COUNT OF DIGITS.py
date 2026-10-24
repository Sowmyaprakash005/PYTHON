n=int(input("enter a number"))
c=0
if n==0:
    c=1
else:
    while n>0:  #n!=0
        c+=1
        n=n//10
print("count:",c)
