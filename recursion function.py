def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
z=fact(5)
print(z)
