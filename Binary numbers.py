n=int(input("enter a number"))
if n==0:
    print(0)
else:
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n//=2
print("Binary=",binary)
